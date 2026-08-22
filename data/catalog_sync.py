"""Automatic species.py → PostgreSQL catalog sync.

On deploy/boot the app calls sync_catalog_if_needed(). It:
1. Ensures tables exist (idempotent schema)
2. Hashes data/species.py
3. Skips work when the hash already matches catalog_meta
4. Otherwise TRUNCATE + batch reloads the full catalog in one transaction

data/species.py remains the authoring source of truth.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
SPECIES_FILE = ROOT / "data" / "species.py"
ENSURE_SCHEMA = ROOT / "database" / "ensure_schema.sql"

META_HASH_KEY = "species_py_sha256"
META_COUNT_KEY = "species_count"
# Fixed advisory lock key so concurrent boots don't double-migrate.
ADVISORY_LOCK_KEY = 78423019


def species_file_path() -> Path:
    return SPECIES_FILE


def hash_species_file(path: Optional[Path] = None) -> str:
    p = path or SPECIES_FILE
    data = p.read_bytes()
    return hashlib.sha256(data).hexdigest()


def load_species_data(path: Optional[Path] = None) -> List[Dict[str, Any]]:
    p = path or SPECIES_FILE
    content = p.read_text(encoding="utf-8")
    start_idx = content.index("SPECIES = [")
    species_json = content[start_idx + len("SPECIES = ") :].strip()
    species_json = re.sub(
        r"\b(True|False|None)\b",
        lambda m: {"True": "true", "False": "false", "None": "null"}[m.group()],
        species_json,
    )
    data = json.loads(species_json)
    if not isinstance(data, list) or not data:
        raise ValueError("species.py did not parse to a non-empty list")
    return data


def _connect(database_url: Optional[str] = None):
    import psycopg2
    import psycopg2.extras

    url = (database_url or os.environ.get("DATABASE_URL", "")).strip()
    if not url:
        raise RuntimeError("DATABASE_URL not set")
    return psycopg2.connect(url), psycopg2.extras


def ensure_schema(conn) -> None:
    sql = ENSURE_SCHEMA.read_text(encoding="utf-8")
    prev = conn.autocommit
    conn.autocommit = True
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
    finally:
        conn.autocommit = prev


def _get_meta(cur, key: str) -> Optional[str]:
    cur.execute("SELECT value FROM catalog_meta WHERE key = %s", (key,))
    row = cur.fetchone()
    if not row:
        return None
    return row[0] if not isinstance(row, dict) else row.get("value")


def _set_meta(cur, key: str, value: str) -> None:
    cur.execute(
        """
        INSERT INTO catalog_meta (key, value, updated_at)
        VALUES (%s, %s, NOW())
        ON CONFLICT (key) DO UPDATE
          SET value = EXCLUDED.value, updated_at = NOW()
        """,
        (key, value),
    )


def migrate_species_data(conn, extras, species_data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Replace catalog tables with species_data. Caller owns transaction."""
    cur = conn.cursor()
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

        extras.execute_batch(
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
            extras.execute_batch(
                cur,
                "INSERT INTO species_aliases VALUES (%s,%s) ON CONFLICT DO NOTHING",
                alias_rows,
                page_size=200,
            )
        if season_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_seasons VALUES (%s,%s) ON CONFLICT DO NOTHING",
                season_rows,
                page_size=200,
            )
        if region_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_regions VALUES (%s,%s) ON CONFLICT DO NOTHING",
                region_rows,
                page_size=200,
            )
        if tree_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_host_trees VALUES (%s,%s) ON CONFLICT DO NOTHING",
                tree_rows,
                page_size=200,
            )
        if cap_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_cap (species_id, shape, colors, diameter_cm) VALUES (%s,%s,%s,%s)",
                cap_rows,
                page_size=100,
            )
        if gill_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_gills (species_id, attachment, spacing, colors) VALUES (%s,%s,%s,%s)",
                gill_rows,
                page_size=100,
            )
        if stem_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_stem (species_id, colors, ring, volva) VALUES (%s,%s,%s,%s)",
                stem_rows,
                page_size=100,
            )
        if lookalike_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_lookalikes (species_id, name, distinguish, link) VALUES (%s,%s,%s,%s)",
                lookalike_rows,
                page_size=200,
            )
        if fun_rows:
            extras.execute_batch(
                cur,
                "INSERT INTO species_fun_facts VALUES (%s,%s) ON CONFLICT DO NOTHING",
                fun_rows,
                page_size=200,
            )

        cur.execute("SELECT COUNT(*) FROM species")
        species_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM species_aliases")
        aliases_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM species_host_trees")
        host_trees_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM species_lookalikes")
        lookalike_count = cur.fetchone()[0]
        return {
            "species": int(species_count),
            "aliases": int(aliases_count),
            "host_trees": int(host_trees_count),
            "lookalikes": int(lookalike_count),
        }
    finally:
        cur.close()


def sync_catalog_if_needed(
    database_url: Optional[str] = None,
    force: bool = False,
    species_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Ensure Postgres matches data/species.py. No-op when hash matches.

    Returns a status dict: {action, hash, counts?, reason?}.
    """
    path = species_path or SPECIES_FILE
    if not path.is_file():
        raise FileNotFoundError("species file missing: %s" % path)

    file_hash = hash_species_file(path)
    conn, extras = _connect(database_url)
    try:
        ensure_schema(conn)

        # Serialize concurrent boots (rolling deploy / multi-instance).
        with conn.cursor() as cur:
            cur.execute("SELECT pg_advisory_lock(%s)", (ADVISORY_LOCK_KEY,))
        conn.commit()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM species")
                db_count = int(cur.fetchone()[0])
                stored_hash = _get_meta(cur, META_HASH_KEY)

            if (
                not force
                and stored_hash == file_hash
                and db_count > 0
            ):
                return {
                    "action": "skipped",
                    "hash": file_hash,
                    "species_count": db_count,
                    "reason": "catalog hash matches",
                }

            species_data = load_species_data(path)
            counts = migrate_species_data(conn, extras, species_data)
            with conn.cursor() as cur:
                _set_meta(cur, META_HASH_KEY, file_hash)
                _set_meta(cur, META_COUNT_KEY, str(counts["species"]))
            conn.commit()
            return {
                "action": "migrated" if not force else "forced",
                "hash": file_hash,
                "counts": counts,
                "previous_hash": stored_hash,
                "previous_count": db_count,
            }
        except Exception:
            conn.rollback()
            raise
        finally:
            with conn.cursor() as cur:
                cur.execute("SELECT pg_advisory_unlock(%s)", (ADVISORY_LOCK_KEY,))
            conn.commit()
    finally:
        conn.close()


def boot_sync(log=sys.stderr) -> Tuple[bool, Dict[str, Any]]:
    """Run sync when DATABASE_URL is set. Returns (ran_or_skipped_ok, status)."""
    if not os.environ.get("DATABASE_URL", "").strip():
        return False, {"action": "disabled", "reason": "no DATABASE_URL"}
    force = os.environ.get("CATALOG_FORCE_SYNC", "").strip().lower() in {
        "1", "true", "yes", "on"
    }
    try:
        status = sync_catalog_if_needed(force=force)
        action = status.get("action")
        if action == "skipped":
            log.write(
                "[mushroom-index] catalog sync skipped (%s species, hash %s…)\n"
                % (status.get("species_count"), (status.get("hash") or "")[:12])
            )
        else:
            counts = status.get("counts") or {}
            log.write(
                "[mushroom-index] catalog %s → %s species "
                "(aliases=%s host_trees=%s lookalikes=%s)\n"
                % (
                    action,
                    counts.get("species"),
                    counts.get("aliases"),
                    counts.get("host_trees"),
                    counts.get("lookalikes"),
                )
            )
        return True, status
    except Exception as e:  # noqa: BLE001
        log.write("[mushroom-index] catalog sync failed: %s\n" % e)
        return False, {"action": "error", "error": str(e)}
