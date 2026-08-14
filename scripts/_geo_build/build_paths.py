#!/usr/bin/env python3
"""Build simplified Robinson-projected continent SVG paths from Natural Earth."""
import json
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
admin = json.loads((HERE / "ne_110m_admin.geojson").read_text(encoding="utf-8"))

conts = defaultdict(int)
for f in admin["features"]:
    c = f["properties"].get("CONTINENT") or f["properties"].get("continent")
    conts[c] += 1
print("continents", dict(conts))

REGION_MAP = {
    "North America": "north-america",
    "South America": "south-america",
    "Europe": "europe",
    "Africa": "africa",
    "Asia": "asia",
    "Oceania": "oceania",
}

# Always keep these even if small area
KEEP_NAMES = {
    "New Zealand", "Iceland", "Madagascar", "Sri Lanka", "Taiwan", "Japan",
    "Philippines", "Indonesia", "United Kingdom", "Ireland", "Cuba", "Haiti",
    "Dominican Rep.", "Jamaica", "Puerto Rico", "Papua New Guinea",
    "New Caledonia", "Fiji", "Solomon Is.", "Vanuatu", "Samoa", "Tonga",
    "Cyprus", "Hispaniola", "Trinidad and Tobago", "Bahamas", "Greenland",
    "Svalbard", "Falkland Is.", "Tasmania",
}


def iter_rings(geom):
    t = geom["type"]
    coords = geom["coordinates"]
    if t == "Polygon":
        yield coords[0]
    elif t == "MultiPolygon":
        for poly in coords:
            yield poly[0]


def ring_area(ring):
    area = 0.0
    for i in range(len(ring) - 1):
        x1, y1 = ring[i]
        x2, y2 = ring[i + 1]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


region_rings = defaultdict(list)
for f in admin["features"]:
    cont = f["properties"].get("CONTINENT")
    rid = REGION_MAP.get(cont)
    name = f["properties"].get("NAME") or f["properties"].get("ADMIN") or ""
    # Natural Earth tags Russia as Europe; for educational continent maps
    # Russia reads as Asia (matches common classroom globe coloring).
    if name in ("Russia", "Russia"):
        rid = "asia"
    # Kazakhstan etc. already Asia. Turkey is Asia in NE.
    if not rid:
        continue
    geom = f["geometry"]
    for ring in iter_rings(geom):
        if len(ring) < 4:
            continue
        area = ring_area(ring)
        if area < 2 and name not in KEEP_NAMES:
            continue
        if area < 8 and name not in KEEP_NAMES and area < 3:
            continue
        region_rings[rid].append({"name": name, "area": area, "ring": ring})

for rid, rings in region_rings.items():
    rings.sort(key=lambda r: -r["area"])
    print(rid, "rings", len(rings), "top", [(r["name"], round(r["area"], 1)) for r in rings[:6]])

# Robinson interpolation table (lat 0..90 step 5): X length factor, Y factor
ROB = [
    (0, 1.0000, 0.0000),
    (5, 0.9986, 0.0620),
    (10, 0.9954, 0.1240),
    (15, 0.9900, 0.1860),
    (20, 0.9822, 0.2480),
    (25, 0.9730, 0.3100),
    (30, 0.9600, 0.3720),
    (35, 0.9427, 0.4340),
    (40, 0.9216, 0.4958),
    (45, 0.8962, 0.5571),
    (50, 0.8679, 0.6176),
    (55, 0.8350, 0.6769),
    (60, 0.7986, 0.7346),
    (65, 0.7597, 0.7903),
    (70, 0.7186, 0.8435),
    (75, 0.6732, 0.8936),
    (80, 0.6213, 0.9394),
    (85, 0.5722, 0.9761),
    (90, 0.5322, 1.0000),
]


def rob_xy_factors(lat):
    alat = abs(lat)
    if alat >= 90:
        return ROB[-1][1], ROB[-1][2] * (1 if lat >= 0 else -1)
    i = int(alat // 5)
    t = (alat - i * 5) / 5.0
    x0, y0 = ROB[i][1], ROB[i][2]
    x1, y1 = ROB[i + 1][1], ROB[i + 1][2]
    X = x0 + t * (x1 - x0)
    Y = y0 + t * (y1 - y0)
    if lat < 0:
        Y = -Y
    return X, Y


def project_robinson(lon, lat, width=1000, height=500, pad=18):
    X, Y = rob_xy_factors(lat)
    usable_w = width - 2 * pad
    usable_h = height - 2 * pad
    R_w = usable_w / (2 * 0.8487 * math.pi)
    R_h = usable_h / (2 * 1.3523)
    R = min(R_w, R_h)
    lam = math.radians(lon)
    x = 0.8487 * R * X * lam
    y = 1.3523 * R * Y
    return width / 2 + x, height / 2 - y


def simplify_ring(ring, tol=0.45):
    """Ramer-Douglas-Peucker on lon/lat degrees."""
    if len(ring) <= 4:
        return ring
    pts = [(float(p[0]), float(p[1])) for p in ring]
    closed = (
        pts[0] == pts[-1]
        or (abs(pts[0][0] - pts[-1][0]) < 1e-9 and abs(pts[0][1] - pts[-1][1]) < 1e-9)
    )
    if closed:
        pts = pts[:-1]

    def perp_dist(p, a, b):
        ax, ay = a
        bx, by = b
        px, py = p
        dx, dy = bx - ax, by - ay
        if dx == 0 and dy == 0:
            return math.hypot(px - ax, py - ay)
        t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
        t = max(0.0, min(1.0, t))
        return math.hypot(px - (ax + t * dx), py - (ay + t * dy))

    def rdp(points, eps):
        if len(points) < 3:
            return points
        a, b = points[0], points[-1]
        max_d, idx = -1.0, 0
        for i in range(1, len(points) - 1):
            d = perp_dist(points[i], a, b)
            if d > max_d:
                max_d, idx = d, i
        if max_d > eps:
            left = rdp(points[: idx + 1], eps)
            right = rdp(points[idx:], eps)
            return left[:-1] + right
        return [a, b]

    simp = rdp(pts, tol)
    if len(simp) < 3:
        return ring
    if closed:
        simp = simp + [simp[0]]
    return simp


def ring_to_svg_path(ring, rid=None):
    pts = []
    for lon, lat in ring:
        lon = max(-179.999, min(179.999, float(lon)))
        lat = max(-89.9, min(89.9, float(lat)))
        x, y = project_robinson(lon, lat)
        pts.append((x, y, lon))
    if len(pts) < 3:
        return ""

    # Split on antimeridian jumps
    segs = []
    cur = [pts[0]]
    for i in range(1, len(pts)):
        plon = pts[i - 1][2]
        lon = pts[i][2]
        if abs(lon - plon) > 180:
            if len(cur) >= 2:
                segs.append(cur)
            cur = [pts[i]]
        else:
            cur.append(pts[i])
    if len(cur) >= 2:
        segs.append(cur)

    # Drop antimeridian-wrap fragments that land on the wrong ocean side.
    # Oceania should live on the right of a Robinson world; NA on the left.
    def keep_seg(seg):
        xs = [p[0] for p in seg]
        mean_x = sum(xs) / len(xs)
        if rid == "oceania" and mean_x < 620:
            return False
        if rid == "north-america" and mean_x > 620:
            return False
        if rid == "asia" and mean_x < 420 and max(xs) - min(xs) < 80:
            # tiny Asia fragments wrapping into Atlantic — drop
            return False
        return True

    segs = [s for s in segs if keep_seg(s)]
    if not segs:
        return ""

    parts = []
    for seg in segs:
        d = f"M{seg[0][0]:.1f},{seg[0][1]:.1f}"
        for x, y, _ in seg[1:]:
            d += f"L{x:.1f},{y:.1f}"
        # Close single-segment rings; multi-seg antimeridian cuts stay open
        if len(segs) == 1 or (abs(seg[0][0] - seg[-1][0]) < 1.5 and abs(seg[0][1] - seg[-1][1]) < 1.5):
            d += "Z"
        elif len(seg) >= 4:
            d += "Z"
        parts.append(d)
    return " ".join(parts)


out = {}
stats = {}
for rid, rings in region_rings.items():
    paths = []
    total_pts = 0
    for r in rings:
        area = r["area"]
        tol = 0.55 if area > 200 else (0.35 if area > 20 else 0.22)
        simp = simplify_ring(r["ring"], tol=tol)
        if len(simp) < 4:
            continue
        d = ring_to_svg_path(simp, rid=rid)
        if not d or len(d) < 12:
            continue
        paths.append(d)
        total_pts += len(simp)
    out[rid] = " ".join(paths)
    stats[rid] = {"parts": len(paths), "pts": total_pts, "chars": len(out[rid])}

print("STATS", stats)
print("total path chars", sum(len(v) for v in out.values()))

ORDER = ["north-america", "south-america", "europe", "africa", "asia", "oceania"]
js_lines = [
    "// Auto-generated Natural Earth 110m continent paths (Robinson projection, viewBox 0 0 1000 500).",
    "// Source: Natural Earth (public domain). Educational region fills — not political borders.",
    "const REGION_PATHS = {",
]
for rid in ORDER:
    d = out.get(rid, "")
    js_lines.append(f"  '{rid}':")
    chunk = 110
    parts = [d[i : i + chunk] for i in range(0, max(len(d), 1), chunk)] or [""]
    for i, p in enumerate(parts):
        esc = p.replace("\\", "\\\\").replace("'", "\\'")
        end = "," if i == len(parts) - 1 else " +"
        prefix = "    "
        js_lines.append(f"{prefix}'{esc}'{end}")
js_lines.append("};")
js_text = "\n".join(js_lines) + "\n"
(HERE / "region_paths_generated.js").write_text(js_text, encoding="utf-8")
print("wrote region_paths_generated.js", len(js_text))

# Also dump as JSON for easier embedding if needed
(HERE / "region_paths.json").write_text(json.dumps(out), encoding="utf-8")

colors = {
    "north-america": "#f5d76e",
    "south-america": "#b388ff",
    "europe": "#7dff9a",
    "africa": "#ffb347",
    "asia": "#c45c5c",
    "oceania": "#f5a9c5",
}
svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="1000" height="500">',
    '<rect width="1000" height="500" fill="#1a4f86"/>',
    '<ellipse cx="500" cy="250" rx="482" ry="232" fill="#2470b0"/>',
]
for rid, col in colors.items():
    d = out.get(rid, "")
    if d:
        svg.append(
            f'<path data-region="{rid}" d="{d}" fill="{col}" '
            f'stroke="#0a1628" stroke-width="0.7" stroke-linejoin="round"/>'
        )
svg.append(
    '<ellipse cx="500" cy="250" rx="482" ry="232" fill="none" stroke="#0a1628" stroke-width="2"/>'
)
svg.append("</svg>")
(HERE / "preview_continents.svg").write_text("\n".join(svg), encoding="utf-8")
print("preview written")
