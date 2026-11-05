import unittest

from src.sources.taifex import _complete_sum, _complete_ratio, _oi_distribution


class CompleteAggregateContractTests(unittest.TestCase):
    def test_futures_institutional_oi_requires_all_three_values(self):
        self.assertEqual(_complete_sum([100, 20, 3]), 123)
        self.assertIsNone(_complete_sum([100, None, 3]))
        self.assertIsNone(_complete_sum([None, None, None]))

    def test_zero_is_a_valid_oi_or_volume_value(self):
        self.assertEqual(_complete_sum([0, 2, 3]), 5)
        self.assertEqual(_complete_sum([0, 0]), 0)

    def test_option_chain_empty_side_is_unavailable(self):
        self.assertIsNone(_complete_sum([]))
        self.assertIsNone(_complete_ratio(100, None))

    def test_option_chain_partial_row_invalidates_only_that_aggregate(self):
        self.assertIsNone(_complete_sum([10, None, 5]))
        self.assertEqual(_complete_sum([10, 0, 5]), 15)

    def test_ratios_require_complete_nonzero_denominator(self):
        self.assertEqual(_complete_ratio(20, 10), 2)
        self.assertIsNone(_complete_ratio(20, 0))
        self.assertIsNone(_complete_ratio(None, 10))
        self.assertIsNone(_complete_ratio(20, None))

    def test_oi_distribution_uses_complete_denominator(self):
        rows = [{"strike": 100, "open_interest": 25},
                {"strike": 110, "open_interest": 75}]
        result = _oi_distribution(rows)
        self.assertEqual([row["pct"] for row in result], [25.0, 75.0])

    def test_partial_oi_distribution_preserves_values_but_hides_percentages(self):
        rows = [{"strike": 100, "open_interest": 25},
                {"strike": 110, "open_interest": None},
                {"strike": 120, "open_interest": 75}]
        result = _oi_distribution(rows)
        self.assertEqual([row["oi"] for row in result], [25, 75, None])
        self.assertTrue(all(row["pct"] is None for row in result))

    def test_empty_oi_distribution_is_empty(self):
        self.assertEqual(_oi_distribution([]), [])


if __name__ == "__main__":
    unittest.main()
