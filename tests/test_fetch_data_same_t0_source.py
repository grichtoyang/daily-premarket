import unittest

from src.fetch_data import merge_same_t0


class SameT0SourceAttributionTests(unittest.TestCase):
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

    def test_unavailable_gamma_flip_does_not_carry_forward_old_date(self):
        old = """# DATA_REPORT_20261106
- T0 交易日期：`2026-11-06`
- 產出盤別：`全日`

## 四、選擇權
### 14．Gamma Flip
| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-gamma-levels) |
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
| 資料日期 | unavailable | unavailable |
"""
        merged, _ = merge_same_t0(old, new, new_session="全日", protect=True)
        self.assertIn("| Gamma Flip 價位 | unavailable | unavailable |", merged)
        self.assertIn("| 資料日期 | unavailable | unavailable |", merged)
        self.assertNotIn("沿用前版（原來源：TAIFEX Proxy (options-gamma-levels)）", merged)


if __name__ == "__main__":
    unittest.main()
