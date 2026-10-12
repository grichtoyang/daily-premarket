# DATA_REPORT_20261008

- 報告日期：`2026-10-12`
- T0 交易日期：`2026-10-08`
- 資料產出時間：`2026-10-12 08:18:56`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,313.44 | 點 | twse-proxy |
| 開盤 | 49,783.06 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,783.06 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 49,189.77 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,313.44 | 點 | twse-proxy |
| 漲跌點數 | -492.93 | 點 | twse-proxy |
| 漲跌幅 | -0.99 | % | twse-proxy |
| 成交金額 | 9,245.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 425 | twse-proxy |
| 下跌家數 | 540 | twse-proxy |
| 平盤家數 | 109 | twse-proxy |
| 漲停家數 | 14 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 356 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 416 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 95 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 23 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 3 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -758.5 | 億元 | twse-proxy /institutional |
| 投信 | +30.1 | 億元 | twse-proxy /institutional |
| 自營商 | -187.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -915.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,742.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +53.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 252,356 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -3,158 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 197.12 | % | wantgoo 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,553,408 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 40,407 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -3 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,245.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,562.3 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,807.4 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,811.54 | 46.18 | +0.59 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,366.17 | 172.83 | +0.64 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,883.15 | 157.34 | +0.51 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,654.95 | 423.31 | +0.83 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,572.42 | -51.29 | -0.41 | Yahoo Finance Chart API |
| VIX | ^VIX | 14.84 | -0.57 | -3.70 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 69,030.92 | -11.19 | -0.02 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,625.93 | -177.97 | -2.62 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,211.35 | 425.56 | +1.79 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,813.79 | 1.89 | +0.05 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,641.86 | 20.96 | +0.17 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,880.50 | 20.75 | +0.26 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 31,259.50 | 150.75 | +0.48 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,034.00 | 108.00 | +0.21 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,828.70 | 6.60 | +0.23 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.60 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.91 | -0.02 | -0.06 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.16 | -0.05 | -0.05 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.12 | 0.06 | +0.04 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,338.48 | -4.51 | -0.34 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 453.31 | -4.68 | -1.02 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 22.96 | 0.14 | +0.61 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 46.43 | 1.17 | +2.59 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 90.86 | -0.99 | -1.08 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,225.80 | 9.50 | +0.23 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,669.30 | 757.07 | +0.91 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：退斡後換房仲買同房｜3個月條款、換房仲、服務費一次看懂
  - 來源：Yahoo 台股；發布時間：2026-10-11T11:52:00Z；台北時間：2026-10-11 19:52
  - 摘要：新北地方法院就曾審理一起案例，買方退斡隔天換另一名房仲，以更低房價買到同一間房，原房仲求償241萬餘元，最後遭法院駁回。

阿明用這個案例，把退斡後重新買房最重要的法律觀念一次整理。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%80%80%E6%96%A1%E5%BE%8C%E6%8F%9B%E6%88%BF%E4%BB%B2%E8%B2%B7%E5%90%8C%E6%88%BF%EF%BD%9C3%E5%80%8B%E6%9C%88%E6%A2%9D%E6%AC%BE%E3%80%81%E6%8F%9B%E6%88%BF%E4%BB%B2%E3%80%81%E6%9C%8D%E5%8B%99%E8%B2%BB%E4%B8%80%E6%AC%A1%E7%9C%8B%E6%87%82-115200216.html
- 事件2：外資瘋搶主動式！「這檔」刷掛牌以來新高價、外資掃入逾6.5萬張　00403A被狂買22.7萬張登買超王
  - 來源：Yahoo 台股；發布時間：2026-10-11T10:30:00Z；台北時間：2026-10-11 18:30
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導台股加權指數上周（10/5～10/8）收在49313.44點，單周上漲837.70點，漲幅約1.73%，站上4萬9千點大關，據證交所資料，外資上...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E7%98%8B%E6%90%B6%E4%B8%BB%E5%8B%95%E5%BC%8F-%E9%80%99%E6%AA%94-%E5%88%B7%E6%8E%9B%E7%89%8C%E4%BB%A5%E4%BE%86%E6%96%B0%E9%AB%98%E5%83%B9-%E5%A4%96%E8%B3%87%E6%8E%83%E5%85%A5%E9%80%BE6-5%E8%90%AC%E5%BC%B5-103000190.html
- 事件3：新北義民祭登場   侯友宜率千人挑擔   青年親子吉祥物創意踩街
  - 來源：Yahoo 台股；發布時間：2026-10-11T09:52:35Z；台北時間：2026-10-11 17:52
  - 摘要：《圖說》市長侯友宜率鄉親們挑擔奉飯進入會場，前排藍背心者為議長蔣根煌。〈客家局提供〉 【記者葉柏成／新北報導】 […]
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E5%8C%97%E7%BE%A9%E6%B0%91%E7%A5%AD%E7%99%BB%E5%A0%B4-%E4%BE%AF%E5%8F%8B%E5%AE%9C%E7%8E%87%E5%8D%83%E4%BA%BA%E6%8C%91%E6%93%94-%E9%9D%92%E5%B9%B4%E8%A6%AA%E5%AD%90%E5%90%89%E7%A5%A5%E7%89%A9%E5%89%B5%E6%84%8F%E8%B8%A9%E8%A1%97-095235843.html
- 事件4：只會存錢真的吃虧嗎？「每月1萬元」對比0050、台積電　網友曝兩派不同答案
  - 來源：Yahoo 台股；發布時間：2026-10-11T07:05:00Z；台北時間：2026-10-11 15:05
  - 摘要：[FTNN新聞網]實習記者盛琳／綜合報導台股多頭氣勢如虹，隨著指數屢創新高，儲蓄與投資的財富差距也成為網路發燒話題。近日一名網友在社群平台Threads吐露焦慮...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%AA%E6%9C%83%E5%AD%98%E9%8C%A2%E7%9C%9F%E7%9A%84%E5%90%83%E8%99%A7%E5%97%8E-%E6%AF%8F%E6%9C%881%E8%90%AC%E5%85%83-%E5%B0%8D%E6%AF%940050-%E5%8F%B0%E7%A9%8D%E9%9B%BB-%E7%B6%B2%E5%8F%8B%E6%9B%9D%E5%85%A9%E6%B4%BE%E4%B8%8D%E5%90%8C%E7%AD%94%E6%A1%88-070500932.html
- 事件5：市值型股息拿來買月配ETF？他想「市值型紅利、高股息股利」通吃　投資人揭盲點
  - 來源：Yahoo 台股；發布時間：2026-10-11T06:50:00Z；台北時間：2026-10-11 14:50
  - 摘要：[FTNN新聞網]實習記者周宗怡／綜合報導對剛出社會的新鮮人來說，如何在累積資產的同時，也打造穩定的被動收入，是不少投資人關注的課題。有網友打算先將資金...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%B8%82%E5%80%BC%E5%9E%8B%E8%82%A1%E6%81%AF%E6%8B%BF%E4%BE%86%E8%B2%B7%E6%9C%88%E9%85%8Detf-%E4%BB%96%E6%83%B3-%E5%B8%82%E5%80%BC%E5%9E%8B%E7%B4%85%E5%88%A9-%E9%AB%98%E8%82%A1%E6%81%AF%E8%82%A1%E5%88%A9-%E9%80%9A%E5%90%83-065000511.html
- 事件6：新北客家義民文化祭登場  挑擔奉飯重現先民慰勞義民軍的文化記憶
  - 來源：Yahoo 台股；發布時間：2026-10-11T06:09:13Z；台北時間：2026-10-11 14:09
  - 摘要：「2026客家義民爺文化祭—義起挺新北」活動今（11）日邁入第2天，重頭戲「挑擔奉飯創意踩街」熱鬧登場。新北市長侯友宜等人共同挑起飯擔繞行市民廣場，結合表演和吉祥物玩偶遊行，重現客家先民奉飯慰勞義民軍的文化記憶，展現感恩、分享與團結互助的義
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E5%8C%97%E5%AE%A2%E5%AE%B6%E7%BE%A9%E6%B0%91%E6%96%87%E5%8C%96%E7%A5%AD%E7%99%BB%E5%A0%B4-%E6%8C%91%E6%93%94%E5%A5%89%E9%A3%AF%E9%87%8D%E7%8F%BE%E5%85%88%E6%B0%91%E6%85%B0%E5%8B%9E%E7%BE%A9%E6%B0%91%E8%BB%8D%E7%9A%84%E6%96%87%E5%8C%96%E8%A8%98%E6%86%B6-060913114.html
- 事件7：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into the economic condition of American families
  - 來源：Federal Reserve；發布時間：Fri, 9 Oct 2026 14:00:00 GMT；台北時間：2026-10-09 22:00
  - 摘要：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261009a.htm
- 事件8：Federal Reserve Board announces enforcement action against American Express Company to address, among other things, the firmâs failure to sufficiently detect and report certain suspicious activity related to money laundering
  - 來源：Federal Reserve；發布時間：Thu, 8 Oct 2026 20:30:00 GMT；台北時間：2026-10-09 04:30
  - 摘要：Federal Reserve Board announces enforcement action against American Express Company to address, among other things, the firmâs failure to sufficient
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261008a.htm
- 事件9：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 來源：Federal Reserve；發布時間：Wed, 7 Oct 2026 18:00:00 GMT；台北時間：2026-10-08 02:00
  - 摘要：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261007a.htm
- 事件10：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 來源：Federal Reserve；發布時間：Mon, 5 Oct 2026 20:30:00 GMT；台北時間：2026-10-06 04:30
  - 摘要：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261005a.htm
- 事件11：Trump created a committee to dig into the Fed's Lisa Cook. What is it and what comes next?
  - 來源：CNBC；發布時間：Fri, 09 Oct 2026 19:19:00 GMT；台北時間：2026-10-10 03:19
  - 摘要：Trump’s bid to fire the Fed's Lisa Cook follows a Supreme Court ruling and could affect Jerome Powell, central bank independence and interest rates.
  - 原文連結：https://www.cnbc.com/2026/10/09/trump-lisa-cook-fed-firing-committee-explained.html
- 事件12：Americans' debt problems are flashing a warning not seen since the Great Recession
  - 來源：CNBC；發布時間：Fri, 09 Oct 2026 19:18:24 GMT；台北時間：2026-10-10 03:18
  - 摘要：Researchers found that while wealth disparities narrowed somewhat, the ability to meet debt payments deteriorated significantly.
  - 原文連結：https://www.cnbc.com/2026/10/09/american-debt-delinquency.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-08

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,480 | TAIFEX Proxy |
| 最高價 | 49,692 | TAIFEX Proxy |
| 最低價 | 49,333 | TAIFEX Proxy |
| 收盤價 | 49,349 | TAIFEX Proxy |
| 漲跌點數 | -619 | TAIFEX Proxy |
| 漲跌幅 | -1.24 | TAIFEX Proxy |
| 成交量 | 65,345 | TAIFEX Proxy |
| 日盤高點及低點 | 49,692 / 49,333 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,946 | TAIFEX Proxy |
| 最高價 | 49,946 | TAIFEX Proxy |
| 最低價 | 49,253 | TAIFEX Proxy |
| 收盤價 | 49,593 | TAIFEX Proxy |
| 漲跌點數 | -375 | TAIFEX Proxy |
| 漲跌幅 | -0.75 | TAIFEX Proxy |
| 成交量 | 29,306 | TAIFEX Proxy |
| 夜盤高點及低點 | 49,946 / 49,253 | TAIFEX Proxy |
| 結算價 | 49,357 | TAIFEX Proxy |
| 未平倉量 | 107,859 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,389 | TAIFEX Proxy |
| 外資空方 OI | 94,583 | TAIFEX Proxy |
| 外資多空淨 OI | -83,194 | TAIFEX Proxy |
| 投信多方 OI | 79,091 | TAIFEX Proxy |
| 投信空方 OI | 2,752 | TAIFEX Proxy |
| 投信多空淨 OI | +76,339 | TAIFEX Proxy |
| 自營商多方 OI | 3,930 | TAIFEX Proxy |
| 自營商空方 OI | 4,464 | TAIFEX Proxy |
| 自營商多空淨 OI | -534 | TAIFEX Proxy |
| 三大法人合計多方 OI | 94,410 | TAIFEX Proxy |
| 三大法人合計空方 OI | 101,799 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,389 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -4,093 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +71 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,719 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,609 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,985 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,624 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-06→2026-10-08) | -1,488 | TAIFEX Proxy snapshots (2026-10-07) |
- 資料日期：2026-10-08 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 34,332 | TAIFEX Proxy |
| 外資日盤空單交易量 | 38,380 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,048 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 21,414 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 21,210 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +204 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -4,252 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +71 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +71 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,819 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +677 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,142 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,158 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +881 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -213.9 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +85.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 49,349 | TAIFEX Proxy |
| 加權指數價格 | 49,313.44 | twse-proxy |
| 台指期與加權指數價差 | +35.56 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.07 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +35.56 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +244 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 49,349 | 49,593 | -244 | TAIFEX Proxy |
| 成交量 | 36,039 | 29,306 | +6,733 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,303（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 34,332 | 38,380 | -4,048 | 21,414 | 21,210 | +204 | -4,252 | 11,389 | 94,583 | -83,194 | -4,093 | TAIFEX Proxy |
| 投信 | 350 | 279 | +71 | 0 | 0 | +0 | +71 | 79,091 | 2,752 | +76,339 | +71 | TAIFEX Proxy |
| 自營商 | 4,907 | 3,088 | +1,819 | 1,547 | 870 | +677 | +1,142 | 3,930 | 4,464 | -534 | +1,719 | TAIFEX Proxy |
| 三大法人合計 | 39,589 | 41,747 | -2,158 | 22,961 | 22,080 | +881 | -3,039 | 94,410 | 101,799 | -7,389 | -2,303 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,609 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,985 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,624 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-06→2026-10-08) | -1,488 | TAIFEX Proxy snapshots (2026-10-07) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 44.85% | TAIFEX Proxy |
| 夜盤漲跌點數 | -375 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +204 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-08 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-12 08:18:56 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 135,324 | TAIFEX Proxy |
| Call 總未平倉量 OI | 42,268 | TAIFEX Proxy |
| Call OI 增減 (2026-10-07→2026-10-08) | +21,873 | TAIFEX Proxy snapshots (2026-10-07) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 118,524 | TAIFEX Proxy |
| Put 總未平倉量 OI | 26,761 | TAIFEX Proxy |
| Put OI 增減 (2026-10-07→2026-10-08) | +15,679 | TAIFEX Proxy snapshots (2026-10-07) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.14 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.58 | TAIFEX Proxy |
| Put／Call Ratio | 0.63 | TAIFEX Proxy |
| Call／Put 比例變化 | -7.43 | TAIFEX Proxy |
| 與前一交易日比較 | -2.07 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX OpenAPI PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 43,034 | TAIFEX Proxy |
| 外資 Call日賣 | 42,839 | TAIFEX Proxy |
| 外資 Call日淨 | +195 | TAIFEX Proxy |
| 外資 Put日買 | 48,026 | TAIFEX Proxy |
| 外資 Put日賣 | 47,126 | TAIFEX Proxy |
| 外資 Put日淨 | +900 | TAIFEX Proxy |
| 外資 Call夜買 | 25,966 | TAIFEX Proxy |
| 外資 Call夜賣 | 25,824 | TAIFEX Proxy |
| 外資 Call夜淨 | +142 | TAIFEX Proxy |
| 外資 Put夜買 | 35,905 | TAIFEX Proxy |
| 外資 Put夜賣 | 35,509 | TAIFEX Proxy |
| 外資 Put夜淨 | +396 | TAIFEX Proxy |
| 外資 日盤淨總量 | -705 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +53 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +504 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 40,083 | TAIFEX Proxy |
| 自營商 Call日賣 | 42,039 | TAIFEX Proxy |
| 自營商 Call日淨 | -1,956 | TAIFEX Proxy |
| 自營商 Put日買 | 33,390 | TAIFEX Proxy |
| 自營商 Put日賣 | 33,124 | TAIFEX Proxy |
| 自營商 Put日淨 | +266 | TAIFEX Proxy |
| 自營商 Call夜買 | 19,775 | TAIFEX Proxy |
| 自營商 Call夜賣 | 24,243 | TAIFEX Proxy |
| 自營商 Call夜淨 | -4,468 | TAIFEX Proxy |
| 自營商 Put夜買 | 24,241 | TAIFEX Proxy |
| 自營商 Put夜賣 | 23,805 | TAIFEX Proxy |
| 自營商 Put夜淨 | +436 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -2,222 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,512 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -170 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 53,400 | 3,632 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,000 | 2,080 | TAIFEX Proxy |
| Call OI 第3大履約價 | 53,000 | 1,757 | TAIFEX Proxy |
| Call OI 最大履約價 | 53,400 | 3,632 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 53,400 | 3,632 | 8.59% | TAIFEX Proxy |
| C2 | 50,000 | 2,080 | 4.92% | TAIFEX Proxy |
| C3 | 53,000 | 1,757 | 4.16% | TAIFEX Proxy |
| C4 | 51,200 | 1,666 | 3.94% | TAIFEX Proxy |
| C5 | 50,400 | 1,439 | 3.4% | TAIFEX Proxy |
| C6 | 50,500 | 1,409 | 3.33% | TAIFEX Proxy |
| C7 | 48,000 | 1,401 | 3.31% | TAIFEX Proxy |
| C8 | 52,500 | 1,381 | 3.27% | TAIFEX Proxy |
| C9 | 50,200 | 1,372 | 3.25% | TAIFEX Proxy |
| C10 | 51,000 | 1,172 | 2.77% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,000 | 1,544 | TAIFEX Proxy |
| Put OI 第2大履約價 | 49,400 | 1,517 | TAIFEX Proxy |
| Put OI 第3大履約價 | 49,500 | 1,360 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,000 | 1,544 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,000 | 1,544 | 5.77% | TAIFEX Proxy |
| P2 | 49,400 | 1,517 | 5.67% | TAIFEX Proxy |
| P3 | 49,500 | 1,360 | 5.08% | TAIFEX Proxy |
| P4 | 48,000 | 1,337 | 5.0% | TAIFEX Proxy |
| P5 | 48,500 | 1,187 | 4.44% | TAIFEX Proxy |
| P6 | 49,300 | 1,121 | 4.19% | TAIFEX Proxy |
| P7 | 48,200 | 816 | 3.05% | TAIFEX Proxy |
| P8 | 48,800 | 747 | 2.79% | TAIFEX Proxy |
| P9 | 49,200 | 736 | 2.75% | TAIFEX Proxy |
| P10 | 48,900 | 692 | 2.59% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 50,000 (+1,665) | TAIFEX Proxy snapshots (2026-10-07) |
| Call OI 減少最多的履約價 | 51,050 (-149) | TAIFEX Proxy snapshots (2026-10-07) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,400 (+1,266) | TAIFEX Proxy snapshots (2026-10-07) |
| Put OI 減少最多的履約價 | 49,700 (-23) | TAIFEX Proxy snapshots (2026-10-07) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 53,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-07→2026-10-08) | +3,400 | TAIFEX Proxy snapshots (2026-10-07) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-07→2026-10-08) | -600 | TAIFEX Proxy snapshots (2026-10-07) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 50,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-08 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 49,226.14 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-08 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 49,200 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-07→2026-10-08) | -450 | TAIFEX Proxy snapshots (2026-10-07) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 90,160 | 90,865 | -705 | 61,475 | 61,729 | -254 | -451 | TAIFEX Proxy |
| 投信 | 0 | 1,160 | -1,160 | 0 | 0 | +0 | -1,160 | TAIFEX Proxy |
| 自營商 | 73,207 | 75,429 | -2,222 | 43,580 | 48,484 | -4,904 | +2,682 | TAIFEX Proxy |
| 三大法人合計 | 163,367 | 167,454 | -4,087 | 105,055 | 110,213 | -5,158 | +1,071 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 8.46 | 8.53 | -0.07 | 4.81 | 4.87 | -0.05 | -0.01 | TAIFEX Proxy |
| 投信 | 0.00 | 0.77 | -0.77 | 0.00 | 0.00 | +0 | -0.77 | TAIFEX Proxy |
| 自營商 | 6.93 | 6.84 | +0.09 | 3.72 | 4.07 | -0.36 | +0.45 | TAIFEX Proxy |
| 三大法人合計 | 15.39 | 16.13 | -0.75 | 8.53 | 8.94 | -0.41 | -0.33 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,045 | TAIFEX Proxy |
| 買權空方 OI | 12,523 | TAIFEX Proxy |
| 買權多空淨 OI | +1,522 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-06→2026-10-08) | +227 | TAIFEX Proxy snapshots (2026-10-07) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,630 | TAIFEX Proxy |
| 賣權空方 OI | 10,536 | TAIFEX Proxy |
| 賣權多空淨 OI | +94 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-06→2026-10-08) | +577 | TAIFEX Proxy snapshots (2026-10-07) |
- 資料日期：買權 2026-10-08／賣權 2026-10-08 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,488 | 2026-10-06→2026-10-08 | TAIFEX Proxy snapshots (2026-10-07) |
| 買權前十大 | +227 | 2026-10-06→2026-10-08 | TAIFEX Proxy snapshots (2026-10-07) |
| 賣權前十大 | +577 | 2026-10-06→2026-10-08 | TAIFEX Proxy snapshots (2026-10-07) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-08；資料時間：2026-10-12 08:18:56；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：2 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (0)：無
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-10-09，非 T0 2026-10-08)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
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
| 外資 | -758.5 | -83,194 | -4,048 | +204 | -705 | -254 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +30.1 | +76,339 | +71 | +0 | -1,160 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -187.3 | -534 | +1,819 | +677 | -2,222 | -4,904 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
