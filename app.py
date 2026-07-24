#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mushroom Search Index - backend server.

Zero-dependency: uses only the Python standard library so it runs anywhere
`python app.py` works (Python 3.7+). Serves a small JSON search API plus the
static frontend.

API
---
GET /api/species            list/search species (query params below)
GET /api/species/<id>       full record for one species
GET /api/facets             available filter values (for building the UI)
GET /                      frontend (index.html)

Query params for /api/species (all optional, combined with AND):
    q            free text  -> matches name, scientific_name, aliases, description
    edibility    one of: deadly, poisonous, inedible, unknown, edible, choice
    habitat      forest | grassland | cultivated
    substrate     ground | deadwood | dung | compost
    ecology      mycorrhizal | saprotrophic | parasitic
    spore_print  e.g. white, brown, green, ... (exact-ish match)
    cap_color    e.g. red, brown, ... (matches any cap color)
    gill_attachment  free | attached | decurrent | pores | n/a
    season       spring | summer | autumn | winter
    sort         name | edibility | random
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from functools import partial

# Make the data package importable regardless of where the server is launched.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data.species import SPECIES  # noqa: E402

# Optional image manifest (written by fetch_images.py). Maps species id ->
# {file, credit, license, source, taxon_id, matched_name}.
def _load_manifest():
    path = os.path.join(HERE, "images", "manifest.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except OSError:
        return {}

MANIFEST = _load_manifest()

# --- Lookalike resolver -------------------------------------------------
# Lookalikes are stored as free-text {name, distinguish} with no id link.
# Resolve each to a species id when the named organism is in our dataset so
# the frontend can make the lookalike clickable.
import re as _re

def _slug(s):
    """Lowercase and squash non-alphanumerics to single spaces. Parenthetical
    text is KEPT (separated by spaces) so common names in lookalike labels like
    "Omphalotus (jack-o'-lantern)" or "Cantharellus (chanterelle)" still match
    our aliases ("jack o lantern", "chanterelle") instead of being discarded."""
    s = s.lower().replace('(', ' ').replace(')', ' ')
    return _re.sub(r'[^a-z0-9]+', ' ', s).strip()

# normalized term -> species id (first definition wins)
_LOOKUP = {}
for _s in SPECIES:
    for _t in [_s['name'], _s['scientific_name']] + list(_s.get('aliases', [])):
        _LOOKUP.setdefault(_slug(_t), _s['id'])

def _resolve_lookalike(name):
    """Return a species id if `name` clearly refers to a species we have."""
    n = _slug(name)
    if not n:
        return None
    # Exact (slug-collapsed) match on a real name / alias / scientific name.
    if n in _LOOKUP:
        return _LOOKUP[n]
    # Substring match on any real term (e.g. the parenthetical common name
    # "(chanterelle)" or "jack-o'-lantern"), whole-word bounded to avoid
    # partial collisions like "jack" matching something unrelated.
    for cand, sid in _LOOKUP.items():
        if _re.search(r'\b' + _re.escape(cand) + r'\b', n):
            return sid
    return None


def with_image(s):
    """Return a copy of the species record with an `image` field attached when
    a downloaded photo exists."""
    rec = dict(s)
    meta = MANIFEST.get(s["id"])
    if meta:
        rec["image"] = {
            "url": "/images/" + meta["file"],
            "credit": meta.get("credit"),
            "license": meta.get("license"),
            "source": meta.get("source", "iNaturalist"),
        }
    # Make lookalikes clickable when they resolve to a species in the index.
    lookalikes = s.get("lookalikes")
    if lookalikes:
        rec["lookalikes"] = [
            dict(la, link=_resolve_lookalike(la["name"])) for la in lookalikes
        ]
    return rec

# Vocabulary used for sorting edibility from safest to most dangerous.
EDIBILITY_ORDER = {
    "choice": 0, "edible": 1, "unknown": 2, "inedible": 3,
    "poisonous": 4, "deadly": 5,
}

# Human-friendly labels for edibility badges.
EDIBILITY_LABELS = {
    "choice": "Choice edible",
    "edible": "Edible",
    "unknown": "Unknown",
    "inedible": "Inedible",
    "poisonous": "Poisonous",
    "deadly": "Deadly",
}


def _matches_filters(s, params):
    # `params` carries single string values from the query (or is {}). A key
    # absent -> None -> means "no filter on this field".

    def eq(key, species_val):
        # True when there's no filter on `key`, or the filter matches the
        # species value.
        f = params.get(key)
        return f is None or f == species_val

    def has_value(key, values):
        # `values` is a list from the species record; the filter value is a
        # single string. Absent filter (None) matches everything.
        v = params.get(key)
        return v is None or v in values

    # Text search across name / scientific / aliases / description.
    q = params.get("q")
    if q:
        q = q.lower()
        haystack = " ".join([
            s["name"], s["scientific_name"],
            " ".join(s.get("aliases", [])),
            s.get("description", ""),
        ]).lower()
        if q not in haystack:
            return False

    if not eq("edibility", s.get("edibility")):
        return False
    if not eq("habitat", s.get("habitat")):
        return False
    if not eq("substrate", s.get("substrate")):
        return False
    if not eq("ecology", s.get("ecology")):
        return False
    if not eq("spore_print", s.get("spore_print")):
        return False
    if not eq("season", s.get("season")):
        return False

    # Cap color: species stores a list of colors.
    cap_colors = s.get("cap", {}).get("colors", [])
    if not has_value("cap_color", cap_colors):
        return False

    # Gill attachment.
    gill = s.get("gills", {}).get("attachment")
    g_att = params.get("gill_attachment")
    if g_att and gill != g_att:
        return False

    return True


def build_facets():
    """Derive the set of selectable filter values from the dataset."""
    def collect(key, fn):
        out = set()
        for s in SPECIES:
            out.update(fn(s))
        return sorted(out)

    facets = {
        "edibility": [{"value": k, "label": EDIBILITY_LABELS[k]} for k in EDIBILITY_ORDER],
        "habitat": collect("habitat", lambda s: [s.get("habitat")] if s.get("habitat") else []),
        "substrate": collect("substrate", lambda s: [s.get("substrate")] if s.get("substrate") else []),
        "ecology": collect("ecology", lambda s: [s.get("ecology")] if s.get("ecology") else []),
        "spore_print": collect("spore_print", lambda s: [s.get("spore_print")] if s.get("spore_print") else []),
        "cap_color": collect("cap_color", lambda s: s.get("cap", {}).get("colors", [])),
        "gill_attachment": collect("gill", lambda s: [s.get("gills", {}).get("attachment")] if s.get("gills", {}).get("attachment") else []),
        "season": sorted({se for s in SPECIES for se in s.get("season", [])}),
    }
    return facets


FACETS = build_facets()


def search(params):
    results = [s for s in SPECIES if _matches_filters(s, params)]
    sort = params.get("sort", "name")
    if sort == "edibility":
        results.sort(key=lambda s: EDIBILITY_ORDER.get(s.get("edibility"), 9))
    elif sort == "random":
        import random
        random.shuffle(results)
    else:  # name
        results.sort(key=lambda s: s["name"].lower())
    return results


class Handler(BaseHTTPRequestHandler):
    server_version = "MushroomIndex/1.0"

    def _send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path):
        try:
            with open(path, "rb") as f:
                body = f.read()
        except OSError:
            self.send_error(404, "Not found")
            return
        ext = os.path.splitext(path)[1]
        ctype = {
            ".html": "text/html; charset=utf-8",
            ".js": "application/javascript; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".svg": "image/svg+xml",
            ".ico": "image/x-icon",
            ".gif": "image/gif",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp",
            ".json": "application/json; charset=utf-8",
        }.get(ext, "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        route = parsed.path
        params = {k: v[0] for k, v in parse_qs(parsed.query).items()}

        if route == "/api/facets":
            return self._send_json(FACETS)

        if route == "/api/species":
            return self._send_json([with_image(s) for s in search(params)])

        if route.startswith("/api/species/"):
            sid = route[len("/api/species/"):]
            match = next((s for s in SPECIES if s["id"] == sid), None)
            if match:
                return self._send_json(with_image(match))
            return self._send_json({"error": "not found"}, status=404)

        # Static files -- served from a strict whitelist so we never leak
        # source (app.py, data/*.py) or allow traversal. Images are served
        # from the images/ directory by id.
        STATIC_WHITELIST = {
            "/": "index.html",
            "/index.html": "index.html",
            "/styles.css": "styles.css",
            "/app.js": "app.js",
            "/favicon.ico": "favicon.svg",
            "/favicon.svg": "favicon.svg",
            "/bg.gif": "bg.gif",
        }
        if route in STATIC_WHITELIST:
            return self._send_file(os.path.join(HERE, STATIC_WHITELIST[route]))

        if route.startswith("/images/") and route.endswith(".jpg"):
            fname = os.path.basename(route)  # safe: strips any path
            candidate = os.path.join(HERE, "images", fname)
            if candidate.startswith(os.path.join(HERE, "images")) and os.path.isfile(candidate):
                return self._send_file(candidate)

        self.send_error(404, "Not found")

    def log_message(self, fmt, *args):  # quieter logs
        sys.stderr.write("[mushroom-index] " + (fmt % args) + "\n")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Mushroom Search Index server")
    parser.add_argument("--host", default=os.environ.get("HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int,
                        default=int(os.environ.get("PORT", "8000")))
    args = parser.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    url = f"http://{args.host}:{args.port}/"
    print(f"Mushroom Search Index running at {url}")
    print(f"Serving {len(SPECIES)} species. Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        httpd.shutdown()


if __name__ == "__main__":
    main()
