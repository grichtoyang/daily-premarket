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

function declaration(name, nextMarker) {
  const start = source.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `Missing Worker function: ${name}`);
  const end = source.indexOf(nextMarker, start);
  assert.notEqual(end, -1, `Missing end marker after ${name}`);
  return source.slice(start, end).trim();
}

const isoCompactDate = value => {
  const s = String(value ?? "").trim();
  if (/^\d{4}-\d{2}-\d{2}$/.test(s)) return s;
  if (/^\d{8}$/.test(s)) return `${s.slice(0,4)}-${s.slice(4,6)}-${s.slice(6,8)}`;
  return null;
};
const uniqueExpiries = new Function(
  "isoCompactDate",
  `${declaration("uniqueExpiries", "\n\nfunction buildExpirySelectionDiagnostics")}; return uniqueExpiries;`
)(isoCompactDate);
const buildExpirySelectionDiagnostics = new Function(
  "uniqueExpiries", "isoCompactDate",
  `${declaration("buildExpirySelectionDiagnostics", "\n\nfunction findCommonExpiryWithDiagnostics")}; return buildExpirySelectionDiagnostics;`
)(uniqueExpiries, isoCompactDate);
const findCommonExpiryWithDiagnostics = new Function(
  "buildExpirySelectionDiagnostics",
  `${declaration("findCommonExpiryWithDiagnostics", "\n\nfunction findCommonExpiry")}; return findCommonExpiryWithDiagnostics;`
)(buildExpirySelectionDiagnostics);
const scanGammaFlipRange = new Function(
  "findGammaFlipBracket",
  `${declaration("scanGammaFlipRange", "\n\nfunction buildGammaForCommonExpiry")}; return scanGammaFlipRange;`
)(findGammaFlipBracket);

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

const expiryRows = (contract_month, expiry, type = "call") => ({
  contract_month, contract_expiry_date: expiry, type, strike: 40000
});

{
  const result = scanGammaFlipRange(value => value - 105, 100, 110, 2);
  assert.equal(result.gamma_flip.estimated_underlying, 105);
  assert.equal(result.diagnostics.found, true);
  assert.equal(result.diagnostics.evaluations, 4);
}

// Same-day common expiry is recorded but rejected; next future common expiry wins.
{
  const chain = [
    expiryRows("202611F1", "2026-11-06"),
    expiryRows("202611W2", "2026-11-11")
  ];
  const delta = [
    expiryRows("202611F1", "2026-11-06"),
    expiryRows("202611W2", "2026-11-11")
  ];
  const result = findCommonExpiryWithDiagnostics(chain, delta, "2026-11-06");
  assert.deepEqual(result.selected, {
    contract_month: "202611W2", expiry: "2026-11-11"
  });
  assert.equal(result.diagnostics.same_day_common_expiries.length, 1);
  assert.equal(result.diagnostics.selection_reason, "earliest_future_exact_common_expiry");
}

// If Delta omits the same-day expiry, the next shared expiry remains selectable.
{
  const chain = [
    expiryRows("202611F1", "2026-11-06"),
    expiryRows("202611W2", "2026-11-11")
  ];
  const delta = [expiryRows("202611W2", "2026-11-11")];
  const result = findCommonExpiryWithDiagnostics(chain, delta, "2026-11-06");
  assert.equal(result.selected.contract_month, "202611W2");
  assert.equal(result.diagnostics.same_day_common_expiries.length, 0);
}

// Same-day-only overlap must fail closed instead of returning a zero-time expiry.
{
  const result = findCommonExpiryWithDiagnostics(
    [expiryRows("202611F1", "2026-11-06")],
    [expiryRows("202611F1", "2026-11-06")],
    "2026-11-06"
  );
  assert.equal(result.selected, null);
  assert.equal(
    result.diagnostics.selection_reason,
    "same_day_common_expiry_rejected_no_positive_time_to_expiry"
  );
}

// A unique expiry-date match is allowed when source contract-month labels differ.
{
  const result = findCommonExpiryWithDiagnostics(
    [expiryRows("202611W2", "2026-11-11")],
    [expiryRows("202611W02", "2026-11-11")],
    "2026-11-06"
  );
  assert.deepEqual(result.selected, {
    contract_month: "202611W2", expiry: "2026-11-11"
  });
  assert.equal(
    result.diagnostics.selected.match_type,
    "unique_expiry_date_label_mismatch"
  );
}

// Preserve exact contract-month matches ahead of earlier date-only label fallbacks.
{
  const result = findCommonExpiryWithDiagnostics(
    [
      expiryRows("202611W2", "2026-11-11"),
      expiryRows("202611W3", "2026-11-18")
    ],
    [
      expiryRows("202611W02", "2026-11-11"),
      expiryRows("202611W3", "2026-11-18")
    ],
    "2026-11-06"
  );
  assert.equal(result.selected.contract_month, "202611W3");
  assert.equal(
    result.diagnostics.selection_reason,
    "earliest_future_exact_common_expiry"
  );
  assert.equal(result.diagnostics.future_date_fallback_common_expiries.length, 1);
}

console.log("PASS: Worker Gamma Flip, OI, and expiry selection diagnostics");
