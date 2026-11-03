# DATA_REPORT_20261104

- 報告日期：`2026-11-04`
- T0 交易日期：`2026-11-04`
- 資料產出時間：`2026-11-04 02:12:59`
- 時區：`Asia/Taipei`
- 產出盤別：`日盤`
- 產出者：`actions`
- 排定班別：`evening`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 44,920.14 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 44,920.14 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -291.69 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -0.65 | % | TWSE OpenAPI MI_INDEX (備援) |
| 成交金額 | unavailable | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | unavailable | twse-proxy |
| 下跌家數 | unavailable | twse-proxy |
| 平盤家數 | unavailable | twse-proxy |
| 漲停家數 | unavailable | twse-proxy |
| 跌停家數 | unavailable | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | unavailable | TPEX |
| 下跌家數 | unavailable | TPEX |
| 平盤家數 | unavailable | TPEX |
| 漲停家數 | unavailable | TPEX |
| 跌停家數 | unavailable | TPEX |

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
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 194,930 | 張 | HiStock |
| 融券增減 | -1,597 | 張 | HiStock |
| 融資維持率 | 171.80 | % | 前值遞補 (DATA 2026-11-03；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,525,111 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | unavailable | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | unavailable | 億元 | twse-proxy market_statistics+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,591.01 | 49.61 | +0.66 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,466.28 | 301.97 | +1.20 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,286.39 | 296.57 | +1.06 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,861.17 | -122.81 | -0.24 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,664.28 | 335.95 | +3.25 | Yahoo Finance Chart API |
| VIX | ^VIX | 20.70 | -0.45 | -2.13 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,081.86 | -208.25 | -0.33 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,859.08 | 128.34 | +2.24 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,393.32 | 98.90 | +0.42 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,638.03 | 39.01 | +1.08 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,010.68 | 176.90 | +1.63 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,611.25 | 36.75 | +0.49 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,382.00 | 254.50 | +0.90 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,947.00 | -186.00 | -0.36 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,834.70 | 16.90 | +0.60 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.59 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.95 | 0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.33 | 0.06 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.79 | 0.19 | +0.58 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.80 | 0.05 | +0.05 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.48 | 0.80 | +0.51 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,344.55 | 19.03 | +1.44 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 407.20 | 8.57 | +2.15 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.62 | 0.24 | +1.43 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.56 | 0.39 | +1.00 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 95.93 | -0.53 | -0.55 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,942.10 | -27.50 | -0.69 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 77,632.07 | 954.77 | +1.25 | Yahoo Finance Chart API |

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
- 事件9：Job openings posted big September gain in positive sign for labor market ahead of payrolls report
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 16:10:21 GMT；台北時間：2026-11-04 00:10
  - 摘要：The BLS reported job openings at 7.52 million, up 333,000 from August and well above the Dow Jones consensus outlook for 7.15 million
  - 原文連結：https://www.cnbc.com/2026/11/03/job-openings-posted-big-september-gain-in-positive-sign-for-labor-market-ahead-of-payrolls-report.html
- 事件10：Crude oil prices fall for second day as market hopes for diplomatic resolution to Iran war
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 16:01:39 GMT；台北時間：2026-11-04 00:01
  - 摘要：The rebound in oil prices come a day after the U.S. and Iranian presidents signalled they are open to a diplomatic solution to Iran war.
  - 原文連結：https://www.cnbc.com/2026/11/03/oil-prices-climb-after-us-reportedly-strikes-irans-qeshm-island.html
- 事件11：Midterm elections could jolt stocks if Democrats sweep Congress
  - 來源：CNBC；發布時間：Tue, 03 Nov 2026 18:05:18 GMT；台北時間：2026-11-04 02:05
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

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-04

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
| 開盤價 | unavailable | 端點未提供 |
| 最高價 | unavailable | 端點未提供 |
| 最低價 | unavailable | 端點未提供 |
| 收盤價 | unavailable | 端點未提供 |
| 漲跌點數 | unavailable | 端點未提供 |
| 漲跌幅 | unavailable | 端點未提供 |
| 成交量 | unavailable | TAIFEX Proxy |
| 夜盤高點及低點 | unavailable / unavailable | 端點未提供 |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | unavailable | TAIFEX Proxy |
| 外資空方 OI | unavailable | TAIFEX Proxy |
| 外資多空淨 OI | unavailable | TAIFEX Proxy |
| 投信多方 OI | unavailable | TAIFEX Proxy |
| 投信空方 OI | unavailable | TAIFEX Proxy |
| 投信多空淨 OI | unavailable | TAIFEX Proxy |
| 自營商多方 OI | unavailable | TAIFEX Proxy |
| 自營商空方 OI | unavailable | TAIFEX Proxy |
| 自營商多空淨 OI | unavailable | TAIFEX Proxy |
| 三大法人合計多方 OI | 0 | TAIFEX Proxy |
| 三大法人合計空方 OI | 0 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +0 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | unavailable | TAIFEX Proxy |
| 投信多空淨 OI 變化 | unavailable | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | unavailable | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,291 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,052 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,239 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-02→2026-11-02) | +0 | TAIFEX Proxy snapshots (2026-11-03) |
- 資料日期：2026-11-02 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 68,904 | TAIFEX Proxy |
| 外資日盤空單交易量 | 71,286 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,382 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -2,141 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +2,625 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,898 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -169.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,376 | TAIFEX Proxy |
| 加權指數價格 | 44,920.14 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -1,544.14 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -3.44 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -1,544.14 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,376 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 78,044 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 68,904 | 71,286 | -2,382 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 82 | 2,223 | -2,141 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 9,523 | 6,898 | +2,625 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 78,509 | 80,407 | -1,898 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 94,291 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,052 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +14,239 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-02→2026-11-02) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | unavailable | TAIFEX Proxy |
| 夜盤漲跌點數 | unavailable | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 劇本分類 | unavailable | 規則對應 |
| 劇本條件 | unavailable | 規則對應 |
| 劇本特徵 | unavailable | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-04 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-04 02:12:59 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 244,760 | TAIFEX Proxy |
| Call 總未平倉量 OI | 96,494 | TAIFEX Proxy |
| Call OI 增減 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 199,896 | TAIFEX Proxy |
| Put 總未平倉量 OI | 40,135 | TAIFEX Proxy |
| Put OI 增減 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.22 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.40 | TAIFEX Proxy |
| Put／Call Ratio | 0.42 | TAIFEX Proxy |
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
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,900.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-04 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 43,006.60 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-04 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 140,211 | 139,870 | +341 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 200 | 5,246 | -5,046 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 123,594 | 135,042 | -11,448 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 264,005 | 280,158 | -16,153 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
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
| 買權多空淨 OI 變化 (2026-11-02→2026-11-02) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,297 | TAIFEX Proxy |
| 賣權空方 OI | 10,337 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,040 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-02→2026-11-02) | +0 | TAIFEX Proxy snapshots (2026-11-03) |
- 資料日期：買權 2026-11-02／賣權 2026-11-02 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-02→2026-11-02 | TAIFEX Proxy snapshots (2026-11-03) |
| 買權前十大 | +0 | 2026-11-02→2026-11-02 | TAIFEX Proxy snapshots (2026-11-03) |
| 賣權前十大 | +0 | 2026-11-02→2026-11-02 | TAIFEX Proxy snapshots (2026-11-03) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-04；資料時間：2026-11-04 02:12:59；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-03，非 T0 2026-11-04)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-03 非今日 2026-11-04，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-03 非今日 2026-11-04，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-03 非今日 2026-11-04，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-03 (T0 2026-11-04 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-03 (T0 2026-11-04 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-03；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151103, T0=1151104)
- 註記：三大法人回傳日期 20261103 (T0 20261104)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-03)，非 T0 2026-11-04
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,073.1 | unavailable | -2,382 | unavailable | +341 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +184.6 | unavailable | -2,141 | unavailable | -5,046 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -590.5 | unavailable | +2,625 | unavailable | -11,448 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
