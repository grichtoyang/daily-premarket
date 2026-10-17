# DATA_REPORT_20261016

- 報告日期：`2026-10-17`
- T0 交易日期：`2026-10-16`
- 資料產出時間：`2026-10-17 11:34:23`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`local`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,111.26 | 點 | twse-proxy |
| 開盤 | 46,995.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,520.60 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,995.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,111.26 | 點 | twse-proxy |
| 漲跌點數 | 141.39 | 點 | twse-proxy |
| 漲跌幅 | +0.30 | % | twse-proxy |
| 成交金額 | 9,938.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 684 | twse-proxy |
| 下跌家數 | 286 | twse-proxy |
| 平盤家數 | 106 | twse-proxy |
| 漲停家數 | 19 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 542 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 247 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 76 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 21 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -461.5 | 億元 | twse-proxy /institutional |
| 投信 | +110.5 | 億元 | twse-proxy /institutional |
| 自營商 | -334.1 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -685.1 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,638.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -15.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 271,848 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 9,054 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 183.39 | % | wantgoo 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,554,216 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 38,246 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 4,602 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,938.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,218.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,156.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,659.44 | -84.62 | -1.09 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,140.03 | -573.00 | -2.15 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,187.55 | -748.05 | -2.50 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,002.40 | -175.29 | -0.34 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,137.29 | -443.92 | -3.83 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.99 | 3.53 | +21.45 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,324.29 | 898.34 | +1.39 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,668.05 | 113.83 | +2.05 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,186.83 | 124.11 | +0.52 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,716.28 | 8.81 | +0.24 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,802.46 | -14.33 | -0.12 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,704.25 | -86.75 | -1.11 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,391.50 | -752.25 | -2.50 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,200.00 | -230.00 | -0.44 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,735.50 | -46.30 | -1.66 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.74 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.10 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.44 | 0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.43 | 0.10 | +0.31 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.78 | -0.22 | -0.22 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.99 | -0.16 | -0.10 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,329.60 | -11.35 | -0.85 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 412.61 | -9.64 | -2.28 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.82 | -1.10 | -5.26 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.53 | -2.36 | -5.63 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 99.04 | 1.07 | +1.09 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,186.70 | 16.60 | +0.40 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,454.07 | -687.39 | -0.84 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：00946十一月除息0.058元！連15個月不變　想領息最晚這天買
  - 來源：Yahoo 台股；發布時間：2026-10-16T10:53:56Z；台北時間：2026-10-16 18:53
  - 摘要：群益科技高息成長ETF（00946）預估每股配發0.058元，維持連15個月配息水準不變，除息交易日選定11月4日，想參與領息的投資人，來看看最晚哪一天要買進？哪一天入帳？
  - 原文連結：https://tw.stock.yahoo.com/news/00946%E5%8D%81-%E6%9C%88%E9%99%A4%E6%81%AF0-058%E5%85%83-%E9%80%A315%E5%80%8B%E6%9C%88%E4%B8%8D%E8%AE%8A-%E6%83%B3%E9%A0%98%E6%81%AF%E6%9C%80%E6%99%9A%E9%80%99%E5%A4%A9%E8%B2%B7-105356369.html
- 事件2：爸媽贊助200萬頭期款！ 他想丟股市「5年後再買房」 網勸：不是穩賺
  - 來源：Yahoo 台股；發布時間：2026-10-16T10:33:00Z；台北時間：2026-10-16 18:33
  - 摘要：資金該「買房」或「買股」是熱議話題。有網友表示有2百萬資金，若買房家人會再贊助2百萬，但他擔心買房後資金被卡住，考慮「投入股市5年後再買房」，引發兩派網友激辯。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%88%B8%E5%AA%BD%E8%B4%8A%E5%8A%A9200%E8%90%AC%E9%A0%AD%E6%9C%9F%E6%AC%BE-%E4%BB%96%E6%83%B3%E4%B8%9F%E8%82%A1%E5%B8%82-5%E5%B9%B4%E5%BE%8C%E5%86%8D%E8%B2%B7%E6%88%BF-%E7%B6%B2%E5%8B%B8-%E4%B8%8D%E6%98%AF%E7%A9%A9%E8%B3%BA-103300429.html
- 事件3：00939配息新高0.15元！今創歷史新高價　11月3日除息
  - 來源：Yahoo 台股；發布時間：2026-10-16T09:58:37Z；台北時間：2026-10-16 17:58
  - 摘要：每月配息的統一台灣高息動能ETF (00939)，11月即將除息，預計每受益權單位配發0.15元，是掛牌以來的最高配息金額。本次除息交易日為11月3日，想領息的投資人，最晚要在11月2日買進，就能在11月25日領到錢。
  - 原文連結：https://tw.stock.yahoo.com/news/00939%E9%85%8D%E6%81%AF%E6%96%B0%E9%AB%980-15%E5%85%83-%E4%BB%8A%E5%89%B5%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98%E5%83%B9-11%E6%9C%883%E6%97%A5%E9%99%A4%E6%81%AF-095837685.html
- 事件4：她14歲打工照顧中風父…8旬母離家多年來討扶養費 女兒仍得付
  - 來源：Yahoo 台股；發布時間：2026-10-16T09:58:32Z；台北時間：2026-10-16 17:58
  - 摘要：新竹一名8旬老婦年邁無力謀生，向60歲女兒請求扶養；女兒控母親自幼沉迷賭博、外遇離家，自己14歲就得打工，要求免除扶養義務。新竹地院認定無法證明母親未盡扶養責任，裁定女兒每月須付1萬2500元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A5%B914%E6%AD%B2%E6%89%93%E5%B7%A5%E7%85%A7%E9%A1%A7%E4%B8%AD%E9%A2%A8%E7%88%B6-8%E6%97%AC%E6%AF%8D%E9%9B%A2%E5%AE%B6%E5%A4%9A%E5%B9%B4%E4%BE%86%E8%A8%8E%E6%89%B6%E9%A4%8A%E8%B2%BB-%E5%A5%B3%E5%85%92%E4%BB%8D%E5%BE%97%E4%BB%98-095832555.html
- 事件5：政府積極推動亞資中心！賴清德：先留資、再引資 持續壯大金融市場
  - 來源：Yahoo 台股；發布時間：2026-10-16T08:58:00Z；台北時間：2026-10-16 16:58
  - 摘要：政府積極推動亞洲資產管理中心計畫，總統賴清德今天（16日）接受網路財經頻道《游皓庭的財經視角》專訪時表示，亞資管理中心是要先將把資金留下來，先留資、再引資，透過引資創造台灣更好的投資動能，持續壯大台灣的金融市場，目前政策推動順利。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%94%BF%E5%BA%9C%E7%A9%8D%E6%A5%B5%E6%8E%A8%E5%8B%95%E4%BA%9E%E8%B3%87%E4%B8%AD%E5%BF%83-%E8%B3%B4%E6%B8%85%E5%BE%B7-%E5%85%88%E7%95%99%E8%B3%87-%E5%86%8D%E5%BC%95%E8%B3%87-%E6%8C%81%E7%BA%8C%E5%A3%AF%E5%A4%A7%E9%87%91%E8%9E%8D%E5%B8%82%E5%A0%B4-085800107.html
- 事件6：買房撞上股市大跌！他月底要繳150萬工程款「錢都在ETF」　過來人建議：會怕就趕快賣
  - 來源：Yahoo 台股；發布時間：2026-10-16T08:05:00Z；台北時間：2026-10-16 16:05
  - 摘要：[FTNN新聞網]實習記者鄭巧薰／綜合報導股市投資除了追求報酬為，也得留意資金調度問題。近日一名網友在PTT發文表示，上個月才買下一間預售屋，月底就得繳約15...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B2%B7%E6%88%BF%E6%92%9E%E4%B8%8A%E8%82%A1%E5%B8%82%E5%A4%A7%E8%B7%8C-%E4%BB%96%E6%9C%88%E5%BA%95%E8%A6%81%E7%B9%B3150%E8%90%AC%E5%B7%A5%E7%A8%8B%E6%AC%BE-%E9%8C%A2%E9%83%BD%E5%9C%A8etf-%E9%81%8E%E4%BE%86%E4%BA%BA%E5%BB%BA%E8%AD%B0-%E6%9C%83%E6%80%95%E5%B0%B1%E8%B6%95%E5%BF%AB%E8%B3%A3-080500364.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：Analysis: Why a $2 trillion deficit and 5% Treasury yields are becoming America's biggest economic challenge
  - 來源：CNBC；發布時間：Fri, 16 Oct 2026 22:33:05 GMT；台北時間：2026-10-17 06:33
  - 摘要：Treasury yields above 5% are raising borrowing costs for households and the federal government, highlighting the challenge of financing $2 trillion de
  - 原文連結：https://www.cnbc.com/2026/10/15/treasury-yields-deficit-national-debt-ai.html
- 事件9：Fed's Warsh withholds rate signal, praises recent global tightening
  - 來源：CNBC；發布時間：Fri, 16 Oct 2026 12:36:00 GMT；台北時間：2026-10-16 20:36
  - 摘要：Warsh refrained from signaling another interest rate hike this month, pointed to a "synchronous tightening" by central banks in the fight against infl
  - 原文連結：https://www.cnbc.com/2026/10/16/feds-warsh-says-ai-development-path-will-be-very-bumpy-.html
- 事件10：The bond market shrugged off two inflation shocks. Why stock investors should pay attention.
  - 來源：MarketWatch；發布時間：Fri, 16 Oct 2026 21:30:00 GMT；台北時間：2026-10-17 05:30
  - 摘要：Hot CPI and PPI data should have pushed Treasury yields higher. Instead, bond buyers stepped in to suggest yields have risen high enough to become att
  - 原文連結：https://www.marketwatch.com/story/the-bond-market-shrugged-off-two-inflation-shocks-why-stock-investors-should-pay-attention-5da4f771?mod=mw_rss_topstories
- 事件11：Your Social Security check will rise an average of $75 a month &#x2014; will it be able to keep up with inflation?
  - 來源：MarketWatch；發布時間：Fri, 16 Oct 2026 19:45:00 GMT；台北時間：2026-10-17 03:45
  - 摘要：The 3.6% COLA for 2027 is aimed at helping more than 68 million beneficiaries keep pace with the cost of living
  - 原文連結：https://www.marketwatch.com/story/social-securitys-cola-will-be-3-6-in-2027-as-inflation-persists-f7c9dff2?mod=mw_rss_topstories
- 事件12：Brent oil touches $110 as Iran escalates Hormuz attacks, Ukraine vows to hit Russian refineries
  - 來源：CNBC；發布時間：Fri, 16 Oct 2026 20:02:21 GMT；台北時間：2026-10-17 04:02
  - 摘要：U.S. crude oil prices rose sharply Friday as Iran escalated attacks in the Strait of Hormuz this week.
  - 原文連結：https://www.cnbc.com/2026/10/16/oil-price-today-iran-strait-hormuz-ukraine-russia.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-16

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,228 | TAIFEX Proxy |
| 最高價 | 47,634 | TAIFEX Proxy |
| 最低價 | 47,140 | TAIFEX Proxy |
| 收盤價 | 47,242 | TAIFEX Proxy |
| 漲跌點數 | +311 | TAIFEX Proxy |
| 漲跌幅 | +0.66 | TAIFEX Proxy |
| 成交量 | 104,595 | TAIFEX Proxy |
| 日盤高點及低點 | 47,634 / 47,140 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,926 | TAIFEX Proxy |
| 最高價 | 47,417 | TAIFEX Proxy |
| 最低價 | 46,456 | TAIFEX Proxy |
| 收盤價 | 47,366 | TAIFEX Proxy |
| 漲跌點數 | +435 | TAIFEX Proxy |
| 漲跌幅 | +0.93 | TAIFEX Proxy |
| 成交量 | 41,283 | TAIFEX Proxy |
| 夜盤高點及低點 | unavailable / unavailable | 端點未提供 |
| 結算價 | 47,284 | TAIFEX Proxy |
| 未平倉量 | 97,247 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,812 | TAIFEX Proxy |
| 外資空方 OI | 103,487 | TAIFEX Proxy |
| 外資多空淨 OI | -93,675 | TAIFEX Proxy |
| 投信多方 OI | 85,208 | TAIFEX Proxy |
| 投信空方 OI | 2,744 | TAIFEX Proxy |
| 投信多空淨 OI | +82,464 | TAIFEX Proxy |
| 自營商多方 OI | 7,760 | TAIFEX Proxy |
| 自營商空方 OI | 4,563 | TAIFEX Proxy |
| 自營商多空淨 OI | +3,197 | TAIFEX Proxy |
| 三大法人合計多方 OI | 102,780 | TAIFEX Proxy |
| 三大法人合計空方 OI | 110,794 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -8,014 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +3,907 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +3,535 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -3,697 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 75,382 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,888 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +2,494 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-14→2026-10-16) | -1,577 | TAIFEX Proxy snapshots (2026-10-15) |
- 資料日期：2026-10-16 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 67,924 | TAIFEX Proxy |
| 外資日盤空單交易量 | 64,083 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +3,841 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 24,854 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 24,082 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +772 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +3,069 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +3,535 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +3,535 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -3,677 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +93 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -3,770 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +3,699 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +865 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +349.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +81.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 47,242 | TAIFEX Proxy |
| 加權指數價格 | 47,111.26 | twse-proxy |
| 台指期與加權指數價差 | +130.74 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.28 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +130.74 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +124 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 47,242 | 47,366 | -124 | TAIFEX Proxy |
| 成交量 | 63,312 | 41,283 | +22,029 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+3,745（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 67,924 | 64,083 | +3,841 | 24,854 | 24,082 | +772 | +3,069 | 9,812 | 103,487 | -93,675 | +3,907 | TAIFEX Proxy |
| 投信 | 9,852 | 6,317 | +3,535 | 0 | 0 | +0 | +3,535 | 85,208 | 2,744 | +82,464 | +3,535 | TAIFEX Proxy |
| 自營商 | 7,101 | 10,778 | -3,677 | 1,613 | 1,520 | +93 | -3,770 | 7,760 | 4,563 | +3,197 | -3,697 | TAIFEX Proxy |
| 三大法人合計 | 84,877 | 81,178 | +3,699 | 26,467 | 25,602 | +865 | +2,834 | 102,780 | 110,794 | -8,014 | +3,745 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 75,382 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,888 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +2,494 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-14→2026-10-16) | -1,577 | TAIFEX Proxy snapshots (2026-10-15) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 39.47% | TAIFEX Proxy |
| 夜盤漲跌點數 | +435 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +772 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-16 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F3 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-17 11:34:23 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 389,402 | TAIFEX Proxy |
| Call 總未平倉量 OI | 89,062 | TAIFEX Proxy |
| Call OI 增減 (2026-10-15→2026-10-16) | +19,916 | TAIFEX Proxy snapshots (2026-10-15) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 358,736 | TAIFEX Proxy |
| Put 總未平倉量 OI | 68,443 | TAIFEX Proxy |
| Put OI 增減 (2026-10-15→2026-10-16) | +35,066 | TAIFEX Proxy snapshots (2026-10-15) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.09 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.30 | TAIFEX Proxy |
| Put／Call Ratio | 0.77 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-15→2026-10-16) | 13.76 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-15→2026-10-16) | 6.76 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 130,253 | TAIFEX Proxy |
| 外資 Call日賣 | 133,320 | TAIFEX Proxy |
| 外資 Call日淨 | -3,067 | TAIFEX Proxy |
| 外資 Put日買 | 132,319 | TAIFEX Proxy |
| 外資 Put日賣 | 131,672 | TAIFEX Proxy |
| 外資 Put日淨 | +647 | TAIFEX Proxy |
| 外資 Call夜買 | 26,248 | TAIFEX Proxy |
| 外資 Call夜賣 | 26,357 | TAIFEX Proxy |
| 外資 Call夜淨 | -109 | TAIFEX Proxy |
| 外資 Put夜買 | 26,085 | TAIFEX Proxy |
| 外資 Put夜賣 | 25,181 | TAIFEX Proxy |
| 外資 Put夜淨 | +904 | TAIFEX Proxy |
| 外資 日盤淨總量 | -3,714 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -2,958 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -257 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 110,650 | TAIFEX Proxy |
| 自營商 Call日賣 | 108,651 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,999 | TAIFEX Proxy |
| 自營商 Put日買 | 92,031 | TAIFEX Proxy |
| 自營商 Put日賣 | 101,003 | TAIFEX Proxy |
| 自營商 Put日淨 | -8,972 | TAIFEX Proxy |
| 自營商 Call夜買 | 23,084 | TAIFEX Proxy |
| 自營商 Call夜賣 | 23,366 | TAIFEX Proxy |
| 自營商 Call夜淨 | -282 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,090 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,527 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,437 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +10,971 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,281 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -6,535 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,500 | 7,026 | TAIFEX Proxy |
| Call OI 第2大履約價 | 52,000 | 4,083 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,300 | 3,971 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,500 | 7,026 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,500 | 7,026 | 7.89% | TAIFEX Proxy |
| C2 | 52,000 | 4,083 | 4.58% | TAIFEX Proxy |
| C3 | 47,300 | 3,971 | 4.46% | TAIFEX Proxy |
| C4 | 47,500 | 3,618 | 4.06% | TAIFEX Proxy |
| C5 | 47,400 | 3,519 | 3.95% | TAIFEX Proxy |
| C6 | 49,000 | 3,005 | 3.37% | TAIFEX Proxy |
| C7 | 48,000 | 2,886 | 3.24% | TAIFEX Proxy |
| C8 | 47,600 | 2,558 | 2.87% | TAIFEX Proxy |
| C9 | 48,200 | 2,158 | 2.42% | TAIFEX Proxy |
| C10 | 48,600 | 2,083 | 2.34% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 44,500 | 4,129 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,200 | 3,442 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,000 | 3,360 | TAIFEX Proxy |
| Put OI 最大履約價 | 44,500 | 4,129 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 44,500 | 4,129 | 6.03% | TAIFEX Proxy |
| P2 | 47,200 | 3,442 | 5.03% | TAIFEX Proxy |
| P3 | 47,000 | 3,360 | 4.91% | TAIFEX Proxy |
| P4 | 47,250 | 3,069 | 4.48% | TAIFEX Proxy |
| P5 | 47,100 | 2,829 | 4.13% | TAIFEX Proxy |
| P6 | 46,000 | 2,704 | 3.95% | TAIFEX Proxy |
| P7 | 46,500 | 2,508 | 3.66% | TAIFEX Proxy |
| P8 | 47,300 | 2,254 | 3.29% | TAIFEX Proxy |
| P9 | 46,800 | 2,208 | 3.23% | TAIFEX Proxy |
| P10 | 47,150 | 2,098 | 3.07% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 47,300 (+3,285) | TAIFEX Proxy snapshots (2026-10-15) |
| Call OI 減少最多的履約價 | 50,000 (-580) | TAIFEX Proxy snapshots (2026-10-15) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,250 (+2,918) | TAIFEX Proxy snapshots (2026-10-15) |
| Put OI 減少最多的履約價 | 47,800 (-146) | TAIFEX Proxy snapshots (2026-10-15) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-15→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-15) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 44,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-15→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-15) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 資料日期 | 2026-10-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,906.04 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 資料日期 | 2026-10-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,300 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-15→2026-10-16) | -50 | TAIFEX Proxy snapshots (2026-10-15) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 261,925 | 265,639 | -3,714 | 108,739 | 109,921 | -1,182 | -2,532 | TAIFEX Proxy |
| 投信 | 60 | 8,200 | -8,140 | 0 | 0 | +0 | -8,140 | TAIFEX Proxy |
| 自營商 | 211,653 | 200,682 | +10,971 | 73,160 | 74,176 | -1,016 | +11,987 | TAIFEX Proxy |
| 三大法人合計 | 473,638 | 474,521 | -883 | 181,899 | 184,097 | -2,198 | +1,315 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.71 | 13.42 | +0.28 | 6.01 | 6.03 | -0.01 | +0.30 | TAIFEX Proxy |
| 投信 | 0.03 | 5.91 | -5.88 | 0.00 | 0.00 | +0 | -5.88 | TAIFEX Proxy |
| 自營商 | 17.24 | 11.32 | +5.91 | 4.75 | 4.32 | +0.43 | +5.48 | TAIFEX Proxy |
| 三大法人合計 | 30.97 | 30.65 | +0.31 | 10.76 | 10.35 | +0.41 | -0.10 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 22,175 | TAIFEX Proxy |
| 買權空方 OI | 25,773 | TAIFEX Proxy |
| 買權多空淨 OI | -3,598 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | -4,595 | TAIFEX Proxy snapshots (2026-10-15) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 13,668 | TAIFEX Proxy |
| 賣權空方 OI | 12,300 | TAIFEX Proxy |
| 賣權多空淨 OI | +1,368 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | +525 | TAIFEX Proxy snapshots (2026-10-15) |
- 資料日期：買權 unavailable／賣權 unavailable (TypeOfTraders=0 全部交易人；契約月份 unavailable)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,577 | 2026-10-14→2026-10-16 | TAIFEX Proxy snapshots (2026-10-15) |
| 買權前十大 | -4,595 | — | TAIFEX Proxy snapshots (2026-10-15) |
| 賣權前十大 | +525 | — | TAIFEX Proxy snapshots (2026-10-15) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-16；資料時間：2026-10-17 11:34:23；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：78 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (1)：options.top10_change
- 註記：futures-price-after-hours 日期 2026-10-16 非今日 2026-10-17，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-19 非今日 2026-10-17，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-19 非今日 2026-10-17，視為無新節次，不採用
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
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
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -461.5 | -93,675 | +3,841 | +772 | -3,714 | -1,182 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +110.5 | +82,464 | +3,535 | +0 | -8,140 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -334.1 | +3,197 | -3,677 | +93 | +10,971 | -1,016 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
