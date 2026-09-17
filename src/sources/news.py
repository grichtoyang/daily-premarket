"""重大經濟數據/央行事件/市場新聞 (台股優先，其次國際)。

台股：tw.stock.yahoo.com/news 列表 (標題+連結) + 內文 datePublished/og:description。
國際：Fed 公告 RSS (央行事件) + CNBC 要聞 RSS + MarketWatch 要聞 RSS (備援)。
investing hk 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查 → Phase 2。
"""
from __future__ import annotations
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin
from zoneinfo import ZoneInfo
import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
YAHOO_LIST = "https://tw.stock.yahoo.com/news"
INVEST_FEEDS = {"Federal Reserve": "https://www.federalreserve.gov/feeds/press_all.xml",
                "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
                "MarketWatch": "https://feeds.marketwatch.com/marketwatch/topstories/"}
TAIPEI = ZoneInfo("Asia/Taipei")

def _clean(s: str) -> str:
    return re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", s, flags=re.S)
KEYWORDS_MACRO = ("央行", "利率", "升息", "降息", "通膨", "CPI", "PCE", "就業", "非農", "失業率",
                  "GDP", "關稅", "制裁", "地緣", "聯準會", "Fed", "鮑爾", "FOMC", "衰退", "景氣",
                  "美債", "殖利率", "降準", "MLF", "PMI", "匯率干預",
                  "central bank", "rate hike", "rate cut", "inflation", "payrolls", "unemployment",
                  "tariff", "sanction", "powell", "recession", "treasury", "yield", "fomc")
KEYWORDS_MARKET = ("半導體", "晶片", "美股", "港股", "匯市", "油價", "金價",
                   "比特幣", "債市", "期貨", "現貨金",
                   "stocks", "dollar", "oil", "gold", "bitcoin", "chips", "semiconductor",
                   "tsmc", "taiwan", "wall street", "nasdaq", "s&p")
EXCLUDE_URL = ("insider-trading-news",)

def _parse_time(s: str):
    s = re.sub(r"\s+(GMT|UTC)$", " +0000", s.strip())
    m = re.match(r"(\w{3}) (\d{1,2}), (\d{4}) (\d{2}):(\d{2})", s)
    if m:
        try:
            mon = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                   "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}[m.group(1)]
            return datetime(int(m.group(3)), mon, int(m.group(2)),
                            int(m.group(4)), int(m.group(5)), tzinfo=timezone.utc)
        except (ValueError, KeyError):
            pass
    for fmt in ("%Y-%m-%d %H:%M:%S", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%SZ"):
        try:
            v = s[:-1] + "+0000" if fmt.endswith("SZ") and s.endswith("Z") else s
            dt = datetime.strptime(v, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None

def _tw_news(max_items: int = 6, days: int = 7) -> list[dict]:
    """Yahoo 台股新聞列表 + 內文時間/摘要。"""
    out: list[dict] = []
    try:
        r = requests.get(YAHOO_LIST, headers=UA, timeout=25)
        r.raise_for_status()
        links = re.findall(r'href="((?:https://tw\.stock\.yahoo\.com)?/news/[^"]+\.html)"[^>]*>([^<]{8,80})<', r.text)
        seen = set()
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        for href, title in links:
            url = urljoin("https://tw.stock.yahoo.com", href)
            if url in seen or len(out) >= max_items:
                break
            seen.add(url)
            try:
                a = requests.get(url, headers=UA, timeout=20)
                if a.status_code != 200:
                    continue
                dp = re.search(r'"datePublished"\s*:\s*"([^"]+)"', a.text)
                og = re.search(r'<meta[^>]+property="og:description"[^>]+content="([^"]+)"', a.text)
                dt = _parse_time(dp.group(1)) if dp else None
                if dt is not None and dt < cutoff:
                    continue
                out.append({"title": title.strip(), "source": "Yahoo 台股",
                            "pub": dp.group(1) if dp else "unavailable",
                            "taipei": dt.astimezone(TAIPEI).strftime("%Y-%m-%d %H:%M") if dt else "unavailable",
                            "summary": (og.group(1)[:120] if og else "unavailable"),
                            "link": url})
            except Exception:  # noqa: BLE001
                continue
    except Exception as e:  # noqa: BLE001
        print(f"[WARN] yahoo tw news failed: {e}")
    return out

def _intl_news(max_items: int = 6, days: int = 7) -> list[dict]:
    out: list[dict] = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    for src, url in INVEST_FEEDS.items():
        r = None
        import time
        for _try in range(2):
            try:
                r = requests.get(url, headers=UA, timeout=25)
                r.raise_for_status()
                break
            except Exception as e:  # noqa: BLE001
                print(f"[WARN] news feed failed {url} (try {_try + 1}): {e}")
                time.sleep(3)
        if r is None:
            continue
        try:
            for m in re.finditer(r"<item>(.*?)</item>", r.text, re.S):
                b = m.group(1)
                title = re.search(r"<title>(.*?)</title>", b, re.S)
                link = re.search(r"<link>(.*?)</link>", b)
                pub = re.search(r"<pubDate>(.*?)</pubDate>", b)
                desc = re.search(r"<description>(.*?)</description>", b, re.S)
                if not (title and link):
                    continue
                t = _clean(title.group(1)).strip()
                t = t.replace("&apos;", "'").replace("&#x2019;", "'").replace("&quot;", '"').replace("&amp;", "&")
                lk = _clean(link.group(1)).strip()
                if any(x in lk for x in EXCLUDE_URL):
                    continue
                pub_s = _clean(pub.group(1)) if pub else ""
                dt = _parse_time(pub_s) if pub else None
                if dt is not None and dt < cutoff:
                    continue
                tl = t.lower()
                tier = 2 if any(k.lower() in tl for k in KEYWORDS_MACRO) else (
                    1 if any(k.lower() in tl for k in KEYWORDS_MARKET) else 0)
                if not tier:
                    continue
                _desc = _clean(desc.group(1)).strip() if desc else ""
                _desc = re.sub(r"\s+", " ", _desc)[:150] or "unavailable"
                out.append({"title": t, "source": src, "tier": tier,
                            "pub": pub_s.strip() if pub else "unavailable",
                            "taipei": dt.astimezone(TAIPEI).strftime("%Y-%m-%d %H:%M") if dt else "unavailable",
                            "summary": _desc, "link": lk})
                if sum(1 for x in out if x["source"] == src) >= 6:
                    break
        except Exception as e:  # noqa: BLE001
            print(f"[WARN] news feed failed {url}: {e}")
    out.sort(key=lambda x: -x.pop("tier"))
    seen, uniq = set(), []
    for x in out:
        if x["link"] not in seen:
            seen.add(x["link"])
            uniq.append(x)
    return uniq[:max_items]

def get(tw_n: int = 6, intl_n: int = 6) -> dict:
    tw = _tw_news(tw_n)
    intl_all = _intl_news(intl_n)
    seen = {x["link"] for x in tw}
    intl = [x for x in intl_all if x["link"] not in seen][:intl_n]
    note = ("台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；"
            "investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用")
    return {"items": tw + intl, "note": note, "ok": bool(tw + intl)}
