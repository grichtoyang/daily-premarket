import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const source = readFileSync(
  new URL("../workers/taifex-proxy_V1.5.js", import.meta.url),
  "utf8"
);

function extractFunction(name, nextMarker) {
  const start = source.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `Missing Worker function: ${name}`);
  const end = source.indexOf(nextMarker, start);
  assert.notEqual(end, -1, `Missing end marker after ${name}`);
  const declaration = source.slice(start, end).trim();
  return new Function(`${declaration}; return ${name};`)();
}

const findGammaFlipBracket = extractFunction(
  "findGammaFlipBracket",
  "\n\nfunction summarizeExpiryOi"
);
const summarizeExpiryOi = extractFunction(
  "summarizeExpiryOi",
  "\n\nfunction buildGammaForCommonExpiry"
);

assert.deepEqual(
  findGammaFlipBracket(100, 0, 110, 12),
  {
    lower_underlying: 100,
    upper_underlying: 100,
    estimated_underlying: 100,
    lower_net_gex_1pct: 0,
    upper_net_gex_1pct: 0
  },
  "An exact zero at the lower sample must be detected"
);

assert.deepEqual(
  findGammaFlipBracket(100, -12, 110, 0),
  {
    lower_underlying: 110,
    upper_underlying: 110,
    estimated_underlying: 110,
    lower_net_gex_1pct: 0,
    upper_net_gex_1pct: 0
  },
  "An exact zero at the upper sample must be detected"
);

assert.equal(
  findGammaFlipBracket(100, -10, 110, 10).estimated_underlying,
  105,
  "A negative-to-positive bracket must retain linear interpolation"
);
assert.equal(
  findGammaFlipBracket(100, 10, 110, -10).estimated_underlying,
  105,
  "A positive-to-negative bracket must retain linear interpolation"
);
assert.equal(
  findGammaFlipBracket(100, 5, 110, 15),
  null,
  "Same-sign samples must not create a Flip"
);
assert.equal(
  findGammaFlipBracket(100, Number.NaN, 110, 0),
  null,
  "Non-finite samples must not create a Flip"
);

assert.deepEqual(
  summarizeExpiryOi([
    { type: "call", open_interest: 100 },
    { type: "call", open_interest: 0 },
    { type: "put", open_interest: 30 }
  ], "call"),
  { rows: 2, valid_rows: 2, invalid_rows: 0, total: 100 }
);
assert.deepEqual(
  summarizeExpiryOi([
    { type: "put", open_interest: 20 },
    { type: "put", open_interest: null },
    { type: "put", open_interest: "" },
    { type: "put", open_interest: true }
  ], "put"),
  { rows: 4, valid_rows: 1, invalid_rows: 3, total: null },
  "Incomplete OI must not be reported as a complete total"
);

console.log("PASS: Worker Gamma Flip exact-zero, sign-crossing, and expiry OI diagnostics");
