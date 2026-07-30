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

function setMode(mode) {
  const isLookalikes = mode === 'lookalikes';
  el('search-mode-wrap').hidden = isLookalikes;
  el('lookalikes-mode-wrap').hidden = !isLookalikes;
  el('mode-search-btn').classList.toggle('active', !isLookalikes);
  el('mode-search-btn').setAttribute('aria-selected', String(!isLookalikes));
  el('mode-lookalikes-btn').classList.toggle('active', isLookalikes);
  el('mode-lookalikes-btn').setAttribute('aria-selected', String(isLookalikes));
  if (isLookalikes && !lookalikesLoaded) {
    lookalikesLoaded = true;
    loadLookalikePairs();
  }
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

  el('mode-search-btn').addEventListener('click', () => setMode('search'));
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
