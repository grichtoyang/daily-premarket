# DATA_REPORT_20261007

- 報告日期：`2026-10-08`
- T0 交易日期：`2026-10-07`
- 資料產出時間：`2026-10-08 08:08:10`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,806.37 | 點 | twse-proxy |
| 開盤 | 49,857.32 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,966.89 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 49,567.52 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,806.37 | 點 | twse-proxy |
| 漲跌點數 | -16.18 | 點 | twse-proxy |
| 漲跌幅 | -0.03 | % | twse-proxy |
| 成交金額 | 9,862.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 588 | twse-proxy |
| 下跌家數 | 387 | twse-proxy |
| 平盤家數 | 99 | twse-proxy |
| 漲停家數 | 12 | twse-proxy |
| 跌停家數 | 4 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 419 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 357 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 97 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 23 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 3 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -130.4 | 億元 | twse-proxy /institutional |
| 投信 | -33.2 | 億元 | twse-proxy /institutional |
| 自營商 | -78.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -241.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,689.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +51.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 255,514 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 4,769 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 200.72 | % | 前值遞補 (DATA 2026-10-06；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,520,472 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 40,410 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 4,194 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,862.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,991.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,854.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,801.77 | -17.16 | -0.22 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,538.69 | -61.10 | -0.22 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 31,160.08 | -64.39 | -0.21 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,179.87 | -341.41 | -0.66 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 13,066.15 | -151.67 | -1.15 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.08 | 0.07 | +0.47 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 70,683.98 | 737.12 | +1.05 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,941.39 | -62.35 | -0.89 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,280.56 | 240.22 | +1.00 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,853.25 | -20.75 | -0.26 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 31,432.75 | -50.50 | -0.16 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,439.00 | -377.00 | -0.73 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,810.20 | -38.00 | -1.33 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.77 | -0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.28 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.66 | 0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.85 | 0.07 | +0.22 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.25 | 0.42 | +0.41 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.91 | -0.38 | -0.24 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,337.97 | -1.77 | -0.13 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 482.30 | -3.50 | -0.72 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 23.19 | -0.73 | -3.05 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 46.78 | -0.75 | -1.58 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 88.95 | -0.49 | -0.55 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,134.40 | -52.70 | -1.26 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,222.90 | -2,334.66 | -2.73 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：212億賣壓壓境台股卡關5萬 光聖台塑四寶火力全開
  - 來源：Yahoo 台股；發布時間：2026-10-07T09:09:00Z；台北時間：2026-10-07 17:09
  - 摘要：5萬關前遇賣壓，台股小跌16點！今(7)日加權指數終場下跌16.18點、跌幅0.03%，收49,806.37點，成交金額9277.67億元；盤中最高衝上49,966.89點，距5萬點僅約33點，隨後高檔獲利了結與連假前調節賣壓出籠，指數震盪
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B3%95%E4%BA%BA%E9%BD%8A%E7%A0%8D212%E5%84%84%E5%8F%B0%E8%82%A1%E6%94%BB5%E8%90%AC%E5%B7%AE34%E9%BB%9E%EF%BC%81%E5%85%89%E8%81%96%E4%BA%AE%E7%87%88%E9%A0%98%E8%BB%8D%E5%85%89%E9%80%9A%E8%A8%8A%E3%80%81%E5%8F%B0%E5%A1%91%E5%9B%9B%E5%AF%B6%E7%88%86%E9%87%8F%E6%89%9B%E5%A4%A7%E6%97%97%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090900709.html
- 事件2：美光工會宣布正式取得罷工權 勞動部首度回應
  - 來源：Yahoo 台股；發布時間：2026-10-07T08:33:01Z；台北時間：2026-10-07 16:33
  - 摘要：台灣美光勞資爭議持續延燒，桃園美光晶圓工會今（7）日宣布罷工投票結果，在2,012名投票會員中，共有1,994票同意罷工，工會宣布正式取得罷工權。對此，勞動部今日最新回應表示，尊重工會投票結果，並認為結果反映員工對合理分潤制度的期盼，呼籲公
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E5%85%89%E5%B7%A5%E6%9C%83%E5%8F%96%E5%BE%97%E7%BD%B7%E5%B7%A5%E6%AC%8A%EF%BC%81%E8%BF%912%E5%8D%83%E7%A5%A8%E5%90%8C%E6%84%8F-%E5%8B%9E%E5%8B%95%E9%83%A8%E9%A6%96%E5%BA%A6%E5%9B%9E%E6%87%89%EF%BC%9A%E6%8F%90%E5%87%BA%E5%85%B7%E9%AB%94%E6%96%B9%E6%A1%88%E5%8D%94%E5%95%86-083301061.html
- 事件3：報導引述法人看好獲利暴增1.33倍 聯電重訊澄清
  - 來源：Yahoo 台股；發布時間：2026-10-07T07:49:00Z；台北時間：2026-10-07 15:49
  - 摘要：法人喊聯電獲利暴增1.33倍 公司重訊：屬臆測性報導
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B3%95%E4%BA%BA%E5%96%8A%E8%81%AF%E9%9B%BB%E7%8D%B2%E5%88%A9%E6%9A%B4%E5%A2%9E1-33%E5%80%8D-%E5%85%AC%E5%8F%B8%E9%87%8D%E8%A8%8A-%E5%B1%AC%E8%87%86%E6%B8%AC%E6%80%A7%E5%A0%B1%E5%B0%8E-074900306.html
- 事件4：記憶體雙雄還能衝多高 法人力挺加碼目標價雙雙曝光
  - 來源：Yahoo 台股；發布時間：2026-10-07T07:48:37Z；台北時間：2026-10-07 15:48
  - 摘要：記憶體大廠南亞科與華邦電公布9月營收，雙雙繳出年月雙增佳績，反映產業強勁拉貨動能。法人指出，受惠記憶體報價強勁漲勢，南亞科與華邦電後市獲利爆發力十足，南亞科目標價更上看720元，華邦電則上看200元，雙雄明後兩年營運前景備受市場高度肯定與期
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%A8%98%E6%86%B6%E9%AB%94%E9%9B%99%E9%9B%84%E9%82%84%E8%83%BD%E6%BC%B2-%E6%B3%95%E4%BA%BA%E6%96%B0%E8%A9%95%E5%83%B9-073500548.html
- 事件5：從中職季冠軍看投資痛點 專家分析三檔主動式ETF
  - 來源：Yahoo 台股；發布時間：2026-10-07T06:46:02Z；台北時間：2026-10-07 14:46
  - 摘要：中華職棒37年(2026年)例行賽於昨天(10月6日)正式收官，由中信兄隊拿下季冠軍(請參考附表一)。中信兄弟在上一季的表現低迷，在本季可以繳出亮麗成績單，讓我感到相當好奇，於是乎身為分析師的職業病馬上就犯了，我研究了一下今年各項排行榜數據
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%BE%9E%E4%B8%AD%E8%81%B7%E5%AD%A3%E5%86%A0%E8%BB%8D%E7%9C%8B%E6%8A%95%E8%B3%87%E7%97%9B%E9%BB%9E%EF%BC%8C%E5%A4%A7%E5%A4%9A%E6%95%B8%E4%BA%BA%E9%83%BD%E6%B2%92%E6%83%B3%E5%88%B0-064602027.html
- 事件6：Q3營收達101億元寫紀錄！「記憶體模組大廠」9月破40億創次高　NAND Flash+DRAM有望漲價續點火
  - 來源：Yahoo 台股；發布時間：2026-10-07T23:40:00Z；台北時間：2026-10-08 07:40
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導記憶體模組大廠十銓（4967）昨（7）日公布新一期營收，其中9月合併營收為40.81億元，月增16.17%、年增109.69%，寫下歷史單...
  - 原文連結：https://tw.stock.yahoo.com/news/q3%E7%87%9F%E6%94%B6%E9%81%94101%E5%84%84%E5%85%83%E5%AF%AB%E7%B4%80%E9%8C%84-%E8%A8%98%E6%86%B6%E9%AB%94%E6%A8%A1%E7%B5%84%E5%A4%A7%E5%BB%A0-9%E6%9C%88%E7%A0%B440%E5%84%84%E5%89%B5%E6%AC%A1%E9%AB%98-nand-flash-234000837.html
- 事件7：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 來源：Federal Reserve；發布時間：Wed, 7 Oct 2026 18:00:00 GMT；台北時間：2026-10-08 02:00
  - 摘要：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261007a.htm
- 事件8：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 來源：Federal Reserve；發布時間：Mon, 5 Oct 2026 20:30:00 GMT；台北時間：2026-10-06 04:30
  - 摘要：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261005a.htm
- 事件9：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:45:00 GMT；台北時間：2026-10-03 04:45
  - 摘要：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261002a.htm
- 事件10：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:00:00 GMT；台北時間：2026-10-03 04:00
  - 摘要：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261002a.htm
- 事件11：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 15:00:00 GMT；台北時間：2026-10-02 23:00
  - 摘要：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261002a.htm
- 事件12：Fed officials see another hike coming, but no sign as to when, minutes show
  - 來源：CNBC；發布時間：Wed, 07 Oct 2026 18:42:36 GMT；台北時間：2026-10-08 02:42
  - 摘要：The Federal Reserve on Wednesday released minutes from its Sept. 15-16 policy meeting.
  - 原文連結：https://www.cnbc.com/2026/10/07/fed-officials-see-another-hike-coming-but-no-sign-as-to-when-minutes-show.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-07

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 50,050 | TAIFEX Proxy |
| 最高價 | 50,117 | TAIFEX Proxy |
| 最低價 | 49,842 | TAIFEX Proxy |
| 收盤價 | 49,979 | TAIFEX Proxy |
| 漲跌點數 | -103 | TAIFEX Proxy |
| 漲跌幅 | -0.21 | TAIFEX Proxy |
| 成交量 | 48,492 | TAIFEX Proxy |
| 日盤高點及低點 | 50,117 / 49,842 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,946 | TAIFEX Proxy |
| 最高價 | 49,946 | TAIFEX Proxy |
| 最低價 | 49,253 | TAIFEX Proxy |
| 收盤價 | 49,593 | TAIFEX Proxy |
| 漲跌點數 | -375 | TAIFEX Proxy |
| 漲跌幅 | -0.75 | TAIFEX Proxy |
| 成交量 | 18,643 | TAIFEX Proxy |
| 夜盤高點及低點 | 49,946 / 49,253 | TAIFEX Proxy |
| 結算價 | 49,968 | TAIFEX Proxy |
| 未平倉量 | 108,332 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 13,545 | TAIFEX Proxy |
| 外資空方 OI | 92,646 | TAIFEX Proxy |
| 外資多空淨 OI | -79,101 | TAIFEX Proxy |
| 投信多方 OI | 79,016 | TAIFEX Proxy |
| 投信空方 OI | 2,748 | TAIFEX Proxy |
| 投信多空淨 OI | +76,268 | TAIFEX Proxy |
| 自營商多方 OI | 2,833 | TAIFEX Proxy |
| 自營商空方 OI | 5,086 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,253 | TAIFEX Proxy |
| 三大法人合計多方 OI | 95,394 | TAIFEX Proxy |
| 三大法人合計空方 OI | 100,480 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,086 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +416 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +60 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -369 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 84,587 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,045 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,542 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-05→2026-10-07) | +866 | TAIFEX Proxy snapshots (2026-10-06) |
- 資料日期：2026-10-07 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 27,005 | TAIFEX Proxy |
| 外資日盤空單交易量 | 26,597 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +408 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 14,000 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,794 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -2,794 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +3,202 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +60 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +60 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -415 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +998 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,413 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +53 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,796 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +5.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -178.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 49,979 | TAIFEX Proxy |
| 加權指數價格 | 49,806.37 | twse-proxy |
| 台指期與加權指數價差 | +172.63 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.35 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +172.63 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -386 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 49,979 | 49,593 | +386 | TAIFEX Proxy |
| 成交量 | 29,849 | 18,643 | +11,206 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+107（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 27,005 | 26,597 | +408 | 14,000 | 16,794 | -2,794 | +3,202 | 13,545 | 92,646 | -79,101 | +416 | TAIFEX Proxy |
| 投信 | 150 | 90 | +60 | 0 | 0 | +0 | +60 | 79,016 | 2,748 | +76,268 | +60 | TAIFEX Proxy |
| 自營商 | 2,684 | 3,099 | -415 | 1,696 | 698 | +998 | -1,413 | 2,833 | 5,086 | -2,253 | -369 | TAIFEX Proxy |
| 三大法人合計 | 29,839 | 29,786 | +53 | 15,696 | 17,492 | -1,796 | +1,849 | 95,394 | 100,480 | -5,086 | +107 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 84,587 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,045 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,542 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-05→2026-10-07) | +866 | TAIFEX Proxy snapshots (2026-10-06) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 38.45% | TAIFEX Proxy |
| 夜盤漲跌點數 | -375 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -2,794 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-07 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-08 08:08:10 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 283,842 | TAIFEX Proxy |
| Call 總未平倉量 OI | 72,083 | TAIFEX Proxy |
| Call OI 增減 (2026-10-06→2026-10-07) | +22,031 | TAIFEX Proxy snapshots (2026-10-06) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 274,405 | TAIFEX Proxy |
| Put 總未平倉量 OI | 62,417 | TAIFEX Proxy |
| Put OI 增減 (2026-10-06→2026-10-07) | +13,813 | TAIFEX Proxy snapshots (2026-10-06) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.03 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.15 | TAIFEX Proxy |
| Put／Call Ratio | 0.87 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-05→2026-10-06) | 6.15 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-05→2026-10-06) | 3.52 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 100,978 | TAIFEX Proxy |
| 外資 Call日賣 | 104,212 | TAIFEX Proxy |
| 外資 Call日淨 | -3,234 | TAIFEX Proxy |
| 外資 Put日買 | 102,684 | TAIFEX Proxy |
| 外資 Put日賣 | 102,298 | TAIFEX Proxy |
| 外資 Put日淨 | +386 | TAIFEX Proxy |
| 外資 Call夜買 | 23,465 | TAIFEX Proxy |
| 外資 Call夜賣 | 23,340 | TAIFEX Proxy |
| 外資 Call夜淨 | +125 | TAIFEX Proxy |
| 外資 Put夜買 | 22,134 | TAIFEX Proxy |
| 外資 Put夜賣 | 22,076 | TAIFEX Proxy |
| 外資 Put夜淨 | +58 | TAIFEX Proxy |
| 外資 日盤淨總量 | -3,620 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -3,359 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +328 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 70,437 | TAIFEX Proxy |
| 自營商 Call日賣 | 70,141 | TAIFEX Proxy |
| 自營商 Call日淨 | +296 | TAIFEX Proxy |
| 自營商 Put日買 | 68,277 | TAIFEX Proxy |
| 自營商 Put日賣 | 77,186 | TAIFEX Proxy |
| 自營商 Put日淨 | -8,909 | TAIFEX Proxy |
| 自營商 Call夜買 | 13,388 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,266 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,878 | TAIFEX Proxy |
| 自營商 Put夜買 | 13,633 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,608 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,025 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +9,205 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +4,174 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -9,934 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 50,000 | 6,574 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,800 | 5,405 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,900 | 3,681 | TAIFEX Proxy |
| Call OI 最大履約價 | 50,000 | 6,574 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 50,000 | 6,574 | 9.12% | TAIFEX Proxy |
| C2 | 49,800 | 5,405 | 7.5% | TAIFEX Proxy |
| C3 | 49,900 | 3,681 | 5.11% | TAIFEX Proxy |
| C4 | 49,850 | 3,393 | 4.71% | TAIFEX Proxy |
| C5 | 52,500 | 2,871 | 3.98% | TAIFEX Proxy |
| C6 | 52,000 | 2,847 | 3.95% | TAIFEX Proxy |
| C7 | 49,750 | 2,757 | 3.82% | TAIFEX Proxy |
| C8 | 50,700 | 2,754 | 3.82% | TAIFEX Proxy |
| C9 | 49,700 | 2,609 | 3.62% | TAIFEX Proxy |
| C10 | 50,200 | 2,248 | 3.12% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,600 | 3,353 | TAIFEX Proxy |
| Put OI 第2大履約價 | 49,500 | 2,993 | TAIFEX Proxy |
| Put OI 第3大履約價 | 49,000 | 2,979 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,600 | 3,353 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,600 | 3,353 | 5.37% | TAIFEX Proxy |
| P2 | 49,500 | 2,993 | 4.8% | TAIFEX Proxy |
| P3 | 49,000 | 2,979 | 4.77% | TAIFEX Proxy |
| P4 | 49,700 | 2,868 | 4.59% | TAIFEX Proxy |
| P5 | 49,800 | 2,734 | 4.38% | TAIFEX Proxy |
| P6 | 49,750 | 2,310 | 3.7% | TAIFEX Proxy |
| P7 | 48,800 | 2,089 | 3.35% | TAIFEX Proxy |
| P8 | 49,400 | 2,042 | 3.27% | TAIFEX Proxy |
| P9 | 49,650 | 1,969 | 3.15% | TAIFEX Proxy |
| P10 | 48,000 | 1,700 | 2.72% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 49,800 (+4,140) | TAIFEX Proxy snapshots (2026-10-06) |
| Call OI 減少最多的履約價 | 49,500 (-396) | TAIFEX Proxy snapshots (2026-10-06) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,600 (+2,393) | TAIFEX Proxy snapshots (2026-10-06) |
| Put OI 減少最多的履約價 | 49,200 (-939) | TAIFEX Proxy snapshots (2026-10-06) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 50,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-06→2026-10-07) | +0 | TAIFEX Proxy snapshots (2026-10-06) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,600 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-06→2026-10-07) | +600 | TAIFEX Proxy snapshots (2026-10-06) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 49,300.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 資料日期 | 2026-10-07 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 49,585.51 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 資料日期 | 2026-10-07 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 49,650 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-06→2026-10-07) | +400 | TAIFEX Proxy snapshots (2026-10-06) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 203,276 | 206,896 | -3,620 | 45,541 | 45,474 | +67 | -3,687 | TAIFEX Proxy |
| 投信 | 205 | 4,984 | -4,779 | 0 | 0 | +0 | -4,779 | TAIFEX Proxy |
| 自營商 | 147,623 | 138,418 | +9,205 | 25,996 | 30,899 | -4,903 | +14,108 | TAIFEX Proxy |
| 三大法人合計 | 351,104 | 350,298 | +806 | 71,537 | 76,373 | -4,836 | +5,642 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 10.66 | 10.47 | +0.18 | 4.14 | 4.14 | -0.00 | +0.18 | TAIFEX Proxy |
| 投信 | 0.14 | 3.74 | -3.60 | 0.00 | 0.00 | +0 | -3.60 | TAIFEX Proxy |
| 自營商 | 10.25 | 6.63 | +3.62 | 2.61 | 3.18 | -0.57 | +4.19 | TAIFEX Proxy |
| 三大法人合計 | 21.04 | 20.84 | +0.20 | 6.75 | 7.33 | -0.57 | +0.77 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,110 | TAIFEX Proxy |
| 買權空方 OI | 12,403 | TAIFEX Proxy |
| 買權多空淨 OI | +1,707 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-05→2026-10-07) | +146 | TAIFEX Proxy snapshots (2026-10-06) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,123 | TAIFEX Proxy |
| 賣權空方 OI | 10,076 | TAIFEX Proxy |
| 賣權多空淨 OI | +47 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-05→2026-10-07) | +935 | TAIFEX Proxy snapshots (2026-10-06) |
- 資料日期：買權 2026-10-07／賣權 2026-10-07 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +866 | 2026-10-05→2026-10-07 | TAIFEX Proxy snapshots (2026-10-06) |
| 買權前十大 | +146 | 2026-10-05→2026-10-07 | TAIFEX Proxy snapshots (2026-10-06) |
| 賣權前十大 | +935 | 2026-10-05→2026-10-07 | TAIFEX Proxy snapshots (2026-10-06) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-07；資料時間：2026-10-08 08:08:10；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
- 註記：夜盤 OHLC 資料日期 2026-10-08 (T0 2026-10-07)，來源 proxy
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
- margin_ratio：`前值遞補 (DATA 2026-10-06；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-06)，非 T0 2026-10-07
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -130.4 | -79,101 | +408 | -2,794 | -3,620 | +67 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -33.2 | +76,268 | +60 | +0 | -4,779 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -78.0 | -2,253 | -415 | +998 | +9,205 | -4,903 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
