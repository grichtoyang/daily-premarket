import unittest
from unittest.mock import patch

from src.sources import taifex


class Top10RolloverBaselineTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = {
            "date": "2026-11-17",
            "data": {
                "top10fut": [
                    {
                        "Date": "20261116",
                        "SettlementMonth": "202611",
                        "Top10Buy": "12000",
                        "Top10Sell": "9000",
                    }
                ],
                "top10opt": [
                    {
                        "Date": "20261116",
                        "SettlementMonth": "202611",
                        "CallPut": "買權",
                        "Top10Buy": "5000",
                        "Top10Sell": "4000",
                    },
                    {
                        "Date": "20261116",
                        "SettlementMonth": "202611",
                        "CallPut": "賣權",
                        "Top10Buy": "4500",
                        "Top10Sell": "4200",
                    },
                ],
            },
        }

    @patch("src.sources.taifex.snapshot_bundle")
    def test_contract_month_mismatch_returns_rollover_baseline_reset(self, snapshot_bundle):
        snapshot_bundle.return_value = self.snapshot
        result = taifex.snap_top10_change(
            "202612", "2026-11-18", 2500, cur_date="2026-11-18"
        )
        self.assertEqual(result["status"], "rollover_baseline_reset")
        self.assertIsNone(result["chg"])
        self.assertEqual(result["prev_month"], "202611")
        self.assertEqual(result["current_month"], "202612")
        self.assertIn("不跨月相減", result["reason"])

    @patch("src.sources.taifex.snapshot_bundle")
    def test_options_rollover_is_filtered_by_callput(self, snapshot_bundle):
        snapshot_bundle.return_value = self.snapshot
        result = taifex.snap_top10_change(
            "202612", "2026-11-18", 1000,
            cur_date="2026-11-18", dataset="top10opt", callput="買權"
        )
        self.assertEqual(result["status"], "rollover_baseline_reset")
        self.assertEqual(result["prev_month"], "202611")

    @patch("src.sources.taifex.snapshot_bundle")
    def test_same_contract_month_still_calculates_daily_change(self, snapshot_bundle):
        snapshot_bundle.return_value = self.snapshot
        result = taifex.snap_top10_change(
            "202611", "2026-11-18", 3500, cur_date="2026-11-18"
        )
        self.assertEqual(result["chg"], 500)
        self.assertEqual(result["status"], "available")

    @patch("src.sources.taifex.snapshot_bundle")
    def test_missing_snapshot_remains_unavailable_not_rollover(self, snapshot_bundle):
        snapshot_bundle.return_value = None
        self.assertIsNone(
            taifex.snap_top10_change("202612", "2026-11-18", 2500)
        )


if __name__ == "__main__":
    unittest.main()
