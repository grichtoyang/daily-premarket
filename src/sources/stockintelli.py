"""股市智投 StockIntelli 資料來源。

主力來源：https://www.stockintelli.com
- 產業資金流向 API (公開，免登入)
- 融資融券歷史 (SSR，已整合至 maint_ratio.py)

注意：本平台資料僅供參考，不構成交易建議。
其餘排行頁面 (法人/資金動能/注意股/處置股) 為 client-side 渲染，
需 headless browser 或 API 認證，暫不纳入。
"""
from __future__ import annotations
import requests


UA = {"User-Agent": "Mozilla/5.0"}
BASE = "https://www.stockintelli.com"
_session: requests.Session | None = None
_warmup_done = False


def _get_session() -> requests.Session:
    global _session, _warmup_done
    if _session is None:
        _session = requests.Session()
        _session.headers.update(UA)
    if not _warmup_done:
        import time
        try:
            _session.get(BASE + "/market/industry-flow", timeout=15)
            time.sleep(2)  # stockintelli API 有速率限制
            _warmup_done = True
        except Exception:  # noqa: BLE001
            pass
    return _session


def _get(path: str, timeout: int = 20, retries: int = 2) -> requests.Response | None:
    import time
    for attempt in range(retries + 1):
        try:
            s = _get_session()
            r = s.get(BASE + path, timeout=timeout)
            if r.status_code == 403 and attempt < retries:
                time.sleep(3)
                continue
            r.raise_for_status()
            return r
        except Exception as e:  # noqa: BLE001
            if attempt < retries:
                time.sleep(2)
                continue
            print(f"[WARN] stockintelli {path} failed: {e}")
            return None
    return None


# ============================================================
# 產業資金流向 (公開 API)
# ============================================================

def industry_flow(limit: int = 10, timeout: int = 15) -> dict:
    """產業資金流向排行。回傳 {inflow: [...], outflow: [...], summary: {...}, ok}。

    每筆 item 包含:
      rank, stock_code, security_name, industry,
      trade_value, net_flow_value, inflow_value, outflow_value,
      closing_price, price_change, price_change_percent
    """
    out = {"inflow": [], "outflow": [], "summary": {}, "ok": False}
    for direction in ("inflow", "outflow"):
        r = _get(f"/api/market/industry-flow/ranking?direction={direction}&limit={limit}",
                 timeout=timeout)
        if r is None:
            continue
        try:
            data = r.json()
            inner = data.get("data", data) if isinstance(data, dict) else data
            if isinstance(inner, dict):
                stocks = inner.get("stocks", [])
                summary = inner.get("summary", {})
                if stocks:
                    out[direction] = stocks[:limit]
                    out["ok"] = True
                if summary:
                    out["summary"] = summary
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] stockintelli industry_flow parse failed: {e}")
    return out


def format_industry_flow(data: dict) -> str:
    """格式化產業資金流向為可讀文字。"""
    lines = []
    for direction, label in [("inflow", "流入"), ("outflow", "流出")]:
        items = data.get(direction, [])
        if items:
            lines.append(f"**{label}前 5：**")
            for s in items[:5]:
                name = s.get("security_name", "?")
                code = s.get("stock_code", "?")
                net = s.get("net_flow_value", 0)
                chg = s.get("price_change_percent", 0)
                sign = "+" if net > 0 else ""
                lines.append(f"- {code} {name}：{sign}{net/1e8:.1f}億 ({chg:+.2f}%)")
    return "\n".join(lines)
