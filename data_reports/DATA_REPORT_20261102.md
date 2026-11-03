# DATA_REPORT_20261102

- 報告日期：`2026-11-03`
- T0 交易日期：`2026-11-02`
- 資料產出時間：`2026-11-03 12:32:18`
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
| 加權指數 | 44,920.14 | 點 | twse-proxy |
| 開盤 | 45,034.53 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 45,156.17 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 44,399.10 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 44,920.14 | 點 | twse-proxy |
| 漲跌點數 | -291.69 | 點 | twse-proxy |
| 漲跌幅 | -0.65 | % | twse-proxy |
| 成交金額 | 7,996.9 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 518 | twse-proxy |
| 下跌家數 | 447 | twse-proxy |
| 平盤家數 | 116 | twse-proxy |
| 漲停家數 | 10 | twse-proxy |
| 跌停家數 | 5 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 390 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 389 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 82 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 31 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 3 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -735.2 | 億元 | twse-proxy /institutional |
| 投信 | +338.2 | 億元 | twse-proxy /institutional |
| 自營商 | -152.9 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -549.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,271.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -16.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 231,634 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -1,903 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 171.70 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,664,523 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,704 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 526 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 7,996.9 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,548.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 9,545.8 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,541.40 | -38.67 | -0.51 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,164.36 | -272.64 | -1.07 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,989.82 | -395.03 | -1.39 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,983.98 | 213.67 | +0.41 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,328.33 | -360.47 | -3.37 | Yahoo Finance Chart API |
| VIX | ^VIX | 21.15 | 1.73 | +8.91 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,081.86 | -208.25 | -0.33 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,645.93 | -213.15 | -3.64 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,515.29 | 121.97 | +0.52 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,612.09 | -25.95 | -0.71 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,993.07 | -17.61 | -0.16 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,566.25 | -8.25 | -0.11 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,148.50 | 21.00 | +0.07 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,937.00 | -196.00 | -0.38 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,814.30 | -3.50 | -0.12 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.59 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.27 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.74 | 0.13 | +0.40 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.77 | 0.02 | +0.02 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.89 | 0.22 | +0.14 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,339.50 | 13.98 | +1.05 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 398.63 | -7.50 | -1.85 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.39 | -0.29 | -1.74 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.17 | -0.33 | -0.84 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 96.80 | 0.34 | +0.35 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,934.90 | -34.70 | -0.87 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,885.17 | -1,363.28 | -1.74 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：聯發科25年股東報酬率33倍 蔡力行喊「買我們的股票」
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:13:29Z；台北時間：2026-11-03 11:13
  - 摘要：由金管會攜手證交所、櫃買中心、期交所及集保結算所共同舉辦的2026年第二屆「台灣週」，今（3）日正式揭開序幕，活動將一路持續至11月13日。IC設計龍頭聯發科（2454）副董事長暨執行長蔡力行出席開幕式時表示，聯發科自2001年上市以來，市
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E7%99%BC%E7%A7%91%E6%94%BE25%E5%B9%B4%E6%BB%BE33%E5%80%8D%EF%BC%81%E8%94%A1%E5%8A%9B%E8%A1%8C%E6%8F%AA%E5%A4%A7%E5%AE%B6%E3%80%8C%E8%B2%B7%E6%88%91%E5%80%91%E8%82%A1%E7%A5%A8%E3%80%8D-031329391.html
- 事件2：大盤高點回落5800點 財經作家點出「市場貪婪訊號」
  - 來源：Yahoo 台股；發布時間：2026-11-03T02:35:31Z；台北時間：2026-11-03 10:35
  - 摘要：台股近期持續走弱，今（3）日開盤重挫逾700點，最低下探44152.77點，自指數逼近5萬點高點以來，短短數周已大跌逾5800點，市場至今仍未出現明顯反彈，讓投資人信心受到打擊。財經作家狄驤在臉書發文分析指出，這波股市修正的關鍵問題，在於市
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E7%8B%82%E7%80%895800%E9%BB%9E%E9%82%84%E6%B2%92%E8%B7%8C%E5%AE%8C-%E5%B0%88%E5%AE%B6%E6%8F%AD%E8%87%B4%E5%91%BD%E6%95%97%E7%AD%86-%E6%AF%947%E6%9C%88%E8%82%A1%E7%81%BD%E6%9B%B4%E7%B3%9F-023531259.html
- 事件3：市值排名洗牌 台達電從三哥寶座摔落
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:07:30Z；台北時間：2026-11-03 11:07
  - 摘要：[NOWNEWS今日新聞]台北股市今（3）日開低走低，加權指數盤中最低下探44,152.77點，重挫767.37點，失守45K關卡，市場進一步面臨4萬4000點整數關卡保衛戰。另一方面，權值股市值排名...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E8%87%A844k%E4%BF%9D%E8%A1%9B%E6%88%B0-%E9%B4%BB%E6%B5%B7%E5%B8%82%E5%80%BC%E8%B6%85%E8%BB%8A%E5%8F%B0%E9%81%94%E9%9B%BB%E5%A5%AA%E7%AC%AC3-030730408.html
- 事件4：國巨股價4字頭、近3個月低點 分析師：難立刻反彈
  - 來源：Yahoo 台股；發布時間：2026-11-03T02:31:44Z；台北時間：2026-11-03 10:31
  - 摘要：被動元件大廠國巨（2327）今（3）日股價來到476.5元，觸及近3個月低點，已接近7月底創下的前低。凱旭投顧分析師王士維指出，目前國巨以明年獲利來看本益比來到合理區間，且籌碼凌亂，短線上台股止跌的話，要馬上跟著反彈難度相對較高。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%B7%A8%E5%A4%B1%E5%AE%88500%E5%85%83%E5%86%8D%E8%B7%8C4%E8%BF%913%E6%9C%88%E6%96%B0%E4%BD%8E%E6%98%AF%E3%80%8C%E7%94%9C%E7%94%9C%E5%83%B9%E3%80%8D%EF%BC%9F%E5%88%86%E6%9E%90%E5%B8%AB%E6%9B%9D%E9%97%9C%E9%8D%B5%EF%BC%9A%E9%9B%A3%E7%AB%8B%E5%88%BB%E5%8F%8D%E5%BD%88-023226646.html
- 事件5：台積電連四跌失守2300元 分析師喊：短線築底反彈
  - 來源：Yahoo 台股；發布時間：2026-11-03T01:14:46Z；台北時間：2026-11-03 09:14
  - 摘要：台積電今（3）日開盤後走勢疲軟，早盤失守2300元關卡，最低觸及2295元，寫下近4個月新低，也是連續四個交易日下跌，對此，倫元投顧分析師王春盛表示，短線有望進行築底反彈，考量KD指標已落在20以下的超賣區，投資人可在此位階採取「分批佈局」
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E9%80%A3%E5%9B%9B%E8%B7%8C%EF%BC%81%E5%A4%B1%E5%AE%882300%E5%85%83%E9%97%9C%E5%8D%A1%E5%88%B7%E6%96%B04%E5%80%8B%E6%9C%88%E7%9B%A4%E4%B8%AD%E6%9C%80%E4%BD%8E-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E8%A6%81%E7%AF%89%E5%BA%95%E5%8F%8D%E5%BD%88%E4%BA%86-011446679.html
- 事件6：大盤震盪越跌越買 00406A、0050等受益人數創高
  - 來源：Yahoo 台股；發布時間：2026-11-03T02:22:39Z；台北時間：2026-11-03 10:22
  - 摘要：[NOWNEWS今日新聞]無懼台股震盪，投資人越跌越買！台股ETF受益人數連續3周創新高。根據集保戶股權分散10月30日最新統計資料顯示，台股ETF受益人數周增17.7萬人，總人數來到1975萬770...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B6%8A%E8%B7%8C%E8%B6%8A%E8%B2%B7-24%E6%AA%94%E5%8F%B0%E8%82%A1etf%E5%8F%97%E7%9B%8A%E4%BA%BA%E6%95%B8%E5%89%B5%E9%AB%98-022239609.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Australia hikes rates to 18-year high to fight inflation
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 03:46:20 GMT；台北時間：2026-11-03 11:46
  - 摘要：The Reserve Bank of Australia's decision was in line with expectations from economists polled by Reuters, and marked its fifth rate increase this year
  - 原文連結：https://www.cnbc.com/2026/11/03/australia-hikes-rates-18-year-high-finflation.html
- 事件10：Feeling isolated? Half of in-office workers describe their desk jobs as 'remote,' NY Fed survey finds
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 02:31:00 GMT；台北時間：2026-11-03 10:31
  - 摘要：Employees describing jobs as 'remote' are now often in-office, as companies fail to create the collaboration they claim is critical, NY Fed research s
  - 原文連結：https://www.cnbc.com/2026/11/02/remote-work-in-office-mandate-new-york-fed.html
- 事件11：Crude oil prices sell off more than 7% on Iran peace talk hopes ahead of U.S. midterms
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 20:19:25 GMT；台北時間：2026-11-03 04:19
  - 摘要：Oil fell Monday, amid news that both the U.S. and Iran are pursuing diplomacy amid ongoing Mideast tensions
  - 原文連結：https://www.cnbc.com/2026/11/02/oil-prices-fall-as-iran-us-pursue-diplomacy.html
- 事件12：Stock market after midterm elections: What S&P 500 history shows
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 23:13:34 GMT；台北時間：2026-11-03 07:13
  - 摘要：Midterms historically precede a strong year for the S&P 500. What to know if Democrats win back Congress
  - 原文連結：https://www.cnbc.com/2026/11/02/stock-market-after-midterm-elections-sp-500-history.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-02

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,000 | TAIFEX Proxy |
| 最高價 | 45,332 | TAIFEX Proxy |
| 最低價 | 44,700 | TAIFEX Proxy |
| 收盤價 | 45,256 | TAIFEX Proxy |
| 漲跌點數 | -44 | TAIFEX Proxy |
| 漲跌幅 | -0.10 | TAIFEX Proxy |
| 成交量 | 52,221 | TAIFEX Proxy |
| 日盤高點及低點 | 45,332 / 44,700 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,227 | TAIFEX Proxy |
| 最高價 | 45,487 | TAIFEX Proxy |
| 最低價 | 44,271 | TAIFEX Proxy |
| 收盤價 | 44,310 | TAIFEX Proxy |
| 漲跌點數 | -917 | TAIFEX Proxy |
| 漲跌幅 | -2.03 | TAIFEX Proxy |
| 成交量 | 38,487 | TAIFEX Proxy |
| 夜盤高點及低點 | 45,487 / 44,271 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,952 | TAIFEX Proxy |
| 外資空方 OI | 98,331 | TAIFEX Proxy |
| 外資多空淨 OI | -89,379 | TAIFEX Proxy |
| 投信多方 OI | 91,953 | TAIFEX Proxy |
| 投信空方 OI | 2,814 | TAIFEX Proxy |
| 投信多空淨 OI | +89,139 | TAIFEX Proxy |
| 自營商多方 OI | 5,640 | TAIFEX Proxy |
| 自營商空方 OI | 4,333 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,307 | TAIFEX Proxy |
| 三大法人合計多方 OI | 106,545 | TAIFEX Proxy |
| 三大法人合計空方 OI | 105,478 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +1,067 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +2,862 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -72 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -429 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,291 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,052 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,239 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-28→2026-11-02) | -664 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：2026-11-02 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 57,787 | TAIFEX Proxy |
| 外資日盤空單交易量 | 54,986 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,801 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 21,868 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 23,217 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,349 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +4,150 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -72 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -72 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -457 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +173 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -630 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,272 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,176 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +203.5 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -107.2 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 45,256 | TAIFEX Proxy |
| 加權指數價格 | 44,920.14 | twse-proxy |
| 台指期與加權指數價差 | +335.86 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.75 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +335.86 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -946 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 45,256 | 44,310 | +946 | TAIFEX Proxy |
| 成交量 | 52,221 | 38,487 | +13,734 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+2,361（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 57,787 | 54,986 | +2,801 | 21,868 | 23,217 | -1,349 | +4,150 | 8,952 | 98,331 | -89,379 | +2,862 | TAIFEX Proxy |
| 投信 | 121 | 193 | -72 | 0 | 0 | +0 | -72 | 91,953 | 2,814 | +89,139 | -72 | TAIFEX Proxy |
| 自營商 | 4,663 | 5,120 | -457 | 843 | 670 | +173 | -630 | 5,640 | 4,333 | +1,307 | -429 | TAIFEX Proxy |
| 三大法人合計 | 62,571 | 60,299 | +2,272 | 22,711 | 23,887 | -1,176 | +3,448 | 106,545 | 105,478 | +1,067 | +2,361 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,291 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,052 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,239 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-28→2026-11-02) | -664 | TAIFEX Proxy snapshots (2026-10-29) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 42.43% | TAIFEX Proxy |
| 夜盤漲跌點數 | -917 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,349 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-02 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-03 12:32:18 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 140,350 | TAIFEX Proxy |
| Call 總未平倉量 OI | 61,578 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 135,722 | TAIFEX Proxy |
| Put 總未平倉量 OI | 34,887 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.03 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.77 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-30→2026-11-02) | 2.84 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-30→2026-11-02) | -1.01 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 43,372 | TAIFEX Proxy |
| 外資 Call日賣 | 43,672 | TAIFEX Proxy |
| 外資 Call日淨 | -300 | TAIFEX Proxy |
| 外資 Put日買 | 47,746 | TAIFEX Proxy |
| 外資 Put日賣 | 47,879 | TAIFEX Proxy |
| 外資 Put日淨 | -133 | TAIFEX Proxy |
| 外資 Call夜買 | 27,173 | TAIFEX Proxy |
| 外資 Call夜賣 | 27,381 | TAIFEX Proxy |
| 外資 Call夜淨 | -208 | TAIFEX Proxy |
| 外資 Put夜買 | 25,389 | TAIFEX Proxy |
| 外資 Put夜賣 | 25,019 | TAIFEX Proxy |
| 外資 Put夜淨 | +370 | TAIFEX Proxy |
| 外資 日盤淨總量 | -167 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -92 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -503 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 41,575 | TAIFEX Proxy |
| 自營商 Call日賣 | 35,503 | TAIFEX Proxy |
| 自營商 Call日淨 | +6,072 | TAIFEX Proxy |
| 自營商 Put日買 | 36,775 | TAIFEX Proxy |
| 自營商 Put日賣 | 38,102 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,327 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,778 | TAIFEX Proxy |
| 自營商 Call夜賣 | 13,663 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,885 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,623 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,864 | TAIFEX Proxy |
| 自營商 Put夜淨 | +759 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +7,399 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +8,957 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -2,086 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,000 | 4,503 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,400 | 4,384 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,500 | 2,534 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,000 | 4,503 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,000 | 4,503 | 7.31% | TAIFEX Proxy |
| C2 | 49,400 | 4,384 | 7.12% | TAIFEX Proxy |
| C3 | 44,500 | 2,534 | 4.12% | TAIFEX Proxy |
| C4 | 51,000 | 2,336 | 3.79% | TAIFEX Proxy |
| C5 | 46,000 | 2,072 | 3.36% | TAIFEX Proxy |
| C6 | 46,500 | 1,877 | 3.05% | TAIFEX Proxy |
| C7 | 44,300 | 1,731 | 2.81% | TAIFEX Proxy |
| C8 | 44,000 | 1,685 | 2.74% | TAIFEX Proxy |
| C9 | 44,100 | 1,672 | 2.72% | TAIFEX Proxy |
| C10 | 43,900 | 1,643 | 2.67% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 44,000 | 2,661 | TAIFEX Proxy |
| Put OI 第2大履約價 | 43,000 | 2,543 | TAIFEX Proxy |
| Put OI 第3大履約價 | 41,400 | 1,756 | TAIFEX Proxy |
| Put OI 最大履約價 | 44,000 | 2,661 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 44,000 | 2,661 | 7.63% | TAIFEX Proxy |
| P2 | 43,000 | 2,543 | 7.29% | TAIFEX Proxy |
| P3 | 41,400 | 1,756 | 5.03% | TAIFEX Proxy |
| P4 | 42,000 | 1,461 | 4.19% | TAIFEX Proxy |
| P5 | 43,500 | 1,274 | 3.65% | TAIFEX Proxy |
| P6 | 40,600 | 1,250 | 3.58% | TAIFEX Proxy |
| P7 | 42,500 | 1,220 | 3.5% | TAIFEX Proxy |
| P8 | 45,000 | 1,178 | 3.38% | TAIFEX Proxy |
| P9 | 44,500 | 1,105 | 3.17% | TAIFEX Proxy |
| P10 | 43,300 | 841 | 2.41% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | unavailable | 端點未提供 |
| Call OI 減少最多的履約價 | unavailable | 端點未提供 |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | unavailable | 端點未提供 |
| Put OI 減少最多的履約價 | unavailable | 端點未提供 |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 46,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-02 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 44,256.47 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-02 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 44,400 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 91,251 | 91,418 | -167 | 52,192 | 52,770 | -578 | +411 | TAIFEX Proxy |
| 投信 | 0 | 6,362 | -6,362 | 0 | 0 | +0 | -6,362 | TAIFEX Proxy |
| 自營商 | 79,677 | 72,278 | +7,399 | 24,642 | 28,286 | -3,644 | +11,043 | TAIFEX Proxy |
| 三大法人合計 | 170,928 | 170,058 | +870 | 76,834 | 81,056 | -4,222 | +5,092 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.36 | 11.17 | +0.18 | 4.82 | 4.93 | -0.11 | +0.29 | TAIFEX Proxy |
| 投信 | 0.00 | 3.01 | -3.01 | 0.00 | 0.00 | +0 | -3.01 | TAIFEX Proxy |
| 自營商 | 10.22 | 8.40 | +1.82 | 2.18 | 2.48 | -0.30 | +2.12 | TAIFEX Proxy |
| 三大法人合計 | 21.57 | 22.58 | -1.01 | 7.00 | 7.41 | -0.41 | -0.60 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 10,357 | TAIFEX Proxy |
| 買權空方 OI | 13,230 | TAIFEX Proxy |
| 買權多空淨 OI | -2,873 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-28→2026-11-02) | -1,741 | TAIFEX Proxy snapshots (2026-10-29) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,297 | TAIFEX Proxy |
| 賣權空方 OI | 10,337 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,040 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-28→2026-11-02) | +12 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：買權 2026-11-02／賣權 2026-11-02 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -664 | 2026-10-28→2026-11-02 | TAIFEX Proxy snapshots (2026-10-29) |
| 買權前十大 | -1,741 | 2026-10-28→2026-11-02 | TAIFEX Proxy snapshots (2026-10-29) |
| 賣權前十大 | +12 | 2026-10-28→2026-11-02 | TAIFEX Proxy snapshots (2026-10-29) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-02；資料時間：2026-11-03 12:32:18；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-11-02 非今日 2026-11-03，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202610F5→新202611W1），日對日 OI/Walls 變化不適用

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
| 外資 | -735.2 | -89,379 | +2,801 | -1,349 | -167 | -578 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +338.2 | +89,139 | -72 | +0 | -6,362 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -152.9 | +1,307 | -457 | +173 | +7,399 | -3,644 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
