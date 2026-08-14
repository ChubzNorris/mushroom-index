const fs = require('fs');
const vm = require('vm');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(/if \(document\.readyState[\s\S]*$/, '');
const sandbox = {
  console,
  document: {
    getElementById: () => ({
      addEventListener() {},
      classList: { toggle() {}, add() {}, remove() {} },
      setAttribute() {},
      style: {},
      innerHTML: '',
      textContent: '',
      querySelectorAll: () => [],
      querySelector: () => null,
    }),
    querySelector: () => null,
    querySelectorAll: () => [],
    addEventListener() {},
    body: { style: {}, classList: { add() {}, remove() {} } },
    createElement: () => ({
      classList: { add() {}, toggle() {} },
      setAttribute() {},
      style: {},
      addEventListener() {},
      appendChild() {},
      dataset: {},
    }),
  },
  window: { addEventListener() {}, matchMedia: () => ({ matches: false }) },
  URLSearchParams,
  Set,
  Map,
  Array,
  Object,
  Math,
  String,
  Number,
  Boolean,
  JSON,
  parseInt,
  parseFloat,
  isNaN,
  encodeURIComponent,
  setTimeout: () => 0,
  clearTimeout: () => 0,
  fetch: async () => ({ ok: true, json: async () => [] }),
};
sandbox.global = sandbox;
sandbox.self = sandbox;
vm.createContext(sandbox);
vm.runInContext(
  code +
    '; this.E={REGION_PATHS,regionGlobeSVG,detailRegionMapHTML,MAP_REGIONS};',
  sandbox
);
const E = sandbox.E;
for (const rid of E.MAP_REGIONS.filter((r) => r !== 'global')) {
  const d = E.REGION_PATHS[rid];
  const xs = [...d.matchAll(/[ML](\d+\.?\d*),/g)].map((m) => +m[1]);
  console.log(
    rid,
    'pts',
    xs.length,
    'x',
    Math.min(...xs).toFixed(0) + '-' + Math.max(...xs).toFixed(0)
  );
}
const ocxs = [...E.REGION_PATHS.oceania.matchAll(/[ML](\d+\.?\d*),/g)].map(
  (m) => +m[1]
);
if (Math.min(...ocxs) < 600) {
  console.error('OC still left', Math.min(...ocxs));
  process.exit(1);
}
const naxs = [
  ...E.REGION_PATHS['north-america'].matchAll(/[ML](\d+\.?\d*),/g),
].map((m) => +m[1]);
if (Math.min(...naxs) > 350) {
  console.error('NA not left');
  process.exit(1);
}
const svg = E.regionGlobeSVG(
  'asia',
  Object.fromEntries(E.MAP_REGIONS.map((r) => [r, 15]))
);
if (
  !svg.includes('data-region="asia"') ||
  !svg.includes('viewBox="0 0 1000 500"')
) {
  process.exit(1);
}
const mini = E.detailRegionMapHTML(['europe', 'africa']);
if (!mini.includes('detail-region-path on')) process.exit(1);
console.log('REAL MAP PASS');
