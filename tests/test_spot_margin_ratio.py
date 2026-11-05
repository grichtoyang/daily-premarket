import unittest
from datetime import datetime
from zoneinfo import ZoneInfo
from unittest.mock import patch

from src.sources import spot, spot_raw, twse, twse_proxy
from src.sources.spot import _get_margin_ratio, SELF_BUILT_RATIO_TIMEOUT, BLAVE_RATIO_TIMEOUT
from src.fetch_data import _sbl_status_line, _sbl_publication_line, _sbl_market_table


T0 = "2026-10-30"


def self_built_result(ratio=171.747):
    return {
        "ok": True, "date": T0, "ratio": ratio, "coverage": 1.0,
        "financed_security_count": 1238, "priced_security_count": 1238,
        "stale_price_security_count": 4,
        "price_date_min": "20260402", "price_date_max": "20261030",
    }


class SblMarketReportTests(unittest.TestCase):
    def test_report_shows_listed_otc_and_combined_values_separately(self):
        table = _sbl_market_table({
            "listed_sale_bal": 1200, "otc_sale_bal": 300, "sale_bal": 1500,
            "listed_sale_chg": 100, "otc_sale_chg": -20, "sale_chg": 80,
        })
        self.assertIn("| 借券賣出餘額 | 1,200 | 300 | 1,500 | 張 |", table)
        self.assertIn("| 借券賣出增減 | 100 | -20 | 80 | 張 |", table)

    def test_missing_market_is_not_filled_from_combined_value(self):
        table = _sbl_market_table({
            "listed_sale_bal": 1200, "otc_sale_bal": None, "sale_bal": 1200,
            "listed_sale_chg": 100, "otc_sale_chg": None, "sale_chg": 100,
        })
        self.assertIn("| 借券賣出餘額 | 1,200 | unavailable | 1,200 | 張 |", table)
        self.assertIn("| 借券賣出增減 | 100 | unavailable | 100 | 張 |", table)


class SblReportStatusOutputTests(unittest.TestCase):
    def test_complete_status_is_written_explicitly(self):
        self.assertEqual(_sbl_status_line("借券賣出餘額", "complete"), "- 借券賣出餘額完整性：`complete`")

    def test_partial_status_is_written_explicitly(self):
        self.assertEqual(_sbl_status_line("借券賣出餘額", "partial"), "- 借券賣出餘額完整性：`partial`")

    def test_unavailable_status_is_written_explicitly(self):
        self.assertEqual(_sbl_status_line("借券賣出餘額", "unavailable"), "- 借券賣出餘額完整性：`unavailable`")

    def test_missing_or_unknown_status_fails_closed(self):
        self.assertEqual(_sbl_status_line("借券賣出餘額", None), "- 借券賣出餘額完整性：`unavailable`")
        self.assertEqual(_sbl_status_line("借券賣出餘額", "unknown"), "- 借券賣出餘額完整性：`unavailable`")

class SblPublicationStatusTests(unittest.TestCase):
    TAIPEI = ZoneInfo("Asia/Taipei")

    def test_tpex_pending_before_final_public_page_update(self):
        result = spot_raw._sbl_publication_metadata("20261105", "22:30", now=datetime(2026, 11, 5, 22, 29, tzinfo=self.TAIPEI))
        self.assertEqual(result["status"], "pending")
        self.assertIsNone(result["production_time"])

    def test_twse_pending_before_official_production_time(self):
        result = spot_raw._sbl_publication_metadata("20261105", "23:30", now=datetime(2026, 11, 5, 23, 29, tzinfo=self.TAIPEI))
        self.assertEqual(result["status"], "pending")

    def test_after_schedule_without_valid_data_remains_unknown(self):
        result = spot_raw._sbl_publication_metadata("20261105", "22:30", now=datetime(2026, 11, 5, 22, 31, tzinfo=self.TAIPEI))
        self.assertEqual(result["status"], "unknown")
        self.assertIsNone(result["production_time"])

    def test_matching_data_observed_after_schedule_is_not_claimed_as_published(self):
        result = spot_raw._sbl_publication_metadata("20261105", "22:30", now=datetime(2026, 11, 5, 22, 31, tzinfo=self.TAIPEI), data_available=True)
        self.assertEqual(result["status"], "available_after_schedule")
        self.assertEqual(result["checked_at"], "2026-11-05T22:31:00+08:00")
        self.assertIsNone(result["production_time"])

    def test_explicit_source_production_time_confirms_published(self):
        result = spot_raw._sbl_publication_metadata("20261105", "22:30", actual_time="2235")
        self.assertEqual(result["status"], "published")
        self.assertEqual(result["production_time"], "2235")

    def test_report_line_separates_source_time_from_query_time(self):
        line = _sbl_publication_line("TPEx S47", {"data_date": "20261105", "expected_time": "22:30", "production_time": None, "checked_at": "2026-11-05T22:31:00+08:00", "status": "available_after_schedule"})
        self.assertIn("來源回報產製時間：`unavailable`", line)
        self.assertIn("本次查詢時間：`2026-11-05T22:31:00+08:00`", line)
        self.assertIn("狀態：`available_after_schedule`", line)

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



class _Response:
    status_code = 200

    def __init__(self, payload):
        self.payload = payload

    def json(self):
        return self.payload


class InstitutionalDateValidationTests(unittest.TestCase):
    def test_normalizes_gregorian_and_roc_dates(self):
        self.assertEqual(twse._normalize_date8("2026-11-05"), "20261105")
        self.assertEqual(twse._normalize_date8("115/11/05"), "20261105")

    @patch("requests.get")
    def test_proxy_rejects_actual_date_mismatch(self, get):
        get.return_value = _Response({
            "ok": True, "actual_date": "20261104", "date": "20261105",
            "date_mismatch": True, "data": {"foreign": 12},
        })
        self.assertIsNone(twse._proxy_institutional("20261105"))

    @patch("requests.get")
    def test_proxy_rejects_missing_actual_date(self, get):
        get.return_value = _Response({
            "ok": True, "date": "20261105", "data": {"foreign": 12},
        })
        self.assertIsNone(twse._proxy_institutional("20261105"))

    @patch("requests.get")
    def test_proxy_accepts_matching_actual_date(self, get):
        get.return_value = _Response({
            "ok": True, "actual_date": "2026-11-05", "date_mismatch": False,
            "data": {"foreign": 12, "investment_trust": 3, "dealer": 2, "total": 17},
        })
        result = twse._proxy_institutional("20261105")
        self.assertEqual(result["date"], "20261105")
        self.assertEqual(result["foreign"], 12)

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_rwd_rejects_mismatched_date(self, fetch, _proxy):
        fetch.return_value = _Response({
            "stat": "OK", "date": "2026/11/04",
            "data": [["外資及陸資", "", "", "100,000,000"]],
        })
        self.assertEqual(twse.get_institutional("20261105"), {})

    @patch("src.sources.twse._proxy_institutional", return_value=None)
    @patch("src.sources.twse._fetch")
    def test_rwd_accepts_matching_date(self, fetch, _proxy):
        fetch.return_value = _Response({
            "stat": "OK", "date": "2026/11/05",
            "data": [["外資及陸資", "", "", "100,000,000"]],
        })
        result = twse.get_institutional("20261105")
        self.assertEqual(result["date"], "20261105")
        self.assertEqual(result["foreign"], 1.0)

    def test_spot_contract_rejects_missing_or_wrong_date(self):
        self.assertFalse(spot._institutional_matches_t0({"date": "", "foreign": 1}, "20261105"))
        self.assertFalse(spot._institutional_matches_t0({"date": "20261104", "foreign": 1}, "20261105"))
        self.assertTrue(spot._institutional_matches_t0({"date": "2026/11/05", "foreign": 1}, "20261105"))


class TaiexUpstreamDateValidationTests(unittest.TestCase):
    @patch("src.sources.twse_proxy.requests.get")
    def test_proxy_accepts_matching_ind_and_ms_dates(self, get):
        response = _Response({
            "ok": True,
            "date": "2026-11-05",
            "endpoints": {
                "IND": {"date_valid": True, "actual_date": "2026/11/05"},
                "MS": {"date_valid": True, "actual_date": "2026/11/05"},
            },
            "data": {"taiex": {"close": "27000"}, "market_statistics": {"data": []},
                     "advance_decline": {"data": []}},
        })
        response.raise_for_status = lambda: None
        get.return_value = response
        result = twse_proxy.fetch("20261105")
        self.assertIsNotNone(result)
        self.assertEqual(result["data"]["taiex"]["close"], "27000")

    @patch("src.sources.twse_proxy.requests.get")
    def test_proxy_rejects_missing_or_mismatched_ind_date(self, get):
        for metadata in (
            {"date_valid": True, "actual_date": None},
            {"date_valid": False, "actual_date": "2026/11/04"},
        ):
            response = _Response({
                "ok": True, "endpoints": {"IND": metadata},
                "data": {"taiex": {"close": "27000"}},
            })
            response.raise_for_status = lambda: None
            get.return_value = response
            self.assertIsNone(twse_proxy.fetch("20261105"))

    @patch("src.sources.twse_proxy.requests.get")
    def test_proxy_keeps_ind_but_nulls_ms_when_ms_date_is_invalid(self, get):
        response = _Response({
            "ok": True,
            "endpoints": {
                "IND": {"date_valid": True, "actual_date": "2026/11/05"},
                "MS": {"date_valid": False, "actual_date": "2026/11/04"},
            },
            "data": {"taiex": {"close": "27000"}, "market_statistics": {"data": [1]},
                     "advance_decline": {"data": [1]}},
        })
        response.raise_for_status = lambda: None
        get.return_value = response
        result = twse_proxy.fetch("20261105")
        self.assertIsNotNone(result)
        self.assertIsNone(result["data"]["market_statistics"])
        self.assertIsNone(result["data"]["advance_decline"])

    @patch("src.sources.twse_proxy.requests.get")
    def test_official_fallback_rejects_wrong_actual_date(self, get):
        response = _Response({"date": "2026/11/04", "tables": []})
        response.raise_for_status = lambda: None
        get.return_value = response
        result = twse_proxy.official_ind_taiex("20261105")
        self.assertEqual(result, {"close": None, "change": None, "pct": None})

    @patch("src.sources.twse_proxy.requests.get")
    def test_official_fallback_accepts_matching_actual_date(self, get):
        response = _Response({
            "date": "2026/11/05",
            "tables": [{"data": [["發行量加權股價指數", "27000", "<p>+</p>", "100", "0.37%"]]}],
        })
        response.raise_for_status = lambda: None
        get.return_value = response
        result = twse_proxy.official_ind_taiex("20261105")
        self.assertEqual(result["close"], 27000.0)
        self.assertEqual(result["change"], 100.0)



class BorrowedSecuritiesMarketAggregationTests(unittest.TestCase):
    def test_both_markets_present_returns_complete_sum(self):
        self.assertEqual(spot._complete_market_sum(100.0, 25.0), (125.0, "complete"))

    def test_listed_only_is_partial_and_has_no_combined_value(self):
        self.assertEqual(spot._complete_market_sum(100.0, None), (None, "partial"))

    def test_otc_only_is_partial_and_has_no_combined_value(self):
        self.assertEqual(spot._complete_market_sum(None, 25.0), (None, "partial"))

    def test_both_markets_missing_is_unavailable(self):
        self.assertEqual(spot._complete_market_sum(None, None), (None, "unavailable"))


    def test_partial_coverage_note_has_explicit_status_marker(self):
        self.assertEqual(
            spot._partial_coverage_note("借券賣出餘額"),
            "[partial] 借券賣出餘額僅取得單一市場；不提供不完整的合計數值",
        )

class TpexSblCompletenessTests(unittest.TestCase):
    FIELDS = ["股票代號", "前日餘額", "當日賣出", "當日還券", "當日調整數額", "當日餘額"]

    def _run(self, rows):
        payload = {"tables": [{"date": "115/11/05", "fields": self.FIELDS, "data": rows}]}
        with patch("src.sources.spot_raw._get_json", return_value=payload):
            return spot_raw.tpex_sbl("1151105")

    def test_all_stock_rows_valid_returns_complete_total(self):
        result = self._run([["2330", "100", "20", "5", "0", "115"], ["2317", "50", "10", "2", "0", "58"]])
        self.assertTrue(result["date_ok"])
        self.assertEqual(result["sale_bal"], 173.0)
        self.assertEqual(result["sale_chg"], 23.0)

    def test_one_stock_missing_required_value_rejects_whole_total(self):
        result = self._run([["2330", "100", "20", "5", "0", "115"], ["2317", "50", "", "2", "0", "48"]])
        self.assertFalse(result["date_ok"])
        self.assertIsNone(result["sale_bal"])

    def test_one_stock_roll_forward_mismatch_rejects_whole_total(self):
        result = self._run([["2330", "100", "20", "5", "0", "999"]])
        self.assertFalse(result["date_ok"])
        self.assertIsNone(result["sale_bal"])

    def test_all_stock_rows_invalid_returns_unavailable(self):
        result = self._run([["2330", "100", "20", "5", "0", "999"], ["2317", "50", "", "2", "0", "48"]])
        self.assertFalse(result["date_ok"])
        self.assertIsNone(result["sale_bal"])

    def test_non_stock_summary_row_is_excluded(self):
        result = self._run([["2330", "100", "20", "5", "0", "115"], ["合計", "100", "20", "5", "0", "115"]])
        self.assertTrue(result["date_ok"])
        self.assertEqual(result["sale_bal"], 115.0)


if __name__ == "__main__":
    unittest.main()
