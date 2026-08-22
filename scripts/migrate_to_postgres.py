#!/usr/bin/env python3
"""Migrate data/species.py → PostgreSQL (forced full reload).

Prefer scripts/sync_catalog.py for day-to-day deploys (hash-aware no-op).
This script always reloads, matching the old one-shot migrator behavior.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv
except ImportError:
    os.system("python -m pip install psycopg2-binary python-dotenv")
    from dotenv import load_dotenv


def main() -> int:
    load_dotenv()
    if not os.environ.get("DATABASE_URL", "").strip():
        print("DATABASE_URL environment variable not set", file=sys.stderr)
        return 2
    from data.catalog_sync import sync_catalog_if_needed

    status = sync_catalog_if_needed(force=True)
    counts = status.get("counts") or {}
    print("Successfully migrated %s species!" % counts.get("species"))
    print("Aliases: %s" % counts.get("aliases"))
    print("Host tree associations: %s" % counts.get("host_trees"))
    print("Lookalikes: %s" % counts.get("lookalikes"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
