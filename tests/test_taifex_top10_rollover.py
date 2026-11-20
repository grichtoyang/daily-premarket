import unittest
from unittest.mock import patch

from src.sources import taifex


class Top10RolloverBaselineTests(unittest.TestCase):
    def setUp(self):
        self.prev_day_patcher = patch(
            "src.sources.taifex._previous_trading_day_iso",
            side_effect=lambda day: {
                "2026-11-19": "2026-11-18",
                "2026-11-18": "2026-11-17",
                "2026-11-17": "2026-11-16",
            }.get(day),
        )
        self.prev_day_patcher.start()
        self.addCleanup(self.prev_day_patcher.stop)
        self.snapshot = {
            "date": "2026-11-19",
            "data": {
                "top10fut": [
                    {
                        "Date": "20261118",
                        "SettlementMonth": "202611",
                        "Top10Buy": "12000",
                        "Top10Sell": "9000",
                    }
                ],
                "top10opt": [
                    {
                        "Date": "20261118",
                        "SettlementMonth": "202611",
                        "CallPut": "買權",
                        "Top10Buy": "5000",
                        "Top10Sell": "4000",
                    },
                    {
                        "Date": "20261118",
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
            "202612", "2026-11-19", 2500, cur_date="2026-11-19"
        )
        snapshot_bundle.assert_called_once_with("2026-11-19")
        self.assertEqual(result["status"], "rollover_baseline_reset")
        self.assertIsNone(result["chg"])
        self.assertEqual(result["prev_month"], "202611")
        self.assertEqual(result["current_month"], "202612")
        self.assertIn("不跨月相減", result["reason"])

    @patch("src.sources.taifex.snapshot_bundle")
    def test_reverse_contract_month_is_unavailable_not_rollover(self, snapshot_bundle):
        snapshot_bundle.return_value = self.snapshot
        result = taifex.snap_top10_change(
            "202610", "2026-11-19", 2500, cur_date="2026-11-19"
        )
        self.assertIsNone(result)

    @patch("src.sources.taifex.snapshot_bundle")
    def test_options_rollover_is_filtered_by_callput(self, snapshot_bundle):
        snapshot_bundle.return_value = self.snapshot
        result = taifex.snap_top10_change(
            "202612", "2026-11-19", 1000,
            cur_date="2026-11-19", dataset="top10opt", callput="買權"
        )
        self.assertEqual(result["status"], "rollover_baseline_reset")
        self.assertEqual(result["prev_month"], "202611")

    @patch("src.sources.taifex.snapshot_bundle")
    def test_same_contract_month_recovers_on_next_trading_day_after_rollover(self, snapshot_bundle):
        recovered = {
            **self.snapshot,
            "data": {
                **self.snapshot["data"],
                "top10fut": [{
                    "Date": "20261118",
                    "SettlementMonth": "202612",
                    "Top10Buy": "12000",
                    "Top10Sell": "9000",
                }],
            },
        }
        snapshot_bundle.return_value = recovered
        result = taifex.snap_top10_change(
            "202612", "2026-11-19", 3500, cur_date="2026-11-19"
        )
        snapshot_bundle.assert_called_once_with("2026-11-19")
        self.assertEqual(result["chg"], 500)
        self.assertEqual(result["status"], "available")



    @patch("src.sources.taifex.snapshot_bundle")
    @patch(
        "src.sources.taifex._previous_trading_day_iso",
        side_effect=lambda day: {
            "2026-11-16": "2026-11-13",
            "2026-11-13": "2026-11-12",
        }.get(day),
    )
    def test_uses_previous_trading_day_across_weekend(self, previous_day, snapshot_bundle):
        weekend_data = {
            key: [
                {**row, "Date": "20261113"}
                for row in rows
            ]
            for key, rows in self.snapshot["data"].items()
        }
        snapshot_bundle.return_value = {
            **self.snapshot,
            "date": "2026-11-16",
            "data": weekend_data,
        }
        result = taifex.snap_top10_change(
            "202611", "2026-11-16", 3500, cur_date="2026-11-16"
        )
        snapshot_bundle.assert_called_once_with("2026-11-16")
        self.assertEqual(result["status"], "available")

    @patch("src.sources.taifex.snapshot_bundle")
    def test_top10_source_date_is_independently_trusted_when_position_flag_is_false(self, snapshot_bundle):
        untrusted_positions = dict(self.snapshot, trust_pos=False)
        snapshot_bundle.return_value = untrusted_positions
        result = taifex.snap_top10_change(
            "202611", "2026-11-19", 3500, cur_date="2026-11-19"
        )
        self.assertEqual(result["status"], "available")
        self.assertEqual(result["chg"], 500)

    @patch("src.sources.taifex.snapshot_bundle")
    def test_snapshot_date_mismatch_is_rejected(self, snapshot_bundle):
        bad_snapshot = dict(self.snapshot, date="2026-11-18")
        snapshot_bundle.return_value = bad_snapshot
        self.assertIsNone(
            taifex.snap_top10_change("202612", "2026-11-19", 2500)
        )

    @patch("src.sources.taifex.snapshot_bundle")
    def test_inconsistent_source_dates_are_rejected(self, snapshot_bundle):
        bad_snapshot = {
            **self.snapshot,
            "data": {
                **self.snapshot["data"],
                "top10fut": self.snapshot["data"]["top10fut"] + [{
                    "Date": "20261115",
                    "SettlementMonth": "202612",
                    "Top10Buy": "13000",
                    "Top10Sell": "9500",
                }],
            },
        }
        snapshot_bundle.return_value = bad_snapshot
        self.assertIsNone(
            taifex.snap_top10_change("202612", "2026-11-19", 2500)
        )


    @patch("src.sources.taifex.snapshot_bundle")
    def test_consistently_stale_source_rows_are_rejected(self, snapshot_bundle):
        stale_data = {
            key: [
                {**row, "Date": "20261117"}
                for row in rows
            ]
            for key, rows in self.snapshot["data"].items()
        }
        snapshot_bundle.return_value = {
            **self.snapshot,
            "data": stale_data,
        }
        self.assertIsNone(
            taifex.snap_top10_change("202611", "2026-11-19", 3500)
        )

    @patch("src.sources.taifex.snapshot_bundle")
    def test_future_dated_source_rows_are_rejected(self, snapshot_bundle):
        bad_snapshot = {
            **self.snapshot,
            "data": {
                **self.snapshot["data"],
                "top10fut": [{
                    "Date": "20261119",
                    "SettlementMonth": "202611",
                    "Top10Buy": "12000",
                    "Top10Sell": "9000",
                }],
            },
        }
        snapshot_bundle.return_value = bad_snapshot
        self.assertIsNone(
            taifex.snap_top10_change("202611", "2026-11-19", 3500)
        )

    @patch("src.sources.taifex.snapshot_bundle")
    def test_invalid_settlement_month_sentinels_do_not_override_valid_rollover_baseline(self, snapshot_bundle):
        data = {
            "top10fut": list(self.snapshot["data"]["top10fut"]),
            "top10opt": list(self.snapshot["data"]["top10opt"]),
        }
        for dataset, callput in (
            ("top10fut", None),
            ("top10opt", "買權"),
            ("top10opt", "賣權"),
        ):
            sentinels = [
                {
                    "Date": "20261118",
                    "SettlementMonth": "666666",
                    "Top10Buy": "1",
                    "Top10Sell": "1",
                    **({"CallPut": callput} if callput else {}),
                },
                {
                    "Date": "20261118",
                    "SettlementMonth": "999912",
                    "Top10Buy": "1",
                    "Top10Sell": "1",
                    **({"CallPut": callput} if callput else {}),
                },
            ]
            data[dataset].extend(sentinels)

        snapshot_bundle.return_value = {**self.snapshot, "data": data}
        cases = (
            ("top10fut", None),
            ("top10opt", "買權"),
            ("top10opt", "賣權"),
        )
        for dataset, callput in cases:
            with self.subTest(dataset=dataset, callput=callput):
                result = taifex.snap_top10_change(
                    "202612", "2026-11-19", 2500,
                    cur_date="2026-11-19", dataset=dataset, callput=callput
                )
                self.assertEqual(result["status"], "rollover_baseline_reset")
                self.assertEqual(result["prev_month"], "202611")

    @patch("src.sources.taifex.snapshot_bundle")
    def test_rollover_baseline_is_independent_of_snapshot_row_order(self, snapshot_bundle):
        rows = self.snapshot["data"]["top10fut"] + [
            {
                "Date": "20261118",
                "SettlementMonth": "666666",
                "Top10Buy": "1",
                "Top10Sell": "1",
            },
            {
                "Date": "20261118",
                "SettlementMonth": "999912",
                "Top10Buy": "1",
                "Top10Sell": "1",
            },
        ]
        results = []
        for ordered_rows in (rows, list(reversed(rows))):
            snapshot_bundle.return_value = {
                **self.snapshot,
                "data": {**self.snapshot["data"], "top10fut": ordered_rows},
            }
            results.append(taifex.snap_top10_change(
                "202612", "2026-11-19", 2500, cur_date="2026-11-19"
            ))
        for result in results:
            self.assertEqual(result["status"], "rollover_baseline_reset")
            self.assertEqual(result["prev_month"], "202611")

    @patch("src.sources.taifex.snapshot_bundle")
    def test_snapshot_with_only_invalid_settlement_months_is_not_rollover(self, snapshot_bundle):
        invalid_rows = [
            {
                "Date": "20261118",
                "SettlementMonth": sentinel,
                "Top10Buy": "1",
                "Top10Sell": "1",
            }
            for sentinel in ("666666", "999912", "000000", "202613")
        ]
        snapshot_bundle.return_value = {
            **self.snapshot,
            "data": {**self.snapshot["data"], "top10fut": invalid_rows},
        }
        self.assertIsNone(
            taifex.snap_top10_change("202612", "2026-11-19", 2500)
        )

    @patch("src.sources.taifex.snapshot_bundle")
    def test_missing_snapshot_remains_unavailable_not_rollover(self, snapshot_bundle):
        snapshot_bundle.return_value = None
        self.assertIsNone(
            taifex.snap_top10_change("202612", "2026-11-19", 2500)
        )


if __name__ == "__main__":
    unittest.main()
