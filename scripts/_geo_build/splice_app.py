#!/usr/bin/env python3
"""Splice Natural Earth REGION_PATHS into app.js (replace existing REGION_PATHS block)."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
app_path = ROOT / "app.js"
app = app_path.read_text(encoding="utf-8")
paths_js = (ROOT / "scripts/_geo_build/region_paths_generated.js").read_text(encoding="utf-8")

m = re.search(
    r"// Auto-generated Natural Earth[\s\S]*?const REGION_PATHS = \{[\s\S]*?\n\};\n",
    app,
)
if not m:
    m = re.search(r"const REGION_PATHS = \{[\s\S]*?\n\};\n", app)
if not m:
    raise SystemExit("REGION_PATHS block not found in app.js")

app = app[: m.start()] + paths_js.rstrip() + "\n\n" + app[m.end() :]
app_path.write_text(app, encoding="utf-8")
print("replaced REGION_PATHS at", m.start(), "new bytes", len(paths_js))

r = subprocess.run(["node", "--check", str(app_path)], capture_output=True, text=True)
print("node check", r.returncode)
if r.stderr:
    print(r.stderr)
