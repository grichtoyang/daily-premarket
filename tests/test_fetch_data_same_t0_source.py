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


if __name__ == "__main__":
    unittest.main()
