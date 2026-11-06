# DATA_REPORT_20261106

- 報告日期：`2026-11-07`
- T0 交易日期：`2026-11-06`
- 資料產出時間：`2026-11-07 01:47:16`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`evening`

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
| 融資維持率 | 155.70 | % | 前值遞補 (DATA 2026-11-05；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,885,386 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,390.16 | 36.43 | +0.50 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,574.05 | 259.05 | +1.07 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,966.05 | 336.24 | +1.26 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,454.88 | -68.18 | -0.13 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,272.96 | 261.82 | +2.91 | Yahoo Finance Chart API |
| VIX | ^VIX | 24.53 | -3.65 | -12.95 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,077.90 | -1,110.73 | -1.79 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,383.80 | -300.00 | -5.28 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,796.98 | 877.48 | +3.67 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,689.91 | 3.74 | +0.10 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,471.09 | 135.40 | +1.19 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,413.25 | 30.25 | +0.41 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,081.75 | 329.75 | +1.23 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,490.00 | -125.00 | -0.24 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,754.90 | 19.50 | +0.71 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.46 | -0.12 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.85 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.24 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.77 | -0.06 | -0.17 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.16 | 0.61 | +0.60 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.18 | -0.18 | -0.11 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,362.39 | 22.32 | +1.67 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 371.90 | 18.80 | +5.33 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.71 | 0.33 | +2.47 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 31.16 | 1.44 | +4.85 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 90.12 | -0.40 | -0.44 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,067.10 | -46.40 | -1.13 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 75,536.24 | -405.88 | -0.53 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：台股「黑五」崩最大盤中跌點 雙正2各自爆百萬張
  - 來源：Yahoo 台股；發布時間：2026-11-06T09:12:16Z；台北時間：2026-11-06 17:12
  - 摘要：黑色星期五！台股重挫1873點摔回3字頭，收盤失守4萬！今(6)日加權指數早盤一度急殺3737.67點至37,837.05點，創史上最大盤中跌點，隨後低接買盤進場，指數自低點拉升近2600點、一度重返4萬，終場仍下跌1873.08點、跌幅4
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E3%80%8C%E9%BB%91%E4%BA%94%E3%80%8D%E7%9B%A4%E4%B8%AD%E8%A1%80%E6%B4%973737%E9%BB%9E%E5%8F%B2%E4%B8%8A%E6%9C%80%E6%85%98%EF%BC%81%E3%80%8C%E9%9B%99%E6%AD%A32%E3%80%8D%E6%94%9C%E6%89%8B%E7%88%86%E9%87%8F%E7%99%BE%E8%90%AC%E5%BC%B5%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091216012.html
- 事件3：5千億銀彈要進場了 國安基金拍板第10度護盤
  - 來源：Yahoo 台股；發布時間：2026-11-06T09:53:21Z；台北時間：2026-11-06 17:53
  - 摘要：台股今（6）日盤中崩跌3737.67點，創下史上盤中最大跌點，終場下跌1873.08點、收在39,701.64，寫史上第四大收盤跌點。面對投資信心重挫，國安基金今日下午召開第131次臨時委員會議，經討論及共識決議，授權執行秘書視情況動用資金
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B2%E4%B8%8A%E7%AC%AC%E5%8D%81%E6%AC%A1%EF%BC%81%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E5%AE%A3%E5%B8%83%E9%80%B2%E5%A0%B4%E8%AD%B7%E7%9B%A4-5%E5%8D%83%E5%84%84%E5%85%83%E9%8A%80%E5%BD%88%E4%B8%8A%E8%86%9B-101441531.html
- 事件4：0050漲到116.6元沒跑！一路下跌他後悔 網曝「最佳賣點」
  - 來源：Yahoo 台股；發布時間：2026-11-06T10:32:00Z；台北時間：2026-11-06 18:32
  - 摘要：許多人買進元大台灣50（0050），都打算長期投資存股，但有網友表示，此前0050一度漲破116元，當時抱著沒賣，如今帳上獲利縮水難免後悔，問：存到何時才能賣？
  - 原文連結：https://tw.stock.yahoo.com/news/0050%E6%BC%B2%E5%88%B0116-6%E5%85%83%E6%B2%92%E8%B7%91-%E8%B7%AF%E4%B8%8B%E8%B7%8C%E4%BB%96%E5%BE%8C%E6%82%94-%E7%B6%B2%E6%9B%9D-%E6%9C%80%E4%BD%B3%E8%B3%A3%E9%BB%9E-103200318.html
- 事件5：台股史詩級大崩盤！黃鐙輝「獲利全蒸發」 搶3小孩紅包曝驚人操作
  - 來源：Yahoo 台股；發布時間：2026-11-06T10:23:11Z；台北時間：2026-11-06 18:23
  - 摘要：台股今（6）爆發史詩級股災！受到美股科技股全面重挫衝擊，台股開盤即遭遇猛烈賣壓，加權指數一度暴跌逾3700點，最低下探至37837點，直接摜破4萬點整數關卡，連年線也告失守，跌幅一度逼近9%，市場哀鴻遍野。在演藝圈對投資頗有心得的黃鐙輝今出
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%8F%B2%E8%A9%A9%E7%B4%9A%E5%A4%A7%E5%B4%A9%E7%9B%A4-%E9%BB%83%E9%90%99%E8%BC%9D-%E7%8D%B2%E5%88%A9%E5%85%A8%E8%92%B8%E7%99%BC-%E6%90%B63%E5%B0%8F%E5%AD%A9%E7%B4%85%E5%8C%85%E6%9B%9D%E9%A9%9A%E4%BA%BA%E6%93%8D%E4%BD%9C-102311967.html
- 事件6：封測綠油油！「這檔」累跌34.8%領京元電、頎邦跌停　訊芯、聯鈞、穎崴都掉9%
  - 來源：Yahoo 台股；發布時間：2026-11-06T10:05:00Z；台北時間：2026-11-06 18:05
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導經輝達（NVIDIA）、英特爾（Intel）、美光（Micron）、超微（AMD）等美股科技巨頭同步慘跌影響，台股大盤今（6）日收跌，加...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%B0%81%E6%B8%AC%E7%B6%A0%E6%B2%B9%E6%B2%B9-%E9%80%99%E6%AA%94-%E7%B4%AF%E8%B7%8C34-8-%E9%A0%98%E4%BA%AC%E5%85%83%E9%9B%BB-100500077.html
- 事件7：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件8：U.S. economy added 165,000 jobs in October, way more than expected; unemployment rate slips to 4.1%
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 16:06:59 GMT；台北時間：2026-11-07 00:06
  - 摘要：Nonfarm payrolls were expected to increase by 59,000 in October as the unemployment rate was expected to hold steady at 4.2%.
  - 原文連結：https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html
- 事件9：The AI ‘credit card’ is getting costlier as CoreWeave bond yield tops 16%
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 17:09:53 GMT；台北時間：2026-11-07 01:09
  - 摘要：Coreweave's steep yields reflect stress in the AI debt markets as investors worry about a data center slowdown. What comes next.
  - 原文連結：https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html
- 事件10：Wall Street's fear gauge may be flashing a buy sign
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 16:29:01 GMT；台北時間：2026-11-07 00:29
  - 摘要：History shows that similar spikes in the VIX have been good entry points for stocks
  - 原文連結：https://www.cnbc.com/2026/11/06/wall-streets-fear-gauge-may-be-flashing-a-buy-sign.html
- 事件11：Nasdaq drops into correction territory — here’s what typically happens next
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 13:47:43 GMT；台北時間：2026-11-06 21:47
  - 摘要：Nasdaq’s slide into correction territory puts its history of recoveries in focus. Here's what history shows.
  - 原文連結：https://www.cnbc.com/2026/11/05/nasdaq-drops-into-correction-territory-heres-what-typically-happens-next.html
- 事件12：Watch the Annual Meeting: Cramer on the fate of the AI buildout and stocks to buy now
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 17:46:02 GMT；台北時間：2026-11-07 01:46
  - 摘要：At the Investing Club's 4th annual meeting, Cramer also reveals his outlook for 2027 and answers questions from the live audience and members at home.
  - 原文連結：https://www.cnbc.com/investingclub/2026/11/06/watch-jim-cramer-live.html


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
| 前十大交易人多方 OI | 100,370 | TAIFEX Proxy |
| 前十大交易人空方 OI | 86,653 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,717 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-04→2026-11-05) | +455 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：2026-11-05 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 140,566 | TAIFEX Proxy |
| 外資日盤空單交易量 | 144,876 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,310 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +154 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -875 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -5,031 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -390.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 39,786 | TAIFEX Proxy |
| 加權指數價格 | 39,701.64 | twse-proxy |
| 台指期與加權指數價差 | +84.36 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.21 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +84.36 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,786 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 143,277 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：-4,775（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 140,566 | 144,876 | -4,310 | unavailable | unavailable | unavailable | unavailable | 15,873 | 115,803 | -99,930 | -4,279 | TAIFEX Proxy |
| 投信 | 1,275 | 1,121 | +154 | unavailable | unavailable | unavailable | unavailable | 94,158 | 3,721 | +90,437 | +154 | TAIFEX Proxy |
| 自營商 | 18,917 | 19,792 | -875 | unavailable | unavailable | unavailable | unavailable | 6,022 | 4,342 | +1,680 | -650 | TAIFEX Proxy |
| 三大法人合計 | 160,758 | 165,789 | -5,031 | unavailable | unavailable | unavailable | unavailable | 116,053 | 123,866 | -7,813 | -4,775 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,370 | TAIFEX Proxy |
| 前十大交易人空方 OI | 86,653 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,717 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-04→2026-11-05) | +455 | TAIFEX Proxy snapshots (2026-11-05) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | unavailable | TAIFEX Proxy |
| 夜盤漲跌點數 | unavailable | TAIFEX Proxy+twse-proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 劇本分類 | unavailable | 規則對應 |
| 劇本條件 | unavailable | 規則對應 |
| 劇本特徵 | unavailable | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-06 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-07 01:47:16 | 本機 |
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
| Call／Put 比例變化 (量比 2026-11-04→2026-11-05) | -12.37 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-04→2026-11-05) | -5.28 | TAIFEX Proxy |
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
| 外資 Call夜買 | 48,207 | TAIFEX Proxy |
| 外資 Call夜賣 | 48,365 | TAIFEX Proxy |
| 外資 Call夜淨 | -158 | TAIFEX Proxy |
| 外資 Put夜買 | 39,168 | TAIFEX Proxy |
| 外資 Put夜賣 | 39,090 | TAIFEX Proxy |
| 外資 Put夜淨 | +78 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,391 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -1,291 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -2,918 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 113,529 | TAIFEX Proxy |
| 自營商 Call日賣 | 135,263 | TAIFEX Proxy |
| 自營商 Call日淨 | -21,734 | TAIFEX Proxy |
| 自營商 Put日買 | 95,740 | TAIFEX Proxy |
| 自營商 Put日賣 | 105,967 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,227 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,180 | TAIFEX Proxy |
| 自營商 Call夜賣 | 36,118 | TAIFEX Proxy |
| 自營商 Call夜淨 | -10,938 | TAIFEX Proxy |
| 自營商 Put夜買 | 30,288 | TAIFEX Proxy |
| 自營商 Put夜賣 | 26,194 | TAIFEX Proxy |
| 自營商 Put夜淨 | +4,094 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,507 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -10,796 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -14,321 | TAIFEX Proxy |

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
| Gamma Wall 價位 | 38,900.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,300 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -1,650 | TAIFEX Proxy snapshots (2026-11-05) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 292,511 | 291,120 | +1,391 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 224 | 15,330 | -15,106 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 219,496 | 231,003 | -11,507 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 512,231 | 537,453 | -25,222 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 32.09 | 31.02 | +1.06 | 10.21 | 10.14 | +0.07 | +1.00 | TAIFEX Proxy |
| 投信 | 0.14 | 11.00 | -10.86 | 0.00 | 0.00 | +0 | -10.86 | TAIFEX Proxy |
| 自營商 | 45.40 | 37.81 | +7.59 | 10.47 | 13.12 | -2.65 | +10.24 | TAIFEX Proxy |
| 三大法人合計 | 77.63 | 79.84 | -2.21 | 20.68 | 23.27 | -2.59 | +0.38 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 13,429 | TAIFEX Proxy |
| 買權空方 OI | 18,160 | TAIFEX Proxy |
| 買權多空淨 OI | -4,731 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-04→2026-11-05) | -605 | TAIFEX Proxy snapshots (2026-11-05) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,834 | TAIFEX Proxy |
| 賣權空方 OI | 11,619 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,785 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-04→2026-11-05) | -66 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：買權 2026-11-05／賣權 2026-11-05 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +455 | 2026-11-04→2026-11-05 | TAIFEX Proxy snapshots (2026-11-05) |
| 買權前十大 | -605 | 2026-11-04→2026-11-05 | TAIFEX Proxy snapshots (2026-11-05) |
| 賣權前十大 | -66 | 2026-11-04→2026-11-05 | TAIFEX Proxy snapshots (2026-11-05) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-06；資料時間：2026-11-07 01:47:16；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：1 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-11-06 非今日 2026-11-09，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-06 非今日 2026-11-09，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-06 非今日 2026-11-09，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-11-05；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-05)，非 T0 2026-11-06
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -911.9 | -99,930 | -4,310 | unavailable | +1,391 | unavailable | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +266.9 | +90,437 | +154 | unavailable | -15,106 | unavailable | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -494.8 | +1,680 | -875 | unavailable | -11,507 | unavailable | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
