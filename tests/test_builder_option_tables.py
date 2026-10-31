from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from v9_pro_builder import parse_data_report


class BuilderOptionTableTests(unittest.TestCase):
    def test_existing_data_report_option_tables_are_parsed(self):
        report = ROOT / "data_reports" / "DATA_REPORT_20261030.md"
        self.assertTrue(report.exists(), "Protected DATA_REPORT sample must remain available")
        parsed = parse_data_report(report)
        options = parsed["options"]

        self.assertGreaterEqual(len(options["instOpt"]), 3)
        self.assertGreaterEqual(len(options["instOptForce"]), 3)
        self.assertGreaterEqual(len(options["top10Call"]), 3)
        self.assertGreaterEqual(len(options["top10Put"]), 3)

        self.assertEqual(options["instOpt"][0][0], "外資")
        self.assertEqual(options["instOptForce"][0][0], "外資")
        self.assertIn("買權", options["top10Call"][0][0])
        self.assertIn("賣權", options["top10Put"][0][0])


    def test_stale_margin_ratio_provenance_is_not_current_t0(self):
        report = ROOT / "data_reports" / "DATA_REPORT_20261030.md"
        parsed = parse_data_report(report)
        margin = parsed["margin"]

        self.assertEqual(margin["ratio"], 178.40)
        self.assertEqual(margin["ratio_status"], "previous_report_fallback")
        self.assertEqual(margin["ratio_source_date"], "2026-10-29")
        self.assertFalse(margin["ratio_is_t0"])


if __name__ == "__main__":
    unittest.main()
