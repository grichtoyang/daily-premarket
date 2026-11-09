# DATA_REPORT_20261110

- 報告日期：`2026-11-10`
- T0 交易日期：`2026-11-10`
- 資料產出時間：`2026-11-10 05:15:56`
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
| 加權指數 | 39,701.64 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 39,701.64 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -1,873.08 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -4.51 | % | TWSE OpenAPI MI_INDEX (備援) |
| 成交金額 | unavailable | 億元 | twse-proxy |

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
| 外資 | -900.6 | 億元 | twse-proxy /institutional |
| 投信 | +313.1 | 億元 | twse-proxy /institutional |
| 自營商 | -312.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -899.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 242,766 | 張 | HiStock |
| 融券增減 | 1,773 | 張 | HiStock |
| 融資維持率 | 151.90 | % | 前值遞補 (DATA 2026-11-06；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 286,044 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | unavailable | 億元 | twse-proxy |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | unavailable | 億元 | twse-proxy+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,549.94 | 173.08 | +2.35 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,253.14 | 673.71 | +2.74 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,907.62 | 917.63 | +3.40 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,389.75 | 1,104.02 | +2.15 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,033.93 | 643.68 | +6.85 | Yahoo Finance Chart API |
| VIX | ^VIX | 20.04 | -5.60 | -21.84 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 57,434.77 | -3,643.13 | -5.96 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,059.69 | -324.11 | -6.02 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,481.86 | -315.12 | -1.27 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,649.18 | -40.73 | -1.10 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,175.78 | -295.31 | -2.57 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,574.50 | 172.50 | +2.33 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,016.25 | 931.00 | +3.44 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,502.00 | 1,117.00 | +2.17 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,848.70 | 88.20 | +3.20 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.56 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.86 | 0.00 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.26 | -0.00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.76 | -0.35 | -1.05 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.67 | -0.63 | -0.61 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.92 | 0.43 | +0.27 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,340.33 | -16.01 | -1.18 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 388.62 | 13.18 | +3.51 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.89 | 1.04 | +7.51 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 34.36 | 2.73 | +8.63 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 87.00 | -3.83 | -4.22 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,147.10 | 72.20 | +1.77 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 74,803.47 | 218.82 | +0.29 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：台股漲停派對開起來 收盤飆1960點史上次強
  - 來源：Yahoo 台股；發布時間：2026-11-09T09:07:16Z；台北時間：2026-11-09 17:07
  - 摘要：台股大反攻！收漲1960點站回4萬1，寫下史上第二大收盤漲點。今(9)日加權指數盤中一度大漲2647.72點，終場上漲1960.06點、漲幅4.94%，收41,661.70點，收復部分上周跌幅，上市成交金額為8393.67億元。國安基金宣示
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E4%B8%80%E5%96%8A237%E6%AA%94%E4%BA%AE%E7%87%88%EF%BC%81%E5%9C%8B%E5%B7%A8%E5%A4%A7%E7%AB%8B%E5%85%89%E8%81%AF%E7%99%BC%E7%A7%91%E6%BC%B2%E5%81%9C-%E6%8B%B1%E5%8F%B0%E8%82%A1%E9%A3%86%E5%8F%B2%E4%B8%8A%E7%AC%AC%E4%BA%8C%E5%A4%A7%E6%BC%B2%E9%BB%9E%E9%87%8D%E5%9B%9E4%E8%90%AC1%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090716485.html
- 事件3：熱門股拉交割警報 景碩聯亞富喬違約金額破億
  - 來源：Yahoo 台股；發布時間：2026-11-09T10:34:45Z；台北時間：2026-11-09 18:34
  - 摘要：台股今（9）日多檔個股爆發違約交割，累計金額已近1.18億元。其中PCB廠景碩（3189）遭5家券商分公司通報違約，涉及金額高達2,908萬元。富喬違約交割更是波及18家券商據點，金額衝破6,953.75萬元。此外，聯亞也在美好證券楊梅分公
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9F%AD%E8%8F%9C%E7%BF%BB%E8%BB%8A%E9%80%A3%E7%92%B0%E7%88%86%EF%BC%81%E6%99%AF%E7%A2%A9%E3%80%81%E8%81%AF%E4%BA%9E%E3%80%81%E5%AF%8C%E5%96%AC%E7%88%86%E9%81%95%E7%B4%84%E4%BA%A4%E5%89%B2%E7%A0%B4%E5%84%84%E5%85%83-103445315.html
- 事件4：新台幣失血貶逾1角 交易員點名3大變數
  - 來源：Yahoo 台股；發布時間：2026-11-09T10:07:34Z；台北時間：2026-11-09 18:07
  - 摘要：（中央社記者潘姿羽台北9日電）國安基金護盤助威，台股今天展開絕地大反攻，不過新台幣匯率依舊疲弱，今天收盤收32.882元，重貶1.14角，出口商與外資激烈交鋒之下，交投熱絡，台北及元太外匯市場總成交金額放大至45億美元，為史上第8大量。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%BC%B7%E5%BD%88%E9%9B%A3%E6%93%8B%E5%A4%96%E8%B3%87%E5%8C%AF%E5%87%BA-%E6%96%B0%E5%8F%B0%E5%B9%A3%E7%88%86%E9%87%8F%E9%87%8D%E8%B2%B6%E9%80%BE1%E8%A7%92%E6%94%B632-882%E5%85%83-100734985.html
- 事件5：台股先嗨後跌人氣沒退 10月交易戶數創3個月新高
  - 來源：Yahoo 台股；發布時間：2026-11-09T10:09:36Z；台北時間：2026-11-09 18:09
  - 摘要：（中央社記者曾仁凱台北9日電）台股10月先盛後衰，月初一度逼近5萬點大關，但隨後回檔，全月下跌2728.30點，以45211.83點作收。根據台灣證券交易所統計，10月台股有交易戶數629萬2136戶，比9月增加約86.42萬戶，創下近3個
  - 原文連結：https://tw.stock.yahoo.com/news/10%E6%9C%88%E5%8F%B0%E8%82%A1%E6%9C%89%E4%BA%A4%E6%98%93%E6%88%B6%E6%95%B8629%E8%90%AC%E6%88%B6-3%E5%80%8B%E6%9C%88%E6%96%B0%E9%AB%98-100936483.html
- 事件6：統一超20億入股LOPIA獲放行 預計年底交割
  - 來源：Yahoo 台股；發布時間：2026-11-09T09:53:51Z；台北時間：2026-11-09 17:53
  - 摘要：統一超商（2912）砸下逾20億元入股日本連鎖超市LOPIA，正式獲公平會放行！公平會今（9）日宣布，通過統一企業透過旗下統一超商，取得日商樂比亞在台新設零售超市及食品加工公司股權的結合案。其中，統一超將分別取得兩家公司51%及49%股份。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%B5%B1%E4%B8%80%E8%B6%85%E7%A0%B820%E5%84%84%E5%85%A5%E8%82%A1lopia%E9%81%8E%E9%97%9C%EF%BC%81%E5%85%AC%E5%B9%B3%E6%9C%83%E9%BB%9E%E9%A0%AD-%E5%85%AC%E5%8F%B8%E4%B9%9F%E5%9B%9E%E6%87%89%E4%BA%86-105359594.html
- 事件7：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件8：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件9：A key report for where inflation stood in October comes out Tuesday. Here's what to expect
  - 來源：CNBC；發布時間：Mon, 09 Nov 2026 21:03:55 GMT；台北時間：2026-11-10 05:03
  - 摘要：The CPI headline reading is expected to show an increase of 0.3% while the core is forecast to increase 0.2%.
  - 原文連結：https://www.cnbc.com/2026/11/09/october-cpi-report-2026-inflation.html
- 事件10：Trump administration proposes stricter work-search rules for unemployment benefits
  - 來源：CNBC；發布時間：Mon, 09 Nov 2026 19:59:55 GMT；台北時間：2026-11-10 03:59
  - 摘要：A Labor Department proposal would require unemployment claimants to report at least five qualifying work-search activities each week.
  - 原文連結：https://www.cnbc.com/2026/11/09/trump-unemployment-work-search-rule.html
- 事件11：Hot U.S. inflation hasn't cooled off. Rising consumer prices to keep Fed rate hike on track.
  - 來源：MarketWatch；發布時間：Mon, 09 Nov 2026 21:01:00 GMT；台北時間：2026-11-10 05:01
  - 摘要：Rising prices point to the Fed increasing borrowing costs before Christmas.
  - 原文連結：https://www.marketwatch.com/story/hot-u-s-inflation-hasnt-cooled-off-rising-consumer-prices-to-keep-fed-rate-hike-on-track-926c44b0?mod=mw_rss_topstories
- 事件12：The stock-market rally keeps spreading beyond Big Tech. October inflation data could put it to the test.
  - 來源：MarketWatch；發布時間：Mon, 09 Nov 2026 20:42:00 GMT；台北時間：2026-11-10 04:42
  - 摘要：Tuesday&#x2019;s CPI inflation report and a heavy lineup of Federal Reserve speakers could test the rotation trade&#x2019;s resilience
  - 原文連結：https://www.marketwatch.com/story/the-stock-market-rally-keeps-spreading-beyond-big-tech-october-inflation-data-could-put-it-to-the-test-c1b87dcd?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-10

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 40,099 | TAIFEX Proxy |
| 最高價 | 42,317 | TAIFEX Proxy |
| 最低價 | 39,996 | TAIFEX Proxy |
| 收盤價 | 41,423 | TAIFEX Proxy |
| 漲跌點數 | +1,771 | TAIFEX Proxy |
| 漲跌幅 | +4.47 | TAIFEX Proxy |
| 成交量 | 94,766 | TAIFEX Proxy |
| 日盤高點及低點 | 42,317 / 39,996 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 102,490 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,600 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,890 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-06→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-09) |
- 資料日期：2026-11-06 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 99,731 | TAIFEX Proxy |
| 外資日盤空單交易量 | 102,516 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,785 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +5,114 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -696 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,633 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +136.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 41,423 | TAIFEX Proxy |
| 加權指數價格 | 39,701.64 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +1,721.36 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +4.34 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +1,721.36 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 41,423 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 94,766 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 99,731 | 102,516 | -2,785 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 5,134 | 20 | +5,114 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 7,672 | 8,368 | -696 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 112,537 | 110,904 | +1,633 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 102,490 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,600 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,890 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-06→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

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
| 交易日期 | 2026-11-10 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-10 05:15:56 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 136,615 | TAIFEX Proxy |
| Call 總未平倉量 OI | 68,097 | TAIFEX Proxy |
| Call OI 增減 (2026-11-09→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 109,360 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,424 | TAIFEX Proxy |
| Put OI 增減 (2026-11-09→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.25 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.17 | TAIFEX Proxy |
| Put／Call Ratio | 0.46 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-05→2026-11-06) | 3.22 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-05→2026-11-06) | -4.36 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 32,589 | TAIFEX Proxy |
| 外資 Call日賣 | 30,109 | TAIFEX Proxy |
| 外資 Call日淨 | +2,480 | TAIFEX Proxy |
| 外資 Put日買 | 33,416 | TAIFEX Proxy |
| 外資 Put日賣 | 32,877 | TAIFEX Proxy |
| 外資 Put日淨 | +539 | TAIFEX Proxy |
| 外資 Call夜買 | 11,803 | TAIFEX Proxy |
| 外資 Call夜賣 | 11,695 | TAIFEX Proxy |
| 外資 Call夜淨 | +108 | TAIFEX Proxy |
| 外資 Put夜買 | 9,946 | TAIFEX Proxy |
| 外資 Put夜賣 | 9,941 | TAIFEX Proxy |
| 外資 Put夜淨 | +5 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,941 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2,372 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +534 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 54,273 | TAIFEX Proxy |
| 自營商 Call日賣 | 48,638 | TAIFEX Proxy |
| 自營商 Call日淨 | +5,635 | TAIFEX Proxy |
| 自營商 Put日買 | 38,984 | TAIFEX Proxy |
| 自營商 Put日賣 | 45,295 | TAIFEX Proxy |
| 自營商 Put日淨 | -6,311 | TAIFEX Proxy |
| 自營商 Call夜買 | 14,346 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,375 | TAIFEX Proxy |
| 自營商 Call夜淨 | +1,971 | TAIFEX Proxy |
| 自營商 Put夜買 | 10,572 | TAIFEX Proxy |
| 自營商 Put夜賣 | 11,338 | TAIFEX Proxy |
| 自營商 Put夜淨 | -766 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +11,946 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +3,664 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,545 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,692 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,300 | 3,846 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 2,981 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,692 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,692 | 12.76% | TAIFEX Proxy |
| C2 | 48,300 | 3,846 | 5.65% | TAIFEX Proxy |
| C3 | 45,000 | 2,981 | 4.38% | TAIFEX Proxy |
| C4 | 43,000 | 2,509 | 3.68% | TAIFEX Proxy |
| C5 | 44,000 | 1,724 | 2.53% | TAIFEX Proxy |
| C6 | 44,500 | 1,692 | 2.48% | TAIFEX Proxy |
| C7 | 41,000 | 1,616 | 2.37% | TAIFEX Proxy |
| C8 | 46,500 | 1,429 | 2.1% | TAIFEX Proxy |
| C9 | 42,000 | 1,246 | 1.83% | TAIFEX Proxy |
| C10 | 40,700 | 1,140 | 1.67% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 37,400 | 2,258 | TAIFEX Proxy |
| Put OI 第2大履約價 | 38,000 | 2,008 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 1,887 | TAIFEX Proxy |
| Put OI 最大履約價 | 37,400 | 2,258 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 37,400 | 2,258 | 7.19% | TAIFEX Proxy |
| P2 | 38,000 | 2,008 | 6.39% | TAIFEX Proxy |
| P3 | 40,000 | 1,887 | 6.0% | TAIFEX Proxy |
| P4 | 35,700 | 1,756 | 5.59% | TAIFEX Proxy |
| P5 | 39,000 | 1,290 | 4.11% | TAIFEX Proxy |
| P6 | 41,000 | 1,114 | 3.55% | TAIFEX Proxy |
| P7 | 39,500 | 924 | 2.94% | TAIFEX Proxy |
| P8 | 40,900 | 835 | 2.66% | TAIFEX Proxy |
| P9 | 40,500 | 755 | 2.4% | TAIFEX Proxy |
| P10 | 37,500 | 750 | 2.39% | TAIFEX Proxy |


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
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-09→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 37,400 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-09→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-10 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 40,506.19 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-10 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-09→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 65,466 | 63,525 | +1,941 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 347 | 280 | +67 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 99,568 | 87,622 | +11,946 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 165,381 | 151,427 | +13,954 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 28.80 | 28.30 | +0.50 | 20.78 | 20.89 | -0.11 | +0.61 | TAIFEX Proxy |
| 投信 | 0.13 | 0.05 | +0.08 | 0.00 | 0.00 | +0 | +0.08 | TAIFEX Proxy |
| 自營商 | 19.47 | 17.73 | +1.75 | 7.22 | 6.76 | +0.46 | +1.29 | TAIFEX Proxy |
| 三大法人合計 | 48.41 | 46.08 | +2.32 | 28.00 | 27.66 | +0.35 | +1.97 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,097 | TAIFEX OpenAPI |
| 買權空方 OI | 19,390 | TAIFEX OpenAPI |
| 買權多空淨 OI | -5,293 | TAIFEX OpenAPI |
| 買權多空淨 OI 變化 (2026-11-06→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,486 | TAIFEX OpenAPI |
| 賣權空方 OI | 13,491 | TAIFEX OpenAPI |
| 賣權多空淨 OI | -3,005 | TAIFEX OpenAPI |
| 賣權多空淨 OI 變化 (2026-11-06→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-09) |
- 資料日期：買權 2026-11-06／賣權 2026-11-06 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-06→2026-11-06 | TAIFEX Proxy snapshots (2026-11-09) |
| 買權前十大 | +0 | 2026-11-06→2026-11-06 | TAIFEX Proxy snapshots (2026-11-09) |
| 賣權前十大 | +0 | 2026-11-06→2026-11-06 | TAIFEX Proxy snapshots (2026-11-09) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-10；資料時間：2026-11-10 05:15:56；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-09，非 T0 2026-11-10)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-09 非今日 2026-11-10，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-09 非今日 2026-11-10，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-09 非今日 2026-11-10，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-09 (T0 2026-11-10 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-09 (T0 2026-11-10 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-06；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151109, T0=1151110)
- 註記：三大法人回傳日期 20261109 (T0 20261110)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-06)，非 T0 2026-11-10
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -900.6 | unavailable | -2,785 | unavailable | +1,941 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +313.1 | unavailable | +5,114 | unavailable | +67 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -312.2 | unavailable | -696 | unavailable | +11,946 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
