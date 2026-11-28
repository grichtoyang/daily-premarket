import unittest

from src.fetch_data import (
    merge_same_t0, _snapshot_chain_source_label, _sum_gex_model_oi, _adr_stale_note, _gamma_flip_status_label,
    _market_coverage, _validate_market_quote_completeness,
)
from src.sources.us_market import _apply_adr_freshness


class SameT0SourceAttributionTests(unittest.TestCase):

    def test_market_coverage_counts_unavailable_and_partial_quotes(self):
        market_data = {
            "亞洲主要指數": [
                ("日經225", {"symbol": "^N225", "price": None, "change": None, "pct": None}),
            ],
            "美股指數": [
                ("S&P 500", {"symbol": "^GSPC", "price": 7297.49, "change": None, "pct": 1.6}),
            ],
        }
        partial, unavailable = _market_coverage(market_data)
        self.assertEqual(len(unavailable), 3)
        self.assertTrue(all("日經225" in item for item in unavailable))
        self.assertTrue(any(".price" in item for item in unavailable))
        self.assertTrue(any(".change" in item for item in unavailable))
        self.assertTrue(any(".pct" in item for item in unavailable))
        self.assertEqual(len(partial), 1)
        self.assertIn("change", partial[0])

    def test_market_report_validator_rejects_unavailable_market_quote(self):
        text = """## 二、重要市場
| 項目 | 價格 | 漲跌 |
|---|---|---|
| 台積電ADR | unavailable | unavailable |
## 三、期貨
"""
        with self.assertRaisesRegex(ValueError, "重要市場行情仍有缺值"):
            _validate_market_quote_completeness(text)

    def test_market_report_validator_accepts_complete_market_quote(self):
        text = """## 二、重要市場
| 項目 | 價格 | 漲跌 |
|---|---|---|
| 台積電ADR | 353.34 | +11.00 |
## 三、期貨
"""
        _validate_market_quote_completeness(text)

    def test_raw_chain_oi_and_model_eligible_oi_are_reconciled_separately(self):
        levels = [
            {"call_oi": 12000, "put_oi": 3000},
            {"call_oi": 31644, "put_oi": 4235},
        ]
        raw_call_oi = 43690
        raw_put_oi = 7235
        model_call_oi = _sum_gex_model_oi(levels, "call_oi")
        model_put_oi = _sum_gex_model_oi(levels, "put_oi")
        self.assertEqual(model_call_oi, 43644)
        self.assertEqual(model_put_oi, raw_put_oi)
        self.assertEqual(raw_call_oi - model_call_oi, 46)

    def test_same_t0_freezes_first_publish_time_but_refreshes_update_time(self):
        old = """# DATA_REPORT_20261106
- 報告日期：`2026-11-08`
- T0 交易日期：`2026-11-06`
- 資料產出時間：`2026-11-08 10:38:08`
- 本次更新開始時間：`2026-11-08 10:38:08`
- 產出盤別：`全日`

## 一、現貨
"""
        new = """# DATA_REPORT_20261106
- 報告日期：`2026-11-08`
- T0 交易日期：`2026-11-06`
- 首次資料產出時間：`2026-11-08 11:04:09`
- 本次更新開始時間：`2026-11-08 11:04:09`
- 產出盤別：`全日`

## 一、現貨
"""
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("- 首次資料產出時間：`2026-11-08 10:38:08`", merged)
        self.assertIn("- 本次更新開始時間：`2026-11-08 11:04:09`", merged)
        self.assertNotIn("- 本次更新開始時間：`2026-11-08 10:38:08`", merged)


    def test_force_rewrite_preserves_first_publish_time_but_refreshes_update_time(self):
        old = """# DATA_REPORT_20261127
- 報告日期：`2026-11-28`
- T0 交易日期：`2026-11-27`
- 首次資料產出時間：`2026-11-28 11:04:08`
- 本次更新開始時間：`2026-11-28 11:04:08`
- 產出盤別：`全日`
"""
        new = """# DATA_REPORT_20261127
- 報告日期：`2026-11-28`
- T0 交易日期：`2026-11-27`
- 首次資料產出時間：`2026-11-28 12:51:09`
- 本次更新開始時間：`2026-11-28 12:51:09`
- 產出盤別：`全日`
"""
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=False)
        self.assertIn("- 首次資料產出時間：`2026-11-28 11:04:08`", merged)
        self.assertIn("- 本次更新開始時間：`2026-11-28 12:51:09`", merged)

    def test_previous_day_gamma_proxy_is_explicitly_reference_only(self):
        status = _gamma_flip_status_label(
            "2026-11-27", 37182.94, "2026-11-26", "options-market-structure-compact (proxy)"
        )
        self.assertIn("前一交易日 Proxy", status)
        self.assertIn("2026-11-26", status)
        self.assertIn("不作當日正式 Flip", status)

    def test_current_day_formal_gamma_flip_is_distinguished_from_proxy(self):
        status = _gamma_flip_status_label(
            "2026-11-27", 34633.93, "2026-11-27", "options-gamma-levels"
        )
        self.assertIn("T0 正式 GEX 模型 Flip", status)

    def test_borrowed_value_is_not_carried_forward_when_fresh_source_is_unavailable(self):
        old = """# DATA_REPORT_20261030
- 報告日期：`2026-10-31`
- T0 交易日期：`2026-10-30`
- 資料產出時間：`2026-10-31 08:00:00`
- 產出盤別：`全日`

## 一、現貨
### 5. 借券資料
| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券賣出增減 | -1,273 | 張 | TWSE TWT93U + TPEX margin_sbl |
"""
        new = """# DATA_REPORT_20261030
- 報告日期：`2026-10-31`
- T0 交易日期：`2026-10-30`
- 資料產出時間：`2026-11-01 23:51:51`
- 產出盤別：`全日`

## 一、現貨
### 5. 借券資料
| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券賣出增減 | unavailable | 張 | TPEX margin_sbl |
"""
        merged, filled = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertEqual(filled, 0)
        self.assertIn("| 借券賣出增減 | unavailable | 張 | TPEX margin_sbl |", merged)
        self.assertNotIn("| 借券賣出增減 | -1,273 |", merged)



    def test_stale_asian_quotes_are_not_restored_by_same_t0_protection(self):
        old = """# DATA_REPORT_20261120
- T0 交易日期：`2026-11-20`
- 產出盤別：`全日`

## 二、重要市場
### 2. 亞洲主要指數
| 指數 | 收盤／最新值 | 漲跌點數 | 漲跌幅 | 資料日期 | 更新時間 | 時區 | 資料來源 |
|---|---:|---:|---:|---|---|---|---|
| 日經225 | 59,444.21 | 419.93 | +0.71 | 2026-11-19 | 2026-11-21T00:14:45+00:00 | Asia/Tokyo | 沿用前版（原來源：Yahoo Finance Chart API） |
"""
        new = """# DATA_REPORT_20261120
- T0 交易日期：`2026-11-20`
- 產出盤別：`全日`

## 二、重要市場
### 2. 亞洲主要指數
| 指數 | 收盤／最新值 | 漲跌點數 | 漲跌幅 | 資料日期 | 更新時間 | 時區 | 資料來源 |
|---|---:|---:|---:|---|---|---|---|
| 日經225 | unavailable | unavailable | unavailable | 2026-11-19 | 2026-11-21T00:14:45+00:00 | Asia/Tokyo | Yahoo Finance Chart API（資料日期早於 T0，已排除） |

- 註記：亞洲主要指數資料日期落後 T0 2026-11-20，已將舊行情排除並標示 unavailable；原始資料日期：日經225 2026-11-19
"""
        merged, filled = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertEqual(filled, 0)
        self.assertIn("| 日經225 | unavailable | unavailable | unavailable | 2026-11-19 |", merged)
        self.assertNotIn("59,444.21", merged)
        self.assertNotIn("沿用前版（原來源：Yahoo Finance Chart API）", merged)

    def test_new_common_contract_oi_values_keep_their_snapshot_source(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 2．Call 總成交量、OI、OI 增減
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call OI 增減 (2026-11-05→2026-11-06) | unavailable | 端點未提供 |
### 9．Call OI 增減集中區
| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | unavailable | 端點未提供 |
"""
        new = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 2．Call 總成交量、OI、OI 增減
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call OI 增減 (2026-11-05→2026-11-06) | +43,511 | TAIFEX Proxy snapshots (2026-11-05) |
### 9．Call OI 增減集中區
| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 40,000 (+4,752) | TAIFEX Proxy snapshots (2026-11-05) |
"""
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| Call OI 增減 (2026-11-05→2026-11-06) | +43,511 | TAIFEX Proxy snapshots (2026-11-05) |", merged)
        self.assertIn("| Call OI 增加最多的履約價 | 40,000 (+4,752) | TAIFEX Proxy snapshots (2026-11-05) |", merged)

    def test_valid_oi_changes_refresh_stale_endpoint_source_on_same_t0(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 2．Call 總成交量、OI、OI 增減
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call OI 增減（共同合約） (2026-11-05→2026-11-06) | +43,511 | 端點未提供 |
### 3．Put 總成交量、OI、OI 增減
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put OI 增減（共同合約） (2026-11-05→2026-11-06) | +16,839 | 端點未提供 |
### 9．Call OI 增減集中區
| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 40,000 (+4,752) | 端點未提供 |
| Call OI 減少最多的履約價（共同合約） | 46,500 (-1,958) | 端點未提供 |
### 10．Put OI 增減集中區
| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 39,700 (+3,026) | 端點未提供 |
| Put OI 減少最多的履約價（共同合約） | 40,500 (-429) | 端點未提供 |
"""
        new = old.replace("端點未提供", "TAIFEX Proxy snapshots (2026-11-05)")
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertNotIn("端點未提供", merged)
        self.assertEqual(merged.count("TAIFEX Proxy snapshots (2026-11-05)"), 6)
        self.assertIn("| Call OI 增減（共同合約） (2026-11-05→2026-11-06) | +43,511 | TAIFEX Proxy snapshots (2026-11-05) |", merged)
        self.assertIn("| Put OI 增減（共同合約） (2026-11-05→2026-11-06) | +16,839 | TAIFEX Proxy snapshots (2026-11-05) |", merged)


    def test_unavailable_gamma_flip_keeps_current_gex_data_date(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 14．Gamma Flip
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| GEX 資料日期 | 2026-11-05 | TAIFEX Proxy (options-gamma-levels) |
"""
        new = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 14．Gamma Flip
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | unavailable |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| GEX 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |
"""
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| Gamma Flip 價位 | unavailable | unavailable |", merged)
        self.assertNotIn("41,102.53", merged)
        self.assertIn("| GEX 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |", merged)
        self.assertNotIn("2026-11-05 | TAIFEX Proxy", merged)
        self.assertNotIn("沿用前版（原來源：TAIFEX Proxy (options-gamma-levels)）", merged)


    def test_option_report_production_timestamp_refreshes_on_same_t0(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 1．選擇權交易日期、到期日與報告產製時間
| 項目 | 數值 | 資料來源 |
|---|---|---|
| 本次報告產製時間 | 2026-11-08 13:52:30 | 本機 |
"""
        new = old.replace("2026-11-08 13:52:30", "2026-11-08 15:20:21")
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| 本次報告產製時間 | 2026-11-08 15:20:21 | 本機 |", merged)
        self.assertNotIn("13:52:30", merged)

    def test_night_quote_carry_forward_is_explicitly_attributed(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 三、期貨
### 2．台指期近月夜盤行情
| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 收盤價 | 40,298 | 點 | TAIFEX Proxy |
| 成交量 | 69,882 | 口 | TAIFEX Proxy |
"""
        new = old.replace("40,298 | 點 | TAIFEX Proxy", "unavailable | 點 | unavailable")
        new = new.replace("69,882 | 口 | TAIFEX Proxy", "unavailable | 口 | unavailable")
        merged, filled = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertEqual(filled, 4)  # value and source cells for each of two rows
        self.assertIn("| 收盤價 | 40,298 | 點 | 沿用前版（原來源：TAIFEX Proxy） |", merged)
        self.assertIn("| 成交量 | 69,882 | 口 | 沿用前版（原來源：TAIFEX Proxy） |", merged)

    def test_valid_new_same_t0_night_quotes_replace_old_values(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 三、期貨
### 2．台指期近月夜盤行情
| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 收盤價 | 40,298 | 點 | TAIFEX Proxy |
| 成交量 | 69,882 | 口 | TAIFEX Proxy |
"""
        new = old.replace("40,298 | 點 | TAIFEX Proxy", "40,310 | 點 | TAIFEX Proxy")
        new = new.replace("69,882 | 口 | TAIFEX Proxy", "70,120 | 口 | TAIFEX Proxy")
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| 收盤價 | 40,310 | 點 | TAIFEX Proxy |", merged)
        self.assertIn("| 成交量 | 70,120 | 口 | TAIFEX Proxy |", merged)
        self.assertNotIn("沿用前版", merged)

    def test_night_derived_rows_refresh_source_when_values_are_unchanged(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 三、期貨
### 6．期貨與現貨關係
| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤價格相對日盤收盤的變化 | +512 | 沿用前版（原來源：TAIFEX Proxy） |
### 7．日盤、夜盤與籌碼變化對照
#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)
| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,786 | 40,298 | -512 | 沿用前版（原來源：TAIFEX Proxy） |
| 成交量 | 143,277 | 69,882 | +73,395 | 沿用前版（原來源：TAIFEX Proxy） |
"""
        new = old.replace("沿用前版（原來源：TAIFEX Proxy）", "TAIFEX Proxy")
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| 夜盤價格相對日盤收盤的變化 | +512 | TAIFEX Proxy |", merged)
        self.assertIn("| 收盤價 | 39,786 | 40,298 | -512 | TAIFEX Proxy |", merged)
        self.assertIn("| 成交量 | 143,277 | 69,882 | +73,395 | TAIFEX Proxy |", merged)
        self.assertNotIn("沿用前版", merged)
        self.assertNotIn("同 T0 穩定", merged)

    def test_night_derived_rows_still_freeze_when_values_change(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 三、期貨
### 6．期貨與現貨關係
| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤價格相對日盤收盤的變化 | +512 | 沿用前版（原來源：TAIFEX Proxy） |
"""
        new = old.replace("+512", "+520").replace("沿用前版（原來源：TAIFEX Proxy）", "TAIFEX Proxy")
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| 夜盤價格相對日盤收盤的變化 | +512 | 沿用前版（原來源：TAIFEX Proxy） |", merged)
        self.assertNotIn("| 夜盤價格相對日盤收盤的變化 | +520 |", merged)

    def test_oi_snapshot_source_label_uses_chain_provenance_not_endpoint(self):
        chain = {"c_chg": 43511, "p_chg": 16839, "snapshot_date": "2026-11-05"}
        self.assertEqual(
            _snapshot_chain_source_label(chain, None, "2026-11-06"),
            "TAIFEX Proxy snapshot bundle (2026-11-05→2026-11-06)"
        )
        self.assertEqual(
            _snapshot_chain_source_label({"c_chg": 43511}, None, "2026-11-06"),
            "TAIFEX Proxy snapshot bundle (快照日期未提供→2026-11-06)"
        )
        self.assertEqual(_snapshot_chain_source_label({}, None, "2026-11-06"), "unavailable")



    def test_stale_adr_quote_is_never_restored_during_same_t0_merge(self):
        old = """# DATA_REPORT_20261127
- T0 交易日期：`2026-11-27`
- 產出盤別：`全日`

## 二、重要市場
### 5. 台灣相關ADR
| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---:|---:|---:|---|---|---|---|
| 台積電ADR | TSM | 353.34 | 11.00 | +3.21% | 2026-11-27 | 2026-11-28T00:43:30+00:00 | America/New_York | Yahoo Finance Chart API |
"""
        new = """# DATA_REPORT_20261127
- T0 交易日期：`2026-11-27`
- 產出盤別：`全日`

## 二、重要市場
### 5. 台灣相關ADR
| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---:|---:|---:|---|---|---|---|
| 台積電ADR | TSM | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-28T01:07:19+00:00 | America/New_York | Yahoo Finance Chart API（資料日期過期，已排除） |
- 註記：台灣相關 ADR 新鮮度異常，已排除舊行情：台積電ADR（TSM，資料日期 2026-11-25）
<!-- ADR_STALE_SYMBOLS:TSM -->
"""
        for protect in (True, False):
            with self.subTest(protect=protect):
                merged, filled = merge_same_t0(old, new, new_session="全日", protect=protect)
                self.assertEqual(filled, 0)
                self.assertIn("| 台積電ADR | TSM | unavailable | unavailable | unavailable | 2026-11-25 |", merged)
                self.assertNotIn("353.34", merged)
                self.assertNotIn("11.00", merged)

    def test_unavailable_adr_quote_is_marked_and_cannot_be_restored_during_merge(self):
        # Exercise the full guard chain: source failure -> stale note/marker -> same-T0 merge.
        rows = [
            ("台積電ADR", {
                "symbol": "TSM", "price": None, "change": None, "pct": None,
                "date": None, "ok": False, "source": "Yahoo Finance Chart API",
            })
        ]
        rows = _apply_adr_freshness(rows, "2026-11-27")
        mk = {"台灣相關ADR": rows}
        note = _adr_stale_note(mk)
        self.assertIsNotNone(note)
        self.assertIn("<!-- ADR_STALE_SYMBOLS:TSM -->", note)

        old = """# DATA_REPORT_20261127
- T0 交易日期：`2026-11-27`
- 產出盤別：`全日`

## 二、重要市場
### 5. 台灣相關ADR
| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---:|---:|---:|---|---|---|---|
| 台積電ADR | TSM | 353.34 | 11.00 | +3.21% | 2026-11-27 | 2026-11-28T00:43:30+00:00 | America/New_York | Yahoo Finance Chart API |
"""
        new = f"""# DATA_REPORT_20261127
- T0 交易日期：`2026-11-27`
- 產出盤別：`全日`

## 二、重要市場
### 5. 台灣相關ADR
| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---:|---:|---:|---|---|---|---|
| 台積電ADR | TSM | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | Yahoo Finance Chart API（本次未取得報價，已排除） |
- 註記：{note}
"""
        for protect in (True, False):
            with self.subTest(protect=protect):
                merged, filled = merge_same_t0(old, new, new_session="全日", protect=protect)
                self.assertEqual(filled, 0)
                self.assertIn("| 台積電ADR | TSM | unavailable | unavailable | unavailable |", merged)
                self.assertNotIn("353.34", merged)
                self.assertNotIn("11.00", merged)

    def test_fresh_adr_row_is_not_blocked_by_another_stale_symbol_marker(self):
        old = """# DATA_REPORT_20261127
- T0 交易日期：`2026-11-27`
- 產出盤別：`全日`

## 二、重要市場
### 5. 台灣相關ADR
| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---:|---:|---:|---|---|---|---|
| 日月光ADR | ASX | 29.49 | 0.16 | +0.55% | 2026-11-25 | 2026-11-28T01:07:19+00:00 | America/New_York | Yahoo Finance Chart API |
"""
        new = old.replace("29.49 | 0.16 | +0.55%", "31.34 | 1.85 | +6.27%").replace(
            "2026-11-25 | 2026-11-28T01:07:19", "2026-11-27 | 2026-11-28T01:07:19"
        ) + "<!-- ADR_STALE_SYMBOLS:TSM -->\n"
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=False)
        self.assertIn("| 日月光ADR | ASX | 31.34 | 1.85 | +6.27% | 2026-11-27 |", merged)
        self.assertNotIn("| 日月光ADR | ASX | 29.49 |", merged)


if __name__ == "__main__":
    unittest.main()
