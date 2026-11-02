from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from v9_pro_builder import build_option_force_analysis, parse_data_report


class OptionForceAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.force_rows = [
            ["外資", "11.36", "11.17", "+0.18", "4.88", "4.94", "-0.06", "+0.24", "TAIFEX Proxy"],
            ["投信", "0.00", "3.01", "-3.01", "0.00", "0.00", "+0", "-3.01", "TAIFEX Proxy"],
            ["自營商", "10.22", "8.40", "+1.82", "2.81", "3.35", "-0.54", "+2.35", "TAIFEX Proxy"],
            ["三大法人合計", "21.57", "22.58", "-1.01", "7.70", "8.29", "-0.60", "-0.41", "TAIFEX Proxy"],
        ]
        self.volume_rows = [
            ["外資", "91251", "91418", "-167", "41871", "41965", "-94", "-73", "TAIFEX Proxy"],
            ["投信", "0", "6362", "-6362", "0", "0", "+0", "-6362", "TAIFEX Proxy"],
            ["自營商", "79677", "72278", "+7399", "21826", "23217", "-1391", "+8790", "TAIFEX Proxy"],
            ["三大法人合計", "170928", "170058", "+870", "63697", "65182", "-1485", "+2355", "TAIFEX Proxy"],
        ]

    def test_real_report_builds_interpretation_and_flags_amount_volume_divergence(self):
        report = ROOT / "data_reports" / "DATA_REPORT_20261102.md"
        self.assertTrue(report.exists(), "Current T0 DATA_REPORT must be available")
        parsed = parse_data_report(report)
        analysis = parsed["options"]["instOptForceAnalysis"]

        self.assertEqual(analysis["status"], "available")
        self.assertAlmostEqual(analysis["day_imbalance_pct"], -2.29, places=2)
        self.assertAlmostEqual(analysis["night_imbalance_pct"], -3.75, places=2)
        self.assertTrue(any("外資日盤" in item for item in analysis["volume_divergences"]))
        self.assertIn("投信", analysis["look"])
        self.assertIn("自營商", analysis["look"])
        self.assertIn("不單憑本區塊追多或追空", analysis["target"])

    def test_amount_volume_direction_comparison_is_explicit(self):
        analysis = build_option_force_analysis(self.force_rows, self.volume_rows)
        self.assertEqual(analysis["status"], "available")
        self.assertEqual(len(analysis["volume_divergences"]), 1)
        self.assertIn("外資日盤", analysis["volume_divergences"][0])
        self.assertIn("4 組同向、1 組背離、1 組中性", analysis["compass"])
        self.assertIn("來源日淨－夜淨差 -0.41 億元", analysis["look"])
        self.assertEqual(len(analysis["volume_concordant"]), 4)
        self.assertEqual(len(analysis["volume_neutral"]), 1)

    def test_missing_values_are_not_silently_converted_to_zero(self):
        rows = [list(row) for row in self.force_rows]
        rows[1][4] = "unavailable"
        analysis = build_option_force_analysis(rows, self.volume_rows)
        self.assertEqual(analysis["status"], "unavailable")
        self.assertIn("暫停法人方向判讀", analysis["look"])

    def test_inconsistent_net_or_total_blocks_directional_conclusion(self):
        rows = [list(row) for row in self.force_rows]
        rows[1][3] = "-2.50"
        analysis = build_option_force_analysis(rows, self.volume_rows)
        self.assertEqual(analysis["status"], "inconsistent")
        self.assertIn("一致性檢查未通過", analysis["compass"])

    def test_day_minus_night_is_not_mislabeled_as_day_over_day_change(self):
        analysis = build_option_force_analysis(self.force_rows, self.volume_rows)
        self.assertAlmostEqual(analysis["day_minus_night"], -0.41, places=2)
        self.assertIn("日淨－夜淨」是兩個時段淨額相減", analysis["method"])


if __name__ == "__main__":
    unittest.main()
