# DATA_REPORT_20261030

- 報告日期：`2026-11-03`
- T0 交易日期：`2026-10-30`
- 資料產出時間：`2026-11-03 21:26:27`
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
| 上漲家數 | 127 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 下跌家數 | 691 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 平盤家數 | 56 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 漲停家數 | 14 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
| 跌停家數 | 7 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,073.1 | 億元 | twse-proxy /institutional |
| 投信 | +184.6 | 億元 | twse-proxy /institutional |
| 自營商 | -590.5 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,479.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `TWSE 上市自建估算（資料日期：2026-10-30；估值 1238 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）；Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,287.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -151.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 233,537 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 7,084 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 171.75 | % | TWSE 上市自建估算（資料日期：2026-10-30；估值 1238 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）；Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,525,111 | 張 | TWSE TWT96U + TWT96U GRETAI（上櫃） |
| 借券賣出餘額 | 36,178 | 張 | 沿用前版（原來源：TWSE TWT93U + TPEX margin_sbl） |
| 借券賣出增減 | -1,273 | 張 | 沿用前版（原來源：TWSE TWT93U + TPEX margin_sbl） |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,396.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,987.7 | 億元 | 沿用前版（原來源：TPEX OpenAPI tpex_mainborad_highlight） |
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
| VIX | ^VIX | 21.47 | 0.32 | +1.51 | Yahoo Finance Chart API |

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
| S&P500期貨 | ES=F | 7,562.75 | -11.75 | -0.16 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,214.00 | 86.50 | +0.31 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,747.00 | -386.00 | -0.74 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,817.00 | -0.80 | -0.03 | Yahoo Finance Chart API |

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
| USD/TWD | TWD=X | 32.78 | 0.17 | +0.53 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.83 | 0.08 | +0.08 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.18 | 0.50 | +0.32 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.62 | 18.10 | +1.37 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 97.31 | 0.85 | +0.88 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,945.10 | -24.50 | -0.62 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 77,366.19 | 688.89 | +0.90 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：台股血崩誰撐場 資安股集體紅燈、台玻逆襲有原因
  - 來源：Yahoo 台股；發布時間：2026-11-03T09:08:12Z；台北時間：2026-11-03 17:08
  - 摘要：電子金融齊倒，台股重挫1612點、失守4萬4！今(3)日加權指數終場下跌1,612.60點、跌幅3.59%，收43,307.54點，創史上第七大單日收盤跌點，指數持續位於周線、月線之下，成交金額9,301.54億元。市場對AI投資回報與估值
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%8F%B2%E4%B8%8A%E7%AC%AC%E5%85%AB%E5%A4%A7%E8%B3%A3%E8%B6%85%E7%A0%8D%E5%87%BA%E5%8F%B0%E8%82%A1%E7%AC%AC%E4%B8%83%E5%A4%A7%E8%B7%8C%E9%BB%9E%EF%BC%81%E3%80%8C%E9%9B%BB%E9%87%91%E3%80%8D%E7%B6%A0%E6%B2%B9%E6%B2%B9-%E8%B3%87%E5%AE%89%E8%82%A1%E4%BA%AE%E4%B8%80%E6%8E%92%E7%B4%85%E7%87%88%E6%88%90%E9%81%BF%E9%A2%A8%E6%B8%AF%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090812427.html
- 事件3：穩定幣不是有錢就能發 科技業想入場先過金管會兩關
  - 來源：Yahoo 台股；發布時間：2026-11-03T09:30:54Z；台北時間：2026-11-03 17:30
  - 摘要：金管會今（3）日正式公布穩定幣發行辦法，過去有科技業想利用穩定幣加速匯款，對切入全球供應鍊金融興趣十足！銀行局副局長王允中今（3）日正式宣示，對非銀行的業者（如科技業）想發行穩定幣設立二道門檻，需與金融業設合資子公司才行，且持有股權不得過半
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%A7%91%E6%8A%80%E6%A5%AD%E6%83%B3%E7%99%BC%E7%A9%A9%E5%AE%9A%E5%B9%A3-%E9%87%91%E7%AE%A1%E6%9C%83%E8%A8%AD2%E9%96%80%E6%AA%BB%EF%BC%9A%E9%9C%80%E8%88%87%E9%87%91%E8%9E%8D%E6%A5%AD%E5%90%88%E8%B3%87%E3%80%81%E8%82%A1%E6%AC%8A%E4%B8%8D%E9%81%8E%E5%8D%8A-093054386.html
- 事件4：網喊「基本麵吃到吐」金管會回應揭三大下跌原因
  - 來源：Yahoo 台股；發布時間：2026-11-03T10:02:18Z；台北時間：2026-11-03 18:02
  - 摘要：台股暴跌如何信心喊話？過去每逢股市大跌，金管會上市櫃公司營收、殖利率等「基本面」等數字充利多，被PTT網友以「吃麵」諧音梗嘲諷「麵都吃到吐了」。美期中選舉前夕，台股3日暴跌1,612.60點，寫史上第七大跌點，加權指數收43,307.54點
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%9A%B4%E8%B7%8C%E5%8F%88%E7%AB%AF%E3%80%8C%E5%9F%BA%E6%9C%AC%E9%BA%B5%E3%80%8D%EF%BC%81%E9%87%91%E7%AE%A1%E6%9C%83%E9%A6%96%E5%9B%9E%E6%87%89%EF%BC%9A%E4%BF%A1%E5%BF%83%E5%96%8A%E8%A9%B1%E3%80%8C%E9%A1%8C%E6%9D%90%E6%9C%89%E9%99%90%E3%80%8D-100218585.html
- 事件5：權證愈跌愈買恐等到歸零 加碼前先做三項檢查
  - 來源：Yahoo 台股；發布時間：2026-11-03T07:04:32Z；台北時間：2026-11-03 15:04
  - 摘要：在股票投資中，「逢低加碼、攤平成本」是許多存股族與波段交易者常見的操作策略；然而，當這個習慣被帶入「權證」市場時，往往是散戶走向本金歸零的開始。接續先前幾篇的權證基礎、交易與結算解析，本周《投資診聊室》就來為大家深入診斷：權證到底能不能套牢
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%AC%8A%E8%AD%89%E5%8F%AF%E4%BB%A5%E5%A5%97%E7%89%A2%E6%94%A4%E5%B9%B3%E5%97%8E%EF%BC%9F%E6%98%AF%E9%80%A2%E4%BD%8E%E5%8A%A0%E7%A2%BC%E9%82%84%E6%98%AF%E3%80%8C%E8%B6%8A%E6%94%A4%E8%B6%8A%E5%B9%B3%E3%80%8D%EF%BC%9F%E4%B8%80%E6%96%87%E7%9C%8B%E6%87%82%E6%AC%8A%E8%AD%89%E6%8A%95%E8%B3%87%E7%AD%96%E7%95%A5-072302286.html
- 事件6：美股一天只休一小時 Nasdaq擬12月上路還有兩大布局
  - 來源：Yahoo 台股；發布時間：2026-11-03T09:49:27Z；台北時間：2026-11-03 17:49
  - 摘要：全球投資需求跨越時區，證券市場也正加速改變交易方式。Nasdaq（美股：NDAQ）執行副董事長Edward Knight今（3）日在「Taiwan Weeks 2026臺灣週」表示，Nasdaq仍依計畫朝12月6日啟動23/5交易推進，也就
  - 原文連結：https://tw.stock.yahoo.com/news/nasdaq%E9%A0%90%E8%A8%8812%E6%9C%886%E6%97%A5%E5%95%9F%E5%8B%9523%E5%B0%8F%E6%99%82%E4%BA%A4%E6%98%93-edward-knight%E8%AE%9A%E5%98%86%E5%8F%B0%E7%81%A3%E5%AF%A6%E5%8A%9B-%E6%9A%A2%E8%AB%87%E8%AD%89%E5%88%B8%E4%BB%A3%E5%B9%A3%E5%8C%96%E8%88%87ai%E5%B8%83%E5%B1%80-094927208.html
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
- 事件11：Midterm elections could jolt stocks if Democrats sweep Congress
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 11:54:28 GMT；台北時間：2026-11-03 19:54
  - 摘要：Wall Street weighs how the 2026 midterms could affect stocks, Treasury yields, artificial intelligence, energy prices, banks, defense and healthcare.
  - 原文連結：https://www.cnbc.com/2026/11/03/midterm-election-stock-market.html
- 事件12：Santoli: AI bull market almost surely needs tech stocks to recover to keep advancing
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 13:01:23 GMT；台北時間：2026-11-03 21:01
  - 摘要：The road to bull-market glory does not run through Walmart and Berkshire Hathaway and Eli Lilly.
  - 原文連結：https://www.cnbc.com/2026/11/03/santoli-ai-bull-market-needs-tech-stocks.html


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

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 68,904 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 71,286 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,382 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -2,141 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +2,625 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,898 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -169.8 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | unavailable | 億元 | TAIFEX Proxy |

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
| 外資 | 68,904 | 71,286 | -2,382 | 26,142 | 24,777 | +1,365 | -3,145 | 6,528 | 98,769 | -92,241 | -2,719 | 沿用前版（原來源：TAIFEX Proxy） |
| 投信 | 82 | 2,223 | -2,141 | 0 | 0 | +0 | +1,993 | 92,025 | 2,814 | +89,211 | +1,993 | 沿用前版（原來源：TAIFEX Proxy） |
| 自營商 | 9,523 | 6,898 | +2,625 | 887 | 641 | +246 | -141 | 6,106 | 4,370 | +1,736 | +225 | 沿用前版（原來源：TAIFEX Proxy） |
| 三大法人合計 | 78,509 | 80,407 | -1,898 | 27,029 | 25,418 | +1,611 | -1,293 | 104,659 | 105,953 | -1,294 | -501 | 沿用前版（原來源：TAIFEX Proxy） |

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
| 外資夜盤多空淨交易量 | +1,365 | 沿用前版（原來源：TAIFEX Proxy） |
| 劇本分類 | 劇本四 | 沿用前版（原來源：規則對應） |
| 劇本條件 | 夜盤下跌＋外資偏多 | 沿用前版（原來源：規則對應） |
| 劇本特徵 | 先跌、開低反彈 | 沿用前版（原來源：規則對應） |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-30 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F5 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-03 21:26:27 | 本機 |
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

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.06 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.64 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.61 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-10-30→2026-11-02) | 2.84 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-10-30→2026-11-02) | -1.01 | 百分點（pp） | TAIFEX Proxy |
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
| Gamma Wall 價位 | 44,500.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-30 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 44,049.22 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-30 | TAIFEX Proxy (options-gamma-levels) |

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 1,294,327,419.01 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 6,320,130,202.13 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 履約價資料筆數 | 139 | 資料日期：2026-10-30 |
| 正 Net GEX 最大履約價 | 44,500 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 44,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：44,500（339,560,594.26 NT$）、44,200（159,001,036.65 NT$）、44,300（155,243,900.90 NT$）、45,300（115,682,818.16 NT$）、46,000（115,525,885.27 NT$）
- 負 Net GEX Top 5：44,000（-300,268,961.25 NT$）、45,000（-215,006,111.29 NT$）、43,000（-107,788,999.27 NT$）、44,600（-61,509,566.44 NT$）、43,500（-56,208,333.13 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-10-30","underlying":45211.83,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":1294327419.0091748,"gross_gex_1pct":6320130202.132608,"levels":[{"strike":41400.0,"call_gex_1pct":0.0,"put_gex_1pct":-25135323.24286124,"net_gex_1pct":-25135323.24286124,"gross_gex_1pct":25135323.24286124,"call_oi":0,"put_oi":841},{"strike":41500.0,"call_gex_1pct":0.0,"put_gex_1pct":-5271089.899713166,"net_gex_1pct":-5271089.899713166,"gross_gex_1pct":5271089.899713166,"call_oi":0,"put_oi":157},{"strike":41600.0,"call_gex_1pct":0.0,"put_gex_1pct":-11416623.823120328,"net_gex_1pct":-11416623.823120328,"gross_gex_1pct":11416623.823120328,"call_oi":0,"put_oi":321},{"strike":41700.0,"call_gex_1pct":0.0,"put_gex_1pct":-3340256.458952387,"net_gex_1pct":-3340256.458952387,"gross_gex_1pct":3340256.458952387,"call_oi":0,"put_oi":88},{"strike":41800.0,"call_gex_1pct":0.0,"put_gex_1pct":-4319387.092578739,"net_gex_1pct":-4319387.092578739,"gross_gex_1pct":4319387.092578739,"call_oi":0,"put_oi":106},{"strike":41900.0,"call_gex_1pct":0.0,"put_gex_1pct":-1388837.6373620916,"net_gex_1pct":-1388837.6373620916,"gross_gex_1pct":1388837.6373620916,"call_oi":0,"put_oi":32},{"strike":42000.0,"call_gex_1pct":0.0,"put_gex_1pct":-17148165.612905703,"net_gex_1pct":-17148165.612905703,"gross_gex_1pct":17148165.612905703,"call_oi":0,"put_oi":369},{"strike":42100.0,"call_gex_1pct":0.0,"put_gex_1pct":-3461208.7860913672,"net_gex_1pct":-3461208.7860913672,"gross_gex_1pct":3461208.7860913672,"call_oi":0,"put_oi":70},{"strike":42200.0,"call_gex_1pct":0.0,"put_gex_1pct":-3964874.695138297,"net_gex_1pct":-3964874.695138297,"gross_gex_1pct":3964874.695138297,"call_oi":0,"put_oi":75},{"strike":42300.0,"call_gex_1pct":0.0,"put_gex_1pct":-5592127.475650332,"net_gex_1pct":-5592127.475650332,"gross_gex_1pct":5592127.475650332,"call_oi":0,"put_oi":99},{"strike":42400.0,"call_gex_1pct":0.0,"put_gex_1pct":-21122736.810536854,"net_gex_1pct":-21122736.810536854,"gross_gex_1pct":21122736.810536854,"call_oi":0,"put_oi":353},{"strike":42500.0,"call_gex_1pct":0.0,"put_gex_1pct":-19601376.563104793,"net_gex_1pct":-19601376.563104793,"gross_gex_1pct":19601376.563104793,"call_oi":0,"put_oi":302},{"strike":42600.0,"call_gex_1pct":0.0,"put_gex_1pct":-5004392.963035988,"net_gex_1pct":-5004392.963035988,"gross_gex_1pct":5004392.963035988,"call_oi":0,"put_oi":72},{"strike":42700.0,"call_gex_1pct":0.0,"put_gex_1pct":-10103689.670431262,"net_gex_1pct":-10103689.670431262,"gross_gex_1pct":10103689.670431262,"call_oi":0,"put_oi":135},{"strike":42800.0,"call_gex_1pct":0.0,"put_gex_1pct":-3961690.404794335,"net_gex_1pct":-3961690.404794335,"gross_gex_1pct":3961690.404794335,"call_oi":0,"put_oi":50},{"strike":42900.0,"call_gex_1pct":0.0,"put_gex_1pct":-3813311.3618619596,"net_gex_1pct":-3813311.3618619596,"gross_gex_1pct":3813311.3618619596,"call_oi":0,"put_oi":44},{"strike":43000.0,"call_gex_1pct":0.0,"put_gex_1pct":-107788999.2711138,"net_gex_1pct":-107788999.2711138,"gross_gex_1pct":107788999.2711138,"call_oi":0,"put_oi":1152},{"strike":43100.0,"call_gex_1pct":0.0,"put_gex_1pct":-23176413.419474564,"net_gex_1pct":-23176413.419474564,"gross_gex_1pct":23176413.419474564,"call_oi":0,"put_oi":232},{"strike":43200.0,"call_gex_1pct":0.0,"put_gex_1pct":-14185832.51765619,"net_gex_1pct":-14185832.51765619,"gross_gex_1pct":14185832.51765619,"call_oi":0,"put_oi":131},{"strike":43300.0,"call_gex_1pct":0.0,"put_gex_1pct":-34004930.19894648,"net_gex_1pct":-34004930.19894648,"gross_gex_1pct":34004930.19894648,"call_oi":0,"put_oi":293},{"strike":43400.0,"call_gex_1pct":0.0,"put_gex_1pct":-12061569.744501514,"net_gex_1pct":-12061569.744501514,"gross_gex_1pct":12061569.744501514,"call_oi":0,"put_oi":96},{"strike":43500.0,"call_gex_1pct":0.0,"put_gex_1pct":-56208333.13364849,"net_gex_1pct":-56208333.13364849,"gross_gex_1pct":56208333.13364849,"call_oi":0,"put_oi":411},{"strike":43600.0,"call_gex_1pct":0.0,"put_gex_1pct":-36894952.738443576,"net_gex_1pct":-36894952.738443576,"gross_gex_1pct":36894952.738443576,"call_oi":0,"put_oi":251},{"strike":43700.0,"call_gex_1pct":0.0,"put_gex_1pct":-22428050.66217165,"net_gex_1pct":-22428050.66217165,"gross_gex_1pct":22428050.66217165,"call_oi":0,"put_oi":142},{"strike":43800.0,"call_gex_1pct":0.0,"put_gex_1pct":-31171746.856139626,"net_gex_1pct":-31171746.856139626,"gross_gex_1pct":31171746.856139626,"call_oi":0,"put_oi":184},{"strike":43900.0,"call_gex_1pct":0.0,"put_gex_1pct":-43417831.922930606,"net_gex_1pct":-43417831.922930606,"gross_gex_1pct":43417831.922930606,"call_oi":0,"put_oi":240},{"strike":44000.0,"call_gex_1pct":0.0,"put_gex_1pct":-300268961.2520295,"net_gex_1pct":-300268961.2520295,"gross_gex_1pct":300268961.2520295,"call_oi":0,"put_oi":1560},{"strike":44100.0,"call_gex_1pct":142745795.74482593,"put_gex_1pct":-45173749.51950166,"net_gex_1pct":97572046.22532427,"gross_gex_1pct":187919545.2643276,"call_oi":864,"put_oi":223},{"strike":44200.0,"call_gex_1pct":203184454.61228508,"put_gex_1pct":-44183417.966718845,"net_gex_1pct":159001036.64556623,"gross_gex_1pct":247367872.57900393,"call_oi":881,"put_oi":206},{"strike":44300.0,"call_gex_1pct":217355360.1375478,"put_gex_1pct":-62111459.24090873,"net_gex_1pct":155243900.89663905,"gross_gex_1pct":279466819.37845653,"call_oi":818,"put_oi":281},{"strike":44400.0,"call_gex_1pct":19048556.076212633,"put_gex_1pct":-34166382.59168019,"net_gex_1pct":-15117826.515467558,"gross_gex_1pct":53214938.66789283,"call_oi":67,"put_oi":149},{"strike":44500.0,"call_gex_1pct":434401101.82316893,"put_gex_1pct":-94840507.56596242,"net_gex_1pct":339560594.2572065,"gross_gex_1pct":529241609.38913137,"call_oi":1436,"put_oi":397},{"strike":44600.0,"call_gex_1pct":16453286.397280565,"put_gex_1pct":-77962852.83343633,"net_gex_1pct":-61509566.43615576,"gross_gex_1pct":94416139.23071688,"call_oi":51,"put_oi":321},{"strike":44700.0,"call_gex_1pct":14510249.400216196,"put_gex_1pct":-31025062.933710817,"net_gex_1pct":-16514813.533494622,"gross_gex_1pct":45535312.33392701,"call_oi":44,"put_oi":122},{"strike":44750.0,"call_gex_1pct":11150481.573954972,"put_gex_1pct":-17754057.679383725,"net_gex_1pct":-6603576.105428753,"gross_gex_1pct":28904539.253338695,"call_oi":33,"put_oi":71},{"strike":44800.0,"call_gex_1pct":10275456.172893122,"put_gex_1pct":-46810537.86494077,"net_gex_1pct":-36535081.69204765,"gross_gex_1pct":57085994.03783389,"call_oi":30,"put_oi":184},{"strike":44850.0,"call_gex_1pct":29497524.493803896,"put_gex_1pct":-25611407.46166943,"net_gex_1pct":3886117.032134466,"gross_gex_1pct":55108931.955473326,"call_oi":85,"put_oi":101},{"strike":44900.0,"call_gex_1pct":29339279.358190455,"put_gex_1pct":-36701724.56900734,"net_gex_1pct":-7362445.210816883,"gross_gex_1pct":66041003.92719779,"call_oi":88,"put_oi":140},{"strike":44950.0,"call_gex_1pct":22986412.617064867,"put_gex_1pct":-15887280.463980349,"net_gex_1pct":7099132.153084518,"gross_gex_1pct":38873693.08104522,"call_oi":66,"put_oi":62},{"strike":45000.0,"call_gex_1pct":88236261.94634807,"put_gex_1pct":-303242373.2336051,"net_gex_1pct":-215006111.28725702,"gross_gex_1pct":391478635.17995316,"call_oi":253,"put_oi":1182},{"strike":45050.0,"call_gex_1pct":39458661.073345535,"put_gex_1pct":-22345454.213920716,"net_gex_1pct":17113206.85942482,"gross_gex_1pct":61804115.287266254,"call_oi":113,"put_oi":87},{"strike":45100.0,"call_gex_1pct":69919285.90653273,"put_gex_1pct":-32916858.408712737,"net_gex_1pct":37002427.49782,"gross_gex_1pct":102836144.31524548,"call_oi":200,"put_oi":127},{"strike":45150.0,"call_gex_1pct":17849439.971893515,"put_gex_1pct":-19249450.991953976,"net_gex_1pct":-1400011.020060461,"gross_gex_1pct":37098890.96384749,"call_oi":51,"put_oi":73},{"strike":45200.0,"call_gex_1pct":172344076.08680698,"put_gex_1pct":-60851426.16577283,"net_gex_1pct":111492649.92103416,"gross_gex_1pct":233195502.2525798,"call_oi":494,"put_oi":238},{"strike":45250.0,"call_gex_1pct":22903685.272215463,"put_gex_1pct":-15491748.400622142,"net_gex_1pct":7411936.871593321,"gross_gex_1pct":38395433.67283761,"call_oi":66,"put_oi":61},{"strike":45300.0,"call_gex_1pct":245600933.8860988,"put_gex_1pct":-129918115.7297379,"net_gex_1pct":115682818.15636091,"gross_gex_1pct":375519049.6158367,"call_oi":716,"put_oi":511},{"strike":45350.0,"call_gex_1pct":11626238.044966578,"put_gex_1pct":-11617324.78527911,"net_gex_1pct":8913.25968746841,"gross_gex_1pct":23243562.83024569,"call_oi":34,"put_oi":46},{"strike":45400.0,"call_gex_1pct":68548615.57413399,"put_gex_1pct":-59207934.75165238,"net_gex_1pct":9340680.82248161,"gross_gex_1pct":127756550.32578638,"call_oi":199,"put_oi":236},{"strike":45450.0,"call_gex_1pct":17816155.984102543,"put_gex_1pct":-12212329.19239235,"net_gex_1pct":5603826.791710194,"gross_gex_1pct":30028485.176494893,"call_oi":52,"put_oi":49},{"strike":45500.0,"call_gex_1pct":177556522.07287055,"put_gex_1pct":-84870710.42001821,"net_gex_1pct":92685811.65285234,"gross_gex_1pct":262427232.49288875,"call_oi":533,"put_oi":335},{"strike":45550.0,"call_gex_1pct":18934481.412088506,"put_gex_1pct":-6347692.165711517,"net_gex_1pct":12586789.246376988,"gross_gex_1pct":25282173.577800024,"call_oi":56,"put_oi":26},{"strike":45600.0,"call_gex_1pct":108702388.36489275,"put_gex_1pct":-53578101.89957713,"net_gex_1pct":55124286.46531562,"gross_gex_1pct":162280490.2644699,"call_oi":330,"put_oi":216},{"strike":45650.0,"call_gex_1pct":21814232.677708246,"put_gex_1pct":-8433634.433319425,"net_gex_1pct":13380598.24438882,"gross_gex_1pct":30247867.111027673,"call_oi":69,"put_oi":35},{"strike":45700.0,"call_gex_1pct":53126351.9423569,"put_gex_1pct":-29728430.116510473,"net_gex_1pct":23397921.825846426,"gross_gex_1pct":82854782.05886737,"call_oi":171,"put_oi":126},{"strike":45750.0,"call_gex_1pct":43455673.61445363,"put_gex_1pct":-7680253.249921868,"net_gex_1pct":35775420.36453176,"gross_gex_1pct":51135926.864375494,"call_oi":139,"put_oi":33},{"strike":45800.0,"call_gex_1pct":96013792.90464455,"put_gex_1pct":-86371191.8594071,"net_gex_1pct":9642601.045237452,"gross_gex_1pct":182384984.76405165,"call_oi":314,"put_oi":371},{"strike":45850.0,"call_gex_1pct":24271061.579665486,"put_gex_1pct":-4949097.013450609,"net_gex_1pct":19321964.566214878,"gross_gex_1pct":29220158.593116093,"call_oi":83,"put_oi":22},{"strike":45900.0,"call_gex_1pct":41770619.84573196,"put_gex_1pct":-7181392.663547213,"net_gex_1pct":34589227.18218475,"gross_gex_1pct":48952012.50927917,"call_oi":146,"put_oi":33},{"strike":45950.0,"call_gex_1pct":26259518.60790847,"put_gex_1pct":-12481438.040794227,"net_gex_1pct":13778080.567114241,"gross_gex_1pct":38740956.648702696,"call_oi":94,"put_oi":57},{"strike":46000.0,"call_gex_1pct":136396785.75617588,"put_gex_1pct":-20870900.48277467,"net_gex_1pct":115525885.2734012,"gross_gex_1pct":157267686.23895055,"call_oi":501,"put_oi":96},{"strike":46050.0,"call_gex_1pct":14321179.70225654,"put_gex_1pct":-12838074.316589901,"net_gex_1pct":1483105.3856666386,"gross_gex_1pct":27159254.01884644,"call_oi":54,"put_oi":61},{"strike":46100.0,"call_gex_1pct":37389602.67305124,"put_gex_1pct":-16919809.019760117,"net_gex_1pct":20469793.65329112,"gross_gex_1pct":54309411.692811355,"call_oi":145,"put_oi":81},{"strike":46150.0,"call_gex_1pct":14783513.678282507,"put_gex_1pct":-6758324.769940696,"net_gex_1pct":8025188.908341811,"gross_gex_1pct":21541838.448223203,"call_oi":59,"put_oi":33},{"strike":46200.0,"call_gex_1pct":89126405.64812374,"put_gex_1pct":-29719818.567263518,"net_gex_1pct":59406587.08086023,"gross_gex_1pct":118846224.21538725,"call_oi":363,"put_oi":148},{"strike":46250.0,"call_gex_1pct":12754207.870023448,"put_gex_1pct":-1363347.5002342227,"net_gex_1pct":11390860.369789226,"gross_gex_1pct":14117555.37025767,"call_oi":54,"put_oi":7},{"strike":46300.0,"call_gex_1pct":46387997.13623231,"put_gex_1pct":-5406772.5959184235,"net_gex_1pct":40981224.540313885,"gross_gex_1pct":51794769.73215073,"call_oi":204,"put_oi":28},{"strike":46350.0,"call_gex_1pct":15642549.747084325,"put_gex_1pct":-2811560.1252290453,"net_gex_1pct":12830989.62185528,"gross_gex_1pct":18454109.87231337,"call_oi":71,"put_oi":15},{"strike":46400.0,"call_gex_1pct":41253224.66627397,"put_gex_1pct":-4413026.866965205,"net_gex_1pct":36840197.79930876,"gross_gex_1pct":45666251.53323917,"call_oi":194,"put_oi":24},{"strike":46450.0,"call_gex_1pct":7796656.878741465,"put_gex_1pct":-4551733.202830849,"net_gex_1pct":3244923.6759106154,"gross_gex_1pct":12348390.081572313,"call_oi":38,"put_oi":25},{"strike":46500.0,"call_gex_1pct":87930762.22006232,"put_gex_1pct":-13387714.63347722,"net_gex_1pct":74543047.58658509,"gross_gex_1pct":101318476.85353954,"call_oi":446,"put_oi":75},{"strike":46550.0,"call_gex_1pct":8904242.548302967,"put_gex_1pct":-5378795.411112558,"net_gex_1pct":3525447.137190409,"gross_gex_1pct":14283037.959415525,"call_oi":47,"put_oi":31},{"strike":46600.0,"call_gex_1pct":41116697.06547461,"put_gex_1pct":-4423499.621439766,"net_gex_1pct":36693197.444034845,"gross_gex_1pct":45540196.68691437,"call_oi":227,"put_oi":26},{"strike":46650.0,"call_gex_1pct":17045427.374762878,"put_gex_1pct":-5297204.5346340975,"net_gex_1pct":11748222.84012878,"gross_gex_1pct":22342631.909396976,"call_oi":98,"put_oi":32},{"strike":46700.0,"call_gex_1pct":74938284.04237254,"put_gex_1pct":-7953884.828459028,"net_gex_1pct":66984399.213913515,"gross_gex_1pct":82892168.87083156,"call_oi":453,"put_oi":49},{"strike":46750.0,"call_gex_1pct":13578741.7216129,"put_gex_1pct":-3635839.2787084156,"net_gex_1pct":9942902.442904485,"gross_gex_1pct":17214581.000321317,"call_oi":86,"put_oi":23},{"strike":46800.0,"call_gex_1pct":105427537.41090241,"put_gex_1pct":-9566578.768618705,"net_gex_1pct":95860958.64228371,"gross_gex_1pct":114994116.17952111,"call_oi":701,"put_oi":61},{"strike":46850.0,"call_gex_1pct":18861747.02790479,"put_gex_1pct":-1527415.9096581878,"net_gex_1pct":17334331.118246604,"gross_gex_1pct":20389162.937562976,"call_oi":132,"put_oi":10},{"strike":46900.0,"call_gex_1pct":56163025.06504066,"put_gex_1pct":-3721191.3988237437,"net_gex_1pct":52441833.66621692,"gross_gex_1pct":59884216.46386441,"call_oi":410,"put_oi":25},{"strike":46950.0,"call_gex_1pct":12682566.663792199,"put_gex_1pct":-5660231.362080245,"net_gex_1pct":7022335.301711953,"gross_gex_1pct":18342798.025872443,"call_oi":97,"put_oi":39},{"strike":47000.0,"call_gex_1pct":71490961.49431857,"put_gex_1pct":-6513093.58456566,"net_gex_1pct":64977867.90975291,"gross_gex_1pct":78004055.07888423,"call_oi":595,"put_oi":46},{"strike":47050.0,"call_gex_1pct":12402015.602179248,"put_gex_1pct":-967408.5212516767,"net_gex_1pct":11434607.080927571,"gross_gex_1pct":13369424.123430924,"call_oi":109,"put_oi":7},{"strike":47100.0,"call_gex_1pct":13695959.688216472,"put_gex_1pct":-1489401.110060613,"net_gex_1pct":12206558.578155858,"gross_gex_1pct":15185360.798277086,"call_oi":128,"put_oi":11},{"strike":47150.0,"call_gex_1pct":5260246.069297474,"put_gex_1pct":-264491.1271543095,"net_gex_1pct":4995754.942143165,"gross_gex_1pct":5524737.196451783,"call_oi":52,"put_oi":2},{"strike":47200.0,"call_gex_1pct":51080119.53438016,"put_gex_1pct":-1942498.6283419575,"net_gex_1pct":49137620.9060382,"gross_gex_1pct":53022618.16272212,"call_oi":563,"put_oi":15},{"strike":47250.0,"call_gex_1pct":8783304.751253426,"put_gex_1pct":-1139023.8983724331,"net_gex_1pct":7644280.852880993,"gross_gex_1pct":9922328.64962586,"call_oi":100,"put_oi":9},{"strike":47300.0,"call_gex_1pct":48148199.11093868,"put_gex_1pct":-1361110.397473521,"net_gex_1pct":46787088.71346516,"gross_gex_1pct":49509309.508412205,"call_oi":603,"put_oi":11},{"strike":47350.0,"call_gex_1pct":6075192.356199203,"put_gex_1pct":-121030.07597488709,"net_gex_1pct":5954162.280224316,"gross_gex_1pct":6196222.43217409,"call_oi":80,"put_oi":1},{"strike":47400.0,"call_gex_1pct":15991104.773188412,"put_gex_1pct":-118468.05619903725,"net_gex_1pct":15872636.716989376,"gross_gex_1pct":16109572.829387449,"call_oi":229,"put_oi":1},{"strike":47450.0,"call_gex_1pct":3459081.1570586674,"put_gex_1pct":-115934.7868641617,"net_gex_1pct":3343146.370194506,"gross_gex_1pct":3575015.943922829,"call_oi":53,"put_oi":1},{"strike":47500.0,"call_gex_1pct":37953030.892766,"put_gex_1pct":-1588988.8416612274,"net_gex_1pct":36364042.05110477,"gross_gex_1pct":39542019.73442723,"call_oi":625,"put_oi":14},{"strike":47550.0,"call_gex_1pct":3482666.0220219796,"put_gex_1pct":-111155.90051142916,"net_gex_1pct":3371510.1215105504,"gross_gex_1pct":3593821.9225334087,"call_oi":60,"put_oi":1},{"strike":47600.0,"call_gex_1pct":10216440.524278028,"put_gex_1pct":-108899.86356823197,"net_gex_1pct":10107540.660709796,"gross_gex_1pct":10325340.38784626,"call_oi":198,"put_oi":1},{"strike":47650.0,"call_gex_1pct":1008705.620501882,"put_gex_1pct":-426905.72087585926,"net_gex_1pct":581799.8996260228,"gross_gex_1pct":1435611.3413777412,"call_oi":21,"put_oi":4},{"strike":47700.0,"call_gex_1pct":4879295.387059847,"put_gex_1pct":-523156.30954728427,"net_gex_1pct":4356139.077512562,"gross_gex_1pct":5402451.6966071315,"call_oi":107,"put_oi":5},{"strike":47750.0,"call_gex_1pct":2097271.688822667,"put_gex_1pct":0.0,"net_gex_1pct":2097271.688822667,"gross_gex_1pct":2097271.688822667,"call_oi":49,"put_oi":0},{"strike":47800.0,"call_gex_1pct":8065643.459962951,"put_gex_1pct":-503299.1045915603,"net_gex_1pct":7562344.3553713905,"gross_gex_1pct":8568942.56455451,"call_oi":198,"put_oi":5},{"strike":47850.0,"call_gex_1pct":1489129.558411955,"put_gex_1pct":0.0,"net_gex_1pct":1489129.558411955,"gross_gex_1pct":1489129.558411955,"call_oi":38,"put_oi":0},{"strike":47900.0,"call_gex_1pct":8196533.881945091,"put_gex_1pct":-386638.8380716807,"net_gex_1pct":7809895.043873411,"gross_gex_1pct":8583172.720016772,"call_oi":227,"put_oi":4},{"strike":47950.0,"call_gex_1pct":2948213.191804176,"put_gex_1pct":0.0,"net_gex_1pct":2948213.191804176,"gross_gex_1pct":2948213.191804176,"call_oi":88,"put_oi":0},{"strike":48000.0,"call_gex_1pct":13556182.062776465,"put_gex_1pct":-372666.01833014184,"net_gex_1pct":13183516.044446323,"gross_gex_1pct":13928848.081106607,"call_oi":446,"put_oi":4},{"strike":48050.0,"call_gex_1pct":3957486.796207176,"put_gex_1pct":0.0,"net_gex_1pct":3957486.796207176,"gross_gex_1pct":3957486.796207176,"call_oi":136,"put_oi":0},{"strike":48100.0,"call_gex_1pct":3481194.8005490145,"put_gex_1pct":-89897.41395959305,"net_gex_1pct":3391297.3865894214,"gross_gex_1pct":3571092.2145086075,"call_oi":125,"put_oi":1},{"strike":48150.0,"call_gex_1pct":726354.3117196643,"put_gex_1pct":0.0,"net_gex_1pct":726354.3117196643,"gross_gex_1pct":726354.3117196643,"call_oi":29,"put_oi":0},{"strike":48200.0,"call_gex_1pct":12163916.235951766,"put_gex_1pct":-173664.26252843437,"net_gex_1pct":11990251.973423332,"gross_gex_1pct":12337580.4984802,"call_oi":498,"put_oi":2},{"strike":48250.0,"call_gex_1pct":571910.4760034516,"put_gex_1pct":0.0,"net_gex_1pct":571910.4760034516,"gross_gex_1pct":571910.4760034516,"call_oi":24,"put_oi":0},{"strike":48300.0,"call_gex_1pct":8370696.961116455,"put_gex_1pct":-1007432.465294253,"net_gex_1pct":7363264.4958222015,"gross_gex_1pct":9378129.426410707,"call_oi":377,"put_oi":12},{"strike":48350.0,"call_gex_1pct":629716.9338725266,"put_gex_1pct":0.0,"net_gex_1pct":629716.9338725266,"gross_gex_1pct":629716.9338725266,"call_oi":31,"put_oi":0},{"strike":48400.0,"call_gex_1pct":9253316.541967211,"put_gex_1pct":0.0,"net_gex_1pct":9253316.541967211,"gross_gex_1pct":9253316.541967211,"call_oi":480,"put_oi":0},{"strike":48500.0,"call_gex_1pct":7622300.827047983,"put_gex_1pct":0.0,"net_gex_1pct":7622300.827047983,"gross_gex_1pct":7622300.827047983,"call_oi":427,"put_oi":0},{"strike":48600.0,"call_gex_1pct":1916315.3191051963,"put_gex_1pct":0.0,"net_gex_1pct":1916315.3191051963,"gross_gex_1pct":1916315.3191051963,"call_oi":118,"put_oi":0},{"strike":48700.0,"call_gex_1pct":1282568.9163593526,"put_gex_1pct":0.0,"net_gex_1pct":1282568.9163593526,"gross_gex_1pct":1282568.9163593526,"call_oi":84,"put_oi":0},{"strike":48800.0,"call_gex_1pct":2889406.8674163064,"put_gex_1pct":0.0,"net_gex_1pct":2889406.8674163064,"gross_gex_1pct":2889406.8674163064,"call_oi":205,"put_oi":0},{"strike":48900.0,"call_gex_1pct":1142928.8084702413,"put_gex_1pct":0.0,"net_gex_1pct":1142928.8084702413,"gross_gex_1pct":1142928.8084702413,"call_oi":88,"put_oi":0},{"strike":49000.0,"call_gex_1pct":7118699.07959754,"put_gex_1pct":0.0,"net_gex_1pct":7118699.07959754,"gross_gex_1pct":7118699.07959754,"call_oi":610,"put_oi":0},{"strike":49100.0,"call_gex_1pct":437736.90177800076,"put_gex_1pct":0.0,"net_gex_1pct":437736.90177800076,"gross_gex_1pct":437736.90177800076,"call_oi":41,"put_oi":0},{"strike":49200.0,"call_gex_1pct":240040.4380113107,"put_gex_1pct":-128516.04907764898,"net_gex_1pct":111524.38893366173,"gross_gex_1pct":368556.48708895966,"call_oi":24,"put_oi":2},{"strike":49300.0,"call_gex_1pct":400288.80419206194,"put_gex_1pct":0.0,"net_gex_1pct":400288.80419206194,"gross_gex_1pct":400288.80419206194,"call_oi":44,"put_oi":0},{"strike":49400.0,"call_gex_1pct":33558995.64095215,"put_gex_1pct":0.0,"net_gex_1pct":33558995.64095215,"gross_gex_1pct":33558995.64095215,"call_oi":4220,"put_oi":0},{"strike":49500.0,"call_gex_1pct":1929442.8233633917,"put_gex_1pct":0.0,"net_gex_1pct":1929442.8233633917,"gross_gex_1pct":1929442.8233633917,"call_oi":261,"put_oi":0},{"strike":49600.0,"call_gex_1pct":171514.5990940013,"put_gex_1pct":0.0,"net_gex_1pct":171514.5990940013,"gross_gex_1pct":171514.5990940013,"call_oi":25,"put_oi":0},{"strike":49700.0,"call_gex_1pct":109849.41256553507,"put_gex_1pct":0.0,"net_gex_1pct":109849.41256553507,"gross_gex_1pct":109849.41256553507,"call_oi":20,"put_oi":0},{"strike":49800.0,"call_gex_1pct":137959.00442404483,"put_gex_1pct":0.0,"net_gex_1pct":137959.00442404483,"gross_gex_1pct":137959.00442404483,"call_oi":26,"put_oi":0},{"strike":49900.0,"call_gex_1pct":107729.92695456032,"put_gex_1pct":0.0,"net_gex_1pct":107729.92695456032,"gross_gex_1pct":107729.92695456032,"call_oi":21,"put_oi":0},{"strike":50000.0,"call_gex_1pct":4352461.154841954,"put_gex_1pct":0.0,"net_gex_1pct":4352461.154841954,"gross_gex_1pct":4352461.154841954,"call_oi":990,"put_oi":0},{"strike":50100.0,"call_gex_1pct":21279.429692353384,"put_gex_1pct":0.0,"net_gex_1pct":21279.429692353384,"gross_gex_1pct":21279.429692353384,"call_oi":5,"put_oi":0},{"strike":50200.0,"call_gex_1pct":84486.943467283,"put_gex_1pct":0.0,"net_gex_1pct":84486.943467283,"gross_gex_1pct":84486.943467283,"call_oi":22,"put_oi":0},{"strike":50300.0,"call_gex_1pct":78407.01850016038,"put_gex_1pct":0.0,"net_gex_1pct":78407.01850016038,"gross_gex_1pct":78407.01850016038,"call_oi":25,"put_oi":0},{"strike":50400.0,"call_gex_1pct":164219.3611879932,"put_gex_1pct":0.0,"net_gex_1pct":164219.3611879932,"gross_gex_1pct":164219.3611879932,"call_oi":54,"put_oi":0},{"strike":50500.0,"call_gex_1pct":177714.5962378995,"put_gex_1pct":0.0,"net_gex_1pct":177714.5962378995,"gross_gex_1pct":177714.5962378995,"call_oi":67,"put_oi":0},{"strike":50600.0,"call_gex_1pct":18136.40734386398,"put_gex_1pct":0.0,"net_gex_1pct":18136.40734386398,"gross_gex_1pct":18136.40734386398,"call_oi":8,"put_oi":0},{"strike":50700.0,"call_gex_1pct":6604.839434666439,"put_gex_1pct":0.0,"net_gex_1pct":6604.839434666439,"gross_gex_1pct":6604.839434666439,"call_oi":3,"put_oi":0},{"strike":50800.0,"call_gex_1pct":8556.960576613597,"put_gex_1pct":0.0,"net_gex_1pct":8556.960576613597,"gross_gex_1pct":8556.960576613597,"call_oi":4,"put_oi":0},{"strike":50900.0,"call_gex_1pct":24865.381212536322,"put_gex_1pct":0.0,"net_gex_1pct":24865.381212536322,"gross_gex_1pct":24865.381212536322,"call_oi":14,"put_oi":0},{"strike":51000.0,"call_gex_1pct":4035084.3306592335,"put_gex_1pct":-85874.75091940559,"net_gex_1pct":3949209.579739828,"gross_gex_1pct":4120959.081578639,"call_oi":2336,"put_oi":2},{"strike":51100.0,"call_gex_1pct":15042.258584418816,"put_gex_1pct":0.0,"net_gex_1pct":15042.258584418816,"gross_gex_1pct":15042.258584418816,"call_oi":11,"put_oi":0},{"strike":51200.0,"call_gex_1pct":7986.2065132996695,"put_gex_1pct":0.0,"net_gex_1pct":7986.2065132996695,"gross_gex_1pct":7986.2065132996695,"call_oi":6,"put_oi":0},{"strike":51300.0,"call_gex_1pct":3888.506226634964,"put_gex_1pct":0.0,"net_gex_1pct":3888.506226634964,"gross_gex_1pct":3888.506226634964,"call_oi":3,"put_oi":0},{"strike":51500.0,"call_gex_1pct":4577.383822181604,"put_gex_1pct":0.0,"net_gex_1pct":4577.383822181604,"gross_gex_1pct":4577.383822181604,"call_oi":5,"put_oi":0},{"strike":51600.0,"call_gex_1pct":68722.46580729223,"put_gex_1pct":0.0,"net_gex_1pct":68722.46580729223,"gross_gex_1pct":68722.46580729223,"call_oi":77,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 45,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | -600 | TAIFEX Proxy snapshots (2026-10-29) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 140,211 | 139,870 | +341 | 41,871 | 41,965 | -94 | +6,718 | 沿用前版（原來源：TAIFEX Proxy） |
| 投信 | 200 | 5,246 | -5,046 | 0 | 0 | +0 | -4,937 | 沿用前版（原來源：TAIFEX Proxy） |
| 自營商 | 123,594 | 135,042 | -11,448 | 21,826 | 23,217 | -1,391 | +2,733 | 沿用前版（原來源：TAIFEX Proxy） |
| 三大法人合計 | 264,005 | 280,158 | -16,153 | 63,697 | 65,182 | -1,485 | +4,514 | 沿用前版（原來源：TAIFEX Proxy） |
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
- 資料日期：2026-10-30；資料時間：2026-11-03 21:26:27；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：50 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：73 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (10)：otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, sbl.sale_bal, sbl.sale_chg, turnover.otc, futures.futures.night.settle, futures.futures.night.oi
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-03，非 T0 2026-10-30)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-03 非今日 2026-11-02，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-03 非今日 2026-11-02，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-03 非今日 2026-11-02，視為無新節次，不採用
- 註記：法人交易量變化無昨日交易端點，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`TWSE 上市自建估算（資料日期：2026-10-30；估值 1238 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）；Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點）`
- sbl_bal：`TWSE TWT96U + TWT96U GRETAI（上櫃）`
- sbl_sale_bal：`端點未提供`
- sbl_sale_chg：`端點未提供`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151103, T0=1151030)
- 註記：三大法人回傳日期 20261103 (T0 20261030)，採用最新可得
- 註記：上市市場維持率以 TWSE 自建計算為主；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）。Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,073.1 | -92,241 | -2,382 | +1,365 | +341 | -94 | 避險／對沖 | 對沖避險 | 沿用前版（原來源：twse-proxy／TAIFEX Proxy） |
| 投信 | +184.6 | +89,211 | -2,141 | +0 | -5,046 | +0 | 避險／對沖 | 分歧 | 沿用前版（原來源：twse-proxy／TAIFEX Proxy） |
| 自營商 | -590.5 | +1,736 | +2,625 | +246 | -11,448 | -1,391 | 避險／對沖 | 分歧 | 沿用前版（原來源：twse-proxy／TAIFEX Proxy） |
