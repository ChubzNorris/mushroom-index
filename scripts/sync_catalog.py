#!/usr/bin/env python3
"""CLI: sync data/species.py into Postgres (hash-aware).

Usage:
  python scripts/sync_catalog.py           # skip if unchanged
  python scripts/sync_catalog.py --force   # always reload
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
    parser = argparse.ArgumentParser(description="Sync species.py → PostgreSQL")
    parser.add_argument("--force", action="store_true", help="Reload even if hash matches")
    parser.add_argument("--json", action="store_true", help="Print status as JSON")
    args = parser.parse_args()

    if not os.environ.get("DATABASE_URL", "").strip():
        print("DATABASE_URL not set", file=sys.stderr)
        return 2

    from data.catalog_sync import sync_catalog_if_needed

    try:
        status = sync_catalog_if_needed(force=args.force)
    except Exception as e:  # noqa: BLE001
        print("sync failed: %s" % e, file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(status, indent=2))
    else:
        action = status.get("action")
        if action == "skipped":
            print(
                "Catalog already up to date (%s species)."
                % status.get("species_count")
            )
        else:
            counts = status.get("counts") or {}
            print(
                "Catalog %s: %s species, %s aliases, %s host trees, %s lookalikes"
                % (
                    action,
                    counts.get("species"),
                    counts.get("aliases"),
                    counts.get("host_trees"),
                    counts.get("lookalikes"),
                )
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
