#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spore Drop Index - backend server.

Zero-dependency: uses only the Python standard library so it runs anywhere
`python app.py` works (Python 3.7+). Serves a small JSON search API plus the
static frontend.

API
---
GET /api/species            list/search species (query params below)
GET /api/species/<id>       full record for one species
GET /api/facets             available filter values (for building the UI)
GET /api/lookalike-pairs    dangerous cross-species lookalike pairs (safety mode)
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
    potency      low | moderate | high (psychoactive species only)
    regions      north-america | europe | asia | south-america | africa |
                 oceania | global (matches ANY of comma-separated values)
    bioluminescent  true | yes | 1  (species tagged as glow / foxfire fungi)
    host_trees   oak | pine | birch | ... (mycorrhizal host trees; ANY of
                 comma-separated values). Educational associations only.
    sort         name | edibility | random
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from functools import partial
from PIL import Image, ImageFilter

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

# --- AI-assisted identify via Gemini (optional, falls back to local) --------
# If GEMINI_API_KEY is set (Railway env var, never committed), we ask a real
# vision model to pick the closest matches from OUR dataset only -- it is
# given the species list and told to answer strictly from it, so it can't
# invent a species we don't carry. On any failure (no key, network error,
# bad response, rate limit) we fall back to the local visual-similarity
# matcher below so /api/identify never hard-fails.
import base64 as _base64
import urllib.request as _urlreq
import urllib.error as _urlerr

_GEMINI_MODEL = "gemini-3.1-flash-lite"
_GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    + _GEMINI_MODEL + ":generateContent"
)


def _gemini_api_key():
    return os.environ.get("GEMINI_API_KEY", "").strip()


def _gemini_species_catalog():
    """Compact 'id | common name | scientific name' catalog the model must
    choose from, so it can only return species we actually have."""
    return "\n".join(
        "%s | %s | %s" % (s["id"], s["name"], s["scientific_name"]) for s in SPECIES
    )


def identify_by_photo_ai(upload_path, top_n=5, timeout=20):
    """Ask Gemini to rank the closest matches from our species catalog.
    Returns a list of dicts (id/name/scientific_name/edibility/confidence/
    reasoning) or raises on any failure -- caller falls back to the local
    matcher.
    """
    api_key = _gemini_api_key()
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")

    with open(upload_path, "rb") as f:
        img_b64 = _base64.b64encode(f.read()).decode("ascii")

    prompt = (
        "You are assisting an EDUCATIONAL mushroom reference app. You are NOT "
        "identifying this mushroom for consumption safety -- never claim certainty "
        "and never suggest it is safe to eat. Below is a catalog of species IDs "
        "this app has entries for, one per line as 'id | common name | scientific "
        "name'. Look at the uploaded photo and pick up to " + str(top_n) + " species "
        "FROM THIS CATALOG ONLY that are the closest visual matches (cap shape/color, "
        "gills/pores, stem, habitat cues visible in the photo). Do not invent a "
        "species that is not in the catalog. If nothing in the catalog is a "
        "plausible match, return an empty list.\n\n"
        "Respond with ONLY compact JSON (no markdown fences, no prose) in this "
        "exact shape:\n"
        '{"matches": [{"id": "<catalog id>", "confidence": <0.0-1.0>, '
        '"reasoning": "<one short phrase, visible traits only>"}]}\n\n'
        "Catalog:\n" + _gemini_species_catalog()
    )

    body = json.dumps({
        "contents": [{
            "parts": [
                {"text": prompt},
                {"inline_data": {"mime_type": "image/jpeg", "data": img_b64}},
            ]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "responseMimeType": "application/json",
        },
    }).encode("utf-8")

    req = _urlreq.Request(
        _GEMINI_URL + "?key=" + api_key,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with _urlreq.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except _urlerr.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:500]
        raise RuntimeError("Gemini HTTP %s: %s" % (e.code, detail))

    try:
        text = payload["candidates"][0]["content"]["parts"][0]["text"]
        parsed = json.loads(text)
        raw_matches = parsed.get("matches", [])
    except (KeyError, IndexError, ValueError) as e:
        raise RuntimeError("Unexpected Gemini response shape: %s" % e)

    by_id = {s["id"]: s for s in SPECIES}
    out = []
    for m in raw_matches[:top_n]:
        sid = m.get("id")
        s = by_id.get(sid)
        if not s:
            continue  # ignore any id Gemini hallucinated outside the catalog
        rec = {
            "id": s["id"],
            "name": s["name"],
            "scientific_name": s["scientific_name"],
            "edibility": s.get("edibility"),
            "confidence": round(float(m.get("confidence", 0)), 3),
            "reasoning": str(m.get("reasoning", ""))[:200],
        }
        img = with_image(s).get("image")
        if img:
            rec["image"] = img
        out.append(rec)
    return out


# --- Photo-based "visual similarity" matcher (local, no external API) -------
# Cheap, dependency-free features (Pillow only): an HSV colour histogram plus
# an edge-density measure. This is NOT identification -- it ranks our indexed
# photos by how much they look like the uploaded one. The UI is required to
# present results as "visually similar", never "this is species X".
import math as _math

def _photo_features(img):
    """Return {hsv: [768 ints], edge: float} for a PIL image."""
    small = img.convert("RGB").resize((64, 64))
    hsv = small.convert("HSV").histogram()  # 256*3 bins
    edge = small.convert("L").filter(ImageFilter.FIND_EDGES).histogram()
    edge_density = sum(i * c for i, c in enumerate(edge)) / float(64 * 64 * 255)
    return {"hsv": hsv, "edge": edge_density}

def _features_from_file(path):
    with open(path, "rb") as f:
        return _photo_features(Image.open(f))

def _dist(a, b):
    """Lower = more visually similar. Combines HSV histogram distance
    (chi-square) with edge-density difference."""
    ha, hb = a["hsv"], b["hsv"]
    chi = 0.0
    for x, y in zip(ha, hb):
        s = x + y
        if s:
            chi += (x - y) ** 2 / s
    chi *= 0.5  # normalise to ~[0, 1]
    edge_diff = abs(a["edge"] - b["edge"])
    return 0.85 * chi + 0.15 * min(edge_diff, 1.0)

# Precompute features for every indexed photo so an upload ranks in O(n).
_PHOTO_FEATURES = {}
for _sid, _meta in MANIFEST.items():
    _p = os.path.join(HERE, "images", _meta.get("file", ""))
    if _p and os.path.isfile(_p):
        try:
            _PHOTO_FEATURES[_sid] = _features_from_file(_p)
        except Exception:
            pass

def identify_by_photo(upload_path, top_n=8):
    """Rank indexed species by visual similarity to an uploaded photo.
    Returns a list of dicts with id/name/edibility/similarity, best first."""
    q = _features_from_file(upload_path)
    scored = []
    for s in SPECIES:
        f = _PHOTO_FEATURES.get(s["id"])
        if not f:
            continue
        scored.append((_dist(q, f), s))
    if not scored:
        return []
    scored.sort(key=lambda t: t[0])
    lo = scored[0][0]
    hi = max(t[0] for t in scored)
    span = (hi - lo) or 1.0
    out = []
    for d, s in scored[:top_n]:
        sim = 1.0 - (d - lo) / span  # 1.0 = closest match
        rec = {
            "id": s["id"],
            "name": s["name"],
            "scientific_name": s["scientific_name"],
            "edibility": s.get("edibility"),
            "similarity": round(sim, 3),
        }
        img = with_image(s).get("image")
        if img:
            rec["image"] = img
        out.append(rec)
    return out


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


def _esc_html(s):
    """Minimal HTML-attribute-safe escaping for server-side meta tag
    injection (no templating engine dependency)."""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

# normalized term -> species id (first definition wins)
_LOOKUP = {}
for _s in SPECIES:
    for _t in [_s['name'], _s['scientific_name']] + list(_s.get('aliases', [])):
        _LOOKUP.setdefault(_slug(_t), _s['id'])

# Canonical genus -> species id, used only when a lookalike names a genus we
# have exactly one (or one canonical) species of. Keeps "Psilocybe species",
# "Verpa species", "Young puffballs (Calvatia)", etc. clickable without
# hand-editing every lookalike entry.
_GENUS_MAP = {
    "psilocybe": "psilocybe-cubensis",
    "verpa": "verpa-bohemica",
    "calvatia": "calvatia-gigantea",
    "galerina": "galerina-marginata",
    "morchella": "morchella-esculenta",  # canonical edible morel
}


def _resolve_lookalike(name, source_id=None):
    """Return a species id if `name` clearly refers to a species we have.

    Resolution order: exact slug -> whole-word term match -> a specific
    indexed organism named inside the label -> genus-level fallback.
    `source_id` is excluded so a species never links to itself.
    """
    n = _slug(name)
    if not n:
        return None
    # 1) Exact (slug-collapsed) match on a real name / alias / scientific name.
    if n in _LOOKUP:
        return _LOOKUP[n]
    # 2) Whole-word substring on any lookup term (parenthetical common names,
    #    e.g. "(chanterelle)" or "jack-o'-lantern").
    for cand, sid in _LOOKUP.items():
        if sid != source_id and _re.search(r'\b' + _re.escape(cand) + r'\b', n):
            return sid
    # 3) The label names a specific indexed organism as a phrase
    #    ("Galerina marginata (deadly galerina)", "Agaricus campestris
    #    (field mushroom)", ...). Link to the longest matching term.
    best = None
    best_len = 0
    for sp in SPECIES:
        sid = sp["id"]
        if sid == source_id:
            continue
        for term in [sp["name"], sp["scientific_name"]] + list(sp.get("aliases", [])):
            t = _slug(term)
            if len(t) < 4:
                continue
            if _re.search(r'\b' + _re.escape(t) + r'\b', n) and len(t) > best_len:
                best = sid
                best_len = len(t)
    if best:
        return best
    # 4) Genus-level fallback for single/canonical-species genera.
    for genus, sid in _GENUS_MAP.items():
        if sid != source_id and _re.search(r'\b' + _re.escape(genus) + r'\b', n):
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
            dict(la, link=_resolve_lookalike(la["name"], s["id"])) for la in lookalikes
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

# Vocabulary + labels for the psychoactive potency tier (subset of species).
POTENCY_ORDER = {"low": 0, "moderate": 1, "high": 2}
POTENCY_LABELS = {
    "low": "Low potency",
    "moderate": "Moderate potency",
    "high": "High potency",
}

# Controlled vocabulary + labels for the structured region filter.
REGION_LABELS = {
    "north-america": "North America",
    "europe": "Europe",
    "asia": "Asia",
    "south-america": "South America",
    "africa": "Africa",
    "oceania": "Oceania",
    "global": "Global / widespread",
}

# Boolean-ish trait facet: glow / foxfire fungi (curated tag on a subset).
BIOLUM_LABELS = {
    "true": "Bioluminescent only",
}

# Mycorrhizal host-tree associations (educational; not exclusive occurrence).
# Order controls facet chip ordering in the sidebar.
HOST_TREE_LABELS = {
    "oak": "Oak",
    "pine": "Pine",
    "birch": "Birch",
    "beech": "Beech",
    "fir": "Fir",
    "spruce": "Spruce",
    "hemlock": "Hemlock",
    "aspen": "Aspen",
    "poplar": "Poplar",
    "willow": "Willow",
    "hazel": "Hazel",
    "chestnut": "Chestnut",
    "larch": "Larch",
    "cedar": "Cedar",
    "maple": "Maple",
    "alder": "Alder",
    "hickory": "Hickory",
    "douglas-fir": "Douglas-fir",
    "tanoak": "Tanoak",
    "madrone": "Madrone",
    "eucalyptus": "Eucalyptus",
    "hardwoods": "Hardwoods (mixed)",
    "conifers": "Conifers (mixed)",
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
        host_labels = [
            HOST_TREE_LABELS.get(t, t) for t in s.get("host_trees", [])
        ]
        haystack = " ".join([
            s["name"], s["scientific_name"],
            " ".join(s.get("aliases", [])),
            s.get("description", ""),
            " ".join(s.get("host_trees", [])),
            " ".join(host_labels),
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
    # Season: species stores a list of seasons it fruits in; the filter is a
    # single value that must appear in that list (bug fix -- this used to be
    # an exact `eq` against the whole list, which could never match).
    if not has_value("season", s.get("season", [])):
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

    # Potency (psychoactive species only -- exact match, like edibility).
    if not eq("potency", s.get("potency")):
        return False

    # Regions: species stores a list; query param may be comma-separated
    # (array-style, like cap_color) -- matches if ANY requested region is
    # present on the species.
    regions_param = params.get("regions")
    if regions_param:
        requested = {r.strip() for r in regions_param.split(",") if r.strip()}
        species_regions = set(s.get("regions", []))
        if not (requested & species_regions):
            return False

    # Bioluminescent: only filter when the client asks for glow species.
    # Accept true/yes/1; anything else is ignored (no "false-only" mode).
    biolum = params.get("bioluminescent")
    if biolum is not None:
        want = str(biolum).strip().lower() in {"1", "true", "yes", "y", "on"}
        if want and not s.get("bioluminescent"):
            return False

    # Host trees: mycorrhizal associations stored as a list; query may be
    # comma-separated (OR match), same contract as regions.
    host_param = params.get("host_trees")
    if host_param:
        requested = {r.strip() for r in host_param.split(",") if r.strip()}
        species_hosts = set(s.get("host_trees", []))
        if not (requested & species_hosts):
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
        "potency": [{"value": k, "label": POTENCY_LABELS[k]} for k in POTENCY_ORDER
                    if any(s.get("potency") == k for s in SPECIES)],
        "regions": [{"value": k, "label": REGION_LABELS[k]} for k in REGION_LABELS
                    if any(k in s.get("regions", []) for s in SPECIES)],
        "bioluminescent": (
            [{"value": "true", "label": BIOLUM_LABELS["true"]}]
            if any(s.get("bioluminescent") for s in SPECIES)
            else []
        ),
        "host_trees": [
            {"value": k, "label": HOST_TREE_LABELS[k]}
            for k in HOST_TREE_LABELS
            if any(k in s.get("host_trees", []) for s in SPECIES)
        ],
    }
    return facets


FACETS = build_facets()


# --- Dangerous lookalike pairs -------------------------------------------
# Walks every species' resolved lookalikes (see _resolve_lookalike above) and
# surfaces cross-species pairs where the safety stakes are real: the two
# species have different edibility and at least one side is poisonous/deadly.
# Pairs where both sides are in the "safe-ish" tier (edible/choice) are not
# the safety-relevant case and are skipped, as are same-edibility pairs.
_DANGEROUS_TIERS = {"poisonous", "deadly"}


def _lookalike_brief(sp):
    rec = {
        "id": sp["id"],
        "name": sp["name"],
        "scientific_name": sp["scientific_name"],
        "edibility": sp.get("edibility"),
    }
    img = with_image(sp).get("image")
    if img:
        rec["image"] = img
    return rec


def build_lookalike_pairs():
    by_id = {s["id"]: s for s in SPECIES}
    seen = set()  # unordered {id, id} pairs already emitted
    pairs = []
    for s in SPECIES:
        for la in s.get("lookalikes", []) or []:
            link = _resolve_lookalike(la["name"], s["id"])
            other = by_id.get(link)
            if not other:
                continue
            a_ed, b_ed = s.get("edibility"), other.get("edibility")
            if a_ed == b_ed:
                continue  # not a cross-tier confusion
            if not (a_ed in _DANGEROUS_TIERS or b_ed in _DANGEROUS_TIERS):
                continue  # e.g. edible vs choice -- not the safety-relevant case
            key = frozenset((s["id"], other["id"]))
            if key in seen:
                continue
            seen.add(key)
            pairs.append({
                "a": _lookalike_brief(s),
                "b": _lookalike_brief(other),
                "distinguish": la.get("distinguish", ""),
            })
    # Most dangerous first (deadly involved, then poisonous), then by name.
    def rank(p):
        eds = {p["a"]["edibility"], p["b"]["edibility"]}
        return (0 if "deadly" in eds else 1, p["a"]["name"])
    pairs.sort(key=rank)
    return pairs


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
    server_version = "SporeDropIndex/1.0"

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
        # Keep HTML/JS/CSS fresh behind Cloudflare. Images can stay longer.
        if ext in (".html", ".js", ".css", ".svg"):
            self.send_header("Cache-Control", "public, max-age=120, must-revalidate")
        elif ext in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
            self.send_header("Cache-Control", "public, max-age=86400")
        self.end_headers()
        self.wfile.write(body)

    def _origin(self):
        """Best-effort absolute origin for building og:image/og:url. Prefers
        the Host header (works behind Railway's proxy) over host/port."""
        host = self.headers.get("Host")
        if not host:
            host = "%s:%s" % self.server.server_address[:2]
        scheme = "https" if os.environ.get("RAILWAY_ENVIRONMENT") else "http"
        return "%s://%s" % (scheme, host)

    def _send_species_page(self, species):
        """Serve index.html with per-species <title>/meta tags swapped in via
        plain string replacement (no templating engine). The SPA's own JS/CSS
        is untouched, so app.js boots normally and opens this species'
        detail view (see app.js's DEEPLINK_SPECIES_ID / init())."""
        try:
            with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
                html = f.read()
        except OSError:
            self.send_error(404, "Not found")
            return

        name = species.get("name", "")
        sci = species.get("scientific_name", "")
        desc = species.get("description", "") or ""
        # Keep the meta description short and punchy.
        short_desc = (desc[:197] + "...") if len(desc) > 200 else desc
        title = "%s (%s) — The Spore Drop" % (name, sci) if sci else "%s — The Spore Drop" % name

        origin = self._origin()
        img_url = origin + "/images/" + species["id"] + ".jpg"
        page_url = origin + "/species/" + species["id"]

        html = _re.sub(r"<title>.*?</title>", "<title>%s</title>" % _esc_html(title), html, count=1, flags=_re.S)

        # Replace/insert each meta tag. If the tag already exists (matched by
        # its name/property attribute), swap its content; otherwise inject it
        # right before </head>.
        def upsert_meta(html, attr, attr_value, content):
            pattern = _re.compile(
                r'<meta\s+%s="%s"[^>]*>' % (attr, _re.escape(attr_value)), _re.IGNORECASE
            )
            tag = '<meta %s="%s" content="%s" />' % (attr, attr_value, _esc_html(content))
            if pattern.search(html):
                return pattern.sub(tag, html, count=1)
            return html.replace("</head>", "  " + tag + "\n</head>", 1)

        html = upsert_meta(html, "name", "description", short_desc)
        html = upsert_meta(html, "property", "og:title", title)
        html = upsert_meta(html, "property", "og:description", short_desc)
        html = upsert_meta(html, "property", "og:image", img_url)
        html = upsert_meta(html, "property", "og:url", page_url)
        html = upsert_meta(html, "property", "og:type", "article")
        html = upsert_meta(html, "name", "twitter:card", "summary_large_image")

        # Hand the species id to the frontend so app.js's init() opens that
        # species' detail modal on load (see DEEPLINK_SPECIES_ID in app.js).
        boot_script = (
            '<script>window.__DEEPLINK_SPECIES_ID = %s;</script>\n'
            % json.dumps(species["id"])
        )
        html = html.replace("</head>", "  " + boot_script + "</head>", 1)

        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=60, must-revalidate")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        route = parsed.path
        params = {k: v[0] for k, v in parse_qs(parsed.query).items()}

        if route == "/api/facets":
            return self._send_json(FACETS)

        if route == "/api/lookalike-pairs":
            return self._send_json(build_lookalike_pairs())

        if route == "/api/species":
            return self._send_json([with_image(s) for s in search(params)])

        if route.startswith("/api/species/"):
            sid = route[len("/api/species/"):]
            match = next((s for s in SPECIES if s["id"] == sid), None)
            if match:
                return self._send_json(with_image(match))
            return self._send_json({"error": "not found"}, status=404)

        # Per-species permalink: same SPA shell (index.html) with server-side
        # rewritten <title>/meta tags so link previews (Twitter/X, Discord,
        # etc.) show that species' real name/description/photo instead of
        # the generic site-wide OG tags. Does not collide with the JSON API
        # above (that's /api/species/<id>; this is /species/<id>).
        if route.startswith("/species/"):
            sid = route[len("/species/"):]
            match = next((s for s in SPECIES if s["id"] == sid), None)
            if not match:
                self.send_error(404, "Species not found")
                return
            return self._send_species_page(match)

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
        }
        if route in STATIC_WHITELIST:
            return self._send_file(os.path.join(HERE, STATIC_WHITELIST[route]))

        if route.startswith("/images/") and route.endswith(".jpg"):
            fname = os.path.basename(route)  # safe: strips any path
            candidate = os.path.join(HERE, "images", fname)
            if candidate.startswith(os.path.join(HERE, "images")) and os.path.isfile(candidate):
                return self._send_file(candidate)

        self.send_error(404, "Not found")

    def do_POST(self):
        parsed = urlparse(self.path)
        route = parsed.path
        if route != "/api/identify":
            return self.send_error(404, "Not found")
        try:
            ctype = self.headers.get("Content-Type", "")
            if "multipart/form-data" not in ctype:
                return self.send_error(400, "Expected multipart/form-data")
            # Boundary looks like: boundary=----WebKitFormBoundaryXXXX
            boundary = None
            for part in ctype.split(";"):
                part = part.strip()
                if part.startswith("boundary="):
                    boundary = part[len("boundary="):].strip().strip('"')
            if not boundary:
                return self.send_error(400, "Missing multipart boundary")
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                return self.send_error(400, "Bad Content-Length")
            raw = self.rfile.read(length)
            # Split into parts on \r\n--<boundary>
            delim = ("--" + boundary).encode("utf-8")
            parts = raw.split(b"\r\n" + delim)
            image_bytes = None
            for p in parts:
                if not p or p == b"--\r\n" or p == b"--":
                    continue
                # Each part: headers \r\n\r\n body, with a leading \r\n we strip.
                if p.startswith(b"\r\n"):
                    p = p[2:]
                sep = b"\r\n\r\n"
                idx = p.find(sep)
                if idx < 0:
                    continue
                header_block = p[:idx].decode("utf-8", "replace")
                body = p[idx + len(sep):]
                # Drop trailing \r\n that belongs to the boundary delimiter.
                if body.endswith(b"\r\n"):
                    body = body[:-2]
                if 'name="image"' in header_block and body:
                    image_bytes = body
                    break
            if not image_bytes:
                return self.send_error(400, "No image uploaded")
            # Stash to a temp file and run the local similarity matcher.
            import tempfile
            fd, tmppath = tempfile.mkstemp(suffix=".jpg", prefix="id_")
            with os.fdopen(fd, "wb") as fh:
                fh.write(image_bytes)
            try:
                from PIL import UnidentifiedImageError
                try:
                    Image.open(tmppath).verify()
                except (UnidentifiedImageError, OSError):
                    os.remove(tmppath)
                    return self.send_error(400, "File is not a valid image")
                method = "local"
                try:
                    results = identify_by_photo_ai(tmppath, top_n=5)
                    method = "ai"
                    if not results:
                        # Empty AI result (no plausible catalog match) --
                        # still useful to fall back to visual similarity
                        # rather than showing nothing.
                        results = identify_by_photo(tmppath, top_n=8)
                        method = "local"
                except Exception as ai_err:  # noqa: BLE001
                    sys.stderr.write(
                        "[mushroom-index] Gemini identify unavailable, "
                        "falling back to local matcher: %s\n" % ai_err
                    )
                    results = identify_by_photo(tmppath, top_n=8)
            finally:
                if os.path.exists(tmppath):
                    os.remove(tmppath)
            self._send_json({"results": results, "method": method})
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("[mushroom-index] identify error: %s\n" % e)
            self.send_error(500, "Identification failed")

    def log_message(self, fmt, *args):  # quieter logs
        sys.stderr.write("[mushroom-index] " + (fmt % args) + "\n")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Spore Drop Index server")
    parser.add_argument("--host", default=os.environ.get("HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int,
                        default=int(os.environ.get("PORT", "8000")))
    args = parser.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    url = f"http://{args.host}:{args.port}/"
    print(f"Spore Drop Index running at {url}")
    print(f"Serving {len(SPECIES)} species. Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        httpd.shutdown()


if __name__ == "__main__":
    main()
