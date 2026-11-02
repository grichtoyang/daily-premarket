# DATA_REPORT_20261102

- 報告日期：`2026-11-02`
- T0 交易日期：`2026-11-02`
- 資料產出時間：`2026-11-02 14:35:26`
- 時區：`Asia/Taipei`
- 產出盤別：`日盤`
- 產出者：`actions`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 44,920.14 | 點 | twse-proxy |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 44,920.14 | 點 | twse-proxy |
| 漲跌點數 | -291.69 | 點 | twse-proxy |
| 漲跌幅 | -0.65 | % | twse-proxy |
| 成交金額 | 7,588.8 | 億元 | twse-proxy market_statistics |

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
| 上漲家數 | unavailable | TPEX |
| 下跌家數 | unavailable | TPEX |
| 平盤家數 | unavailable | TPEX |
| 漲停家數 | unavailable | TPEX |
| 跌停家數 | unavailable | TPEX |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,124.7 | 億元 | twse-proxy /institutional |
| 投信 | +236.2 | 億元 | twse-proxy /institutional |
| 自營商 | -513.7 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,402.2 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 197,359 | 張 | HiStock |
| 融券增減 | 9,581 | 張 | HiStock |
| 融資維持率 | unavailable | % | unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,525,241 | 張 | TWSE TWT96U + TWSE TWT96U OTC |
| 借券賣出餘額 | unavailable | 張 | 端點未提供 |
| 借券賣出增減 | unavailable | 張 | 端點未提供 |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 7,588.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | 7,588.8 | 億元 | twse-proxy market_statistics+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,580.07 | -140.32 | -1.82 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,437.00 | -747.72 | -2.86 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,384.85 | -1,017.66 | -3.46 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,770.31 | -572.25 | -1.09 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,688.80 | -829.40 | -7.20 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.42 | 2.22 | +12.91 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,034.58 | -255.53 | -0.40 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,872.72 | 141.98 | +2.48 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,413.81 | 119.39 | +0.51 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,634.00 | 34.98 | +0.97 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,044.90 | 211.12 | +1.95 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,647.50 | 33.50 | +0.44 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,777.00 | 243.00 | +0.85 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,073.00 | 155.00 | +0.30 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,835.10 | 13.80 | +0.49 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.56 | -0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.93 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.31 | -0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.61 | 0.04 | +0.13 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.86 | -0.02 | -0.02 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.87 | 0.06 | +0.04 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.88 | 5.90 | +0.44 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 406.13 | -25.68 | -5.95 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.68 | -1.36 | -7.54 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.50 | -5.05 | -11.34 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 100.70 | -3.42 | -3.28 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,919.10 | 20.20 | +0.52 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 78,071.52 | 636.77 | +0.82 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股下跌291點 終場仍守不住4萬5
  - 來源：Yahoo 台股；發布時間：2026-11-02T05:53:37Z；台北時間：2026-11-02 13:53
  - 摘要：即時中心／綜合報導美股四大指數上週五（29日）全面走弱，費半跌幅更高達7.2％，投資人憂心台股本週恐面臨新一波壓力。台股今（2）日早盤一度來到44,399.10點、大跌812.73點，所幸指數盤中逐步上拉；終場就收在44,920.14點、下
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%A4%B1%E5%AE%884%E8%90%AC5%E5%A4%A7%E9%97%9C-%E7%B5%82%E5%A0%B4%E4%B8%8B%E8%B7%8C291%E9%BB%9E-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%94%B62330%E5%85%83-055337085.html
- 事件2：00403A股價頻破發 首次配息恐怕面臨「0元」窘境
  - 來源：Yahoo 台股；發布時間：2026-11-02T05:20:00Z；台北時間：2026-11-02 13:20
  - 摘要：[FTNN新聞網]實習記者陳又綺／綜合報導主動型ETF「主動統一升級50（00403A）」即將迎來成立滿180天後的首次配息評價，全台超過79.3萬名投資人關注配息結果。...
  - 原文連結：https://tw.stock.yahoo.com/news/00403a%E9%A6%96%E6%AC%A1-%E9%85%8D%E6%81%AF%E6%81%90%E6%8E%9B0-%E7%88%86%E9%87%8F13%E8%90%AC%E5%BC%B5%E8%82%A1%E5%83%B9%E9%A0%BB%E7%A0%B4%E7%99%BC-%E7%90%86%E8%B2%A1%E5%B0%88%E5%AE%B6%E6%9B%9D%E9%97%9C%E9%8D%B5%E6%A2%9D%E4%BB%B6-052000991.html
- 事件3：00830啟動股票分割 倍數將依本月19日淨值決定
  - 來源：Yahoo 台股；發布時間：2026-11-02T05:40:53Z；台北時間：2026-11-02 13:40
  - 摘要：[Newtalk新聞] 面對國際金融市場震盪、台股短線波動加劇，投資人如何在市場變化中掌握布局契機，成為近期關注焦點。隨著AI、雲端及半導體產業需求持續升溫，台股中長期成長動能仍值得期待。 以下是國泰證期顧問整理最新熱門ETF，涵蓋半導體產
  - 原文連結：https://tw.stock.yahoo.com/news/00830%E5%95%9F%E5%8B%95%E8%82%A1%E7%A5%A8%E5%88%86%E5%89%B2-00406a%E5%B9%B4%E5%8C%96%E9%85%8D%E6%81%AF%E7%8E%8718-5-054053579.html
- 事件4：每股50元揪團賣股惹議 力晶告發起人籲查幕後買家
  - 來源：Yahoo 台股；發布時間：2026-11-02T04:42:37Z；台北時間：2026-11-02 12:42
  - 摘要：【財訊快報／記者李純君報導】力晶投控發布官方新聞稿，宣布提告違法公開收購股權，並已經正式啟動法律動作，更公開籲請政府嚴查鉅額金流合法性。力晶投控發布官宣，針對外界「揪團賣股」向不特定股東期約以超過136億元新台幣收購20%股權，已經在今（2
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8A%9B%E6%99%B6%E6%8A%95%E6%8E%A7%E6%8F%90%E5%91%8A%E9%81%95%E6%B3%95%E5%85%AC%E9%96%8B%E6%94%B6%E8%B3%BC%E8%82%A1%E6%AC%8A-%E7%B1%B2%E8%AB%8B%E6%94%BF%E5%BA%9C%E5%9A%B4%E6%9F%A5%E5%A2%83%E5%A4%96%E9%89%85%E9%A1%8D%E9%87%91%E6%B5%81-044237985.html
- 事件5：台積跌跤誰喊痛 8金控一天帳面蒸發百億
  - 來源：Yahoo 台股；發布時間：2026-11-02T03:48:07Z；台北時間：2026-11-02 11:48
  - 摘要：英特爾財測欠佳上周五一度暴跌30%，台積電（2330）今（2）早也一度大跌60元，盤中一度下探2310元低位寫四個月新低價，剛好八家金控最新公布9月底持有「護國神山」共計19.6萬張，短短一天帳面一度蒸發117億元之多。富邦金（2881）一
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%9A%B4%E8%B7%8C60%E5%85%83%E3%80%8C%E8%8B%A6%E4%B8%BB%E3%80%8D%E5%87%BA%E5%88%97-8%E9%87%91%E6%8E%A7%E4%B8%80%E5%A4%A9%E5%B8%B3%E9%9D%A2%E8%92%B8%E7%99%BC%E7%99%BE%E5%84%84%E5%85%83-034807394.html
- 事件6：友達財報失色買盤仍爆量 南亞強漲也吸睛
  - 來源：Yahoo 台股；發布時間：2026-11-02T04:37:00Z；台北時間：2026-11-02 12:37
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導台股今（2）日開低走低，開盤下跌177.3點至45034.53點，截至中午12點20分暫報45018.95點，下跌192.88點，跌幅0.43%。觀察今...
  - 原文連結：https://tw.stock.yahoo.com/news/q3%E7%94%B1%E7%9B%88%E8%BD%89%E8%99%A7-%E9%9D%A2%E6%9D%BF%E5%A4%A7%E5%BB%A0-%E8%B7%8C%E5%81%9C%E5%BE%8C%E5%8F%8D%E5%BD%88%E7%82%B8%E9%87%8F18%E8%90%AC%E5%BC%B5%E5%B1%85%E5%86%A0-%E5%8D%97%E4%BA%9E%E7%9B%AE%E6%A8%99%E5%83%B9375%E5%85%83%E6%88%90%E4%BA%A4%E9%87%8F%E8%B6%856-8%E8%90%AC%E5%BC%B5-043700504.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Treasury Department announces new Series I bond rate of 5.51% for the next six months
  - 來源：CNBC；發布時間：Fri, 30 Oct 2026 17:15:53 GMT；台北時間：2026-10-31 01:15
  - 摘要：The U.S. Department of the Treasury has announced new Series I bond rates through April 2027.
  - 原文連結：https://www.cnbc.com/2026/10/30/treasury-i-bond-rate-through-april-2027.html
- 事件10：Anthropic's path to the Nasdaq just got a lot bumpier
  - 來源：CNBC；發布時間：Sat, 31 Oct 2026 11:00:01 GMT；台北時間：2026-10-31 19:00
  - 摘要：Concerning projections from hyperscalers this week punished tech stocks and pushed the Nasdaq to its first three-week losing streak since March.
  - 原文連結：https://www.cnbc.com/2026/10/31/anthropic-ipo-ai-spending.html
- 事件11：Top Wall Street analysts are bullish on these 3 stocks for the long haul
  - 來源：CNBC；發布時間：Sun, 01 Nov 2026 12:33:53 GMT；台北時間：2026-11-01 20:33
  - 摘要：Investors looking beyond short-term noise and focusing on long-term returns can track top analysts to pick the right stocks, backed by strong research
  - 原文連結：https://www.cnbc.com/2026/11/01/top-analysts-are-bullish-on-these-3-stocks-for-the-long-haul.html
- 事件12：Trump called out Big Oil profits. Here’s how much their refining earnings have surged since
  - 來源：CNBC；發布時間：Sat, 31 Oct 2026 06:00:02 GMT；台北時間：2026-10-31 14:00
  - 摘要：Trump criticized Big Oil for making “too much money,” but oil majors have since reported surging refining earnings as fuel supplies tightened.
  - 原文連結：https://www.cnbc.com/2026/10/31/trump-big-oil-refining-profits.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-02

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,410 | TAIFEX Proxy |
| 最高價 | 45,597 | TAIFEX Proxy |
| 最低價 | 44,908 | TAIFEX Proxy |
| 收盤價 | 45,301 | TAIFEX Proxy |
| 漲跌點數 | -1,268 | TAIFEX Proxy |
| 漲跌幅 | -2.72 | TAIFEX Proxy |
| 成交量 | 73,987 | TAIFEX Proxy |
| 日盤高點及低點 | 45,597 / 44,908 | TAIFEX Proxy |

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
| 外資多方 OI | 0 | TAIFEX Proxy |
| 外資空方 OI | 0 | TAIFEX Proxy |
| 外資多空淨 OI | +0 | TAIFEX Proxy |
| 投信多方 OI | 0 | TAIFEX Proxy |
| 投信空方 OI | 0 | TAIFEX Proxy |
| 投信多空淨 OI | +0 | TAIFEX Proxy |
| 自營商多方 OI | 0 | TAIFEX Proxy |
| 自營商空方 OI | 0 | TAIFEX Proxy |
| 自營商多空淨 OI | +0 | TAIFEX Proxy |
| 三大法人合計多方 OI | 0 | TAIFEX Proxy |
| 三大法人合計空方 OI | 0 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +0 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +92,241 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -89,211 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,736 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 93,812 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,190 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,622 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-28→2026-10-30) | -3,281 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：2026-10-30 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 57,787 | TAIFEX Proxy |
| 外資日盤空單交易量 | 54,986 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,801 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 26,142 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 24,777 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,365 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,436 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -72 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -72 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -457 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +246 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -703 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,272 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,611 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +203.5 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +144.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 45,301 | TAIFEX Proxy |
| 加權指數價格 | 44,920.14 | twse-proxy |
| 台指期與加權指數價差 | +380.86 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.85 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +380.86 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -868 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 45,301 | 44,433 | +868 | TAIFEX Proxy |
| 成交量 | 73,987 | 44,305 | +29,682 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,294（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 57,787 | 54,986 | +2,801 | 26,142 | 24,777 | +1,365 | +1,436 | 0 | 0 | +0 | +92,241 | TAIFEX Proxy |
| 投信 | 121 | 193 | -72 | 0 | 0 | +0 | -72 | 0 | 0 | +0 | -89,211 | TAIFEX Proxy |
| 自營商 | 4,663 | 5,120 | -457 | 887 | 641 | +246 | -703 | 0 | 0 | +0 | -1,736 | TAIFEX Proxy |
| 三大法人合計 | 62,571 | 60,299 | +2,272 | 27,029 | 25,418 | +1,611 | +661 | 0 | 0 | +0 | +1,294 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 93,812 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,190 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,622 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-28→2026-10-30) | -3,281 | TAIFEX Proxy snapshots (2026-10-29) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 37.45% | TAIFEX Proxy |
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
| 交易日期 | 2026-11-02 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-02 14:35:26 | 本機 |
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

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.03 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.77 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-29→2026-10-30) | 9.95 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-29→2026-10-30) | -1.87 | TAIFEX Proxy |
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
| 外資 Call夜買 | 21,396 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,563 | TAIFEX Proxy |
| 外資 Call夜淨 | -167 | TAIFEX Proxy |
| 外資 Put夜買 | 20,402 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,475 | TAIFEX Proxy |
| 外資 Put夜淨 | -73 | TAIFEX Proxy |
| 外資 日盤淨總量 | -167 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -133 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -60 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 41,575 | TAIFEX Proxy |
| 自營商 Call日賣 | 35,503 | TAIFEX Proxy |
| 自營商 Call日淨 | +6,072 | TAIFEX Proxy |
| 自營商 Put日買 | 36,775 | TAIFEX Proxy |
| 自營商 Put日賣 | 38,102 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,327 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,028 | TAIFEX Proxy |
| 自營商 Call夜賣 | 11,963 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,935 | TAIFEX Proxy |
| 自營商 Put夜買 | 11,254 | TAIFEX Proxy |
| 自營商 Put夜賣 | 11,798 | TAIFEX Proxy |
| 自營商 Put夜淨 | -544 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +7,399 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +8,007 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -783 | TAIFEX Proxy |

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
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | unavailable | 端點未提供 |
| Gross GEX（標的變動 1%） | unavailable | 端點未提供 |
| 模型品質 | unavailable | unavailable |
| 履約價資料筆數 | unavailable | 資料日期：unavailable |
| 正 Net GEX 最大履約價 | unavailable | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | unavailable | 依 Net GEX 排序 |
- GEX 明細 unavailable；不以 Wall／Flip proxy 代替。

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 44,400 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 91,251 | 91,418 | -167 | 41,871 | 41,965 | -94 | -73 | TAIFEX Proxy |
| 投信 | 0 | 6,362 | -6,362 | 0 | 0 | +0 | -6,362 | TAIFEX Proxy |
| 自營商 | 79,677 | 72,278 | +7,399 | 21,826 | 23,217 | -1,391 | +8,790 | TAIFEX Proxy |
| 三大法人合計 | 170,928 | 170,058 | +870 | 63,697 | 65,182 | -1,485 | +2,355 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.36 | 11.17 | +0.18 | 4.88 | 4.94 | -0.06 | +0.24 | TAIFEX Proxy |
| 投信 | 0.00 | 3.01 | -3.01 | 0.00 | 0.00 | +0 | -3.01 | TAIFEX Proxy |
| 自營商 | 10.22 | 8.40 | +1.82 | 2.81 | 3.35 | -0.54 | +2.35 | TAIFEX Proxy |
| 三大法人合計 | 21.57 | 22.58 | -1.01 | 7.70 | 8.29 | -0.60 | -0.41 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 9,881 | TAIFEX Proxy |
| 買權空方 OI | 12,037 | TAIFEX Proxy |
| 買權多空淨 OI | -2,156 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-28→2026-10-30) | -1,024 | TAIFEX Proxy snapshots (2026-10-29) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,631 | TAIFEX Proxy |
| 賣權空方 OI | 10,961 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,330 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-28→2026-10-30) | -278 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：買權 2026-10-30／賣權 2026-10-30 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -3,281 | 2026-10-28→2026-10-30 | TAIFEX Proxy snapshots (2026-10-29) |
| 買權前十大 | -1,024 | 2026-10-28→2026-10-30 | TAIFEX Proxy snapshots (2026-10-29) |
| 賣權前十大 | -278 | 2026-10-28→2026-10-30 | TAIFEX Proxy snapshots (2026-10-29) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-02；資料時間：2026-11-02 14:35:26；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (18)：taiex.open, taiex.high, taiex.low, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, margin.ratio, sbl.sale_bal, sbl.sale_chg, turnover.otc, futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-10-30 非今日 2026-11-02，視為無新節次，不採用
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall 無資料（原始端點與 Proxy 備援皆未取得），標 unavailable
- 註記：Gamma Flip 無資料（原始端點與 Proxy 備援皆未取得），標 unavailable
- 註記：逐履約價 GEX／Net GEX／Gross GEX 未取得或資料不完整，標 unavailable（不以 Wall/Flip proxy 代替）
- 註記：跨到期換月（舊202610F5→新202611W1），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用）`
- sbl_bal：`TWSE TWT96U + TWSE TWT96U OTC`
- sbl_sale_bal：`端點未提供`
- sbl_sale_chg：`端點未提供`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151030, T0=1151102)
- 註記：三大法人回傳日期 20261030 (T0 20261102)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：上市融資維持率 unavailable；自建計算：ValueError: TWSE margin date mismatch: missing != 20261102；Blave：exact T0 2026-11-02 not found。不影響其他融資融券欄位、DATA_REPORT、JSON 與 Dashboard 產出。
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,124.7 | +0 | +2,801 | +1,365 | -167 | -94 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +236.2 | +0 | -72 | +0 | -6,362 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -513.7 | +0 | -457 | +246 | +7,399 | -1,391 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
