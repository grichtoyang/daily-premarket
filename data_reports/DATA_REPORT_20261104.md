# DATA_REPORT_20261104

- 報告日期：`2026-11-05`
- T0 交易日期：`2026-11-04`
- 資料產出時間：`2026-11-05 10:46:49`
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
| 加權指數 | 42,948.91 | 點 | twse-proxy |
| 開盤 | 43,449.45 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 43,741.54 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 41,855.82 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 42,948.91 | 點 | twse-proxy |
| 漲跌點數 | -358.63 | 點 | twse-proxy |
| 漲跌幅 | -0.83 | % | twse-proxy |
| 成交金額 | 11,769.3 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 438 | twse-proxy |
| 下跌家數 | 544 | twse-proxy |
| 平盤家數 | 99 | twse-proxy |
| 漲停家數 | 20 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 397 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 416 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 68 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 29 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,499.0 | 億元 | twse-proxy /institutional |
| 投信 | +272.6 | 億元 | twse-proxy /institutional |
| 自營商 | -375.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,601.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `Blave 上市市場融資維持率估算（資料日期：2026-11-04；自建計算備援）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,878.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -84.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 281,221 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -15,111 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 164.67 | % | Blave 上市市場融資維持率估算（資料日期：2026-11-04；自建計算備援） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 31,451,773 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |
| 借券賣出餘額 | 19,732,584 | 張 | TWSE TWT93U（上市） + TPEX S47（上櫃） |
| 借券賣出增減 | 346,020 | 張 | TWSE TWT93U（上市） + TPEX S47（上櫃） |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 11,769.3 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,400.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,169.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,688.62 | 119.70 | +1.58 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,736.51 | 364.50 | +1.44 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,437.17 | 256.91 | +0.91 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 53,356.12 | 1,569.40 | +3.03 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,268.65 | -331.75 | -3.13 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.61 | -4.22 | -20.26 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,913.51 | -275.12 | -0.44 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,523.01 | -160.79 | -2.83 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,655.92 | 736.42 | +3.08 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,694.82 | 8.65 | +0.23 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,569.18 | 233.49 | +2.06 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,716.75 | -3.75 | -0.05 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,410.50 | 104.75 | +0.37 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 53,661.00 | 1,766.00 | +3.40 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,870.60 | 45.60 | +1.61 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.58 | -0.03 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.06 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.30 | -0.05 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.28 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.93 | 0.19 | +0.59 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.31 | -0.20 | -0.20 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.93 | -0.54 | -0.34 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.13 | 0.23 | +0.02 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 395.75 | -9.05 | -2.24 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.06 | -0.34 | -2.07 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 37.51 | -1.54 | -3.94 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 87.51 | -0.61 | -0.69 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,133.40 | 60.40 | +1.48 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,556.90 | 3,211.85 | +4.15 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：銅箔基板倒一片 台光電重挫跌停拖累族群
  - 來源：Yahoo 台股；發布時間：2026-11-05T01:53:33Z；台北時間：2026-11-05 09:53
  - 摘要：銅箔基板概念股一片倒！銅箔基板龍頭廠台光電今日重挫跌停，台燿、聯茂也難逃綠燈族群一片慘綠。運達投顧分析師陳石輝認為，在美國期中選舉後，因政策關係AI放緩的疑慮浮現，漲價題材股優先遇上賣壓，此處雖然已經回跌置起漲點，但別再貿然殺低，後續若反彈
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%8A%85%E7%AE%94%E5%9F%BA%E6%9D%BF%E5%80%92%E4%B8%80%E7%89%87%EF%BC%81%E5%8F%B0%E5%85%89%E9%9B%BB%E8%81%AF%E8%8C%82%E5%8F%B0%E7%87%BF%E4%B8%80%E5%BA%A6%E5%85%A8%E7%B6%A0%E7%87%88-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E7%AD%89%E5%8F%8D%E5%BD%88%E9%81%A9%E5%BA%A6%E8%AA%BF%E7%AF%80-015333595.html
- 事件3：台股重挫逾600點 電子股爆逃難潮
  - 來源：Yahoo 台股；發布時間：2026-11-05T01:40:00Z；台北時間：2026-11-05 09:40
  - 摘要：[FTNN新聞網]記者何亞軒／綜合報導今（15）日台股加權指數開盤42,666.13點，隨後早盤跌幅擴大，一度下跌超過500點，暫報42,311.92點，跌636.99點，跌幅1.48%...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%B7%AA%E4%BA%8C%E5%93%A5%E6%8F%90%E6%AC%BE%E6%A9%9F-%E9%96%8B%E7%9B%A4%E9%87%8D%E6%8C%AB600%E9%BB%9E%E9%9B%BB%E5%AD%90%E8%82%A1%E7%88%86%E8%B7%8C%E5%81%9C%E9%80%83%E9%9B%A3%E6%BD%AE-%E8%81%AF%E8%8C%82-%E5%BF%97%E8%81%96-%E9%80%99%E6%AA%94%E7%9B%AE%E6%A8%99%E5%83%B9%E8%90%AC%E5%85%83-014000226.html
- 事件4：受惠國際油價暴跌 航空四雄全數翻紅齊漲
  - 來源：Yahoo 台股；發布時間：2026-11-05T01:23:10Z；台北時間：2026-11-05 09:23
  - 摘要：國際油價暴跌8%受惠股！航空四雄今（5）早全數翻紅大漲，其中華航（2610）開盤10分鐘就爆2.5萬張，成交量擠上前七強，股價最高飆8%，長榮航（2618）一度飆6%站上46.5元，唯一廉航台灣虎航（6757）也漲4.8%，星宇（2646）
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B2%B9%E5%83%B9%E6%9A%B4%E8%B7%8C%E5%8F%97%E6%83%A0%E8%82%A1%EF%BC%81%E8%88%AA%E7%A9%BA%E5%9B%9B%E9%9B%84%E5%85%A8%E8%B5%B7%E9%A3%9B-%E9%95%B7%E6%A6%AE%E8%88%AA%E8%8F%AF%E8%88%AA%E9%A3%86%E9%80%BE6-012310680.html
- 事件5：德州選後「變天」AI基建藏變數？設廠台鏈嚴陣以待
  - 來源：Yahoo 台股；發布時間：2026-11-04T22:54:48Z；台北時間：2026-11-05 06:54
  - 摘要：主張嚴管AI資料中心的民主黨，在美國期中選舉大翻盤，更拿下台灣代工大廠美國布局重鎮德州，時值AI伺服器出貨正熱，台系AI伺服器代工廠嚴陣以待，隨時準備機動調度產能，確保出貨無虞。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E6%9C%9F%E4%B8%AD%E9%81%B8%E8%88%89%E8%AE%8A%E5%A4%A9-%E6%B0%91%E4%B8%BB%E9%BB%A8%E6%8B%BF%E4%B8%8B%E5%BE%B7%E5%B7%9E-%E4%BC%BA%E6%9C%8D%E5%99%A8%E4%BB%A3%E5%B7%A5%E5%8F%B0%E9%8F%88%E5%9A%B4%E9%99%A3%E4%BB%A5%E5%BE%85-225448406.html
- 事件6：王品子公司系統驚傳異常存取 影響範圍待調查
  - 來源：Yahoo 台股；發布時間：2026-11-04T14:33:35Z；台北時間：2026-11-04 22:33
  - 摘要：王品今（4）日指出，子公司萬鮮公司接獲委外購物網站服務廠商通知，發現委外服務系統近期有異常資料存取狀況，廠商發現問題後，已先行阻擋異常存取行為。王品透露，萬鮮公司接獲通知後，也立即啟動資安事件應變及調查機制，並要求委外服務廠商儘速確認受影響
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8E%8B%E5%93%81%E7%AA%81%E7%99%BC%E9%87%8D%E8%A8%8A-%E5%AD%90%E5%85%AC%E5%8F%B8-%E7%B3%BB%E7%B5%B1%E9%A9%9A%E5%82%B3%E7%95%B0%E5%B8%B8%E5%AD%98%E5%8F%96-%E5%BD%B1%E9%9F%BF%E7%AF%84%E5%9C%8D%E5%BE%85%E8%AA%BF%E6%9F%A5-143335630.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：White House panel delays hearing on Fed's Lisa Cook to Dec. 14
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 01:11:26 GMT；台北時間：2026-11-05 09:11
  - 摘要：President Donald Trump first tried to fire Lisa Cook in August 2025, but the Supreme Court in June blocked him from doing so, for now.
  - 原文連結：https://www.cnbc.com/2026/11/04/trump-federal-reserve-lisa-cook-hearing.html
- 事件9：What Wall Street billionaires are saying about Democrats' midterm sweep
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 23:17:56 GMT；台北時間：2026-11-05 07:17
  - 摘要：Billionaire political spending met criticism from ... billionaires in the wake of Tuesday's blue wave election.
  - 原文連結：https://www.cnbc.com/2026/11/04/billionaires-musk-branson-democrats-midterms-ai-wall-street.html
- 事件10：Jim Cramer warns investors may be reading too much into Wall Street's post-election rally
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 23:18:56 GMT；台北時間：2026-11-05 07:18
  - 摘要：Cramer warned that Wall Street may be getting ahead of itself following the midterm elections.
  - 原文連結：https://www.cnbc.com/2026/11/04/cramer-midterms-ai-stocks.html
- 事件11：Crude oil prices fall below $90 a barrel as Vance blames GOP election defeat on Iran war
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 20:14:52 GMT；台北時間：2026-11-05 04:14
  - 摘要：Crude oil prices tumbled Wednesday after Vice President JD Vance blamed the Republicans' steep midterm election losses on the Iran war.
  - 原文連結：https://www.cnbc.com/2026/11/04/oil-price-iran-war-us-election-strait-hormuz.html
- 事件12：This year's worst-performing S&P 500 stock is finally seeing some major relief
  - 來源：MarketWatch；發布時間：Thu, 05 Nov 2026 01:05:00 GMT；台北時間：2026-11-05 09:05
  - 摘要：AppLovin&#x2019;s stock is popping after &#x201c;clearly positive&#x201d; earnings results.
  - 原文連結：https://www.marketwatch.com/story/this-years-worst-performing-s-p-500-stock-is-finally-seeing-some-major-relief-fff3fa85?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-04

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,450 | TAIFEX Proxy |
| 最高價 | 43,774 | TAIFEX Proxy |
| 最低價 | 42,050 | TAIFEX Proxy |
| 收盤價 | 43,204 | TAIFEX Proxy |
| 漲跌點數 | -149 | TAIFEX Proxy |
| 漲跌幅 | -0.34 | TAIFEX Proxy |
| 成交量 | 113,674 | TAIFEX Proxy |
| 日盤高點及低點 | 43,774 / 42,050 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,430 | TAIFEX Proxy |
| 最高價 | 44,274 | TAIFEX Proxy |
| 最低價 | 43,141 | TAIFEX Proxy |
| 收盤價 | 43,404 | TAIFEX Proxy |
| 漲跌點數 | +201 | TAIFEX Proxy |
| 漲跌幅 | +0.47 | TAIFEX Proxy |
| 成交量 | 66,939 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,274 / 43,141 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,103 | TAIFEX Proxy |
| 外資空方 OI | 104,750 | TAIFEX Proxy |
| 外資多空淨 OI | -93,647 | TAIFEX Proxy |
| 投信多方 OI | 92,491 | TAIFEX Proxy |
| 投信空方 OI | 2,991 | TAIFEX Proxy |
| 投信多空淨 OI | +89,500 | TAIFEX Proxy |
| 自營商多方 OI | 6,858 | TAIFEX Proxy |
| 自營商空方 OI | 3,897 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,961 | TAIFEX Proxy |
| 三大法人合計多方 OI | 110,452 | TAIFEX Proxy |
| 三大法人合計空方 OI | 111,638 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -1,186 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,835 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +2,502 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,015 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-02→2026-11-04) | -977 | TAIFEX Proxy snapshots (2026-11-03) |
- 資料日期：2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 93,663 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 95,523 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,860 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 38,711 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 39,180 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -469 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,391 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,502 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +2,502 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -991 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -310 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -681 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -349 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -779 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -26.1 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -69.7 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,204 | TAIFEX Proxy |
| 加權指數價格 | 42,948.91 | twse-proxy |
| 台指期與加權指數價差 | +255.09 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.59 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +255.09 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +200 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,204 | 43,404 | -200 | TAIFEX Proxy |
| 成交量 | 113,674 | 66,939 | +46,735 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-348（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 93,663 | 95,523 | -1,860 | 38,711 | 39,180 | -469 | -1,391 | 11,103 | 104,750 | -93,647 | -1,835 | TAIFEX Proxy |
| 投信 | 2,514 | 12 | +2,502 | 0 | 0 | +0 | +2,502 | 92,491 | 2,991 | +89,500 | +2,502 | TAIFEX Proxy |
| 自營商 | 12,388 | 13,379 | -991 | 1,328 | 1,638 | -310 | -681 | 6,858 | 3,897 | +2,961 | -1,015 | TAIFEX Proxy |
| 三大法人合計 | 108,565 | 108,914 | -349 | 40,039 | 40,818 | -779 | +430 | 110,452 | 111,638 | -1,186 | -348 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-02→2026-11-04) | -977 | TAIFEX Proxy snapshots (2026-11-03) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 37.06% | TAIFEX Proxy |
| 夜盤漲跌點數 | +201 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -469 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-04 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-05 10:46:49 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 438,164 | TAIFEX Proxy |
| Call 總未平倉量 OI | 123,799 | TAIFEX Proxy |
| Call OI 增減 (2026-11-03→2026-11-04) | +27,305 | TAIFEX Proxy snapshots (2026-11-03) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 387,135 | TAIFEX Proxy |
| Put 總未平倉量 OI | 65,804 | TAIFEX Proxy |
| Put OI 增減 (2026-11-03→2026-11-04) | +25,669 | TAIFEX Proxy snapshots (2026-11-03) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.13 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.88 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.53 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-03→2026-11-04) | 5.01 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-03→2026-11-04) | 1.60 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 146,103 | TAIFEX Proxy |
| 外資 Call日賣 | 147,099 | TAIFEX Proxy |
| 外資 Call日淨 | -996 | TAIFEX Proxy |
| 外資 Put日買 | 144,973 | TAIFEX Proxy |
| 外資 Put日賣 | 149,598 | TAIFEX Proxy |
| 外資 Put日淨 | -4,625 | TAIFEX Proxy |
| 外資 Call夜買 | 39,947 | TAIFEX Proxy |
| 外資 Call夜賣 | 40,962 | TAIFEX Proxy |
| 外資 Call夜淨 | -1,015 | TAIFEX Proxy |
| 外資 Put夜買 | 34,664 | TAIFEX Proxy |
| 外資 Put夜賣 | 34,763 | TAIFEX Proxy |
| 外資 Put夜淨 | -99 | TAIFEX Proxy |
| 外資 日盤淨總量 | +3,629 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +19 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,526 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 113,663 | TAIFEX Proxy |
| 自營商 Call日賣 | 117,752 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,089 | TAIFEX Proxy |
| 自營商 Put日買 | 96,474 | TAIFEX Proxy |
| 自營商 Put日賣 | 101,454 | TAIFEX Proxy |
| 自營商 Put日淨 | -4,980 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,062 | TAIFEX Proxy |
| 自營商 Call夜賣 | 26,325 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,263 | TAIFEX Proxy |
| 自營商 Put夜買 | 19,833 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,869 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,036 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +891 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -2,826 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -3,944 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 5,405 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 5,041 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,000 | 4,681 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 5,405 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 5,405 | 4.37% | TAIFEX Proxy |
| C2 | 43,000 | 5,041 | 4.07% | TAIFEX Proxy |
| C3 | 48,000 | 4,681 | 3.78% | TAIFEX Proxy |
| C4 | 44,000 | 3,694 | 2.98% | TAIFEX Proxy |
| C5 | 44,500 | 3,580 | 2.89% | TAIFEX Proxy |
| C6 | 45,000 | 3,430 | 2.77% | TAIFEX Proxy |
| C7 | 49,400 | 3,028 | 2.45% | TAIFEX Proxy |
| C8 | 44,200 | 2,889 | 2.33% | TAIFEX Proxy |
| C9 | 43,500 | 2,867 | 2.32% | TAIFEX Proxy |
| C10 | 46,200 | 2,809 | 2.27% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 42,000 | 3,334 | TAIFEX Proxy |
| Put OI 第2大履約價 | 41,000 | 3,186 | TAIFEX Proxy |
| Put OI 第3大履約價 | 43,000 | 2,909 | TAIFEX Proxy |
| Put OI 最大履約價 | 42,000 | 3,334 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 42,000 | 3,334 | 5.07% | TAIFEX Proxy |
| P2 | 41,000 | 3,186 | 4.84% | TAIFEX Proxy |
| P3 | 43,000 | 2,909 | 4.42% | TAIFEX Proxy |
| P4 | 42,800 | 2,445 | 3.72% | TAIFEX Proxy |
| P5 | 42,500 | 2,223 | 3.38% | TAIFEX Proxy |
| P6 | 41,500 | 2,166 | 3.29% | TAIFEX Proxy |
| P7 | 42,300 | 2,066 | 3.14% | TAIFEX Proxy |
| P8 | 42,900 | 1,982 | 3.01% | TAIFEX Proxy |
| P9 | 40,600 | 1,859 | 2.83% | TAIFEX Proxy |
| P10 | 40,400 | 1,807 | 2.75% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 43,000 (+3,982) | TAIFEX Proxy snapshots (2026-11-03) |
| Call OI 減少最多的履約價 | 49,400 (-1,350) | TAIFEX Proxy snapshots (2026-11-03) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 41,000 (+2,468) | TAIFEX Proxy snapshots (2026-11-03) |
| Put OI 減少最多的履約價 | 44,000 (-559) | TAIFEX Proxy snapshots (2026-11-03) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-03) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 42,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | -1,000 | TAIFEX Proxy snapshots (2026-11-03) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 44,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-04 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 39,901.34 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | 2026-11-04 | TAIFEX Proxy (options-gamma-levels) |

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 2,521,729,091.75 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 5,765,974,976.35 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 履約價資料筆數 | 184 | 資料日期：2026-11-04 |
| 正 Net GEX 最大履約價 | 44,000 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 42,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：44,000（274,214,369.32 NT$）、44,500（250,353,053.17 NT$）、44,300（182,489,838.13 NT$）、44,200（178,568,285.13 NT$）、42,800（163,927,477.11 NT$）
- 負 Net GEX Top 5：42,000（-156,500,195.46 NT$）、42,500（-95,050,850.72 NT$）、40,000（-39,690,655.82 NT$）、41,400（-37,031,972.05 NT$）、41,900（-27,298,239.05 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-04","underlying":42948.91,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":2521729091.753471,"gross_gex_1pct":5765974976.351615,"levels":[{"strike":38900.0,"call_gex_1pct":0.0,"put_gex_1pct":-15869062.30185238,"net_gex_1pct":-15869062.30185238,"gross_gex_1pct":15869062.30185238,"call_oi":0,"put_oi":748},{"strike":39000.0,"call_gex_1pct":0.0,"put_gex_1pct":-6942861.138183099,"net_gex_1pct":-6942861.138183099,"gross_gex_1pct":6942861.138183099,"call_oi":0,"put_oi":297},{"strike":39100.0,"call_gex_1pct":0.0,"put_gex_1pct":-5275978.902175584,"net_gex_1pct":-5275978.902175584,"gross_gex_1pct":5275978.902175584,"call_oi":0,"put_oi":214},{"strike":39200.0,"call_gex_1pct":0.0,"put_gex_1pct":-2465827.4458268536,"net_gex_1pct":-2465827.4458268536,"gross_gex_1pct":2465827.4458268536,"call_oi":0,"put_oi":96},{"strike":39300.0,"call_gex_1pct":0.0,"put_gex_1pct":-944334.6474924021,"net_gex_1pct":-944334.6474924021,"gross_gex_1pct":944334.6474924021,"call_oi":0,"put_oi":34},{"strike":39400.0,"call_gex_1pct":48322.02539035023,"put_gex_1pct":-1185465.349114641,"net_gex_1pct":-1137143.3237242908,"gross_gex_1pct":1233787.3745049913,"call_oi":1,"put_oi":40},{"strike":39500.0,"call_gex_1pct":0.0,"put_gex_1pct":-19311534.41513286,"net_gex_1pct":-19311534.41513286,"gross_gex_1pct":19311534.41513286,"call_oi":0,"put_oi":611},{"strike":39600.0,"call_gex_1pct":0.0,"put_gex_1pct":-1520215.2253688076,"net_gex_1pct":-1520215.2253688076,"gross_gex_1pct":1520215.2253688076,"call_oi":0,"put_oi":46},{"strike":39700.0,"call_gex_1pct":55869.079272840594,"put_gex_1pct":-1195578.4157595653,"net_gex_1pct":-1139709.3364867247,"gross_gex_1pct":1251447.495032406,"call_oi":1,"put_oi":33},{"strike":39800.0,"call_gex_1pct":0.0,"put_gex_1pct":-1632233.8516739549,"net_gex_1pct":-1632233.8516739549,"gross_gex_1pct":1632233.8516739549,"call_oi":0,"put_oi":43},{"strike":39900.0,"call_gex_1pct":0.0,"put_gex_1pct":-897721.125426115,"net_gex_1pct":-897721.125426115,"gross_gex_1pct":897721.125426115,"call_oi":0,"put_oi":22},{"strike":40000.0,"call_gex_1pct":0.0,"put_gex_1pct":-39690655.821447104,"net_gex_1pct":-39690655.821447104,"gross_gex_1pct":39690655.821447104,"call_oi":0,"put_oi":887},{"strike":40100.0,"call_gex_1pct":66169.73689898768,"put_gex_1pct":-6250497.156736773,"net_gex_1pct":-6184327.419837786,"gross_gex_1pct":6316666.893635761,"call_oi":1,"put_oi":132},{"strike":40200.0,"call_gex_1pct":0.0,"put_gex_1pct":-2401044.802684866,"net_gex_1pct":-2401044.802684866,"gross_gex_1pct":2401044.802684866,"call_oi":0,"put_oi":47},{"strike":40300.0,"call_gex_1pct":664935.8796018624,"put_gex_1pct":-5056437.154045535,"net_gex_1pct":-4391501.274443673,"gross_gex_1pct":5721373.0336473975,"call_oi":9,"put_oi":90},{"strike":40400.0,"call_gex_1pct":619650.0557362697,"put_gex_1pct":-17454516.14341237,"net_gex_1pct":-16834866.0876761,"gross_gex_1pct":18074166.19914864,"call_oi":8,"put_oi":289},{"strike":40500.0,"call_gex_1pct":81324175.24779505,"put_gex_1pct":-23510999.852283563,"net_gex_1pct":57813175.39551148,"gross_gex_1pct":104835175.10007861,"call_oi":1000,"put_oi":354},{"strike":40600.0,"call_gex_1pct":86956117.93665898,"put_gex_1pct":-38047268.20390207,"net_gex_1pct":48908849.732756905,"gross_gex_1pct":125003386.14056104,"call_oi":1004,"put_oi":534},{"strike":40700.0,"call_gex_1pct":91159684.36933559,"put_gex_1pct":-22127388.060863856,"net_gex_1pct":69032296.30847174,"gross_gex_1pct":113287072.43019944,"call_oi":1000,"put_oi":286},{"strike":40800.0,"call_gex_1pct":96217175.4735078,"put_gex_1pct":-36137677.445358574,"net_gex_1pct":60079498.02814923,"gross_gex_1pct":132354852.91886638,"call_oi":1001,"put_oi":431},{"strike":40900.0,"call_gex_1pct":102313829.99964732,"put_gex_1pct":-63468669.21091805,"net_gex_1pct":38845160.78872927,"gross_gex_1pct":165782499.21056536,"call_oi":1000,"put_oi":684},{"strike":41000.0,"call_gex_1pct":108218758.3990768,"put_gex_1pct":-84349307.60778354,"net_gex_1pct":23869450.791293263,"gross_gex_1pct":192568066.00686035,"call_oi":1000,"put_oi":841},{"strike":41100.0,"call_gex_1pct":7829639.065916878,"put_gex_1pct":-14911528.866280302,"net_gex_1pct":-7081889.800363424,"gross_gex_1pct":22741167.93219718,"call_oi":68,"put_oi":139},{"strike":41200.0,"call_gex_1pct":122377498.84316163,"put_gex_1pct":-64431634.94583898,"net_gex_1pct":57945863.89732265,"gross_gex_1pct":186809133.7890006,"call_oi":1000,"put_oi":552},{"strike":41300.0,"call_gex_1pct":129372005.94801159,"put_gex_1pct":-12230544.169439347,"net_gex_1pct":117141461.77857225,"gross_gex_1pct":141602550.11745095,"call_oi":1000,"put_oi":97},{"strike":41400.0,"call_gex_1pct":825185.766262512,"put_gex_1pct":-37857157.81261787,"net_gex_1pct":-37031972.04635536,"gross_gex_1pct":38682343.57888038,"call_oi":6,"put_oi":275},{"strike":41500.0,"call_gex_1pct":4105300.9602227905,"put_gex_1pct":-29311365.512066603,"net_gex_1pct":-25206064.55184381,"gross_gex_1pct":33416666.472289395,"call_oi":28,"put_oi":197},{"strike":41600.0,"call_gex_1pct":125574023.0642533,"put_gex_1pct":-51906018.73678708,"net_gex_1pct":73668004.32746622,"gross_gex_1pct":177480041.80104038,"call_oi":806,"put_oi":324},{"strike":41700.0,"call_gex_1pct":20676035.862153016,"put_gex_1pct":-16648416.764359891,"net_gex_1pct":4027619.0977931246,"gross_gex_1pct":37324452.62651291,"call_oi":128,"put_oi":97},{"strike":41800.0,"call_gex_1pct":141878661.07019037,"put_gex_1pct":-44673577.263537265,"net_gex_1pct":97205083.80665311,"gross_gex_1pct":186552238.33372763,"call_oi":820,"put_oi":243},{"strike":41900.0,"call_gex_1pct":920032.8723065405,"put_gex_1pct":-28218271.920451283,"net_gex_1pct":-27298239.048144743,"gross_gex_1pct":29138304.792757824,"call_oi":5,"put_oi":145},{"strike":42000.0,"call_gex_1pct":7552884.456367216,"put_gex_1pct":-164053079.92061862,"net_gex_1pct":-156500195.4642514,"gross_gex_1pct":171605964.37698585,"call_oi":39,"put_oi":791},{"strike":42050.0,"call_gex_1pct":980759.1254951044,"put_gex_1pct":-5138826.767155784,"net_gex_1pct":-4158067.64166068,"gross_gex_1pct":6119585.892650888,"call_oi":5,"put_oi":24},{"strike":42100.0,"call_gex_1pct":1005607.6426740612,"put_gex_1pct":-19129307.96832614,"net_gex_1pct":-18123700.325652078,"gross_gex_1pct":20134915.611000203,"call_oi":5,"put_oi":87},{"strike":42150.0,"call_gex_1pct":618714.6359106695,"put_gex_1pct":-2900619.993303482,"net_gex_1pct":-2281905.3573928126,"gross_gex_1pct":3519334.6292141513,"call_oi":3,"put_oi":13},{"strike":42200.0,"call_gex_1pct":55840518.07108677,"put_gex_1pct":-15703450.48845324,"net_gex_1pct":40137067.58263353,"gross_gex_1pct":71543968.55954,"call_oi":264,"put_oi":68},{"strike":42250.0,"call_gex_1pct":3421510.252861498,"put_gex_1pct":-8331641.75154487,"net_gex_1pct":-4910131.4986833725,"gross_gex_1pct":11753152.004406368,"call_oi":16,"put_oi":35},{"strike":42300.0,"call_gex_1pct":10088573.913663061,"put_gex_1pct":-15045785.363450928,"net_gex_1pct":-4957211.449787866,"gross_gex_1pct":25134359.27711399,"call_oi":46,"put_oi":62},{"strike":42350.0,"call_gex_1pct":1786273.2160201245,"put_gex_1pct":-4436521.1839129105,"net_gex_1pct":-2650247.967892786,"gross_gex_1pct":6222794.399933035,"call_oi":8,"put_oi":18},{"strike":42400.0,"call_gex_1pct":2273136.241230349,"put_gex_1pct":-13721975.307960954,"net_gex_1pct":-11448839.066730604,"gross_gex_1pct":15995111.549191304,"call_oi":10,"put_oi":54},{"strike":42450.0,"call_gex_1pct":1388505.5214669395,"put_gex_1pct":-4875837.3893214045,"net_gex_1pct":-3487331.867854465,"gross_gex_1pct":6264342.910788344,"call_oi":6,"put_oi":19},{"strike":42500.0,"call_gex_1pct":20801076.845010906,"put_gex_1pct":-115851927.56330305,"net_gex_1pct":-95050850.71829215,"gross_gex_1pct":136653004.40831396,"call_oi":89,"put_oi":448},{"strike":42550.0,"call_gex_1pct":1427635.9235961488,"put_gex_1pct":-6100419.366452806,"net_gex_1pct":-4672783.442856656,"gross_gex_1pct":7528055.290048955,"call_oi":6,"put_oi":23},{"strike":42600.0,"call_gex_1pct":8273068.321967196,"put_gex_1pct":-16478044.897751987,"net_gex_1pct":-8204976.575784791,"gross_gex_1pct":24751113.219719183,"call_oi":35,"put_oi":61},{"strike":42650.0,"call_gex_1pct":10030505.134013392,"put_gex_1pct":-3114707.382852952,"net_gex_1pct":6915797.75116044,"gross_gex_1pct":13145212.516866345,"call_oi":41,"put_oi":11},{"strike":42700.0,"call_gex_1pct":13718286.448878221,"put_gex_1pct":-12829141.539644545,"net_gex_1pct":889144.9092336763,"gross_gex_1pct":26547427.988522768,"call_oi":56,"put_oi":47},{"strike":42750.0,"call_gex_1pct":2993579.006217148,"put_gex_1pct":-6430594.940111973,"net_gex_1pct":-3437015.933894825,"gross_gex_1pct":9424173.94632912,"call_oi":12,"put_oi":23},{"strike":42800.0,"call_gex_1pct":213122697.60327646,"put_gex_1pct":-49195220.492423214,"net_gex_1pct":163927477.11085325,"gross_gex_1pct":262317918.09569967,"call_oi":846,"put_oi":168},{"strike":42850.0,"call_gex_1pct":5851385.099035595,"put_gex_1pct":-12808273.922974437,"net_gex_1pct":-6956888.823938843,"gross_gex_1pct":18659659.022010032,"call_oi":23,"put_oi":45},{"strike":42900.0,"call_gex_1pct":20028377.45840025,"put_gex_1pct":-20437822.265895743,"net_gex_1pct":-409444.80749549344,"gross_gex_1pct":40466199.72429599,"call_oi":80,"put_oi":72},{"strike":42950.0,"call_gex_1pct":10735040.365711277,"put_gex_1pct":-7273821.939282067,"net_gex_1pct":3461218.42642921,"gross_gex_1pct":18008862.304993346,"call_oi":41,"put_oi":25},{"strike":43000.0,"call_gex_1pct":124075822.22121899,"put_gex_1pct":-58557413.11441444,"net_gex_1pct":65518409.10680455,"gross_gex_1pct":182633235.33563343,"call_oi":486,"put_oi":209},{"strike":43050.0,"call_gex_1pct":7477253.537191704,"put_gex_1pct":-2333015.805371625,"net_gex_1pct":5144237.731820079,"gross_gex_1pct":9810269.34256333,"call_oi":29,"put_oi":8},{"strike":43100.0,"call_gex_1pct":63716220.25711076,"put_gex_1pct":-23648577.86415186,"net_gex_1pct":40067642.392958894,"gross_gex_1pct":87364798.12126262,"call_oi":249,"put_oi":81},{"strike":43150.0,"call_gex_1pct":12552546.620399686,"put_gex_1pct":-4341101.367982852,"net_gex_1pct":8211445.252416833,"gross_gex_1pct":16893647.988382537,"call_oi":49,"put_oi":15},{"strike":43200.0,"call_gex_1pct":39239836.85212025,"put_gex_1pct":-19989103.314583305,"net_gex_1pct":19250733.537536945,"gross_gex_1pct":59228940.16670355,"call_oi":157,"put_oi":69},{"strike":43250.0,"call_gex_1pct":10710573.829770496,"put_gex_1pct":-2584211.326267725,"net_gex_1pct":8126362.503502771,"gross_gex_1pct":13294785.156038221,"call_oi":41,"put_oi":9},{"strike":43300.0,"call_gex_1pct":54857240.70509265,"put_gex_1pct":-40512933.567264564,"net_gex_1pct":14344307.13782809,"gross_gex_1pct":95370174.27235723,"call_oi":215,"put_oi":141},{"strike":43350.0,"call_gex_1pct":10108783.501987886,"put_gex_1pct":-1708094.9532633808,"net_gex_1pct":8400688.548724504,"gross_gex_1pct":11816878.455251267,"call_oi":40,"put_oi":6},{"strike":43400.0,"call_gex_1pct":40500800.74953495,"put_gex_1pct":-43426876.86696471,"net_gex_1pct":-2926076.117429763,"gross_gex_1pct":83927677.61649966,"call_oi":161,"put_oi":154},{"strike":43450.0,"call_gex_1pct":10604883.463517264,"put_gex_1pct":-3596632.438969189,"net_gex_1pct":7008251.024548074,"gross_gex_1pct":14201515.902486453,"call_oi":43,"put_oi":13},{"strike":43500.0,"call_gex_1pct":128896065.87709303,"put_gex_1pct":-32315568.85437348,"net_gex_1pct":96580497.02271955,"gross_gex_1pct":161211634.7314665,"call_oi":527,"put_oi":118},{"strike":43550.0,"call_gex_1pct":14572067.143673692,"put_gex_1pct":-3727088.904728814,"net_gex_1pct":10844978.238944877,"gross_gex_1pct":18299156.048402507,"call_oi":60,"put_oi":14},{"strike":43600.0,"call_gex_1pct":50627295.68765384,"put_gex_1pct":-10526270.557002092,"net_gex_1pct":40101025.13065175,"gross_gex_1pct":61153566.24465593,"call_oi":215,"put_oi":41},{"strike":43650.0,"call_gex_1pct":4959413.04743786,"put_gex_1pct":-2517978.114789584,"net_gex_1pct":2441434.9326482755,"gross_gex_1pct":7477391.162227444,"call_oi":21,"put_oi":10},{"strike":43700.0,"call_gex_1pct":103883905.24990833,"put_gex_1pct":-12217278.730668161,"net_gex_1pct":91666626.51924017,"gross_gex_1pct":116101183.98057649,"call_oi":451,"put_oi":48},{"strike":43750.0,"call_gex_1pct":15770132.357299054,"put_gex_1pct":-3259213.156679554,"net_gex_1pct":12510919.2006195,"gross_gex_1pct":19029345.513978608,"call_oi":69,"put_oi":13},{"strike":43800.0,"call_gex_1pct":101632040.02293229,"put_gex_1pct":-7779157.346082684,"net_gex_1pct":93852882.6768496,"gross_gex_1pct":109411197.36901498,"call_oi":458,"put_oi":32},{"strike":43850.0,"call_gex_1pct":14571842.91009892,"put_gex_1pct":-1669201.839220357,"net_gex_1pct":12902641.070878563,"gross_gex_1pct":16241044.749319276,"call_oi":67,"put_oi":7},{"strike":43900.0,"call_gex_1pct":71189780.25951919,"put_gex_1pct":-11763055.585828813,"net_gex_1pct":59426724.67369038,"gross_gex_1pct":82952835.845348,"call_oi":335,"put_oi":51},{"strike":43950.0,"call_gex_1pct":8746098.3349758,"put_gex_1pct":-1114314.4455422978,"net_gex_1pct":7631783.889433501,"gross_gex_1pct":9860412.780518098,"call_oi":42,"put_oi":5},{"strike":44000.0,"call_gex_1pct":309248627.6853359,"put_gex_1pct":-35034258.36798272,"net_gex_1pct":274214369.3173531,"gross_gex_1pct":344282886.0533186,"call_oi":1530,"put_oi":162},{"strike":44050.0,"call_gex_1pct":9127968.937049152,"put_gex_1pct":-1246350.087129149,"net_gex_1pct":7881618.849920004,"gross_gex_1pct":10374319.024178302,"call_oi":46,"put_oi":6},{"strike":44100.0,"call_gex_1pct":165619604.12095246,"put_gex_1pct":-73125721.73927894,"net_gex_1pct":92493882.38167351,"gross_gex_1pct":238745325.8602314,"call_oi":858,"put_oi":372},{"strike":44150.0,"call_gex_1pct":4492582.14514188,"put_gex_1pct":-2067629.3289911451,"net_gex_1pct":2424952.816150735,"gross_gex_1pct":6560211.474133025,"call_oi":24,"put_oi":11},{"strike":44200.0,"call_gex_1pct":181448380.90387136,"put_gex_1pct":-2880095.7728558024,"net_gex_1pct":178568285.13101557,"gross_gex_1pct":184328476.67672715,"call_oi":999,"put_oi":16},{"strike":44250.0,"call_gex_1pct":8966634.947852775,"put_gex_1pct":-3050519.82796021,"net_gex_1pct":5916115.1198925655,"gross_gex_1pct":12017154.775812985,"call_oi":51,"put_oi":18},{"strike":44300.0,"call_gex_1pct":188666429.3978687,"put_gex_1pct":-6176591.268808081,"net_gex_1pct":182489838.12906063,"gross_gex_1pct":194843020.66667676,"call_oi":1108,"put_oi":38},{"strike":44350.0,"call_gex_1pct":6414135.919633536,"put_gex_1pct":-756710.8437329786,"net_gex_1pct":5657425.075900557,"gross_gex_1pct":7170846.763366514,"call_oi":39,"put_oi":5},{"strike":44400.0,"call_gex_1pct":36685520.3964075,"put_gex_1pct":-1800366.890454038,"net_gex_1pct":34885153.50595346,"gross_gex_1pct":38485887.28686154,"call_oi":231,"put_oi":13},{"strike":44450.0,"call_gex_1pct":7499024.548077697,"put_gex_1pct":-664847.8003175497,"net_gex_1pct":6834176.747760147,"gross_gex_1pct":8163872.348395247,"call_oi":49,"put_oi":5},{"strike":44500.0,"call_gex_1pct":255903199.96815172,"put_gex_1pct":-5550146.800083978,"net_gex_1pct":250353053.16806775,"gross_gex_1pct":261453346.76823568,"call_oi":1732,"put_oi":47},{"strike":44550.0,"call_gex_1pct":7063116.158461022,"put_gex_1pct":-494082.4267605232,"net_gex_1pct":6569033.731700499,"gross_gex_1pct":7557198.585221546,"call_oi":50,"put_oi":5},{"strike":44600.0,"call_gex_1pct":20342174.673963815,"put_gex_1pct":-1328369.2913711523,"net_gex_1pct":19013805.382592663,"gross_gex_1pct":21670543.965334967,"call_oi":149,"put_oi":14},{"strike":44650.0,"call_gex_1pct":6539366.255584149,"put_gex_1pct":0.0,"net_gex_1pct":6539366.255584149,"gross_gex_1pct":6539366.255584149,"call_oi":50,"put_oi":0},{"strike":44700.0,"call_gex_1pct":59466734.18121478,"put_gex_1pct":-579352.9856328709,"net_gex_1pct":58887381.195581906,"gross_gex_1pct":60046087.16684765,"call_oi":474,"put_oi":9},{"strike":44750.0,"call_gex_1pct":16492083.989177829,"put_gex_1pct":0.0,"net_gex_1pct":16492083.989177829,"gross_gex_1pct":16492083.989177829,"call_oi":138,"put_oi":0},{"strike":44800.0,"call_gex_1pct":25336647.24636294,"put_gex_1pct":0.0,"net_gex_1pct":25336647.24636294,"gross_gex_1pct":25336647.24636294,"call_oi":220,"put_oi":0},{"strike":44850.0,"call_gex_1pct":7223811.149713806,"put_gex_1pct":0.0,"net_gex_1pct":7223811.149713806,"gross_gex_1pct":7223811.149713806,"call_oi":66,"put_oi":0},{"strike":44900.0,"call_gex_1pct":7479606.065873792,"put_gex_1pct":0.0,"net_gex_1pct":7479606.065873792,"gross_gex_1pct":7479606.065873792,"call_oi":71,"put_oi":0},{"strike":44950.0,"call_gex_1pct":12801613.944355799,"put_gex_1pct":0.0,"net_gex_1pct":12801613.944355799,"gross_gex_1pct":12801613.944355799,"call_oi":129,"put_oi":0},{"strike":45000.0,"call_gex_1pct":105941707.55347288,"put_gex_1pct":0.0,"net_gex_1pct":105941707.55347288,"gross_gex_1pct":105941707.55347288,"call_oi":1128,"put_oi":0},{"strike":45050.0,"call_gex_1pct":6454482.322727583,"put_gex_1pct":0.0,"net_gex_1pct":6454482.322727583,"gross_gex_1pct":6454482.322727583,"call_oi":71,"put_oi":0},{"strike":45100.0,"call_gex_1pct":25383858.996927075,"put_gex_1pct":0.0,"net_gex_1pct":25383858.996927075,"gross_gex_1pct":25383858.996927075,"call_oi":300,"put_oi":0},{"strike":45150.0,"call_gex_1pct":3520616.411656724,"put_gex_1pct":0.0,"net_gex_1pct":3520616.411656724,"gross_gex_1pct":3520616.411656724,"call_oi":43,"put_oi":0},{"strike":45200.0,"call_gex_1pct":26173890.41770683,"put_gex_1pct":0.0,"net_gex_1pct":26173890.41770683,"gross_gex_1pct":26173890.41770683,"call_oi":341,"put_oi":0},{"strike":45250.0,"call_gex_1pct":3852806.13129856,"put_gex_1pct":0.0,"net_gex_1pct":3852806.13129856,"gross_gex_1pct":3852806.13129856,"call_oi":53,"put_oi":0},{"strike":45300.0,"call_gex_1pct":24353155.951673217,"put_gex_1pct":0.0,"net_gex_1pct":24353155.951673217,"gross_gex_1pct":24353155.951673217,"call_oi":367,"put_oi":0},{"strike":45350.0,"call_gex_1pct":4292981.289701465,"put_gex_1pct":0.0,"net_gex_1pct":4292981.289701465,"gross_gex_1pct":4292981.289701465,"call_oi":67,"put_oi":0},{"strike":45400.0,"call_gex_1pct":5135126.250309202,"put_gex_1pct":0.0,"net_gex_1pct":5135126.250309202,"gross_gex_1pct":5135126.250309202,"call_oi":85,"put_oi":0},{"strike":45450.0,"call_gex_1pct":3800419.076361454,"put_gex_1pct":0.0,"net_gex_1pct":3800419.076361454,"gross_gex_1pct":3800419.076361454,"call_oi":69,"put_oi":0},{"strike":45500.0,"call_gex_1pct":24976812.826138765,"put_gex_1pct":0.0,"net_gex_1pct":24976812.826138765,"gross_gex_1pct":24976812.826138765,"call_oi":476,"put_oi":0},{"strike":45550.0,"call_gex_1pct":2446315.2861964116,"put_gex_1pct":0.0,"net_gex_1pct":2446315.2861964116,"gross_gex_1pct":2446315.2861964116,"call_oi":49,"put_oi":0},{"strike":45600.0,"call_gex_1pct":7005775.974635797,"put_gex_1pct":0.0,"net_gex_1pct":7005775.974635797,"gross_gex_1pct":7005775.974635797,"call_oi":154,"put_oi":0},{"strike":45650.0,"call_gex_1pct":1547293.548116699,"put_gex_1pct":0.0,"net_gex_1pct":1547293.548116699,"gross_gex_1pct":1547293.548116699,"call_oi":36,"put_oi":0},{"strike":45700.0,"call_gex_1pct":4253156.34377317,"put_gex_1pct":0.0,"net_gex_1pct":4253156.34377317,"gross_gex_1pct":4253156.34377317,"call_oi":109,"put_oi":0},{"strike":45750.0,"call_gex_1pct":2226602.1527006812,"put_gex_1pct":0.0,"net_gex_1pct":2226602.1527006812,"gross_gex_1pct":2226602.1527006812,"call_oi":61,"put_oi":0},{"strike":45800.0,"call_gex_1pct":3898307.7070926847,"put_gex_1pct":0.0,"net_gex_1pct":3898307.7070926847,"gross_gex_1pct":3898307.7070926847,"call_oi":112,"put_oi":0},{"strike":45850.0,"call_gex_1pct":2852291.9174538883,"put_gex_1pct":0.0,"net_gex_1pct":2852291.9174538883,"gross_gex_1pct":2852291.9174538883,"call_oi":84,"put_oi":0},{"strike":45900.0,"call_gex_1pct":2996724.9456421477,"put_gex_1pct":0.0,"net_gex_1pct":2996724.9456421477,"gross_gex_1pct":2996724.9456421477,"call_oi":95,"put_oi":0},{"strike":45950.0,"call_gex_1pct":1135512.0997133562,"put_gex_1pct":0.0,"net_gex_1pct":1135512.0997133562,"gross_gex_1pct":1135512.0997133562,"call_oi":39,"put_oi":0},{"strike":46000.0,"call_gex_1pct":20697186.816607956,"put_gex_1pct":0.0,"net_gex_1pct":20697186.816607956,"gross_gex_1pct":20697186.816607956,"call_oi":751,"put_oi":0},{"strike":46050.0,"call_gex_1pct":3931303.222315048,"put_gex_1pct":0.0,"net_gex_1pct":3931303.222315048,"gross_gex_1pct":3931303.222315048,"call_oi":147,"put_oi":0},{"strike":46100.0,"call_gex_1pct":2282002.986833743,"put_gex_1pct":0.0,"net_gex_1pct":2282002.986833743,"gross_gex_1pct":2282002.986833743,"call_oi":96,"put_oi":0},{"strike":46150.0,"call_gex_1pct":720097.330402941,"put_gex_1pct":0.0,"net_gex_1pct":720097.330402941,"gross_gex_1pct":720097.330402941,"call_oi":31,"put_oi":0},{"strike":46200.0,"call_gex_1pct":2436093.3692192314,"put_gex_1pct":0.0,"net_gex_1pct":2436093.3692192314,"gross_gex_1pct":2436093.3692192314,"call_oi":110,"put_oi":0},{"strike":46250.0,"call_gex_1pct":611594.3382037911,"put_gex_1pct":0.0,"net_gex_1pct":611594.3382037911,"gross_gex_1pct":611594.3382037911,"call_oi":29,"put_oi":0},{"strike":46300.0,"call_gex_1pct":10694676.567851277,"put_gex_1pct":0.0,"net_gex_1pct":10694676.567851277,"gross_gex_1pct":10694676.567851277,"call_oi":561,"put_oi":0},{"strike":46350.0,"call_gex_1pct":1939532.1362207762,"put_gex_1pct":0.0,"net_gex_1pct":1939532.1362207762,"gross_gex_1pct":1939532.1362207762,"call_oi":104,"put_oi":0},{"strike":46400.0,"call_gex_1pct":5965703.904369272,"put_gex_1pct":0.0,"net_gex_1pct":5965703.904369272,"gross_gex_1pct":5965703.904369272,"call_oi":346,"put_oi":0},{"strike":46450.0,"call_gex_1pct":882328.7971902197,"put_gex_1pct":0.0,"net_gex_1pct":882328.7971902197,"gross_gex_1pct":882328.7971902197,"call_oi":55,"put_oi":0},{"strike":46500.0,"call_gex_1pct":43882319.05015887,"put_gex_1pct":0.0,"net_gex_1pct":43882319.05015887,"gross_gex_1pct":43882319.05015887,"call_oi":2956,"put_oi":0},{"strike":46550.0,"call_gex_1pct":1228070.6821435946,"put_gex_1pct":0.0,"net_gex_1pct":1228070.6821435946,"gross_gex_1pct":1228070.6821435946,"call_oi":90,"put_oi":0},{"strike":46600.0,"call_gex_1pct":3166125.5733328583,"put_gex_1pct":0.0,"net_gex_1pct":3166125.5733328583,"gross_gex_1pct":3166125.5733328583,"call_oi":241,"put_oi":0},{"strike":46650.0,"call_gex_1pct":1504680.959796323,"put_gex_1pct":0.0,"net_gex_1pct":1504680.959796323,"gross_gex_1pct":1504680.959796323,"call_oi":119,"put_oi":0},{"strike":46700.0,"call_gex_1pct":742079.961394939,"put_gex_1pct":0.0,"net_gex_1pct":742079.961394939,"gross_gex_1pct":742079.961394939,"call_oi":61,"put_oi":0},{"strike":46750.0,"call_gex_1pct":374378.361143709,"put_gex_1pct":0.0,"net_gex_1pct":374378.361143709,"gross_gex_1pct":374378.361143709,"call_oi":32,"put_oi":0},{"strike":46800.0,"call_gex_1pct":1536938.1738985183,"put_gex_1pct":0.0,"net_gex_1pct":1536938.1738985183,"gross_gex_1pct":1536938.1738985183,"call_oi":134,"put_oi":0},{"strike":46850.0,"call_gex_1pct":497125.69093665405,"put_gex_1pct":0.0,"net_gex_1pct":497125.69093665405,"gross_gex_1pct":497125.69093665405,"call_oi":47,"put_oi":0},{"strike":46900.0,"call_gex_1pct":426377.6005630713,"put_gex_1pct":0.0,"net_gex_1pct":426377.6005630713,"gross_gex_1pct":426377.6005630713,"call_oi":43,"put_oi":0},{"strike":46950.0,"call_gex_1pct":826143.6475053643,"put_gex_1pct":0.0,"net_gex_1pct":826143.6475053643,"gross_gex_1pct":826143.6475053643,"call_oi":87,"put_oi":0},{"strike":47000.0,"call_gex_1pct":4686624.154791371,"put_gex_1pct":0.0,"net_gex_1pct":4686624.154791371,"gross_gex_1pct":4686624.154791371,"call_oi":503,"put_oi":0},{"strike":47050.0,"call_gex_1pct":133751.22082988682,"put_gex_1pct":0.0,"net_gex_1pct":133751.22082988682,"gross_gex_1pct":133751.22082988682,"call_oi":15,"put_oi":0},{"strike":47100.0,"call_gex_1pct":289845.55179383676,"put_gex_1pct":0.0,"net_gex_1pct":289845.55179383676,"gross_gex_1pct":289845.55179383676,"call_oi":34,"put_oi":0},{"strike":47150.0,"call_gex_1pct":100438.81461218423,"put_gex_1pct":0.0,"net_gex_1pct":100438.81461218423,"gross_gex_1pct":100438.81461218423,"call_oi":12,"put_oi":0},{"strike":47200.0,"call_gex_1pct":318367.8236907124,"put_gex_1pct":0.0,"net_gex_1pct":318367.8236907124,"gross_gex_1pct":318367.8236907124,"call_oi":41,"put_oi":0},{"strike":47250.0,"call_gex_1pct":136040.86766787968,"put_gex_1pct":0.0,"net_gex_1pct":136040.86766787968,"gross_gex_1pct":136040.86766787968,"call_oi":19,"put_oi":0},{"strike":47300.0,"call_gex_1pct":18641437.71853401,"put_gex_1pct":0.0,"net_gex_1pct":18641437.71853401,"gross_gex_1pct":18641437.71853401,"call_oi":2743,"put_oi":0},{"strike":47350.0,"call_gex_1pct":25750.72799889908,"put_gex_1pct":0.0,"net_gex_1pct":25750.72799889908,"gross_gex_1pct":25750.72799889908,"call_oi":4,"put_oi":0},{"strike":47400.0,"call_gex_1pct":139176.56188733818,"put_gex_1pct":0.0,"net_gex_1pct":139176.56188733818,"gross_gex_1pct":139176.56188733818,"call_oi":22,"put_oi":0},{"strike":47450.0,"call_gex_1pct":23920.536468488044,"put_gex_1pct":0.0,"net_gex_1pct":23920.536468488044,"gross_gex_1pct":23920.536468488044,"call_oi":4,"put_oi":0},{"strike":47500.0,"call_gex_1pct":523205.20888398576,"put_gex_1pct":0.0,"net_gex_1pct":523205.20888398576,"gross_gex_1pct":523205.20888398576,"call_oi":89,"put_oi":0},{"strike":47550.0,"call_gex_1pct":55436.20762553653,"put_gex_1pct":0.0,"net_gex_1pct":55436.20762553653,"gross_gex_1pct":55436.20762553653,"call_oi":10,"put_oi":0},{"strike":47600.0,"call_gex_1pct":109029.65765313864,"put_gex_1pct":0.0,"net_gex_1pct":109029.65765313864,"gross_gex_1pct":109029.65765313864,"call_oi":20,"put_oi":0},{"strike":47650.0,"call_gex_1pct":128684.7209369735,"put_gex_1pct":0.0,"net_gex_1pct":128684.7209369735,"gross_gex_1pct":128684.7209369735,"call_oi":24,"put_oi":0},{"strike":47700.0,"call_gex_1pct":601312.1337187024,"put_gex_1pct":0.0,"net_gex_1pct":601312.1337187024,"gross_gex_1pct":601312.1337187024,"call_oi":114,"put_oi":0},{"strike":47750.0,"call_gex_1pct":731762.6973977039,"put_gex_1pct":0.0,"net_gex_1pct":731762.6973977039,"gross_gex_1pct":731762.6973977039,"call_oi":141,"put_oi":0},{"strike":47800.0,"call_gex_1pct":366164.72001526924,"put_gex_1pct":0.0,"net_gex_1pct":366164.72001526924,"gross_gex_1pct":366164.72001526924,"call_oi":75,"put_oi":0},{"strike":47850.0,"call_gex_1pct":922585.6427441669,"put_gex_1pct":0.0,"net_gex_1pct":922585.6427441669,"gross_gex_1pct":922585.6427441669,"call_oi":192,"put_oi":0},{"strike":47900.0,"call_gex_1pct":146632.30901668064,"put_gex_1pct":0.0,"net_gex_1pct":146632.30901668064,"gross_gex_1pct":146632.30901668064,"call_oi":31,"put_oi":0},{"strike":47950.0,"call_gex_1pct":4656.9475811993425,"put_gex_1pct":0.0,"net_gex_1pct":4656.9475811993425,"gross_gex_1pct":4656.9475811993425,"call_oi":1,"put_oi":0},{"strike":48000.0,"call_gex_1pct":871280.0738202869,"put_gex_1pct":0.0,"net_gex_1pct":871280.0738202869,"gross_gex_1pct":871280.0738202869,"call_oi":190,"put_oi":0},{"strike":48050.0,"call_gex_1pct":25806.318828672353,"put_gex_1pct":0.0,"net_gex_1pct":25806.318828672353,"gross_gex_1pct":25806.318828672353,"call_oi":6,"put_oi":0},{"strike":48100.0,"call_gex_1pct":25418.471103337157,"put_gex_1pct":0.0,"net_gex_1pct":25418.471103337157,"gross_gex_1pct":25418.471103337157,"call_oi":6,"put_oi":0},{"strike":48150.0,"call_gex_1pct":8346.746643809185,"put_gex_1pct":0.0,"net_gex_1pct":8346.746643809185,"gross_gex_1pct":8346.746643809185,"call_oi":2,"put_oi":0},{"strike":48200.0,"call_gex_1pct":723691.4095551721,"put_gex_1pct":0.0,"net_gex_1pct":723691.4095551721,"gross_gex_1pct":723691.4095551721,"call_oi":176,"put_oi":0},{"strike":48250.0,"call_gex_1pct":11526.537332738428,"put_gex_1pct":0.0,"net_gex_1pct":11526.537332738428,"gross_gex_1pct":11526.537332738428,"call_oi":3,"put_oi":0},{"strike":48300.0,"call_gex_1pct":3786.5343640959654,"put_gex_1pct":0.0,"net_gex_1pct":3786.5343640959654,"gross_gex_1pct":3786.5343640959654,"call_oi":1,"put_oi":0},{"strike":48400.0,"call_gex_1pct":29433.550931030397,"put_gex_1pct":0.0,"net_gex_1pct":29433.550931030397,"gross_gex_1pct":29433.550931030397,"call_oi":8,"put_oi":0},{"strike":48500.0,"call_gex_1pct":2135984.685890438,"put_gex_1pct":0.0,"net_gex_1pct":2135984.685890438,"gross_gex_1pct":2135984.685890438,"call_oi":633,"put_oi":0},{"strike":48600.0,"call_gex_1pct":13128.013113727404,"put_gex_1pct":0.0,"net_gex_1pct":13128.013113727404,"gross_gex_1pct":13128.013113727404,"call_oi":4,"put_oi":0},{"strike":48700.0,"call_gex_1pct":8984.278884200552,"put_gex_1pct":0.0,"net_gex_1pct":8984.278884200552,"gross_gex_1pct":8984.278884200552,"call_oi":3,"put_oi":0},{"strike":48800.0,"call_gex_1pct":23323.794600282745,"put_gex_1pct":0.0,"net_gex_1pct":23323.794600282745,"gross_gex_1pct":23323.794600282745,"call_oi":8,"put_oi":0},{"strike":48900.0,"call_gex_1pct":85189.04244053146,"put_gex_1pct":0.0,"net_gex_1pct":85189.04244053146,"gross_gex_1pct":85189.04244053146,"call_oi":30,"put_oi":0},{"strike":49000.0,"call_gex_1pct":5974877.738447266,"put_gex_1pct":0.0,"net_gex_1pct":5974877.738447266,"gross_gex_1pct":5974877.738447266,"call_oi":2320,"put_oi":0},{"strike":49200.0,"call_gex_1pct":17137.83381813022,"put_gex_1pct":0.0,"net_gex_1pct":17137.83381813022,"gross_gex_1pct":17137.83381813022,"call_oi":7,"put_oi":0},{"strike":49300.0,"call_gex_1pct":30838.51590318926,"put_gex_1pct":0.0,"net_gex_1pct":30838.51590318926,"gross_gex_1pct":30838.51590318926,"call_oi":14,"put_oi":0},{"strike":49400.0,"call_gex_1pct":2149.775790512133,"put_gex_1pct":0.0,"net_gex_1pct":2149.775790512133,"gross_gex_1pct":2149.775790512133,"call_oi":1,"put_oi":0},{"strike":49500.0,"call_gex_1pct":46175.80168650564,"put_gex_1pct":0.0,"net_gex_1pct":46175.80168650564,"gross_gex_1pct":46175.80168650564,"call_oi":22,"put_oi":0},{"strike":49600.0,"call_gex_1pct":6150.031357120203,"put_gex_1pct":0.0,"net_gex_1pct":6150.031357120203,"gross_gex_1pct":6150.031357120203,"call_oi":3,"put_oi":0},{"strike":49700.0,"call_gex_1pct":2003.0010948265187,"put_gex_1pct":0.0,"net_gex_1pct":2003.0010948265187,"gross_gex_1pct":2003.0010948265187,"call_oi":1,"put_oi":0},{"strike":49900.0,"call_gex_1pct":20932.40362125869,"put_gex_1pct":0.0,"net_gex_1pct":20932.40362125869,"gross_gex_1pct":20932.40362125869,"call_oi":12,"put_oi":0},{"strike":50000.0,"call_gex_1pct":179133.35711680222,"put_gex_1pct":0.0,"net_gex_1pct":179133.35711680222,"gross_gex_1pct":179133.35711680222,"call_oi":105,"put_oi":0},{"strike":50100.0,"call_gex_1pct":14978.519923861595,"put_gex_1pct":0.0,"net_gex_1pct":14978.519923861595,"gross_gex_1pct":14978.519923861595,"call_oi":10,"put_oi":0},{"strike":50300.0,"call_gex_1pct":7564.977625459207,"put_gex_1pct":0.0,"net_gex_1pct":7564.977625459207,"gross_gex_1pct":7564.977625459207,"call_oi":6,"put_oi":0},{"strike":50400.0,"call_gex_1pct":14813.908642789862,"put_gex_1pct":0.0,"net_gex_1pct":14813.908642789862,"gross_gex_1pct":14813.908642789862,"call_oi":12,"put_oi":0},{"strike":50500.0,"call_gex_1pct":3091.039729989163,"put_gex_1pct":0.0,"net_gex_1pct":3091.039729989163,"gross_gex_1pct":3091.039729989163,"call_oi":3,"put_oi":0},{"strike":50600.0,"call_gex_1pct":1009.3226345019959,"put_gex_1pct":0.0,"net_gex_1pct":1009.3226345019959,"gross_gex_1pct":1009.3226345019959,"call_oi":1,"put_oi":0},{"strike":50700.0,"call_gex_1pct":12842.285644681078,"put_gex_1pct":0.0,"net_gex_1pct":12842.285644681078,"gross_gex_1pct":12842.285644681078,"call_oi":16,"put_oi":0},{"strike":50800.0,"call_gex_1pct":3933.092708405733,"put_gex_1pct":0.0,"net_gex_1pct":3933.092708405733,"gross_gex_1pct":3933.092708405733,"call_oi":5,"put_oi":0},{"strike":51000.0,"call_gex_1pct":217017.96628339813,"put_gex_1pct":0.0,"net_gex_1pct":217017.96628339813,"gross_gex_1pct":217017.96628339813,"call_oi":387,"put_oi":0},{"strike":51300.0,"call_gex_1pct":2117.155814505645,"put_gex_1pct":0.0,"net_gex_1pct":2117.155814505645,"gross_gex_1pct":2117.155814505645,"call_oi":4,"put_oi":0},{"strike":51500.0,"call_gex_1pct":302.44502211687114,"put_gex_1pct":0.0,"net_gex_1pct":302.44502211687114,"gross_gex_1pct":302.44502211687114,"call_oi":1,"put_oi":0},{"strike":51800.0,"call_gex_1pct":572.6230647322604,"put_gex_1pct":0.0,"net_gex_1pct":572.6230647322604,"gross_gex_1pct":572.6230647322604,"call_oi":2,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,100 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-03→2026-11-04) | -900 | TAIFEX Proxy snapshots (2026-11-03) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 295,701 | 292,072 | +3,629 | 74,710 | 75,626 | -916 | +4,545 | TAIFEX Proxy |
| 投信 | 202 | 15,585 | -15,383 | 0 | 0 | +0 | -15,383 | TAIFEX Proxy |
| 自營商 | 215,117 | 214,226 | +891 | 45,931 | 46,158 | -227 | +1,118 | TAIFEX Proxy |
| 三大法人合計 | 511,020 | 521,883 | -10,863 | 120,641 | 121,784 | -1,143 | -9,720 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 21.05 | 20.57 | +0.47 | 8.79 | 8.93 | -0.14 | +0.61 | TAIFEX Proxy |
| 投信 | 0.05 | 14.56 | -14.51 | 0.00 | 0.00 | +0 | -14.51 | TAIFEX Proxy |
| 自營商 | 33.99 | 21.10 | +12.89 | 7.45 | 6.28 | +1.18 | +11.72 | TAIFEX Proxy |
| 三大法人合計 | 55.09 | 56.23 | -1.14 | 16.25 | 15.21 | +1.04 | -2.18 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,926 | TAIFEX Proxy |
| 買權空方 OI | 16,052 | TAIFEX Proxy |
| 買權多空淨 OI | -4,126 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-02→2026-11-04) | -1,253 | TAIFEX Proxy snapshots (2026-11-03) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,715 | TAIFEX Proxy |
| 賣權空方 OI | 11,434 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,719 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-02→2026-11-04) | -679 | TAIFEX Proxy snapshots (2026-11-03) |
- 資料日期：買權 2026-11-04／賣權 2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -977 | 2026-11-02→2026-11-04 | TAIFEX Proxy snapshots (2026-11-03) |
| 買權前十大 | -1,253 | 2026-11-02→2026-11-04 | TAIFEX Proxy snapshots (2026-11-03) |
| 賣權前十大 | -679 | 2026-11-02→2026-11-04 | TAIFEX Proxy snapshots (2026-11-03) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-04；資料時間：2026-11-05 10:46:49；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：futures.futures.night.settle, futures.futures.night.oi
- 註記：futures-price-after-hours 日期 2026-11-04 非今日 2026-11-05，視為無新節次，不採用
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
- margin_ratio：`Blave 上市市場融資維持率估算（資料日期：2026-11-04；自建計算備援）`
- sbl_bal：`TWSE TWT72U（SLBNLB；上市+上櫃）`
- sbl_sale_bal：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- sbl_sale_chg：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：TWSE 自建計算未成功（ValueError: listed securities missing T0 close: ['1589']）；改用 Blave 同 T0 數值（2026-11-04）。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,499.0 | -93,647 | -1,860 | -469 | +3,629 | -916 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +272.6 | +89,500 | +2,502 | +0 | -15,383 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -375.2 | +2,961 | -991 | -310 | +891 | -227 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
