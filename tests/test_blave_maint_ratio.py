import unittest
from unittest.mock import Mock, patch

from src.sources import blave_maint_ratio


class BlaveMaintenanceRatioTests(unittest.TestCase):
    @patch("src.sources.blave_maint_ratio.requests.get")
    def test_returns_exact_t0_value(self, get):
        get.return_value = Mock(
            json=lambda: {"data": [
                {"date": "2026-10-29", "maintenance_ratio": 172.1},
                {"date": "2026-10-30", "maintenance_ratio": 171.754},
            ]},
            raise_for_status=lambda: None,
        )
        result = blave_maint_ratio.get("2026-10-30")
        self.assertTrue(result["ok"])
        self.assertEqual(result["ratio"], 171.754)
        self.assertEqual(result["date"], "2026-10-30")

    @patch("src.sources.blave_maint_ratio.requests.get")
    def test_rejects_latest_value_when_t0_missing(self, get):
        get.return_value = Mock(
            json=lambda: {"data": [
                {"date": "2026-10-29", "maintenance_ratio": 172.1},
            ]},
            raise_for_status=lambda: None,
        )
        result = blave_maint_ratio.get("2026-10-30")
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])

    @patch("src.sources.blave_maint_ratio.requests.get")
    def test_rejects_invalid_ratio(self, get):
        get.return_value = Mock(
            json=lambda: {"data": [
                {"date": "2026-10-30", "maintenance_ratio": 0},
            ]},
            raise_for_status=lambda: None,
        )
        result = blave_maint_ratio.get("2026-10-30")
        self.assertFalse(result["ok"])


if __name__ == "__main__":
    unittest.main()
