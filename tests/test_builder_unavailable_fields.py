import re
import tempfile
import unittest
from pathlib import Path

from scripts.v9_pro_builder import parse_data_report


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "data_reports" / "DATA_REPORT_20261030.md"


def replace_row_value(report, label, value="unavailable", occurrence=0):
    pattern = re.compile(rf"(?m)^(\|\s*{re.escape(label)}\s*\|)[^|\n]*(\|)")
    matches = list(pattern.finditer(report))
    if len(matches) <= occurrence:
        raise AssertionError(f"fixture row not found: {label} #{occurrence}")
    match = matches[occurrence]
    return report[:match.start()] + match.group(1) + " " + value + " " + match.group(2) + report[match.end():]


class BuilderUnavailableFieldTests(unittest.TestCase):
    def setUp(self):
        self.report = FIXTURE.read_text(encoding="utf-8")

    def parse_modified(self, report):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "DATA_REPORT.md"
            path.write_text(report, encoding="utf-8")
            return parse_data_report(path)

    def test_explicit_unavailable_spot_and_institution_fields_are_preserved(self):
        report = self.report
        for label in ("加權指數", "漲跌點數", "成交金額", "上漲家數", "下跌家數", "自營商", "三大法人合計"):
            report = replace_row_value(report, label)
        parsed = self.parse_modified(report)
        self.assertIsNone(parsed["spot"]["close"])
        self.assertIsNone(parsed["spot"]["diff"])
        self.assertIsNone(parsed["spot"]["vol"])
        self.assertIsNone(parsed["spot"]["up"])
        self.assertIsNone(parsed["spot"]["down"])
        self.assertIsNone(parsed["inst"]["dealer"])
        self.assertIsNone(parsed["inst"]["all"])

    def test_explicit_unavailable_futures_fields_are_preserved(self):
        report = self.report
        for label in ("開盤價", "投信多空淨 OI", "自營商多空淨 OI", "前十大交易人多空淨 OI"):
            report = replace_row_value(report, label)
        parsed = self.parse_modified(report)
        self.assertIsNone(parsed["tx"]["day"]["o"])
        self.assertIsNone(parsed["futures"]["trust_oi"])
        self.assertIsNone(parsed["futures"]["dealer_oi"])
        self.assertIsNone(parsed["futures"]["top10"])

    def test_explicit_unavailable_option_volume_and_oi_are_preserved(self):
        report = self.report
        for label in ("Call 總成交量", "Call 總未平倉量 OI", "Put 總成交量", "Put 總未平倉量 OI"):
            report = replace_row_value(report, label)
        parsed = self.parse_modified(report)
        self.assertIsNone(parsed["options"]["callVol"])
        self.assertIsNone(parsed["options"]["callOi"])
        self.assertIsNone(parsed["options"]["putVol"])
        self.assertIsNone(parsed["options"]["putOi"])

    def test_missing_required_row_still_fails_closed(self):
        report = re.sub(r"(?m)^\| Call 總成交量 \|[^\n]*\n", "", self.report, count=1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "DATA_REPORT.md"
            path.write_text(report, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Call成交"):
                parse_data_report(path)


if __name__ == "__main__":
    unittest.main()
