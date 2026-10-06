# DATA_REPORT_20261005

- 報告日期：`2026-10-06`
- T0 交易日期：`2026-10-05`
- 資料產出時間：`2026-10-06 08:40:58`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,712.04 | 點 | twse-proxy |
| 開盤 | 48,574.95 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,770.66 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,574.95 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,712.04 | 點 | twse-proxy |
| 漲跌點數 | 1,236.30 | 點 | twse-proxy |
| 漲跌幅 | +2.55 | % | twse-proxy |
| 成交金額 | 12,110.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 364 | twse-proxy |
| 下跌家數 | 631 | twse-proxy |
| 平盤家數 | 87 | twse-proxy |
| 漲停家數 | 27 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 296 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 499 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 76 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 22 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +719.0 | 億元 | twse-proxy /institutional |
| 投信 | -52.9 | 億元 | twse-proxy /institutional |
| 自營商 | +109.5 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +775.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,575.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +8.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 254,968 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -14,794 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 200.67 | % | istock 大盤融資維持率 (資料日期 2026-10-05；T0當日；補登；wantgoo 最新為 10-02 值 197.07；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,497,033 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,510 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,266 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 12,110.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 3,213.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 15,324.3 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,773.95 | 51.23 | +0.66 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,477.31 | 286.45 | +1.05 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 31,076.44 | 268.51 | +0.87 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,267.90 | 90.94 | +0.18 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 13,172.74 | 36.07 | +0.27 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.52 | 0.21 | +1.37 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 70,161.82 | 1,852.36 | +2.71 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,004.14 | 0.40 | +0.01 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,972.29 | -640.98 | -2.60 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,834.25 | 57.00 | +0.73 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 31,378.25 | 316.50 | +1.02 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,601.00 | 124.00 | +0.24 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,868.90 | 18.00 | +0.63 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.84 | 0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.31 | 0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.66 | 0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.76 | -0.07 | -0.23 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.16 | 0.23 | +0.23 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.87 | 0.14 | +0.09 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.48 | -0.08 | -0.01 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 472.78 | 13.58 | +2.96 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 26.27 | 1.06 | +4.20 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.45 | 2.72 | +6.08 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 89.39 | -1.72 | -1.89 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,171.40 | 9.10 | +0.22 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 85,803.69 | -676.62 | -0.78 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：5個月內二度來台 蘇姿丰找台積也要鞏固後段供應鏈
  - 來源：Yahoo 台股；發布時間：2026-10-05T22:00:00Z；台北時間：2026-10-06 06:00
  - 摘要：超微（AMD）執行長蘇姿丰5日搭乘專機抵達台北松山機場，距離上次訪台不到5個月，又親自飛來台灣。據悉，AMD下半年量產MI450系列AI平台，MI455明年上半年緊接著上陣，蘇姿丰這趟從台積電一路追到封測、載板及AI伺服器代工廠，提前卡位2
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E5%A5%B3%E7%8E%8B%E5%BF%AB%E9%96%831-%E8%98%87%E5%A7%BF%E4%B8%B05%E5%80%8B%E6%9C%882%E5%BA%A6%E4%BE%86%E5%8F%B0-amd%E5%BE%9E%E5%8F%B0%E7%A9%8D%E9%9B%BB-%E8%B7%AF%E6%90%B6%E5%88%B0%E5%B0%81%E6%B8%AC-%E8%BC%89%E6%9D%BF-220000949.html
- 事件2：景碩本益比203倍、禾伸堂當沖占比逾6成 全列注意股
  - 來源：Yahoo 台股；發布時間：2026-10-06T00:00:00Z；台北時間：2026-10-06 08:00
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導台股加權指數昨（5）日開高直奔4萬9大關，盤中一度衝上49770點，最終以49712.04點作收，上揚1236.3點，漲幅2.55%，成交金額...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%A2%AB%E5%8B%95%E5%85%83%E4%BB%B6%E6%8C%81%E7%BA%8C%E7%99%BC%E7%87%99-%E8%8F%AF%E6%96%B0%E7%A7%91%E8%88%87-%E9%80%99%E5%A4%A7%E5%BB%A0-%E8%A2%AB%E6%89%93%E5%85%A5%E6%B3%A8%E6%84%8F%E8%82%A1-%E5%B7%9D%E6%B9%96%E9%80%A3%E5%90%8C%E8%BC%89%E6%9D%BF%E4%B8%89%E9%9B%84-000000162.html
- 事件3：郭哲榮怒批聯發科「高層亂搞事情」揚言不改善將賣股
  - 來源：Yahoo 台股；發布時間：2026-10-05T16:04:00Z；台北時間：2026-10-06 00:04
  - 摘要：知名財經投資長郭哲榮日前在節目中深度剖析科技巨頭AI政策差異，指出輝達每月提供員工高達2萬美元的AI Token額度，讓員工能全力運用AI輔助開發；反觀聯發科卻傳出大幅縮減額度，一天僅提供約2.2美元，引發工程師強烈不滿。郭哲榮痛批聯發科高
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%83%AD%E5%93%B2%E6%A6%AE%E5%96%8A-%E5%87%BA%E6%B8%85%E8%81%AF%E7%99%BC%E7%A7%91%E6%8C%81%E8%82%A1-%E6%80%92%E6%89%B9%E9%AB%98%E5%B1%A4%E4%BA%82%E6%90%9E%E4%BA%8B%E6%83%85-%E4%B8%8D%E6%94%B9%E9%80%99%E5%85%AC%E5%8F%B8%E6%B2%92%E6%95%91%E4%BA%86-160400522.html
- 事件4：美股4大指數收高、那指登峰 SpaceX飆逾7%
  - 來源：Yahoo 台股；發布時間：2026-10-05T21:38:59Z；台北時間：2026-10-06 05:38
  - 摘要：科技股領漲，美股三大指數週一收高，那指創收盤與盤中新高 10年期美債殖利率升至5.311%，市場憂通膨高檔、Fed將維持高利率 ISM 9月服務業PMI 54.9%，油價下跌；9月會議紀錄將成後續政策焦點
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E7%9B%A4%E5%BE%8C-%E7%84%A1%E8%A6%96%E7%BE%8E%E5%82%B5%E8%B3%A3%E5%A3%93-ai%E6%A6%82%E5%BF%B5%E8%82%A1%E7%8B%82%E6%AD%A1-%E9%82%A3%E6%8C%87%E7%B7%A0%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98%E7%B4%80%E9%8C%84-213859719.html
- 事件5：15檔個股連續兩天創歷史新高 不是繼續軋空就是回檔
  - 來源：Yahoo 台股；發布時間：2026-10-05T23:13:18Z；台北時間：2026-10-06 07:13
  - 摘要：欣興、景碩、南電都是走AI需求暴增題材，景碩若算從今年1月起漲的話，至今已上漲...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%89%B5%E6%96%B0%E9%AB%98-%E9%80%9915%E6%AA%94%E5%80%8B%E8%82%A1%E9%80%A3%E7%BA%8C%E5%85%A9%E5%A4%A9%E5%89%B5%E6%AD%B7%E5%8F%B2%E6%96%B0%E9%AB%98-%E9%80%B1%E4%BA%8C%E4%B8%8D%E6%98%AF%E7%B9%BC%E7%BA%8C%E8%BB%8B%E7%A9%BA%E5%B0%B1%E6%98%AF%E5%9B%9E%E6%AA%94-231318028.html
- 事件6：乖乖工會發動無限期罷工　董座提補償方案「最快10/6解除」
  - 來源：Yahoo 台股；發布時間：2026-10-05T14:26:00Z；台北時間：2026-10-05 22:26
  - 摘要：三地集團將中壢乖乖工廠出售給日月光，引發工會不滿，乖乖工會於本月2日發起無限期罷工行動，桃園市勞動局今天（5日）進行勞資協商，乖乖董事長鍾育霖提出相關補償辦法，工會預計
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B9%96%E4%B9%96%E5%B7%A5%E6%9C%83%E7%99%BC%E5%8B%95%E7%84%A1%E9%99%90%E6%9C%9F%E7%BD%B7%E5%B7%A5-%E8%91%A3%E5%BA%A7%E6%8F%90%E8%A3%9C%E5%84%9F%E6%96%B9%E6%A1%88-%E6%9C%80%E5%BF%AB10-6%E8%A7%A3%E9%99%A4-142600295.html
- 事件7：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 來源：Federal Reserve；發布時間：Mon, 5 Oct 2026 20:30:00 GMT；台北時間：2026-10-06 04:30
  - 摘要：Federal Reserve Board announces approval of application by Isabella Bank Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261005a.htm
- 事件8：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:45:00 GMT；台北時間：2026-10-03 04:45
  - 摘要：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261002a.htm
- 事件9：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:00:00 GMT；台北時間：2026-10-03 04:00
  - 摘要：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261002a.htm
- 事件10：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 15:00:00 GMT；台北時間：2026-10-02 23:00
  - 摘要：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261002a.htm
- 事件11：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress test-related capital requirements
  - 來源：Federal Reserve；發布時間：Wed, 30 Sep 2026 13:00:00 GMT；台北時間：2026-09-30 21:00
  - 摘要：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress t
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm
- 事件12：Stocks are hitting records despite surging yields. Cramer explains why
  - 來源：CNBC；發布時間：Mon, 05 Oct 2026 22:18:13 GMT；台北時間：2026-10-06 06:18
  - 摘要：CNBC’s Jim Cramer said Nvidia, Microsoft and Meta are helping push stocks to records even as surging Treasury yields pressure much of the broader mark
  - 原文連結：https://www.cnbc.com/2026/10/05/cramer-ai-stocks-treasury-yields.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-05

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,470 | TAIFEX Proxy |
| 最高價 | 50,097 | TAIFEX Proxy |
| 最低價 | 49,461 | TAIFEX Proxy |
| 收盤價 | 49,949 | TAIFEX Proxy |
| 漲跌點數 | +1,280 | TAIFEX Proxy |
| 漲跌幅 | +2.63 | TAIFEX Proxy |
| 成交量 | 74,146 | TAIFEX Proxy |
| 日盤高點及低點 | 50,097 / 49,461 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,960 | TAIFEX Proxy |
| 最高價 | 50,247 | TAIFEX Proxy |
| 最低價 | 49,933 | TAIFEX Proxy |
| 收盤價 | 50,118 | TAIFEX Proxy |
| 漲跌點數 | +174 | TAIFEX Proxy |
| 漲跌幅 | +0.35 | TAIFEX Proxy |
| 成交量 | 32,288 | TAIFEX Proxy |
| 夜盤高點及低點 | 50,247 / 49,933 | TAIFEX Proxy |
| 結算價 | 49,944 | TAIFEX Proxy |
| 未平倉量 | 108,339 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 14,760 | TAIFEX Proxy |
| 外資空方 OI | 91,764 | TAIFEX Proxy |
| 外資多空淨 OI | -77,004 | TAIFEX Proxy |
| 投信多方 OI | 77,893 | TAIFEX Proxy |
| 投信空方 OI | 2,749 | TAIFEX Proxy |
| 投信多空淨 OI | +75,144 | TAIFEX Proxy |
| 自營商多方 OI | 2,810 | TAIFEX Proxy |
| 自營商空方 OI | 4,965 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,155 | TAIFEX Proxy |
| 三大法人合計多方 OI | 95,463 | TAIFEX Proxy |
| 三大法人合計空方 OI | 99,478 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -4,015 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +3,300 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +475 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,149 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,796 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,120 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,676 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-30→2026-10-05) | +147 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：2026-10-05 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 43,262 | TAIFEX Proxy |
| 外資日盤空單交易量 | 39,967 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +3,295 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 10,020 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 11,047 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,027 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +4,322 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +475 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +475 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,003 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +417 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,420 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,767 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -610 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +273.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -61.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 49,949 | TAIFEX Proxy |
| 加權指數價格 | 49,712.04 | twse-proxy |
| 台指期與加權指數價差 | +236.96 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.48 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +236.96 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +169 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 49,949 | 50,118 | -169 | TAIFEX Proxy |
| 成交量 | 41,858 | 32,288 | +9,570 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+2,626（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 43,262 | 39,967 | +3,295 | 10,020 | 11,047 | -1,027 | +4,322 | 14,760 | 91,764 | -77,004 | +3,300 | TAIFEX Proxy |
| 投信 | 579 | 104 | +475 | 0 | 0 | +0 | +475 | 77,893 | 2,749 | +75,144 | +475 | TAIFEX Proxy |
| 自營商 | 4,841 | 5,844 | -1,003 | 835 | 418 | +417 | -1,420 | 2,810 | 4,965 | -2,155 | -1,149 | TAIFEX Proxy |
| 三大法人合計 | 48,682 | 45,915 | +2,767 | 10,855 | 11,465 | -610 | +3,377 | 95,463 | 99,478 | -4,015 | +2,626 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,796 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,120 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,676 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-30→2026-10-05) | +147 | TAIFEX Proxy snapshots (2026-10-01) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 43.55% | TAIFEX Proxy |
| 夜盤漲跌點數 | +174 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,027 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-05 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-06 08:40:58 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 150,404 | TAIFEX Proxy |
| Call 總未平倉量 OI | 36,246 | TAIFEX Proxy |
| Call OI 增減 (2026-10-01→2026-10-05) | +30,492 | TAIFEX Proxy snapshots (2026-10-01) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 151,786 | TAIFEX Proxy |
| Put 總未平倉量 OI | 35,467 | TAIFEX Proxy |
| Put OI 增減 (2026-10-01→2026-10-05) | +29,229 | TAIFEX Proxy snapshots (2026-10-01) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.99 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.02 | TAIFEX Proxy |
| Put／Call Ratio | 0.98 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-02→2026-10-05) | 12.60 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-02→2026-10-05) | 11.11 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 52,075 | TAIFEX Proxy |
| 外資 Call日賣 | 50,899 | TAIFEX Proxy |
| 外資 Call日淨 | +1,176 | TAIFEX Proxy |
| 外資 Put日買 | 48,804 | TAIFEX Proxy |
| 外資 Put日賣 | 48,948 | TAIFEX Proxy |
| 外資 Put日淨 | -144 | TAIFEX Proxy |
| 外資 Call夜買 | 19,938 | TAIFEX Proxy |
| 外資 Call夜賣 | 20,232 | TAIFEX Proxy |
| 外資 Call夜淨 | -294 | TAIFEX Proxy |
| 外資 Put夜買 | 22,303 | TAIFEX Proxy |
| 外資 Put夜賣 | 22,157 | TAIFEX Proxy |
| 外資 Put夜淨 | +146 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,320 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,470 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -290 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 46,390 | TAIFEX Proxy |
| 自營商 Call日賣 | 42,294 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,096 | TAIFEX Proxy |
| 自營商 Put日買 | 44,917 | TAIFEX Proxy |
| 自營商 Put日賣 | 48,939 | TAIFEX Proxy |
| 自營商 Put日淨 | -4,022 | TAIFEX Proxy |
| 自營商 Call夜買 | 11,724 | TAIFEX Proxy |
| 自營商 Call夜賣 | 13,361 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,637 | TAIFEX Proxy |
| 自營商 Put夜買 | 16,657 | TAIFEX Proxy |
| 自營商 Put夜賣 | 16,348 | TAIFEX Proxy |
| 自營商 Put夜淨 | +309 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +8,118 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,733 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -4,331 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 52,500 | 2,886 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,000 | 1,794 | TAIFEX Proxy |
| Call OI 第3大履約價 | 50,700 | 1,772 | TAIFEX Proxy |
| Call OI 最大履約價 | 52,500 | 2,886 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 52,500 | 2,886 | 7.96% | TAIFEX Proxy |
| C2 | 50,000 | 1,794 | 4.95% | TAIFEX Proxy |
| C3 | 50,700 | 1,772 | 4.89% | TAIFEX Proxy |
| C4 | 52,000 | 1,363 | 3.76% | TAIFEX Proxy |
| C5 | 49,500 | 1,179 | 3.25% | TAIFEX Proxy |
| C6 | 50,500 | 992 | 2.74% | TAIFEX Proxy |
| C7 | 51,000 | 977 | 2.7% | TAIFEX Proxy |
| C8 | 50,400 | 967 | 2.67% | TAIFEX Proxy |
| C9 | 50,200 | 958 | 2.64% | TAIFEX Proxy |
| C10 | 46,600 | 950 | 2.62% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,000 | 1,918 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,000 | 1,789 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,500 | 1,761 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,000 | 1,918 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,000 | 1,918 | 5.41% | TAIFEX Proxy |
| P2 | 48,000 | 1,789 | 5.04% | TAIFEX Proxy |
| P3 | 48,500 | 1,761 | 4.97% | TAIFEX Proxy |
| P4 | 48,800 | 1,392 | 3.92% | TAIFEX Proxy |
| P5 | 47,000 | 1,182 | 3.33% | TAIFEX Proxy |
| P6 | 48,200 | 1,108 | 3.12% | TAIFEX Proxy |
| P7 | 48,700 | 1,004 | 2.83% | TAIFEX Proxy |
| P8 | 48,600 | 832 | 2.35% | TAIFEX Proxy |
| P9 | 48,400 | 830 | 2.34% | TAIFEX Proxy |
| P10 | 43,800 | 821 | 2.31% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 52,500 (+2,875) | TAIFEX Proxy snapshots (2026-10-01) |
| Call OI 減少最多的履約價 | 47,950 (-5) | TAIFEX Proxy snapshots (2026-10-01) |
| Call 最大 OI 履約價增減 (Call Wall 52,500) | 52,500 (+2,875) | TAIFEX Proxy snapshots (2026-10-01) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,000 (+1,913) | TAIFEX Proxy snapshots (2026-10-01) |
| Put OI 減少最多的履約價 | 43,300 (-4) | TAIFEX Proxy snapshots (2026-10-01) |
| Put 最大 OI 履約價增減 (Put Wall 49,000) | 49,000 (+1,913) | TAIFEX Proxy snapshots (2026-10-01) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 52,500 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-05) | +3,500 | TAIFEX Proxy snapshots (2026-10-01) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-05) | +1,000 | TAIFEX Proxy snapshots (2026-10-01) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 50,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 資料日期 | 2026-10-05 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 49,445.97 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 資料日期 | 2026-10-05 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,800 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-05) | +850 | TAIFEX Proxy snapshots (2026-10-01) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 101,023 | 99,703 | +1,320 | 42,095 | 42,535 | -440 | +1,760 | TAIFEX Proxy |
| 投信 | 0 | 2,150 | -2,150 | 0 | 0 | +0 | -2,150 | TAIFEX Proxy |
| 自營商 | 95,329 | 87,211 | +8,118 | 28,072 | 30,018 | -1,946 | +10,064 | TAIFEX Proxy |
| 三大法人合計 | 196,352 | 189,064 | +7,288 | 70,167 | 72,553 | -2,386 | +9,674 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 10.04 | 9.55 | +0.49 | 3.51 | 3.55 | -0.04 | +0.53 | TAIFEX Proxy |
| 投信 | 0.00 | 1.58 | -1.58 | 0.00 | 0.00 | +0 | -1.58 | TAIFEX Proxy |
| 自營商 | 10.25 | 8.45 | +1.81 | 2.04 | 2.51 | -0.47 | +2.28 | TAIFEX Proxy |
| 三大法人合計 | 20.30 | 19.58 | +0.71 | 5.54 | 6.05 | -0.51 | +1.22 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 13,465 | TAIFEX Proxy |
| 買權空方 OI | 11,904 | TAIFEX Proxy |
| 買權多空淨 OI | +1,561 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-30→2026-10-05) | +515 | TAIFEX Proxy snapshots (2026-10-01) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,331 | TAIFEX Proxy |
| 賣權空方 OI | 9,219 | TAIFEX Proxy |
| 賣權多空淨 OI | -888 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-30→2026-10-05) | -264 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：買權 2026-10-05／賣權 2026-10-05 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +147 | 2026-09-30→2026-10-05 | TAIFEX Proxy snapshots (2026-10-01) |
| 買權前十大 | +515 | 2026-09-30→2026-10-05 | TAIFEX Proxy snapshots (2026-10-01) |
| 賣權前十大 | -264 | 2026-09-30→2026-10-05 | TAIFEX Proxy snapshots (2026-10-01) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-05；資料時間：2026-10-06 08:40:58；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：3 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (0)：無
- 註記：夜盤 OHLC 資料日期 2026-10-06 (T0 2026-10-05)，來源 proxy
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
- margin_ratio：`istock 大盤融資維持率 (資料日期 2026-10-05；T0當日；補登；wantgoo 最新為 10-02 值 197.07；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率 200.67 為補登（T0 當日值，istock；wantgoo 最新為 10-02 值 197.07；晨跑 runner 端被擋，詳 HANDOFF）
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +719.0 | -77,004 | +3,295 | -1,027 | +1,320 | -440 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -52.9 | +75,144 | +475 | +0 | -2,150 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +109.5 | -2,155 | -1,003 | +417 | +8,118 | -1,946 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
