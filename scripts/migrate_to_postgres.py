#!/usr/bin/env python3
"""Migrate data/species.py → PostgreSQL. Requires DATABASE_URL."""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import psycopg2
    import psycopg2.extras
    from dotenv import load_dotenv
except ImportError:
    os.system("python -m pip install psycopg2-binary python-dotenv")
    import psycopg2
    import psycopg2.extras
    from dotenv import load_dotenv


def load_species_data():
    species_file = Path("data/species.py")
    content = species_file.read_text(encoding="utf-8")
    start_idx = content.index("SPECIES = [")
    species_json = content[start_idx + len("SPECIES = ") :].strip()
    species_json = re.sub(
        r"\b(True|False|None)\b",
        lambda m: {"True": "true", "False": "false", "None": "null"}[m.group()],
        species_json,
    )
    return json.loads(species_json)


def get_db_connection():
    load_dotenv()
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set")
    return psycopg2.connect(database_url)


def migrate_data():
    species_data = load_species_data()
    conn = get_db_connection()
    cur = conn.cursor()
    print(f"Migrating {len(species_data)} species to PostgreSQL...")

    try:
        cur.execute(
            """
            TRUNCATE TABLE
              species, species_aliases, species_seasons, species_regions,
              species_host_trees, species_cap, species_gills, species_stem,
              species_lookalikes, species_fun_facts
            CASCADE
            """
        )

        species_rows = []
        alias_rows = []
        season_rows = []
        region_rows = []
        tree_rows = []
        cap_rows = []
        gill_rows = []
        stem_rows = []
        lookalike_rows = []
        fun_rows = []

        for s in species_data:
            sid = s["id"]
            species_rows.append(
                (
                    sid,
                    s["name"],
                    s["scientific_name"],
                    s.get("edibility"),
                    s.get("habitat"),
                    s.get("substrate"),
                    s.get("ecology"),
                    s.get("spore_print"),
                    s.get("potency"),
                    bool(s.get("bioluminescent")),
                    s.get("description"),
                    s.get("distribution"),
                )
            )
            for alias in s.get("aliases") or []:
                if alias:
                    alias_rows.append((sid, alias))
            for season in s.get("season") or []:
                if season:
                    season_rows.append((sid, season))
            for region in s.get("regions") or []:
                if region:
                    region_rows.append((sid, region))
            for tree in s.get("host_trees") or []:
                if tree:
                    tree_rows.append((sid, tree))

            cap = s.get("cap") or {}
            if cap:
                cap_rows.append(
                    (sid, cap.get("shape") or [], cap.get("colors") or [], cap.get("diameter_cm") or [])
                )
            gills = s.get("gills") or {}
            if gills:
                gill_rows.append(
                    (
                        sid,
                        gills.get("attachment"),
                        gills.get("spacing"),
                        gills.get("colors") or [],
                    )
                )
            stem = s.get("stem") or {}
            if stem:
                stem_rows.append(
                    (
                        sid,
                        stem.get("colors") or [],
                        bool(stem.get("ring")),
                        bool(stem.get("volva")),
                    )
                )
            for lookalike in s.get("lookalikes") or []:
                lookalike_rows.append(
                    (
                        sid,
                        lookalike.get("name") or "",
                        lookalike.get("distinguish") or "",
                        lookalike.get("link"),
                    )
                )
            fun = s.get("fun_fact")
            if fun:
                fun_rows.append((sid, fun))

        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO species (
              id, name, scientific_name, edibility, habitat, substrate, ecology,
              spore_print, potency, bioluminescent, description, distribution
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            species_rows,
            page_size=100,
        )
        if alias_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_aliases VALUES (%s,%s) ON CONFLICT DO NOTHING",
                alias_rows,
                page_size=200,
            )
        if season_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_seasons VALUES (%s,%s) ON CONFLICT DO NOTHING",
                season_rows,
                page_size=200,
            )
        if region_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_regions VALUES (%s,%s) ON CONFLICT DO NOTHING",
                region_rows,
                page_size=200,
            )
        if tree_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_host_trees VALUES (%s,%s) ON CONFLICT DO NOTHING",
                tree_rows,
                page_size=200,
            )
        if cap_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_cap (species_id, shape, colors, diameter_cm) VALUES (%s,%s,%s,%s)",
                cap_rows,
                page_size=100,
            )
        if gill_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_gills (species_id, attachment, spacing, colors) VALUES (%s,%s,%s,%s)",
                gill_rows,
                page_size=100,
            )
        if stem_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_stem (species_id, colors, ring, volva) VALUES (%s,%s,%s,%s)",
                stem_rows,
                page_size=100,
            )
        if lookalike_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_lookalikes (species_id, name, distinguish, link) VALUES (%s,%s,%s,%s)",
                lookalike_rows,
                page_size=200,
            )
        if fun_rows:
            psycopg2.extras.execute_batch(
                cur,
                "INSERT INTO species_fun_facts VALUES (%s,%s) ON CONFLICT DO NOTHING",
                fun_rows,
                page_size=200,
            )

        conn.commit()
        cur.execute("SELECT COUNT(*) FROM species")
        species_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM species_aliases")
        aliases_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM species_host_trees")
        host_trees_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM species_lookalikes")
        lookalike_count = cur.fetchone()[0]
        print(f"Successfully migrated {species_count} species!")
        print(f"Aliases: {aliases_count}")
        print(f"Host tree associations: {host_trees_count}")
        print(f"Lookalikes: {lookalike_count}")
    except Exception as e:
        conn.rollback()
        print(f"Migration failed: {e}")
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    migrate_data()
