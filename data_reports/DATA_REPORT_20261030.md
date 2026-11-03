# DATA_REPORT_20261030

- 報告日期：`2026-11-03`
- T0 交易日期：`2026-10-30`
- 資料產出時間：`2026-11-03 18:40:23`
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
| 加權指數 | 45,211.83 | 點 | twse-proxy |
| 開盤 | 46,139.79 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,139.79 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 44,726.26 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 45,211.83 | 點 | twse-proxy |
| 漲跌點數 | -1,156.50 | 點 | twse-proxy |
| 漲跌幅 | -2.49 | % | twse-proxy |
| 成交金額 | 9,396.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 92 | twse-proxy |
| 下跌家數 | 941 | twse-proxy |
| 平盤家數 | 45 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 11 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 127 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 691 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 56 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 14 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 7 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,073.1 | 億元 | twse-proxy /institutional |
| 投信 | +199.0 | 億元 | twse-proxy /institutional |
| 自營商 | -590.6 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,464.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,287.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -151.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 233,537 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 7,084 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 171.75 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,525,111 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,178 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,273 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,396.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,987.7 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 9,396.1 | 億元 | twse-proxy market_statistics+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,541.40 | -38.67 | -0.51 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,164.31 | -272.69 | -1.07 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,989.82 | -395.03 | -1.39 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,983.98 | 213.67 | +0.41 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,328.33 | -360.47 | -3.37 | Yahoo Finance Chart API |
| VIX | ^VIX | 21.31 | 0.16 | +0.76 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,081.86 | -208.25 | -0.33 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,648.79 | -210.29 | -3.59 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,525.97 | 132.65 | +0.57 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,608.10 | -29.93 | -0.82 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,876.99 | -133.69 | -1.21 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,570.00 | -4.50 | -0.06 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,231.75 | 104.25 | +0.37 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,848.00 | -285.00 | -0.55 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,816.70 | -1.10 | -0.04 | Yahoo Finance Chart API |

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
| USD/TWD | TWD=X | 32.79 | 0.19 | +0.57 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.81 | 0.06 | +0.05 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.18 | 0.50 | +0.32 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.98 | 18.46 | +1.39 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 97.77 | 1.31 | +1.36 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,912.10 | -57.50 | -1.45 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,870.69 | 193.39 | +0.25 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：金管會證實 永豐銀419人受害遭盜轉走4千多萬
  - 來源：Yahoo 台股；發布時間：2026-11-03T09:03:29Z；台北時間：2026-11-03 17:03
  - 摘要：永豐金（2890）旗下永豐銀行今（3日）驚傳嚴重的網銀資安疑慮，多名用戶在未開啟手機APP的情況下，帳戶竟無故遭轉出新台幣10萬元。銀行局副局長王允中今（3）日下午被詢問時證實已接獲銀行通知，被匯入的北富銀帳戶已暫時凍結、永豐金新APP先下
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B0%B8%E8%B1%90%E9%8A%80%E8%A1%8C%E7%B3%BB%E7%B5%B1%E5%87%BA%E5%8C%85%EF%BC%81%E9%A9%9A%E7%88%86%E9%9B%86%E5%9C%98%E7%9B%9C%E8%BD%8910%E8%90%AC%E5%85%83-%E9%87%91%E7%AE%A1%E6%9C%83%E8%AD%89%E5%AF%A6%E3%80%8C419%E4%BA%BA%E5%8F%97%E5%BD%B1%E9%9F%BF4%E5%8D%83%E5%A4%9A%E8%90%AC%E5%85%83%E3%80%8D-091458126.html
- 事件3：永和房價登百萬 漢皇集團千戶公辦都更正式簽約
  - 來源：Yahoo 台股；發布時間：2026-11-03T08:30:00Z；台北時間：2026-11-03 16:30
  - 摘要：新北市永和頂溪捷運站周邊公辦都更案正式邁入實施階段。漢皇集團旗下漢庭營造今（3）日與新北市住宅及都市更新中心簽訂「新北市頂溪捷運周邊地區公辦都市更新案（A區）」實施者契約，由新北市長侯友宜出席見證。全案基地約5,000坪，規劃興建地上35層
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B0%B8%E5%92%8C%E6%88%BF%E5%83%B9%E6%8C%BA%E9%80%B2%E7%99%BE%E8%90%AC%E4%BF%B1%E6%A8%82%E9%83%A8-%E6%BC%A2%E7%9A%87400%E5%84%84%E9%A0%82%E6%BA%AA%E5%85%AC%E8%BE%A6%E9%83%BD%E6%9B%B4%E7%B0%BD%E7%B4%84-083000093.html
- 事件4：移工十年就能領勞退？勞動部澄清
  - 來源：Yahoo 台股；發布時間：2026-11-03T06:48:58Z；台北時間：2026-11-03 14:48
  - 摘要：社群媒體近日流傳「移工在台工作11年118天即可領百萬元退休金」的說法，勞動部澄清為錯誤訊息。產業移工適用勞退舊制，須符合年資與年齡門檻並受留台期限限制，並非工作滿10年就能請領；雇主提撥退休準備金也不代表移工即可領取。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%B6%B2%E5%82%B3%E7%A7%BB%E5%B7%A5-%E5%B7%A5%E4%BD%9C10%E5%B9%B4%E5%B0%B1%E9%A0%98%E7%99%BE%E8%90%AC%E9%80%80%E4%BC%91%E9%87%91-%E5%8B%9E%E5%8B%95%E9%83%A8-%E9%8C%AF%E8%AA%A4%E8%A8%8A%E6%81%AF-064858384.html
- 事件5：配息創高00878太貴不敢追 達人看「息利雙收」有機會
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:28:00Z；台北時間：2026-11-03 11:28
  - 摘要：高股息ETF再傳配息利多！擁有大量存股族的國泰永續高股息（00878）公布最新一期預估配息，每單位擬配發1.25元，創下單季配息新高。不過，00878股價已逼近35.75元的歷史高點，讓不少尚未進場的投資人猶豫是否追買。投資達人《股票分析情
  - 原文連結：https://tw.stock.yahoo.com/news/00878%E9%85%8D%E6%81%AF%E5%89%B5%E6%96%B0%E9%AB%98-%E9%81%94%E4%BA%BA%E6%9B%9D1%E6%8B%9B-%E6%81%AF%E5%88%A9%E9%9B%99%E6%94%B6-%E7%B5%95%E4%B8%8D%E6%9C%83%E6%8B%96%E5%A4%AA%E4%B9%85-032800131.html
- 事件6：外資連砍四天何時轉多 分析師畫出空單水位關鍵線
  - 來源：Yahoo 台股；發布時間：2026-11-03T07:06:47Z；台北時間：2026-11-03 15:06
  - 摘要：台股失守4萬4大關，收在43,307點，三大法人今（3）日合計賣超台股1464.56億元，其中外資再砍1073.06億元，砍出歷史第八大賣超金額，連4賣累計提款3621億元。資深證券分析師呂漢威指出，外資押注美國期中選舉波動，不僅現貨賣超、
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90follow%E6%B3%95%E4%BA%BA%E3%80%91%E5%A4%96%E8%B3%87%E5%86%8D%E6%8F%90%E6%AC%BE%E5%8F%B0%E7%A9%8D%E9%9B%BB273%E5%84%84%E5%85%83%EF%BC%81%E5%90%8C%E6%AD%A5%E7%A0%8D%E8%8F%AF%E9%82%A6%E9%9B%BB%E3%80%81%E5%8A%9B%E7%A9%8D%E9%9B%BB%E5%90%84%E9%80%BE3%E8%90%AC%E5%BC%B5-%E5%8F%8D%E6%89%8B%E6%95%B2%E9%80%B2%E5%8F%B0%E7%8E%BB-082856644.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Feeling isolated? Half of in-office workers describe their desk jobs as 'remote,' NY Fed survey finds
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 02:31:00 GMT；台北時間：2026-11-03 10:31
  - 摘要：Employees describing jobs as 'remote' are now often in-office, as companies fail to create the collaboration they claim is critical, NY Fed research s
  - 原文連結：https://www.cnbc.com/2026/11/02/remote-work-in-office-mandate-new-york-fed.html
- 事件10：Australia hikes rates to 18-year high to fight inflation
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 03:46:20 GMT；台北時間：2026-11-03 11:46
  - 摘要：The Reserve Bank of Australia's decision was in line with expectations from economists polled by Reuters, and marked its fifth rate increase this year
  - 原文連結：https://www.cnbc.com/2026/11/03/australia-hikes-rates-18-year-high-finflation.html
- 事件11：Oil prices climb after U.S. strikes Iran's Qeshm Island
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 09:58:37 GMT；台北時間：2026-11-03 17:58
  - 摘要：The rebound in oil prices come a day after the U.S. and Iranian presidents signalled they are open to a diplomatic solution to Iran war.
  - 原文連結：https://www.cnbc.com/2026/11/03/oil-prices-climb-after-us-reportedly-strikes-irans-qeshm-island.html
- 事件12：Jim Cramer says these six fashion stocks are buys beyond the AI trade
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 23:54:27 GMT；台北時間：2026-11-03 07:54
  - 摘要：While technology stocks have come under pressure in recent weeks, consumer stocks have been resilient.
  - 原文連結：https://www.cnbc.com/2026/11/02/jim-cramer-fashion-stocks.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-30

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
| 開盤價 | 45,395 | TAIFEX Proxy |
| 最高價 | 45,420 | TAIFEX Proxy |
| 最低價 | 44,052 | TAIFEX Proxy |
| 收盤價 | 44,433 | TAIFEX Proxy |
| 漲跌點數 | -867 | TAIFEX Proxy |
| 漲跌幅 | -1.91 | TAIFEX Proxy |
| 成交量 | 44,305 | TAIFEX Proxy |
| 夜盤高點及低點 | 45,420 / 44,052 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 6,528 | TAIFEX Proxy |
| 外資空方 OI | 98,769 | TAIFEX Proxy |
| 外資多空淨 OI | -92,241 | TAIFEX Proxy |
| 投信多方 OI | 92,025 | TAIFEX Proxy |
| 投信空方 OI | 2,814 | TAIFEX Proxy |
| 投信多空淨 OI | +89,211 | TAIFEX Proxy |
| 自營商多方 OI | 6,106 | TAIFEX Proxy |
| 自營商空方 OI | 4,370 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,736 | TAIFEX Proxy |
| 三大法人合計多方 OI | 104,659 | TAIFEX Proxy |
| 三大法人合計空方 OI | 105,953 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -1,294 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,719 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,993 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +225 | TAIFEX Proxy |

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
| 外資日盤多單交易量 | 68,904 | TAIFEX Proxy |
| 外資日盤空單交易量 | 71,286 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,382 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 26,142 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 24,777 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,365 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,145 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -2,141 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,993 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +2,625 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +246 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -141 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,898 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,611 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -169.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +144.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,376 | TAIFEX Proxy |
| 加權指數價格 | 45,211.83 | twse-proxy |
| 台指期與加權指數價差 | -1,835.83 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -4.06 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -1,835.83 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +1,057 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,376 | 44,433 | -1,057 | TAIFEX Proxy |
| 成交量 | 78,044 | 44,305 | +33,739 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-501（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 68,904 | 71,286 | -2,382 | 26,142 | 24,777 | +1,365 | -3,145 | 6,528 | 98,769 | -92,241 | -2,719 | TAIFEX Proxy |
| 投信 | 82 | 2,223 | -2,141 | 0 | 0 | +0 | +1,993 | 92,025 | 2,814 | +89,211 | +1,993 | TAIFEX Proxy |
| 自營商 | 9,523 | 6,898 | +2,625 | 887 | 641 | +246 | -141 | 6,106 | 4,370 | +1,736 | +225 | TAIFEX Proxy |
| 三大法人合計 | 78,509 | 80,407 | -1,898 | 27,029 | 25,418 | +1,611 | -1,293 | 104,659 | 105,953 | -1,294 | -501 | TAIFEX Proxy |

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
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 36.21% | TAIFEX Proxy |
| 夜盤漲跌點數 | -867 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,365 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-30 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F5 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-03 18:40:23 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 397,427 | TAIFEX Proxy |
| Call 總未平倉量 OI | 98,551 | TAIFEX Proxy |
| Call OI 增減 (2026-10-29→2026-10-30) | +36,035 | TAIFEX Proxy snapshots (2026-10-29) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 376,322 | TAIFEX Proxy |
| Put 總未平倉量 OI | 59,945 | TAIFEX Proxy |
| Put OI 增減 (2026-10-29→2026-10-30) | +24,893 | TAIFEX Proxy snapshots (2026-10-29) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.06 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.64 | TAIFEX Proxy |
| Put／Call Ratio | 0.61 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-30→2026-11-02) | 2.84 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-30→2026-11-02) | -1.01 | TAIFEX Proxy |
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
| 外資 Call夜買 | 27,173 | TAIFEX Proxy |
| 外資 Call夜賣 | 27,381 | TAIFEX Proxy |
| 外資 Call夜淨 | -208 | TAIFEX Proxy |
| 外資 Put夜買 | 25,389 | TAIFEX Proxy |
| 外資 Put夜賣 | 25,019 | TAIFEX Proxy |
| 外資 Put夜淨 | +370 | TAIFEX Proxy |
| 外資 日盤淨總量 | +341 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,597 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +678 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 67,095 | TAIFEX Proxy |
| 自營商 Call日賣 | 74,800 | TAIFEX Proxy |
| 自營商 Call日淨 | -7,705 | TAIFEX Proxy |
| 自營商 Put日買 | 60,242 | TAIFEX Proxy |
| 自營商 Put日賣 | 56,499 | TAIFEX Proxy |
| 自營商 Put日淨 | +3,743 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,778 | TAIFEX Proxy |
| 自營商 Call夜賣 | 13,663 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,885 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,623 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,864 | TAIFEX Proxy |
| 自營商 Put夜淨 | +759 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,448 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -4,820 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +2,984 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 4,116 | TAIFEX Proxy |
| Call OI 第2大履約價 | 45,300 | 4,005 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,200 | 3,905 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 4,116 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 4,116 | 4.18% | TAIFEX Proxy |
| C2 | 45,300 | 4,005 | 4.06% | TAIFEX Proxy |
| C3 | 49,200 | 3,905 | 3.96% | TAIFEX Proxy |
| C4 | 45,400 | 3,662 | 3.72% | TAIFEX Proxy |
| C5 | 45,200 | 3,499 | 3.55% | TAIFEX Proxy |
| C6 | 45,500 | 3,446 | 3.5% | TAIFEX Proxy |
| C7 | 47,000 | 3,364 | 3.41% | TAIFEX Proxy |
| C8 | 46,000 | 3,188 | 3.23% | TAIFEX Proxy |
| C9 | 45,600 | 2,845 | 2.89% | TAIFEX Proxy |
| C10 | 46,600 | 2,271 | 2.3% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 45,000 | 3,910 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,200 | 3,659 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,250 | 2,871 | TAIFEX Proxy |
| Put OI 最大履約價 | 45,000 | 3,910 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 45,000 | 3,910 | 6.52% | TAIFEX Proxy |
| P2 | 45,200 | 3,659 | 6.1% | TAIFEX Proxy |
| P3 | 45,250 | 2,871 | 4.79% | TAIFEX Proxy |
| P4 | 45,100 | 2,653 | 4.43% | TAIFEX Proxy |
| P5 | 44,500 | 2,484 | 4.14% | TAIFEX Proxy |
| P6 | 46,000 | 2,336 | 3.9% | TAIFEX Proxy |
| P7 | 45,300 | 2,128 | 3.55% | TAIFEX Proxy |
| P8 | 44,800 | 1,875 | 3.13% | TAIFEX Proxy |
| P9 | 44,900 | 1,792 | 2.99% | TAIFEX Proxy |
| P10 | 44,000 | 1,542 | 2.57% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 45,300 (+3,205) | TAIFEX Proxy snapshots (2026-10-29) |
| Call OI 減少最多的履約價 | 47,300 (-587) | TAIFEX Proxy snapshots (2026-10-29) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 45,200 (+2,632) | TAIFEX Proxy snapshots (2026-10-29) |
| Put OI 減少最多的履約價 | 45,500 (-958) | TAIFEX Proxy snapshots (2026-10-29) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | -1,000 | TAIFEX Proxy snapshots (2026-10-29) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 44,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 44,049.22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 45,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | -600 | TAIFEX Proxy snapshots (2026-10-29) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 140,211 | 139,870 | +341 | 41,871 | 41,965 | -94 | +6,718 | TAIFEX Proxy |
| 投信 | 200 | 5,246 | -5,046 | 0 | 0 | +0 | -4,937 | TAIFEX Proxy |
| 自營商 | 123,594 | 135,042 | -11,448 | 21,826 | 23,217 | -1,391 | +2,733 | TAIFEX Proxy |
| 三大法人合計 | 264,005 | 280,158 | -16,153 | 63,697 | 65,182 | -1,485 | +4,514 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 14.35 | 14.07 | +0.28 | 4.82 | 4.93 | -0.11 | +0.39 | TAIFEX Proxy |
| 投信 | 0.02 | 1.37 | -1.35 | 0.00 | 0.00 | +0 | -1.35 | TAIFEX Proxy |
| 自營商 | 12.87 | 13.70 | -0.83 | 2.18 | 2.48 | -0.30 | -0.53 | TAIFEX Proxy |
| 三大法人合計 | 27.23 | 29.13 | -1.90 | 7.00 | 7.41 | -0.41 | -1.49 | TAIFEX Proxy |

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
- 資料日期：2026-10-30；資料時間：2026-11-03 18:40:23；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：64 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：238 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (12)：otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, sbl.sale_bal, sbl.sale_chg, turnover.otc, futures.gamma_wall, futures.gamma_flip, futures.gamma_wall, futures.gamma_flip
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-03，非 T0 2026-10-30)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-03 非今日 2026-11-02，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-03 非今日 2026-11-02，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-03 非今日 2026-11-02，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`stockintelli 大盤融資維持率 (民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151103, T0=1151030)
- 註記：三大法人回傳日期 20261103 (T0 20261030)，採用最新可得
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,073.1 | -92,241 | -2,382 | +1,365 | +341 | -94 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +199.0 | +89,211 | -2,141 | +0 | -5,046 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -590.6 | +1,736 | +2,625 | +246 | -11,448 | -1,391 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
