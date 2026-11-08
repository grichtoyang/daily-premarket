import unittest

from src.sources.taifex import _gamma_proxy_fallback, _gamma_status


class GammaProxyFallbackTests(unittest.TestCase):
    def test_t1_wall_does_not_block_t2_flip_fallback(self):
        payloads = {
            "2026-11-05": {
                "ok": True,
                "data": {
                    "gamma": {
                        "gamma_wall_proxy": 38900,
                        "gamma_flip_proxy": None,
                    },
                    "call_wall": {"strike": 39000},
                },
            },
            "2026-11-04": {
                "ok": True,
                "data": {
                    "gamma": {
                        "gamma_wall_proxy": 38800,
                        "gamma_flip_proxy": 39750.5,
                    },
                },
            },
        }

        result = _gamma_proxy_fallback(
            lambda day: payloads[day],
            ["2026-11-05", "2026-11-04"],
        )

        self.assertEqual(result["wall"], 38900)
        self.assertEqual(result["wall_date"], "2026-11-05")
        self.assertEqual(result["flip"], 39750.5)
        self.assertEqual(result["flip_date"], "2026-11-04")
        self.assertEqual(
            result["payload"]["data"]["gamma"]["gamma_flip_proxy"],
            39750.5,
        )
        self.assertEqual(
            result["payload"]["data"]["call_wall"]["strike"],
            39000,
        )

    def test_no_proxy_values_returns_empty_payload(self):
        result = _gamma_proxy_fallback(
            lambda day: {"ok": True, "data": {"gamma": {}}},
            ["2026-11-05", "2026-11-04"],
        )
        self.assertIsNone(result["payload"])
        self.assertIsNone(result["wall"])
        self.assertIsNone(result["flip"])

    def test_missing_flip_is_not_misreported_as_missing_gex_model(self):
        unavailable, notes = _gamma_status(
            ["gamma_flip"], False, 38900, None,
            "options-gamma-levels", gex_model_available=True,
        )
        self.assertIn("gamma_flip", unavailable)
        self.assertTrue(any("逐履約價 GEX 模型仍可用" in note for note in notes))
        self.assertFalse(any("原始端點與 Proxy 備援皆未取得" in note for note in notes))


if __name__ == "__main__":
    unittest.main()
