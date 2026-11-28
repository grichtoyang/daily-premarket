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
assert.match(section("async function fetchTAIFEX(path)", "function institutionCode"), /!pageDataDate\(html\)/);
assert.match(section("async function fetchOpenAPIInstitutionalFutures", "async function fetchOpenAPIInstitutionalOptionsRows"), /timeoutMs: Number\.isFinite\(options\.timeoutMs\) \? options\.timeoutMs : 8000/);
assert.match(section("async function fetchOpenAPIInstitutionalFutures", "async function fetchOpenAPIInstitutionalOptionsRows"), /dates\.length !== 1/);
assert.match(section("function parseFuturesInstitutional", "function parseFuturesInstitutionalOI"), /seen\.has\(institution\)/);
assert.match(section("function parseFuturesInstitutional", "function parseFuturesInstitutionalOI"), /investment_trust/);
assert.match(section("async function institutionalEndpoint", "/* =========================\n   Worker"), /parsed\.found !== true/);
assert.match(source, /date: fb\.date/);
assert.match(source, /sourceDateMatches = key !== "fut_trade_day" \|\| r\.date === taipeiISO/);

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


const fallbackStart = source.indexOf("async function fetchOpenAPIInstitutionalFutures(options = {})");
const fallbackEnd = source.indexOf("async function fetchOpenAPIInstitutionalOptionsRows", fallbackStart);
const fallbackSource = source.slice(fallbackStart, fallbackEnd);
const apiValue = (row, keys) => {
  for (const key of keys) if (row && Object.prototype.hasOwnProperty.call(row, key)) return row[key];
  return null;
};
const apiDateISO = value => {
  const digits = String(value ?? "").replace(/\D/g, "");
  return digits.length === 8 ? digits.slice(0, 4) + "-" + digits.slice(4, 6) + "-" + digits.slice(6, 8) : null;
};
const apiRows = ["外資", "投信", "自營商"].map(Item => ({
  ContractCode: "臺股期貨", Date: "20261127", Item,
  "TradingVolume(Long)": 1, "TradingValue(Long)(Thousands)": 2,
  "TradingVolume(Short)": 3, "TradingValue(Short)(Thousands)": 4,
  "TradingVolume(Net)": 5, "TradingValue(Net)(Thousands)": 6
}));
const makeFallback = rows => new Function(
  "fetchTAIFEXOpenAPI", "apiValue", "apiDateISO", "number",
  fallbackSource + "; return fetchOpenAPIInstitutionalFutures;"
)(
  async () => ({ found: true, rows }), apiValue, apiDateISO,
  value => value === null || value === undefined ? null : Number(value)
);
const fallbackGood = await makeFallback(apiRows)();
assert.equal(fallbackGood.found, true);
assert.equal(fallbackGood.date, "2026-11-27");
assert.equal(fallbackGood.rows.length, 3);
const fallbackStaleMix = await makeFallback([
  apiRows[0], apiRows[1], { ...apiRows[2], Date: "20261126" }
])();
assert.equal(fallbackStaleMix.found, false);
const fallbackMissingCategory = await makeFallback(apiRows.slice(0, 2))();
assert.equal(fallbackMissingCategory.found, false);

console.log("PASS: V1.8 institutional timeout/fallback/date/completeness contract");
