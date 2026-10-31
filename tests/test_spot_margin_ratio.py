import unittest
from unittest.mock import patch

from src.sources.spot import _get_margin_ratio, SELF_BUILT_RATIO_TIMEOUT, BLAVE_RATIO_TIMEOUT


T0 = "2026-10-30"


def self_built_result(ratio=171.747):
    return {
        "ok": True, "date": T0, "ratio": ratio, "coverage": 1.0,
        "financed_security_count": 1238, "priced_security_count": 1238,
        "stale_price_security_count": 4,
        "price_date_min": "20260402", "price_date_max": "20261030",
    }


class SpotMarginRatioPolicyTests(unittest.TestCase):
    @patch("src.sources.spot.blave_maint_ratio.get")
    @patch("src.sources.spot.listed_maint_ratio.get")
    def test_self_built_is_primary_and_blave_is_cross_check(self, get_self, get_blave):
        get_self.return_value = self_built_result()
        get_blave.return_value = {"ok": True, "date": T0, "ratio": 171.754}
        result = _get_margin_ratio(T0, {})
        get_self.assert_called_once_with(T0, timeout=SELF_BUILT_RATIO_TIMEOUT)
        get_blave.assert_called_once_with(T0, timeout=BLAVE_RATIO_TIMEOUT)
        self.assertEqual(result["ratio"], 171.747)
        self.assertIn("TWSE 上市自建估算", result["source"])
        self.assertIn("Blave 同 T0 交叉驗證", result["source"])
        self.assertIn("0.007 個百分點", result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    @patch("src.sources.spot.listed_maint_ratio.get")
    def test_blave_cross_check_failure_does_not_discard_self_built_value(self, get_self, get_blave):
        get_self.return_value = self_built_result()
        get_blave.return_value = {"ok": False, "date": None, "ratio": None, "reason": "timeout"}
        result = _get_margin_ratio(T0, {})
        self.assertEqual(result["ratio"], 171.747)
        self.assertIn("TWSE 上市自建估算", result["source"])
        self.assertIn("Blave 交叉驗證未取得", result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    @patch("src.sources.spot.listed_maint_ratio.get")
    def test_blave_is_fallback_only_when_self_built_fails(self, get_self, get_blave):
        get_self.return_value = {"ok": False, "date": T0, "ratio": None, "reason": "TWSE timeout"}
        get_blave.return_value = {"ok": True, "date": T0, "ratio": 171.754}
        result = _get_margin_ratio(T0, {})
        self.assertEqual(result["ratio"], 171.754)
        self.assertIn("Blave", result["source"])
        self.assertIn("自建計算備援", result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    @patch("src.sources.spot.listed_maint_ratio.get")
    def test_manual_is_last_fallback_and_requires_exact_t0(self, get_self, get_blave):
        get_self.return_value = {"ok": False, "date": T0, "ratio": None, "reason": "unavailable"}
        get_blave.return_value = {"ok": False, "date": None, "ratio": None, "reason": "timeout"}
        result = _get_margin_ratio(T0, {
            "MANUAL_LISTED_MARGIN_RATIO": "172.1",
            "MANUAL_LISTED_MARGIN_RATIO_DATE": T0,
        })
        self.assertEqual(result["ratio"], 172.1)
        self.assertIn("人工輸入", result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    @patch("src.sources.spot.listed_maint_ratio.get")
    def test_wrong_date_manual_input_is_rejected(self, get_self, get_blave):
        get_self.return_value = {"ok": False, "date": T0, "ratio": None, "reason": "unavailable"}
        get_blave.return_value = {"ok": False, "date": None, "ratio": None, "reason": "timeout"}
        result = _get_margin_ratio(T0, {
            "MANUAL_LISTED_MARGIN_RATIO": "172.1",
            "MANUAL_LISTED_MARGIN_RATIO_DATE": "2026-10-29",
        })
        self.assertIsNone(result["ratio"])
        self.assertIn("unavailable", result["source"])

    @patch("src.sources.spot.blave_maint_ratio.get")
    @patch("src.sources.spot.listed_maint_ratio.get")
    def test_all_sources_unavailable_does_not_raise_or_block_other_fields(self, get_self, get_blave):
        get_self.return_value = {"ok": False, "date": T0, "ratio": None, "reason": "timeout"}
        get_blave.return_value = {"ok": False, "date": None, "ratio": None, "reason": "timeout"}
        result = _get_margin_ratio(T0, {})
        self.assertIsNone(result["ratio"])
        self.assertIn("unavailable", result["source"])
        self.assertIn("DATA_REPORT", result["note"])

    def test_total_source_wait_budget_is_bounded(self):
        self.assertEqual(SELF_BUILT_RATIO_TIMEOUT + BLAVE_RATIO_TIMEOUT, 13)


if __name__ == "__main__":
    unittest.main()
