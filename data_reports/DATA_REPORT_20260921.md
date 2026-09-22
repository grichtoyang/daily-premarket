# DATA_REPORT_20260921

- 報告日期：`2026-09-22`
- T0 交易日期：`2026-09-21`
- 資料產出時間：`2026-09-22 10:18:24`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,718.84 | 點 | twse-proxy |
| 開盤 | 47,207.30 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,750.98 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,207.30 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,718.84 | 點 | twse-proxy |
| 漲跌點數 | 538.09 | 點 | twse-proxy |
| 漲跌幅 | +1.14 | % | twse-proxy |
| 成交金額 | 8,668.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 484 | twse-proxy |
| 下跌家數 | 498 | twse-proxy |
| 平盤家數 | 95 | twse-proxy |
| 漲停家數 | 32 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 438 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 343 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 94 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 34 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +204.8 | 億元 | twse-proxy /institutional |
| 投信 | +46.0 | 億元 | twse-proxy /institutional |
| 自營商 | +227.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +478.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,097.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +111.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 270,468 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 12,082 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 191.44 | % | wantgoo 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,531,587 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 38,886 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 3,463 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,668.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,125.7 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,793.9 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,764.70 | 114.20 | +1.49 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,122.09 | 599.55 | +2.26 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,482.35 | 838.18 | +2.83 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,048.83 | 366.19 | +0.71 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,433.17 | 511.48 | +4.29 | Yahoo Finance Chart API |
| VIX | ^VIX | 14.87 | 0.06 | +0.41 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,018.95 | 882.70 | +1.38 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,123.75 | 116.03 | +1.66 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 25,128.20 | 85.49 | +0.34 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,965.39 | 15.48 | +0.39 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,897.13 | 167.11 | +1.22 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,835.75 | 2.25 | +0.03 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,883.00 | 98.25 | +0.32 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,404.00 | -71.00 | -0.14 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,895.10 | -2.30 | -0.08 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.96 | -0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.69 | -0.12 | -0.37 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 100.43 | 0.00 | +0.00 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.50 | 0.45 | +0.29 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,360.98 | -23.88 | -1.72 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 445.14 | 10.47 | +2.41 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 25.43 | 0.82 | +3.33 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.73 | 2.10 | +5.04 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 92.99 | -2.79 | -2.91 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,381.90 | -2.00 | -0.05 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 85,580.17 | 4,437.56 | +5.47 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：抽中一張賺近250萬 漢測上櫃首日狂飆坐穩「三哥」
  - 來源：Yahoo 台股；發布時間：2026-09-22T01:25:08Z；台北時間：2026-09-22 09:25
  - 摘要：「漢民集團」旗下金雞母、半導體測試設備廠漢測（7856）今（22）日正式掛牌上櫃，蜜月首日最高價站上4475元，較承銷價2250元翻倍飆漲110%，剛掛牌就創上櫃第三高價，僅次於股王信驊（5274）及上櫃股后旺矽（6223）。而這家新股曾虧
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%98%94%E6%97%A5%E6%9B%BE%E9%80%A3%E8%99%A710%E5%B9%B4%EF%BC%81%E6%BC%A2%E6%B8%AC%E6%8E%9B%E7%89%8C%E9%A6%96%E6%97%A5%E7%A0%B44475%E5%85%83%E7%99%BB%E4%B8%8A%E6%AB%83%E3%80%8C%E4%B8%89%E5%93%A5%E3%80%8D%E5%AF%B6%E5%BA%A7-012508764.html
- 事件2：魏哲家一句「趕上聯發科」台積衝出近月盤中最高價
  - 來源：Yahoo 台股；發布時間：2026-09-22T01:27:06Z；台北時間：2026-09-22 09:27
  - 摘要：魏哲家一句「希望台積電股價趕快趕上聯發科」，市場樂看神山股價要起飛，台積電（2330）今（22）日盤中最高觸及2510元，上漲30元，股價創下9月初以來、近一個月盤中最高價。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%AD%8F%E5%93%B2%E5%AE%B6%E4%B8%80%E5%80%8B%E6%9A%97%E8%99%9F%EF%BC%81%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%BC%B230%E5%85%83%E8%87%B32510%E5%85%83-%E8%BF%91%E4%B8%80%E5%80%8B%E6%9C%88%E7%9B%A4%E4%B8%AD%E6%9C%80%E9%AB%98%E5%83%B9-012706948.html
- 事件3：iPhone Duo下月開賣 量產卡關良率僅約60%
  - 來源：Yahoo 台股；發布時間：2026-09-21T22:42:46Z；台北時間：2026-09-22 06:42
  - 摘要：陸媒報導，蘋果首款折疊機iPhone Duo距10月23日開賣只剩一個多月，但量產爬坡仍未達標，由於蘋果今年最有亮點的新產品就是iPhone Duo，如今量產「卡卡」，恐牽動今年蘋果整體iPhone銷售量，進而影響台積電、大立光、鴻海、新日
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8A%98%E7%96%8Aiphone%E9%87%8F%E7%94%A2%E5%8D%A1%E9%97%9C-%E7%89%BD%E5%8B%95%E8%98%8B%E6%9E%9C%E4%BB%8A%E5%B9%B4%E6%95%B4%E9%AB%94%E6%89%8B%E6%A9%9F%E9%8A%B7%E5%94%AE%E9%87%8F-224246845.html
- 事件4：市場熱烈追價友達 法人態度審慎：本業恐轉為虧損
  - 來源：Yahoo 台股；發布時間：2026-09-21T23:57:42Z；台北時間：2026-09-22 07:57
  - 摘要：面板大廠友達近期成為市場焦點，傳聞英特爾與台積電有意在先進封裝及Micro LED領域展開合作，帶動友達股價爆量強攻漲停。對此，英特爾不予置評，友達董事長彭双浪則證實正與夥伴開發玻璃基板等技術，但未透露合作細節。然而，法人態度轉趨審慎，分析
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9D%A2%E6%9D%BF%E5%A4%A7%E5%BB%A0%E7%88%8681%E8%90%AC%E5%BC%B5%E4%BA%AE%E7%87%88%E6%BC%B2%E5%81%9C-%E5%85%A9%E5%A4%A7%E5%B7%A8%E9%A0%AD%E6%90%B6%E5%90%88%E4%BD%9C-%E5%85%A9%E5%A4%A7%E6%B3%95%E4%BA%BA%E5%8D%BB%E7%9C%8B%E8%A1%B0-%E5%8E%9F%E5%9B%A0%E6%9B%9D-204700843.html
- 事件5：漢測今重磅上櫃 前7月營收已超車去年全年
  - 來源：Yahoo 台股；發布時間：2026-09-22T00:26:00Z；台北時間：2026-09-22 08:26
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導半導體測試介面大廠漢測（7856）今（22）日掛牌上櫃，將成為上櫃市場重磅新成員！日前漢測進行上櫃前公開申購，不但承銷價...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%94%B3%E8%B3%BC%E5%87%8D%E7%B5%908656%E5%84%84%E5%85%83%E7%A0%B4%E7%B4%80%E9%8C%84-%E6%BC%A2%E6%B8%AC%E4%BB%8A%E6%8C%BE215%E5%84%84%E9%87%8D%E7%A3%85%E4%B8%8A%E6%AB%83-%E5%89%8D7%E6%9C%88%E7%87%9F%E6%94%B6%E5%8D%B3%E8%B6%85%E8%BB%8A%E5%8E%BB%E5%B9%B4%E5%85%A8%E5%B9%B4-002600084.html
- 事件6：分潤制度遭「已讀不回」台灣美光工會將發動罷工投票
  - 來源：Yahoo 台股；發布時間：2026-09-21T13:44:00Z；台北時間：2026-09-21 21:44
  - 摘要：台灣美光勞資爭議持續延燒，今日美光與桃園工會的調解會議中並未達成共識，預計10月22日將與台中工會再舉行調解會議。美光工會表示，美光公司仍然沒有對員工最關心的「分潤制度」提出具體方案，沒有方案的回應不僅不尊重工會成員，更讓員工的不滿到達了極
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%88%86%E6%BD%A4%E5%88%B6%E5%BA%A6%E6%B2%92%E4%B8%8B%E6%96%87-%E7%BE%8E%E5%85%89%E5%B7%A5%E6%9C%83%E5%B0%87%E7%99%BC%E5%8B%95%E7%BD%B7%E5%B7%A5%E6%8A%95%E7%A5%A8-%E8%AA%BF%E8%A7%A3%E6%B2%92%E5%85%B1%E8%AD%98-%E5%93%A1%E5%B7%A5%E4%B8%8D%E6%BB%BF%E5%88%B0%E6%A5%B5%E9%99%90-134400390.html
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
  - 來源：CNBC；發布時間：Mon, 21 Sep 2026 15:04:04 GMT；台北時間：2026-09-21 23:04
  - 摘要：Tariffs, fuel prices and interest rates are squeezing American companies, particularly manufacturers, auto suppliers, retailers and transportation bus
  - 原文連結：https://www.cnbc.com/2026/09/20/tariffs-fuel-prices-and-interest-rates-squeeze-us-companies.html
- 事件12：Stocks had a great day on the surface. But something alarming occurred not seen since 1999
  - 來源：CNBC；發布時間：Mon, 21 Sep 2026 21:20:41 GMT；台北時間：2026-09-22 05:20
  - 摘要：The market just posted major gains, but the latest performance is not as strong as it may seem.
  - 原文連結：https://www.cnbc.com/2026/09/21/stocks-had-a-great-day-on-the-surface-but-something-alarming-occurred-not-seen-since-1999.html


### 9. 產業資金流向 (股市智投)

**資料來源：** `StockIntelli API` — https://www.stockintelli.com/market/industry-flow

- unavailable (StockIntelli API 速率限制或回應異常)

## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-21

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,607 | TAIFEX Proxy |
| 最高價 | 48,091 | TAIFEX Proxy |
| 最低價 | 47,496 | TAIFEX Proxy |
| 收盤價 | 48,077 | TAIFEX Proxy |
| 漲跌點數 | +649 | TAIFEX Proxy |
| 漲跌幅 | +1.37 | TAIFEX Proxy |
| 成交量 | 59,264 | TAIFEX Proxy |
| 日盤高點及低點 | 48,091 / 47,496 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,494 | proxy |
| 最高價 | 47,584 | proxy |
| 最低價 | 47,208 | proxy |
| 收盤價 | 47,405 | proxy |
| 漲跌點數 | -23 | proxy |
| 漲跌幅 | -0.05 | proxy |
| 成交量 | 21,514 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,584 / 47,208 | proxy |
| 結算價 | 48,053 | TAIFEX Proxy |
| 未平倉量 | 101,502 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,318 | TAIFEX Proxy |
| 外資空方 OI | 84,399 | TAIFEX Proxy |
| 外資多空淨 OI | -74,081 | TAIFEX Proxy |
| 投信多方 OI | 76,936 | TAIFEX Proxy |
| 投信空方 OI | 2,917 | TAIFEX Proxy |
| 投信多空淨 OI | +74,019 | TAIFEX Proxy |
| 自營商多方 OI | 2,199 | TAIFEX Proxy |
| 自營商空方 OI | 5,553 | TAIFEX Proxy |
| 自營商多空淨 OI | -3,354 | TAIFEX Proxy |
| 三大法人合計多方 OI | 89,453 | TAIFEX Proxy |
| 三大法人合計空方 OI | 92,869 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,416 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +2,029 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -1,091 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -162 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,066 | TAIFEX Proxy |
| 前十大交易人空方 OI | 69,303 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,763 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：2026-09-21 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 33,783 | TAIFEX Proxy |
| 外資日盤空單交易量 | 31,749 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,034 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 11,094 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 10,839 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +255 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,779 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -1,091 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -1,091 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -138 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +73 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -211 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +805 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +328 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +77.9 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +31.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,077 | TAIFEX Proxy |
| 加權指數價格 | 47,718.84 | twse-proxy |
| 台指期與加權指數價差 | +358.16 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.75 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +358.16 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -672 | proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,077 | 47,405 | +672 | TAIFEX Proxy |
| 成交量 | 37,750 | 21,514 | +16,236 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+776（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 33,783 | 31,749 | +2,034 | 11,094 | 10,839 | +255 | +1,779 | 10,318 | 84,399 | -74,081 | +2,029 | TAIFEX Proxy |
| 投信 | 112 | 1,203 | -1,091 | 0 | 0 | +0 | -1,091 | 76,936 | 2,917 | +74,019 | -1,091 | TAIFEX Proxy |
| 自營商 | 3,731 | 3,869 | -138 | 441 | 368 | +73 | -211 | 2,199 | 5,553 | -3,354 | -162 | TAIFEX Proxy |
| 三大法人合計 | 37,626 | 36,821 | +805 | 11,535 | 11,207 | +328 | +477 | 89,453 | 92,869 | -3,416 | +776 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,066 | TAIFEX Proxy |
| 前十大交易人空方 OI | 69,303 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,763 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 端點未提供 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 36.30% | TAIFEX Proxy |
| 夜盤漲跌點數 | -23 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +255 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-21 | TAIFEX Proxy |
| 到期月份／到期日 | 202609W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-22 10:18:24 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 115,764 | TAIFEX Proxy |
| Call 總未平倉量 OI | 30,570 | TAIFEX Proxy |
| Call OI 增減 (2026-09-16→2026-09-21) | +24,539 | TAIFEX Proxy snapshots (2026-09-16) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 144,629 | TAIFEX Proxy |
| Put 總未平倉量 OI | 36,042 | TAIFEX Proxy |
| Put OI 增減 (2026-09-16→2026-09-21) | +31,338 | TAIFEX Proxy snapshots (2026-09-16) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.80 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 0.85 | TAIFEX Proxy |
| Put／Call Ratio | 1.18 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-18→2026-09-21) | 25.75 | TAIFEX OpenAPI |
| 與前一交易日比較 (OI 比 2026-09-18→2026-09-21) | 19.88 | TAIFEX OpenAPI |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call 部位 (夜盤淨口數) | +25 | TAIFEX Proxy |
| 外資 Put 部位 (夜盤淨口數) | +372 | TAIFEX Proxy |
| 外資 Call／Put 淨部位 (日盤淨口數) | -394 | TAIFEX Proxy |
| 外資部位增減 | unavailable | 端點未提供 |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call 部位 (夜盤淨口數) | -1,148 | TAIFEX Proxy |
| 自營商 Put 部位 (夜盤淨口數) | -1,464 | TAIFEX Proxy |
| 自營商 Call／Put 淨部位 (日盤淨口數) | +851 | TAIFEX Proxy |
| 自營商部位增減 | unavailable | 端點未提供 |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 1,485 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,000 | 1,336 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,500 | 1,163 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 1,485 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 1,485 | 4.86% | TAIFEX Proxy |
| C2 | 48,000 | 1,336 | 4.37% | TAIFEX Proxy |
| C3 | 47,500 | 1,163 | 3.8% | TAIFEX Proxy |
| C4 | 50,000 | 1,086 | 3.55% | TAIFEX Proxy |
| C5 | 48,600 | 1,062 | 3.47% | TAIFEX Proxy |
| C6 | 52,000 | 1,049 | 3.43% | TAIFEX Proxy |
| C7 | 50,500 | 985 | 3.22% | TAIFEX Proxy |
| C8 | 47,200 | 926 | 3.03% | TAIFEX Proxy |
| C9 | 46,900 | 912 | 2.98% | TAIFEX Proxy |
| C10 | 48,400 | 837 | 2.74% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,000 | 1,760 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,000 | 1,507 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,000 | 1,419 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,000 | 1,760 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,000 | 1,760 | 4.88% | TAIFEX Proxy |
| P2 | 46,000 | 1,507 | 4.18% | TAIFEX Proxy |
| P3 | 45,000 | 1,419 | 3.94% | TAIFEX Proxy |
| P4 | 46,500 | 1,409 | 3.91% | TAIFEX Proxy |
| P5 | 46,400 | 1,316 | 3.65% | TAIFEX Proxy |
| P6 | 44,000 | 1,045 | 2.9% | TAIFEX Proxy |
| P7 | 46,600 | 985 | 2.73% | TAIFEX Proxy |
| P8 | 46,700 | 970 | 2.69% | TAIFEX Proxy |
| P9 | 46,800 | 931 | 2.58% | TAIFEX Proxy |
| P10 | 45,700 | 915 | 2.54% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,500 (+1,277) | TAIFEX Proxy snapshots (2026-09-16) |
| Call OI 減少最多的履約價 | 49,900 (-92) | TAIFEX Proxy snapshots (2026-09-16) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,000 (+1,753) | TAIFEX Proxy snapshots (2026-09-16) |
| Put OI 減少最多的履約價 | 42,200 (-46) | TAIFEX Proxy snapshots (2026-09-16) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-21) | +2,500 | TAIFEX Proxy snapshots (2026-09-16) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-21) | +1,500 | TAIFEX Proxy snapshots (2026-09-16) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 資料日期 | 2026-09-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,530.33 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 資料日期 | 2026-09-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-16→2026-09-21) | +1,250 | TAIFEX Proxy snapshots (2026-09-16) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-21；資料時間：2026-09-22 10:18:24；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (1)：futures.top10_change
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
- margin_ratio：`wantgoo 大盤融資維持率 (民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。
