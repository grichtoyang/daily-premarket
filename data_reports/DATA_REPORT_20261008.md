# DATA_REPORT_20261008

- 報告日期：`2026-10-08`
- T0 交易日期：`2026-10-08`
- 資料產出時間：`2026-10-08 19:16:01`
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
| 投信 | +46.9 | 億元 | twse-proxy /institutional |
| 自營商 | -187.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -899.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 215,104 | 張 | HiStock |
| 融券增減 | 3,168 | 張 | HiStock |
| 融資維持率 | 199.17 | % | 前值遞補 (DATA 2026-10-07；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,402,952 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

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
| S&P 500 | ^GSPC | 7,801.77 | -17.16 | -0.22 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,538.69 | -61.10 | -0.22 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 31,160.08 | -64.39 | -0.21 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,179.87 | -341.41 | -0.66 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 13,066.15 | -151.67 | -1.15 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.96 | 0.88 | +5.84 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 69,042.11 | -993.60 | -1.42 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,625.93 | -177.97 | -2.62 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,785.79 | -344.71 | -1.43 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,811.90 | -30.29 | -0.79 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,620.90 | -266.72 | -2.07 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,806.00 | -46.75 | -0.60 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 31,136.25 | -266.00 | -0.85 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,915.00 | -534.00 | -1.04 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,780.50 | -31.70 | -1.13 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.77 | -0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.28 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.66 | 0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.96 | 0.18 | +0.58 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.44 | 0.20 | +0.19 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.25 | -0.04 | -0.03 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,344.78 | 5.04 | +0.38 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 472.20 | -10.10 | -2.09 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 23.31 | 0.12 | +0.52 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 45.76 | -1.02 | -2.18 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 92.71 | 4.43 | +5.02 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,139.40 | -1.30 | -0.03 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 82,315.62 | -960.31 | -1.15 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：外資國慶前翻臉權值股沒電 台塑被動元件自帶火力開趴
  - 來源：Yahoo 台股；發布時間：2026-10-08T09:06:57Z；台北時間：2026-10-08 17:06
  - 摘要：國慶行情變調，外資賣壓出籠，台股失守5日線！今(8)日加權指數終場走跌492.93點、跌幅0.99%，收49,313.44點，本周仍上漲837.7點、周線連四紅，成交金額8721.09億元。在美債殖利率攀升、美股回檔，加上連假前資金調節，壓
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%9C%8B%E6%85%B6%E5%89%8D%E8%AE%8A%E8%87%89%E5%8F%B0%E8%82%A1%E6%91%94%E7%A0%B4%E4%BA%94%E6%97%A5%E7%B7%9A%EF%BC%81%E6%AC%8A%E5%80%BC%E8%82%A1%E8%BB%9F%E8%85%B3-%E5%8F%B0%E5%A1%91%E9%9B%86%E5%9C%98%E6%8F%AA%E8%A2%AB%E5%8B%95%E5%85%83%E4%BB%B6%E7%95%B6%E6%8A%97%E8%B7%8C%E5%A4%A7%E9%9A%8A-%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090657722.html
- 事件2：167萬股民嗨翻！「這國民ETF」霸氣配1.72元創高、外資不賞臉提款3.9億　再砍00992A超6千張
  - 來源：Yahoo 台股；發布時間：2026-10-08T10:30:00Z；台北時間：2026-10-08 18:30
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導台股今（8）日開低走低，終場收49313.44點，大跌492.93點，跌幅0.99%，成交額8721.09億元。根據證交所盤後公布籌碼動向，外...
  - 原文連結：https://tw.stock.yahoo.com/news/167%E8%90%AC%E8%82%A1%E6%B0%91%E5%97%A8%E7%BF%BB-%E9%80%99%E5%9C%8B%E6%B0%91etf-%E9%9C%B8%E6%B0%A3%E9%85%8D1-72%E5%85%83%E5%89%B5%E9%AB%98-%E5%A4%96%E8%B3%87%E4%B8%8D%E8%B3%9E%E8%87%89%E6%8F%90%E6%AC%BE3-103000909.html
- 事件3：證交所第23屆「校園證券投資智慧王」競賽報名囉　冠軍隊獨得12萬
  - 來源：Yahoo 台股；發布時間：2026-10-08T05:34:07Z；台北時間：2026-10-08 13:34
  - 摘要：為持續深化校園投資人教育，協助年輕世代建立正確的投資觀念與風險意識，證券交易所舉辦第23屆「校園證券投資智慧王」競賽活動，即日起開放全國大專院校學生組隊報名。本屆總獎金超過80萬元，總決賽冠軍隊伍可獨得12萬元獎金，邀請不同科系學生跨域組隊
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%AD%89%E4%BA%A4%E6%89%80%E7%AC%AC23%E5%B1%86-%E6%A0%A1%E5%9C%92%E8%AD%89%E5%88%B8%E6%8A%95%E8%B3%87%E6%99%BA%E6%85%A7%E7%8E%8B-%E7%AB%B6%E8%B3%BD%E5%A0%B1%E5%90%8D%E5%9B%89-%E5%86%A0%E8%BB%8D%E9%9A%8A%E7%8D%A8%E5%BE%9712%E8%90%AC-053407310.html
- 事件4：31歲股票資產破2600萬！他「4檔ETF帳賺逾千萬」想退休
  - 來源：Yahoo 台股；發布時間：2026-10-08T05:08:55Z；台北時間：2026-10-08 13:08
  - 摘要：靠存股累積資產是不少投資人的目標，一名31歲網友近日在Dcard曬出投資成果，持有0050、0056、00713及00878等4檔ETF，股票市值已達2699.1萬元，整體帳面獲利超過1034萬元、報酬率62.35%，並透露目前每月股利約7
  - 原文連結：https://tw.stock.yahoo.com/news/31%E6%AD%B2%E8%82%A1%E7%A5%A8%E8%B3%87%E7%94%A2%E7%A0%B42600%E8%90%AC-%E4%BB%96-4%E6%AA%94etf%E5%B8%B3%E8%B3%BA%E9%80%BE%E5%8D%83%E8%90%AC-%E6%83%B3%E9%80%80%E4%BC%91-050855800.html
- 事件5：被動元件慘回檔！華新科噴43%後急殺6%拖國巨、蜜望實下挫　惟「這2檔」連拉2根漲停
  - 來源：Yahoo 台股；發布時間：2026-10-08T02:45:00Z；台北時間：2026-10-08 10:45
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導受累於台積電（2330）、聯發科（2454）、台達電（2308）等權值股齊下行，台股大盤今（8）日走低，截至10點17分，加權指數暫...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%A2%AB%E5%8B%95%E5%85%83%E4%BB%B6%E6%85%98%E5%9B%9E%E6%AA%94-%E8%8F%AF%E6%96%B0%E7%A7%91%E5%99%B443-%E5%BE%8C%E6%80%A5%E6%AE%BA6-%E6%8B%96%E5%9C%8B%E5%B7%A8-%E8%9C%9C%E6%9C%9B%E5%AF%A6%E4%B8%8B%E6%8C%AB-024500627.html
- 事件6：台積電股利入帳！最大股東 不到1個月「帳上增值破3500億元」
  - 來源：Yahoo 台股；發布時間：2026-10-08T02:39:06Z；台北時間：2026-10-08 10:39
  - 摘要：台積電（2330）今（8）日發放股利，自 9 月除息以來，台積電上漲205元（算到昨日收盤價），相當於持有一張帳上就增值 20.5 萬元。最大股東國發基金不僅115.7 億元股息入帳，帳上股價增值更達3,390億元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E8%82%A1%E5%88%A9%E5%85%A5%E5%B8%B3%EF%BC%81%E6%9C%80%E5%A4%A7%E8%82%A1%E6%9D%B1-%E4%B8%8D%E5%88%B01%E5%80%8B%E6%9C%88%E3%80%8C%E5%B8%B3%E4%B8%8A%E5%A2%9E%E5%80%BC%E7%A0%B43500%E5%84%84%E5%85%83%E3%80%8D-023906209.html
- 事件7：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 來源：Federal Reserve；發布時間：Wed, 7 Oct 2026 18:00:00 GMT；台北時間：2026-10-08 02:00
  - 摘要：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261007a.htm
- 事件8：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 來源：Federal Reserve；發布時間：Mon, 5 Oct 2026 20:30:00 GMT；台北時間：2026-10-06 04:30
  - 摘要：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261005a.htm
- 事件9：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:45:00 GMT；台北時間：2026-10-03 04:45
  - 摘要：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261002a.htm
- 事件10：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:00:00 GMT；台北時間：2026-10-03 04:00
  - 摘要：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261002a.htm
- 事件11：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 15:00:00 GMT；台北時間：2026-10-02 23:00
  - 摘要：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261002a.htm
- 事件12：Americans grow more pessimistic about their finances, New York Fed finds — expert warns of ‘tough choices’ ahead
  - 來源：CNBC；發布時間：Wed, 07 Oct 2026 19:40:31 GMT；台北時間：2026-10-08 03:40
  - 摘要：As affordability pressures mount, Americans are increasingly concerned about their financial future, the New York Fed's data shows.
  - 原文連結：https://www.cnbc.com/2026/10/07/new-york-fed-financial-outlook-inflation.html


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
| 前十大交易人多方 OI | 84,587 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,045 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,542 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-06→2026-10-07) | +1,430 | TAIFEX Proxy snapshots (2026-10-07) |
- 資料日期：2026-10-07 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 34,332 | TAIFEX Proxy |
| 外資日盤空單交易量 | 38,380 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,048 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 14,000 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,794 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -2,794 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,254 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +71 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +71 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,819 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +998 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +821 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,158 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,796 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -213.9 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -178.0 | TAIFEX Proxy |

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
| 外資 | 34,332 | 38,380 | -4,048 | 14,000 | 16,794 | -2,794 | -1,254 | 11,389 | 94,583 | -83,194 | -4,093 | TAIFEX Proxy |
| 投信 | 350 | 279 | +71 | 0 | 0 | +0 | +71 | 79,091 | 2,752 | +76,339 | +71 | TAIFEX Proxy |
| 自營商 | 4,907 | 3,088 | +1,819 | 1,696 | 698 | +998 | +821 | 3,930 | 4,464 | -534 | +1,719 | TAIFEX Proxy |
| 三大法人合計 | 39,589 | 41,747 | -2,158 | 15,696 | 17,492 | -1,796 | -362 | 94,410 | 101,799 | -7,389 | -2,303 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 84,587 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,045 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +7,542 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-06→2026-10-07) | +1,430 | TAIFEX Proxy snapshots (2026-10-07) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 44.85% | TAIFEX Proxy |
| 夜盤漲跌點數 | -375 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -2,794 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-08 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-08 19:16:01 | 本機 |
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
| Call／Put 比例變化 (量比 2026-10-06→2026-10-07) | -13.34 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-06→2026-10-07) | -13.22 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 43,034 | TAIFEX Proxy |
| 外資 Call日賣 | 42,839 | TAIFEX Proxy |
| 外資 Call日淨 | +195 | TAIFEX Proxy |
| 外資 Put日買 | 48,026 | TAIFEX Proxy |
| 外資 Put日賣 | 47,126 | TAIFEX Proxy |
| 外資 Put日淨 | +900 | TAIFEX Proxy |
| 外資 Call夜買 | 23,465 | TAIFEX Proxy |
| 外資 Call夜賣 | 23,340 | TAIFEX Proxy |
| 外資 Call夜淨 | +125 | TAIFEX Proxy |
| 外資 Put夜買 | 22,134 | TAIFEX Proxy |
| 外資 Put夜賣 | 22,076 | TAIFEX Proxy |
| 外資 Put夜淨 | +58 | TAIFEX Proxy |
| 外資 日盤淨總量 | -705 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +70 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +842 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 40,083 | TAIFEX Proxy |
| 自營商 Call日賣 | 42,039 | TAIFEX Proxy |
| 自營商 Call日淨 | -1,956 | TAIFEX Proxy |
| 自營商 Put日買 | 33,390 | TAIFEX Proxy |
| 自營商 Put日賣 | 33,124 | TAIFEX Proxy |
| 自營商 Put日淨 | +266 | TAIFEX Proxy |
| 自營商 Call夜買 | 13,388 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,266 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,878 | TAIFEX Proxy |
| 自營商 Put夜買 | 13,633 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,608 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,025 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -2,222 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,922 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -759 | TAIFEX Proxy |

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
| Gamma Wall 價位 | 49,300.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-07 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 49,585.51 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-07 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 49,200 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-07→2026-10-08) | -450 | TAIFEX Proxy snapshots (2026-10-07) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 90,160 | 90,865 | -705 | 45,541 | 45,474 | +67 | -772 | TAIFEX Proxy |
| 投信 | 0 | 1,160 | -1,160 | 0 | 0 | +0 | -1,160 | TAIFEX Proxy |
| 自營商 | 73,207 | 75,429 | -2,222 | 25,996 | 30,899 | -4,903 | +2,681 | TAIFEX Proxy |
| 三大法人合計 | 163,367 | 167,454 | -4,087 | 71,537 | 76,373 | -4,836 | +749 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 8.46 | 8.53 | -0.07 | 4.14 | 4.14 | -0.00 | -0.06 | TAIFEX Proxy |
| 投信 | 0.00 | 0.77 | -0.77 | 0.00 | 0.00 | +0 | -0.77 | TAIFEX Proxy |
| 自營商 | 6.93 | 6.84 | +0.09 | 2.61 | 3.18 | -0.57 | +0.66 | TAIFEX Proxy |
| 三大法人合計 | 15.39 | 16.13 | -0.75 | 6.75 | 7.33 | -0.57 | -0.17 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,110 | TAIFEX Proxy |
| 買權空方 OI | 12,403 | TAIFEX Proxy |
| 買權多空淨 OI | +1,707 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-06→2026-10-07) | +412 | TAIFEX Proxy snapshots (2026-10-07) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,123 | TAIFEX Proxy |
| 賣權空方 OI | 10,076 | TAIFEX Proxy |
| 賣權多空淨 OI | +47 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-06→2026-10-07) | +530 | TAIFEX Proxy snapshots (2026-10-07) |
- 資料日期：買權 2026-10-07／賣權 2026-10-07 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,430 | 2026-10-06→2026-10-07 | TAIFEX Proxy snapshots (2026-10-07) |
| 買權前十大 | +412 | 2026-10-06→2026-10-07 | TAIFEX Proxy snapshots (2026-10-07) |
| 賣權前十大 | +530 | 2026-10-06→2026-10-07 | TAIFEX Proxy snapshots (2026-10-07) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-08；資料時間：2026-10-08 19:16:01；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg
- 註記：Gamma 資料日期 2026-10-07 (T0 2026-10-08 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-07 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-07；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-07)，非 T0 2026-10-08
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -758.5 | -83,194 | -4,048 | -2,794 | -705 | +67 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +46.9 | +76,339 | +71 | +0 | -1,160 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -187.3 | -534 | +1,819 | +998 | -2,222 | -4,903 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
