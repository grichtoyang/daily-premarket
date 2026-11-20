import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const source = readFileSync(
  new URL("../workers/taifex-proxy_V1.7.js", import.meta.url),
  "utf8"
);

function functionSource(name, nextMarker) {
  const start = source.indexOf(`async function ${name}(`);
  assert.notEqual(start, -1, `missing async function ${name}`);
  const end = source.indexOf(nextMarker, start);
  assert.notEqual(end, -1, `missing end marker for ${name}`);
  return source.slice(start, end);
}

assert.match(source, /V1\.7 ADDITIVE/);
assert.match(source, /version: "V1\.7 — V1\.6 \+ bounded compact fetch \+ parallel Delta\/TAIEX \(additive\)"/);
assert.match(source, /compactDeadlineAt = compactStartedAt \+ 75000/);

const chain = functionSource(
  "fetchTXOChainForDate",
  "\n\nfunction today()"
);
assert.match(chain, /fetchTXOChainForDateWithDeadline\(taifexDate, options\)/);

const delta = functionSource(
  "fetchTXODeltaForDate",
  "\n\nfunction buildGammaProxy"
);
assert.match(delta, /deadlineAt: options\.deadlineAt/);
assert.match(delta, /Delta_\$\{compact\}\.csv/);\nassert.match(delta, /fetch\(sourceUrl/);\nassert.match(delta, /TextDecoder\("big5"\)/);
assert.match(delta, /fetchOpenAPIDeltaForDate\(requestedISO, requestContext\)/);
assert.match(delta, /parseTAIFEXDeltaCsv\(text, requestedISO\)/);

const taiEX = functionSource(
  "fetchTAIEXCloseForDate",
  "\n\nfunction "
);
assert.match(taiEX, /gexFetchOptions\(options\)/);

const routeStart = source.indexOf('"/options-market-structure-compact"');
assert.notEqual(routeStart, -1);
const route = source.slice(routeStart, routeStart + 18000);
assert.match(route, /const compactOptions = \{ deadlineAt: compactDeadlineAt \}/);
assert.match(route, /fetchTXOChainForDate\(taifexDate, compactOptions\)/);
assert.match(route, /fetchTXODeltaForDate\(queryDate, compactOptions\)/);
assert.match(route, /fetchTAIEXCloseForDate\(queryDate, compactOptions\)/);
assert.match(route, /Promise\.allSettled\(\[/);
assert.match(route, /deltaSettled\.status === "fulfilled"/);
assert.match(route, /taiexSettled\.status === "fulfilled"/);
assert.match(route, /Delta fetch threw/);
assert.match(route, /TAIEX fetch threw/);
assert.match(route, /stage: "chain_fetch"/);
assert.match(route, /stage: "delta_taiex_parallel"/);

console.log("PASS: V1.7 compact deadline propagation and parallel fetch contract");
