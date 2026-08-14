/* Spore Drop Index - frontend logic */
'use strict';

const state = {
  q: '',
  filters: {},   // key -> value (single-select chips)
  sort: 'name',
};

const stateKey = (k) => k;
const FILTER_DEFS = [
  { key: 'edibility', title: 'Edibility' },
  { key: 'potency', title: 'Potency (psychoactive)' },
  { key: 'habitat', title: 'Habitat' },
  { key: 'substrate', title: 'Substrate' },
  { key: 'ecology', title: 'Ecology' },
  { key: 'spore_print', title: 'Spore print' },
  { key: 'cap_color', title: 'Cap color' },
  { key: 'gill_attachment', title: 'Gills / pores' },
  { key: 'season', title: 'Season' },
  { key: 'regions', title: 'Region', multi: true },
];

// Keys whose state.filters value is an array (multi-select, matches ANY);
// everything else is a single-select string.
const MULTI_KEYS = new Set(FILTER_DEFS.filter(d => d.multi).map(d => d.key));

const GILL_LABELS = {
  'free': 'Gills (free)',
  'attached': 'Gills (attached)',
  'decurrent': 'Gills (decurrent)',
  'pores': 'Pores (bolete)',
  'n/a': 'No gills/pores',
};

const EMOJI_FOR = {
  'deadly': '☠️', 'poisonous': '🤢', 'inedible': '🚫',
  'unknown': '❓', 'edible': '🍽️', 'choice': '⭐',
};

const REGION_LABELS = {
  'north-america': 'North America',
  'europe': 'Europe',
  'asia': 'Asia',
  'south-america': 'South America',
  'africa': 'Africa',
  'oceania': 'Oceania',
  'global': 'Global / widespread',
  // legacy alias present on a few older entries
  'na': 'North America',
};

// Canonical region order for map UI (excludes legacy "na" alias).
const MAP_REGIONS = [
  'north-america',
  'south-america',
  'europe',
  'africa',
  'asia',
  'oceania',
  'global',
];

// Educational continent rings as [lon, lat] degrees (WGS-ish).
// Stylized blobs for range browsing — not political borders.
const REGION_RINGS = {
  'north-america': [
    // Mainland + Alaska bulge + Central America taper
    [-168, 65], [-155, 71], [-140, 70], [-125, 72], [-105, 72], [-90, 70],
    [-80, 62], [-70, 58], [-60, 52], [-55, 47], [-65, 42], [-75, 35],
    [-82, 28], [-90, 22], [-97, 18], [-105, 20], [-112, 24], [-118, 32],
    [-125, 38], [-130, 48], [-140, 58], [-155, 60], [-168, 65],
  ],
  'south-america': [
    [-81, 12], [-70, 12], [-60, 8], [-50, 2], [-40, -5], [-35, -15],
    [-38, -30], [-45, -40], [-55, -50], [-68, -55], [-75, -50], [-78, -40],
    [-80, -25], [-82, -10], [-81, 5], [-81, 12],
  ],
  'europe': [
    [-10, 36], [-9, 43], [-5, 50], [-1, 58], [5, 62], [15, 70],
    [28, 71], [40, 68], [42, 58], [40, 48], [35, 42], [28, 38],
    [18, 36], [8, 38], [0, 38], [-8, 37], [-10, 36],
  ],
  'africa': [
    [-17, 28], [-10, 35], [0, 36], [12, 33], [25, 32], [35, 28],
    [42, 18], [50, 12], [51, 0], [48, -12], [40, -25], [32, -34],
    [20, -35], [12, -30], [5, -20], [-5, -10], [-12, 0], [-17, 12],
    [-18, 22], [-17, 28],
  ],
  'asia': [
    // Broad Eurasia + India + SE Asia (one educational blob)
    [42, 55], [50, 65], [70, 72], [100, 74], [130, 70], [150, 62],
    [165, 55], [160, 42], [145, 35], [140, 22], [125, 10], [110, 5],
    [100, 2], [90, 8], [80, 12], [75, 22], [70, 28], [62, 28],
    [55, 32], [48, 38], [44, 45], [42, 55],
  ],
  'oceania': [
    // Australia + NZ-ish satellite as one range tag
    [114, -20], [125, -12], [140, -11], [150, -15], [153, -28],
    [150, -38], [140, -42], [125, -36], [116, -34], [114, -26],
    [114, -20],
  ],
};

// Orthographic globe layout (square viewBox so the disc reads as a sphere).
const GLOBE = {
  CX: 500,
  CY: 500,
  R: 430,
  // Center over the Atlantic so NA / EU / AF / SA all read on the front.
  // Asia/Oceania sit toward the limb — chips still catch them.
  LON0: -20,
  LAT0: 12,
};

const POTENCY_LABELS = {
  'low': 'Low potency',
  'moderate': 'Moderate potency',
  'high': 'High potency',
};

function el(id) { return document.getElementById(id); }

function pairCardHTML(sp) {
  const emoji = EMOJI_FOR[sp.edibility] || '🍄';
  const img = sp.image
    ? `<img class="card-img" src="${sp.image.url}" alt="${escapeHTML(sp.name)}" loading="lazy" />`
    : `<div class="card-emoji">${emoji}</div>`;
  return `
    <div class="pair-side" data-id="${sp.id}" tabindex="0" role="button" aria-label="View ${escapeHTML(sp.name)} details">
      <div class="card-media">${img}</div>
      <h3>${escapeHTML(sp.name)}</h3>
      <p class="sci">${escapeHTML(sp.scientific_name)}</p>
      <span class="badge ${sp.edibility}">${sp.edibility}</span>
    </div>`;
}

function pairComparisonHTML(pair) {
  return `
    <article class="pair-card">
      <div class="pair-sides">
        ${pairCardHTML(pair.a)}
        <div class="pair-vs" aria-hidden="true">vs</div>
        ${pairCardHTML(pair.b)}
      </div>
      ${pair.distinguish ? `<p class="pair-distinguish"><b>How to tell them apart:</b> ${escapeHTML(pair.distinguish)}</p>` : ''}
    </article>`;
}

async function loadLookalikePairs() {
  const grid = el('lookalikes-grid');
  const countEl = el('lookalikes-count');
  grid.innerHTML = '';
  countEl.textContent = 'Loading…';
  try {
    const pairs = await fetchJSON('/api/lookalike-pairs');
    countEl.textContent = pairs.length
      ? `${pairs.length} dangerous look-alike pair${pairs.length === 1 ? '' : 's'}`
      : 'No dangerous look-alike pairs found in the current dataset.';
    grid.innerHTML = pairs.map(pairComparisonHTML).join('');
    grid.querySelectorAll('.pair-side').forEach(sideEl => {
      const open = () => openDetail(sideEl.dataset.id);
      sideEl.addEventListener('click', open);
      sideEl.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
      });
    });
  } catch (e) {
    countEl.textContent = 'Could not load look-alike pairs.';
    console.error(e);
  }
}

let lookalikesLoaded = false;
let mapInitialized = false;
let mapSelectedRegion = null; // null = all regions overview
let mapCounts = {};           // region -> species count
let mapAllSpecies = [];       // cached full species list for map mode
let mapGlobeLon0 = GLOBE.LON0; // rotatable yaw (degrees)

function setMode(mode) {
  const isSearch = mode === 'search';
  const isMap = mode === 'map';
  const isLookalikes = mode === 'lookalikes';

  el('search-mode-wrap').hidden = !isSearch;
  el('map-mode-wrap').hidden = !isMap;
  el('lookalikes-mode-wrap').hidden = !isLookalikes;

  el('mode-search-btn').classList.toggle('active', isSearch);
  el('mode-search-btn').setAttribute('aria-selected', String(isSearch));
  el('mode-map-btn').classList.toggle('active', isMap);
  el('mode-map-btn').setAttribute('aria-selected', String(isMap));
  el('mode-lookalikes-btn').classList.toggle('active', isLookalikes);
  el('mode-lookalikes-btn').setAttribute('aria-selected', String(isLookalikes));

  if (isLookalikes && !lookalikesLoaded) {
    lookalikesLoaded = true;
    loadLookalikePairs();
  }
  if (isMap) {
    ensureMapReady();
  }
}

/* ---- Region globe (educational continent ranges) ---- */
function normalizeRegion(r) {
  return r === 'na' ? 'north-america' : r;
}

function speciesRegions(sp) {
  const out = new Set();
  for (const r of (sp.regions || [])) {
    const n = normalizeRegion(r);
    if (n) out.add(n);
  }
  return out;
}

function buildMapCounts(list) {
  const counts = Object.fromEntries(MAP_REGIONS.map(r => [r, 0]));
  for (const sp of list) {
    const regs = speciesRegions(sp);
    // Count each species once per canonical region it belongs to.
    for (const r of regs) {
      if (r in counts) counts[r] += 1;
    }
  }
  return counts;
}

function regionFillIntensity(count, maxCount) {
  if (!maxCount || !count) return 0.12;
  // 0.18 .. 0.78 opacity band on mint fill
  return 0.18 + 0.6 * (count / maxCount);
}

function deg2rad(d) { return d * Math.PI / 180; }

/** Orthographic project lon/lat → SVG xy. Returns null if on the far side. */
function projectOrtho(lon, lat, lon0 = mapGlobeLon0, lat0 = GLOBE.LAT0) {
  const λ = deg2rad(lon - lon0);
  const φ = deg2rad(lat);
  const φ0 = deg2rad(lat0);
  const cosc = Math.sin(φ0) * Math.sin(φ) + Math.cos(φ0) * Math.cos(φ) * Math.cos(λ);
  if (cosc <= 0.02) return null; // back-face / limb cutoff
  const x = GLOBE.R * Math.cos(φ) * Math.sin(λ);
  const y = GLOBE.R * (Math.cos(φ0) * Math.sin(φ) - Math.sin(φ0) * Math.cos(φ) * Math.cos(λ));
  return { x: GLOBE.CX + x, y: GLOBE.CY - y, cosc };
}

/** Densify a lon/lat ring, drop back-face points, build an SVG path. */
function ringToPath(ring, stepsPerSeg = 6) {
  const pts = [];
  for (let i = 0; i < ring.length; i++) {
    const [lon1, lat1] = ring[i];
    const [lon2, lat2] = ring[(i + 1) % ring.length];
    for (let s = 0; s < stepsPerSeg; s++) {
      const t = s / stepsPerSeg;
      const lon = lon1 + (lon2 - lon1) * t;
      const lat = lat1 + (lat2 - lat1) * t;
      const p = projectOrtho(lon, lat);
      if (p) pts.push(p);
    }
  }
  if (pts.length < 3) return '';
  let d = `M${pts[0].x.toFixed(1)},${pts[0].y.toFixed(1)}`;
  for (let i = 1; i < pts.length; i++) {
    d += `L${pts[i].x.toFixed(1)},${pts[i].y.toFixed(1)}`;
  }
  return d + 'Z';
}

function graticulePaths() {
  const lines = [];
  // Parallels
  for (const lat of [-60, -30, 0, 30, 60]) {
    const pts = [];
    for (let lon = -180; lon <= 180; lon += 4) {
      const p = projectOrtho(lon, lat);
      if (p) pts.push(p);
      else if (pts.length > 1) {
        lines.push(ptsToPolyline(pts));
        pts.length = 0;
      } else {
        pts.length = 0;
      }
    }
    if (pts.length > 1) lines.push(ptsToPolyline(pts));
  }
  // Meridians
  for (let lon = -180; lon < 180; lon += 30) {
    const pts = [];
    for (let lat = -90; lat <= 90; lat += 3) {
      const p = projectOrtho(lon, lat);
      if (p) pts.push(p);
      else if (pts.length > 1) {
        lines.push(ptsToPolyline(pts));
        pts.length = 0;
      } else {
        pts.length = 0;
      }
    }
    if (pts.length > 1) lines.push(ptsToPolyline(pts));
  }
  return lines.join('');
}

function ptsToPolyline(pts) {
  let d = `M${pts[0].x.toFixed(1)},${pts[0].y.toFixed(1)}`;
  for (let i = 1; i < pts.length; i++) d += `L${pts[i].x.toFixed(1)},${pts[i].y.toFixed(1)}`;
  return `<path class="globe-graticule-line" d="${d}" fill="none"/>`;
}

function regionGlobeSVG(selected, counts) {
  const maxCount = Math.max(1, ...MAP_REGIONS.filter(r => r !== 'global').map(r => counts[r] || 0));
  const { CX, CY, R } = GLOBE;

  const paths = MAP_REGIONS.filter(r => r !== 'global').map(rid => {
    const d = ringToPath(REGION_RINGS[rid] || []);
    if (!d) return '';
    const count = counts[rid] || 0;
    const active = selected === rid;
    const opacity = active ? 0.92 : regionFillIntensity(count, maxCount);
    const label = REGION_LABELS[rid] || rid;
    return (
      `<path class="region-path${active ? ' active' : ''}" data-region="${rid}" ` +
      `d="${d}" style="--region-fill-opacity:${opacity.toFixed(3)}" ` +
      `tabindex="0" role="button" aria-label="${escapeHTML(label)}: ${count} species" ` +
      `aria-pressed="${active ? 'true' : 'false'}">` +
      `<title>${escapeHTML(label)} — ${count} species</title></path>`
    );
  }).join('');

  const globalActive = selected === 'global';
  const globalCount = counts.global || 0;
  const uid = 'g' + Math.random().toString(36).slice(2, 8);
  // Count how many continents are currently on the front face.
  const visibleFront = MAP_REGIONS.filter(r => r !== 'global' && ringToPath(REGION_RINGS[r] || [])).length;

  return `
    <div class="globe-frame">
    <svg class="region-globe-svg" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Orthographic globe of mushroom regions">
      <defs>
        <radialGradient id="${uid}-ocean" cx="38%" cy="32%" r="68%">
          <stop offset="0%" stop-color="#16324f"/>
          <stop offset="45%" stop-color="#0a1628"/>
          <stop offset="78%" stop-color="#050b14"/>
          <stop offset="100%" stop-color="#02050a"/>
        </radialGradient>
        <radialGradient id="${uid}-shine" cx="32%" cy="28%" r="55%">
          <stop offset="0%" stop-color="rgba(180,230,255,0.22)"/>
          <stop offset="35%" stop-color="rgba(110,180,255,0.06)"/>
          <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
        </radialGradient>
        <radialGradient id="${uid}-limb" cx="50%" cy="50%" r="50%">
          <stop offset="70%" stop-color="rgba(0,0,0,0)"/>
          <stop offset="92%" stop-color="rgba(0,0,0,0.35)"/>
          <stop offset="100%" stop-color="rgba(0,0,0,0.65)"/>
        </radialGradient>
        <filter id="${uid}-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3.5" result="b"/>
          <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        <clipPath id="${uid}-clip">
          <circle cx="${CX}" cy="${CY}" r="${R}"/>
        </clipPath>
      </defs>

      <!-- faint outer atmosphere -->
      <circle class="globe-halo" cx="${CX}" cy="${CY}" r="${R + 18}"/>
      <circle class="globe-disc" cx="${CX}" cy="${CY}" r="${R}" fill="url(#${uid}-ocean)"/>

      <g clip-path="url(#${uid}-clip)">
        <g class="globe-grid" opacity="0.22">${graticulePaths()}</g>
        <g class="region-layer" filter="url(#${uid}-glow)">${paths}</g>
        <!-- specular highlight + limb darkening for sphere read -->
        <circle cx="${CX}" cy="${CY}" r="${R}" fill="url(#${uid}-shine)" pointer-events="none"/>
        <circle cx="${CX}" cy="${CY}" r="${R}" fill="url(#${uid}-limb)" pointer-events="none"/>
      </g>

      <circle class="globe-rim" cx="${CX}" cy="${CY}" r="${R}"/>
      <!-- tiny terminator crescent -->
      <path class="globe-terminator" d="M${CX - R * 0.15},${CY - R * 0.96}
        A ${R},${R} 0 0 0 ${CX - R * 0.15},${CY + R * 0.96}" fill="none"/>
    </svg>
    <div class="globe-controls" role="group" aria-label="Rotate globe">
      <button type="button" class="globe-rot-btn" id="globe-rot-left" title="Rotate west" aria-label="Rotate globe west">⟲</button>
      <button type="button" class="globe-rot-btn" id="globe-rot-reset" title="Reset view" aria-label="Reset globe view">◎</button>
      <button type="button" class="globe-rot-btn" id="globe-rot-right" title="Rotate east" aria-label="Rotate globe east">⟳</button>
    </div>
    <p class="globe-hint">${visibleFront < 6 ? 'Spin the globe to bring other continents into view.' : 'Click a lit continent to filter.'}</p>
    </div>
    <button type="button" class="global-chip${globalActive ? ' active' : ''}" id="map-global-btn"
      aria-pressed="${globalActive ? 'true' : 'false'}"
      title="Species tagged global / widespread">
      🌐 Global / widespread <span class="global-count">${globalCount}</span>
    </button>
  `;
}

function bindRegionGlobeHandlers(root) {
  root.querySelectorAll('.region-path').forEach(pathEl => {
    const pick = () => selectMapRegion(pathEl.dataset.region);
    pathEl.addEventListener('click', pick);
    pathEl.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); }
    });
  });
  const gBtn = root.querySelector('#map-global-btn');
  if (gBtn) {
    gBtn.addEventListener('click', () => selectMapRegion('global'));
  }
  const left = root.querySelector('#globe-rot-left');
  const right = root.querySelector('#globe-rot-right');
  const reset = root.querySelector('#globe-rot-reset');
  if (left) left.addEventListener('click', () => rotateGlobe(-30));
  if (right) right.addEventListener('click', () => rotateGlobe(30));
  if (reset) reset.addEventListener('click', () => {
    mapGlobeLon0 = GLOBE.LON0;
    renderMapGlobe();
  });

  // Drag starts on the SVG; move/up handled at window level so re-renders
  // during spin don't drop the gesture.
  const svg = root.querySelector('.region-globe-svg');
  if (svg) {
    svg.style.touchAction = 'none';
    svg.addEventListener('pointerdown', (e) => {
      if (e.target && e.target.classList && e.target.classList.contains('region-path')) return;
      if (e.button != null && e.button !== 0) return;
      globeDrag = { lastX: e.clientX, moved: false };
      try { svg.setPointerCapture(e.pointerId); } catch (_) { /* ignore */ }
    });
  }
}

// Module-level drag state survives re-renders of the globe SVG.
let globeDrag = null;
let globeDragRaf = 0;

function onGlobePointerMove(e) {
  if (!globeDrag) return;
  const dx = e.clientX - globeDrag.lastX;
  if (Math.abs(dx) < 1) return;
  globeDrag.lastX = e.clientX;
  globeDrag.moved = true;
  // Drag right → rotate west (natural globe feel).
  mapGlobeLon0 = ((mapGlobeLon0 - dx * 0.5) % 360 + 540) % 360 - 180;
  if (!globeDragRaf) {
    globeDragRaf = requestAnimationFrame(() => {
      globeDragRaf = 0;
      renderMapGlobe();
    });
  }
}

function onGlobePointerUp() {
  globeDrag = null;
}

if (typeof window !== 'undefined') {
  window.addEventListener('pointermove', onGlobePointerMove);
  window.addEventListener('pointerup', onGlobePointerUp);
  window.addEventListener('pointercancel', onGlobePointerUp);
}

function rotateGlobe(deltaDeg) {
  mapGlobeLon0 = ((mapGlobeLon0 + deltaDeg) % 360 + 540) % 360 - 180;
  renderMapGlobe();
}

// Approximate centroid lon for each region (for auto-facing the globe).
const REGION_FOCUS_LON = {
  'north-america': -100,
  'south-america': -60,
  'europe': 15,
  'africa': 20,
  'asia': 100,
  'oceania': 135,
  'global': GLOBE.LON0,
};

function faceRegion(region) {
  if (!region || region === 'global') return;
  const target = REGION_FOCUS_LON[region];
  if (target == null) return;
  mapGlobeLon0 = target;
}

function renderRegionChips(selected, counts) {
  const wrap = el('map-region-chips');
  if (!wrap) return;
  wrap.innerHTML = MAP_REGIONS.map(rid => {
    const label = REGION_LABELS[rid] || rid;
    const count = counts[rid] || 0;
    const active = selected === rid;
    return `<button type="button" class="map-chip${active ? ' active' : ''}" data-region="${rid}">` +
      `${escapeHTML(label)} <span class="map-chip-count">${count}</span></button>`;
  }).join('') +
    `<button type="button" class="map-chip map-chip-clear${selected ? '' : ' active'}" data-region="">All regions</button>`;

  wrap.querySelectorAll('.map-chip').forEach(btn => {
    btn.addEventListener('click', () => {
      const r = btn.dataset.region;
      selectMapRegion(r || null);
    });
  });
}

function renderMapGlobe() {
  const host = el('region-globe');
  if (!host) return;
  host.innerHTML = regionGlobeSVG(mapSelectedRegion, mapCounts);
  bindRegionGlobeHandlers(host);
  renderRegionChips(mapSelectedRegion, mapCounts);
}

function mapSpeciesForRegion(region) {
  if (!region) return mapAllSpecies.slice();
  return mapAllSpecies.filter(sp => speciesRegions(sp).has(region));
}

function renderMapSpeciesList(region) {
  const list = mapSpeciesForRegion(region);
  // Stable A–Z
  list.sort((a, b) => (a.name || '').localeCompare(b.name || ''));

  const title = el('map-region-title');
  const sub = el('map-region-sub');
  const countEl = el('map-species-count');
  const grid = el('map-species-grid');
  const empty = el('map-no-results');

  if (!region) {
    title.textContent = 'All regions';
    sub.textContent = 'Click a continent (or Global) to filter the index by range.';
  } else {
    title.textContent = REGION_LABELS[region] || region;
    sub.textContent = region === 'global'
      ? 'Species tagged as global / widespread in the dataset.'
      : 'Species whose educational range includes this region.';
  }
  countEl.textContent = list.length
    ? `${list.length} species`
    : '';

  if (!list.length) {
    grid.innerHTML = '';
    empty.hidden = false;
    return;
  }
  empty.hidden = true;
  // Cap initial paint for huge "all" views; still show full region subsets.
  const SHOW = region ? list.length : Math.min(list.length, 48);
  const slice = list.slice(0, SHOW);
  grid.innerHTML = slice.map(cardHTML).join('') +
    (!region && list.length > SHOW
      ? `<p class="map-more-hint">Showing ${SHOW} of ${list.length}. Pick a region to narrow the list.</p>`
      : '');

  grid.querySelectorAll('.card').forEach(card => {
    const open = () => openDetail(card.dataset.id);
    card.addEventListener('click', open);
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
    });
  });
}

function selectMapRegion(region) {
  // Toggle off if re-clicking the active region.
  if (region && mapSelectedRegion === region) {
    mapSelectedRegion = null;
  } else {
    mapSelectedRegion = region || null;
    if (mapSelectedRegion) faceRegion(mapSelectedRegion);
  }
  renderMapGlobe();
  renderMapSpeciesList(mapSelectedRegion);

  // Keep search-mode region filter in sync so switching back preserves context.
  if (mapSelectedRegion && mapSelectedRegion !== 'global') {
    state.filters.regions = [mapSelectedRegion];
  } else if (mapSelectedRegion === 'global') {
    state.filters.regions = ['global'];
  }
  // Don't clear filters on "all regions" — user may have other trait filters.
}

async function ensureMapReady() {
  if (!mapInitialized) {
    try {
      mapAllSpecies = await fetchJSON('/api/species');
      mapCounts = buildMapCounts(mapAllSpecies);
      mapInitialized = true;
    } catch (e) {
      console.error('map load failed', e);
      el('map-species-count').textContent = 'Could not load species for the map.';
      return;
    }
  }
  renderMapGlobe();
  renderMapSpeciesList(mapSelectedRegion);
}

function detailRegionMapHTML(regions) {
  const regs = new Set((regions || []).map(normalizeRegion));
  if (!regs.size) return '';

  const { CX, CY, R } = GLOBE;
  const uid = 'd' + Math.random().toString(36).slice(2, 8);
  const paths = MAP_REGIONS.filter(r => r !== 'global').map(rid => {
    const d = ringToPath(REGION_RINGS[rid] || []);
    if (!d) return '';
    const on = regs.has(rid) || regs.has('global');
    return `<path class="detail-region-path${on ? ' on' : ''}" d="${d}"></path>`;
  }).join('');

  const labels = [...regs].map(r => REGION_LABELS[r] || r).join(' · ');

  return `
    <div class="detail-section detail-map-section">
      <h4>Where found (broad regions)</h4>
      <div class="detail-region-map" aria-label="Region map: ${escapeHTML(labels)}">
        <svg viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <radialGradient id="${uid}-ocean" cx="38%" cy="32%" r="68%">
              <stop offset="0%" stop-color="#16324f"/>
              <stop offset="55%" stop-color="#0a1628"/>
              <stop offset="100%" stop-color="#02050a"/>
            </radialGradient>
            <clipPath id="${uid}-clip"><circle cx="${CX}" cy="${CY}" r="${R}"/></clipPath>
          </defs>
          <circle cx="${CX}" cy="${CY}" r="${R}" fill="url(#${uid}-ocean)" class="detail-globe-disc"/>
          <g clip-path="url(#${uid}-clip)">${paths}</g>
          <circle cx="${CX}" cy="${CY}" r="${R}" class="detail-globe-rim" fill="none"/>
        </svg>
      </div>
      <p class="detail-map-note">Educational range tags only — not a precise occurrence or forage map. ${escapeHTML(labels)}</p>
    </div>`;
}

/* ---- "What's fruiting near me now" quick-filter ----
   Northern Hemisphere month->season mapping assumed here (spring: Mar-May,
   summer: Jun-Aug, autumn: Sep-Nov, winter: Dec-Feb). Good enough for a
   quick client-side default; users in the Southern Hemisphere can still
   pick season manually via the sidebar's full Season filter. */
function currentSeasonNorthernHemisphere(date = new Date()) {
  const month = date.getMonth(); // 0-11
  if (month >= 2 && month <= 4) return 'spring';
  if (month >= 5 && month <= 7) return 'summer';
  if (month >= 8 && month <= 10) return 'autumn';
  return 'winter';
}

function initQuickFilter(facets) {
  const season = currentSeasonNorthernHemisphere();
  const seasonBtn = el('qf-season-btn');
  const seasonLabel = el('qf-season-label');
  const regionSelect = el('qf-region-select');
  const applyBtn = el('qf-apply-btn');

  seasonLabel.textContent = season.charAt(0).toUpperCase() + season.slice(1);
  let seasonSelected = true; // "This season" is on by default

  function refreshSeasonBtn() {
    seasonBtn.classList.toggle('active', seasonSelected);
  }
  refreshSeasonBtn();
  seasonBtn.addEventListener('click', () => {
    seasonSelected = !seasonSelected;
    refreshSeasonBtn();
  });

  // Populate the region dropdown from the same vocabulary as the sidebar's
  // regions facet (array of {value, label}).
  const regions = facets.regions || [];
  for (const r of regions) {
    const opt = document.createElement('option');
    opt.value = r.value;
    opt.textContent = r.label;
    regionSelect.appendChild(opt);
  }

  applyBtn.addEventListener('click', () => {
    // Switch to the normal search/filter view and apply via the same
    // filter-application state/rendering path as the sidebar chips.
    setMode('search');
    if (seasonSelected) {
      state.filters.season = season;
    } else {
      delete state.filters.season;
    }
    const region = regionSelect.value;
    if (region) {
      state.filters.regions = [region];
    } else {
      delete state.filters.regions;
    }
    renderFilters(facets);
    refresh();
  });
}

async function fetchJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error('Request failed: ' + res.status);
  return res.json();
}

function buildQueryString() {
  const p = new URLSearchParams();
  if (state.q) p.set('q', state.q);
  for (const [k, v] of Object.entries(state.filters)) {
    if (!v) continue;
    if (Array.isArray(v)) {
      if (v.length) p.set(k, v.join(','));
    } else {
      p.set(k, v);
    }
  }
  if (state.sort !== 'name') p.set('sort', state.sort);
  return p.toString();
}

/* Which filter-group titles the user has manually collapsed, so re-renders
   (e.g. after clicking a chip) don't snap sections back open. */
const collapsedGroups = new Set();

// Start with all filter groups collapsed by default
FILTER_DEFS.forEach(def => collapsedGroups.add(def.key));

/* ---- Render filters from facets ---- */
function renderFilters(facets) {
  const wrap = el('filter-groups');
  wrap.innerHTML = '';
  for (const def of FILTER_DEFS) {
    const values = facets[def.key] || [];
    if (!values.length) continue;
    const isMulti = MULTI_KEYS.has(def.key);
    const isCollapsed = collapsedGroups.has(def.key);
    const group = document.createElement('div');
    group.className = 'filter-group' + (isCollapsed ? ' collapsed' : '');

    const title = document.createElement('button');
    title.type = 'button';
    title.className = 'fg-title';
    title.setAttribute('aria-expanded', String(!isCollapsed));
    const activeVal = state.filters[def.key];
    const activeCount = isMulti ? (activeVal || []).length : (activeVal ? 1 : 0);
    title.innerHTML =
      `<span>${def.title}</span>` +
      (activeCount ? `<span class="fg-count">${activeCount} selected</span>` : '') +
      `<span class="fg-caret" aria-hidden="true">▾</span>`;
    title.addEventListener('click', () => {
      const nowCollapsed = group.classList.toggle('collapsed');
      title.setAttribute('aria-expanded', String(!nowCollapsed));
      if (nowCollapsed) collapsedGroups.add(def.key);
      else collapsedGroups.delete(def.key);
    });
    group.appendChild(title);

    const row = document.createElement('div');
    row.className = 'chip-row';
    for (const v of values) {
      // Facet values are strings, except `edibility`/`potency`/`regions`
      // which are {value, label}.
      const isObj = v && typeof v === 'object';
      const val = isObj ? v.value : v;
      const label = isObj ? v.label
        : (def.key === 'gill_attachment' ? (GILL_LABELS[v] || v) : v);
      const chip = document.createElement('span');
      const edClass = def.key === 'edibility' ? ' ed-' + val : '';
      const potClass = def.key === 'potency' ? ' pot-' + val : '';
      const isActive = isMulti
        ? (state.filters[def.key] || []).includes(val)
        : state.filters[def.key] === val;
      chip.className = 'chip' + edClass + potClass + (isActive ? ' active' : '');
      chip.textContent = label;
      chip.addEventListener('click', () => {
        if (isMulti) {
          const current = new Set(state.filters[def.key] || []);
          if (current.has(val)) current.delete(val);
          else current.add(val);
          if (current.size) state.filters[def.key] = Array.from(current);
          else delete state.filters[def.key];
        } else {
          // single-select toggle
          if (state.filters[def.key] === val) delete state.filters[def.key];
          else state.filters[def.key] = val;
        }
        renderFilters(facets); // refresh active states
        refresh();
      });
      row.appendChild(chip);
    }
    group.appendChild(row);
    wrap.appendChild(group);
  }
}

/* ---- Render a single result card ---- */
function cardHTML(s) {
  const emoji = EMOJI_FOR[s.edibility] || '🍄';
  const colors = (s.cap && s.cap.colors || []).slice(0, 3)
    .map(c => `<span class="tag cap-color">${c}</span>`).join('');
  const img = s.image
    ? `<img class="card-img" src="${s.image.url}" alt="${escapeHTML(s.name)}" loading="lazy" />`
    : `<div class="card-emoji">${emoji}</div>`;
  const potencyBadge = s.potency
    ? `<span class="badge-potency pot-${s.potency}" title="Psychoactive potency (see detail for sourcing)">${POTENCY_LABELS[s.potency] || s.potency}</span>`
    : '';
  return `
    <article class="card" data-id="${s.id}" tabindex="0">
      <div class="card-media">${img}</div>
      <h3>${escapeHTML(s.name)}</h3>
      <p class="sci">${escapeHTML(s.scientific_name)}</p>
      <span class="badge ${s.edibility}">${s.edibility}</span>${potencyBadge}
      <div class="traits">${colors}
        <span class="tag">${escapeHTML(s.habitat || '—')}</span>
      </div>
    </article>`;
}

function escapeHTML(str) {
  return String(str).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

/* ---- Render the results grid, batched with a "Load more" control ---- */
const PAGE_SIZE = 24;
let currentResults = [];
let shownCount = 0;

function renderResults(list) {
  currentResults = list;
  shownCount = 0;
  const countEl = el('result-count');
  countEl.textContent = list.length;
  if (!list.length) {
    el('results-grid').innerHTML = '';
    el('no-results').hidden = false;
    removePager();
    return;
  }
  el('no-results').hidden = true;
  el('results-grid').innerHTML = '';
  renderNextPage();
}

function renderNextPage() {
  const grid = el('results-grid');
  const nextSlice = currentResults.slice(shownCount, shownCount + PAGE_SIZE);
  const frag = document.createElement('div');
  frag.innerHTML = nextSlice.map(cardHTML).join('');
  while (frag.firstChild) grid.appendChild(frag.firstChild);
  shownCount += nextSlice.length;

  grid.querySelectorAll('.card:not([data-bound])').forEach(card => {
    card.dataset.bound = '1';
    const open = () => openDetail(card.dataset.id);
    card.addEventListener('click', open);
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
    });
  });

  renderPager();
}

function removePager() {
  const existing = el('load-more-wrap');
  if (existing) existing.remove();
}

function renderPager() {
  removePager();
  const resultsSection = document.querySelector('.results');
  const remaining = currentResults.length - shownCount;
  const wrap = document.createElement('div');
  wrap.id = 'load-more-wrap';
  wrap.className = 'load-more-wrap';
  if (remaining > 0) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'load-more-btn';
    btn.textContent = `Load more (${remaining} more species)`;
    btn.addEventListener('click', () => {
      renderNextPage();
    });
    wrap.appendChild(btn);
  } else if (currentResults.length > PAGE_SIZE) {
    const status = document.createElement('p');
    status.className = 'pagination-status';
    status.textContent = `Showing all ${currentResults.length} species.`;
    wrap.appendChild(status);
  }
  if (wrap.childNodes.length) resultsSection.appendChild(wrap);
}

/* ---- Detail modal ---- */
async function openDetail(id) {
  try {
    const s = await fetchJSON('/api/species/' + encodeURIComponent(id));
    el('detail-content').innerHTML = detailHTML(s);
    el('detail-overlay').hidden = false;
    document.body.style.overflow = 'hidden';
  } catch (e) {
    console.error(e);
  }
}

function detailHTML(s) {
  const emoji = EMOJI_FOR[s.edibility] || '🍄';
  const cap = s.cap || {};
  const gills = s.gills || {};
  const stem = s.stem || {};
  const rows = [
    ['Cap shape', (cap.shape || []).join(', ')],
    ['Cap diameter', cap.diameter_cm ? cap.diameter_cm.join('–') + ' cm' : '—'],
    ['Gills / pores', gills.attachment || '—'],
    ['Gill spacing', gills.spacing !== 'n/a' ? gills.spacing : '—'],
    ['Stem', (stem.colors && stem.colors.join(', ')) || '—' + (stem.ring ? ' · ring' : '') + (stem.volva ? ' · volva' : '')],
    ['Spore print', s.spore_print || '—'],
    ['Habitat', s.habitat || '—'],
    ['Substrate', s.substrate || '—'],
    ['Ecology', s.ecology || '—'],
    ['Season', (s.season || []).join(', ')],
    ['Distribution', s.distribution || '—'],
    ['Regions', (s.regions || []).map(r => REGION_LABELS[r] || r).join(', ') || '—'],
  ];
  const specs = rows.map(([k, v]) =>
    `<tr><td>${k}</td><td>${escapeHTML(v)}</td></tr>`).join('');

  const look = (s.lookalikes || []).map(l => {
    const nameHTML = l.link
      ? `<a class="lookalike-link" href="#" data-id="${escapeHTML(l.link)}" title="View ${escapeHTML(l.name)}">${escapeHTML(l.name)} ↗</a>`
      : `<b>${escapeHTML(l.name)}</b>`;
    return `<div class="lookalike">${nameHTML}<br>${escapeHTML(l.distinguish)}</div>`;
  }).join('');

  const aliases = (s.aliases || []).length
    ? `<p>${s.aliases.map(escapeHTML).join(' · ')}</p>` : '';

  const hero = s.image
    ? `<img class="detail-img" src="${s.image.url}" alt="${escapeHTML(s.name)}" />
       <p class="photo-credit">Photo: ${escapeHTML(s.image.credit || 'iNaturalist contributor')}
         (${escapeHTML(s.image.license || 'CC')}) via ${escapeHTML(s.image.source || 'iNaturalist')}.</p>`
    : `<div class="detail-emoji">${emoji}</div>`;

  const potencyBadge = s.potency
    ? `<span class="badge-potency pot-${s.potency}" style="margin-left:8px" title="Psychoactive potency">${POTENCY_LABELS[s.potency] || s.potency}</span>`
    : '';

  return `
    <div class="detail-head">
      <div>
        <h2 id="detail-name">${escapeHTML(s.name)}</h2>
        <div class="sci">${escapeHTML(s.scientific_name)}</div>
      </div>
      <span class="badge ${s.edibility}" style="margin-left:auto">${s.edibility}</span>${potencyBadge}
    </div>
    <div class="detail-hero">${hero}</div>
    <div class="detail-section">
      <h4>Also known as</h4>
      ${aliases || '<p style="color:var(--ink-dim)">—</p>'}
    </div>
    <div class="detail-section">
      <h4>Description</h4>
      <p>${escapeHTML(s.description || '')}</p>
    </div>
    <div class="detail-section">
      <h4>Traits</h4>
      <table class="spec-table">${specs}</table>
    </div>
    ${detailRegionMapHTML(s.regions)}
    ${look ? `<div class="detail-section"><h4>Look-alikes & how to tell them apart</h4>${look}</div>` : ''}
    ${s.fun_fact ? `<div class="fun-fact">🧠 ${escapeHTML(s.fun_fact)}</div>` : ''}
  `;
}

function closeDetail() {
  el('detail-overlay').hidden = true;
  document.body.style.overflow = '';
}

/* ---- Photo identify (local visual-similarity, not identification) ---- */
function initIdentify() {
  const input = el('identify-input');
  const btn = el('identify-btn');
  const removeBtn = el('identify-remove');
  const fname = el('identify-filename');
  const preview = el('identify-preview');
  const previewImg = el('identify-preview-img');
  const note = el('identify-note');
  const results = el('identify-results');
  let pendingFile = null;

  // Reset everything back to the empty/choose state.
  function resetIdentify() {
    pendingFile = null;
    input.value = '';
    fname.textContent = '';
    preview.hidden = true;
    previewImg.removeAttribute('src');
    removeBtn.hidden = true;
    btn.disabled = true;
    note.hidden = true;
    results.hidden = true;
    results.innerHTML = '';
  }

  input.addEventListener('change', () => {
    const f = input.files && input.files[0];
    pendingFile = f || null;
    if (!f) {
      resetIdentify();
      return;
    }
    fname.textContent = f.name;
    removeBtn.hidden = false;
    btn.disabled = false;
    preview.hidden = false;
    const reader = new FileReader();
    reader.onload = e => { previewImg.src = e.target.result; };
    reader.readAsDataURL(f);
    results.hidden = true;
    results.innerHTML = '';
    note.hidden = true;
  });

  removeBtn.addEventListener('click', resetIdentify);

  btn.addEventListener('click', async () => {
    if (!pendingFile) return;
    btn.disabled = true;
    btn.textContent = 'Matching…';
    note.hidden = false;
    note.textContent = 'Analyzing photo…';
    try {
      const fd = new FormData();
      fd.append('image', pendingFile);
      const res = await fetch('/api/identify', { method: 'POST', body: fd });
      if (!res.ok) throw new Error('Identify failed: ' + res.status);
      const data = await res.json();
      const list = data.results || [];
      const method = data.method || 'local';
      results.innerHTML = list.map(r => identifyCardHTML(r, method)).join('');
      results.hidden = false;
      note.hidden = false;
      if (!list.length) {
        note.textContent = 'No indexed photos to compare against.';
      } else if (method === 'ai') {
        note.innerHTML = 'Top matches from an <b>AI visual assessment</b> against our indexed species. ' +
          'This is <b>not</b> an identification — confirm with an expert before touching anything.';
      } else {
        note.innerHTML = 'Top matches by <b>visual similarity</b> (colour/texture). ' +
          'This is <b>not</b> an identification — confirm with an expert.';
      }
      results.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => openDetail(card.dataset.id));
      });
    } catch (e) {
      note.hidden = false;
      note.textContent = 'Could not process that photo. Try a different image.';
      console.error(e);
    } finally {
      btn.disabled = false;
      btn.textContent = 'Find similar';
    }
  });
}

function identifyCardHTML(r, method) {
  const emoji = EMOJI_FOR[r.edibility] || '🍄';
  const img = r.image
    ? `<img class="card-img" src="${r.image.url}" alt="${escapeHTML(r.name)}" loading="lazy" />`
    : `<div class="card-emoji">${emoji}</div>`;
  let tagHTML;
  if (method === 'ai') {
    const pct = Math.round((r.confidence || 0) * 100);
    const reasonTag = r.reasoning
      ? `<span class="tag" title="${escapeHTML(r.reasoning)}">${escapeHTML(r.reasoning)}</span>`
      : '';
    tagHTML = `<span class="tag">${pct}% confidence</span>${reasonTag}`;
  } else {
    const pct = Math.round((r.similarity || 0) * 100);
    tagHTML = `<span class="tag">${pct}% similar</span>`;
  }
  return `
    <article class="card" data-id="${r.id}" tabindex="0">
      <div class="card-media">${img}</div>
      <h3>${escapeHTML(r.name)}</h3>
      <p class="sci">${escapeHTML(r.scientific_name)}</p>
      <span class="badge ${r.edibility}">${r.edibility}</span>
      <div class="traits">${tagHTML}</div>
    </article>`;
}

/* ---- Orchestration ---- */
async function refresh() {
  const qs = buildQueryString();
  try {
    const list = await fetchJSON('/api/species' + (qs ? '?' + qs : ''));
    renderResults(list);
  } catch (e) {
    console.error('refresh failed', e);
  }
}

async function init() {
  // footer count
  try {
    const all = await fetchJSON('/api/species');
    document.querySelector('.site-footer p').innerHTML =
      `The Spore Drop Index · ${all.length} species · Educational reference from the Spore Drop newsletter.`;
  } catch (e) {}

  try {
    const facets = await fetchJSON('/api/facets');
    renderFilters(facets);
    initQuickFilter(facets);
  } catch (e) { console.error(e); }

  await refresh();

  el('search-form').addEventListener('submit', e => {
    e.preventDefault();
    state.q = el('search-input').value.trim();
    refresh();
  });
  el('search-input').addEventListener('input', () => {
    // gentle debounce
    clearTimeout(window.__t);
    window.__t = setTimeout(() => {
      state.q = el('search-input').value.trim();
      refresh();
    }, 250);
  });
  el('clear-btn').addEventListener('click', async () => {
    state.q = '';
    state.filters = {};
    state.sort = 'name';
    el('search-input').value = '';
    el('sort-select').value = 'name';
    try {
      const facets = await fetchJSON('/api/facets');
      renderFilters(facets);
    } catch (e) {}
    refresh();
  });
  el('sort-select').addEventListener('change', e => {
    state.sort = e.target.value;
    refresh();
  });
  el('detail-close').addEventListener('click', closeDetail);
  el('detail-overlay').addEventListener('click', e => {
    if (e.target === el('detail-overlay')) closeDetail();
  });
  // Lookalike links navigate to that species' detail view (modal stays open).
  el('detail-content').addEventListener('click', e => {
    const a = e.target.closest('.lookalike-link');
    if (a) {
      e.preventDefault();
      openDetail(a.dataset.id);
      el('detail-content').scrollTop = 0;
    }
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeDetail();
  });

  el('mode-search-btn').addEventListener('click', () => {
    setMode('search');
    // If map set a region filter, refresh search results to match.
    refresh();
    // Re-paint chips so region selection from the globe shows as active.
    fetchJSON('/api/facets').then(renderFilters).catch(() => {});
  });
  el('mode-map-btn').addEventListener('click', () => setMode('map'));
  el('mode-lookalikes-btn').addEventListener('click', () => setMode('lookalikes'));

  // Photo identify panel (local visual-similarity, never an identification).
  initIdentify();

  // Per-species permalink deep-link: app.py's /species/<id> route stamps
  // window.__DEEPLINK_SPECIES_ID before this script loads. Open that
  // species' detail modal on boot so the SPA lands on the right view.
  if (window.__DEEPLINK_SPECIES_ID) {
    openDetail(window.__DEEPLINK_SPECIES_ID);
  }

  // Mobile filter toggle: collapse the filter panel by default on small screens
  // so the results show first; the "Filters" button expands it.
  const filtersEl = el('filters');
  const toggle = el('filters-toggle');
  if (toggle) {
    const isMobile = window.matchMedia('(max-width: 820px)').matches;
    if (isMobile) filtersEl.classList.add('collapsed');
    toggle.setAttribute('aria-expanded', String(!filtersEl.classList.contains('collapsed')));
    toggle.addEventListener('click', () => {
      const collapsed = filtersEl.classList.toggle('collapsed');
      toggle.setAttribute('aria-expanded', String(!collapsed));
      toggle.textContent = collapsed ? 'Filters ▾' : 'Filters ▴';
    });
  }
}

document.addEventListener('DOMContentLoaded', init);
