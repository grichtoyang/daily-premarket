import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const source = readFileSync(new URL("../workers/taifex-proxy_V1.8.js", import.meta.url), "utf8");

function declaration(name, nextMarker) {
  const start = source.indexOf("function " + name + "(");
  assert.notEqual(start, -1, "Missing Worker function: " + name);
  const end = source.indexOf(nextMarker, start);
  assert.notEqual(end, -1, "Missing end marker after " + name);
  return source.slice(start, end).trim();
}

const nullableNumber = value => {
  if (value === null || value === undefined || value === "") return null;
  const number = Number(value);
  return Number.isFinite(number) ? number : null;
};
const isoCompactDate = value => {
  const text = String(value ?? "").trim();
  if (/^\d{4}-\d{2}-\d{2}$/.test(text)) return text;
  if (/^\d{8}$/.test(text)) return text.slice(0,4) + "-" + text.slice(4,6) + "-" + text.slice(6,8);
  return null;
};
const parseCsvFields = new Function(
  declaration("parseCsvFields", "\n\nfunction parseTAIFEXDeltaCsv") + "; return parseCsvFields;"
)();
const parseTAIFEXDeltaCsv = new Function(
  "nullableNumber", "isoCompactDate", "parseCsvFields",
  declaration("parseTAIFEXDeltaCsv", "\n\nasync function fetchTXODeltaForDate") + "; return parseTAIFEXDeltaCsv;"
)(nullableNumber, isoCompactDate, parseCsvFields);

const sample = [
  ",,,公布日期時間,2026/11/19 04:35:34 PM",
  "商品,買賣權,到期月份(週別),履約價格,Delta值,契約到期日",
  "TXO,買權,202611F3,35700,1.0000,20261120",
  "TXO,賣權,202611F3,35700,0.0000,20261120",
  "TEO,買權,202611F3,35700,0.5000,20261120"
].join("\n");

assert.deepEqual(
  parseCsvFields('TXO,"買權",202611W4,21500,0.6789,20261125'),
  ["TXO", "買權", "202611W4", "21500", "0.6789", "20261125"]
);

{
  const result = parseTAIFEXDeltaCsv(sample, "2026-11-19");
  assert.equal(result.found, true);
  assert.equal(result.raw_rows, 2);
  assert.equal(result.rows.length, 2);
  assert.equal(result.diagnostics.call_rows, 1);
  assert.equal(result.diagnostics.put_rows, 1);
  assert.deepEqual(result.rows[0], {
    contract: "TXO", contract_month: "202611F3",
    contract_expiry_date: "2026-11-20", strike: 35700,
    type: "call", delta: 1.0
  });
  assert.equal(result.rows[1].type, "put");
}

{
  const result = parseTAIFEXDeltaCsv(sample, "2026-11-20");
  assert.equal(result.found, false);
  assert.match(result.reason, /date mismatch/);
  assert.equal(result.rows.length, 0);
}

{
  const result = parseTAIFEXDeltaCsv(sample.replace("1.0000", "not-a-number"), "2026-11-19");
  assert.equal(result.diagnostics.invalid_rows, 1);
  assert.equal(result.rows.length, 1);
}

console.log("PASS: TAIFEX historical Delta CSV parser and date validation");
