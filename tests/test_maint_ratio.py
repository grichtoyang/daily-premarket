import unittest
from datetime import datetime, timezone
from unittest.mock import patch

from src.sources import maint_ratio


class MaintenanceRatioSourceTests(unittest.TestCase):
    def test_wantgoo_rejects_previous_date(self):
        previous = int(datetime(2026, 10, 29, tzinfo=timezone.utc).timestamp() * 1000)
        response = type("Response", (), {
            "status_code": 200,
            "raise_for_status": lambda self: None,
            "json": lambda self: [{"date": previous, "marginRatio": 1.784}],
        })()
        with patch.object(maint_ratio.requests, "get", return_value=response):
            result = maint_ratio._wantgoo("2026-10-30")
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])

    def test_wantgoo_accepts_exact_t0(self):
        exact = int(datetime(2026, 10, 30, tzinfo=timezone.utc).timestamp() * 1000)
        response = type("Response", (), {
            "status_code": 200,
            "raise_for_status": lambda self: None,
            "json": lambda self: [{"date": exact, "marginRatio": 1.7061}],
        })()
        with patch.object(maint_ratio.requests, "get", return_value=response):
            result = maint_ratio._wantgoo("2026-10-30")
        self.assertTrue(result["ok"])
        self.assertEqual(result["date"], "2026-10-30")
        self.assertEqual(result["ratio"], 170.61)

    def test_stale_wantgoo_cannot_override_exact_stockintelli(self):
        with patch.object(maint_ratio, "_wantgoo", return_value={
            "ratio": None, "date": None, "ok": False
        }), patch.object(maint_ratio, "_stockintelli", return_value={
            "ratio": 171.80, "date": "2026-10-30", "ok": True
        }), patch.object(maint_ratio, "_istock", return_value={
            "ratio": 170.61, "date": "2026-10-30", "ok": True
        }):
            result = maint_ratio.get("2026-10-30")
        self.assertEqual(result["source"], "stockintelli")
        self.assertEqual(result["ratio"], 171.80)

    def test_all_sources_without_t0_return_unavailable(self):
        unavailable = {"ratio": None, "date": None, "ok": False}
        with patch.object(maint_ratio, "_wantgoo", return_value=unavailable), \
             patch.object(maint_ratio, "_stockintelli", return_value=unavailable), \
             patch.object(maint_ratio, "_istock", return_value=unavailable):
            result = maint_ratio.get("2026-10-30")
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])


if __name__ == "__main__":
    unittest.main()
