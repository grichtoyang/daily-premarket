---
name: daily-premarket-analysis-v9-pro
description: V9 Pro 17F + 機構級圖表 + 純 React 母版 + data.json 分離架構 + 6頁 dashboard。基於 V8 Pro 17F + VIX動態 + RSI/MACD + SQLite真DB + 41張全動態升級，圖表達到 Bloomberg / TradingView 機構級。Use when user asks for 盤前分析 v9, V9 Pro, 機構級圖表, 6頁 dashboard, 總覽 現貨 重要市場 期貨 選擇權 綜合分析。
---

# 台股每日盤前分析 Skill V9 Pro - 17F + 機構級圖表 + 純 React + data.json 分離 + 6頁

## 基於 V8 Pro 最新版 (2026-10-28) 升級點

### V8 Pro 基礎 (來自 daily-premarket-analysis-v8)
- 17因子：基礎15因子 + RSI 3% + MACD 3% = 17F
  - 現貨趨勢13%、外資現貨12%、外資期貨8%、投信5%、基差7%、夜盤8%、美股費半12%、PCR7%、GEX7%、PutWall3%、ADR溢價3%、殖利率5%、量能3%、均線乖離3%、VIX2% + RSI3% + MACD3%
- VIX動態：VIX>25恐慌 美股12%->20%，VIX<15平靜 美股7%台股20%，基差過大假多 7%->2%
- 方案C 3層備援：
  ```
  層1 Yahoo Finance ^TWII 1mo (主) → 30天高低收 → RSI14 + MACD + KD
  層2 FinMind TaiwanStockPrice 14天 (備援1)
  層3 SQLite DB 歷史累積 (備援2)
  全失敗 → weight 0%，15因子運算，不當機
  ```
- SQLite真DB：v9_pro_history + factor_performance，真勝率10天回測，歷史相似度找過去Bias相似盤勢
- 41張全動態 + 20模板輪替 + 權重回測
- Output Path Rule：dashboards/ 唯一，禁止 dashboard/ 或 dashboard_v8/

### V9 Pro 核心改進 (2026-10-29)

#### 1. 純 React 母版 + data.json 分離架構 (重大架構變更)
```
V8: Builder 讀 Golden Master.html → regex 替換 he 物件 → 寫出 dashboards/taifex-YYYYMMDD.html (數據混在HTML)

V9: templates/v9-pro-react-template.html 純淨母版，無範例數據
    ↓ 讀取
    window.DASHBOARD_DATA || null → 空狀態引導頁
    ↑
    scripts/v9_pro_builder.py 只產 data.json，不產HTML
    ↓ 解析 DATA_REPORT
    dashboards/data-YYYYMMDD.json 17F + 41張 + 28市場 + 12新聞 + 6頁
    ↓ 注入 (預覽用)
    dashboards/v9-pro-...html = 母版 + <script>window.DASHBOARD_DATA={...}</script>
```
- 母版：templates/v9-pro-react-template.html 31KB，暗色 #070e1c，React 18 UMD createElement，無外部依賴，無46096等範例數據
- Builder：scripts/v9_pro_builder.py 60KB，只寫 dashboards/data-YYYYMMDD.json，size 34KB，bias 55分 47張，CHECK OK: 17F + VIX Dynamic + RSI/MACD + SQLite真DB + 41張全動態 + data.json only + pure React template
- 預覽注入：artifact = 母版 + data.json，生產環境 = 母版 + fetch(data.json)

#### 2. 6頁 Dashboard 結構 (按 DATA_REPORT 四大類對位)
按 user 明確指示：dashboard 分成6個頁面，四大類分別貼入對應頁面

1. 總覽/總結：KPI 8宮格 + Bias 17因子 + 加權5日 + 關鍵水位 + 三大法人快照 + 期選結構 + 美股連動 + 新聞
2. 現貨：對位 DATA_REPORT 一、現貨 6區塊
   - 大盤行情 OHLC 47035.58 +2.04% 開46402 高47060 低46402 量7503億
   - 漲跌家數 上市714/280/87/32/2 上櫃590/202/80/31/0
   - 三大法人 外資+159.6 投信+143.2 自營+21.7 合計+324.4
   - 融資融券 8435.4億 +108.9億 維持率183.30%
   - 借券 4,590,969張 賣出39,926張 +2,559張
   - 成交結構 上市7503億 上櫃1633億 合計9136億
3. 重要市場：對位 二、重要市場 8區塊
   - 美股 S&P+0.28% Nasdaq+0.27% SOX+1.75% VIX-3.48%
   - 亞洲 日經+2.17% KOSPI+5.59% 恆生-0.73% 上證-1.33% 深圳-2.50%
   - 美期 ES+0.07% NQ-0.41% YM+0.48% RTY+1.07%
   - 美債 2Y 4.67% -0.03 10Y 5.05% +0.05 30Y 5.36% +0.06
   - 匯率 USD/TWD 32.40 -0.09% DXY -0.16%
   - ADR TSM+2.95% ASX+5.39%
   - 商品 WTI+2.02% 黃金-0.07% BTC-0.03%
   - 新聞12則
4. 期貨：對位 三、期貨 6區塊
   - 日盤 47244 +1138 +2.47% 量43867 基差+208.42 +0.44%
   - 夜盤 47121 -128 -0.27% 量31298 變化-123
   - 價差 基差+208.42 正價差0.44%
   - 法人OI 外資-84917 投信+87179 自營+483 前十大+5879
   - 日夜交易 外資日+1050夜-1089 投信日+2127 自營日-964夜+68
   - 夜盤劇本 量占比41.64% 劇本分類
5. 選擇權：對位 四、選擇權 7區塊
   - Vol OI PCR 1.09 Call Wall 47000 Put Wall 46700 Gamma Wall 47500 Flip 46571 MaxPain 46750
   - OI集中 Call 47200 2608口 Put 46700 4447口
   - Call分布 Top10 / Put分布 Top10 Mountain 山形圖
   - 5牆 Order Book Depth
   - 法人選擇權 外資日+8216夜-1201 投信-12786 自營+13641夜-1252
   - 前十大 Call淨-1132 Put淨-2052
6. 綜合分析：三市場法人主力大戶
   - 多空籌碼結構 期現選對照表 外資+159.6/期-84917/選+8216 判定避險/對沖
   - 多空買賣力道 法人力道表 日多11.44空10.31淨+1.13
   - 日夜盤劇本 收盤-123 成交量+12569 劇本分類
   - 三劇本/檢查表/相關性熱圖

#### 3. 每個數據區塊 圖表 + 分析→判斷→操作 (user 明確要求)
- 圖表：機構級 Canvas，非玩具
- 解析文字三段式：
  - 分析：數據圖表代表的含意，帶當日真實數字，例如「外資現貨+159.6億買超，投信+143.2億對作，合計+324.4億大買，法人一致偏多」
  - 判斷：市場多空趨勢走向的預判，例如「外資期空-84917仍高，但現貨大買翻多，Put Wall上移1700至46700為最後防線，偏多判斷」
  - 操作：如何進行交易的操作，例如「46700不破前震盪偏多，跌破追空至46200，反彈至47200減碼」

#### 4. 機構級圖表升級 (解決 醜 + 文字重疊)

**V8 Pro 風格保留：** 暗色 #070e1c 卡 #111f35 漸層 邊 #1e2e47，Canvas引擎 DPR + ResizeObserver + debounce

**防重疊全局規則：**
- measureText 預留4px，過長...，數值永遠在條外，三欄固定寬 左90/中彈性/右60，軸標籤間距>=40px自動稀釋，圖例與圖表分離，容器固定160-220px padding 16px

**新圖表類型 (Bloomberg / TradingView 級)：**
- KPI 8宮格：Micro Sparkline 60x22 Area，quadraticCurveTo 平滑 + Area漸層0.22→0 + 末點3px白邊glow，Y緊縮 min*0.995 max*1.005，顏色邏輯正確 漲綠#3dd68c 跌紅#ff6b6b，頂部2px accent線
- 漲跌家數：雙 Donut 並列 上市/上櫃，圓環12px厚圓角端，中心大字，綠紅灰，漸層+發光，引線標籤
- 三大法人：Lollipop 棒棒糖 2px漸層線+6px圓點白邊+glow，零線居中，數值外側4px
- 融資融券：半圓 Gauge 儀表 7000-9000刻度 + 指針 + Delta箭頭 + 維持率進度條
- 成交結構：Donut 中心總額 9136億，引線標籤 7503億85% / 1633億15%
- 重要市場：Sparkline Table Bloomberg風格 每行 名稱 | 30px bezier微線 | pill漲跌箭頭 | 收盤 | 背景tint按強度 綠/紅微著色
- 期貨日夜：Mini Candlestick Pro 12px實體漸層 + 1.2px影線白邊 + O/H/L/C膠囊 + 量小柱 + 基差標籤
- 法人OI/前十大：Butterfly Diverging Dot 零線居中，外資-84917紅大點 投信+87179綠大點 前十大+5879藍中點，點大小按口數，虛線對作
- 選擇權OI分布：Mountain 山形圖 OI連成山峰填充漸層，現價47035亮線，Call Wall 47000 / Put Wall 46700 旗標+虛線
- 5牆水位：Order Book Depth 垂直深度圖，綠買紅賣shading，R/S/P/W/F虛線，現價脈動箭頭
- Bias：半圓Gauge 260px高，軌道#1e2e47 18px 圓角，活躍弧到55分 漸層綠橘紅按分數，刻度0/25/50/75/100，指針白2px+10px白環圓心+shadow，中心大字42px 55/100，下方黃字震盪 46700防線，三Pill Flip 46571藍 / GEX紅 / MaxPain 46750綠，2欄迷你Lollipop前8大因子，可展開17F (仿附圖 V8 Pro Gauge)
- 相關性熱圖：5x5圓角格 40px間距4px 深色白字淺色黑字自適應，右側legend漸層條

**附圖參考：**
- Bias附圖：34/100半圓Gauge，軌道深色，活躍弧綠#3dd68c→#a8d86e 粗18px圓角，指針白，中心34/100，黃字震盪偏空 46K防線，三Pill Flip/GEX/MaxPain，分析判斷操作三段

#### 5. Builder 規格
- 路徑: scripts/v9_pro_builder.py (60,029 bytes, hash 參考 v8)
- 執行: python scripts/v9_pro_builder.py --data_report DATA_REPORT_20261028.md --out dashboards/data-YYYYMMDD.json --date YYYYMMDD
- 產出: dashboards/data-YYYYMMDD.json (34KB, 17F + 41張 + 28市場 + 12新聞 + 6頁) + dashboards/v9_pro_history.db
- 特性：Yahoo 3層備援 + SQLite真DB + 歷史相似度 + 無DB回退 + 純data.json only
- Data Source: DATA_REPORT (twse-proxy + TAIFEX Proxy + Yahoo Chart API + FinMind)
- 解析: spot/institutional/margin/sbl/turnover/markets(7)/tx/futures/options(15)/news/analysis(bias/regime/factors/weights/look/compass/target/cards/levels/correlation/historical/db_status)

#### 6. Template 規格
- 路徑: templates/v9-pro-react-template.html (31,312 bytes)
- 技術: React 18 UMD createElement，useCanvas hook + ResizeObserver + DPR，無外部依賴，window.DASHBOARD_DATA純淨判斷 null空狀態引導
- 樣式: 暗色 #070e1c 卡 #111f35 #0f1c2e 邊 #1e2e47 #223247 文字 #d6e2f0 muted #8ea7c3 dim #5a718a accent #6bb6ff 綠 #3dd68c 紅 #ff6b6b 黃 #ffd93d 橙 #ff9f43
- 6頁 Tab，KPI 8宮格，41張全覽搜尋，Canvas 40+，debounce 150ms，ResizeObserver
- 版型鎖死，數據只改 window.DASHBOARD_DATA

#### 7. Output Path Rule
- 產出統一 dashboards/ 唯一，禁止 dashboard/ 或 dashboard_v8/
- Template: templates/v9-pro-react-template.html
- Builder僅寫 dashboards/data-YYYYMMDD.json
- DB: dashboards/v9_pro_history.db (真回測，10天有勝率)
- Artifact預覽: dashboards/v9-pro-YYYYMMDD.html = 母版 + <script>window.DASHBOARD_DATA={...}</script>

#### 8. 每日流程 (V9 Pro)
1. 抓 DATA_REPORT_YYYYMMDD.md
2. Yahoo ^TWII 30天算RSI/MACD (3層備援)
3. 17因子算Bias 0-100 + VIX動態 + 恐慌加成 + 權重優化 (DB真勝率)
4. Regime + 相關性SOX+TSM ADR + 歷史相似度 (若DB>=3天)
5. 解析四大類對位：現貨6區塊 / 重要市場8區塊 / 期貨6區塊 / 選擇權7區塊 / 綜合分析6區塊
6. 機構級圖表：Donut/Lollipop/Gauge/SparklineTable/Candlestick/Butterfly/Mountain/Depth/Ladder/Heatmap/Gauge
7. 41張全動態注入 分析→判斷→操作 帶當日數據
8. 存DB + 更新昨日next_day_pct
9. 產出 dashboards/data-YYYYMMDD.json

#### 9. 今日實測 20261028
- DATA_REPORT_20261028 T0 2026-10-28 報告2026-10-29 09:30
- 加權47035.58 +939.35 +2.04% 開46402 高47060 低46402 量7503億 漲714跌280
- 外資+159.6 投信+143.2 自營+21.7 合計+324.4 融資8435.4 +108.9 維持率183.30%
- 日盤47244 +1138 +2.47% 基差+208.42 夜盤47121 -128 -0.27%
- 外資期-84917 投信+87179 PCR1.09 CallWall47000 PutWall46700 Gamma47500 Flip46571 MaxPain46750
- Bias 55分 震盪 (昨天44分 高檔偏空) 因子外資翻多+費半+1.75%+PCR回中性
- 產出 dashboards/data-20261028.json 34248 bytes bias55 cards47 db_mode no-db-partial
- Dashboard: [V9 Pro 今日實測 20261028](dashboards/v9-pro-20261028.html)

## 使用
- 安裝: 將此md放入 .claude/skills/ 或 skills/
- 觸發: 盤前分析, 每日盤前, V9 Pro, 機構級圖表, 6頁 dashboard
- 執行: python scripts/v9_pro_builder.py --data_report DATA_REPORT_*.md --out dashboards/data-YYYYMMDD.json
- 預覽: 將 data-YYYYMMDD.json 注入 templates/v9-pro-react-template.html
- 依賴: Python 3.9+, requests, sqlite3, React 18 UMD

## 附錄：V8 Pro 附圖 Gauge 規格
- 標題 Bias 盤前偏向 34/100 右上角V8 Pro pill 副標題 震盪偏空 · 46K防線失守風險 · Short Gamma加速
- 中間大半圓 Gauge 0-100 軌道#1e2e47 厚18px 圓角端 活躍弧到34 綠漸層 粗18px 指針白2px+白環10px 中心34/100 黃字震盪偏空 46K防線
- 下方三pill Flip 45920.93藍 GEX -2.3B紅 MaxPain 46K綠
- 下方分析判斷操作三段帶icon 🔍 🧭 🎯
