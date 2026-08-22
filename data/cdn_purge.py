"""Cloudflare cache purge helpers for Spore Drop Index.

Uses CLOUDFLARE_API_TOKEN + CLOUDFLARE_ZONE_ID (Railway web env).
Never logs the token. No-ops cleanly when env is missing.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

DEFAULT_PURGE_URLS = [
    "https://www.sporedropindex.com/",
    "https://www.sporedropindex.com/index.html",
    "https://www.sporedropindex.com/api/species",
    "https://www.sporedropindex.com/api/facets",
    "https://www.sporedropindex.com/api/lookalike-pairs",
    "https://sporedropindex.com/",
    "https://sporedropindex.com/api/species",
    "https://sporedropindex.com/api/facets",
]


def _env(name: str) -> str:
    return (os.environ.get(name) or "").strip()


def configured() -> bool:
    return bool(_env("CLOUDFLARE_API_TOKEN") and _env("CLOUDFLARE_ZONE_ID"))


def purge_urls(urls: Optional[List[str]] = None) -> Dict[str, Any]:
    """Purge specific URLs from Cloudflare cache."""
    token = _env("CLOUDFLARE_API_TOKEN")
    zone = _env("CLOUDFLARE_ZONE_ID")
    if not token or not zone:
        return {"ok": False, "action": "disabled", "reason": "missing CLOUDFLARE_* env"}

    targets = list(urls or DEFAULT_PURGE_URLS)
    # Cloudflare files purge max 30 URLs per request
    batches = [targets[i : i + 30] for i in range(0, len(targets), 30)] or [[]]
    results = []
    for batch in batches:
        if not batch:
            continue
        body = json.dumps({"files": batch}).encode("utf-8")
        req = urllib.request.Request(
            "https://api.cloudflare.com/client/v4/zones/%s/purge_cache" % zone,
            data=body,
            method="POST",
            headers={
                "Authorization": "Bearer %s" % token,
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:500]
            return {
                "ok": False,
                "action": "error",
                "status": e.code,
                "detail": detail,
            }
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "action": "error", "detail": str(e)}
        if not payload.get("success"):
            return {
                "ok": False,
                "action": "error",
                "errors": payload.get("errors"),
            }
        results.append(payload.get("result"))
    return {"ok": True, "action": "purged_urls", "count": len(targets), "results": results}


def purge_everything() -> Dict[str, Any]:
    """Nuclear option — purge entire zone. Prefer purge_urls for normal deploys."""
    token = _env("CLOUDFLARE_API_TOKEN")
    zone = _env("CLOUDFLARE_ZONE_ID")
    if not token or not zone:
        return {"ok": False, "action": "disabled", "reason": "missing CLOUDFLARE_* env"}
    body = json.dumps({"purge_everything": True}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.cloudflare.com/client/v4/zones/%s/purge_cache" % zone,
        data=body,
        method="POST",
        headers={
            "Authorization": "Bearer %s" % token,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "action": "error", "detail": str(e)}
    if not payload.get("success"):
        return {"ok": False, "action": "error", "errors": payload.get("errors")}
    return {"ok": True, "action": "purged_everything"}


def purge_after_catalog_change(log=sys.stderr) -> Dict[str, Any]:
    """Called when catalog sync actually rewrote Postgres."""
    if not configured():
        log.write("[mushroom-index] CDN purge skipped (Cloudflare env not set)\n")
        return {"ok": False, "action": "disabled"}
    status = purge_urls()
    if status.get("ok"):
        log.write(
            "[mushroom-index] CDN purged %s catalog URLs\n" % status.get("count", 0)
        )
    else:
        log.write(
            "[mushroom-index] CDN purge failed: %s\n"
            % (status.get("detail") or status.get("errors") or status.get("reason"))
        )
    return status
