import unittest

from src.fetch_data import merge_same_t0


class SameT0SourceAttributionTests(unittest.TestCase):
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


class DataReportWriteSafetyTests(unittest.TestCase):
    def valid_report(self, t0="2026-11-06"):
        from src.fetch_data import _validate_data_report_text
        return "\n".join([
            f"# DATA_REPORT_{t0.replace('-', '')}",
            f"- T0 交易日期：`{t0}`",
            "## 一、現貨", "## 二、重要市場", "## 三、期貨",
            "## 四、選擇權", "## 五、資料來源、時間與完整性",
            "## 六、期現選方向對照", "內容" * 600,
        ])

    def test_atomic_write_replaces_only_after_validation(self):
        from src.fetch_data import _atomic_write_data_report
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "DATA_REPORT_20261106.md"
            target.write_text("舊報告", encoding="utf-8")
            _atomic_write_data_report(target, self.valid_report(), "2026-11-06")
            self.assertTrue(target.read_text(encoding="utf-8").startswith("# DATA_REPORT_20261106"))
            self.assertEqual(list(Path(directory).glob("*.tmp")), [])

    def test_invalid_report_keeps_previous_file_and_cleans_temp(self):
        from src.fetch_data import _atomic_write_data_report
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "DATA_REPORT_20261106.md"
            target.write_text("舊報告", encoding="utf-8")
            with self.assertRaises(ValueError):
                _atomic_write_data_report(target, "# DATA_REPORT_20261106\n不完整", "2026-11-06")
            self.assertEqual(target.read_text(encoding="utf-8"), "舊報告")
            self.assertEqual(list(Path(directory).glob(".*.tmp")), [])

    def test_replace_failure_keeps_previous_file_and_cleans_temp(self):
        from unittest.mock import patch
        from src.fetch_data import _atomic_write_data_report
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "DATA_REPORT_20261106.md"
            target.write_text("舊報告", encoding="utf-8")
            with patch("src.fetch_data.os.replace", side_effect=OSError("simulated")):
                with self.assertRaises(OSError):
                    _atomic_write_data_report(target, self.valid_report(), "2026-11-06")
            self.assertEqual(target.read_text(encoding="utf-8"), "舊報告")
            self.assertEqual(list(Path(directory).glob(".*.tmp")), [])

    def test_report_validator_rejects_wrong_t0_and_missing_sections(self):
        from src.fetch_data import _validate_data_report_text
        with self.assertRaises(ValueError):
            _validate_data_report_text(self.valid_report(), "2026-11-07")
        incomplete = self.valid_report().replace("## 四、選擇權\n", "")
        with self.assertRaises(ValueError):
            _validate_data_report_text(incomplete, "2026-11-06")

    def test_workflow_requires_success_exit_and_validated_report_path(self):
        from pathlib import Path
        workflow = (ROOT / ".github" / "workflows" / "daily_data.yml").read_text(encoding="utf-8")
        self.assertIn('if [ "$FETCH_RC" -eq 0 ]', workflow)
        self.assertIn("validate_data_report_file", workflow)
        self.assertIn("grep -F", workflow)
        self.assertNotIn("find data_reports -name 'DATA_REPORT_*.md' -newermt", workflow)
