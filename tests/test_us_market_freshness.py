import unittest

from src.sources.us_market import _apply_asia_freshness


class AsianMarketFreshnessTests(unittest.TestCase):
    def _rows(self, dates):
        return [
            (name, {
                "symbol": symbol,
                "price": price,
                "change": 10.0,
                "pct": 1.0,
                "date": day,
                "source": "Yahoo Finance Chart API",
                "ok": True,
            })
            for name, symbol, price, day in dates
        ]

    def test_entire_asia_batch_older_than_t0_is_marked_unavailable(self):
        rows = self._rows([
            ("日經225", "^N225", 59444.21, "2026-11-19"),
            ("韓國KOSPI", "^KS11", 5137.89, "2026-11-19"),
            ("香港恆生", "^HSI", 22841.62, "2026-11-19"),
        ])

        result = _apply_asia_freshness(rows, "2026-11-20")

        for _, quote in result:
            self.assertTrue(quote["stale"])
            self.assertFalse(quote["ok"])
            self.assertIsNone(quote["price"])
            self.assertIsNone(quote["change"])
            self.assertIsNone(quote["pct"])
            self.assertEqual(quote["date"], "2026-11-19")
            self.assertIn("早於或無法核對報告 T0", quote["stale_reason"])

    def test_batch_with_t0_data_is_not_rejected(self):
        rows = self._rows([
            ("日經225", "^N225", 56000.0, "2026-11-20"),
            ("韓國KOSPI", "^KS11", 48000.0, "2026-11-20"),
        ])

        result = _apply_asia_freshness(rows, "2026-11-20")

        for _, quote in result:
            self.assertNotIn("stale", quote)
            self.assertTrue(quote["ok"])
            self.assertIsNotNone(quote["price"])

    def test_older_single_market_is_rejected_when_another_market_has_t0(self):
        # Freshness is evaluated per index; another market's T0 quote cannot
        # make this older quote appear current.
        rows = self._rows([
            ("日經225", "^N225", 56000.0, "2026-11-20"),
            ("香港恆生", "^HSI", 22841.62, "2026-11-19"),
        ])

        result = _apply_asia_freshness(rows, "2026-11-20")

        self.assertFalse(result[0][1].get("stale", False))
        self.assertEqual(result[0][1]["price"], 56000.0)
        self.assertTrue(result[1][1]["stale"])
        self.assertFalse(result[1][1]["ok"])
        self.assertIsNone(result[1][1]["price"])
        self.assertIsNone(result[1][1]["change"])
        self.assertIsNone(result[1][1]["pct"])

    def test_missing_expected_date_preserves_legacy_behavior(self):
        rows = self._rows([
            ("日經225", "^N225", 59444.21, "2026-11-19"),
        ])

        result = _apply_asia_freshness(rows, None)

        self.assertEqual(result[0][1]["price"], 59444.21)
        self.assertNotIn("stale", result[0][1])


if __name__ == "__main__":
    unittest.main()
