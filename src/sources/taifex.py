"""TAIFEX 期貨+選擇權：Cloudflare Proxy (主來源)。

https://taifex.grichtoyang.workers.dev/
端點：futures-price[-after-hours]、futures-institutional[-after-hours]、
  futures-institutional-oi[-history]、futures-options-chain、
  options-delta、options-key-levels、options-market-structure-compact、
  options-institutional[-after-hours]、options-after-hours
(gamma-levels 上游 502，Gamma Wall/Flip 標 unavailable)

金額欄位單位：千元 (→億元 /1e5)。近月 = 日盤成交量最大契約。
前十大交易人走 taifex_official (proxy 優先)。
純數據整理，不做分析判斷。
"""
from __future__ import annotations
import requests
from src.utils import HEADERS

BASE = "https://taifex.grichtoyang.workers.dev"
DATE_EPS = {"futures-institutional-oi", "futures-institutional-oi-history", "futures-options-chain",
            "options-delta", "options-key-levels", "options-market-structure-compact"}
FREE_EPS = ["futures-price", "futures-price-after-hours", "futures-institutional",
            "futures-institutional-after-hours", "options-institutional",
            "options-institutional-after-hours", "options-after-hours",
            "options-day-call-put"]
INST_ZH = {"foreign": "外資", "investment_trust": "投信", "dealer": "自營商"}

def _get(ep: str, t0: str, timeout: int = 40) -> dict | None:
    import time
    url = f"{BASE}/{ep}?date={t0}" if ep in DATE_EPS else f"{BASE}/{ep}"
    for attempt in range(2):
        try:
            r = requests.get(url, headers={**HEADERS, "accept": "application/json"}, timeout=timeout)
            if r.status_code == 200:
                j = r.json()
                if isinstance(j, dict) and j.get("ok") is True and j.get("data") is not None:
                    return j
                # 200 但上游暫時無資料 → 有限重試一次後放棄
                if attempt == 0:
                    time.sleep(4)
                    continue
                return None
            if r.status_code in (429, 502, 503):
                time.sleep(3)
                continue
            return None
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] taifex {ep} failed (try {attempt + 1}): {e}")
            time.sleep(2)
    return None

def _rows(payload: dict | None) -> list:
    d = (payload or {}).get("data")
    return d if isinstance(d, list) else []

def _by_inst(rows: list) -> dict:
    return {r.get("institution"): r for r in rows if isinstance(r, dict) and r.get("institution")}

def _get_dates(ep: str, dates: list[str], timeout: int = 40) -> tuple[dict | None, str | None]:
    """依序嘗試多個日期 (Gamma FMTQIK 落後時遞補 T-1…)。回傳 (payload, 實際日期)。"""
    for d in dates:
        p = _get(ep, d, timeout)
        if p is not None and (p.get("date") or d) == d:
            return p, d
        if p is not None:
            return p, p.get("date") or d
    return None, None

def _next_trading_day(d):
    """T0 的下一個交易日。期交所報表把「T0 15:00 → T0+1 05:00」的夜盤掛在 T0 的下一個交易日
    （不是日曆 T0+1）。2026-10-17 實證：查 2026-10-19 得 10/16 夜盤 47269/47380/46107/46140/-1144
    （漲跌基準 47,284 = 10/16 結算價）；查 2026-10-17 全空。週五 T0 若用日曆 T0+1 必抓不到。
    日曆不可用（load_closed 失敗，src.t0._LAST_CAL_ERROR 非空）→ 回 None（B3 fail-loud）：
    舊行為退週末判斷會把假日當交易日，夜盤查詢日靜默偏一節。"""
    import src.t0 as _cal
    from datetime import timedelta as _tdd

    def _load(y):
        """載入休市日曆；失敗（例外或 _LAST_CAL_ERROR 非空）→ 警告並回 None。"""
        try:
            closed = _cal.load_closed(y)
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] 交易日曆不可用（load_closed 例外：{e}），不退週末判斷（fail-loud）")
            return None
        if _cal._LAST_CAL_ERROR:
            print(f"[WARN] 交易日曆不可用（{_cal._LAST_CAL_ERROR}），不退週末判斷（fail-loud）")
            return None
        return closed

    _y = d.year
    closed = _load(_y)
    if closed is None:
        return None
    for _ in range(14):
        d = d + _tdd(days=1)
        if d.year != _y:
            _y = d.year
            closed = _load(_y)
            if closed is None:
                return None
        if _cal.is_trading_day(d, closed):
            return d
    return d

def _night_query_date(t0=None, session="全日", now=None) -> str | None:
    """夜盤查詢日（期交所語義：查日期 D → D-1 15:00~D 05:00 節，2026-10-16 官網截圖實證）。
    全日版要 T0 當晚節（15:00 T0 → 05:00 T0+1）→ 查 T0 的下一個交易日
    （報表把該節掛在下一個交易日，不是日曆 T0+1；2026-10-17 實證：查 2026-10-19
    得 10/16 夜盤，查 2026-10-17 全空；週五 T0 用日曆 T0+1 必失效）；
    日盤版要前一夜（今晨收盤節）→ 查今天（此時 T0 即今天）。
    10-12 改查今天是誤診（假日無節次的回退被當成規則錯），此次改回；
    嚴格把關（回傳日期不符視為無新節次）保留，假日照樣安全。
    交易日曆不可用時回 None（B3 fail-loud，不猜測）。"""
    from datetime import date as _date
    from datetime import datetime as _dt
    from datetime import timedelta as _td
    from zoneinfo import ZoneInfo as _ZI
    now = now or _dt.now(_ZI("Asia/Taipei"))
    if session != "日盤" and t0:
        _nxt = _next_trading_day(_date.fromisoformat(t0))
        if _nxt is None:
            return None
        return _nxt.isoformat()
    return now.date().isoformat()


def _night_ohlc(t0: str, month: str | None, session: str = "全日", now=None) -> dict | None:
    """夜盤 OHLC：proxy /futures-night-ohlc (V1.4+) 優先，官方 DailyMarketReportFut 備援。
    回傳含 via/date/qdate，或 None。
    期交所規則：查日期 D + Session=F → D-1 15:00~D 05:00（查詢日為節次收盤日）。
    全日查 T0 的下一個交易日、日盤查今天（_night_query_date）；回傳 date 必須等於查詢日，否則視為無新節次。
    節次完整性：全日節在 T0+1（日曆）05:00 收盤，此前查詢只抓得到半成品，一律不採用。
    官方備援同理，只收查詢日當天列。"""
    import os
    from datetime import datetime as _dt2
    from datetime import timedelta as _td2
    from zoneinfo import ZoneInfo as _ZI2
    now = now or _dt2.now(_ZI2("Asia/Taipei"))
    query_date = _night_query_date(t0, session, now)
    if query_date is None:
        import src.t0 as _cal
        print(f"[WARN] 夜盤 OHLC 不採用：交易日曆不可用（{_cal._LAST_CAL_ERROR or 'load_closed 失敗'}），"
              f"夜盤查詢日無法判定（T0 {t0}，session {session}），不猜測（B3 fail-loud）")
        return None
    if session != "日盤":
        _end_src = (_dt2.fromisoformat(t0) + _td2(days=1)) if t0 else _dt2.fromisoformat(query_date)
        _end = _end_src.replace(
            tzinfo=_ZI2("Asia/Taipei")).replace(hour=5, minute=0)
        if now < _end:
            print(f"[INFO] 夜盤節未收盤（T0 {t0} 節次 {_end} 才收），不採用半成品")
            return None
    base = os.getenv("TAIFEX_PROXY_BASE_URL", BASE).rstrip("/")
    if month:
        try:
            r = requests.get(f"{base}/futures-night-ohlc", params={"date": query_date, "month": month},
                             headers={**HEADERS, "accept": "application/json"}, timeout=30)
            if r.status_code == 200:
                j = r.json()
                if isinstance(j, dict) and j.get("ok") is True and isinstance(j.get("data"), dict):
                    d = j["data"]
                    if d.get("close") is not None and (j.get("date") or "") == query_date:
                        return {"open": d.get("open"), "high": d.get("high"), "low": d.get("low"),
                                "close": d.get("close"), "change": d.get("change"),
                                "pct": _pct(d.get("change_percent")),
                                "volume": d.get("volume"),
                                "via": "proxy", "date": query_date,
                                "qdate": query_date}
                    print(f"[INFO] proxy night-ohlc 回退 (查 {query_date} 得 {j.get('date')})，改官方備援")
        except Exception as e:  # noqa: BLE001
            print(f"[INFO] proxy night-ohlc 不可用，改官方備援：{e}")
    try:
        from src.sources import taifex_official as _off
        rows = [x for x in _off._get("/DailyMarketReportFut")
                if x.get("Contract") == "TX" and x.get("TradingSession") == "盤後"
                and x.get("ContractMonth(Week)") == month
                and _off._iso(x.get("Date", "")) == query_date]
        if not rows:
            return None
        rows.sort(key=lambda x: x.get("Date", ""), reverse=True)
        r0 = rows[0]
        def _n(v):
            try:
                return float(str(v).replace(",", "")) if v not in (None, "", "-", "NULL") else None
            except (ValueError, TypeError):
                return None
        chg, close = _n(r0.get("Change")), _n(r0.get("Last"))
        return {"open": _n(r0.get("Open")), "high": _n(r0.get("High")), "low": _n(r0.get("Low")),
                "close": close, "change": chg,
                "pct": (chg / (close - chg) * 100) if chg is not None and close else None,
                "via": "official", "date": _off._iso(r0.get("Date", "")),
                "qdate": query_date}
    except Exception as e:  # noqa: BLE001
        print(f"[INFO] official night-ohlc 不可用：{e}")
        return None

def snapshot_bundle(date: str, timeout: int = 40) -> dict | None:
    """讀 worker 快照 (V1.4+ /snapshots/bundle)。未部署/無資料回 None。
    日盤部位類僅當 collected_at 與標示日期同日才可信 (cron 當日收盤後收集；
    手動回填舊日期時其無日期源實為抓取當下值，不可採用)。"""
    import os, time
    base = os.getenv("TAIFEX_PROXY_BASE_URL", BASE).rstrip("/")
    for _try in range(2):
        try:
            r = requests.get(f"{base}/snapshots/bundle", params={"date": date},
                             headers={**HEADERS, "accept": "application/json"}, timeout=60)
            if r.status_code != 200:
                print(f"[WARN] snapshot http {r.status_code} (try {_try + 1})")
                time.sleep(5)
                continue
            j = r.json()
            if isinstance(j, dict) and j.get("ok") is True and isinstance(j.get("data"), dict):
                b = j["data"]
                inner = b.get("data") if isinstance(b.get("data"), dict) else b
                trust_pos = str(b.get("collected_at", ""))[:10] == j.get("date")
                return {"date": j.get("date"), "data": inner, "trust_pos": trust_pos}
            print(f"[WARN] snapshot ok!=true (try {_try + 1})")
            time.sleep(5)
        except Exception as e:  # noqa: BLE001
            print(f"[INFO] snapshot 不可用 (try {_try + 1})：{e}")
            time.sleep(5)
    return None

def _prev_dates(t0: str, n: int = 5) -> list[str]:
    from datetime import date as _d, timedelta as _td
    base = _d.fromisoformat(t0)
    return [(base - _td(days=i)).isoformat() for i in range(n + 1)]

def dateless_content_date(now=None) -> str:
    """無日期端點的內容日期判定 (日盤 08:45 開、13:45 收；僅平日)。
    08:00 正式跑時回傳 T0；盤中跑回傳今日。"""
    from datetime import datetime as _dt
    from zoneinfo import ZoneInfo as _ZI
    now = now or _dt.now(_ZI("Asia/Taipei"))
    d = now.date()
    if now.hour < 13 or (now.hour == 13 and now.minute < 45):
        from datetime import timedelta as _td
        d -= _td(days=1)
    while d.weekday() >= 5:
        from datetime import timedelta as _td
        d -= _td(days=1)
    return d.isoformat()

def build(t0: str, taiex_close=None, session: str = "全日") -> dict:
    unav: list[str] = []
    notes: list[str] = []
    _content = dateless_content_date()
    if _content != t0:
        notes.append(f"無日期端點為最新盤勢快照 (判定資料日期 {_content}，非 T0 {t0})，"
                     "適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註")
    P = {ep: _get(ep, t0) for ep in list(FREE_EPS) + sorted(DATE_EPS - {"options-gamma-levels", "options-market-structure-compact", "futures-options-chain"})}
    # 夜盤附屬端點（量/結算/法人夜交易）同口徑把關：payload 日期必須等於今天，
    # 否則視為無新節次，不採用（回退舊值曾靜默混入，2026-10-08 全日版教訓）。
    # options-after-hours 不在此列（它供日盤買賣權拆分，非純夜盤歸屬）。
    _today = _night_query_date(t0, session)
    if _today is None:
        import src.t0 as _cal0
        notes.append(f"交易日曆不可用（{_cal0._LAST_CAL_ERROR or 'load_closed 失敗'}），"
                     "夜盤查詢日無法判定，夜盤附屬端點一律不採用（B3 fail-loud）")
    for _ep in ("futures-price-after-hours", "futures-institutional-after-hours",
                "options-institutional-after-hours"):
        _p = P.get(_ep)
        _d = (_p or {}).get("date")
        if _p is None:
            continue
        if _today is None:
            P[_ep] = None
        elif _d is not None and _d != _today:
            notes.append(f"{_ep} 日期 {_d} 非今日 {_today}，視為無新節次，不採用")
            P[_ep] = None
    # Gamma 端點需 TAIEX 收盤 (FMTQIK 落後約一日)：有值才算命中，否則向 T-1…遞補並標示實際日期
    g_pay, g_date, c_pay, c_date = None, None, None, None
    for _d in _prev_dates(t0, 2):
        if g_pay is None:
            _p = _get("options-gamma-levels", _d)
            _w = (((_p or {}).get("data") or {}).get("gamma_wall") or {}).get("strike")
            if _w is not None:
                g_pay, g_date = _p, _d
        if c_pay is None:
            _p = _get("options-market-structure-compact", _d)
            _w = (((_p or {}).get("data") or {}).get("gamma") or {}).get("gamma_wall_proxy")
            if _w is not None:
                c_pay, c_date = _p, _d
        if g_pay is not None and c_pay is not None:
            break
    P["options-gamma-levels"] = g_pay
    P["options-market-structure-compact"] = c_pay
    gamma_date = g_date or c_date
    # Walls 端點 (key-levels/compact) 工人偶發 503：有 Call Wall 才算命中，否則遞補並標示日期
    kl_pay, kl_date = None, None
    cp_pay, cp_date = None, None
    for _d in _prev_dates(t0, 2):
        if kl_pay is None:
            _p = _get("options-key-levels", _d, timeout=90)
            if (((_p or {}).get("data") or {}).get("call_wall") or {}).get("strike") is not None:
                kl_pay, kl_date = _p, _d
        if cp_pay is None:
            _p = P["options-market-structure-compact"] if _d == t0 else _get("options-market-structure-compact", _d, timeout=90)
            if (((_p or {}).get("data") or {}).get("call_wall") or {}).get("strike") is not None:
                cp_pay, cp_date = _p, _d
        if kl_pay is not None and cp_pay is not None:
            break
    if kl_pay is not None:
        P["options-key-levels"] = kl_pay
    if cp_pay is not None and (P["options-market-structure-compact"] is None):
        P["options-market-structure-compact"] = cp_pay
    walls_date = kl_date or cp_date
    if walls_date and walls_date != t0:
        notes.append(f"Call/Put Wall 與 Max Pain 資料日期 {walls_date} (T0 {t0} 端點不穩，採最新可得)")
    if gamma_date and gamma_date != t0:
        notes.append(f"Gamma 資料日期 {gamma_date} (T0 {t0} 尚無，上游 FMTQIK 落後，採最新可得)")

    # ---------- 期貨 1/2：近月日夜盤 ----------
    prices = _rows(P["futures-price"])
    ahp = _rows(P["futures-price-after-hours"])
    near = max(prices, key=lambda r: (r.get("regular_volume") or 0)) if prices else {}
    ah = next((r for r in ahp if r.get("contract_month") == near.get("contract_month")), {})
    day = {"month": near.get("contract_month"), "open": near.get("open"), "high": near.get("high"),
           "low": near.get("low"), "close": near.get("close"), "change": near.get("change"),
           "pct": _pct(near.get("change_percent")), "vol": near.get("total_volume"),
           "vol_day": near.get("regular_volume"), "oi": near.get("open_interest")}
    night = {"month": ah.get("contract_month"), "vol": ah.get("after_hours_volume"),
             "oi": ah.get("open_interest"), "settle": ah.get("settlement_price"),
             "open": None, "high": None, "low": None, "close": None, "change": None, "pct": None,
             "via": "proxy"}
    # 夜盤 OHLC：proxy V1.4+ /futures-night-ohlc 優先，官方 DailyMarketReportFut 備援
    # 全日查 T0+1、日盤查今天（今晨收盤節）；回傳非查詢日一律視為無新節次（_night_ohlc 內部把關＋完整性檢查）
    _nh = _night_ohlc(t0, day["month"], session=session)
    if _nh is not None:
        night.update({k: _nh.get(k) for k in ("open", "high", "low", "close", "change", "pct")})
        # 量取 OHLC 端點（同節次聚合；after-hours 端點量口徑常不一致，2026-10-12 教訓）
        if _nh.get("volume") is not None:
            night["vol"] = _nh.get("volume")
        night["via"] = _nh.get("via", "proxy")
        _q = _nh.get("qdate") or t0
        if _nh.get("date") and _nh["date"] != _q:
            notes.append(f"夜盤 OHLC 回退：查 {_q} 得 {_nh['date']} (T0 {t0})，來源 {_nh.get('via')}，無新節次")
    else:
        import src.t0 as _cal1
        # 全日節 _night_ohlc 內必經 load_closed：_LAST_CAL_ERROR 非空 ⟺ 本次曆失敗，歸因準確
        if session != "日盤" and _cal1._LAST_CAL_ERROR:
            notes.append(f"夜盤開高低收未取得（交易日曆不可用：{_cal1._LAST_CAL_ERROR}），僅成交量/OI/結算價")
        else:
            notes.append("夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價")

    # ---------- 期貨 3：法人 OI + 變化 ----------
    oi = _by_inst(_rows(P["futures-institutional-oi"]))
    hist = (_get("futures-institutional-oi-history", t0) or {}).get("data") or []
    prev = {}
    if len(hist) >= 2:
        for r in hist[1].get("data") or []:
            prev[r.get("institution")] = r
    fut_oi = {}
    for k in ("foreign", "investment_trust", "dealer"):
        cur = oi.get(k, {})
        pr = prev.get(k, {})
        net = cur.get("net_oi")
        fut_oi[k] = {"long": cur.get("long_oi"), "short": cur.get("short_oi"), "net": net,
                     "d_long": _diff(cur.get("long_oi"), pr.get("long_oi")),
                     "d_short": _diff(cur.get("short_oi"), pr.get("short_oi")),
                     "d_net": _diff(net, pr.get("net_oi"))}
    tot = lambda f: sum(v[f] for v in fut_oi.values() if v[f] is not None)
    fut_oi["total"] = {"long": tot("long"), "short": tot("short"), "net": tot("net"),
                       "d_long": tot("d_long"), "d_short": tot("d_short"), "d_net": tot("d_net")}
    if fut_oi["foreign"]["long"] is None:
        notes.append("法人 OI 未取得")

    # ---------- 期貨 5：日夜盤法人交易 ----------
    day_t = _by_inst(_rows(P["futures-institutional"]))
    night_t = _by_inst(_rows(P["futures-institutional-after-hours"]))
    fut_trade = {}
    for sess, src in (("day", day_t), ("night", night_t)):
        for k in ("foreign", "investment_trust", "dealer"):
            r = src.get(k, {})
            fut_trade[(sess, k)] = {"long": r.get("long_volume"), "short": r.get("short_volume"),
                                    "net": r.get("net_volume"),
                                    "long_amt_yi": _yi(r.get("long_amount")), "short_amt_yi": _yi(r.get("short_amount")),
                                    "net_amt_yi": _yi(r.get("net_amount"))}
    notes.append("法人交易量變化無昨日交易端點，標 unavailable")

    # ---------- 期貨 6：期現關係 ----------
    basis = None
    basis_pct = None
    if day["close"] is not None and taiex_close is not None:
        basis = day["close"] - taiex_close
        basis_pct = basis / taiex_close * 100 if taiex_close else None

    # ---------- 期貨 7：對照 (量/OI/籌碼變化；價格變化無昨日價格端點) ----------
    oi_chg = fut_oi["total"]["d_net"]

    # ---------- 選擇權 chain (失敗向 T-1…遞補並標示日期) ----------
    chain, chain_date = [], None
    for _d in _prev_dates(t0, 2):
        _p = _get("futures-options-chain", _d, timeout=90)
        if _p is not None:
            chain, chain_date = _rows(_p), _d
            break
    if chain_date and chain_date != t0:
        notes.append(f"選擇權 chain 資料日期 {chain_date} (T0 {t0} 端點不穩，採最新可得)")
    kl = (P["options-key-levels"] or {}).get("data") or {}
    prim = (kl.get("primary_expiry") or {}) if isinstance(kl, dict) else {}
    prim_month = prim.get("contract_month")
    pc = [r for r in chain if r.get("contract_month") == prim_month] if prim_month else chain
    calls = [r for r in pc if r.get("type") == "call"]
    puts = [r for r in pc if r.get("type") == "put"]
    c_vol = sum(r.get("total_volume") or 0 for r in calls)
    p_vol = sum(r.get("total_volume") or 0 for r in puts)
    c_oi = sum(r.get("open_interest") or 0 for r in calls)
    p_oi = sum(r.get("open_interest") or 0 for r in puts)
    opt_tot = {"expiry": prim_month, "c_vol": c_vol, "p_vol": p_vol, "c_oi": c_oi, "p_oi": p_oi,
               "vol_ratio": c_vol / p_vol if p_vol else None,
               "oi_ratio": c_oi / p_oi if p_oi else None,
               "pc_ratio": p_oi / c_oi if c_oi else None}
    def top_oi(rows, n=3):
        return sorted(rows, key=lambda r: r.get("open_interest") or 0, reverse=True)[:n]
    tc, tp = top_oi(calls), top_oi(puts)
    opt_conc = {"c_top": [(r.get("strike"), r.get("open_interest")) for r in tc],
                "p_top": [(r.get("strike"), r.get("open_interest")) for r in tp],
                "c_max": (tc[0].get("strike"), tc[0].get("open_interest")) if tc else (None, None),
                "p_max": (tp[0].get("strike"), tp[0].get("open_interest")) if tp else (None, None)}
    # OI 分布明細 Top10 (機器可讀，Dashboard 繪圖用)
    def _dist(rows):
        tot = sum(r.get("open_interest") or 0 for r in rows)
        top = sorted(rows, key=lambda r: r.get("open_interest") or 0, reverse=True)[:10]
        return [{"strike": r.get("strike"), "oi": r.get("open_interest"),
                 "pct": round((r.get("open_interest") or 0) / tot * 100, 2) if tot else None}
                for r in top]
    opt_dist = {"expiry": prim_month, "call": _dist(calls), "put": _dist(puts)}
    if not chain:
        notes.append("選擇權 chain 未取得，總量/OI/集中區 unavailable")

    # ---------- 選擇權法人 ----------
    oi_inst = _by_inst(_rows(P["options-institutional"]))
    ah_inst = (P["options-after-hours"] or {}).get("data") or {}
    ah_c = _by_inst(ah_inst.get("call") or [])
    ah_p = _by_inst(ah_inst.get("put") or [])
    opt_pos = {}
    for k in ("foreign", "dealer"):
        r = oi_inst.get(k, {})
        opt_pos[k] = {"long": r.get("long_volume"), "short": r.get("short_volume"), "net": r.get("net_volume"),
                      "ah_c_net": (ah_c.get(k) or {}).get("net_volume"),
                      "ah_p_net": (ah_p.get(k) or {}).get("net_volume")}
    if opt_pos["foreign"]["long"] is None:
        notes.append("選擇權法人部位未取得")

    # ---------- 選擇權買賣權拆分 (日盤新端點＋夜盤；口數金額供完整版/力道表) ----------
    _dcp = (P.get("options-day-call-put") or {}).get("data") or {}
    _dcp_c = _by_inst(_dcp.get("call") or [])
    _dcp_p = _by_inst(_dcp.get("put") or [])
    _ncp = (P.get("options-after-hours") or {}).get("data") or {}
    _ncp_c = _by_inst(_ncp.get("call") or [])
    _ncp_p = _by_inst(_ncp.get("put") or [])
    opt_split = {}
    for sess, src in (("day", {"call": _dcp_c, "put": _dcp_p}),
                      ("night", {"call": _ncp_c, "put": _ncp_p})):
        for k in ("foreign", "investment_trust", "dealer"):
            c = (src["call"].get(k) or {})
            p = (src["put"].get(k) or {})
            opt_split[(sess, k)] = {
                "c_long": c.get("long_volume"), "c_short": c.get("short_volume"),
                "c_net": c.get("net_volume"),
                "c_lamt": c.get("long_amount"), "c_samt": c.get("short_amount"),
                "p_long": p.get("long_volume"), "p_short": p.get("short_volume"),
                "p_net": p.get("net_volume"),
                "p_lamt": p.get("long_amount"), "p_samt": p.get("short_amount")}
    if opt_split[("day", "foreign")]["c_net"] is None:
        unav.append("opt_split")
        notes.append("選擇權日盤買賣權拆分未取得")

    # ---------- 選擇權法人日夜盤交易 (同 期貨 5；夜盤為晨收已結算節) ----------
    opt_night_t = _by_inst(_rows(P["options-institutional-after-hours"]))
    opt_trade = {}
    for sess, src in (("day", oi_inst), ("night", opt_night_t)):
        for k in ("foreign", "investment_trust", "dealer"):
            r = src.get(k, {})
            opt_trade[(sess, k)] = {"long": r.get("long_volume"), "short": r.get("short_volume"),
                                    "net": r.get("net_volume")}
    if opt_trade[("day", "foreign")]["long"] is None:
        unav.append("opt_trade")
        notes.append("選擇權法人日夜盤交易未取得")

    # ---------- Walls ----------
    def _wall(v):
        return v if isinstance(v, dict) else {}
    walls = {"call": _wall(kl.get("call_wall")), "put": _wall(kl.get("put_wall")),
             "maxpain": _wall(kl.get("max_pain")), "expiry": prim_month}
    # ---------- Gamma (T0 缺時已遞補，g_date 為實際日期) ----------
    gdata = (P["options-gamma-levels"] or {}).get("data") or {}
    cdata = (P["options-market-structure-compact"] or {}).get("data") or {}
    cgamma = cdata.get("gamma") or {}
    wall = (gdata.get("gamma_wall") or {}).get("strike")
    flip = (gdata.get("gamma_flip") or {}).get("estimated_underlying")
    gsrc = "options-gamma-levels"
    if wall is None and cgamma.get("gamma_wall_proxy") is not None:
        wall, flip = cgamma.get("gamma_wall_proxy"), cgamma.get("gamma_flip_proxy")
        gsrc = "options-market-structure-compact (proxy)"
    gamma = {"wall": wall, "flip": flip,
             "model": gdata.get("model"), "quality": gdata.get("model_quality"),
             "underlying": gdata.get("underlying_price"), "date": gamma_date, "src": gsrc}
    if gamma["wall"] is None:
        unav += ["gamma_wall", "gamma_flip"]
        notes.append("Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable")
    elif gamma_date and gamma_date != t0:
        notes.append(f"Gamma Wall/Flip 資料日期 {gamma_date} (來源 {gsrc})")

    # ---------- 快照差值 (V1.4+；無快照則維持 unavailable) ----------
    from datetime import date as _dd, timedelta as _td
    _t1 = (_dd.fromisoformat(t0) - _td(days=1)).isoformat()
    _sb = snapshot_bundle(_t1)
    _sdate = (_sb or {}).get("date")
    _sd = (_sb or {}).get("data") or {}
    snapchg = {"date": _sdate}
    # C2 跨到期換月檢查：快照主力到期 vs 當前主力到期不同 → 日對日差值無意義
    # （實證：10-14 快照主力 202610W2，當前 202610F3；舊寫法會拿 F3 今值減 W2 舊值）。
    # 注意：不能只比到期集合是否相交（兩邊常同時含新舊合約），必須比主力。
    _roll, _roll_old = _chain_rollover(
        _sd.get("chain", []),
        ((_sd.get("walls") or {}).get("primary_expiry") or {}).get("contract_month"),
        prim_month)
    if _sdate and _roll:
        snapchg["chain"] = None
        snapchg["walls"] = None
        notes.append(f"跨到期換月（舊{_roll_old}→新{prim_month}），日對日 OI/Walls 變化不適用")
    if _sdate:
        # chain：總量增減 + 增減集中 (primary 到期月，按 month|expiry|strike|type 對齊)
        _pmap = {(x.get("contract_month"), x.get("contract_expiry_date"), x.get("strike"), x.get("type")): x
                 for x in _sd.get("chain", []) if isinstance(x, dict)}
        if not _roll and _pmap and prim_month:
            _moves = []
            for r in [x for x in chain if x.get("contract_month") == prim_month]:
                p = _pmap.get((r.get("contract_month"), r.get("contract_expiry_date"),
                               r.get("strike"), r.get("type")), {})
                _moves.append({"strike": r.get("strike"), "type": r.get("type"),
                               "d_oi": (r.get("open_interest") or 0) - (p.get("open_interest") or 0)})
            _cm = sorted([m for m in _moves if m["type"] == "call"], key=lambda x: x["d_oi"], reverse=True)
            _pm = sorted([m for m in _moves if m["type"] == "put"], key=lambda x: x["d_oi"], reverse=True)
            snapchg["chain"] = {
                "c_chg": sum(m["d_oi"] for m in _cm), "p_chg": sum(m["d_oi"] for m in _pm),
                "c_up": _cm[0] if _cm and _cm[0]["d_oi"] > 0 else None,
                "c_dn": _cm[-1] if _cm and _cm[-1]["d_oi"] < 0 else None,
                "p_up": _pm[0] if _pm and _pm[0]["d_oi"] > 0 else None,
                "p_dn": _pm[-1] if _pm and _pm[-1]["d_oi"] < 0 else None}
        # 部位：日盤淨差值 (僅快照當日收集才可信)
        _sfd = {x.get("institution"): x for x in _sd.get("fut_trade_day", [])} \
            if (_sb or {}).get("trust_pos") else {}
        _sod = {x.get("institution"): x for x in _sd.get("opt_pos_day", [])} \
            if (_sb or {}).get("trust_pos") else {}
        _pos = {}
        for _k in ("foreign", "dealer"):
            _cf = (fut_trade.get(("day", _k)) or {}).get("net")
            _sf = (_sfd.get(_k) or {}).get("net_volume")
            _co = (opt_pos.get(_k) or {}).get("net")
            _so = (_sod.get(_k) or {}).get("net_volume")
            _pos[_k] = {"fut_chg": _diff(_cf, _sf), "opt_chg": _diff(_co, _so)}
        snapchg["pos"] = _pos
        # walls
        if not _roll:
            _sw = _sd.get("walls") or {}
            snapchg["walls"] = {
                "call": _diff((walls["call"] or {}).get("strike"), (_sw.get("call_wall") or {}).get("strike")),
                "put": _diff((walls["put"] or {}).get("strike"), (_sw.get("put_wall") or {}).get("strike")),
                "maxpain": _diff((walls["maxpain"] or {}).get("strike"), (_sw.get("max_pain") or {}).get("strike"))}

    return {"day": day, "night": night, "fut_oi": fut_oi, "fut_trade": fut_trade,
            "basis": basis, "basis_pct": basis_pct, "oi_chg": oi_chg,
            "opt_tot": opt_tot, "opt_conc": opt_conc, "opt_dist": opt_dist, "opt_pos": opt_pos,
            "opt_trade": opt_trade, "opt_split": opt_split, "walls": walls,
            "gamma": gamma, "trade_date": t0, "opt_expiry": prim_month, "snapchg": snapchg,
            "unavailable": unav, "notes": notes}


def _chain_rollover(snap_rows, snap_walls_primary, cur_primary):
    """快照主力到期 vs 當前主力到期是否換月。純函式，可單測。
    old 取快照 walls 主力，無則取快照 chain Call OI 最大月份；任一未知 → (False, old)。
    回傳 (is_rollover, old_primary)。"""
    old = snap_walls_primary
    if not old and snap_rows:
        _m = {}
        for x in snap_rows:
            if isinstance(x, dict) and x.get("type") == "call":
                try:
                    _m[str(x.get("contract_month"))] = _m.get(
                        str(x.get("contract_month")), 0) + int(x.get("open_interest") or 0)
                except (ValueError, TypeError):
                    pass
        old = max(_m, key=_m.get) if _m else None
    if not old or not cur_primary or old == cur_primary:
        return False, old
    return True, old


def _iso8(v: str | None) -> str | None:
    """yyyymmdd / yyyy-mm-dd → yyyy-mm-dd；無法解析回 None。"""
    s = str(v or "").strip().replace("-", "")
    if len(s) == 8 and s.isdigit():
        return f"{s[:4]}-{s[4:6]}-{s[6:8]}"
    s2 = str(v or "").strip()
    if len(s2) == 10 and s2[4] == "-" and s2[7] == "-":
        return s2
    return None


def snap_top10_change(month: str, t0: str, cur_net, cur_date: str | None = None,
                      dataset: str = "top10fut", callput: str | None = None) -> dict | None:
    """前十大淨變化 (快照 T-1)。dataset: top10fut (期貨) / top10opt (選擇權，需 callput)。
    上游 OpenAPI 落後約一日，快照內容日期常比快照鍵日期早 (含週末)，
    故不硬比快照日期，改按契約月份對齊、取該月最新內容日期。
    回傳 {chg, prev_date, cur_date, snap_date} 或 None。"""
    from datetime import date as _dd, timedelta as _td
    _t1 = (_dd.fromisoformat(t0) - _td(days=1)).isoformat()
    _sb = snapshot_bundle(_t1)
    if not _sb:
        return None
    rows = [r for r in (_sb["data"].get(dataset) or []) if isinstance(r, dict)]
    if callput:
        rows = [r for r in rows if str(r.get("CallPut", "")) == str(callput)]
    if month:
        _mrows = [r for r in rows if str(r.get("SettlementMonth", "")) == str(month)]
        if _mrows:
            rows = _mrows
    if not rows or cur_net is None:
        return None
    rows.sort(key=lambda r: str(r.get("Date", "")))
    r0 = rows[-1]
    prev_date = _iso8(r0.get("Date"))
    if prev_date is None:
        return None
    try:
        prev = float(r0.get("Top10Buy", 0)) - float(r0.get("Top10Sell", 0))
    except (ValueError, TypeError):
        return None
    return {"chg": cur_net - prev, "prev_date": prev_date,
            "cur_date": _iso8(cur_date) or t0, "snap_date": _sb["date"]}

def _pct(v):
    try:
        return float(v) if v is not None else None
    except (ValueError, TypeError):
        return None

def _diff(a, b):
    return a - b if a is not None and b is not None else None

def _yi(v):
    """千元 → 億元。"""
    try:
        return float(v) / 1e5 if v is not None else None
    except (ValueError, TypeError):
        return None
