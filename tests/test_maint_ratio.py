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

    def test_listed_only_sources_cannot_override_combined_istock(self):
        with patch.object(maint_ratio, "_wantgoo", return_value={
            "ratio": 171.75, "date": "2026-10-30", "ok": True, "source": "wantgoo"
        }), patch.object(maint_ratio, "_stockintelli", return_value={
            "ratio": 171.80, "date": "2026-10-30", "ok": True
        }), patch.object(maint_ratio, "_istock", return_value={
            "ratio": 170.61, "date": "2026-10-30", "ok": True
        }):
            result = maint_ratio.get("2026-10-30")
        self.assertEqual(result["source"], "istock_combined")
        self.assertEqual(result["ratio"], 170.61)

    def test_listed_only_sources_are_not_market_wide_fallback(self):
        with patch.object(maint_ratio, "_wantgoo", return_value={
            "ratio": 171.75, "date": "2026-10-30", "ok": True
        }), patch.object(maint_ratio, "_stockintelli", return_value={
            "ratio": 171.80, "date": "2026-10-30", "ok": True
        }), patch.object(maint_ratio, "_istock", return_value={
            "ratio": None, "date": None, "ok": False
        }):
            result = maint_ratio.get("2026-10-30")
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])
        self.assertEqual(result["source"], "unavailable")

    def test_all_sources_without_t0_return_unavailable(self):
        unavailable = {"ratio": None, "date": None, "ok": False}
        with patch.object(maint_ratio, "_wantgoo", return_value=unavailable), \
             patch.object(maint_ratio, "_stockintelli", return_value=unavailable), \
             patch.object(maint_ratio, "_istock", return_value=unavailable):
            result = maint_ratio.get("2026-10-30")
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])

    def test_istock_extracts_combined_ratio_not_listed_only(self):
        html = """
        <html><body>
        <div>大盤融資維持率</div><div>171.75%</div>
        <div>上櫃融資維持率</div><div>167.14%</div>
        <div>上市櫃整體維持率</div><div>170.61%</div>
        <div>資料日期：2026-10-30</div>
        </body></html>
        """
        result = maint_ratio._parse_istock_html("2026-10-30", html)
        self.assertTrue(result["ok"])
        self.assertEqual(result["date"], "2026-10-30")
        self.assertEqual(result["ratio"], 170.61)

    def test_istock_rejects_stale_date(self):
        html = """
        <div>上市櫃整體維持率</div><div>170.61%</div>
        <div>資料日期：2026-10-29</div>
        """
        result = maint_ratio._parse_istock_html("2026-10-30", html)
        self.assertFalse(result["ok"])
        self.assertIsNone(result["ratio"])


if __name__ == "__main__":
    unittest.main()
