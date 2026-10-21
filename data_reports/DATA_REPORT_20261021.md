# DATA_REPORT_20261021

- 報告日期：`2026-10-22`
- T0 交易日期：`2026-10-21`
- 資料產出時間：`2026-10-22 07:24:52`
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
| 加權指數 | 46,887.77 | 點 | twse-proxy |
| 開盤 | 46,454.33 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,254.93 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,454.33 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,887.77 | 點 | twse-proxy |
| 漲跌點數 | 594.84 | 點 | twse-proxy |
| 漲跌幅 | +1.28 | % | twse-proxy |
| 成交金額 | 8,746.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 600 | twse-proxy |
| 下跌家數 | 380 | twse-proxy |
| 平盤家數 | 101 | twse-proxy |
| 漲停家數 | 24 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 520 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 253 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 96 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 27 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +22.4 | 億元 | twse-proxy /institutional |
| 投信 | +128.0 | 億元 | twse-proxy /institutional |
| 自營商 | -135.7 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +14.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,603.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +72.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 231,082 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -23,914 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 178.93 | % | 前值遞補 (DATA 2026-10-20；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,570,871 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 38,484 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -600 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,746.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,144.0 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,890.2 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,757.17 | 44.60 | +0.58 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,702.86 | 278.04 | +1.05 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,822.52 | 332.24 | +1.13 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,856.09 | 360.21 | +0.69 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,505.56 | 221.75 | +1.97 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.68 | -0.63 | -3.64 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 64,075.42 | -841.28 | -1.30 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,552.74 | -215.27 | -3.73 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,867.74 | -319.09 | -1.32 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,735.37 | 4.45 | +0.12 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,801.29 | -16.13 | -0.14 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,771.50 | 16.25 | +0.21 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,830.00 | 154.75 | +0.52 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,937.00 | 218.00 | +0.41 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,782.20 | -4.70 | -0.17 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.81 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.15 | 0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.44 | 0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.39 | -0.19 | -0.57 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.69 | -0.04 | -0.04 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.15 | -0.12 | -0.07 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,325.94 | 2.00 | +0.15 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 431.89 | 6.81 | +1.60 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.82 | 0.15 | +0.76 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 42.41 | 1.64 | +4.02 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 97.80 | -3.99 | -3.92 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,145.00 | 2.40 | +0.06 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 84,290.01 | 1,349.01 | +1.63 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股強彈594點4萬7卻沒守住「電金」聯手扛反攻旗
  - 來源：Yahoo 台股；發布時間：2026-10-21T09:43:30Z；台北時間：2026-10-21 17:43
  - 摘要：電金聯手反攻，台股強彈594點、站回五日線！今(21)日加權指數終場上漲594.84點、漲幅1.28%，收46,887.77點，成交金額8,348.41億元。大盤盤中一度大漲962點、上探47,254.93點，隨後漲勢收斂，4萬7關卡得而復
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E7%B5%82%E6%96%BC%E8%BD%89%E8%B2%B7%E4%BA%94%E6%97%A5%E7%B7%9A%E6%90%B6%E5%9B%9E%E3%80%814%E8%90%AC7%E6%B2%92%E5%AE%88%E4%BD%8F%EF%BC%81%E5%8F%B0%E8%82%A1%E6%BC%B2594%E9%BB%9E%E3%80%8C%E9%9B%BB%E9%87%91%E3%80%8D%E8%81%AF%E6%89%8B%E6%94%BE%E7%B4%85%E8%89%B2%E7%85%99%E7%81%AB%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-094330511.html
- 事件2：SpaceX的AI營收暴增830％ 專家盤點台灣ETF誰最敢押
  - 來源：Yahoo 台股；發布時間：2026-10-21T10:44:57Z；台北時間：2026-10-21 18:44
  - 摘要：SpaceX第三季營收年增161%，淨利衝上44億美元！AI算力業務年增830%超越星鏈。財經專家葉育碩點名玉山未來全球算力（009827）持股SpaceX近12%，完整解析其布局亮點與投資策略。（記者唐家興）
  - 原文連結：https://tw.stock.yahoo.com/news/spacex%E5%96%AE%E5%AD%A3%E7%8B%82%E8%B3%BA1400%E5%84%84-%E5%8F%B0%E7%81%A3etf%E8%AA%B0%E6%9C%80%E6%95%A2%E6%8A%BC-%E8%91%89%E8%82%B2%E7%A2%A9%E9%BB%9E%E5%90%8D%E9%80%99%E6%AA%94-%E6%8C%81%E8%82%A1%E8%BF%9112-103200432.html
- 事件3：台郡搭輝達題材股價狂飆 自結財報出爐8月仍未轉盈
  - 來源：Yahoo 台股；發布時間：2026-10-21T08:58:44Z；台北時間：2026-10-21 16:58
  - 摘要：軟板廠台郡（6269）今日因當沖率、漲幅過高等原因而遭列注意股，因此被強制公布自結獲利，8月台郡單月虧損1.35億元，年減率達535%，每股虧損來到0.01元。
  - 原文連結：https://tw.stock.yahoo.com/news/6%E5%A4%A9%E9%A3%865%E6%88%90%E5%88%97%E6%B3%A8%E6%84%8F%E8%82%A1%EF%BC%81%E3%80%8C%E8%BC%9D%E9%81%94%E6%A6%82%E5%BF%B5%E8%82%A1%E3%80%8D%E5%8F%B0%E9%83%A1%E8%87%AA%E7%B5%908%E6%9C%88%E6%AF%8F%E8%82%A1%E8%99%A7001%E5%85%83-%E5%B9%B4%E6%B8%9B98-085911152.html
- 事件4：薔琵逼近搶菜潮來了嗎 兩大量販曝採買仍平穩
  - 來源：Yahoo 台股；發布時間：2026-10-21T08:57:41Z；台北時間：2026-10-21 16:57
  - 摘要：薔琵颱風逼近台灣，適逢光復節3天連假將至，民眾是否已提前搶購蔬菜、泡麵及飲用水等防颱物資？萬家福量販與愛買今（21）日表示，目前賣場尚未出現明顯搶購潮，整體採買情況平穩，其中愛買指出，蔬菜、泡麵及飲用水等商品銷量仍與平常持平，也沒有缺貨情況
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%96%94%E7%90%B5%E9%A2%B1%E9%A2%A8%E4%BE%86%E8%A5%B2%E6%90%B6%E8%8F%9C%E6%BD%AE%E8%A6%81%E4%BE%86%E4%BA%86%EF%BC%9F%E8%90%AC%E5%AE%B6%E7%A6%8F%E3%80%81%E6%84%9B%E8%B2%B7%E6%9B%9D%E6%9C%80%E6%96%B0%E8%B2%B7%E6%B0%A3%EF%BC%9A%E5%B0%9A%E6%9C%AA%E7%BC%BA%E8%B2%A8-094231582.html
- 事件5：存股資優生也要拚斜槓 水泥股從配息到轉型一次看
  - 來源：Yahoo 台股；發布時間：2026-10-20T10:00:00Z；台北時間：2026-10-20 18:00
  - 摘要：台泥（1101）是許多傳統存股族的心頭好，日前召開股東臨時會通過歐洲子公司Cimpor International Holdings海外上市案，近期股價衝上16個月新高。不只台泥，10月15日台股狂瀉1655點，水泥族群卻表現抗跌，日前亞泥
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E6%B3%A5%E3%80%81%E4%BA%9E%E6%B3%A5%E9%80%A3%E7%BA%8C%E9%85%8D%E6%81%AF43%E5%B9%B4%E2%8B%AF%E6%98%94%E6%97%A5%E7%9A%84%E5%AD%98%E8%82%A1%E8%B3%87%E5%84%AA%E7%94%9F%E7%8F%BE%E5%9C%A8%E9%82%84%E8%83%BD%E5%AD%98%E5%97%8E%EF%BC%9F%E6%B0%B4%E6%B3%A5%E6%97%8F%E7%BE%A4%E7%9A%84%E7%BE%8E%E9%BA%97%E8%88%87%E5%93%80%E6%84%81-%E5%90%84%E5%AE%B6%E6%8B%9A%E8%BD%89%E5%9E%8B%E5%90%84%E9%A1%AF%E7%A5%9E%E9%80%9A%EF%BC%81%EF%BD%9C%E7%9B%A4%E9%BB%9E%E6%A6%82%E5%BF%B5%E8%82%A1-100000179.html
- 事件6：美光罷工倒數4》董事長出面仍破局　桃園罷工24小時、台中掀連署反彈
  - 來源：Yahoo 台股；發布時間：2026-10-21T15:25:49Z；台北時間：2026-10-21 23:25
  - 摘要：美光勞資爭議再掀波瀾！美光甫與台中工會簽署協議，桃園工會卻宣布22日罷工24小時。美光派出台灣美光董事長及執行長（CEO）幕僚長參與協商，仍未化解分潤爭議；另一方面，《民報》獨家披露美光新獎酬制度後，相關內容在網路引發討論與轉傳，更出現要求
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E5%85%89%E7%BD%B7%E5%B7%A5%E5%80%92%E6%95%B84-%E8%91%A3%E4%BA%8B%E9%95%B7%E5%87%BA%E9%9D%A2%E4%BB%8D%E7%A0%B4%E5%B1%80-%E6%A1%83%E5%9C%92%E7%BD%B7%E5%B7%A524%E5%B0%8F%E6%99%82-%E5%8F%B0%E4%B8%AD%E6%8E%80%E9%80%A3%E7%BD%B2%E5%8F%8D%E5%BD%88-152549950.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：CoreWeave’s market confidence erodes as bond yields spike and stock sinks
  - 來源：CNBC；發布時間：Wed, 21 Oct 2026 22:50:35 GMT；台北時間：2026-10-22 06:50
  - 摘要：CoreWeave shares are down 29% in October, and the spreads in its credit default swaps are widening.
  - 原文連結：https://www.cnbc.com/2026/10/21/coreweaves-market-confidence-erodes-as-bond-yields-spike-stock-sinks.html
- 事件9：Housing is flashing warning signs just as the Fed weighs more interest rate hikes
  - 來源：CNBC；發布時間：Wed, 21 Oct 2026 11:20:58 GMT；台北時間：2026-10-21 19:20
  - 摘要：Housing data deteriorated further in September, according to separate reports Tuesday.
  - 原文連結：https://www.cnbc.com/2026/10/20/housing-mortgage-rates-real-estate-federal-reserve.html
- 事件10：Apple's iPhone Duo in short supply — plus, the 2 stocks fueling an AI rebound
  - 來源：CNBC；發布時間：Wed, 21 Oct 2026 19:47:38 GMT；台北時間：2026-10-22 03:47
  - 摘要：Every weekday, the Investing Club releases the Homestretch; an actionable afternoon update just in time for the last hour of trading.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/21/apples-iphone-duo-in-short-supply-plus-2-stocks-fueling-an-ai-rebound.html
- 事件11：Expanding AI trade is turning safety stocks into a 'Texas hedge'
  - 來源：CNBC；發布時間：Wed, 21 Oct 2026 17:14:14 GMT；台北時間：2026-10-22 01:14
  - 摘要：The growing AI trade is infiltrating traditionally safe sectors like utilities, making hedging more difficult.
  - 原文連結：https://www.cnbc.com/2026/10/21/expanding-ai-trade-is-turning-safety-stocks-into-a-texas-hedge.html
- 事件12：Goldman Sachs, JPMorgan and Morgan Stanley are dominating the AI stock boom. Here's their edge
  - 來源：CNBC；發布時間：Wed, 21 Oct 2026 15:30:50 GMT；台北時間：2026-10-21 23:30
  - 摘要：Wall Street’s Big Three have generated $52 billion in equity trading revenue this year, capturing about 80% of the market on rising margin lending to 
  - 原文連結：https://www.cnbc.com/2026/10/21/goldman-sachs-jpmorgan-morgan-stanley-ai-trading.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-21

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,388 | TAIFEX Proxy |
| 最高價 | 47,450 | TAIFEX Proxy |
| 最低價 | 46,872 | TAIFEX Proxy |
| 收盤價 | 46,992 | TAIFEX Proxy |
| 漲跌點數 | +482 | TAIFEX Proxy |
| 漲跌幅 | +1.04 | TAIFEX Proxy |
| 成交量 | 48,578 | TAIFEX Proxy |
| 日盤高點及低點 | 47,450 / 46,872 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,991 | TAIFEX Proxy |
| 最高價 | 47,555 | TAIFEX Proxy |
| 最低價 | 46,983 | TAIFEX Proxy |
| 收盤價 | 47,482 | TAIFEX Proxy |
| 漲跌點數 | +469 | TAIFEX Proxy |
| 漲跌幅 | +1.00 | TAIFEX Proxy |
| 成交量 | 35,753 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,555 / 46,983 | TAIFEX Proxy |
| 結算價 | 47,013 | TAIFEX Proxy |
| 未平倉量 | 114,962 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,410 | TAIFEX Proxy |
| 外資空方 OI | 95,482 | TAIFEX Proxy |
| 外資多空淨 OI | -86,072 | TAIFEX Proxy |
| 投信多方 OI | 86,485 | TAIFEX Proxy |
| 投信空方 OI | 2,707 | TAIFEX Proxy |
| 投信多空淨 OI | +83,778 | TAIFEX Proxy |
| 自營商多方 OI | 5,149 | TAIFEX Proxy |
| 自營商空方 OI | 3,433 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,716 | TAIFEX Proxy |
| 三大法人合計多方 OI | 101,044 | TAIFEX Proxy |
| 三大法人合計空方 OI | 101,622 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -578 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +3,676 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -611 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -984 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 7,685 | TAIFEX Proxy |
| 前十大交易人空方 OI | 11,817 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -4,132 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-19→2026-10-20) | -6,740 | TAIFEX Proxy snapshots (2026-10-20) |
- 資料日期：2026-10-20 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 54,619 | TAIFEX Proxy |
| 外資日盤空單交易量 | 53,557 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,062 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 18,496 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 19,414 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -918 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,980 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,466 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,466 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -2,306 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +536 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -2,842 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +222 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -382 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +19.5 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -36.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,992 | TAIFEX Proxy |
| 加權指數價格 | 46,887.77 | twse-proxy |
| 台指期與加權指數價差 | +104.23 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.22 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +104.23 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +490 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,992 | 47,482 | -490 | TAIFEX Proxy |
| 成交量 | 40,515 | 35,753 | +4,762 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 54,619 | 53,557 | +1,062 | 18,496 | 19,414 | -918 | +1,980 | 9,410 | 95,482 | -86,072 | +3,676 | TAIFEX Proxy |
| 投信 | 1,737 | 271 | +1,466 | 0 | 0 | +0 | +1,466 | 86,485 | 2,707 | +83,778 | -611 | TAIFEX Proxy |
| 自營商 | 8,699 | 11,005 | -2,306 | 1,231 | 695 | +536 | -2,842 | 5,149 | 3,433 | +1,716 | -984 | TAIFEX Proxy |
| 三大法人合計 | 65,055 | 64,833 | +222 | 19,727 | 20,109 | -382 | +604 | 101,044 | 101,622 | -578 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 7,685 | TAIFEX Proxy |
| 前十大交易人空方 OI | 11,817 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -4,132 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-19→2026-10-20) | -6,740 | TAIFEX Proxy snapshots (2026-10-20) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 46.88% | TAIFEX Proxy |
| 夜盤漲跌點數 | +469 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -918 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-21 | TAIFEX Proxy |
| 到期月份／到期日 | 202610 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-22 07:24:52 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 385,732 | TAIFEX Proxy |
| Call 總未平倉量 OI | 129,567 | TAIFEX Proxy |
| Call OI 增減 (2026-10-20→2026-10-21) | +22,864 | TAIFEX Proxy snapshots (2026-10-20) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 452,016 | TAIFEX Proxy |
| Put 總未平倉量 OI | 87,614 | TAIFEX Proxy |
| Put OI 增減 (2026-10-20→2026-10-21) | +19,394 | TAIFEX Proxy snapshots (2026-10-20) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.85 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.48 | TAIFEX Proxy |
| Put／Call Ratio | 0.68 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-19→2026-10-20) | 34.52 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-19→2026-10-20) | 4.57 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 129,875 | TAIFEX Proxy |
| 外資 Call日賣 | 136,026 | TAIFEX Proxy |
| 外資 Call日淨 | -6,151 | TAIFEX Proxy |
| 外資 Put日買 | 178,176 | TAIFEX Proxy |
| 外資 Put日賣 | 177,124 | TAIFEX Proxy |
| 外資 Put日淨 | +1,052 | TAIFEX Proxy |
| 外資 Call夜買 | 18,352 | TAIFEX Proxy |
| 外資 Call夜賣 | 18,236 | TAIFEX Proxy |
| 外資 Call夜淨 | +116 | TAIFEX Proxy |
| 外資 Put夜買 | 20,801 | TAIFEX Proxy |
| 外資 Put夜賣 | 21,125 | TAIFEX Proxy |
| 外資 Put夜淨 | -324 | TAIFEX Proxy |
| 外資 日盤淨總量 | -7,203 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -6,267 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,376 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 99,080 | TAIFEX Proxy |
| 自營商 Call日賣 | 102,995 | TAIFEX Proxy |
| 自營商 Call日淨 | -3,915 | TAIFEX Proxy |
| 自營商 Put日買 | 106,651 | TAIFEX Proxy |
| 自營商 Put日賣 | 117,234 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,583 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,497 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,186 | TAIFEX Proxy |
| 自營商 Call夜淨 | -689 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,128 | TAIFEX Proxy |
| 自營商 Put夜賣 | 14,336 | TAIFEX Proxy |
| 自營商 Put夜淨 | +3,792 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +6,668 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -3,226 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -14,375 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 47,000 | 7,175 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,500 | 6,329 | TAIFEX Proxy |
| Call OI 第3大履約價 | 54,000 | 5,684 | TAIFEX Proxy |
| Call OI 最大履約價 | 47,000 | 7,175 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 47,000 | 7,175 | 5.54% | TAIFEX Proxy |
| C2 | 49,500 | 6,329 | 4.88% | TAIFEX Proxy |
| C3 | 54,000 | 5,684 | 4.39% | TAIFEX Proxy |
| C4 | 52,000 | 5,158 | 3.98% | TAIFEX Proxy |
| C5 | 48,000 | 3,851 | 2.97% | TAIFEX Proxy |
| C6 | 47,200 | 3,723 | 2.87% | TAIFEX Proxy |
| C7 | 49,000 | 3,502 | 2.7% | TAIFEX Proxy |
| C8 | 47,500 | 3,164 | 2.44% | TAIFEX Proxy |
| C9 | 46,900 | 3,158 | 2.44% | TAIFEX Proxy |
| C10 | 46,650 | 2,716 | 2.1% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 5,858 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,500 | 4,530 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,000 | 3,668 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 5,858 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 5,858 | 6.69% | TAIFEX Proxy |
| P2 | 46,500 | 4,530 | 5.17% | TAIFEX Proxy |
| P3 | 45,000 | 3,668 | 4.19% | TAIFEX Proxy |
| P4 | 47,000 | 2,669 | 3.05% | TAIFEX Proxy |
| P5 | 46,600 | 2,626 | 3.0% | TAIFEX Proxy |
| P6 | 46,800 | 2,131 | 2.43% | TAIFEX Proxy |
| P7 | 46,550 | 1,995 | 2.28% | TAIFEX Proxy |
| P8 | 46,300 | 1,988 | 2.27% | TAIFEX Proxy |
| P9 | 46,700 | 1,982 | 2.26% | TAIFEX Proxy |
| P10 | 46,650 | 1,872 | 2.14% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 47,000 (+3,386) | TAIFEX Proxy snapshots (2026-10-20) |
| Call OI 減少最多的履約價 | 47,900 (-504) | TAIFEX Proxy snapshots (2026-10-20) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 46,500 (+2,489) | TAIFEX Proxy snapshots (2026-10-20) |
| Put OI 減少最多的履約價 | 45,000 (-436) | TAIFEX Proxy snapshots (2026-10-20) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 47,000 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-20→2026-10-21) | -2,500 | TAIFEX Proxy snapshots (2026-10-20) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-20→2026-10-21) | +0 | TAIFEX Proxy snapshots (2026-10-20) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,174.50 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,700 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-20→2026-10-21) | +200 | TAIFEX Proxy snapshots (2026-10-20) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 306,999 | 314,202 | -7,203 | 39,477 | 39,037 | +440 | -7,643 | TAIFEX Proxy |
| 投信 | 7 | 9,685 | -9,678 | 0 | 0 | +0 | -9,678 | TAIFEX Proxy |
| 自營商 | 216,314 | 209,646 | +6,668 | 29,833 | 34,314 | -4,481 | +11,149 | TAIFEX Proxy |
| 三大法人合計 | 523,320 | 533,533 | -10,213 | 69,310 | 73,351 | -4,041 | -6,172 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 16.49 | 17.24 | -0.75 | 4.38 | 4.35 | +0.03 | -0.78 | TAIFEX Proxy |
| 投信 | 0.00 | 6.41 | -6.41 | 0.00 | 0.00 | +0 | -6.41 | TAIFEX Proxy |
| 自營商 | 18.51 | 12.51 | +5.99 | 3.19 | 5.02 | -1.83 | +7.82 | TAIFEX Proxy |
| 三大法人合計 | 35.00 | 36.17 | -1.16 | 7.56 | 9.37 | -1.80 | +0.64 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 5,000 | TAIFEX Proxy |
| 買權空方 OI | 6,459 | TAIFEX Proxy |
| 買權多空淨 OI | -1,459 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-19→2026-10-21) | +13,314 | TAIFEX Proxy snapshots (2026-10-20) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,216 | TAIFEX Proxy |
| 賣權空方 OI | 8,501 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,285 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-19→2026-10-21) | -2,449 | TAIFEX Proxy snapshots (2026-10-20) |
- 資料日期：買權 2026-10-21／賣權 2026-10-21 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -6,740 | 2026-10-19→2026-10-20 | TAIFEX Proxy snapshots (2026-10-20) |
| 買權前十大 | +13,314 | 2026-10-19→2026-10-21 | TAIFEX Proxy snapshots (2026-10-20) |
| 賣權前十大 | -2,449 | 2026-10-19→2026-10-21 | TAIFEX Proxy snapshots (2026-10-20) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-21；資料時間：2026-10-22 07:24:52；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：8 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-21 非今日 2026-10-22，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-10-20；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-20)，非 T0 2026-10-21
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +22.4 | -86,072 | +1,062 | -918 | -7,203 | +440 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +128.0 | +83,778 | +1,466 | +0 | -9,678 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -135.7 | +1,716 | -2,306 | +536 | +6,668 | -4,481 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
