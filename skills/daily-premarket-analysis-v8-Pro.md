---
name: daily-premarket-analysis-v8
description: Produce structured 台股 V8 Pro (templates/v8-pro-golden-master.html hash 87d5f1928f6b)  台股 (TWSE / TX) daily pre-market analysis reports in the exact style of the existing 台指盤前 report. Use when user asks for 盤前分析, 每日盤前, 台指盤前, pre-market report, dashboard, or to update / generate the daily bias + levels + scenarios for the Taiwan Index futures. Also generates self-contained HTML dashboard with charts when requested. Primary data source is GitHub Pages https://grichtoyang.github.io/daily-premarket/data_reports/ via Cloudflare Workers twse-proxy and taifex.grichtoyang.workers.dev. Includes AI深度結論, 本日交易計畫, and v8 Pro V8 Canvas引擎機構級 + four-page fusion + full Canvas + three-layer interpretation (分析/判斷/操作) for every block.
---

# 台股每日盤前分析 Skill v7 Pro (附件原版 100% 一致性保證 + 圖表異常修復)

## When to activate
- User says「盤前分析」「每日盤前」「台指盤前」「幫我做今天的盤前」「更新盤前報告」「讀今天 Pages」
- User asks for「dashboard」「產出 dashboard」「HTML」「圖表」「v4」「v6.1」「v7」「四頁」「融合版」「Canvas」「專業」「機構級」「V6引擎」
- User says「AI分析」「交易計畫」「本日交易計畫」「分析判斷操作」
- User says 圖表做的不如V6版好 / 圖表很專業我很喜歡

## Core principles v7 Pro

1. **Data first, opinion second.** Every number must come from Pages md. Never invent.
2. **Bias quantitative 0-100 10因子.** v7 verified Score 34 屬重挫後超賣 6空4多
3. **Scenarios conditional 3條.** Anchor 夜低45,523 / Flip45,920 / 夜高46,399
4. **Sources mandatory.** Pages https://grichtoyang.github.io/daily-premarket/data_reports/DATA_REPORT_*.md + Workers
5. **Cutoff explicit.** 2026-10-24 11:24:33 Asia/Taipei 夜盤10/22 15:00–10/23 05:00
6. **Holiday awareness.** 2026-10-23 薔琵颱風休市 + 周末 -> next open 2026-10-27 Tuesday
7. **AI+交易計畫 mandatory.** AI綜合研判5面向 + AI綜合結論 + 本日交易計畫4階段 + Kelly0.18 + 歷史相似2024/05 72% 平均+320點
8. **Three-layer mandatory.** EVERY card must have 🔍分析 🧭判斷 🎯操作 background #0f1b2d border #1e2e45
9. **Four-page fusion.** 4 tabs 總結 現貨 期貨 選擇權，附件5頁中重要市場併入
11. **Canvas Pro V6引擎 mandatory.** 40+ canvases, native 2D, DPR, debounce 300ms, rect.width===0 skip, grid()虛線, axes(), gradient area, 點位, 數值標籤, V6質感

## Data Schema (20261023 verified)

Header: 報告日期2026-10-24 T0 2026-10-23 產出11:24:33 Asia/Taipei 下次開盤2026-10-27
現貨: 加權46,041.43 -846.34 -1.81% 開46,942 高47,332 低46,041 成交9,334.4億 上市+上櫃10,568.9億 漲跌家數上市247上櫃146 全面普跌 僅少數抗跌 情緒恐慌 三大法人-815.8+94.9-273.8-994.7 融券216,539+24,702 融資8,465.1億-138.3億 維持率176.99%/182.90% 借券2,465,395/4,580,250張/458萬張高檔 空方量1,234.5億估 中小型同步重挫
美股: S&P7623.68-0.52% Nasdaq25955.34-0.21% Dow52215.20-1.23% SOX10779.46+0.44% VIX19.45+2.21% TSM ADR418.51+1.49% / 事件版SOX-6.72%崩 TSM ADR-4.52% ASE ADR-11.01% NQ期-2.96% DXY101.2 台幣32.59貶 美10Y4.95% 原油黃金Bitcoin 日經225 道瓊期
期貨: TX202611 日47164/47337/46217/46272-741-1.58%量55226基差+230.57正價差0.50% 夜46270/46399/45523/45654-580-1.25%量39368變化-618振幅876 外資日-1221夜+1049/夜-918 前十大+9024變化+1334 投信+83,601自營+3260
選擇權: Call量178535OI55024 Put量155316OI31411 C/P量比1.15OI比1.75PCR0.57極低極度悲觀 CallWall49K2444 4.44%天花板磁吸 PutWall46K1829 5.82%防線多空線 GammaWall47K Flip45920.93多空翻轉站回翻多 MaxPain46K磁吸二 反壓重65%失敗 TopCall49K47K51K TopPut46K46.5K45.5K45K 外資Call日+118Put日-181夜+53+370日總+299夜-317自營Call日+822Put日-1933大戶期貨+1334買權-215賣權-350 GEX-2.3B ShortGamma ZeroGamma45920.93加速區 Charm-0.42 Vanna-0.18 IVRank78%25DRR-2.5%Term32%>26%>22%短期恐慌 EM±1.2%±550

## V7 Pro Canvas引擎規格 (V6水準，使用者認可很專業)

**視覺系統:**
- 背景 radial-gradient 1200px 600px at 20% -10% #112040→#060a10
- 卡片 linear-gradient #111a28→#0e1726 border #223247 radius14px shadow0 8px 24px rgba(0,0,0,.35)
- header sticky blur14px bg #060a10e6 border #223247
- tabs底色 #0c1524 padding4px radius10px border #223247 active linear-gradient #6bb6ff→#4a8fe0 shadow0 2px 12px rgba(107,182,255,.4)
- canvas背景 radial-gradient 400px 200px at 50% 0% #111f35→#0c1524 border #1c2e45 radius10px height 180 default 220/240 for levels/timeline/plan
- 字体 @import Noto Sans TC + JetBrains Mono

**Canvas helper mandatory:**
```js
function setupCanvas(id,draw,h=180){
  const c=document.getElementById(id);if(!c)return;
  function rs(){
    const p=c.parentElement;if(!p)return;
    const r=p.getBoundingClientRect();if(r.width===0)return;
    const dpr=devicePixelRatio||1;
    c.width=r.width*dpr; c.height=h*dpr;
    c.style.width=r.width+'px'; c.style.height=h+'px';
    const ctx=c.getContext('2d'); ctx.setTransform(dpr,0,0,dpr,0,0);
    draw(ctx,r.width,h)
  }
  let t; window.addEventListener('resize',()=>{clearTimeout(t);t=setTimeout(rs,300)}); rs()
}
function grid(ctx,W,H){ctx.strokeStyle='#172538';ctx.setLineDash([3,3]);for(i=1;i<4;i++){ctx.beginPath();ctx.moveTo(50,i*H/4);ctx.lineTo(W-20,i*H/4);ctx.stroke()}ctx.setLineDash([])}
```

**16圖機構級繪圖定義 (必須照此實作，V6水準):**

1. Spot5日 47111/46822/46293/46888/46041: line+gradient area rgba(255,92,109,.35→0) + 點底#0a1220+邊框紅 + 數值label + 日期label + axes min45800 max47300
2. Night Path O46270 H46399 L45523 C45654: line藍 + gradient area rgba(107,182,255,.25→0) + 點紅/藍 + H/L標籤生命線 + 虛線紅L45523
3. Institutional 外資-815.8投信+94.9自營-273.8: 水平bar底#101c2f 漸層 + 中軸
4. US% Dow-1.23 S&P-0.52 Nasdaq-0.21 SOX-6.72 TSM-4.52 ASE-11.01 NQ-2.96 VIX+2.21: 分歧bar中軸W/2 紅/綠/黃
5. Foreign Futures -1221 +1049 +9024 +1334: 分歧bar中軸
6. Call vs Put OI Donut 55024 vs 31411: donut r52 ir34 藍/黃 內圈OI比1.75
7. Call OI Top 49K2444 4.44% 47K1800 51K1500: 垂直bar底#101c2f 漸層藍#6bb6ff→#2a5aa8 數值label
8. Put OI Top 46K1829 5.82% 46.5K1500 45.5K1300: 同上漸層黃#f5c86a→#a07a1f
9. GEX -2.3B Zero45920.93: grid + zero線#2a3a52 + Short Gamma紅半透明區 + Zero藍虛線 + 斜線加速
10. IV Skew Rank78% RR-2.5% Charm-0.42 Vanna-0.18: 微笑曲線 quadraticCurve + 點
11. Term 32%>26%>22%倒掛: 折線黃 + 點 + label週月季 + 紅字倒掛短期恐慌
12. PCR 0.74→0.57極低: 遞減紅線 + 點 + label0.74 0.68 0.60 0.57極低 + 紅字PCR極悲觀
13. Foreign Options +118-181+53+370+822-1933: 分歧bar
14. VIX&DXY VIX19.45 DXY101.2: 雙線紅藍 + label
15. Fund Flow 半導體-2.5 AI-1.2 金融+0.3 PCB-0.8 原物料-0.5: 水平分歧
16. Correlation 5x5 加權 SOX NQ TSM DXY: heatmap rgba(107,182,255,alpha)正 藍 負紅 + 數值

**其他圖 V6引擎:**
- c-gauge Bias34: arc #172538底 14px寬 + gradient 綠黃紅 + 數值28px + 文字震盪偏空46K防線
- c-kpi: 分歧bar底#101c2f + 中軸#22364e + 數值
- c-spot c-tx: proLine gradient area + 點
- c-futoi: 外資-87297 前十大+9024 投信+83601 自營+3260 分歧
- c-optwall: Call藍漸層 Put黃漸層 雙區
- c-us: 分歧bar
- c-levels 12階: 虛線 + 顏色紅極限壓力 黃中軸 綠支撐 藍Flip + 標籤 R4 47895 R3 47332 R2 47000 R1 46702 P46471 S1 46041 S3 45523 Put Wall46K Flip45920.93
- c-core: 雷達7軸 外資期空 爆量長黑 台幣貶 美債高 恐慌 正價差 減肥
- c-scen: 三路徑紅A55% 黃B30% 綠C15%
- c-check: donut判斷 多方綠 空方紅 中心l/s
- c-pre: 6項進度bar 綠/紅
- c-ai5: 雷達5軸 5面向
- c-aicon: 路徑守住45523反彈55%目標46,200-46,500失效45,000-44,700
- c-plan: 時間軸5點 08:45 09:30 11:30 13:30 15:00 + 藍路徑
- c-timeline: 熱圖紅高黃中 + 旋轉label -45度
- s1 s3 s4 s6 f1 f2 f5 f6 o2 o3 o6 o7 同V6引擎 漸層+grid+label

**所有卡必須有分析判斷操作三行，具體非模板**

## Required output structure v7 Pro

**總結頁 18卡+16圖:**
1 一句話結論+Bias gauge 34 空方主導開低防破底46K防線
2 市場快照KPI 8宮格 -994.7 -815.8 +94.9 -273.8 216,539 182.90%/176.99% 458萬張 +230.57 0.57 + bar V6
3 16圖機構級大區 grid2 16 canvases V6引擎
4 大盤全景 加權46,041 開46,942 高47,332 低46,041 漲跌-846 成交9,334.4億 10,568.9億 上市247 上櫃146 空方量1,234.5億估 + Spot5日 V6
5 三大法人+融資融券借券全景 + Institutional V6
6 台指期日夜 日46272基差+230.57正價差0.50%假多 夜45654-580振幅876 + Night Path V6
7 期貨籌碼深度 外資淨空-87,297創高 日-1221夜-918 前十大+9024投信+83,601自營+3,260 + Foreign Futures V6
8 選擇權結構牆 Call量178535OI55024 Put量155316OI31411 PCR0.57 CallWall49K2444 PutWall46K1829 Gamma47K Flip45920.93 MaxPain46K GEX-2.3B IV78% Term32>26>22 + Call vs Put OI V6 + 牆V6
9 美股與重要市場 S&P-0.52% Nasdaq-0.21% Dow-1.23% SOX-6.72%崩 TSM-4.52% ASE-11.01% NQ-2.96% VIX19.45 DXY101.2 台幣32.59 美10Y4.95% 原物料 原油黃金Bitcoin 亞洲日經225 道瓊期 + US% V6
10 權重與族群 2330台積 2317鴻海 半導體 AI server 金融 PCB 原物料 + Fund Flow V6
11 關鍵水位12階融合版 R4 47895 R3 47332 R2 47000 R1 46702 P46471 S1 46041 S2 45654 S3 45523 PutWall46K Flip45920.93 MaxPain46K 吸附履約價 + 階梯圖V6 h240
12 盤前核心判斷 支持偏空7點 限制追空5點 狀態支持偏空 + 雷達7軸V6
13 三劇本+Opening Range A55% B30% C15% 15分高低為第一區間 振幅876 + 三路徑V6
14 多空條件檢查表 checkbox 2欄 多方任三試多7項 空方任三續空4項 觀望任一2項 + donut判斷即時5狀態 + V6
15 開盤前必核 6項 美期 VIX 台積ADR 外資夜盤 台幣 融資 + 進度條V6
16 AI綜合研判5面向 現貨9334億月線失守 籌碼8465億維持率176.99% 期貨振幅876外資淨空 選擇權壓力重46K 國際NQ崩 + 雷達5軸V6
17 AI綜合結論 國際拖累型修正 美半導體崩主因 外資高空單 關鍵45523多殺多至44700-44982 站回46200反彈至47000 空方順勢減半 + 路徑圖V6
18 本日交易計畫4階段 開盤09:00-09:30 盤中09:30-11:30 下午12-13 夜盤15 風險Kelly0.18 VaR-680 ES-1050 ATR480 EM±550 歷史相似2024/05 72% 平均+320點 + 時間軸V6 h240
19 行事曆10則 21:30初請 20:30台積法說 18:45日月光ADR 15:00台幣貶 13:30融資176.99% 10:00加權-846 09:00美10Y 04:00NQ期 昨日外資期空-87297 昨日借券458萬張 + 法人解讀技術修正非基本面反轉 + 衝擊熱圖V6 h240 旋轉label

**現貨頁 10卡 V6引擎每卡canvas:**
台股大盤行情 漲跌幅 成交金額 + canvas
市場漲跌家數 上市247上櫃146 全面普跌 + canvas
三大法人 -815.8 +94.9 -273.8 -994.7 + canvas
融券餘額 借券資料 216,539/253,430 2,465,395/4,580,250/458萬張 維持率182.90%/176.99% + 趨勢canvas
市場成交結構 爆大量價跌量增 空方量1,234.5億估 + canvas
融資維持率 8,465.1億-138.3億 176.99%警戒 + 雙軸canvas h240
權重與族群 2330台積 2317鴻海 2308台達 2382廣達 3711日月光 半導體 AI server 金融 PCB 原物料 + canvas
相關指數 電子 金融 半導體30 中型100 + canvas
台灣相關ADR 台積電 日月光 原油黃金Bitcoin 日經225 + canvas
外資投信買賣超清單 Top + canvas

**期貨頁 8卡 V6引擎:**
台指期近月日盤 O47164 H47337 L46217 C46272 -741 -1.58% 量55,226 基差+230.57 正價差0.50% + 日K簡圖canvas
台指期夜盤 O46270 H46399 L45523 C45654 -580 -1.25% 量39,368 振幅876 + 夜路徑canvas
基差與價差 +230.57 0.50%假多 現貨收盤附近 中軸46041 支撐帶45920 + 趨勢canvas
期貨籌碼深度 外資淨-87,297創高 日-1221夜-918 前十大+9024變化+1334 投信+83,601自營+3,260 + OI趨勢canvas
成交量與振幅 55,226口 876點波動劇烈 + 量能canvas
關鍵水位與Pivot 12階融合版 吸附履約價上色 說明讀法 + 階梯圖canvas h240
美股指數期貨連動 NQ期-2.96% 道瓊期 + 連動%canvas
交易與風險提示 日盤正價差仍有撐 跌不破支撐 單日減肥 清理浮額 具磁吸中軸回歸 + canvas

**選擇權頁 9卡 V6引擎:**
選擇權地圖 基差假多 現貨收盤 新版中軸 重壓區 + 地圖canvas
Call vs Put OI Call量178535OI55024 Put量155316OI31411 C/P量比1.15OI比1.75PCR0.57極低極度悲觀 + 雙bar漸層canvas
牆結構 CallWall49K2444 4.44%天花板磁吸 PutWall46K1829 5.82%防線多空線 GammaWall47K Flip45920.93多空翻轉站回翻多 MaxPain46K磁吸二 反壓重65%失敗 + 牆直方圖canvas h240 漸層
Top OI TopCall49K47K51K TopPut46K46.5K45.5K45K + 分布canvas
法人選擇權 外資Call日+118Put日-181夜+53+370日總+299夜-317自營Call日+822Put日-1933大戶期貨+1334買權-215賣權-350 + 分組長條canvas
GEX與希臘字母 GEX-2.3B ShortGamma ZeroGamma45920.93加速區 Charm-0.42 Vanna-0.18 + GEX柱+零線canvas h240
IV與期限 Term32%>26%>22%短期恐慌 IVRank78%25DRR-2.5% EM±1.2%±550 + Term折線canvas
PCR趨勢 0.57極低極度悲觀 0.74->0.57 + 折線canvas
操作地圖 綜合牆操作 + canvas

**HTML Dashboard Spec v7 Pro:**
- Dark radial-gradient #060a10 #112040, panel #111a28→#0e1726, line #223247, muted #8ea0b8, text #e6eef8
- Sticky header blur14px, 4 tabs 總結 現貨 期貨 選擇權, Bias gauge gradient, KPI 8-grid, 16+40 canvases
- Canvas: native 2D no CDN, DPR, debounce 300ms, rect.width===0 skip, grid()虛線, axes(), gradient area, 點+數值
- Charts: Spot 5-day Night path Institutional US% Foreign futures Call vs Put OI Call OI dist Put OI dist GEX Zero Gamma IV Skew Term PCR Foreign options VIX&DXY Fund flow Correlation + per-page
- Levels pills 12階, Scenarios 3 cards, AI 5雷達, Trading Plan 時間軸, Checklist checkbox donut即時判斷5狀態, Timeline 10 events旋轉label
- Every card div.interpretation 3 rows 🔍🧭🎯 bg #0f1b2d border #1e2e45
- Mobile-first single HTML no CDN @import Noto Sans TC + JetBrains Mono mono
- No Print button

Footer: 2026-10-23 薔琵颱風休市 + 周末 下次開盤2026-10-27週二 · 融券借券民間估算 · 選擇權牆吸附至履約價上色 · 盤前核心判斷v5.2保留+v5.1融合 · 歷史相似2024/05相似度72% · Kelly0.18 · V6引擎機構級

Sources: Pages https://grichtoyang.github.io/daily-premarket/data_reports/DATA_REPORT_20261024.md + Workers twse-proxy + taifex.grichtoyang.workers.dev + TPEX + HiStock + Yahoo Finance


## Golden Master Reference (Exact Reproducibility Fix 2026-10-27)

**Root cause of non-identical dashboards:**
Previous skill file was purely descriptive (文字描述). The artifact agent (create_web_artifact_agent) interprets description anew each time, so it generates different canvas code (simplified bar, no gradient, no grid). The liked V7 Pro dashboard you said 很專業 was NOT generated by the agent, but by python_execution writing templates/v7-pro-golden-master.html with exact V6 engine (grid()虛線, gradient area, DPR, debounce, point labels).

**Fix:**
- Golden Master HTML is templates/v7-pro-golden-master.html (52,510 bytes, 2026-10-27 V6引擎重建版). This is the canonical reference you liked.
- Future generation MUST NOT re-interpret description. Instead MUST copy this file's <style> and <script> canvas engine verbatim, including:
  - setupCanvas() with DPR, rect.width===0 skip, debounce 300ms
  - grid() setLineDash([3,3]) #172538
  - All 16+40 canvas draw functions with gradient, point, label as in golden master
  - Visual system radial-gradient #112040→#060a10, card linear-gradient #111a28→#0e1726
- When calling create_web_artifact_agent, MUST pass this file via files param and reference its exact path in prompt: "Base on templates/v7-pro-golden-master.html, copy its style and script verbatim"
- Skill description remains for data schema, but canvas implementation is locked to golden master to ensure 100% identical output.
- If data changes (new trading day), only update numbers in tables, DO NOT change canvas drawing logic.

**Verification:**
After generation, compare canvas count (should be 40+), check c1-c16 exist with gradient, check c-gauge arc gradient, check c-levels虛線. If not identical to golden master, regeneration failed.

Golden Master files:
- templates/v7-pro-golden-master.html (single HTML, V6 engine, liked)

## v7 Pro Stable - 100% 一致性保證 (2026-10-27 修正)

**問題根源診斷：**
1. create_web_artifact_agent 是 LLM 生成，每次都重新詮釋文字描述，canvas 程式碼不可能完全相同
2. 你最喜歡的 V8 Pro Dashboard (附件) 是用 python_execution 直接寫入 templates/v7-pro-golden-master.html 的，這是唯一能保證 100% 相同的方法
3. 照 skill 文字重跑 → 走 agent 路徑 → 必然失真

**穩定解法 - Golden Master 鎖定 + Template Copy：**
- 未來任何「照 V7 Pro 規格產出」都必須執行：
  ```python
  import shutil
  shutil.copyfile("templates/v7-pro-golden-master.html", "dashboards/taifex-{{date}}.html")
  ```
  然後只用字串替換改數據，不改任何 JS/CSS
- 禁止再呼叫 create_web_artifact_agent 去重繪 canvas，必須用 python copy 才能保證 byte-identical
- 數據更新時，只替換表格中的數字與文字，保留所有 canvas draw 函數原封不動

**為什麼這樣才能穩定：**
- LLM 是非確定性的，文字描述→程式碼 永遠會有變異
- 只有「檔案複製」是確定性的，byte-identical 保證
- Canvas 引擎已經是 V6 專業水準，不需要再重寫，只需要換數據

**執行指令：**
以後使用者說「實測再跑一次」「照 V7 Pro 規格產出」→ 直接 copy Golden Master → 改日期與數據 → 回傳該檔案的 container 路徑


## 每日數據更新流程 (版型鎖死，數據每日換)

**問題：** 每日盤前數據都會變，但你要求版型必須跟 V7 Pro 附件一模一樣

**解法：Template Copy + Data Injection**

1. **版型 Golden Master 鎖死**
   - 路徑: templates/v7-pro-golden-master.html hash e6cf29a748b0
   - V7 Pro 原版，V6 Canvas引擎，40+ canvas，已修復圖表異常
   - JS/CSS 永遠不動，保證 100% 相同

2. **數據層 he 物件隔離**
   - 數據都在 `he={date:"2026-10-24",spot:{close:46041.43,...}}` 這一個物件
   - 每日更新時，只替換 he 物件，其他繪圖程式碼完全不動

3. **新對話執行步驟**
   a. 上傳 skill
   b. 上傳 Golden Master
   c. 說：「更新今日盤前數據」
   d. 助手自動抓取 DATA_REPORT 並注入 he

4. **穩定性保證**
   - 複製模式: shutil.copyfile() → sha256 相同
   - 數據注入: 只改 he 欄位
   - 圖表引擎: 完全不動

範例指令：
- 「請安裝附件skill，更新今日2026-10-28盤前數據，版型保持跟附件V7 Pro一模一樣」

## Output Path Rule (V8 Pro 2026-10-27 updated)
**產出路徑統一為 dashboards/ 唯一**
- 禁止再寫入 dashboard/ 或 dashboard_v8/
- builder 僅寫入: dashboards/taifex-YYYYMMDD.html 和 /mnt/data/dashboards/taifex-YYYYMMDD.html
- Golden Master: templates/v8-pro-golden-master.html (207,656 bytes, hash 87d5f1928f6b, V8 PRO top fixed, c4 rgba safe)
- 執行: python v8_pro_builder.py --date YYYYMMDD --golden templates/v8-pro-golden-master.html
- 驗證: 僅檢查 dashboards/ 存在, V8 PRO 1 + V8 Pro 3, mock-hidden False, window.__P True
- 舊的 dashboard/ 和 dashboard_v8/ 資料夾應從 repo 刪除
