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

const parserStart = source.indexOf("function parseFuturesInstitutional(rows)");
const parserEnd = source.indexOf("function parseFuturesInstitutionalOI(rows)", parserStart);
assert.notEqual(parserStart, -1);
assert.notEqual(parserEnd, -1);
const parserSource = source.slice(parserStart, parserEnd);
const institutionCode = name => ({
  "外資": "foreign", "投信": "investment_trust", "自營商": "dealer",
  "陸資": "china_capital"
})[name] || null;
const parseNumber = value => {
  if (value === null || value === undefined) return null;
  const s = String(value).replace(/,/g, "").trim();
  if (!s || s === "-" || s === "--") return 0;
  const n = Number(s);
  return Number.isFinite(n) ? n : null;
};
const parseFuturesInstitutional = new Function(
  "institutionCode", "number", parserSource + "; return parseFuturesInstitutional;"
)(institutionCode, parseNumber);
const completeRows = [
  ["臺股期貨", "外資", 1, 2, 3, 4, 5, 6],
  ["臺股期貨", "投信", 1, 2, 3, 4, 5, 6],
  ["臺股期貨", "自營商", 1, 2, 3, 4, 5, 6]
];
assert.equal(parseFuturesInstitutional(completeRows).found, true);
assert.equal(parseFuturesInstitutional(completeRows.slice(0, 2)).found, false);
assert.equal(parseFuturesInstitutional([
  completeRows[0], completeRows[1], completeRows[1]
]).found, false);
assert.equal(parseFuturesInstitutional([
  completeRows[0], completeRows[1], ["臺股期貨", "自營商", 1, null, 3, 4, 5, 6]
]).found, false);

console.log("PASS: V1.8 institutional timeout/fallback/date/completeness contract");
