"""視覺層 V5：淺藍專業風，五頁（總結/現貨/重要市場/期貨/選擇權）。

- 總結 ← Daily_REPORT（verdict 判定卡＋KPI 7x2＋價位梯＋交易計畫＋國際Top3）
- 其餘四頁 ← DATA_REPORT 對應章節
只讀不寫，本機執行：streamlit run dashboard/app.py
"""
from __future__ import annotations
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"
DATA_DIR = ROOT / "data_reports"
LATEST = REPORTS_DIR / "latest.json"
APP_VERSION = "20260921a"

LIGHT_HEAD = ("<div style='border-left:5px solid #7fb3e8;background:#eaf3fd;"
              "padding:6px 12px;font-size:18px;font-weight:800;color:#1a3a5c;"
              "border-radius:0 6px 6px 0;margin:14px 0 8px;'>{}</div>")


def head(title: str):
    st.markdown(LIGHT_HEAD.format(title), unsafe_allow_html=True)


st.set_page_config(page_title="每日盤前分析", page_icon="📈", layout="wide")
st.markdown("<style>div.block-container{padding-top:3.5rem;max-width:1220px}"
            "table{font-size:13px}</style>",
            unsafe_allow_html=True)

# ---------------- 解析 ----------------
def md_tables(md: str, section: str) -> list[pd.DataFrame]:
    m = re.search(rf"{re.escape(section)}([\s\S]*?)(?=^#{{1,4}} |\Z)", md, re.M)
    if not m:
        return []
    out = []
    for tm in re.finditer(r"((?:\|.*\n){3,})", m.group(1)):
        lines = [l.strip() for l in tm.group(1).strip().splitlines() if l.strip()]
        if len(lines) < 3:
            continue
        hdr = [c.strip() for c in lines[0].strip("|").split("|")]
        rows = [[c.strip() for c in ln.strip("|").split("|")] for ln in lines[2:]]
        try:
            out.append(pd.DataFrame(rows, columns=hdr))
        except Exception:
            pass
    return out

def md_table(md: str, section: str, idx: int = 0) -> pd.DataFrame | None:
    ts = md_tables(md, section)
    return ts[idx] if len(ts) > idx else None

def parse_blocks(md: str) -> dict:
    out: dict[str, list] = {}
    for name in ("kpi", "levels", "oidist", "scenarios", "verdict"):
        m = re.search(rf"```{name}\n(.*?)```", md, re.S)
        rows = []
        if m:
            for line in m.group(1).strip().splitlines():
                parts = [c.strip() for c in line.split("|")]
                if len(parts) >= 2:
                    rows.append(parts)
        out[name] = rows
    return out

def section_text(md: str, header: str) -> str:
    m = re.search(rf"(?m)^(#+) .*?{re.escape(header)}.*?$", md)
    if not m:
        return ""
    level = len(m.group(1))
    out = []
    for line in md[m.end():].splitlines():
        hm = re.match(r"^(#+) ", line)
        if hm and len(hm.group(1)) <= level:
            break
        out.append(line)
    return "\n".join(out).strip()

def num(x) -> float | None:
    try:
        return float(str(x).replace(",", "").replace("+", "").replace("%", ""))
    except (ValueError, TypeError):
        return None

@st.cache_data(ttl=60)
def load_latest() -> dict | None:
    try:
        return json.loads(LATEST.read_text(encoding="utf-8"))
    except Exception:
        return None

@st.cache_data(ttl=60)
def load_md(path_str: str) -> str | None:
    try:
        p = ROOT / path_str
        return p.read_text(encoding="utf-8") if p.exists() else None
    except Exception:
        return None

def list_history() -> list[str]:
    if not REPORTS_DIR.exists():
        return []
    return sorted((f.name for f in REPORTS_DIR.glob("Daily_REPORT_*.md")), reverse=True)

# ---------------- 載入 ----------------
latest = load_latest()
if latest is None:
    st.error("尚無報告：找不到 reports/latest.json。")
    st.stop()
history = list_history()
sel = st.sidebar.selectbox("歷史報告", history if history else ["(無)"])
ana_path = f"reports/{sel}" if history else latest.get("report_path", "")
md = load_md(ana_path)
if md is None:
    st.error(f"找不到分析報告：{ana_path}")
    st.stop()
mdate = re.search(r"(\d{8})", sel or "")
rdate = mdate.group(1) if mdate else latest.get("report_date", "")
dpath = f"data_reports/DATA_REPORT_{rdate}.md"
dmd = load_md(dpath) or ""
ymd = f"{rdate[:4]}-{rdate[4:6]}-{rdate[6:]}" if len(rdate) == 8 else rdate
t0d = f"{rdate[:4]}-{rdate[4:6]}-{rdate[6:]}" if len(rdate) == 8 else rdate
gen = str(latest.get("generated_at", ""))[:10]
try:
    datetime.strptime(gen, "%Y-%m-%d")
    ymd = gen
except ValueError:
    try:
        ymd = (datetime.strptime(t0d, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    except ValueError:
        pass
blocks = parse_blocks(md)
GH = "https://github.com/grichtoyang/daily-premarket/blob/master"
gh_data = f"{GH}/{dpath}"
gh_ana = f"{GH}/{ana_path}"

st.header("每日盤前分析 Dashboard")
st.caption(f"**{ymd} 盤前報告（資料：{t0d} 收盤）**｜Asia/Taipei｜"
           f"價位無特別標註者皆為**台指期近月 (TX)**｜"
           f"[原始 DATA 報告]({gh_data})")

tab_sum, tab_spot, tab_mkt, tab_fut, tab_opt = st.tabs(
    ["總結", "現貨", "重要市場", "期貨", "選擇權"])

# ================= 總結 ← Daily =================
with tab_sum:
    head("總結")
    vd = {r[0]: (r[1] if len(r) > 1 else "") for r in blocks["verdict"]} if blocks["verdict"] else {}
    direction = vd.get("方向", "")
    dcolor = {"偏多": "green", "偏空": "red"}.get(direction, "gray")
    v1, v2 = st.columns([1.3, 1])
    with v1:
        oneline = re.search(r"一句話結論[：:]\s*(.+)", md)
        if oneline:
            st.info(f"💡 {oneline.group(1).strip()}")
        if vd:
            st.markdown(f"**今日盤勢判定：:{dcolor}[{direction}]**　信心：{vd.get('信心', 'N/A')}")
            for k in sorted(vd):
                if k.startswith("理由"):
                    st.markdown(f"- {vd[k]}")
            if vd.get("注意"):
                st.warning(f"⚠️ {vd['注意']}")
    with v2:
        bval = {"偏多": 60, "偏空": -60}.get(direction, 0)
        jb = re.search(r"劇本[一二三四]", dmd)
        if jb:
            bval += {"劇本一": 15, "劇本二": -10, "劇本三": -15, "劇本四": 10}[jb.group(0)]
            bval = max(-100, min(100, bval))
        fig = go.Figure(go.Indicator(
            mode="gauge+number", value=bval, number={"font": {"size": 42}},
            title={"text": "盤前 Bias", "font": {"size": 15}},
            gauge={"axis": {"range": [-100, 100]}, "bar": {"color": "#1a3a5c"},
                   "steps": [{"range": [-100, -20], "color": "#f8d7da"},
                             {"range": [-20, 20], "color": "#fff3cd"},
                             {"range": [20, 100], "color": "#d4edda"}]}))
        fig.update_layout(height=270, margin=dict(l=20, r=20, t=70, b=10))
        st.plotly_chart(fig, use_container_width=True)
    head("關鍵數據")

    def fmt_num(v: str, unit: str = "") -> str:
        s = str(v).strip()
        # 單位是「點」：四捨五入到整數
        if unit == "點":
            try:
                return str(int(round(float(s.replace(',', '').replace('+', '')))))
            except (ValueError, TypeError):
                return s
        # 一般：.00 去掉
        if re.fullmatch(r"[+-]?[\d,]+\.00", s):
            return s.split(".")[0]
        return s

    kpis = blocks["kpi"]
    if kpis:
        for chunk in (kpis[:7], kpis[7:14]):
            if not chunk:
                continue
            cols = st.columns(7)
            for i, row in enumerate(chunk):
                unit_raw = row[2] if len(row) > 2 else ""
                unit_show = unit_raw.replace("億元", "億") if unit_raw else ""
                val = fmt_num(row[1], unit_raw) + (f" {unit_show}" if unit_show else "")
                cols[i].markdown(
                    f"<div style='background:#fff;border:1px solid #aebfd6;border-top:4px solid "
                    f"#7fb3e8;border-radius:7px;padding:8px;min-height:86px'>"
                    f"<div style='font-size:13px;color:#5e6b80;font-weight:800'>{row[0]}</div>"
                    f"<div style='font-size:21px;font-weight:900;color:#1a3a5c;white-space:nowrap;"
                    f"overflow:hidden;text-overflow:ellipsis' title='{val}'>{val}</div></div>",
                    unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        head("關鍵價位梯")
        lv = blocks["levels"]
        prices = []
        for row in lv:
            if len(row) >= 2 and num(row[1]) is not None:
                prices.append((row[0], num(row[1]),
                               {"壓力": "#e74c3c", "中軸": "#7f8c8d", "支撐": "#27ae60"}.get(row[0], "#7fb3e8")))
        if prices:
            mid = next((p for n, p, _ in prices if n == "中軸"), None)
            mid = mid if mid is not None else sum(p for _, p, _ in prices) / len(prices)
            lo, hi = mid - 500, mid + 500
            fig = go.Figure()
            placed = []
            for name, p, c in sorted(prices, key=lambda x: x[1]):
                src = next((r[2] if len(r) > 2 else "" for r in lv if r[0] == name), "")
                side = "right"
                if any(abs(p - q) < 180 for q in placed):
                    side = "left"
                placed.append(p)
                fig.add_hline(y=p, line_color=c, line_width=2.5,
                              annotation_text=f"{name} {p:,.0f}｜{src}",
                              annotation_position=side, annotation_font_size=10)
            fig.add_hline(y=mid, line_color="#7fb3e8", line_width=1, line_dash="dot")
            fig.update_layout(height=360, margin=dict(l=10, r=150, t=10, b=30),
                              yaxis=dict(range=[lo, hi], title="點位"),
                              xaxis=dict(visible=False), showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            st.caption("選位理由：壓力取夜盤高（隔日第一關）＋Call Wall（上檔鐵板）；"
                       "中軸取台指期收盤（多空分界）；支撐取三牆合流。紅＝壓力／綠＝支撐／灰＝中軸")
    with c2:
        head("今日交易計畫")
        sc = blocks["scenarios"]
        if sc:
            hdr = sc[0] if any("情境" in c for c in sc[0]) else None
            body = sc[1:] if hdr else sc
            ncols = max(len(r) for r in body) if body else 3
            cols = (hdr + [""] * ncols)[:ncols] if hdr else ["情境", "條件", "操作", "停損"][:ncols]
            st.table(pd.DataFrame([((r + [""] * ncols)[:ncols]) for r in body], columns=cols))
    head("今日國際焦點 Top3")
    news_sec = section_text(dmd, "重大經濟數據")
    evts = re.findall(r"^- 事件\d+：(.+)$", news_sec, re.M)[:3]
    if evts:
        st.table(pd.DataFrame({"事件": evts}))
    for sec in ("現貨市場分析", "重要市場環境", "國際事件與新聞解讀", "台指期分析",
                "選擇權市場分析", "整合判讀", "盤前交易執行框架", "最終結論"):
        t = section_text(md, sec)
        if t:
            with st.expander(sec, expanded=(sec == "最終結論")):
                st.markdown(t.split("## 附錄")[0][:2500])

# ================= 現貨 ← DATA 第一章 =================
with tab_spot:
    head("現貨")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        t1 = md_table(dmd, "台股大盤行情")
        if t1 is not None:
            a, b = st.columns([1, 1])
            with a:
                st.subheader("台股大盤行情")
                st.table(t1.iloc[:, :3])
            with b:
                st.subheader("市場漲跌家數")
                for sec in ("上市公司", "上櫃公司"):
                    t = md_table(dmd, sec)
                    if t is not None:
                        st.markdown(f"_{sec}_")
                        st.table(t)
        t3 = md_table(dmd, "三大法人現貨買賣超")
        if t3 is not None:
            a, b = st.columns([1, 1])
            with a:
                st.subheader("三大法人現貨買賣超")
                st.table(t3)
            with b:
                try:
                    vals = [num(r[1]) or 0 for _, r in t3.iterrows()]
                    fig = go.Figure(go.Bar(
                        x=list(t3.iloc[:, 0]), y=vals,
                        marker_color=["red" if v < 0 else "green" for v in vals]))
                    fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10),
                                      showlegend=False, yaxis_title="億元")
                    st.plotly_chart(fig, use_container_width=True)
                except Exception:
                    pass
        a, b = st.columns(2)
        with a:
            head("融資融券")
            t = md_table(dmd, "融資融券")
            if t is not None:
                st.table(t.iloc[:, :3])
        with b:
            head("借券資料")
            t = md_table(dmd, "借券資料")
            if t is not None:
                st.table(t.iloc[:, :3])
        head("市場成交結構")
        t = md_table(dmd, "市場成交結構")
        if t is not None:
            st.table(t)

# ================= 重要市場 ← DATA 第二章 =================
with tab_mkt:
    head("重要市場")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        for sec in ("美股指數", "亞洲主要指數", "美股指數期貨", "美國國債殖利率",
                    "主要匯率", "台灣相關ADR", "原油黃金Bitcoin"):
            t = md_table(dmd, sec)
            if t is not None:
                st.subheader(sec)
                st.table(t)
        head("重大事件與新聞")
        news = section_text(dmd, "重大經濟數據")
        evts = re.findall(r"^- 事件\d+：(.+)$", news, re.M)[:10]
        if evts:
            st.table(pd.DataFrame({"事件": evts}))
        with st.expander("新聞明細"):
            st.markdown(news[:4000] if news else "無")


# ================= 期貨 ← DATA 第三章 =================
with tab_fut:
    head("期貨")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        for sec in ("台指期近月日盤行情", "台指期近月夜盤行情", "法人台指期多空未平倉部位",
                    "前十大交易人多空未平倉部位", "日盤、夜盤法人交易資料",
                    "期貨與現貨關係", "日盤、夜盤與籌碼變化對照"):
            ts = md_tables(dmd, sec)
            if not ts:
                continue
            head(sec)
            for t in ts:
                st.table(t)
        with st.expander("夜盤劇本分類"):
            st.markdown(section_text(dmd, "夜盤劇本分類")[:1500])

# ================= 選擇權 ← DATA 第四章 =================
with tab_opt:
    head("選擇權")
    st.link_button("選擇權倒莊監控圖（玩股網，需會員登入）",
                   "https://www.wantgoo.com/option/runaway-bankers")
    if not dmd:
        st.warning(f"找不到 {dpath}")
    else:
        oi = blocks["oidist"]
        calls = [(int(r[1].replace(",", "")), int(r[2].replace(",", "")))
                 for r in oi if len(r) >= 3 and r[0] == "call"
                 and r[1].replace(",", "").isdigit()]
        puts = [(int(r[1].replace(",", "")), int(r[2].replace(",", "")))
                for r in oi if len(r) >= 3 and r[0] == "put"
                and r[1].replace(",", "").isdigit()]
        call_map = {k: v for k, v in calls}
        put_map = {k: v for k, v in puts}
        if call_map or put_map:
            head("選擇權 T 字報價 (OI)")
            strikes = sorted(set(call_map) | set(put_map), reverse=True)
            lv_map = {}
            for row in blocks["levels"]:
                if len(row) >= 2 and num(row[1]) is not None:
                    lv_map[row[0]] = num(row[1])
            mid_px = lv_map.get("中軸")
            near_mid = min(strikes, key=lambda s: abs(s - mid_px)) if mid_px else None
            trows, rcolors = [], []
            for s in strikes:
                mark, color = "", ""
                for name, val in lv_map.items():
                    if val == s:
                        if name.startswith("壓力"):
                            mark += "▲"
                            color = "#f8d7da"
                        elif name.startswith("支撐"):
                            mark += "▼"
                            color = "#d4edda"
                        else:
                            mark += "★"
                            color = "#fff3cd" if not color else color
                if near_mid is not None and s == near_mid and "★" not in mark:
                    mark += "≈中軸"
                    color = color or "#e2e3e5"
                trows.append({"Put OI": put_map.get(s, "—"),
                              "履約價": f"{s:,}{mark}",
                              "Call OI": call_map.get(s, "—")})
                rcolors.append(color)
            df = pd.DataFrame(trows)
            try:
                sty = df.style.apply(
                    lambda r: [f"background-color:{rcolors[r.name]}"
                               if rcolors[r.name] else "" for _ in r],
                    axis=1)
                st.dataframe(sty, use_container_width=True, hide_index=True)
            except Exception:
                st.table(df)
            st.caption("▲壓力（紅底）／▼支撐（綠底）／★中軸（灰底）；"
                       "中軸＝台指期收盤價附近的多空分界參考（取最接近收盤的履約價列，≈中軸）；"
                       "左 Put 右 Call，仿 T 字報價")
        for sec in ("選擇權交易日期", "Call 總成交量", "Put 總成交量", "Call／Put 比例",
                    "外資 Call", "自營商 Call", "選擇權法人日盤", "選擇權前十大",
                    "Call OI 集中", "Put OI 集中",
                    "Call OI 增減", "Put OI 增減", "Call Wall", "Put Wall",
                    "Gamma Wall", "Gamma Flip", "Max Pain"):
            for t in md_tables(dmd, sec):
                head(sec)
                st.table(t)

st.divider()
st.caption(f"分析報告：[{ana_path}]({gh_ana})｜原始數據：[{dpath}]({gh_data})｜"
           "價位未特別標註者皆為台指期近月 (TX)｜非投資建議，僅供參考")
