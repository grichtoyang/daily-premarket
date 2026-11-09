# DATA_REPORT_20261106

- 報告日期：`2026-11-09`
- T0 交易日期：`2026-11-06`
- 資料產出時間：`2026-11-09 11:37:58`
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
| 加權指數 | 39,701.64 | 點 | twse-proxy |
| 開盤 | 38,915.76 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 40,435.83 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 37,837.05 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 39,701.64 | 點 | twse-proxy |
| 漲跌點數 | -1,873.08 | 點 | twse-proxy |
| 漲跌幅 | -4.51 | % | twse-proxy |
| 成交金額 | 13,210.7 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 105 | twse-proxy |
| 下跌家數 | 952 | twse-proxy |
| 平盤家數 | 27 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 24 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 104 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 733 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 38 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 14 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 29 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -911.9 | 億元 | twse-proxy /institutional |
| 投信 | +266.9 | 億元 | twse-proxy /institutional |
| 自營商 | -494.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,139.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,040.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -564.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 272,748 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -40,371 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 151.90 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,475,355 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 29,982 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -6,086 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 13,210.7 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,643.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,854.6 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,376.86 | 23.13 | +0.31 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,579.43 | 264.43 | +1.09 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,989.99 | 360.18 | +1.35 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,285.73 | -237.33 | -0.46 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,390.25 | 379.11 | +4.21 | Yahoo Finance Chart API |
| VIX | ^VIX | 25.64 | -2.54 | -9.01 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,411.34 | 1,976.57 | +3.44 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,129.64 | 69.95 | +1.38 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,529.87 | 48.01 | +0.20 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,668.96 | 19.78 | +0.54 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,230.19 | 54.41 | +0.49 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,447.75 | 45.75 | +0.62 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,255.00 | 169.75 | +0.63 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,763.00 | 378.00 | +0.74 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,783.60 | 23.10 | +0.84 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.51 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.86 | 0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.26 | 0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.76 | -0.35 | -1.05 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.18 | -0.12 | -0.12 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.30 | 0.80 | +0.51 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,356.22 | -0.12 | -0.01 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 375.44 | 22.34 | +6.33 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.85 | 0.47 | +3.51 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 31.63 | 1.91 | +6.43 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 91.18 | 0.35 | +0.39 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,125.30 | 50.40 | +1.24 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 74,909.93 | -837.65 | -1.11 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：萬張買單排隊搶國巨  分析師提醒：籌碼凌亂
  - 來源：Yahoo 台股；發布時間：2026-11-09T02:43:48Z；台北時間：2026-11-09 10:43
  - 摘要：被動元件龍頭廠國巨（2327）今日終於迎來紅燈，且開盤約15分鐘就強勢鎖上漲停板，股價重返400元大關，最高觸及411元漲停價，至截稿為止還有1.3萬張買單排隊等買，熱度可見一斑。不過，分析師也建議，國巨散戶多、籌碼相對凌亂，一旦反彈漲勢趨
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%90%AC%E5%BC%B5%E8%B2%B7%E5%96%AE%E6%8E%92%E9%9A%8A%E6%90%B6%EF%BC%81%E5%9C%8B%E5%B7%A8%E9%8E%96%E6%BC%B2%E5%81%9C%E9%87%8D%E8%BF%94400%E5%85%83-%E5%88%86%E6%9E%90%E5%B8%AB%E5%8D%BB%E6%9B%9D%E4%B8%80%E9%97%9C%E9%8D%B5%EF%BC%9A%E5%8F%8D%E5%BD%88%E5%BE%8C%E9%81%A9%E5%BA%A6%E6%8F%9B%E8%82%A1-024348364.html
- 事件3：大盤一度攻42K！13千金奔漲停
  - 來源：Yahoo 台股；發布時間：2026-11-09T02:50:00Z；台北時間：2026-11-09 10:50
  - 摘要：[FTNN新聞網]記者吳峻光／綜合報導國安基金5千億銀彈救場，台股截至今（9）上午10時25分，暴漲超過2500點，加權指數最高衝上42244.89點，成功帶動13檔千金股...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%90%83%E7%B3%96%E6%BC%BF2500%E9%BB%9E%E5%A4%A7%E7%88%86%E7%99%BC-%E8%81%AF%E7%99%BC%E7%A7%91-%E5%8F%B0%E9%81%94%E9%9B%BB%E7%99%BB%E9%A0%82-13%E6%AA%94%E5%8D%83%E9%87%91%E6%BC%B2%E5%81%9C-0050-025000089.html
- 事件4：近3萬人上周五勇敢買台達電 今迎漲停每張賺10萬
  - 來源：Yahoo 台股；發布時間：2026-11-09T01:34:53Z；台北時間：2026-11-09 09:34
  - 摘要：台達電終於醒了！電源供應器大廠台達電（2308）今日迎來久違的紅燈，盤中一度衝上漲停價1160元，迎來腰斬後最大的一次絕地反彈。根據集保中心統計，上周五台達電最新股東人數高達71萬2,573人，較前一周大增2萬9,465人，直接寫下歷史新高
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E9%81%94%E9%9B%BB71%E8%90%AC%E8%82%A1%E6%9D%B1%E5%97%A8%EF%BC%81%E8%BF%913%E8%90%AC%E4%BA%BA%E4%B8%8A%E5%91%A8%E5%8B%87%E6%95%A2%E6%8A%84%E5%BA%95-%E4%BB%8A%E6%BC%B2%E5%81%9C%E6%AF%8F%E5%BC%B5%E5%A4%A7%E8%B3%BA105%E8%90%AC%E5%85%83-013453435.html
- 事件5：00940配出新高 股東卻從近百萬減到30萬
  - 來源：Yahoo 台股；發布時間：2026-11-09T02:10:00Z；台北時間：2026-11-09 10:10
  - 摘要：[FTNN新聞網]記者薛明峻／台北報導採月月配、受益人數逾30.6萬人的高股息ETF元大台灣價值高息（00940），上周五（6日）公告最新配息每受益權單位實際配發金額...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%93%81%E8%8F%AF%E7%A2%A9-%E8%81%AF%E8%A9%A0-%E7%91%9E%E6%98%B1-00940%E6%9C%88%E9%85%8D0-06%E5%85%83%E5%89%B5%E6%96%B0%E9%AB%98%E4%BB%8A%E6%9C%80%E5%BE%8C%E8%B2%B7%E9%80%B2%E6%97%A5-021000616.html
- 事件6：4高息ETF將換股 3檔個股有戲
  - 來源：Yahoo 台股；發布時間：2026-11-08T22:24:36Z；台北時間：2026-11-09 06:24
  - 摘要：摩根大通證券（小摩）指出，群益台灣精選高息（00919）、復華台灣科技優息、元大台灣高息低波、元大台灣價值高息等四檔高股息ETF將在年底前調整成分股。調整後，創見、亞泥及緯穎等三檔個股可望最受惠，致伸則可能面臨最大的資金淨流出。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9B%9B%E6%AA%94%E9%AB%98%E6%81%AFetf%E5%B0%87%E6%8F%9B%E8%82%A1-%E4%B8%89%E6%AA%94%E5%80%8B%E8%82%A1%E5%8F%AF%E6%9C%9B%E5%8F%97%E6%83%A0-222436185.html
- 事件7：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件8：China wholesale inflation hits highest in more than four years as consumer measure slows
  - 來源：CNBC；發布時間：Mon, 09 Nov 2026 02:50:22 GMT；台北時間：2026-11-09 10:50
  - 摘要：The PPI for October came in at 5.7%, compared to the 5.3% expected by economists polled by Reuters.
  - 原文連結：https://www.cnbc.com/2026/11/09/china-wholesale-inflation-rises-consumer.html
- 事件9：How Democrats will try to end Trump's tariffs
  - 來源：CNBC；發布時間：Sun, 08 Nov 2026 15:36:39 GMT；台北時間：2026-11-08 23:36
  - 摘要：Rep. Hakeem Jeffries, D-N.Y., who is likely the next House speaker, has made clear that ending President Trump's tariffs is one of Democrats' top prio
  - 原文連結：https://www.cnbc.com/2026/11/08/trump-tariffs-democrats-congress-canada.html
- 事件10：Top Wall Street analysts like these 3 dividend stocks for consistent income
  - 來源：CNBC；發布時間：Sun, 08 Nov 2026 11:47:24 GMT；台北時間：2026-11-08 19:47
  - 摘要：Three dividend-paying stocks that are highlighted by Wall Street’s top pros, as tracked by TipRanks.
  - 原文連結：https://www.cnbc.com/2026/11/08/top-analysts-like-these-3-dividend-stocks-for-consistent-income.html
- 事件11：Why the prognosis for healthcare stocks is uncertain ahead of Congress’ new makeup
  - 來源：CNBC；發布時間：Sat, 07 Nov 2026 16:02:33 GMT；台北時間：2026-11-08 00:02
  - 摘要：Healthcare stocks may struggle to find momentum as the Democrats get ready to take over Congress.
  - 原文連結：https://www.cnbc.com/2026/11/07/healthcare-stocks-may-face-trouble-due-to-midterm-results.html
- 事件12：Berkshire shares surge as Wall Street swoons amid AI fears
  - 來源：CNBC；發布時間：Sat, 07 Nov 2026 14:06:20 GMT；台北時間：2026-11-07 22:06
  - 摘要：Berkshire Hathaway shares roared past the S&P 500 index this week and are outperforming the benchmark for the year-to-date.
  - 原文連結：https://www.cnbc.com/2026/11/07/berkshire-shares-surge-as-wall-street-swoons-amid-ai-fears.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-06

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 38,888 | TAIFEX Proxy |
| 最高價 | 40,690 | TAIFEX Proxy |
| 最低價 | 37,694 | TAIFEX Proxy |
| 收盤價 | 39,786 | TAIFEX Proxy |
| 漲跌點數 | -2,096 | TAIFEX Proxy |
| 漲跌幅 | -5.00 | TAIFEX Proxy |
| 成交量 | 143,277 | TAIFEX Proxy |
| 日盤高點及低點 | 40,690 / 37,694 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 39,742 | TAIFEX Proxy |
| 最高價 | 40,845 | TAIFEX Proxy |
| 最低價 | 39,129 | TAIFEX Proxy |
| 收盤價 | 40,298 | TAIFEX Proxy |
| 漲跌點數 | +646 | TAIFEX Proxy |
| 漲跌幅 | +1.63 | TAIFEX Proxy |
| 成交量 | 69,882 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,845 / 39,129 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 15,873 | TAIFEX Proxy |
| 外資空方 OI | 115,803 | TAIFEX Proxy |
| 外資多空淨 OI | -99,930 | TAIFEX Proxy |
| 投信多方 OI | 94,158 | TAIFEX Proxy |
| 投信空方 OI | 3,721 | TAIFEX Proxy |
| 投信多空淨 OI | +90,437 | TAIFEX Proxy |
| 自營商多方 OI | 6,022 | TAIFEX Proxy |
| 自營商空方 OI | 4,342 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,680 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,053 | TAIFEX Proxy |
| 三大法人合計空方 OI | 123,866 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,813 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -4,279 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +154 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -650 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 102,490 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,600 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,890 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-04→2026-11-06) | -4,372 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：2026-11-06 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 140,566 | TAIFEX Proxy |
| 外資日盤空單交易量 | 144,876 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,310 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 41,133 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 42,246 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,113 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,197 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +154 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +154 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -875 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -406 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -469 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -5,031 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,519 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -390.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -123.6 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 39,786 | TAIFEX Proxy |
| 加權指數價格 | 39,701.64 | twse-proxy |
| 台指期與加權指數價差 | +84.36 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.21 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +84.36 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +512 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,786 | 40,298 | -512 | TAIFEX Proxy |
| 成交量 | 143,277 | 69,882 | +73,395 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-4,775（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 140,566 | 144,876 | -4,310 | 41,133 | 42,246 | -1,113 | -3,197 | 15,873 | 115,803 | -99,930 | -4,279 | TAIFEX Proxy |
| 投信 | 1,275 | 1,121 | +154 | 0 | 0 | +0 | +154 | 94,158 | 3,721 | +90,437 | +154 | TAIFEX Proxy |
| 自營商 | 18,917 | 19,792 | -875 | 1,991 | 2,397 | -406 | -469 | 6,022 | 4,342 | +1,680 | -650 | TAIFEX Proxy |
| 三大法人合計 | 160,758 | 165,789 | -5,031 | 43,124 | 44,643 | -1,519 | -3,512 | 116,053 | 123,866 | -7,813 | -4,775 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 102,490 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,600 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,890 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-04→2026-11-06) | -4,372 | TAIFEX Proxy snapshots (2026-11-05) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 32.78% | TAIFEX Proxy |
| 夜盤漲跌點數 | +646 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,113 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-06 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-09 11:37:58 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 502,306 | TAIFEX Proxy |
| Call 總未平倉量 OI | 138,851 | TAIFEX Proxy |
| Call OI 增減 (2026-11-05→2026-11-06) | +48,691 | TAIFEX Proxy snapshots (2026-11-05) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 393,781 | TAIFEX Proxy |
| Put 總未平倉量 OI | 82,744 | TAIFEX Proxy |
| Put OI 增減 (2026-11-05→2026-11-06) | +49,315 | TAIFEX Proxy snapshots (2026-11-05) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.28 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.68 | TAIFEX Proxy |
| Put／Call Ratio | 0.60 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-05→2026-11-06) | 3.22 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-05→2026-11-06) | -4.36 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 160,272 | TAIFEX Proxy |
| 外資 Call日賣 | 161,721 | TAIFEX Proxy |
| 外資 Call日淨 | -1,449 | TAIFEX Proxy |
| 外資 Put日買 | 129,399 | TAIFEX Proxy |
| 外資 Put日賣 | 132,239 | TAIFEX Proxy |
| 外資 Put日淨 | -2,840 | TAIFEX Proxy |
| 外資 Call夜買 | 11,803 | TAIFEX Proxy |
| 外資 Call夜賣 | 11,695 | TAIFEX Proxy |
| 外資 Call夜淨 | +108 | TAIFEX Proxy |
| 外資 Put夜買 | 9,946 | TAIFEX Proxy |
| 外資 Put夜賣 | 9,941 | TAIFEX Proxy |
| 外資 Put夜淨 | +5 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,391 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -1,557 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -2,845 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 113,529 | TAIFEX Proxy |
| 自營商 Call日賣 | 135,263 | TAIFEX Proxy |
| 自營商 Call日淨 | -21,734 | TAIFEX Proxy |
| 自營商 Put日買 | 95,740 | TAIFEX Proxy |
| 自營商 Put日賣 | 105,967 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,227 | TAIFEX Proxy |
| 自營商 Call夜買 | 14,346 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,375 | TAIFEX Proxy |
| 自營商 Call夜淨 | +1,971 | TAIFEX Proxy |
| 自營商 Put夜買 | 10,572 | TAIFEX Proxy |
| 自營商 Put夜賣 | 11,338 | TAIFEX Proxy |
| 自營商 Put夜淨 | -766 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,507 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -23,705 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -9,461 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 40,000 | 4,752 | TAIFEX Proxy |
| Call OI 第2大履約價 | 46,500 | 4,631 | TAIFEX Proxy |
| Call OI 第3大履約價 | 43,000 | 4,055 | TAIFEX Proxy |
| Call OI 最大履約價 | 40,000 | 4,752 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 40,000 | 4,752 | 3.42% | TAIFEX Proxy |
| C2 | 46,500 | 4,631 | 3.34% | TAIFEX Proxy |
| C3 | 43,000 | 4,055 | 2.92% | TAIFEX Proxy |
| C4 | 46,000 | 3,846 | 2.77% | TAIFEX Proxy |
| C5 | 44,000 | 3,765 | 2.71% | TAIFEX Proxy |
| C6 | 40,100 | 3,607 | 2.6% | TAIFEX Proxy |
| C7 | 42,000 | 3,607 | 2.6% | TAIFEX Proxy |
| C8 | 41,000 | 3,497 | 2.52% | TAIFEX Proxy |
| C9 | 45,000 | 3,376 | 2.43% | TAIFEX Proxy |
| C10 | 44,500 | 3,325 | 2.39% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 37,400 | 10,404 | TAIFEX Proxy |
| Put OI 第2大履約價 | 37,500 | 7,588 | TAIFEX Proxy |
| Put OI 第3大履約價 | 39,000 | 3,371 | TAIFEX Proxy |
| Put OI 最大履約價 | 37,400 | 10,404 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 37,400 | 10,404 | 12.57% | TAIFEX Proxy |
| P2 | 37,500 | 7,588 | 9.17% | TAIFEX Proxy |
| P3 | 39,000 | 3,371 | 4.07% | TAIFEX Proxy |
| P4 | 39,700 | 3,253 | 3.93% | TAIFEX Proxy |
| P5 | 37,600 | 2,951 | 3.57% | TAIFEX Proxy |
| P6 | 39,800 | 2,689 | 3.25% | TAIFEX Proxy |
| P7 | 39,600 | 2,577 | 3.11% | TAIFEX Proxy |
| P8 | 38,600 | 2,478 | 2.99% | TAIFEX Proxy |
| P9 | 38,000 | 2,096 | 2.53% | TAIFEX Proxy |
| P10 | 39,500 | 1,969 | 2.38% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 40,000 (+4,752) | TAIFEX Proxy snapshots (2026-11-05) |
| Call OI 減少最多的履約價 | 46,500 (-1,958) | TAIFEX Proxy snapshots (2026-11-05) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 37,400 (+10,404) | TAIFEX Proxy snapshots (2026-11-05) |
| Put OI 減少最多的履約價 | 40,500 (-429) | TAIFEX Proxy snapshots (2026-11-05) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -6,500 | TAIFEX Proxy snapshots (2026-11-05) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 37,400 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -2,600 | TAIFEX Proxy snapshots (2026-11-05) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 38,900.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,300 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -1,650 | TAIFEX Proxy snapshots (2026-11-05) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 292,511 | 291,120 | +1,391 | 21,744 | 21,641 | +103 | +1,288 | TAIFEX Proxy |
| 投信 | 224 | 15,330 | -15,106 | 0 | 0 | +0 | -15,106 | TAIFEX Proxy |
| 自營商 | 219,496 | 231,003 | -11,507 | 25,684 | 22,947 | +2,737 | -14,244 | TAIFEX Proxy |
| 三大法人合計 | 512,231 | 537,453 | -25,222 | 47,428 | 44,588 | +2,840 | -28,062 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 32.09 | 31.02 | +1.06 | 20.78 | 20.89 | -0.11 | +1.18 | TAIFEX Proxy |
| 投信 | 0.14 | 11.00 | -10.86 | 0.00 | 0.00 | +0 | -10.86 | TAIFEX Proxy |
| 自營商 | 45.40 | 37.81 | +7.59 | 7.22 | 6.76 | +0.46 | +7.13 | TAIFEX Proxy |
| 三大法人合計 | 77.63 | 79.84 | -2.21 | 28.00 | 27.66 | +0.35 | -2.56 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,097 | TAIFEX Proxy |
| 買權空方 OI | 19,390 | TAIFEX Proxy |
| 買權多空淨 OI | -5,293 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-04→2026-11-06) | -1,167 | TAIFEX Proxy snapshots (2026-11-05) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,486 | TAIFEX Proxy |
| 賣權空方 OI | 13,491 | TAIFEX Proxy |
| 賣權多空淨 OI | -3,005 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-04→2026-11-06) | -286 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：買權 2026-11-06／賣權 2026-11-06 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -4,372 | 2026-11-04→2026-11-06 | TAIFEX Proxy snapshots (2026-11-05) |
| 買權前十大 | -1,167 | 2026-11-04→2026-11-06 | TAIFEX Proxy snapshots (2026-11-05) |
| 賣權前十大 | -286 | 2026-11-04→2026-11-06 | TAIFEX Proxy snapshots (2026-11-05) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-06；資料時間：2026-11-09 11:37:58；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：1 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：69 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (2)：futures.gamma_wall, futures.gamma_flip
- 註記：futures-price-after-hours 日期 2026-11-06 非今日 2026-11-09，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
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
| 外資 | -911.9 | -99,930 | -4,310 | -1,113 | +1,391 | +103 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +266.9 | +90,437 | +154 | +0 | -15,106 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -494.8 | +1,680 | -875 | -406 | -11,507 | +2,737 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
