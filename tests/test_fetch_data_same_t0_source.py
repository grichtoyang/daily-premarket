import unittest

from src.fetch_data import merge_same_t0, _snapshot_chain_source_label, _sum_gex_model_oi


class SameT0SourceAttributionTests(unittest.TestCase):
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

    def test_carried_forward_value_is_not_labeled_as_fresh_source(self):
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
        self.assertEqual(filled, 1)
        self.assertIn("| 借券賣出增減 | -1,273 | 張 | 沿用前版（原來源：TWSE TWT93U + TPEX margin_sbl） |", merged)
        self.assertNotIn("| 借券賣出增減 | -1,273 | 張 | TPEX margin_sbl |", merged)


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


if __name__ == "__main__":
    unittest.main()
