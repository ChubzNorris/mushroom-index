#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-time helper: fetch a real, CC-licensed photo for every species from the
iNaturalist API, download it into images/, and write images/manifest.json with
attribution metadata (required by most CC licenses).

Usage:  python fetch_images.py
This populates images/<id>.jpg for each species and images/manifest.json.
The web app reads the manifest to show photos + credit lines.

Re-run any time to refresh. Species missing a photo are skipped (the UI falls
back to an emoji).
"""
import json
import os
import sys
import time
import urllib.request
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data.species import SPECIES

IMG_DIR = os.path.join(HERE, "images")
MANIFEST = os.path.join(IMG_DIR, "manifest.json")
UA = "mushroom-index/1.0 (educational; local user)"


def inat_lookup(sci):
    # autocomplete reliably returns the correct taxon for a scientific name.
    url = "https://api.inaturalist.org/v1/taxa/autocomplete?q=" + urllib.parse.quote(sci)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.load(r)
    results = d.get("results") or []
    if not results:
        return None
    r0 = results[0]
    dp = r0.get("default_photo") or {}
    photo = dp.get("medium_url") or dp.get("url")
    # Honest attribution: iNaturalist returns the photographer + license on the
    # photo record. Prefer those over a generic placeholder.
    lic_code = (dp.get("license_code") or "").lower()  # e.g. "cc-by-nc"
    if lic_code:
        license = "CC " + lic_code.replace("cc-", "").upper()  # "CC BY-NC"
    else:
        license = (dp.get("license") or "CC BY-SA")
    # attribution looks like "(c) Name, some rights reserved (CC BY-NC),
    # uploaded by Uploader" -- extract just the photographer's name.
    attr = dp.get("attribution") or ""
    credit = attr.split(", some rights reserved")[0].replace("(c) ", "").strip()
    if not credit:
        credit = "iNaturalist contributor"
    return {
        "taxon_id": r0.get("id"),
        "photo": photo,
        "license": license,
        "credit": credit,
        "source": "iNaturalist",
        "matched_name": r0.get("name"),
        "rank": r0.get("rank"),
    }


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    manifest = {}
    ok = 0
    for s in SPECIES:
        sid = s["id"]
        sci = s["scientific_name"]
        try:
            info = inat_lookup(sci)
        except Exception as e:
            print(f"  skip {s['name']} (lookup error: {e})")
            continue
        if not (info and info["photo"]):
            print(f"  skip {s['name']} (no photo)")
            continue
        dest = os.path.join(IMG_DIR, sid + ".jpg")
        try:
            size = download(info["photo"], dest)
        except Exception as e:
            print(f"  skip {s['name']} (download error: {e})")
            continue
        manifest[sid] = {
            "file": sid + ".jpg",
            "credit": info["credit"],
            "license": info["license"],
            "source": "iNaturalist",
            "taxon_id": info["taxon_id"],
            "matched_name": info["matched_name"],
        }
        ok += 1
        print(f"  ok {s['name']:22} <- {info['matched_name']} ({size} bytes)")
        time.sleep(0.4)

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\nDone: {ok}/{len(SPECIES)} images saved to images/, manifest written.")


if __name__ == "__main__":
    main()
