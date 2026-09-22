# DATA_REPORT_20260922

- 報告日期：`2026-09-22`
- T0 交易日期：`2026-09-22`
- 資料產出時間：`2026-09-22 17:41:36`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,800.17 | 點 | twse-proxy |
| 開盤 | 47,981.04 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,601.53 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,800.17 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,800.17 | 點 | twse-proxy |
| 漲跌點數 | 81.33 | 點 | twse-proxy |
| 漲跌幅 | +0.17 | % | twse-proxy |
| 成交金額 | 10,787.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 330 | twse-proxy |
| 下跌家數 | 636 | twse-proxy |
| 平盤家數 | 113 | twse-proxy |
| 漲停家數 | 14 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 270 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 514 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 88 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 12 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +447.3 | 億元 | twse-proxy /institutional |
| 投信 | +2.4 | 億元 | twse-proxy /institutional |
| 自營商 | +158.5 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +608.2 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 231,582 | 張 | HiStock |
| 融券增減 | 10,189 | 張 | HiStock |
| 融資維持率 | 191.44 | % | wantgoo 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,437,911 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,787.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,770.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 13,558.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

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
| VIX | ^VIX | 14.90 | 0.03 | +0.20 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,018.95 | 882.70 | +1.38 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,017.91 | 10.19 | +0.15 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 25,087.75 | 45.04 | +0.18 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,952.13 | 2.22 | +0.06 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,723.74 | -6.28 | -0.05 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,830.00 | -3.50 | -0.04 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,786.75 | 2.00 | +0.01 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,502.00 | 27.00 | +0.05 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,901.00 | 3.60 | +0.12 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | 0.00 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.96 | -0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.67 | -0.14 | -0.43 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 100.43 | 0.00 | +0.00 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.11 | 0.07 | +0.04 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,356.98 | -27.88 | -2.01 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 91.10 | -4.68 | -4.89 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,352.40 | -31.50 | -0.72 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 86,004.14 | -598.77 | -0.69 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股創高後大甩尾 信驊登兩萬金 友達百萬成交量搶鏡
  - 來源：Yahoo 台股；發布時間：2026-09-22T08:09:08Z；台北時間：2026-09-22 16:09
  - 摘要：台股創高卻上演近900點震盪！今（22）日受美股科技股強力反彈激勵，加權指數開高一度衝破歷史高點，刷出48,601點的新高點，然而隨即高檔獲利了結以及連續假期前的調節賣壓逐步湧現，加上台積電(2330)由紅翻黑，讓盤中的漲幅不斷收斂，終場僅
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%88%B748601%E9%BB%9E%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98%EF%BC%81%E6%BC%B2%E5%B9%85%E6%94%B6%E6%96%82%E4%BB%8D%E5%89%B5%E6%94%B6%E7%9B%A4%E7%B4%80%E9%8C%84-%E4%BF%A1%E9%A9%8A%E7%99%BB%E9%A6%96%E6%AA%94%E3%80%8C%E5%85%A9%E8%90%AC%E9%87%91%E3%80%8D-%E5%8F%8B%E9%81%94%E7%88%86115%E8%90%AC%E5%BC%B5%E9%A9%9A%E5%A4%A9%E5%B7%A8%E9%87%8F-%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-080908250.html
- 事件2：台股儀表板揭開融資斷頭違約 只報總數不公布個股
  - 來源：Yahoo 台股；發布時間：2026-09-22T09:03:21Z；台北時間：2026-09-22 17:03
  - 摘要：台股融資斷頭、不限用途借款、違約交割等市場關心的台股資訊全都露！金管會證期局副局長黃厚銘今（22）日下午正式宣布，台股儀表板明天（23日）將正式上路，優先整合推出「授信業務」、「違約概況」及「上市櫃公司營收」三大面向資訊。他舉例，信用交易擔
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%9E%8D%E8%B3%87%E6%96%B7%E9%A0%AD%E9%81%95%E7%B4%84%E5%85%A8%E9%83%BD%E9%9C%B2%EF%BC%9F%E5%8F%B0%E8%82%A1%E5%84%80%E8%A1%A8%E6%9D%BF23%E6%97%A5%E6%AD%A3%E5%BC%8F%E4%B8%8A%E7%B7%9A-%E5%80%8B%E8%82%A1%E4%BB%8D%E6%9C%AA%E5%85%AC%E5%B8%83-090321422.html
- 事件3：黃仁勳喊AI下一棒輪資安接力 台股4路概念股全盤點
  - 來源：Yahoo 台股；發布時間：2026-09-22T07:47:53Z；台北時間：2026-09-22 15:47
  - 摘要：AI浪潮不只帶動算力與應用需求，網路安全的重要性也更上一層樓。AI教父黃仁勳日前登高一呼，看好網路安全將成為AI下一波重點應用，激勵相關概念股走高。黃仁勳到底說了什麼？所謂的資安包括哪些範圍？如何布局資安股？Yahoo財經編輯室將盤點台股的
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E8%B6%8A%E4%BE%86%E8%B6%8A%E5%BC%B7%E2%8B%AF%E9%BB%83%E4%BB%81%E5%8B%B3%E9%96%8B%E9%87%91%E5%8F%A3%E9%BB%9E%E5%90%8D%E3%80%8C%E8%B3%87%E5%AE%89%E3%80%8D%E6%88%90%E4%B8%8B%E4%B8%80%E6%B3%A2%E9%87%8D%E9%BB%9E%E6%87%89%E7%94%A8-%E5%8F%B0%E8%82%A1%E7%9B%B8%E9%97%9C%E6%97%8F%E7%BE%A44%E5%A4%A7%E9%A1%9E%E4%B8%80%E8%B5%B7%E7%9C%8B%EF%BC%81%EF%BD%9C%E7%9B%A4%E9%BB%9E%E6%A6%82%E5%BF%B5%E8%82%A1-100000941.html
- 事件4：新鮮人還在排隊找工作 8月失業率連3月上升
  - 來源：Yahoo 台股；發布時間：2026-09-22T08:35:52Z；台北時間：2026-09-22 16:35
  - 摘要：畢業季持續推升失業率，主計總處今（22）日公布，今年8月失業率為3.41%，較上月上升0.02個百分點，連續3個月走升，不過仍創近26年同期低點。主計總處國勢普查處副處長譚文玲表示，8月失業率上升主要仍受到應屆畢業生投入求職市場的季節性因素
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%95%A2%E6%A5%AD%E7%94%9F%E9%82%84%E5%9C%A8%E6%89%BE%E5%B7%A5%E4%BD%9C%EF%BC%818%E6%9C%88%E5%A4%B1%E6%A5%AD%E7%8E%87%E5%8D%87%E8%87%B3341-%E9%80%A33%E6%9C%88%E4%B8%8A%E5%8D%87-083552873.html
- 事件5：新青安買氣退燒？五大行申貸占比摔近10個月新低
  - 來源：Yahoo 台股；發布時間：2026-09-22T09:08:26Z；台北時間：2026-09-22 17:08
  - 摘要：央行今（22）日公布8月五大銀行新承做房貸金額為571億元，月減119億元，終結連三升，央行官員分析，主要有三個原因，其中是傳統鬼月觀望氣氛與颱風假干擾銀行作業之外，還有一部份的人覺得新青安 3.0管制趨嚴已提前「上車」，這也讓新青安占比衰
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E9%9D%92%E5%AE%89%E6%95%88%E6%87%89%E9%80%80%E7%87%92%EF%BC%9F8%E6%9C%88%E4%BA%94%E5%A4%A7%E9%8A%80%E8%A1%8C%E7%94%B3%E8%B2%B8%E5%8D%A0%E6%AF%94%E5%89%B5%E8%BF%9110%E5%80%8B%E6%9C%88%E6%96%B0%E4%BD%8E-090826227.html
- 事件6：掛牌首日飆4995元封上櫃「三哥」！漢測中籤戶秒賺274.5萬　昔連虧10年、前8月營收暴增125%
  - 來源：Yahoo 台股；發布時間：2026-09-22T09:30:00Z；台北時間：2026-09-22 17:30
  - 摘要：[FTNN新聞網]記者薛明峻／台北報導曾一度連虧10年的半導體測試介面大廠漢測（7856），今（22）日以每股承銷價2250元正式從興櫃轉上櫃交易，首日展現蜜月行情...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8E%9B%E7%89%8C%E9%A6%96%E6%97%A5%E9%A3%864995%E5%85%83%E5%B0%81%E4%B8%8A%E6%AB%83-%E4%B8%89%E5%93%A5-%E6%BC%A2%E6%B8%AC%E4%B8%AD%E7%B1%A4%E6%88%B6%E7%A7%92%E8%B3%BA274-5%E8%90%AC-%E6%98%94%E9%80%A3%E8%99%A710%E5%B9%B4-093000667.html
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
- 事件11：Trump, Xi seek trade stability and deals, but AI, tariffs and Iran loom large. What to watch
  - 來源：CNBC；發布時間：Mon, 21 Sep 2026 22:25:33 GMT；台北時間：2026-09-22 06:25
  - 摘要：Trump, facing low approval on the economy ahead of the midterm election, has an added incentive to emerge from the summit with China's Xi touting trad
  - 原文連結：https://www.cnbc.com/2026/09/21/trump-xi-china-summit-trade-tariffs.html
- 事件12：U.S. Treasury yields ease as investors await fresh jobs data, Fed comments
  - 來源：CNBC；發布時間：Tue, 22 Sep 2026 09:16:10 GMT；台北時間：2026-09-22 17:16
  - 摘要：Economic data, the Iran war and looming UN meetings are in focus.
  - 原文連結：https://www.cnbc.com/2026/09/22/treasury-yield-us-bond-market-trump.html


### 9. 產業資金流向 (股市智投)

**資料來源：** `StockIntelli API` — https://www.stockintelli.com/market/industry-flow

- unavailable (StockIntelli API 速率限制或回應異常)

## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-22

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,888 | TAIFEX Proxy |
| 最高價 | 48,946 | TAIFEX Proxy |
| 最低價 | 48,034 | TAIFEX Proxy |
| 收盤價 | 48,243 | TAIFEX Proxy |
| 漲跌點數 | +190 | TAIFEX Proxy |
| 漲跌幅 | +0.40 | TAIFEX Proxy |
| 成交量 | 62,576 | TAIFEX Proxy |
| 日盤高點及低點 | 48,946 / 48,034 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,121 | TAIFEX Proxy |
| 最高價 | 48,805 | TAIFEX Proxy |
| 最低價 | 48,105 | TAIFEX Proxy |
| 收盤價 | 48,781 | TAIFEX Proxy |
| 漲跌點數 | +728 | TAIFEX Proxy |
| 漲跌幅 | +1.51 | TAIFEX Proxy |
| 成交量 | 20,885 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,805 / 48,105 | TAIFEX Proxy |
| 結算價 | 48,225 | TAIFEX Proxy |
| 未平倉量 | 102,946 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,740 | TAIFEX Proxy |
| 外資空方 OI | 86,308 | TAIFEX Proxy |
| 外資多空淨 OI | -75,568 | TAIFEX Proxy |
| 投信多方 OI | 76,891 | TAIFEX Proxy |
| 投信空方 OI | 2,914 | TAIFEX Proxy |
| 投信多空淨 OI | +73,977 | TAIFEX Proxy |
| 自營商多方 OI | 2,314 | TAIFEX Proxy |
| 自營商空方 OI | 5,772 | TAIFEX Proxy |
| 自營商多空淨 OI | -3,458 | TAIFEX Proxy |
| 三大法人合計多方 OI | 89,945 | TAIFEX Proxy |
| 三大法人合計空方 OI | 94,994 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,049 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,487 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -42 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -104 | TAIFEX Proxy |

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
| 外資日盤多單交易量 | 33,568 | TAIFEX Proxy |
| 外資日盤空單交易量 | 35,050 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,482 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 11,094 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 10,839 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +255 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,737 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -42 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -42 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -106 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +73 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -179 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,630 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +328 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -157.9 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +31.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,243 | TAIFEX Proxy |
| 加權指數價格 | 47,800.17 | twse-proxy |
| 台指期與加權指數價差 | +442.83 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.93 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +442.83 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +538 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,243 | 48,781 | -538 | TAIFEX Proxy |
| 成交量 | 41,691 | 20,885 | +20,806 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,633（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 33,568 | 35,050 | -1,482 | 11,094 | 10,839 | +255 | -1,737 | 10,740 | 86,308 | -75,568 | -1,487 | TAIFEX Proxy |
| 投信 | 75 | 117 | -42 | 0 | 0 | +0 | -42 | 76,891 | 2,914 | +73,977 | -42 | TAIFEX Proxy |
| 自營商 | 3,128 | 3,234 | -106 | 441 | 368 | +73 | -179 | 2,314 | 5,772 | -3,458 | -104 | TAIFEX Proxy |
| 三大法人合計 | 36,771 | 38,401 | -1,630 | 11,535 | 11,207 | +328 | -1,958 | 89,945 | 94,994 | -5,049 | -1,633 | TAIFEX Proxy |

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
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 33.38% | TAIFEX Proxy |
| 夜盤漲跌點數 | +728 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +255 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-22 | TAIFEX Proxy |
| 到期月份／到期日 | 202609W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-22 17:41:36 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 226,484 | TAIFEX Proxy |
| Call 總未平倉量 OI | 52,742 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 227,087 | TAIFEX Proxy |
| Put 總未平倉量 OI | 47,470 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.00 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.11 | TAIFEX Proxy |
| Put／Call Ratio | 0.90 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-18→2026-09-21) | 25.75 | TAIFEX OpenAPI |
| 與前一交易日比較 (OI 比 2026-09-18→2026-09-21) | 19.88 | TAIFEX OpenAPI |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call 部位 (夜盤淨口數) | +25 | TAIFEX Proxy |
| 外資 Put 部位 (夜盤淨口數) | +372 | TAIFEX Proxy |
| 外資 Call／Put 淨部位 (日盤淨口數) | -3,098 | TAIFEX Proxy |
| 外資部位增減 (日盤淨 2026-09-21→2026-09-22) | -2,704 | TAIFEX Proxy snapshots (2026-09-21) |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call 部位 (夜盤淨口數) | -1,148 | TAIFEX Proxy |
| 自營商 Put 部位 (夜盤淨口數) | -1,464 | TAIFEX Proxy |
| 自營商 Call／Put 淨部位 (日盤淨口數) | -1,381 | TAIFEX Proxy |
| 自營商部位增減 (日盤淨 2026-09-21→2026-09-22) | -2,232 | TAIFEX Proxy snapshots (2026-09-21) |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 3,082 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,000 | 3,025 | TAIFEX Proxy |
| Call OI 第3大履約價 | 50,500 | 2,511 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 3,082 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 3,082 | 5.84% | TAIFEX Proxy |
| C2 | 50,000 | 3,025 | 5.74% | TAIFEX Proxy |
| C3 | 50,500 | 2,511 | 4.76% | TAIFEX Proxy |
| C4 | 48,500 | 2,482 | 4.71% | TAIFEX Proxy |
| C5 | 49,400 | 1,831 | 3.47% | TAIFEX Proxy |
| C6 | 48,000 | 1,779 | 3.37% | TAIFEX Proxy |
| C7 | 48,600 | 1,695 | 3.21% | TAIFEX Proxy |
| C8 | 48,400 | 1,663 | 3.15% | TAIFEX Proxy |
| C9 | 49,300 | 1,604 | 3.04% | TAIFEX Proxy |
| C10 | 48,300 | 1,494 | 2.83% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,500 | 2,057 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,000 | 1,855 | TAIFEX Proxy |
| Put OI 第3大履約價 | 46,400 | 1,628 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,500 | 2,057 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,500 | 2,057 | 4.33% | TAIFEX Proxy |
| P2 | 47,000 | 1,855 | 3.91% | TAIFEX Proxy |
| P3 | 46,400 | 1,628 | 3.43% | TAIFEX Proxy |
| P4 | 48,000 | 1,479 | 3.12% | TAIFEX Proxy |
| P5 | 47,400 | 1,447 | 3.05% | TAIFEX Proxy |
| P6 | 47,700 | 1,383 | 2.91% | TAIFEX Proxy |
| P7 | 47,800 | 1,343 | 2.83% | TAIFEX Proxy |
| P8 | 46,500 | 1,281 | 2.7% | TAIFEX Proxy |
| P9 | 46,000 | 1,272 | 2.68% | TAIFEX Proxy |
| P10 | 45,000 | 1,270 | 2.68% | TAIFEX Proxy |


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
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,500 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

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
| Max Pain 價位 | 47,700 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-22；資料時間：2026-09-22 17:41:36；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (6)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, options.chain_oi_change, futures.top10_change
- 註記：Gamma 資料日期 2026-09-21 (T0 2026-09-22 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-09-21 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`wantgoo 大盤融資維持率 (民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。
