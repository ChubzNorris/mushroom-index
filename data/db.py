"""PostgreSQL load path for Spore Drop Index.

Builds the same in-memory SPECIES list shape the frontend already expects.
Falls back is handled by the caller (app.py) when DATABASE_URL is unset or
the load fails.
"""
from __future__ import annotations

import os
from typing import Any, Dict, List, Optional


def _connect(database_url: Optional[str] = None):
    import psycopg2
    import psycopg2.extras

    url = database_url or os.environ.get("DATABASE_URL", "").strip()
    if not url:
        raise RuntimeError("DATABASE_URL not set")
    conn = psycopg2.connect(url)
    return conn, psycopg2.extras


def load_species_from_db(database_url: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return full species records matching data/species.py dict shape."""
    conn, extras = _connect(database_url)
    try:
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute(
            """
            SELECT id, name, scientific_name, edibility, habitat, substrate,
                   ecology, spore_print, potency, bioluminescent, description,
                   distribution
            FROM species
            ORDER BY name
            """
        )
        rows = list(cur.fetchall())
        if not rows:
            raise RuntimeError("species table is empty")

        ids = [r["id"] for r in rows]

        def group_one_col(table: str, col: str) -> Dict[str, List[str]]:
            cur.execute(
                f"SELECT species_id, {col} AS val FROM {table} WHERE species_id = ANY(%s)",
                (ids,),
            )
            out: Dict[str, List[str]] = {i: [] for i in ids}
            for row in cur.fetchall():
                val = row["val"]
                if val is not None:
                    out.setdefault(row["species_id"], []).append(val)
            return out

        aliases = group_one_col("species_aliases", "alias")
        seasons = group_one_col("species_seasons", "season")
        regions = group_one_col("species_regions", "region")
        hosts = group_one_col("species_host_trees", "tree")

        cur.execute(
            "SELECT species_id, shape, colors, diameter_cm FROM species_cap WHERE species_id = ANY(%s)",
            (ids,),
        )
        caps = {r["species_id"]: r for r in cur.fetchall()}

        cur.execute(
            "SELECT species_id, attachment, spacing, colors FROM species_gills WHERE species_id = ANY(%s)",
            (ids,),
        )
        gills = {r["species_id"]: r for r in cur.fetchall()}

        cur.execute(
            "SELECT species_id, colors, ring, volva FROM species_stem WHERE species_id = ANY(%s)",
            (ids,),
        )
        stems = {r["species_id"]: r for r in cur.fetchall()}

        cur.execute(
            """
            SELECT species_id, name, distinguish, link
            FROM species_lookalikes
            WHERE species_id = ANY(%s)
            ORDER BY id
            """,
            (ids,),
        )
        lookalikes: Dict[str, List[Dict[str, Any]]] = {i: [] for i in ids}
        for r in cur.fetchall():
            la = {"name": r["name"], "distinguish": r["distinguish"]}
            if r.get("link"):
                la["link"] = r["link"]
            lookalikes.setdefault(r["species_id"], []).append(la)

        cur.execute(
            "SELECT species_id, fact FROM species_fun_facts WHERE species_id = ANY(%s)",
            (ids,),
        )
        fun_facts: Dict[str, str] = {}
        for r in cur.fetchall():
            # One fun_fact field on the public JSON shape
            fun_facts.setdefault(r["species_id"], r["fact"])

        species: List[Dict[str, Any]] = []
        for r in rows:
            sid = r["id"]
            cap_row = caps.get(sid) or {}
            gill_row = gills.get(sid) or {}
            stem_row = stems.get(sid) or {}

            diam = cap_row.get("diameter_cm") or []
            if diam:
                # JSON wants numbers; Postgres may return Decimal
                diam = [float(x) if x is not None else x for x in diam]
                # Frontend expects 2-int-ish list when present
                diam = [int(x) if isinstance(x, float) and x.is_integer() else x for x in diam]

            rec: Dict[str, Any] = {
                "id": sid,
                "name": r["name"],
                "scientific_name": r["scientific_name"],
                "aliases": aliases.get(sid, []),
                "edibility": r.get("edibility"),
                "cap": {
                    "shape": list(cap_row.get("shape") or []),
                    "colors": list(cap_row.get("colors") or []),
                    "diameter_cm": diam,
                },
                "gills": {
                    "attachment": gill_row.get("attachment") or "n/a",
                    "spacing": gill_row.get("spacing") or "n/a",
                    "colors": list(gill_row.get("colors") or []),
                },
                "stem": {
                    "colors": list(stem_row.get("colors") or []),
                    "ring": bool(stem_row.get("ring")),
                    "volva": bool(stem_row.get("volva")),
                },
                "spore_print": r.get("spore_print"),
                "habitat": r.get("habitat"),
                "substrate": r.get("substrate"),
                "ecology": r.get("ecology"),
                "season": seasons.get(sid, []),
                "distribution": r.get("distribution"),
                "regions": regions.get(sid, []),
                "description": r.get("description") or "",
                "lookalikes": lookalikes.get(sid, []),
            }
            if sid in fun_facts:
                rec["fun_fact"] = fun_facts[sid]
            if r.get("potency"):
                rec["potency"] = r["potency"]
            if r.get("bioluminescent"):
                rec["bioluminescent"] = True
            host_list = hosts.get(sid, [])
            if host_list:
                rec["host_trees"] = host_list
            species.append(rec)

        return species
    finally:
        conn.close()


def try_load_species() -> tuple[List[Dict[str, Any]], str]:
    """Load species from Postgres when DATABASE_URL is set.

    Returns (species_list, source_label). Raises on hard failure so caller
    can fall back to data/species.py.
    """
    if not os.environ.get("DATABASE_URL", "").strip():
        raise RuntimeError("DATABASE_URL not set")
    species = load_species_from_db()
    return species, "postgres"
