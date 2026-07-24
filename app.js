/* Mushroom Search Index - frontend logic */
'use strict';

const state = {
  q: '',
  filters: {},   // key -> value (single-select chips)
  sort: 'name',
};

const stateKey = (k) => k;
const FILTER_DEFS = [
  { key: 'edibility', title: 'Edibility' },
  { key: 'habitat', title: 'Habitat' },
  { key: 'substrate', title: 'Substrate' },
  { key: 'ecology', title: 'Ecology' },
  { key: 'spore_print', title: 'Spore print' },
  { key: 'cap_color', title: 'Cap color' },
  { key: 'gill_attachment', title: 'Gills / pores' },
  { key: 'season', title: 'Season' },
];

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

function el(id) { return document.getElementById(id); }

async function fetchJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error('Request failed: ' + res.status);
  return res.json();
}

function buildQueryString() {
  const p = new URLSearchParams();
  if (state.q) p.set('q', state.q);
  for (const [k, v] of Object.entries(state.filters)) {
    if (v) p.set(k, v);
  }
  if (state.sort !== 'name') p.set('sort', state.sort);
  return p.toString();
}

/* ---- Render filters from facets ---- */
function renderFilters(facets) {
  const wrap = el('filter-groups');
  wrap.innerHTML = '';
  for (const def of FILTER_DEFS) {
    const values = facets[def.key] || [];
    if (!values.length) continue;
    const group = document.createElement('div');
    group.className = 'filter-group';
    const title = document.createElement('div');
    title.className = 'fg-title';
    title.textContent = def.title;
    group.appendChild(title);

    const row = document.createElement('div');
    row.className = 'chip-row';
    for (const v of values) {
      // Facet values are strings, except `edibility` which is {value, label}.
      const isObj = v && typeof v === 'object';
      const val = isObj ? v.value : v;
      const label = isObj ? v.label
        : (def.key === 'gill_attachment' ? (GILL_LABELS[v] || v) : v);
      const chip = document.createElement('span');
      const edClass = def.key === 'edibility' ? ' ed-' + val : '';
      chip.className = 'chip' + edClass + (state.filters[def.key] === val ? ' active' : '');
      chip.textContent = label;
      chip.addEventListener('click', () => {
        // single-select toggle
        if (state.filters[def.key] === val) delete state.filters[def.key];
        else state.filters[def.key] = val;
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
  return `
    <article class="card" data-id="${s.id}" tabindex="0">
      <div class="card-media">${img}</div>
      <h3>${escapeHTML(s.name)}</h3>
      <p class="sci">${escapeHTML(s.scientific_name)}</p>
      <span class="badge ${s.edibility}">${s.edibility}</span>
      <div class="traits">${colors}
        <span class="tag">${escapeHTML(s.habitat || '—')}</span>
      </div>
    </article>`;
}

function escapeHTML(str) {
  return String(str).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

/* ---- Render the results grid ---- */
function renderResults(list) {
  const grid = el('results-grid');
  const countEl = el('result-count');
  countEl.textContent = list.length;
  if (!list.length) {
    grid.innerHTML = '';
    el('no-results').hidden = false;
    return;
  }
  el('no-results').hidden = true;
  grid.innerHTML = list.map(cardHTML).join('');
  grid.querySelectorAll('.card').forEach(card => {
    const open = () => openDetail(card.dataset.id);
    card.addEventListener('click', open);
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
    });
  });
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
  ];
  const specs = rows.map(([k, v]) =>
    `<tr><td>${k}</td><td>${escapeHTML(v)}</td></tr>`).join('');

  const look = (s.lookalikes || []).map(l =>
    `<div class="lookalike"><b>${escapeHTML(l.name)}</b><br>${escapeHTML(l.distinguish)}</div>`).join('');

  const aliases = (s.aliases || []).length
    ? `<p>${s.aliases.map(escapeHTML).join(' · ')}</p>` : '';

  const hero = s.image
    ? `<img class="detail-img" src="${s.image.url}" alt="${escapeHTML(s.name)}" />
       <p class="photo-credit">Photo: ${escapeHTML(s.image.credit || 'iNaturalist contributor')}
         (${escapeHTML(s.image.license || 'CC')}) via ${escapeHTML(s.image.source || 'iNaturalist')}.</p>`
    : `<div class="detail-emoji">${emoji}</div>`;

  return `
    <div class="detail-head">
      <div>
        <h2 id="detail-name">${escapeHTML(s.name)}</h2>
        <div class="sci">${escapeHTML(s.scientific_name)}</div>
      </div>
      <span class="badge ${s.edibility}" style="margin-left:auto">${s.edibility}</span>
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
      `Mushroom Search Index · ${all.length} species · A Hermes-built educational reference.`;
  } catch (e) {}

  try {
    const facets = await fetchJSON('/api/facets');
    renderFilters(facets);
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
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeDetail();
  });
}

document.addEventListener('DOMContentLoaded', init);
