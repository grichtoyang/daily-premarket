# DATA_REPORT_20261116

- 報告日期：`2026-11-17`
- T0 交易日期：`2026-11-16`
- 資料產出時間：`2026-11-17 13:40:36`
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
| 加權指數 | 41,040.08 | 點 | twse-proxy |
| 開盤 | 43,512.42 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 43,512.42 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 41,040.08 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 41,040.08 | 點 | twse-proxy |
| 漲跌點數 | -2,635.04 | 點 | twse-proxy |
| 漲跌幅 | -6.03 | % | twse-proxy |
| 成交金額 | 9,031.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 99 | twse-proxy |
| 下跌家數 | 948 | twse-proxy |
| 平盤家數 | 36 | twse-proxy |
| 漲停家數 | 8 | twse-proxy |
| 跌停家數 | 83 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 97 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 746 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 35 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 24 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 85 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -701.9 | 億元 | twse-proxy /institutional |
| 投信 | -183.0 | 億元 | twse-proxy /institutional |
| 自營商 | -259.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,143.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 6,922.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -163.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 256,593 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 10,712 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 158.50 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,506,497 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 39,209 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 2,101 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,031.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,705.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,736.6 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,416.59 | -145.08 | -1.92 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,509.76 | -626.51 | -2.49 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,197.15 | -746.59 | -2.67 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,608.17 | -739.38 | -1.41 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,610.65 | -535.67 | -5.28 | Yahoo Finance Chart API |
| VIX | ^VIX | 22.91 | 3.61 | +18.70 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,065.07 | -596.95 | -1.00 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,004.08 | -96.42 | -1.89 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,602.49 | -151.35 | -0.64 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,595.02 | -7.55 | -0.21 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,698.10 | 7.32 | +0.07 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,440.25 | 1.25 | +0.02 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,384.00 | 99.75 | +0.37 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,546.00 | -124.00 | -0.24 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,743.70 | -7.70 | -0.28 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | -0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.12 | -0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.99 | 0.11 | +0.34 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.50 | -0.05 | -0.05 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.16 | -0.62 | -0.39 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,337.38 | 4.13 | +0.31 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 373.45 | -25.28 | -6.34 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.34 | -1.06 | -6.88 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.80 | -2.75 | -7.74 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 84.97 | -0.75 | -0.87 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,886.10 | 33.10 | +0.86 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,878.73 | -426.33 | -0.65 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：半導體設備股倒一片 萬潤跌停辛耘重挫
  - 來源：Yahoo 台股；發布時間：2026-11-17T05:00:00Z；台北時間：2026-11-17 13:00
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導台股今（17）日開低走低，開盤大跌493.44點至40546.64點，截至中午12點35分，暫報40168.31點，下跌871.77點，跌幅2.12%。半...
  - 原文連結：https://tw.stock.yahoo.com/news/10%E6%9C%88%E7%8D%B2%E5%88%A9%E6%9A%B4%E5%A2%9E110-%E4%BB%8D%E9%81%AD%E6%8F%90%E6%AC%BE-%E5%8D%8A%E5%B0%8E%E9%AB%94-%E9%80%99%E6%AA%94-%E9%A0%98%E8%B7%8C6-050000752.html
- 事件2：AI搶人燒到基層 技術員平均年薪逾80萬
  - 來源：Yahoo 台股；發布時間：2026-11-17T04:52:00Z；台北時間：2026-11-17 12:52
  - 摘要：受AI與先進封裝需求升溫影響，科技業技術員與作業員職缺連續三年增加，年增率達35%。知名半導體大廠祭出平均年薪破80萬元並放寬門檻搶人，日月光等企業亦擴大投資產能。面對少子化與人才斷層挑戰，近五成企業願調薪吸引人才，逾四成呼籲推動產學合作，
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%8D%E9%AB%98%E5%AD%B8%E6%AD%B7%E5%B9%B4%E8%96%AA%E7%A0%B480%E8%90%AC-%E5%8D%8A%E5%B0%8E%E9%AB%94%E5%A4%A7%E5%BB%A0%E6%80%A5%E6%90%B6-%E9%80%99%E9%A1%9E%E5%9F%BA%E5%B1%A4-%E8%BF%915%E6%88%90%E4%BC%81%E6%A5%AD%E9%A1%98%E5%8A%A0%E8%96%AA-045200803.html
- 事件3：護盤概念股誰先衝？鴻海等6檔一度漲逾2%
  - 來源：Yahoo 台股；發布時間：2026-11-17T04:20:22Z；台北時間：2026-11-17 12:20
  - 摘要：台股今（17）日早盤一度重挫1253.63點、下探39786.45點，跌破4萬點整數大關，隨後買盤拉抬，帶動加權指數不到半小時從低點急拉1747.39點，最高來到41533.84點、一度上漲493.76點，不過隨後再度翻黑。資深證券分析師鍾
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E6%92%90%E7%9B%A4%EF%BC%9F6%E6%AA%94%E3%80%8C%E8%AD%B7%E7%9B%A4%E6%A6%82%E5%BF%B5%E8%82%A1%E3%80%8D%E4%B8%80%E5%BA%A6%E6%BC%B2%E9%80%BE2-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E9%BB%9E%E7%81%AB%E8%B7%A1%E8%B1%A1%E6%98%8E%E9%A1%AF-042022839.html
- 事件4：輝達換帥牽動ETF 10檔曝險比重揭曉
  - 來源：Yahoo 台股；發布時間：2026-11-17T04:15:00Z；台北時間：2026-11-17 12:15
  - 摘要：[FTNN新聞網]記者陳雅婷／綜合報導台股今（17）日截至中午12時5分報40,395.20點，下跌644.88點，跌幅1.57%。台股昨（16）日才重挫2,635.04點，收在41,040.08...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E7%AA%81%E5%8D%B8%E4%BB%BB%E8%A1%9D%E6%93%8A%E5%8F%B0%E8%82%A1-10%E6%AA%94etf-%E8%97%8F%E8%BC%9D%E9%81%94%E6%9B%9D%E9%9A%AA-%E9%80%99%E6%AA%94%E6%8C%81%E8%82%A1%E6%AF%94%E9%87%8D%E6%9B%BE%E9%80%BE16-041500913.html
- 事件5：009827首換股就大風吹 新增5檔剔除6檔
  - 來源：Yahoo 台股；發布時間：2026-11-17T04:29:28Z；台北時間：2026-11-17 12:29
  - 摘要：玉山未來全球算力ETF（009827）今（17）日公布首次定期審核換股結果，此次新增5檔、剔除6檔成分股，其中SpaceX躍居第一大成分股，持股比重達18.26%，其次為微軟及輝達，權重分別為9.66%、9.52%。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8E%89%E5%B1%B1009827%E9%A6%96%E6%AC%A1%E6%8F%9B%E8%82%A1%E6%8F%AD%E6%9B%89%EF%BC%81%E6%96%B0%E5%A2%9E5%E6%AA%94%E3%80%81%E5%89%94%E9%99%A46%E6%AA%94-spacex%E8%BA%8D%E5%B1%85%E7%AC%AC%E4%B8%80%E5%A4%A7%E6%8C%81%E8%82%A1-042928934.html
- 事件6：「黎明前的黑暗」分析師籲留意止跌、抗跌股
  - 來源：Yahoo 台股；發布時間：2026-11-17T03:52:44Z；台北時間：2026-11-17 11:52
  - 摘要：「糖漿是外資解渴飲料」「糖漿把大家的退休金送給小兒」「你是糖漿還是撐盤狗 呵呵」「基本麵好吃記得吃好吃滿哦」「跌到忘記今天星期擠了」「糖漿是北七嗎 NV財報出來前狂買 之後不就瀑布殺？」
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E5%A4%A7%E7%9B%A4%E6%80%A5%E6%8B%89%E5%8D%83%E9%BB%9E%E5%BE%8C%E5%8F%88%E8%B5%B0%E8%B7%8C%E7%B6%B2%E5%93%80%E3%80%8C%E7%B3%96%E6%BC%BF%E6%98%AF%E5%A4%96%E8%B3%87%E8%A7%A3%E6%B8%B4%E9%A3%B2%E6%96%99%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E9%BB%9E%E9%97%9C%E9%8D%B5%EF%BC%9A%E9%81%B8%E8%82%A1%E4%B8%8D%E9%81%B8%E5%B8%82-035244694.html
- 事件7：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions, and changes to streamline and adjust their check services
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 18:30:00 GMT；台北時間：2026-11-13 02:30
  - 摘要：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions,
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261112a.htm
- 事件8：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 17:45:00 GMT；台北時間：2026-11-13 01:45
  - 摘要：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 16:00:00 GMT；台北時間：2026-11-13 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261112a.htm
- 事件10：Analysis: The Fed's chairman sees an AI revolution coming. Now he has to figure out what it means
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 00:42:33 GMT；台北時間：2026-11-17 08:42
  - 摘要：Kevin Warsh sees AI at a turning point. He faces tough questions on jobs and interest rates.
  - 原文連結：https://www.cnbc.com/2026/11/16/kevin-warsh-fed-ai-jobs-productivity-interest-rateshtml.html
- 事件11：Fed Chairman Kevin Warsh stresses importance of AI to economy, but says it could ‘disappoint’
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 18:46:07 GMT；台北時間：2026-11-17 02:46
  - 摘要：unavailable
  - 原文連結：https://www.cnbc.com/2026/11/16/fed-ai-task-force-kevin-warsh.html
- 事件12：U.S. crude oil declines to $85 a barrel on recovering Middle East exports
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 22:19:02 GMT；台北時間：2026-11-17 06:19
  - 摘要：Oil prices are falling as forecasts project a surplus in oil in the fourth quarter
  - 原文連結：https://www.cnbc.com/2026/11/16/us-crude-oil-declines-to-87-a-barrel-on-recovering-middle-east-exports.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-16

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,656 | TAIFEX Proxy |
| 最高價 | 43,672 | TAIFEX Proxy |
| 最低價 | 40,714 | TAIFEX Proxy |
| 收盤價 | 40,885 | TAIFEX Proxy |
| 漲跌點數 | -2,954 | TAIFEX Proxy |
| 漲跌幅 | -6.74 | TAIFEX Proxy |
| 成交量 | 167,772 | TAIFEX Proxy |
| 日盤高點及低點 | 43,672 / 40,714 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 40,900 | TAIFEX Proxy |
| 最高價 | 41,627 | TAIFEX Proxy |
| 最低價 | 40,616 | TAIFEX Proxy |
| 收盤價 | 40,935 | TAIFEX Proxy |
| 漲跌點數 | +154 | TAIFEX Proxy |
| 漲跌幅 | +0.38 | TAIFEX Proxy |
| 成交量 | 63,335 | TAIFEX Proxy |
| 夜盤高點及低點 | 41,627 / 40,616 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,030 | TAIFEX Proxy |
| 外資空方 OI | 108,817 | TAIFEX Proxy |
| 外資多空淨 OI | -96,787 | TAIFEX Proxy |
| 投信多方 OI | 95,851 | TAIFEX Proxy |
| 投信空方 OI | 3,445 | TAIFEX Proxy |
| 投信多空淨 OI | +92,406 | TAIFEX Proxy |
| 自營商多方 OI | 5,573 | TAIFEX Proxy |
| 自營商空方 OI | 4,414 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,159 | TAIFEX Proxy |
| 三大法人合計多方 OI | 113,454 | TAIFEX Proxy |
| 三大法人合計空方 OI | 116,676 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,222 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +4,083 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -7,517 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +3,930 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-11→2026-11-16) | -15,651 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 162,613 | TAIFEX Proxy |
| 外資日盤空單交易量 | 157,435 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +5,178 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 41,010 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 38,693 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,317 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +2,861 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -7,517 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -7,517 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +4,006 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -706 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +4,712 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,667 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,611 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +135.0 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +131.7 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,885 | TAIFEX Proxy |
| 加權指數價格 | 41,040.08 | twse-proxy |
| 台指期與加權指數價差 | -155.08 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.38 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -155.08 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +50 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,885 | 40,935 | -50 | TAIFEX Proxy |
| 成交量 | 167,772 | 63,335 | +104,437 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+496（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 162,613 | 157,435 | +5,178 | 41,010 | 38,693 | +2,317 | +2,861 | 12,030 | 108,817 | -96,787 | +4,083 | TAIFEX Proxy |
| 投信 | 51,979 | 59,496 | -7,517 | 0 | 0 | +0 | -7,517 | 95,851 | 3,445 | +92,406 | -7,517 | TAIFEX Proxy |
| 自營商 | 15,054 | 11,048 | +4,006 | 2,238 | 2,944 | -706 | +4,712 | 5,573 | 4,414 | +1,159 | +3,930 | TAIFEX Proxy |
| 三大法人合計 | 229,646 | 227,979 | +1,667 | 43,248 | 41,637 | +1,611 | +56 | 113,454 | 116,676 | -3,222 | +496 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-11→2026-11-16) | -15,651 | TAIFEX Proxy snapshots (2026-11-12) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 27.41% | TAIFEX Proxy |
| 夜盤漲跌點數 | +154 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,317 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-16 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-17 13:40:36 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 224,718 | TAIFEX Proxy |
| Call 總未平倉量 OI | 112,991 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 182,619 | TAIFEX Proxy |
| Put 總未平倉量 OI | 59,706 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.23 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.89 | TAIFEX Proxy |
| Put／Call Ratio | 0.53 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-13→2026-11-16) | -17.65 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-13→2026-11-16) | -3.96 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 54,791 | TAIFEX Proxy |
| 外資 Call日賣 | 55,135 | TAIFEX Proxy |
| 外資 Call日淨 | -344 | TAIFEX Proxy |
| 外資 Put日買 | 55,356 | TAIFEX Proxy |
| 外資 Put日賣 | 56,354 | TAIFEX Proxy |
| 外資 Put日淨 | -998 | TAIFEX Proxy |
| 外資 Call夜買 | 28,132 | TAIFEX Proxy |
| 外資 Call夜賣 | 27,501 | TAIFEX Proxy |
| 外資 Call夜淨 | +631 | TAIFEX Proxy |
| 外資 Put夜買 | 15,841 | TAIFEX Proxy |
| 外資 Put夜賣 | 16,953 | TAIFEX Proxy |
| 外資 Put夜淨 | -1,112 | TAIFEX Proxy |
| 外資 日盤淨總量 | +654 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -975 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +114 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 52,481 | TAIFEX Proxy |
| 自營商 Call日賣 | 63,527 | TAIFEX Proxy |
| 自營商 Call日淨 | -11,046 | TAIFEX Proxy |
| 自營商 Put日買 | 56,914 | TAIFEX Proxy |
| 自營商 Put日賣 | 51,589 | TAIFEX Proxy |
| 自營商 Put日淨 | +5,325 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,481 | TAIFEX Proxy |
| 自營商 Call夜賣 | 20,567 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,086 | TAIFEX Proxy |
| 自營商 Put夜買 | 19,141 | TAIFEX Proxy |
| 自營商 Put夜賣 | 18,195 | TAIFEX Proxy |
| 自營商 Put夜淨 | +946 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -16,371 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -7,960 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +4,379 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 9,318 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,500 | 7,874 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 5,357 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 9,318 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 9,318 | 8.25% | TAIFEX Proxy |
| C2 | 47,500 | 7,874 | 6.97% | TAIFEX Proxy |
| C3 | 44,000 | 5,357 | 4.74% | TAIFEX Proxy |
| C4 | 48,000 | 5,068 | 4.49% | TAIFEX Proxy |
| C5 | 45,000 | 4,329 | 3.83% | TAIFEX Proxy |
| C6 | 46,500 | 3,724 | 3.3% | TAIFEX Proxy |
| C7 | 43,000 | 3,567 | 3.16% | TAIFEX Proxy |
| C8 | 47,000 | 3,385 | 3.0% | TAIFEX Proxy |
| C9 | 48,500 | 3,253 | 2.88% | TAIFEX Proxy |
| C10 | 50,000 | 2,700 | 2.39% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 8,465 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 2,741 | TAIFEX Proxy |
| Put OI 第3大履約價 | 42,000 | 1,970 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 8,465 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 8,465 | 14.18% | TAIFEX Proxy |
| P2 | 40,000 | 2,741 | 4.59% | TAIFEX Proxy |
| P3 | 42,000 | 1,970 | 3.3% | TAIFEX Proxy |
| P4 | 38,000 | 1,697 | 2.84% | TAIFEX Proxy |
| P5 | 41,000 | 1,614 | 2.7% | TAIFEX Proxy |
| P6 | 44,000 | 1,562 | 2.62% | TAIFEX Proxy |
| P7 | 41,500 | 1,528 | 2.56% | TAIFEX Proxy |
| P8 | 39,000 | 1,513 | 2.53% | TAIFEX Proxy |
| P9 | 43,000 | 1,464 | 2.45% | TAIFEX Proxy |
| P10 | 42,500 | 1,297 | 2.17% | TAIFEX Proxy |


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
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 40,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,380.47 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,100 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 111,145 | 110,491 | +654 | 45,085 | 43,342 | +1,743 | -1,089 | TAIFEX Proxy |
| 投信 | 83 | 716 | -633 | 5 | 0 | +5 | -638 | TAIFEX Proxy |
| 自營商 | 104,070 | 120,441 | -16,371 | 35,676 | 39,708 | -4,032 | -12,339 | TAIFEX Proxy |
| 三大法人合計 | 215,298 | 231,648 | -16,350 | 80,766 | 83,050 | -2,284 | -14,066 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 18.66 | 17.98 | +0.68 | 5.96 | 5.34 | +0.62 | +0.06 | TAIFEX Proxy |
| 投信 | 0.01 | 0.55 | -0.54 | 0.00 | 0.00 | +0.00 | -0.54 | TAIFEX Proxy |
| 自營商 | 16.94 | 19.81 | -2.87 | 5.68 | 6.23 | -0.55 | -2.32 | TAIFEX Proxy |
| 三大法人合計 | 35.61 | 38.34 | -2.73 | 11.64 | 11.57 | +0.07 | -2.80 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 46,765 | TAIFEX Proxy |
| 買權空方 OI | 70,976 | TAIFEX Proxy |
| 買權多空淨 OI | -24,211 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-11→2026-11-16) | -19,234 | TAIFEX Proxy snapshots (2026-11-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 30,112 | TAIFEX Proxy |
| 賣權空方 OI | 28,929 | TAIFEX Proxy |
| 賣權多空淨 OI | +1,183 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-11→2026-11-16) | +3,690 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：買權 2026-11-16／賣權 2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -15,651 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |
| 買權前十大 | -19,234 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |
| 賣權前十大 | +3,690 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-16；資料時間：2026-11-17 13:40:36；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-11-16 非今日 2026-11-17，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202611F2→新202611），日對日 OI/Walls 變化不適用

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
| 外資 | -701.9 | -96,787 | +5,178 | +2,317 | +654 | +1,743 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | -183.0 | +92,406 | -7,517 | +0 | -633 | +5 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -259.0 | +1,159 | +4,006 | -706 | -16,371 | -4,032 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
