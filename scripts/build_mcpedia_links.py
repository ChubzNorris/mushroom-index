#!/usr/bin/env python3
"""Rebuild data/mcpedia_links.py from mcpedia.earth sitemap ∩ our catalog.

Only slugs present in the public sitemap are kept (SPA pages return 200 even
for unknown routes, so HEAD/GET status is not enough).
"""
from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from data.species import SPECIES  # noqa: E402

SITEMAP = "https://mcpedia.earth/sitemap.xml"
UA = "SporeDropIndexBot/1.0 (+https://www.sporedropindex.com; collab link build)"
OUT = ROOT / "data" / "mcpedia_links.py"


def sci_slug(name: str) -> str:
    if not name:
        return ""
    s = name.lower().strip()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def fetch_slugs() -> set[str]:
    req = urllib.request.Request(SITEMAP, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as resp:
        text = resp.read().decode("utf-8", "replace")
    locs = re.findall(r"<loc>(https://mcpedia\.earth/species/[^<]+)</loc>", text)
    return {u.rstrip("/").split("/")[-1].lower() for u in locs}


def main() -> int:
    slugs = fetch_slugs()
    matched = []
    for sp in SPECIES:
        sid = (sp.get("id") or "").lower()
        sci = sci_slug(sp.get("scientific_name") or "")
        hit = sid if sid in slugs else (sci if sci in slugs else None)
        if hit:
            matched.append((sp["id"], hit, sp.get("name") or "", sp.get("scientific_name") or ""))

    matched.sort(key=lambda x: x[0])
    lines = [
        '"""mcpedia.earth links for taxa shared with Spore Drop Index.\n',
        "\n",
        "Generated from mcpedia sitemap ∩ our species ids / scientific_name slugs.\n",
        "Only include URLs that exist in the sitemap (SPA returns 200 for unknowns).\n",
        "Regenerate: python scripts/build_mcpedia_links.py\n",
        '"""\n\n',
        "MCPEDIA_LINKS = {\n",
    ]
    for oid, slug, name, sci in matched:
        lines.append(
            f'    "{oid}": "https://mcpedia.earth/species/{slug}",  # {name} · {sci}\n'
        )
    lines.append("}\n")
    OUT.write_text("".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({len(matched)}/{len(SPECIES)} linked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
