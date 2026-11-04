import unittest

from scripts.v9_pro_builder import (
    classify_three_market,
    classify_futures_oi,
    classify_option_sessions,
)


class ThreeMarketScenarioTests(unittest.TestCase):
    def test_all_three_markets_bullish(self):
        self.assertEqual(classify_three_market([120, 800, 35]), "三市場一致偏多")

    def test_all_three_markets_bearish(self):
        self.assertEqual(classify_three_market([-120, -800, -35]), "三市場一致偏空")

    def test_cross_market_divergence(self):
        self.assertEqual(classify_three_market([-120, 800, -35]), "三市場方向分歧")

    def test_zero_is_not_directional_consensus(self):
        self.assertEqual(classify_three_market([120, 0, 35]), "三市場方向分歧")

    def test_missing_flow_does_not_become_neutral(self):
        self.assertEqual(classify_three_market([-120, None, -35]), "三市場資料不完整，不能判定一致性")

    def test_all_zero_futures_oi_is_suspicious(self):
        status, suspicious = classify_futures_oi([0, 0, 0])
        self.assertTrue(suspicious)
        self.assertIn("可疑快照", status)

    def test_partial_missing_futures_oi_is_not_all_zero(self):
        status, suspicious = classify_futures_oi([0, None, 0])
        self.assertFalse(suspicious)
        self.assertIn("有缺值", status)

    def test_valid_futures_oi_is_stock_not_flow(self):
        status, suspicious = classify_futures_oi([-10000, 2000, -500])
        self.assertFalse(suspicious)
        self.assertIn("分開解讀", status)

    def test_option_day_night_same_direction(self):
        self.assertEqual(classify_option_sessions(-100, -50), "日夜同向")

    def test_option_day_night_divergence(self):
        self.assertEqual(classify_option_sessions(-100, 50), "日夜方向分歧")

    def test_option_one_session_zero(self):
        self.assertEqual(classify_option_sessions(0, 50), "至少一盤中性")

    def test_option_missing_session(self):
        self.assertEqual(classify_option_sessions(-100, None), "日夜資料不足")


if __name__ == "__main__":
    unittest.main()
