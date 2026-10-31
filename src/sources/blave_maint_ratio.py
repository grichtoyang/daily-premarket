"""Blave listed-market maintenance ratio fallback (exact T0 only)."""
from __future__ import annotations

import requests

URL = "https://api.blave.org/studio/charts/twmarket/margin_maintenance"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://blave.org/studio/twstock/zh/market/margin",
}


def get(t0: str, timeout: int = 8) -> dict:
    try:
        response = requests.get(URL, headers=HEADERS, timeout=timeout)
        response.raise_for_status()
        payload = response.json()
        rows = payload.get("data") if isinstance(payload, dict) else None
        if not isinstance(rows, list):
            raise ValueError("Blave data array missing")
        for row in reversed(rows):
            if not isinstance(row, dict) or row.get("date") != t0:
                continue
            ratio = float(row.get("maintenance_ratio"))
            if not 50 < ratio < 500:
                raise ValueError(f"Blave ratio out of range: {ratio}")
            return {"ok": True, "date": t0, "ratio": round(ratio, 4),
                    "source": "Blave", "classification": "listed_market_estimate"}
        return {"ok": False, "date": None, "ratio": None,
                "source": "Blave", "reason": f"exact T0 {t0} not found"}
    except Exception as exc:
        return {"ok": False, "date": None, "ratio": None,
                "source": "Blave", "reason": f"{type(exc).__name__}: {exc}"}
