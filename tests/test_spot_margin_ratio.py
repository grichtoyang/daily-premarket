import unittest
from unittest.mock import patch

from src.sources.spot import _get_margin_ratio


T0 = "2026-10-30"


class SpotMarginRatioPolicyTests(unittest.TestCase):
    @patch("src.sources.spot.blave_maint_ratio.get")
    def test_blave_is_primary_and_manual_is_not_consulted_when_blave_is_valid(self, get_blave):
        get_blave.return_value = {"ok": True, "date": T0, "ratio": 171.754}
        result = _get_margin_ratio(T0, {
            "MANUAL_LISTED_MARGIN_RATIO": "172.1",
            "MANUAL_LISTED_MARGIN_RATIO_DATE": T0,
        })
        get_blave.assert_called_once_with(T0, timeout=4)
        self.assertEqual(result["ratio"], 171.754)
        self.assertIn("Blave", result["source"])
        self.assertIn(T0, result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    def test_manual_is_the_only_fallback_and_requires_exact_t0(self, get_blave):
        get_blave.return_value = {"ok": False, "date": None, "ratio": None}
        result = _get_margin_ratio(T0, {
            "MANUAL_LISTED_MARGIN_RATIO": "172.1",
            "MANUAL_LISTED_MARGIN_RATIO_DATE": T0,
        })
        get_blave.assert_called_once_with(T0, timeout=4)
        self.assertEqual(result["ratio"], 172.1)
        self.assertIn("人工輸入", result["source"])
        self.assertIn(T0, result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    def test_wrong_date_manual_input_is_rejected_without_previous_value(self, get_blave):
        get_blave.return_value = {"ok": False, "date": None, "ratio": None}
        result = _get_margin_ratio(T0, {
            "MANUAL_LISTED_MARGIN_RATIO": "172.1",
            "MANUAL_LISTED_MARGIN_RATIO_DATE": "2026-10-29",
        })
        get_blave.assert_called_once_with(T0, timeout=4)
        self.assertIsNone(result["ratio"])
        self.assertIn("unavailable", result["source"])
        self.assertIn("融資餘額", result["note"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    def test_invalid_blave_value_falls_back_to_valid_manual_input(self, get_blave):
        get_blave.return_value = {"ok": True, "date": T0, "ratio": 0}
        result = _get_margin_ratio(T0, {
            "MANUAL_LISTED_MARGIN_RATIO": "172.1",
            "MANUAL_LISTED_MARGIN_RATIO_DATE": T0,
        })
        self.assertEqual(result["ratio"], 172.1)
        self.assertIn("人工輸入", result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    def test_unavailable_does_not_block_existing_margin_indicators(self, get_blave):
        get_blave.return_value = {"ok": False, "date": None, "ratio": None}
        result = _get_margin_ratio(T0, {})
        self.assertIsNone(result["ratio"])
        self.assertIn("unavailable", result["source"])
        self.assertIn("融資增減", result["note"])
        self.assertIn("融券餘額", result["note"])
        self.assertIn("融券增減", result["note"])


if __name__ == "__main__":
    unittest.main()
