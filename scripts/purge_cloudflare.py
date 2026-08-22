#!/usr/bin/env python3
"""Purge Spore Drop Index Cloudflare cache.

  python scripts/purge_cloudflare.py           # key catalog URLs
  python scripts/purge_cloudflare.py --all     # entire zone
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def main() -> int:
    if load_dotenv:
        load_dotenv(ROOT / ".env")
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="purge entire zone")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    from data.cdn_purge import configured, purge_everything, purge_urls

    if not configured():
        print("CLOUDFLARE_API_TOKEN / CLOUDFLARE_ZONE_ID not set", file=sys.stderr)
        return 2
    status = purge_everything() if args.all else purge_urls()
    if args.json:
        print(json.dumps(status, indent=2))
    else:
        print(status.get("action"), "ok=" + str(status.get("ok")))
        if not status.get("ok"):
            print(status, file=sys.stderr)
            return 1
    return 0 if status.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
