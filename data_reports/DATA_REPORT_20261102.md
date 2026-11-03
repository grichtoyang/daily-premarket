# DATA_REPORT_20261102

- 報告日期：`2026-11-03`
- T0 交易日期：`2026-11-02`
- 資料產出時間：`2026-11-03 08:55:11`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`manual`

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

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `TWSE 上市自建估算（資料日期：2026-11-02；估值 1239 檔；6 檔採最近有效收盤價（價格日期 20260402 至 20261102）；Blave 同 T0 交叉驗證 171.7110%，差異 0.007 個百分點）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,271.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -16.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 231,634 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -1,903 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 171.70 | % | TWSE 上市自建估算（資料日期：2026-11-02；估值 1239 檔；6 檔採最近有效收盤價（價格日期 20260402 至 20261102）；Blave 同 T0 交叉驗證 171.7110%，差異 0.007 個百分點） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,664,523 | 張 | TWSE TWT96U + TWT96U GRETAI（上櫃） + TPEX margin_sbl |
| 借券賣出餘額 | 36,704 | 張 | TPEX margin_sbl |
| 借券賣出增減 | 526 | 張 | TPEX margin_sbl |

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
| 日經225 | ^N225 | 63,290.11 | -1,369.36 | -2.12 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,685.71 | -45.03 | -0.79 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,294.42 | 335.77 | +1.46 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,599.02 | -52.42 | -1.44 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,833.78 | -304.42 | -2.73 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,584.00 | -30.00 | -0.39 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,192.75 | -341.25 | -1.20 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,137.00 | 219.00 | +0.42 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,820.20 | -1.10 | -0.04 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.59 | 0.00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.03 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.31 | 0.00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.27 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.61 | 0.01 | +0.02 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.78 | -0.10 | -0.10 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.89 | 0.21 | +0.14 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.44 | 16.92 | +1.28 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 96.78 | -7.34 | -7.05 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,962.80 | 63.90 | +1.64 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,936.76 | -1,311.70 | -1.68 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：纏訟多年將和解華映 大同有望回沖近百億訴訟損失
  - 來源：Yahoo 台股；發布時間：2026-11-02T13:00:59Z；台北時間：2026-11-02 21:00
  - 摘要：大同（2371）纏訟多年的華映案有大進展！大同2日晚間召開重訊記者會宣布，雙方董事會通過以人民幣7.68億元（約新台幣近38億元）和解，相較中國最高人民法院原判決人民幣30.29億元，大幅減少約74.6%，由於大同去年保守起見，一次性認列1
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E5%90%8C%E6%93%AC38%E5%84%84%E5%85%83%E5%92%8C%E8%A7%A3%E8%8F%AF%E6%98%A0%EF%BC%81%E6%9C%89%E6%9C%9B%E5%9B%9E%E6%B2%96%E8%BF%91%E7%99%BE%E5%84%84-%E6%AF%8F%E8%82%A1%E8%B2%A2%E7%8D%BB46%E5%85%83-130059812.html
- 事件2：外資持股比創20年新低 台積鉅額交易意外現漲停價
  - 來源：Yahoo 台股；發布時間：2026-11-02T14:22:42Z；台北時間：2026-11-02 22:22
  - 摘要：權值龍頭台積電（2330）2日繼續遭外資無情調節，單日面臨逾1.5萬張提款、賣超金額高達349.7億元。盤中股價一度重挫至2,310元，距離2,300元整數大關僅差10元；尾盤雖在政策買盤加碼護盤下收斂跌幅，終場仍下跌40元，收在2,330
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%96%AE%E6%97%A5%E5%86%8D%E7%A0%8D349%E5%84%84%E5%85%83-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%A4%96%E8%B3%87%E6%8C%81%E8%82%A1%E6%AF%94%E5%89%B520%E5%B9%B4%E6%96%B0%E4%BD%8E-%E9%89%85%E9%A1%8D%E4%BA%A4%E6%98%93%E5%8D%BB%E9%A9%9A%E7%8F%BE%E6%BC%B2%E5%81%9C%E5%83%B9-142242332.html
- 事件3：前三季每股純益逾90元 十銓：記憶體最嚴重缺貨才開始
  - 來源：Yahoo 台股；發布時間：2026-11-02T22:37:10Z；台北時間：2026-11-03 06:37
  - 摘要：記憶體模組廠十銓（4967）執行長陳慶文昨（2）日於法說會表示，AI需求排擠傳統記憶體產能，加上供應鏈高度集中，「這次行情真的不一樣」，預期真正最嚴重的缺貨階段才要開始，價格仍將走高，整體供需最快要到2028年下半年才有機會恢復平衡。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8D%81%E9%8A%93-%E6%9C%80%E5%9A%B4%E9%87%8D%E7%BC%BA%E8%B2%A8%E6%89%8D%E9%96%8B%E5%A7%8B-223710573.html
- 事件4：台指期夜盤狂瀉917點 今恐測試44K
  - 來源：Yahoo 台股；發布時間：2026-11-02T22:24:00Z；台北時間：2026-11-03 06:24
  - 摘要：11月開局不利，美股主要指數週一（2日）跌多漲少，市場資金持續撤離科技股，轉向傳統產業。儘管美國與伊朗有望重啟和平談判，帶動國際油價大跌，一度提振市場信心，但半導體與大型科技股賣壓沉重，拖累那斯達克及標普500指數由紅翻黑，僅道瓊在工業與居
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%9B%A4%E5%89%8D-%E7%BE%8E%E8%B2%BB%E5%8D%8A%E8%A1%80%E5%B4%A93-3-%E5%8F%B0%E6%8C%87%E6%9C%9F%E5%A4%9C%E7%9B%A4%E5%B4%A9917%E9%BB%9E-%E5%8F%B0%E8%82%A14%E8%90%AC4%E9%97%9C%E5%8D%A1%E6%8B%89%E8%AD%A6%E5%A0%B1-222400511.html
- 事件5：15檔注意股出列 冠西電6天累漲44%、聯茂本益比101倍
  - 來源：Yahoo 台股；發布時間：2026-11-03T00:20:00Z；台北時間：2026-11-03 08:20
  - 摘要：[FTNN新聞網]記者莊蕙如／綜合報導證交所公布11月2日共15檔注意股，聯茂（6213）、大量（3167）、禾伸堂（3026）及騰輝電子-KY（6672）等熱門股全數入列，其...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%80%E7%8B%82%E4%B8%8D%E6%98%AF%E8%81%AF%E8%8C%82-%E9%80%99%E6%AA%94-90%E5%A4%A9%E6%9A%B4%E6%BC%B2589-%E6%9D%B1%E5%8F%B06%E5%A4%A9%E9%A3%8639-15%E6%AA%94%E6%B3%A8%E6%84%8F%E8%82%A1%E5%90%8D%E5%96%AE-002000552.html
- 事件6：美股半導體、記憶體族群都低迷 費半慘跌3.3%
  - 來源：Yahoo 台股；發布時間：2026-11-02T21:56:41Z；台北時間：2026-11-03 05:56
  - 摘要：美股週一多收低，那指跌1.07%、費半跌3.37%，資金續撤科技股，標普與那指翻黑，道瓊漲213.67點 美伊釋出重啟和平談判訊號，布蘭特與WTI原油期貨重挫逾7%，帶動市場風險情緒一度回升 甲骨文啟動200億美元融資、AI支出疑慮升溫，M
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E7%9B%A4%E5%BE%8C-%E5%B7%9D%E6%99%AE%E7%A8%B1%E4%B8%8D%E6%80%A5%E6%96%BC%E5%86%8D%E6%89%93%E4%BC%8A%E6%9C%97-%E9%8E%A7%E4%BF%A0%E8%B2%A1%E6%B8%AC%E6%8B%96%E7%B4%AF%E8%A8%98%E6%86%B6%E9%AB%94%E8%82%A1-%E8%B2%BB%E5%8D%8A11%E6%9C%88%E9%A6%96%E6%97%A5%E6%8C%AB%E9%80%BE3-215641206.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Feeling isolated? Half of in-office workers describe their desk jobs as 'remote,' NY Fed survey finds
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 22:34:07 GMT；台北時間：2026-11-03 06:34
  - 摘要：Employees describing jobs as 'remote' are now often in-office, as companies fail to create the collaboration they claim is critical, NY Fed research s
  - 原文連結：https://www.cnbc.com/2026/11/02/remote-work-in-office-mandate-new-york-fed.html
- 事件10：Stock market after midterm elections: What S&P 500 history shows
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 23:13:34 GMT；台北時間：2026-11-03 07:13
  - 摘要：Midterms historically precede a strong year for the S&P 500. What to know if Democrats win back Congress
  - 原文連結：https://www.cnbc.com/2026/11/02/stock-market-after-midterm-elections-sp-500-history.html
- 事件11：Crude oil prices sell off more than 7% on Iran peace talk hopes ahead of U.S. midterms
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 20:19:25 GMT；台北時間：2026-11-03 04:19
  - 摘要：Oil fell Monday, amid news that both the U.S. and Iran are pursuing diplomacy amid ongoing Mideast tensions
  - 原文連結：https://www.cnbc.com/2026/11/02/oil-prices-fall-as-iran-us-pursue-diplomacy.html
- 事件12：Jim Cramer says these six fashion stocks are buys beyond the AI trade
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 23:54:27 GMT；台北時間：2026-11-03 07:54
  - 摘要：While technology stocks have come under pressure in recent weeks, consumer stocks have been resilient.
  - 原文連結：https://www.cnbc.com/2026/11/02/jim-cramer-fashion-stocks.html


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

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 57,787 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 54,986 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,801 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 21,868 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 23,217 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,349 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +4,150 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -72 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -72 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -457 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +173 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -630 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,272 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,176 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | +203.5 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -107.2 | 億元 | TAIFEX Proxy |

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
| 資料更新時間 | 2026-11-03 08:55:11 | 本機 |
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

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.03 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.77 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-10-30→2026-11-02) | 2.84 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-10-30→2026-11-02) | -1.01 | 百分點（pp） | TAIFEX Proxy |
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
| Gamma Wall 價位 | 46,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-02 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 44,256.47 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-02 | TAIFEX Proxy (options-gamma-levels) |

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 3,510,697,647.65 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 16,362,020,678.96 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 履約價資料筆數 | 155 | 資料日期：2026-11-02 |
| 正 Net GEX 最大履約價 | 46,000 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 44,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：46,000（458,793,202.00 NT$）、44,500（453,493,668.97 NT$）、44,300（368,384,608.96 NT$）、45,200（304,172,481.73 NT$）、44,100（271,627,851.16 NT$）
- 負 Net GEX Top 5：44,000（-271,383,834.60 NT$）、43,000（-239,226,039.23 NT$）、43,500（-192,027,359.50 NT$）、44,600（-187,619,113.66 NT$）、44,800（-157,293,759.35 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-02","underlying":44920.14,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":3510697647.653636,"gross_gex_1pct":16362020678.960987,"levels":[{"strike":40600.0,"call_gex_1pct":0.0,"put_gex_1pct":-16084330.965500858,"net_gex_1pct":-16084330.965500858,"gross_gex_1pct":16084330.965500858,"call_oi":0,"put_oi":1250},{"strike":40700.0,"call_gex_1pct":0.0,"put_gex_1pct":-2946597.9652689667,"net_gex_1pct":-2946597.9652689667,"gross_gex_1pct":2946597.9652689667,"call_oi":0,"put_oi":209},{"strike":40800.0,"call_gex_1pct":0.0,"put_gex_1pct":-514942.8262371828,"net_gex_1pct":-514942.8262371828,"gross_gex_1pct":514942.8262371828,"call_oi":0,"put_oi":34},{"strike":40900.0,"call_gex_1pct":0.0,"put_gex_1pct":-556202.5900452189,"net_gex_1pct":-556202.5900452189,"gross_gex_1pct":556202.5900452189,"call_oi":0,"put_oi":35},{"strike":41000.0,"call_gex_1pct":0.0,"put_gex_1pct":-2016077.6365134637,"net_gex_1pct":-2016077.6365134637,"gross_gex_1pct":2016077.6365134637,"call_oi":0,"put_oi":115},{"strike":41100.0,"call_gex_1pct":0.0,"put_gex_1pct":-820427.2431300516,"net_gex_1pct":-820427.2431300516,"gross_gex_1pct":820427.2431300516,"call_oi":0,"put_oi":44},{"strike":41200.0,"call_gex_1pct":0.0,"put_gex_1pct":-995225.4447863783,"net_gex_1pct":-995225.4447863783,"gross_gex_1pct":995225.4447863783,"call_oi":0,"put_oi":49},{"strike":41300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1604895.664065133,"net_gex_1pct":-1604895.664065133,"gross_gex_1pct":1604895.664065133,"call_oi":0,"put_oi":72},{"strike":41400.0,"call_gex_1pct":0.0,"put_gex_1pct":-42170311.517294616,"net_gex_1pct":-42170311.517294616,"gross_gex_1pct":42170311.517294616,"call_oi":0,"put_oi":1756},{"strike":41500.0,"call_gex_1pct":0.0,"put_gex_1pct":-12594212.35554742,"net_gex_1pct":-12594212.35554742,"gross_gex_1pct":12594212.35554742,"call_oi":0,"put_oi":501},{"strike":41600.0,"call_gex_1pct":53420.819250314154,"put_gex_1pct":-11902546.359733073,"net_gex_1pct":-11849125.54048276,"gross_gex_1pct":11955967.178983387,"call_oi":1,"put_oi":423},{"strike":41700.0,"call_gex_1pct":0.0,"put_gex_1pct":-6833453.209323979,"net_gex_1pct":-6833453.209323979,"gross_gex_1pct":6833453.209323979,"call_oi":0,"put_oi":227},{"strike":41800.0,"call_gex_1pct":0.0,"put_gex_1pct":-8858065.00338038,"net_gex_1pct":-8858065.00338038,"gross_gex_1pct":8858065.00338038,"call_oi":0,"put_oi":275},{"strike":41900.0,"call_gex_1pct":0.0,"put_gex_1pct":-15639319.154251935,"net_gex_1pct":-15639319.154251935,"gross_gex_1pct":15639319.154251935,"call_oi":0,"put_oi":446},{"strike":42000.0,"call_gex_1pct":0.0,"put_gex_1pct":-56496921.12952194,"net_gex_1pct":-56496921.12952194,"gross_gex_1pct":56496921.12952194,"call_oi":0,"put_oi":1461},{"strike":42100.0,"call_gex_1pct":0.0,"put_gex_1pct":-31339930.373188056,"net_gex_1pct":-31339930.373188056,"gross_gex_1pct":31339930.373188056,"call_oi":0,"put_oi":758},{"strike":42200.0,"call_gex_1pct":0.0,"put_gex_1pct":-26310899.052309796,"net_gex_1pct":-26310899.052309796,"gross_gex_1pct":26310899.052309796,"call_oi":0,"put_oi":587},{"strike":42300.0,"call_gex_1pct":0.0,"put_gex_1pct":-28166277.186063845,"net_gex_1pct":-28166277.186063845,"gross_gex_1pct":28166277.186063845,"call_oi":0,"put_oi":567},{"strike":42400.0,"call_gex_1pct":0.0,"put_gex_1pct":-21487975.48480006,"net_gex_1pct":-21487975.48480006,"gross_gex_1pct":21487975.48480006,"call_oi":0,"put_oi":400},{"strike":42500.0,"call_gex_1pct":0.0,"put_gex_1pct":-72825135.57103671,"net_gex_1pct":-72825135.57103671,"gross_gex_1pct":72825135.57103671,"call_oi":0,"put_oi":1220},{"strike":42600.0,"call_gex_1pct":0.0,"put_gex_1pct":-30189145.03059831,"net_gex_1pct":-30189145.03059831,"gross_gex_1pct":30189145.03059831,"call_oi":0,"put_oi":472},{"strike":42700.0,"call_gex_1pct":0.0,"put_gex_1pct":-19729493.0092771,"net_gex_1pct":-19729493.0092771,"gross_gex_1pct":19729493.0092771,"call_oi":0,"put_oi":277},{"strike":42800.0,"call_gex_1pct":306936.7276929933,"put_gex_1pct":-33644690.9844067,"net_gex_1pct":-33337754.25671371,"gross_gex_1pct":33951627.71209969,"call_oi":3,"put_oi":437},{"strike":42900.0,"call_gex_1pct":0.0,"put_gex_1pct":-26516336.677755713,"net_gex_1pct":-26516336.677755713,"gross_gex_1pct":26516336.677755713,"call_oi":0,"put_oi":311},{"strike":43000.0,"call_gex_1pct":117212.57592124939,"put_gex_1pct":-239343251.80189836,"net_gex_1pct":-239226039.22597712,"gross_gex_1pct":239460464.3778196,"call_oi":1,"put_oi":2543},{"strike":43100.0,"call_gex_1pct":0.0,"put_gex_1pct":-47119683.641398974,"net_gex_1pct":-47119683.641398974,"gross_gex_1pct":47119683.641398974,"call_oi":0,"put_oi":451},{"strike":43200.0,"call_gex_1pct":2662642.4320243592,"put_gex_1pct":-67508336.56600581,"net_gex_1pct":-64845694.13398145,"gross_gex_1pct":70170978.99803017,"call_oi":20,"put_oi":579},{"strike":43300.0,"call_gex_1pct":2012083.7208181724,"put_gex_1pct":-108788462.9996962,"net_gex_1pct":-106776379.27887802,"gross_gex_1pct":110800546.72051437,"call_oi":14,"put_oi":841},{"strike":43400.0,"call_gex_1pct":5548824.360873498,"put_gex_1pct":-79930999.94005473,"net_gex_1pct":-74382175.57918122,"gross_gex_1pct":85479824.30092824,"call_oi":36,"put_oi":560},{"strike":43500.0,"call_gex_1pct":7818341.275939235,"put_gex_1pct":-199845700.7771515,"net_gex_1pct":-192027359.50121227,"gross_gex_1pct":207664042.05309072,"call_oi":47,"put_oi":1274},{"strike":43600.0,"call_gex_1pct":13090131.502464741,"put_gex_1pct":-52878278.60661153,"net_gex_1pct":-39788147.104146786,"gross_gex_1pct":65968410.10907627,"call_oi":73,"put_oi":304},{"strike":43700.0,"call_gex_1pct":17459754.88979371,"put_gex_1pct":-97154943.9883065,"net_gex_1pct":-79695189.09851278,"gross_gex_1pct":114614698.8781002,"call_oi":90,"put_oi":505},{"strike":43800.0,"call_gex_1pct":185573151.10613367,"put_gex_1pct":-122626146.97237575,"net_gex_1pct":62947004.13375792,"gross_gex_1pct":308199298.07850945,"call_oi":891,"put_oi":578},{"strike":43900.0,"call_gex_1pct":369212234.3191405,"put_gex_1pct":-156220818.77835548,"net_gex_1pct":212991415.540785,"gross_gex_1pct":525433053.097496,"call_oi":1643,"put_oi":669},{"strike":43950.0,"call_gex_1pct":929174.795117457,"put_gex_1pct":-18588701.33006779,"net_gex_1pct":-17659526.534950335,"gross_gex_1pct":19517876.125185248,"call_oi":4,"put_oi":76},{"strike":44000.0,"call_gex_1pct":409206114.0894363,"put_gex_1pct":-680589948.6885774,"net_gex_1pct":-271383834.5991411,"gross_gex_1pct":1089796062.7780137,"call_oi":1685,"put_oi":2661},{"strike":44050.0,"call_gex_1pct":10543440.649276579,"put_gex_1pct":-20442348.84645738,"net_gex_1pct":-9898908.197180802,"gross_gex_1pct":30985789.49573396,"call_oi":42,"put_oi":77},{"strike":44100.0,"call_gex_1pct":433684807.2120429,"put_gex_1pct":-162056956.05450973,"net_gex_1pct":271627851.15753317,"gross_gex_1pct":595741763.2665527,"call_oi":1672,"put_oi":581},{"strike":44150.0,"call_gex_1pct":2679333.6251847814,"put_gex_1pct":-19390970.15016204,"net_gex_1pct":-16711636.52497726,"gross_gex_1pct":22070303.775346823,"call_oi":10,"put_oi":67},{"strike":44200.0,"call_gex_1pct":391577805.20752376,"put_gex_1pct":-154693588.5077217,"net_gex_1pct":236884216.69980207,"gross_gex_1pct":546271393.7152455,"call_oi":1415,"put_oi":511},{"strike":44250.0,"call_gex_1pct":4001534.6040359237,"put_gex_1pct":-39550455.20052071,"net_gex_1pct":-35548920.59648479,"gross_gex_1pct":43551989.80455663,"call_oi":14,"put_oi":127},{"strike":44300.0,"call_gex_1pct":511077196.79225564,"put_gex_1pct":-142692587.83573875,"net_gex_1pct":368384608.95651686,"gross_gex_1pct":653769784.6279944,"call_oi":1731,"put_oi":438},{"strike":44350.0,"call_gex_1pct":7556239.215667491,"put_gex_1pct":-27422761.724385157,"net_gex_1pct":-19866522.508717667,"gross_gex_1pct":34979000.94005265,"call_oi":25,"put_oi":82},{"strike":44400.0,"call_gex_1pct":43937026.01190242,"put_gex_1pct":-186027693.07176182,"net_gex_1pct":-142090667.0598594,"gross_gex_1pct":229964719.08366424,"call_oi":138,"put_oi":538},{"strike":44450.0,"call_gex_1pct":4890580.490757849,"put_gex_1pct":-52909466.37772017,"net_gex_1pct":-48018885.886962324,"gross_gex_1pct":57800046.868478015,"call_oi":15,"put_oi":148},{"strike":44500.0,"call_gex_1pct":863844909.2632166,"put_gex_1pct":-410351240.2909659,"net_gex_1pct":453493668.9722507,"gross_gex_1pct":1274196149.5541825,"call_oi":2534,"put_oi":1105},{"strike":44550.0,"call_gex_1pct":7177836.610128956,"put_gex_1pct":-28893254.625931278,"net_gex_1pct":-21715418.015802324,"gross_gex_1pct":36071091.23606023,"call_oi":21,"put_oi":77},{"strike":44600.0,"call_gex_1pct":52186928.83593628,"put_gex_1pct":-239806042.49319896,"net_gex_1pct":-187619113.65726268,"gross_gex_1pct":291992971.32913524,"call_oi":154,"put_oi":618},{"strike":44650.0,"call_gex_1pct":12187758.669780977,"put_gex_1pct":-19406468.19128758,"net_gex_1pct":-7218709.521506604,"gross_gex_1pct":31594226.861068558,"call_oi":34,"put_oi":51},{"strike":44700.0,"call_gex_1pct":57080013.74306226,"put_gex_1pct":-193672786.63044637,"net_gex_1pct":-136592772.88738412,"gross_gex_1pct":250752800.37350863,"call_oi":159,"put_oi":490},{"strike":44750.0,"call_gex_1pct":49245696.61547757,"put_gex_1pct":-86161804.24510823,"net_gex_1pct":-36916107.62963066,"gross_gex_1pct":135407500.8605858,"call_oi":137,"put_oi":215},{"strike":44800.0,"call_gex_1pct":94227756.83500458,"put_gex_1pct":-251521516.18876782,"net_gex_1pct":-157293759.35376322,"gross_gex_1pct":345749273.0237724,"call_oi":253,"put_oi":619},{"strike":44850.0,"call_gex_1pct":94380657.62910514,"put_gex_1pct":-77001331.24330825,"net_gex_1pct":17379326.38579689,"gross_gex_1pct":171381988.8724134,"call_oi":249,"put_oi":184},{"strike":44900.0,"call_gex_1pct":133447331.64249384,"put_gex_1pct":-282970689.5724274,"net_gex_1pct":-149523357.92993355,"gross_gex_1pct":416418021.21492124,"call_oi":355,"put_oi":686},{"strike":44950.0,"call_gex_1pct":85504836.17794327,"put_gex_1pct":-69319478.63061872,"net_gex_1pct":16185357.547324553,"gross_gex_1pct":154824314.80856198,"call_oi":232,"put_oi":167},{"strike":45000.0,"call_gex_1pct":350883759.4179327,"put_gex_1pct":-494623025.2193969,"net_gex_1pct":-143739265.8014642,"gross_gex_1pct":845506784.6373296,"call_oi":927,"put_oi":1178},{"strike":45050.0,"call_gex_1pct":88400691.07730192,"put_gex_1pct":-39225344.54420499,"net_gex_1pct":49175346.53309693,"gross_gex_1pct":127626035.6215069,"call_oi":230,"put_oi":96},{"strike":45100.0,"call_gex_1pct":258756697.84822488,"put_gex_1pct":-154811651.46795386,"net_gex_1pct":103945046.38027102,"gross_gex_1pct":413568349.31617874,"call_oi":687,"put_oi":367},{"strike":45150.0,"call_gex_1pct":76306198.21578044,"put_gex_1pct":-42723101.95624449,"net_gex_1pct":33583096.259535946,"gross_gex_1pct":119029300.17202494,"call_oi":201,"put_oi":102},{"strike":45200.0,"call_gex_1pct":401787491.16147393,"put_gex_1pct":-97615009.4341379,"net_gex_1pct":304172481.72733605,"gross_gex_1pct":499402500.5956118,"call_oi":1085,"put_oi":242},{"strike":45250.0,"call_gex_1pct":77486812.55456467,"put_gex_1pct":-45491495.190112285,"net_gex_1pct":31995317.364452384,"gross_gex_1pct":122978307.74467695,"call_oi":213,"put_oi":110},{"strike":45300.0,"call_gex_1pct":420053867.85481393,"put_gex_1pct":-221324840.94965225,"net_gex_1pct":198729026.90516168,"gross_gex_1pct":641378708.8044662,"call_oi":1160,"put_oi":556},{"strike":45350.0,"call_gex_1pct":147473979.79899248,"put_gex_1pct":-22512059.65298077,"net_gex_1pct":124961920.14601171,"gross_gex_1pct":169986039.45197326,"call_oi":413,"put_oi":56},{"strike":45400.0,"call_gex_1pct":177026988.19487765,"put_gex_1pct":-57336206.17367413,"net_gex_1pct":119690782.02120352,"gross_gex_1pct":234363194.3685518,"call_oi":502,"put_oi":150},{"strike":45450.0,"call_gex_1pct":79549718.84281726,"put_gex_1pct":-19297893.601695582,"net_gex_1pct":60251825.24112168,"gross_gex_1pct":98847612.44451284,"call_oi":231,"put_oi":53},{"strike":45500.0,"call_gex_1pct":359547698.19979125,"put_gex_1pct":-121190322.56696512,"net_gex_1pct":238357375.63282615,"gross_gex_1pct":480738020.76675636,"call_oi":1076,"put_oi":342},{"strike":45550.0,"call_gex_1pct":157870064.93404344,"put_gex_1pct":-12742381.128920253,"net_gex_1pct":145127683.80512318,"gross_gex_1pct":170612446.0629637,"call_oi":487,"put_oi":37},{"strike":45600.0,"call_gex_1pct":242761021.79134962,"put_gex_1pct":-73822395.46641487,"net_gex_1pct":168938626.32493475,"gross_gex_1pct":316583417.25776446,"call_oi":767,"put_oi":221},{"strike":45650.0,"call_gex_1pct":75148603.35377814,"put_gex_1pct":-11866991.318394175,"net_gex_1pct":63281612.03538396,"gross_gex_1pct":87015594.67217231,"call_oi":244,"put_oi":36},{"strike":45700.0,"call_gex_1pct":189180983.01446858,"put_gex_1pct":-34406509.09238189,"net_gex_1pct":154774473.9220867,"gross_gex_1pct":223587492.10685048,"call_oi":637,"put_oi":109},{"strike":45750.0,"call_gex_1pct":65813683.29493005,"put_gex_1pct":-7483893.680138876,"net_gex_1pct":58329789.61479117,"gross_gex_1pct":73297576.97506893,"call_oi":230,"put_oi":25},{"strike":45800.0,"call_gex_1pct":299247814.1319451,"put_gex_1pct":-86704479.44936693,"net_gex_1pct":212543334.68257815,"gross_gex_1pct":385952293.581312,"call_oi":1090,"put_oi":307},{"strike":45850.0,"call_gex_1pct":81959532.88146332,"put_gex_1pct":-4759631.283400341,"net_gex_1pct":77199901.59806298,"gross_gex_1pct":86719164.16486366,"call_oi":310,"put_oi":18},{"strike":45900.0,"call_gex_1pct":196498393.5437944,"put_gex_1pct":-11645884.747772822,"net_gex_1pct":184852508.79602158,"gross_gex_1pct":208144278.2915672,"call_oi":775,"put_oi":47},{"strike":45950.0,"call_gex_1pct":70297764.32638866,"put_gex_1pct":-13418069.624293694,"net_gex_1pct":56879694.702094965,"gross_gex_1pct":83715833.95068236,"call_oi":290,"put_oi":59},{"strike":46000.0,"call_gex_1pct":479041956.764819,"put_gex_1pct":-20248754.76479964,"net_gex_1pct":458793202.0000194,"gross_gex_1pct":499290711.5296187,"call_oi":2072,"put_oi":94},{"strike":46050.0,"call_gex_1pct":51113353.8561671,"put_gex_1pct":-9524672.414695524,"net_gex_1pct":41588681.44147158,"gross_gex_1pct":60638026.270862624,"call_oi":232,"put_oi":55},{"strike":46100.0,"call_gex_1pct":121603400.41199291,"put_gex_1pct":-12290502.569475008,"net_gex_1pct":109312897.8425179,"gross_gex_1pct":133893902.98146792,"call_oi":581,"put_oi":75},{"strike":46150.0,"call_gex_1pct":70872988.05073616,"put_gex_1pct":-4014798.0833141347,"net_gex_1pct":66858189.96742202,"gross_gex_1pct":74887786.1340503,"call_oi":359,"put_oi":33},{"strike":46200.0,"call_gex_1pct":199915071.81971455,"put_gex_1pct":-1387749.0494495046,"net_gex_1pct":198527322.77026504,"gross_gex_1pct":201302820.86916405,"call_oi":1065,"put_oi":143},{"strike":46250.0,"call_gex_1pct":54982263.424668364,"put_gex_1pct":-63725.81826611303,"net_gex_1pct":54918537.60640225,"gross_gex_1pct":55045989.24293448,"call_oi":310,"put_oi":7},{"strike":46300.0,"call_gex_1pct":108614596.45566505,"put_gex_1pct":0.0,"net_gex_1pct":108614596.45566505,"gross_gex_1pct":108614596.45566505,"call_oi":649,"put_oi":0},{"strike":46350.0,"call_gex_1pct":40395482.8995255,"put_gex_1pct":0.0,"net_gex_1pct":40395482.8995255,"gross_gex_1pct":40395482.8995255,"call_oi":260,"put_oi":0},{"strike":46400.0,"call_gex_1pct":87072581.7309998,"put_gex_1pct":0.0,"net_gex_1pct":87072581.7309998,"gross_gex_1pct":87072581.7309998,"call_oi":589,"put_oi":0},{"strike":46450.0,"call_gex_1pct":58558436.456026375,"put_gex_1pct":0.0,"net_gex_1pct":58558436.456026375,"gross_gex_1pct":58558436.456026375,"call_oi":422,"put_oi":0},{"strike":46500.0,"call_gex_1pct":244554010.41299862,"put_gex_1pct":0.0,"net_gex_1pct":244554010.41299862,"gross_gex_1pct":244554010.41299862,"call_oi":1877,"put_oi":0},{"strike":46550.0,"call_gex_1pct":17069132.821374856,"put_gex_1pct":0.0,"net_gex_1pct":17069132.821374856,"gross_gex_1pct":17069132.821374856,"call_oi":143,"put_oi":0},{"strike":46600.0,"call_gex_1pct":54388120.68691257,"put_gex_1pct":0.0,"net_gex_1pct":54388120.68691257,"gross_gex_1pct":54388120.68691257,"call_oi":488,"put_oi":0},{"strike":46650.0,"call_gex_1pct":20396328.590574283,"put_gex_1pct":0.0,"net_gex_1pct":20396328.590574283,"gross_gex_1pct":20396328.590574283,"call_oi":200,"put_oi":0},{"strike":46700.0,"call_gex_1pct":87680801.42324547,"put_gex_1pct":0.0,"net_gex_1pct":87680801.42324547,"gross_gex_1pct":87680801.42324547,"call_oi":900,"put_oi":0},{"strike":46750.0,"call_gex_1pct":14255303.860764671,"put_gex_1pct":0.0,"net_gex_1pct":14255303.860764671,"gross_gex_1pct":14255303.860764671,"call_oi":159,"put_oi":0},{"strike":46800.0,"call_gex_1pct":125217297.11903483,"put_gex_1pct":0.0,"net_gex_1pct":125217297.11903483,"gross_gex_1pct":125217297.11903483,"call_oi":1479,"put_oi":0},{"strike":46850.0,"call_gex_1pct":9019972.886765031,"put_gex_1pct":0.0,"net_gex_1pct":9019972.886765031,"gross_gex_1pct":9019972.886765031,"call_oi":119,"put_oi":0},{"strike":46900.0,"call_gex_1pct":40462089.87037767,"put_gex_1pct":0.0,"net_gex_1pct":40462089.87037767,"gross_gex_1pct":40462089.87037767,"call_oi":561,"put_oi":0},{"strike":46950.0,"call_gex_1pct":8674925.720571497,"put_gex_1pct":0.0,"net_gex_1pct":8674925.720571497,"gross_gex_1pct":8674925.720571497,"call_oi":133,"put_oi":0},{"strike":47000.0,"call_gex_1pct":93688547.6611256,"put_gex_1pct":0.0,"net_gex_1pct":93688547.6611256,"gross_gex_1pct":93688547.6611256,"call_oi":1486,"put_oi":0},{"strike":47050.0,"call_gex_1pct":8442559.21066228,"put_gex_1pct":0.0,"net_gex_1pct":8442559.21066228,"gross_gex_1pct":8442559.21066228,"call_oi":147,"put_oi":0},{"strike":47100.0,"call_gex_1pct":20959192.097708534,"put_gex_1pct":0.0,"net_gex_1pct":20959192.097708534,"gross_gex_1pct":20959192.097708534,"call_oi":399,"put_oi":0},{"strike":47150.0,"call_gex_1pct":6109122.841701826,"put_gex_1pct":0.0,"net_gex_1pct":6109122.841701826,"gross_gex_1pct":6109122.841701826,"call_oi":124,"put_oi":0},{"strike":47200.0,"call_gex_1pct":24057563.025813133,"put_gex_1pct":0.0,"net_gex_1pct":24057563.025813133,"gross_gex_1pct":24057563.025813133,"call_oi":557,"put_oi":0},{"strike":47250.0,"call_gex_1pct":4722624.378964444,"put_gex_1pct":0.0,"net_gex_1pct":4722624.378964444,"gross_gex_1pct":4722624.378964444,"call_oi":118,"put_oi":0},{"strike":47300.0,"call_gex_1pct":25607127.008075435,"put_gex_1pct":0.0,"net_gex_1pct":25607127.008075435,"gross_gex_1pct":25607127.008075435,"call_oi":700,"put_oi":0},{"strike":47350.0,"call_gex_1pct":3618915.157238817,"put_gex_1pct":0.0,"net_gex_1pct":3618915.157238817,"gross_gex_1pct":3618915.157238817,"call_oi":102,"put_oi":0},{"strike":47400.0,"call_gex_1pct":9717031.799854917,"put_gex_1pct":0.0,"net_gex_1pct":9717031.799854917,"gross_gex_1pct":9717031.799854917,"call_oi":299,"put_oi":0},{"strike":47450.0,"call_gex_1pct":1811049.3441872783,"put_gex_1pct":0.0,"net_gex_1pct":1811049.3441872783,"gross_gex_1pct":1811049.3441872783,"call_oi":58,"put_oi":0},{"strike":47500.0,"call_gex_1pct":27308740.19250931,"put_gex_1pct":0.0,"net_gex_1pct":27308740.19250931,"gross_gex_1pct":27308740.19250931,"call_oi":910,"put_oi":0},{"strike":47550.0,"call_gex_1pct":1651207.683100488,"put_gex_1pct":0.0,"net_gex_1pct":1651207.683100488,"gross_gex_1pct":1651207.683100488,"call_oi":64,"put_oi":0},{"strike":47600.0,"call_gex_1pct":6044365.372072233,"put_gex_1pct":0.0,"net_gex_1pct":6044365.372072233,"gross_gex_1pct":6044365.372072233,"call_oi":241,"put_oi":0},{"strike":47650.0,"call_gex_1pct":653670.7297466861,"put_gex_1pct":0.0,"net_gex_1pct":653670.7297466861,"gross_gex_1pct":653670.7297466861,"call_oi":28,"put_oi":0},{"strike":47700.0,"call_gex_1pct":3156530.2228755183,"put_gex_1pct":0.0,"net_gex_1pct":3156530.2228755183,"gross_gex_1pct":3156530.2228755183,"call_oi":151,"put_oi":0},{"strike":47750.0,"call_gex_1pct":1509031.855850196,"put_gex_1pct":0.0,"net_gex_1pct":1509031.855850196,"gross_gex_1pct":1509031.855850196,"call_oi":77,"put_oi":0},{"strike":47800.0,"call_gex_1pct":5972658.959670757,"put_gex_1pct":0.0,"net_gex_1pct":5972658.959670757,"gross_gex_1pct":5972658.959670757,"call_oi":313,"put_oi":0},{"strike":47850.0,"call_gex_1pct":667822.6499623199,"put_gex_1pct":0.0,"net_gex_1pct":667822.6499623199,"gross_gex_1pct":667822.6499623199,"call_oi":41,"put_oi":0},{"strike":47900.0,"call_gex_1pct":3923697.183473355,"put_gex_1pct":0.0,"net_gex_1pct":3923697.183473355,"gross_gex_1pct":3923697.183473355,"call_oi":268,"put_oi":0},{"strike":47950.0,"call_gex_1pct":1556911.7627896417,"put_gex_1pct":0.0,"net_gex_1pct":1556911.7627896417,"gross_gex_1pct":1556911.7627896417,"call_oi":116,"put_oi":0},{"strike":48000.0,"call_gex_1pct":56989521.69694063,"put_gex_1pct":0.0,"net_gex_1pct":56989521.69694063,"gross_gex_1pct":56989521.69694063,"call_oi":4503,"put_oi":0},{"strike":48050.0,"call_gex_1pct":1817461.1048855078,"put_gex_1pct":0.0,"net_gex_1pct":1817461.1048855078,"gross_gex_1pct":1817461.1048855078,"call_oi":165,"put_oi":0},{"strike":48100.0,"call_gex_1pct":1933922.2917873336,"put_gex_1pct":0.0,"net_gex_1pct":1933922.2917873336,"gross_gex_1pct":1933922.2917873336,"call_oi":188,"put_oi":0},{"strike":48150.0,"call_gex_1pct":641580.1193317528,"put_gex_1pct":0.0,"net_gex_1pct":641580.1193317528,"gross_gex_1pct":641580.1193317528,"call_oi":67,"put_oi":0},{"strike":48200.0,"call_gex_1pct":4573130.205017314,"put_gex_1pct":0.0,"net_gex_1pct":4573130.205017314,"gross_gex_1pct":4573130.205017314,"call_oi":515,"put_oi":0},{"strike":48250.0,"call_gex_1pct":311478.69453084463,"put_gex_1pct":0.0,"net_gex_1pct":311478.69453084463,"gross_gex_1pct":311478.69453084463,"call_oi":38,"put_oi":0},{"strike":48300.0,"call_gex_1pct":6937632.819425732,"put_gex_1pct":0.0,"net_gex_1pct":6937632.819425732,"gross_gex_1pct":6937632.819425732,"call_oi":988,"put_oi":0},{"strike":48350.0,"call_gex_1pct":196715.69841200035,"put_gex_1pct":0.0,"net_gex_1pct":196715.69841200035,"gross_gex_1pct":196715.69841200035,"call_oi":31,"put_oi":0},{"strike":48400.0,"call_gex_1pct":2835947.0842137993,"put_gex_1pct":0.0,"net_gex_1pct":2835947.0842137993,"gross_gex_1pct":2835947.0842137993,"call_oi":500,"put_oi":0},{"strike":48500.0,"call_gex_1pct":4904398.306056055,"put_gex_1pct":0.0,"net_gex_1pct":4904398.306056055,"gross_gex_1pct":4904398.306056055,"call_oi":1004,"put_oi":0},{"strike":48600.0,"call_gex_1pct":486891.6843500997,"put_gex_1pct":0.0,"net_gex_1pct":486891.6843500997,"gross_gex_1pct":486891.6843500997,"call_oi":118,"put_oi":0},{"strike":48700.0,"call_gex_1pct":331956.14582590485,"put_gex_1pct":0.0,"net_gex_1pct":331956.14582590485,"gross_gex_1pct":331956.14582590485,"call_oi":84,"put_oi":0},{"strike":48800.0,"call_gex_1pct":803319.2958913305,"put_gex_1pct":0.0,"net_gex_1pct":803319.2958913305,"gross_gex_1pct":803319.2958913305,"call_oi":212,"put_oi":0},{"strike":48900.0,"call_gex_1pct":352817.12671385065,"put_gex_1pct":0.0,"net_gex_1pct":352817.12671385065,"gross_gex_1pct":352817.12671385065,"call_oi":97,"put_oi":0},{"strike":49000.0,"call_gex_1pct":1827917.4257516998,"put_gex_1pct":0.0,"net_gex_1pct":1827917.4257516998,"gross_gex_1pct":1827917.4257516998,"call_oi":523,"put_oi":0},{"strike":49100.0,"call_gex_1pct":161362.57923047806,"put_gex_1pct":0.0,"net_gex_1pct":161362.57923047806,"gross_gex_1pct":161362.57923047806,"call_oi":48,"put_oi":0},{"strike":49200.0,"call_gex_1pct":103568.55353433611,"put_gex_1pct":0.0,"net_gex_1pct":103568.55353433611,"gross_gex_1pct":103568.55353433611,"call_oi":32,"put_oi":0},{"strike":49300.0,"call_gex_1pct":152820.3758917058,"put_gex_1pct":0.0,"net_gex_1pct":152820.3758917058,"gross_gex_1pct":152820.3758917058,"call_oi":49,"put_oi":0},{"strike":49400.0,"call_gex_1pct":13186708.779702162,"put_gex_1pct":0.0,"net_gex_1pct":13186708.779702162,"gross_gex_1pct":13186708.779702162,"call_oi":4384,"put_oi":0},{"strike":49500.0,"call_gex_1pct":510478.9945761171,"put_gex_1pct":0.0,"net_gex_1pct":510478.9945761171,"gross_gex_1pct":510478.9945761171,"call_oi":252,"put_oi":0},{"strike":49600.0,"call_gex_1pct":78243.41704607673,"put_gex_1pct":0.0,"net_gex_1pct":78243.41704607673,"gross_gex_1pct":78243.41704607673,"call_oi":40,"put_oi":0},{"strike":49700.0,"call_gex_1pct":26464.16491135696,"put_gex_1pct":0.0,"net_gex_1pct":26464.16491135696,"gross_gex_1pct":26464.16491135696,"call_oi":14,"put_oi":0},{"strike":49800.0,"call_gex_1pct":42045.40650281527,"put_gex_1pct":0.0,"net_gex_1pct":42045.40650281527,"gross_gex_1pct":42045.40650281527,"call_oi":23,"put_oi":0},{"strike":49900.0,"call_gex_1pct":27713.850958456776,"put_gex_1pct":0.0,"net_gex_1pct":27713.850958456776,"gross_gex_1pct":27713.850958456776,"call_oi":21,"put_oi":0},{"strike":50000.0,"call_gex_1pct":1263639.150449218,"put_gex_1pct":0.0,"net_gex_1pct":1263639.150449218,"gross_gex_1pct":1263639.150449218,"call_oi":989,"put_oi":0},{"strike":50100.0,"call_gex_1pct":6189.143677733298,"put_gex_1pct":0.0,"net_gex_1pct":6189.143677733298,"gross_gex_1pct":6189.143677733298,"call_oi":5,"put_oi":0},{"strike":50200.0,"call_gex_1pct":16515.906868806327,"put_gex_1pct":0.0,"net_gex_1pct":16515.906868806327,"gross_gex_1pct":16515.906868806327,"call_oi":23,"put_oi":0},{"strike":50300.0,"call_gex_1pct":17407.183775443023,"put_gex_1pct":0.0,"net_gex_1pct":17407.183775443023,"gross_gex_1pct":17407.183775443023,"call_oi":25,"put_oi":0},{"strike":50400.0,"call_gex_1pct":36479.891256927476,"put_gex_1pct":0.0,"net_gex_1pct":36479.891256927476,"gross_gex_1pct":36479.891256927476,"call_oi":54,"put_oi":0},{"strike":50500.0,"call_gex_1pct":43939.380122661976,"put_gex_1pct":0.0,"net_gex_1pct":43939.380122661976,"gross_gex_1pct":43939.380122661976,"call_oi":67,"put_oi":0},{"strike":50600.0,"call_gex_1pct":5095.980445451308,"put_gex_1pct":0.0,"net_gex_1pct":5095.980445451308,"gross_gex_1pct":5095.980445451308,"call_oi":8,"put_oi":0},{"strike":50700.0,"call_gex_1pct":1857.1570530457197,"put_gex_1pct":0.0,"net_gex_1pct":1857.1570530457197,"gross_gex_1pct":1857.1570530457197,"call_oi":3,"put_oi":0},{"strike":50800.0,"call_gex_1pct":2407.6871149582275,"put_gex_1pct":0.0,"net_gex_1pct":2407.6871149582275,"gross_gex_1pct":2407.6871149582275,"call_oi":4,"put_oi":0},{"strike":50900.0,"call_gex_1pct":8197.781499693376,"put_gex_1pct":0.0,"net_gex_1pct":8197.781499693376,"gross_gex_1pct":8197.781499693376,"call_oi":14,"put_oi":0},{"strike":51000.0,"call_gex_1pct":1331305.7913306574,"put_gex_1pct":0.0,"net_gex_1pct":1331305.7913306574,"gross_gex_1pct":1331305.7913306574,"call_oi":2336,"put_oi":0},{"strike":51100.0,"call_gex_1pct":6104.301802494202,"put_gex_1pct":0.0,"net_gex_1pct":6104.301802494202,"gross_gex_1pct":6104.301802494202,"call_oi":11,"put_oi":0},{"strike":51200.0,"call_gex_1pct":3243.6059025213117,"put_gex_1pct":0.0,"net_gex_1pct":3243.6059025213117,"gross_gex_1pct":3243.6059025213117,"call_oi":6,"put_oi":0},{"strike":51300.0,"call_gex_1pct":1580.595134233348,"put_gex_1pct":0.0,"net_gex_1pct":1580.595134233348,"gross_gex_1pct":1580.595134233348,"call_oi":3,"put_oi":0},{"strike":51500.0,"call_gex_1pct":3006.3506885726056,"put_gex_1pct":0.0,"net_gex_1pct":3006.3506885726056,"gross_gex_1pct":3006.3506885726056,"call_oi":6,"put_oi":0},{"strike":51600.0,"call_gex_1pct":38136.29425068336,"put_gex_1pct":0.0,"net_gex_1pct":38136.29425068336,"gross_gex_1pct":38136.29425068336,"call_oi":78,"put_oi":0}]}
```

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
- 資料日期：2026-11-02；資料時間：2026-11-03 08:55:11；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：futures.futures.night.settle, futures.futures.night.oi, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-11-02 非今日 2026-11-03，視為無新節次，不採用
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
- margin_ratio：`TWSE 上市自建估算（資料日期：2026-11-02；估值 1239 檔；6 檔採最近有效收盤價（價格日期 20260402 至 20261102）；Blave 同 T0 交叉驗證 171.7110%，差異 0.007 個百分點）`
- sbl_bal：`TWSE TWT96U + TWT96U GRETAI（上櫃） + TPEX margin_sbl`
- sbl_sale_bal：`TPEX margin_sbl`
- sbl_sale_chg：`TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市市場維持率以 TWSE 自建計算為主；6 檔採最近有效收盤價（價格日期 20260402 至 20261102）。Blave 同 T0 交叉驗證 171.7110%，差異 0.007 個百分點。Blave 不可用不影響 DATA_REPORT 產出。
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
