import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
const source = readFileSync(new URL("../workers/taifex-proxy_V1.8.js", import.meta.url), "utf8");
function section(start, end) {
  const i = source.indexOf(start);
  assert.notEqual(i, -1, "missing " + start);
  const j = source.indexOf(end, i + start.length);
  assert.notEqual(j, -1, "missing end " + end);
  return source.slice(i, j);
}
assert.match(section("async function fetchTAIFEX(path)", "function institutionCode"), /AbortSignal\.timeout\(12000\)/);
assert.match(section("async function fetchTAIFEX(path)", "function institutionCode"), /deadlineAt: institutionalDeadlineAt/);
assert.match(section("async function fetchOpenAPIInstitutionalFutures", "async function fetchOpenAPIInstitutionalOptionsRows"), /timeoutMs: 8000/);
assert.match(section("async function fetchOpenAPIInstitutionalFutures", "async function fetchOpenAPIInstitutionalOptionsRows"), /dates\.length !== 1/);
assert.match(section("function parseFuturesInstitutional", "function parseFuturesInstitutionalOI"), /seen\.has\(institution\)/);
assert.match(section("function parseFuturesInstitutional", "function parseFuturesInstitutionalOI"), /investment_trust/);
assert.match(section("async function institutionalEndpoint", "/* =========================\n   Worker"), /parsed\.found !== true/);
assert.match(source, /date: fb\.date/);
console.log("PASS: V1.8 institutional timeout/fallback/date/completeness contract");
