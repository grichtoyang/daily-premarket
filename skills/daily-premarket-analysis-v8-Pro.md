---
name: daily-premarket-analysis-v8
description: Produce structured 台股 V8 Pro (templates/v8-pro-golden-master.html) 台股 daily pre-market analysis with 17-Factor + VIX Dynamic + RSI/MACD + SQLite + 41 cards full dynamic. Use when user asks for 盤前分析, 每日盤前, 台指盤前, pre-market report, dashboard.
---

# 台股每日盤前分析 Skill V8 Pro - 17因子 + VIX動態 + RSI/MACD + SQLite真DB + 41張全動態

## V8 Pro 核心改進 (2026-10-28)

### 17因子 + VIX動態權重
- 基礎15因子：現貨趨勢13%、外資現貨12%、外資期貨8%、投信5%、基差7%、夜盤8%、美股費半12%、PCR7%、GEX7%、PutWall3%、ADR溢價3%、殖利率5%、量能3%、均線乖離3%、VIX因子2%
- 新增RSI 3% + MACD 3% = 17因子
- VIX動態：VIX>25恐慌 美股權重12%->20%，VIX<15平靜 美股7%台股20%
- 基差過大假多權重7%->2%

### 方案C：Yahoo ^TWII 30天算RSI/MACD + 3層備援
```
層1 Yahoo Finance ^TWII 1mo (主) → 30天高低收 → RSI 14 + MACD + KD
層2 FinMind TaiwanStockPrice 14天 (備援1)
層3 SQLite DB 歷史累積 (備援2)
全失敗 → weight 0%，15因子運算，不當機
```

### SQLite真DB + 歷史相似度 + 無DB回退
```sql
v8_pro_history: date, bias, spot_close, foreign_spot, pcr, gex, vix, rsi, macd, k, d, next_day_pct
factor_performance: factor, wins, total, win_rate
```
- 每天存今日bias + 技術指標
- 第二天回填隔日漲跌 next_day_pct
- 10天後算真勝率：外資勝率80% → 權重12%->15%
- 歷史相似度：找過去bias相似盤勢，算隔日平均-320點勝率70%，真數據非憶測
- DB失敗回退：DB不存在/損毀/不足<5天 → 無DB模式(no-db-*)，41張照樣動態

### 41張全動態 (40 unique + 1重複)
- Bias/KPI/盤前判斷/三劇本/檢查表/必核/AI5面向/AI結論/交易計畫 (9張)
- 現貨/法人/資金流向 (3張)
- 期貨日夜/籌碼深度/外資期貨/前十大/OI結構 (8張)
- 選擇權牆/PCR/GEX/IV Skew/Term/CallPutWall/Gamma (10張)
- 國際美股/亞洲/美期/美債/匯率/商品/VIX&DXY/相關性熱圖 (8張)
- 行事曆/重大新聞 (2張) + 1重複
- 每張 分析→判斷→操作 動態帶當日數據

### 20模板輪替 + 權重回測
- 20句型輪替，day_hash%20避免重複
- 權重依近10日勝率自動優化

## Golden Master
- 路徑: templates/v8-pro-golden-master.html (216,640 bytes, hash b332dca9f3fe)
- 28市場 + 12新聞，V8 Canvas引擎，40+ canvas，DPR，debounce 300ms
- 版型鎖死，數據只改 he 物件

## Builder
- 路徑: v8_pro_builder.py (69,382 bytes, hash e54f8d0fcd8b)
- 執行: python v8_pro_builder.py --date YYYYMMDD --golden templates/v8-pro-golden-master.html --data_report DATA_REPORT.md
- 產出: dashboards/taifex-YYYYMMDD.html (41張) + dashboards/v8_pro_history.db
- 特性：Yahoo RSI/MACD 3層備援 + SQLite真DB + 歷史相似度 + 無DB回退，失敗不影響解析

## Output Path Rule
- 產出統一 dashboards/ 唯一
- 禁止 dashboard/ 或 dashboard_v8/
- Golden: templates/v8-pro-golden-master.html
- Builder僅寫 dashboards/taifex-YYYYMMDD.html
- DB: dashboards/v8_pro_history.db (真回測，10天有勝率)

## Data Source
- DATA_REPORT: https://grichtoyang.github.io/daily-premarket/data_reports/
- Yahoo Finance ^TWII 1mo (RSI/MACD) + 美股6市場
- FinMind TaiwanStockPrice (備援)
- TWSE OpenAPI MI_INDEX
- Cloudflare Workers twse-proxy + taifex.grichtoyang.workers.dev

## 每日流程
1. 抓 DATA_REPORT
2. Yahoo ^TWII 30天算RSI/MACD (3層備援)
3. 17因子算Bias 0-100 + VIX動態 + 恐慌加成
4. Regime空頭/多頭/盤整 + 相關性SOX+TSM ADR
5. 歷史相似度 (若DB>=3天)
6. 41張全動態注入
7. 存DB + 更新昨日next_day_pct
8. 產出 dashboards/taifex-YYYYMMDD.html
