import unittest

from src.fetch_data import merge_same_t0


def report(ratio, source):
    return f"""# DATA_REPORT_20261030
- 產出盤別：全日

## 融資融券

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資維持率 | {ratio} | % | {source} |
"""


class SameT0MarginRatioMergeTests(unittest.TestCase):
    def test_new_self_built_value_replaces_old_blave_value(self):
        old = report("171.754", "Blave 上市市場融資維持率估算（資料日期：2026-10-30）")
        new = report("171.747", "TWSE 上市自建估算（資料日期：2026-10-30）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | 171.747 | % | TWSE 上市自建估算", merged)
        self.assertNotIn("171.754", merged)

    def test_new_self_built_value_replaces_old_manual_value(self):
        old = report("172.100", "人工輸入（MANUAL_LISTED_MARGIN_RATIO；資料日期：2026-10-30）")
        new = report("171.747", "TWSE 上市自建估算（資料日期：2026-10-30）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | 171.747 | % | TWSE 上市自建估算", merged)
        self.assertNotIn("172.100", merged)

    def test_blave_replaces_old_manual_value(self):
        old = report("172.100", "人工輸入（MANUAL_LISTED_MARGIN_RATIO；資料日期：2026-10-30）")
        new = report("171.754", "Blave 上市市場融資維持率估算（資料日期：2026-10-30）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | 171.754 | % | Blave", merged)
        self.assertNotIn("172.100", merged)

    def test_blave_does_not_replace_old_self_built_value(self):
        old = report("171.747", "TWSE 上市自建估算（資料日期：2026-10-30）")
        new = report("171.754", "Blave 上市市場融資維持率估算（資料日期：2026-10-30）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | 171.747 | % | TWSE 上市自建估算", merged)
        self.assertNotIn("171.754", merged)

    def test_manual_does_not_replace_old_blave_value(self):
        old = report("171.754", "Blave 上市市場融資維持率估算（資料日期：2026-10-30）")
        new = report("172.100", "人工輸入（MANUAL_LISTED_MARGIN_RATIO；資料日期：2026-10-30）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | 171.754 | % | Blave", merged)
        self.assertNotIn("172.100", merged)

    def test_manual_does_not_replace_old_self_built_value(self):
        old = report("171.747", "TWSE 上市自建估算（資料日期：2026-10-30）")
        new = report("172.100", "人工輸入（MANUAL_LISTED_MARGIN_RATIO；資料日期：2026-10-30）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | 171.747 | % | TWSE 上市自建估算", merged)
        self.assertNotIn("172.100", merged)

    def test_unavailable_never_carries_old_ratio(self):
        old = report("171.754", "Blave 上市市場融資維持率估算（資料日期：2026-10-30）")
        new = report("unavailable", "unavailable（TWSE 自建、Blave、人工輸入皆不可用）")
        merged, _ = merge_same_t0(old, new, "全日", protect=True)
        self.assertIn("| 融資維持率 | unavailable | % | unavailable", merged)
        self.assertNotIn("171.754", merged)


if __name__ == "__main__":
    unittest.main()
