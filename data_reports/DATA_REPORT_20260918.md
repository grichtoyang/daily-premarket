# DATA_REPORT_20260918

- 報告日期：`2026-09-21`
- T0 交易日期：`2026-09-18`
- 資料產出時間：`2026-09-21 08:08:04`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,180.75 | 點 | twse-proxy |
| 開盤 | 46,449.56 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,180.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,449.56 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,180.75 | 點 | twse-proxy |
| 漲跌點數 | 892.75 | 點 | twse-proxy |
| 漲跌幅 | +1.93 | % | twse-proxy |
| 成交金額 | 11,423.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 748 | twse-proxy |
| 下跌家數 | 251 | twse-proxy |
| 平盤家數 | 78 | twse-proxy |
| 漲停家數 | 32 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 565 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 219 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 84 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 34 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +869.9 | 億元 | twse-proxy /institutional |
| 投信 | +81.5 | 億元 | twse-proxy /institutional |
| 自營商 | +243.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +1,194.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,986.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +73.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 258,389 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 4,868 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | unavailable | % | istock.tw |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,519,861 | 張 | TWSE TWT96U + TPEX margin_sbl |
| 借券賣出餘額 | 35,424 | 張 | TWSE TWT96U + TPEX margin_sbl |
| 借券賣出增減 | -1,809 | 張 | TWSE TWT96U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 11,423.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,736.3 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,159.6 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,650.50 | 12.74 | +0.17 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,522.54 | 104.24 | +0.39 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,644.17 | 197.19 | +0.67 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,682.64 | -95.40 | -0.18 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,921.69 | 322.20 | +2.78 | Yahoo Finance Chart API |
| VIX | ^VIX | 14.81 | -0.63 | -4.08 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,018.95 | 882.70 | +1.38 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,894.23 | 178.82 | +2.66 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,750.78 | 146.49 | +0.60 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,911.87 | 36.27 | +0.94 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,640.87 | 230.96 | +1.72 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,734.50 | 77.15 | +1.01 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,030.00 | 416.32 | +1.41 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,207.00 | 446.00 | +0.86 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,887.80 | 14.57 | +0.51 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | 0.09 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.00 | 0.05 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.33 | 0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.81 | -0.04 | -0.14 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 100.29 | 0.07 | +0.06 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 156.96 | 0.83 | +0.53 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,386.28 | 6.75 | +0.49 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 434.67 | 4.41 | +1.02 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.61 | 0.14 | +0.57 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 41.63 | 1.64 | +4.10 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 95.67 | -4.63 | -4.62 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,411.00 | -13.90 | -0.31 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,450.25 | 216.57 | +0.27 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：CoWoS將一路夯到2027！小摩示警台積電擴產仍不夠　法人點名「它」將成最大受益者：仍有 15到20%短缺
  - 來源：Yahoo 台股；發布時間：2026-09-20T23:15:00Z；台北時間：2026-09-21 07:15
  - 摘要：[FTNN新聞網]記者何亞軒／綜合報導摩根大通（小摩）針對日月光投控（3711）出示報告，表示受惠於AI需求持續強勁，未來相關供應將更供不應求。對此，本土法人...
  - 原文連結：https://tw.stock.yahoo.com/news/cowos%E5%B0%87-%E8%B7%AF%E5%A4%AF%E5%88%B02027-%E5%B0%8F%E6%91%A9%E7%A4%BA%E8%AD%A6%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%93%B4%E7%94%A2%E4%BB%8D%E4%B8%8D%E5%A4%A0-%E6%B3%95%E4%BA%BA%E9%BB%9E%E5%90%8D-%E5%AE%83-231500714.html
- 事件2：法人喊買進　先進封裝15檔
  - 來源：Yahoo 台股；發布時間：2026-09-20T22:50:00Z；台北時間：2026-09-21 06:50
  - 摘要：AI與高效能運算需求強勁，推動半導體先進封裝與測試角色吃重。隨晶圓製程邁向先進奈米，異質整合與矽光子等技術使封裝複雜度大增，帶動單顆測試價值提升。台積電先進封裝產能供不應求，商機外溢至日月光投控、京元電子、力成、矽格等專業封測大廠。法人指出
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B3%95%E4%BA%BA%E5%96%8A%E8%B2%B7%E9%80%B2-%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D15%E6%AA%94-225000626.html
- 事件3：AI鬼故事滿天飛！Q4醞釀反轉　5大概念、23檔一次收
  - 來源：Yahoo 台股；發布時間：2026-09-20T22:05:00Z；台北時間：2026-09-21 06:05
  - 摘要：受AI巨頭呼籲監管減速與聯準會升息影響，科技股估值面臨修正壓力。本土法人指出，台股9月量縮震盪，資金轉向實質獲利標的，長假後醞釀反轉轉折。建議投資人聚焦先進製程、液冷散熱及金融防禦型個股，例如台積電、奇鋐、聯鈞等，並可透過高填息ETF或美債
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E9%AC%BC%E6%95%85%E4%BA%8B%E6%BB%BF%E5%A4%A9%E9%A3%9B-q4%E9%86%9E%E9%87%80%E5%8F%8D%E8%BD%89-5%E5%A4%A7%E6%A6%82%E5%BF%B5-23%E6%AA%94-%E6%AC%A1%E6%94%B6-220500076.html
- 事件4：大摩：全球AI半導體需求成長快速 看好台積電、聯發科等23檔台股
  - 來源：Yahoo 台股；發布時間：2026-09-20T14:30:23Z；台北時間：2026-09-20 22:30
  - 摘要：摩根士丹利證券（大摩）釋出報告指出，全球前14大上市雲端服務供應商（CSP）2028年的總資本支出成長將放慢至12%，AI半導體年複合增長率（CAGR）則高達30%。在供應鏈中，AI、記憶體、封測、半導體設備及成熟製程都將受惠，看好台積電、
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E6%91%A9-%E5%85%A8%E7%90%83ai%E5%8D%8A%E5%B0%8E%E9%AB%94%E9%9C%80%E6%B1%82%E6%88%90%E9%95%B7%E5%BF%AB%E9%80%9F-%E7%9C%8B%E5%A5%BD%E5%8F%B0%E7%A9%8D%E9%9B%BB-%E8%81%AF%E7%99%BC%E7%A7%91%E7%AD%8923%E6%AA%94%E5%8F%B0%E8%82%A1-143023999.html
- 事件5：LED雙雄交易太火熱！光鼎90日狂飆279%、週轉率破112%　「這檔」也同步入列14檔注意股出爐
  - 來源：Yahoo 台股；發布時間：2026-09-21T00:00:00Z；台北時間：2026-09-21 08:00
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導台股上週五（18日）加權指數一舉衝上47,180.75點，漲幅1.93％，證交所公布14檔注意股，被動元件指標廠禾伸堂（3026）在6個...
  - 原文連結：https://tw.stock.yahoo.com/news/led%E9%9B%99%E9%9B%84%E4%BA%A4%E6%98%93%E5%A4%AA%E7%81%AB%E7%86%B1-%E5%85%89%E9%BC%8E90%E6%97%A5%E7%8B%82%E9%A3%86279-%E9%80%B1%E8%BD%89%E7%8E%87%E7%A0%B4112-%E9%80%99%E6%AA%94-%E4%B9%9F%E5%90%8C%E6%AD%A5%E5%85%A5%E5%88%9714%E6%AA%94%E6%B3%A8%E6%84%8F%E8%82%A1%E5%87%BA%E7%88%90-000000307.html
- 事件6：光模塊貢獻上看250億元！法人喊「這低軌衛星大廠」旺季不旺沒關係　真正要注意的是1點：營收占比達半
  - 來源：Yahoo 台股；發布時間：2026-09-20T23:45:00Z；台北時間：2026-09-21 07:45
  - 摘要：[FTNN新聞網]記者何亞軒／綜合報導法人針對低軌衛星大廠華通（2313）出示報告，表示華通雖然第三季營運受到缺料、拉貨遞延等影響，表現不如預期，但隨著第四...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%89%E6%A8%A1%E5%A1%8A%E8%B2%A2%E7%8D%BB%E4%B8%8A%E7%9C%8B250%E5%84%84%E5%85%83-%E6%B3%95%E4%BA%BA%E5%96%8A-%E9%80%99%E4%BD%8E%E8%BB%8C%E8%A1%9B%E6%98%9F%E5%A4%A7%E5%BB%A0-%E6%97%BA%E5%AD%A3%E4%B8%8D%E6%97%BA%E6%B2%92%E9%97%9C%E4%BF%82-%E7%9C%9F%E6%AD%A3%E8%A6%81%E6%B3%A8%E6%84%8F%E7%9A%84%E6%98%AF1%E9%BB%9E-234500913.html
- 事件7：Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula
  - 來源：Federal Reserve；發布時間：Fri, 18 Sep 2026 15:00:00 GMT；台北時間：2026-09-18 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260918b.htm
- 事件8：Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services Company, Inc., and former employee of Regions Bank
  - 來源：Federal Reserve；發布時間：Fri, 18 Sep 2026 15:00:00 GMT；台北時間：2026-09-18 23:00
  - 摘要：Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services C
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260918a.htm
- 事件9：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- 事件10：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
- 事件11：‘It's awful’: How tariffs, soaring fuel costs and higher interest rates are squeezing American companies
  - 來源：CNBC；發布時間：Sun, 20 Sep 2026 12:47:23 GMT；台北時間：2026-09-20 20:47
  - 摘要：Tariffs, fuel prices and interest rates are squeezing American companies, particularly manufacturers, auto suppliers, retailers and transportation bus
  - 原文連結：https://www.cnbc.com/2026/09/20/tariffs-fuel-prices-and-interest-rates-squeeze-us-companies.html
- 事件12：Three words from Kevin Warsh have Wall Street wondering how far the Fed will go with rate hikes
  - 來源：CNBC；發布時間：Fri, 18 Sep 2026 18:28:31 GMT；台北時間：2026-09-19 02:28
  - 摘要：The chairman both explained this week's decision to raise interest rates, and raised vexing questions about what comes next
  - 原文連結：https://www.cnbc.com/2026/09/18/three-words-from-kevin-warsh-have-wall-street-wondering-how-far-the-fed-will-go-with-rate-hikes.html

## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-18

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,080 | TAIFEX Proxy |
| 最高價 | 47,464 | TAIFEX Proxy |
| 最低價 | 46,897 | TAIFEX Proxy |
| 收盤價 | 47,418 | TAIFEX Proxy |
| 漲跌點數 | +959 | TAIFEX Proxy |
| 漲跌幅 | +2.06 | TAIFEX Proxy |
| 成交量 | 65,824 | TAIFEX Proxy |
| 日盤高點及低點 | 47,464 / 46,897 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,594 | proxy |
| 最高價 | 47,205 | proxy |
| 最低價 | 46,538 | proxy |
| 收盤價 | 47,160 | proxy |
| 漲跌點數 | +701 | proxy |
| 漲跌幅 | +1.51 | proxy |
| 成交量 | 21,169 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,205 / 46,538 | proxy |
| 結算價 | 47,428 | TAIFEX Proxy |
| 未平倉量 | 101,893 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,323 | TAIFEX Proxy |
| 外資空方 OI | 86,433 | TAIFEX Proxy |
| 外資多空淨 OI | -76,110 | TAIFEX Proxy |
| 投信多方 OI | 78,053 | TAIFEX Proxy |
| 投信空方 OI | 2,943 | TAIFEX Proxy |
| 投信多空淨 OI | +75,110 | TAIFEX Proxy |
| 自營商多方 OI | 2,183 | TAIFEX Proxy |
| 自營商空方 OI | 5,375 | TAIFEX Proxy |
| 自營商多空淨 OI | -3,192 | TAIFEX Proxy |
| 三大法人合計多方 OI | 90,559 | TAIFEX Proxy |
| 三大法人合計空方 OI | 94,751 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -4,192 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +2,564 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,084 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -2,505 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,879 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,442 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,437 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：2026-09-18 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 39,435 | TAIFEX Proxy |
| 外資日盤空單交易量 | 36,914 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,521 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 11,356 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 12,552 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,196 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +3,717 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,084 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,084 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -2,437 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +410 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -2,847 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,168 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -786 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +109.5 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -74.5 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 47,418 | TAIFEX Proxy |
| 加權指數價格 | 47,180.75 | twse-proxy |
| 台指期與加權指數價差 | +237.25 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.50 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +237.25 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -258 | proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 47,418 | 47,160 | +258 | TAIFEX Proxy |
| 成交量 | 44,655 | 21,169 | +23,486 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,143（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 39,435 | 36,914 | +2,521 | 11,356 | 12,552 | -1,196 | +3,717 | 10,323 | 86,433 | -76,110 | +2,564 | TAIFEX Proxy |
| 投信 | 1,187 | 103 | +1,084 | 0 | 0 | +0 | +1,084 | 78,053 | 2,943 | +75,110 | +1,084 | TAIFEX Proxy |
| 自營商 | 3,420 | 5,857 | -2,437 | 671 | 261 | +410 | -2,847 | 2,183 | 5,375 | -3,192 | -2,505 | TAIFEX Proxy |
| 三大法人合計 | 44,042 | 42,874 | +1,168 | 12,027 | 12,813 | -786 | +1,954 | 90,559 | 94,751 | -4,192 | +1,143 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,879 | TAIFEX Proxy |
| 前十大交易人空方 OI | 70,442 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,437 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 端點未提供 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 32.16% | TAIFEX Proxy |
| 夜盤漲跌點數 | +701 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,196 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-18 | TAIFEX Proxy |
| 到期月份／到期日 | 202609F3 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-21 08:08:04 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 301,618 | TAIFEX Proxy |
| Call 總未平倉量 OI | 53,123 | TAIFEX Proxy |
| Call OI 增減 (2026-09-16→2026-09-18) | +36,106 | TAIFEX Proxy snapshots (2026-09-16) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 296,399 | TAIFEX Proxy |
| Put 總未平倉量 OI | 67,115 | TAIFEX Proxy |
| Put OI 增減 (2026-09-16→2026-09-18) | +54,451 | TAIFEX Proxy snapshots (2026-09-16) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.02 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 0.79 | TAIFEX Proxy |
| Put／Call Ratio | 1.26 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-17→2026-09-18) | -7.89 | TAIFEX OpenAPI |
| 與前一交易日比較 (OI 比 2026-09-17→2026-09-18) | -0.18 | TAIFEX OpenAPI |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call 部位 (夜盤淨口數) | +19 | TAIFEX Proxy |
| 外資 Put 部位 (夜盤淨口數) | -285 | TAIFEX Proxy |
| 外資 Call／Put 淨部位 (日盤淨口數) | +3,637 | TAIFEX Proxy |
| 外資部位增減 | unavailable | 端點未提供 |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call 部位 (夜盤淨口數) | -1,095 | TAIFEX Proxy |
| 自營商 Put 部位 (夜盤淨口數) | +1,059 | TAIFEX Proxy |
| 自營商 Call／Put 淨部位 (日盤淨口數) | +11,917 | TAIFEX Proxy |
| 自營商部位增減 | unavailable | 端點未提供 |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,200 | 3,649 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 3,181 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,500 | 2,775 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,200 | 3,649 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,200 | 3,649 | 6.87% | TAIFEX Proxy |
| C2 | 47,000 | 3,181 | 5.99% | TAIFEX Proxy |
| C3 | 47,500 | 2,775 | 5.22% | TAIFEX Proxy |
| C4 | 47,100 | 2,653 | 4.99% | TAIFEX Proxy |
| C5 | 47,150 | 2,619 | 4.93% | TAIFEX Proxy |
| C6 | 48,500 | 2,393 | 4.5% | TAIFEX Proxy |
| C7 | 47,200 | 2,240 | 4.22% | TAIFEX Proxy |
| C8 | 47,050 | 1,916 | 3.61% | TAIFEX Proxy |
| C9 | 48,000 | 1,796 | 3.38% | TAIFEX Proxy |
| C10 | 47,300 | 1,710 | 3.22% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,000 | 4,822 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,500 | 3,405 | TAIFEX Proxy |
| Put OI 第3大履約價 | 46,800 | 3,080 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,000 | 4,822 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,000 | 4,822 | 7.18% | TAIFEX Proxy |
| P2 | 46,500 | 3,405 | 5.07% | TAIFEX Proxy |
| P3 | 46,800 | 3,080 | 4.59% | TAIFEX Proxy |
| P4 | 46,900 | 2,806 | 4.18% | TAIFEX Proxy |
| P5 | 46,700 | 2,605 | 3.88% | TAIFEX Proxy |
| P6 | 46,000 | 2,592 | 3.86% | TAIFEX Proxy |
| P7 | 46,400 | 2,182 | 3.25% | TAIFEX Proxy |
| P8 | 46,950 | 2,132 | 3.18% | TAIFEX Proxy |
| P9 | 45,500 | 2,012 | 3.0% | TAIFEX Proxy |
| P10 | 47,100 | 2,007 | 2.99% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,200 (+3,458) | TAIFEX Proxy snapshots (2026-09-16) |
| Call OI 減少最多的履約價 | 45,300 (-189) | TAIFEX Proxy snapshots (2026-09-16) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,000 (+4,800) | TAIFEX Proxy snapshots (2026-09-16) |
| Put OI 減少最多的履約價 | 44,300 (-143) | TAIFEX Proxy snapshots (2026-09-16) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,200 | TAIFEX Proxy |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-18) | +2,200 | TAIFEX Proxy snapshots (2026-09-16) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-18) | +1,500 | TAIFEX Proxy snapshots (2026-09-16) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 資料日期 | 2026-09-18 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,515.02 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 資料日期 | 2026-09-18 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,900 | TAIFEX Proxy |
| 對應到期月份 | 202609F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-18) | +1,150 | TAIFEX Proxy snapshots (2026-09-16) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-18；資料時間：2026-09-21 08:08:04；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (5)：margin.ratio, futures.top10_change, options.chain_oi_change, options.pos_change, options.wall_change
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
- sbl：`TWSE TWT96U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (istock 失敗；官方無每日序列)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出餘額/增減為上櫃值 (上市 TWT93U 無機器接口)
- 本報告僅整理資料，不提供交易判斷。
