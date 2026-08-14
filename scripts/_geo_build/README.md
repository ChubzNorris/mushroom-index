# Rebuild Natural Earth continent paths for the region map.
# 1. Download NE 110m admin_0 countries geojson into this folder as ne_110m_admin.geojson
#    https://github.com/nvkelso/natural-earth-vector (public domain)
# 2. python build_paths.py
# 3. python splice_app.py   # writes REGION_PATHS into ../../app.js
# 4. node smoke_realmap.js  # from repo root: node scripts/_geo_build/smoke_realmap.js
