# DATA_REPORT_20261103

- 報告日期：`2026-11-04`
- T0 交易日期：`2026-11-03`
- 資料產出時間：`2026-11-04 11:52:12`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`morning`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 43,307.54 | 點 | twse-proxy |
| 開盤 | 44,481.59 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 44,614.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 43,191.58 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 43,307.54 | 點 | twse-proxy |
| 漲跌點數 | -1,612.60 | 點 | twse-proxy |
| 漲跌幅 | -3.59 | % | twse-proxy |
| 成交金額 | 10,020.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 58 | twse-proxy |
| 下跌家數 | 1,000 | twse-proxy |
| 平盤家數 | 22 | twse-proxy |
| 漲停家數 | 2 | twse-proxy |
| 跌停家數 | 33 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 59 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 782 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 32 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 11 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 41 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,073.1 | 億元 | twse-proxy /institutional |
| 投信 | +184.6 | 億元 | twse-proxy /institutional |
| 自營商 | -590.5 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,479.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,963.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -307.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 296,332 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 64,698 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 162.70 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,755,941 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 38,371 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 1,667 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,020.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,975.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,995.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,568.92 | 27.52 | +0.36 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,372.01 | 207.70 | +0.83 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,180.26 | 190.44 | +0.68 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,786.72 | -197.26 | -0.38 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,600.40 | 272.07 | +2.63 | Yahoo Finance Chart API |
| VIX | ^VIX | 20.83 | -0.32 | -1.51 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 60,423.07 | -2,658.79 | -4.21 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,455.21 | -193.58 | -3.43 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,498.77 | -27.20 | -0.12 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,604.37 | -3.73 | -0.10 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,891.91 | 14.92 | +0.14 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,503.50 | -93.25 | -1.23 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,706.25 | -599.50 | -2.12 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,465.00 | -430.00 | -0.83 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,800.60 | -24.40 | -0.86 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.61 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.95 | 0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.32 | 0.06 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.87 | 0.28 | +0.87 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.31 | -0.56 | -0.55 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.64 | -0.27 | -0.17 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,337.58 | -7.23 | -0.54 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 404.80 | 6.17 | +1.55 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.40 | 0.01 | +0.06 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.05 | -0.12 | -0.31 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 95.71 | -0.38 | -0.40 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,948.50 | 8.10 | +0.21 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,300.01 | -377.29 | -0.49 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：昨87萬散戶進場 斷頭追繳令已發「剛開始鬆動」
  - 來源：Yahoo 台股；發布時間：2026-11-04T03:19:58Z；台北時間：2026-11-04 11:19
  - 摘要：台股跌破4萬3千點可抄底了嗎？據台灣證交所資料顯示，昨（3日）有交易人數高達219.5萬人，較前一天增加了87萬人之多。散戶大舉進場扮「義勇軍」，台股今早仍陷上下震盪整理。對此兆豐投顧副總黃國偉今（4）接受《Yahoo股市》採訪時表示，「還
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E8%B7%8C%E7%A0%B44%E8%90%AC3%E5%8F%AF%E6%8A%84%E5%BA%95%EF%BC%9F87%E8%90%AC%E6%95%A3%E6%88%B6%E5%B7%B2%E9%80%B2%E5%A0%B4-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E6%AE%BA%E8%9E%8D%E8%B3%87%E4%B8%8D%E5%8F%AF%E8%83%BD%E4%B8%80%E5%A4%A9-031958301.html
- 事件3：川湖跌停「幾乎崩回起漲點」空手、攤平策略曝光
  - 來源：Yahoo 台股；發布時間：2026-11-04T03:27:23Z；台北時間：2026-11-04 11:27
  - 摘要：「銅破線 川湖崩 AI沒救了」「川湖8650 朝腰斬邁進」「川湖高點跌了6000元 幾乎崩回起漲點」「川湖不是還吹什麼機櫃宇宙無敵」。
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E8%82%A1%E5%90%8E%E5%B7%9D%E6%B9%96%E8%B7%8C%E5%81%9C%EF%BC%81%E4%B8%80%E5%BC%B5%E8%92%B8%E7%99%BC92%E8%90%AC%E5%85%83-%E7%B6%B2%E6%AD%8E%E3%80%8C%E6%9C%9D%E8%85%B0%E6%96%AC%E9%82%81%E9%80%B2%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E7%A4%BA%E8%AD%A6%EF%BC%9A%E5%88%A5%E6%80%A5%E6%8A%84%E5%BA%95-032723467.html
- 事件4：光電股綠油油⋯玉晶光面臨連五跌
  - 來源：Yahoo 台股；發布時間：2026-11-04T03:15:00Z；台北時間：2026-11-04 11:15
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導台股加權指數今（4）日開高走低，開盤一度衝高至43700點，盤中多空激戰後指數突然一瀉千里，截至上午11點左右報42546.89點...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%89%E9%9B%BB%E8%82%A1%E6%85%98%E9%99%B7%E7%B6%A0%E6%B5%B7-%E9%80%99%E5%85%89%E5%AD%B8%E5%BB%A0-%E9%80%A3%E5%90%9E4%E9%BB%91%E5%86%8D%E8%B7%8C%E5%8D%8A%E6%A0%B9-%E5%86%A0%E8%A5%BF%E9%9B%BB%E6%8C%AB%E9%80%BE7-%E9%9D%A2%E6%9D%BF%E4%B8%89%E9%9B%84%E5%85%A8%E6%94%B6%E9%BB%91-031500603.html
- 事件5：台達電股價腰斬 投顧解析：年底前恐難回2字頭
  - 來源：Yahoo 台股；發布時間：2026-11-03T21:06:30Z；台北時間：2026-11-04 05:06
  - 摘要：電源供應器一哥台達電(2308)跌不停，昨（3）日再跌逾6%收1270元，等於從今年高點2585元迄今回檔約50.9%。至於股價腰斬過後，賣壓何時宣洩完畢，官股金控龍頭旗下投顧分析，鑒於HVDC仍待時間發酵，雖給予「逢低買進」建議，但預期未
  - 原文連結：https://tw.stock.yahoo.com/news/2585%E5%85%83-1270%E5%85%83-%E5%8F%B0%E9%81%94%E9%9B%BB%E8%82%A1%E5%83%B9%E8%85%B0%E6%96%AC%E8%B7%8C%E5%A4%A0%E6%B2%92-%E5%AE%98%E8%82%A1%E9%BE%8D%E9%A0%AD%E6%8C%87%E5%BC%95%E4%BE%86%E4%BA%86-%E7%9B%AE%E6%A8%99%E5%83%B9-210630123.html
- 事件6：日股開市補跌逾2000點 全球NAND二哥跳水13%
  - 來源：Yahoo 台股；發布時間：2026-11-04T02:18:41Z；台北時間：2026-11-04 10:18
  - 摘要：日股昨（3）日休市，逃過亞股大逃殺，但今（4）早開市後難逃補跌命運，日經225指一度狂洩逾2000點、跌幅破3.2%，其中記憶體大廠、全球第二大NAND廠鎧俠重挫13%，連帶在台灣掛牌日股ETF共計11檔也跟進補跌，只有反向及房地產類沒跌，
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%96%8B%E5%B8%82%E8%A3%9C%E8%B7%8C%EF%BC%81%E6%97%A5%E8%82%A1%E7%8B%82%E7%80%892000%E9%BB%9E-%E9%8E%A7%E4%BF%A0%E8%B7%8C13-%E6%97%A5%E8%82%A1etf%E6%9C%80%E9%87%8D%E8%B7%8C6-032522307.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Job openings posted big September gain in positive sign for labor market ahead of payrolls report
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 19:15:21 GMT；台北時間：2026-11-04 03:15
  - 摘要：The BLS reported job openings at 7.52 million, up 333,000 from August and well above the Dow Jones consensus outlook for 7.15 million
  - 原文連結：https://www.cnbc.com/2026/11/03/job-openings-posted-big-september-gain-in-positive-sign-for-labor-market-ahead-of-payrolls-report.html
- 事件10：Midterm elections could jolt stocks as Democrats look poised to sweep Congress
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 03:38:08 GMT；台北時間：2026-11-04 11:38
  - 摘要：Wall Street weighs how the 2026 midterms could affect stocks, Treasury yields, artificial intelligence, energy prices, banks, defense and healthcare.
  - 原文連結：https://www.cnbc.com/2026/11/03/midterm-election-stock-market.html
- 事件11：Stock market after midterm elections: What S&P 500 history shows
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 18:21:05 GMT；台北時間：2026-11-04 02:21
  - 摘要：Midterms historically precede a strong year for the S&P 500. What to know if Democrats win back Congress
  - 原文連結：https://www.cnbc.com/2026/11/02/stock-market-after-midterm-elections-sp-500-history.html
- 事件12：Jim Cramer sees signs of life in tech stocks — but not from the usual winners
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 23:58:09 GMT；台北時間：2026-11-04 07:58
  - 摘要：Cramer said a new group of technology stocks may be emerging as market leaders.
  - 原文連結：https://www.cnbc.com/2026/11/03/jim-cramer-sees-signs-of-life-in-tech-stocks-but-not-from-the-usual-winners.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-03

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 44,400 | TAIFEX Proxy |
| 最高價 | 44,686 | TAIFEX Proxy |
| 最低價 | 43,324 | TAIFEX Proxy |
| 收盤價 | 43,376 | TAIFEX Proxy |
| 漲跌點數 | -1,851 | TAIFEX Proxy |
| 漲跌幅 | -4.09 | TAIFEX Proxy |
| 成交量 | 78,044 | TAIFEX Proxy |
| 日盤高點及低點 | 44,686 / 43,324 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,340 | TAIFEX Proxy |
| 最高價 | 44,069 | TAIFEX Proxy |
| 最低價 | 42,925 | TAIFEX Proxy |
| 收盤價 | 43,779 | TAIFEX Proxy |
| 漲跌點數 | +426 | TAIFEX Proxy |
| 漲跌幅 | +0.98 | TAIFEX Proxy |
| 成交量 | 40,804 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,069 / 42,925 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,506 | TAIFEX Proxy |
| 外資空方 OI | 102,318 | TAIFEX Proxy |
| 外資多空淨 OI | -91,812 | TAIFEX Proxy |
| 投信多方 OI | 89,985 | TAIFEX Proxy |
| 投信空方 OI | 2,987 | TAIFEX Proxy |
| 投信多空淨 OI | +86,998 | TAIFEX Proxy |
| 自營商多方 OI | 7,540 | TAIFEX Proxy |
| 自營商空方 OI | 3,564 | TAIFEX Proxy |
| 自營商多空淨 OI | +3,976 | TAIFEX Proxy |
| 三大法人合計多方 OI | 108,031 | TAIFEX Proxy |
| 三大法人合計空方 OI | 108,869 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -838 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,433 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -2,141 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +2,669 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,444 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,876 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,568 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-30→2026-11-03) | -54 | TAIFEX Proxy snapshots (2026-11-02) |
- 資料日期：2026-11-03 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 68,904 | TAIFEX Proxy |
| 外資日盤空單交易量 | 71,286 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,382 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 25,113 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 23,835 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,278 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,660 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -2,141 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -2,141 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +2,625 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +57 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +2,568 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,898 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,335 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -169.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +116.9 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,376 | TAIFEX Proxy |
| 加權指數價格 | 43,307.54 | twse-proxy |
| 台指期與加權指數價差 | +68.46 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.16 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +68.46 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +403 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,376 | 43,779 | -403 | TAIFEX Proxy |
| 成交量 | 78,044 | 40,804 | +37,240 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,905（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 68,904 | 71,286 | -2,382 | 25,113 | 23,835 | +1,278 | -3,660 | 10,506 | 102,318 | -91,812 | -2,433 | TAIFEX Proxy |
| 投信 | 82 | 2,223 | -2,141 | 0 | 0 | +0 | -2,141 | 89,985 | 2,987 | +86,998 | -2,141 | TAIFEX Proxy |
| 自營商 | 9,523 | 6,898 | +2,625 | 804 | 747 | +57 | +2,568 | 7,540 | 3,564 | +3,976 | +2,669 | TAIFEX Proxy |
| 三大法人合計 | 78,509 | 80,407 | -1,898 | 25,917 | 24,582 | +1,335 | -3,233 | 108,031 | 108,869 | -838 | -1,905 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,444 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,876 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,568 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-30→2026-11-03) | -54 | TAIFEX Proxy snapshots (2026-11-02) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 34.33% | TAIFEX Proxy |
| 夜盤漲跌點數 | +426 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,278 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-03 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-04 11:52:12 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 244,760 | TAIFEX Proxy |
| Call 總未平倉量 OI | 96,494 | TAIFEX Proxy |
| Call OI 增減 (2026-11-02→2026-11-03) | +34,916 | TAIFEX Proxy snapshots (2026-11-02) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 199,896 | TAIFEX Proxy |
| Put 總未平倉量 OI | 40,135 | TAIFEX Proxy |
| Put OI 增減 (2026-11-02→2026-11-03) | +5,248 | TAIFEX Proxy snapshots (2026-11-02) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.22 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.40 | TAIFEX Proxy |
| Put／Call Ratio | 0.42 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-02→2026-11-03) | -13.76 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-02→2026-11-03) | -13.81 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 70,065 | TAIFEX Proxy |
| 外資 Call日賣 | 68,676 | TAIFEX Proxy |
| 外資 Call日淨 | +1,389 | TAIFEX Proxy |
| 外資 Put日買 | 71,194 | TAIFEX Proxy |
| 外資 Put日賣 | 70,146 | TAIFEX Proxy |
| 外資 Put日淨 | +1,048 | TAIFEX Proxy |
| 外資 Call夜買 | 41,041 | TAIFEX Proxy |
| 外資 Call夜賣 | 40,726 | TAIFEX Proxy |
| 外資 Call夜淨 | +315 | TAIFEX Proxy |
| 外資 Put夜買 | 39,417 | TAIFEX Proxy |
| 外資 Put夜賣 | 39,990 | TAIFEX Proxy |
| 外資 Put夜淨 | -573 | TAIFEX Proxy |
| 外資 日盤淨總量 | +341 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,074 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,621 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 67,095 | TAIFEX Proxy |
| 自營商 Call日賣 | 74,800 | TAIFEX Proxy |
| 自營商 Call日淨 | -7,705 | TAIFEX Proxy |
| 自營商 Put日買 | 60,242 | TAIFEX Proxy |
| 自營商 Put日賣 | 56,499 | TAIFEX Proxy |
| 自營商 Put日淨 | +3,743 | TAIFEX Proxy |
| 自營商 Call夜買 | 20,047 | TAIFEX Proxy |
| 自營商 Call夜賣 | 22,430 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,383 | TAIFEX Proxy |
| 自營商 Put夜買 | 20,192 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,485 | TAIFEX Proxy |
| 自營商 Put夜淨 | -293 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,448 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -5,322 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +4,036 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 5,606 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,000 | 5,028 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,400 | 4,378 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 5,606 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 5,606 | 5.81% | TAIFEX Proxy |
| C2 | 48,000 | 5,028 | 5.21% | TAIFEX Proxy |
| C3 | 49,400 | 4,378 | 4.54% | TAIFEX Proxy |
| C4 | 45,000 | 3,378 | 3.5% | TAIFEX Proxy |
| C5 | 44,500 | 3,189 | 3.3% | TAIFEX Proxy |
| C6 | 46,200 | 2,910 | 3.02% | TAIFEX Proxy |
| C7 | 44,000 | 2,823 | 2.93% | TAIFEX Proxy |
| C8 | 44,200 | 2,336 | 2.42% | TAIFEX Proxy |
| C9 | 44,300 | 2,329 | 2.41% | TAIFEX Proxy |
| C10 | 45,500 | 2,179 | 2.26% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 43,000 | 2,322 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,600 | 1,832 | TAIFEX Proxy |
| Put OI 第3大履約價 | 42,500 | 1,775 | TAIFEX Proxy |
| Put OI 最大履約價 | 43,000 | 2,322 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 43,000 | 2,322 | 5.79% | TAIFEX Proxy |
| P2 | 40,600 | 1,832 | 4.56% | TAIFEX Proxy |
| P3 | 42,500 | 1,775 | 4.42% | TAIFEX Proxy |
| P4 | 44,000 | 1,688 | 4.21% | TAIFEX Proxy |
| P5 | 42,000 | 1,594 | 3.97% | TAIFEX Proxy |
| P6 | 41,400 | 1,404 | 3.5% | TAIFEX Proxy |
| P7 | 43,500 | 1,097 | 2.73% | TAIFEX Proxy |
| P8 | 42,300 | 968 | 2.41% | TAIFEX Proxy |
| P9 | 40,400 | 965 | 2.4% | TAIFEX Proxy |
| P10 | 45,000 | 898 | 2.24% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 46,000 (+3,534) | TAIFEX Proxy snapshots (2026-11-02) |
| Call OI 減少最多的履約價 | 51,000 (-1,638) | TAIFEX Proxy snapshots (2026-11-02) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 40,400 (+965) | TAIFEX Proxy snapshots (2026-11-02) |
| Put OI 減少最多的履約價 | 44,000 (-973) | TAIFEX Proxy snapshots (2026-11-02) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-02→2026-11-03) | -2,000 | TAIFEX Proxy snapshots (2026-11-02) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-02→2026-11-03) | -1,000 | TAIFEX Proxy snapshots (2026-11-02) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,900.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-03 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 43,006.60 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-03 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-02→2026-11-03) | -400 | TAIFEX Proxy snapshots (2026-11-02) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 140,211 | 139,870 | +341 | 81,031 | 80,143 | +888 | -547 | TAIFEX Proxy |
| 投信 | 200 | 5,246 | -5,046 | 0 | 0 | +0 | -5,046 | TAIFEX Proxy |
| 自營商 | 123,594 | 135,042 | -11,448 | 40,532 | 42,622 | -2,090 | -9,358 | TAIFEX Proxy |
| 三大法人合計 | 264,005 | 280,158 | -16,153 | 121,563 | 122,765 | -1,202 | -14,951 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 14.35 | 14.07 | +0.28 | 7.00 | 6.93 | +0.07 | +0.21 | TAIFEX Proxy |
| 投信 | 0.02 | 1.37 | -1.35 | 0.00 | 0.00 | +0 | -1.35 | TAIFEX Proxy |
| 自營商 | 12.87 | 13.70 | -0.83 | 5.38 | 4.84 | +0.54 | -1.37 | TAIFEX Proxy |
| 三大法人合計 | 27.23 | 29.13 | -1.90 | 12.38 | 11.77 | +0.61 | -2.51 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 10,686 | TAIFEX Proxy |
| 買權空方 OI | 13,733 | TAIFEX Proxy |
| 買權多空淨 OI | -3,047 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-30→2026-11-03) | -891 | TAIFEX Proxy snapshots (2026-11-02) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,889 | TAIFEX Proxy |
| 賣權空方 OI | 10,181 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,292 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-30→2026-11-03) | +38 | TAIFEX Proxy snapshots (2026-11-02) |
- 資料日期：買權 2026-11-03／賣權 2026-11-03 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -54 | 2026-10-30→2026-11-03 | TAIFEX Proxy snapshots (2026-11-02) |
| 買權前十大 | -891 | 2026-10-30→2026-11-03 | TAIFEX Proxy snapshots (2026-11-02) |
| 賣權前十大 | +38 | 2026-10-30→2026-11-03 | TAIFEX Proxy snapshots (2026-11-02) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-03；資料時間：2026-11-04 11:52:12；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：futures.gamma_wall, futures.gamma_flip
- 註記：futures-price-after-hours 日期 2026-11-03 非今日 2026-11-04，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`stockintelli 大盤融資維持率 (民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,073.1 | -91,812 | -2,382 | +1,278 | +341 | +888 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +184.6 | +86,998 | -2,141 | +0 | -5,046 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -590.5 | +3,976 | +2,625 | +57 | -11,448 | -2,090 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
