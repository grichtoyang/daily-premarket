# DATA_REPORT_20261022

- 報告日期：`2026-10-23`
- T0 交易日期：`2026-10-22`
- 資料產出時間：`2026-10-23 10:29:42`
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
| 加權指數 | 46,041.43 | 點 | twse-proxy |
| 開盤 | 46,942.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,332.18 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,041.43 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,041.43 | 點 | twse-proxy |
| 漲跌點數 | -846.34 | 點 | twse-proxy |
| 漲跌幅 | -1.81 | % | twse-proxy |
| 成交金額 | 9,334.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 247 | twse-proxy |
| 下跌家數 | 756 | twse-proxy |
| 平盤家數 | 74 | twse-proxy |
| 漲停家數 | 3 | twse-proxy |
| 跌停家數 | 5 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 146 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 659 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 63 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 17 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 11 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -815.8 | 億元 | twse-proxy /institutional |
| 投信 | +94.9 | 億元 | twse-proxy /institutional |
| 自營商 | -273.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -994.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,465.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -138.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 253,430 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 22,348 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 176.99 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-22；民間估算；官方無每日序列；gapfill 自動補登) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,580,250 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,891 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,593 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,334.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,255.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,589.8 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,663.43 | -93.74 | -1.21 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,008.86 | -694.00 | -2.60 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,958.69 | -863.83 | -2.90 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,867.98 | 11.89 | +0.02 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,731.98 | -773.58 | -6.72 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.03 | 2.35 | +14.09 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,647.30 | -1,260.54 | -2.00 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,392.84 | -140.93 | -2.55 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,815.38 | -119.30 | -0.52 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,580.38 | -77.65 | -2.12 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,067.01 | -290.31 | -2.56 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,691.75 | -108.50 | -1.39 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,119.50 | -887.50 | -2.96 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,915.00 | -144.00 | -0.27 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,787.70 | -6.50 | -0.23 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.65 | -0.16 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.95 | -0.19 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.29 | -0.15 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.59 | 0.22 | +0.68 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.67 | 0.06 | +0.06 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 156.93 | -1.21 | -0.76 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,324.78 | -0.81 | -0.06 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 412.35 | -19.54 | -4.52 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 18.53 | -1.29 | -6.51 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 37.74 | -4.67 | -11.01 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 100.44 | 3.29 | +3.39 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,029.30 | -120.70 | -2.91 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,521.83 | -2,490.14 | -2.96 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：星巴克去冰補滿15元踩大雷 董座救獲利砍優惠反踢鐵板
  - 來源：Yahoo 台股；發布時間：2026-10-21T10:03:03Z；台北時間：2026-10-21 18:03
  - 摘要：台灣星巴克正在經歷一場由「去冰補滿加15元」引爆的品牌危機，這項企圖找回尊榮感與提升獲利的改革，為何狠狠踩中消費者雷區，又能為品牌經營者帶來什麼警惕？
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%98%9F%E5%B7%B4%E5%85%8B%E5%8E%BB%E5%86%B0%E8%A3%9C%E6%BB%BF15%E5%85%83%E8%AA%A4%E8%B8%A9%E5%85%A9%E9%9B%B7%E5%8D%80-%E8%91%A3%E5%BA%A7%E9%AB%98%E7%A7%80%E7%8E%B2%E6%8B%AF%E6%95%91%E7%8D%B2%E5%88%A9%E7%A0%8D%E5%84%AA%E6%83%A0-%E8%B8%A2%E5%88%B0%E9%90%B5%E6%9D%BF%E9%99%B7%E5%8D%B1%E6%A9%9F-%E5%93%81%E7%89%8C%E7%B6%93%E7%87%9F%E5%BF%85%E5%AD%B8%E7%9A%84%E5%85%A9%E5%8E%9F%E5%89%87-031106581.html
- 事件2：沈伯洋夫妻持股曝 擁0050、0056還有護國神山
  - 來源：Yahoo 台股；發布時間：2026-10-22T22:29:01Z；台北時間：2026-10-23 06:29
  - 摘要：國民ETF元大台灣50（0050）、元大高股息（0056），連台北市長候選人沈伯洋家也愛！中選會最新財產申報揭露，妻子曾心慧持有16張0050、7張0056、元大台灣價值高息（00940）及3檔美股ETF，夫妻也持有台積電、第一金與兩張保單
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B2%88%E4%BC%AF%E6%B4%8B%E7%90%86%E8%B2%A1%E5%AD%B81-%E6%B2%88%E4%BC%AF%E6%B4%8B%E5%A4%AB%E5%A6%BB%E6%8C%81%E8%82%A1%E6%8F%AD%E5%AF%86-0050-0056%E9%83%BD%E5%85%A5%E8%A2%8B-%E6%8A%95%E8%B3%87%E7%B5%84%E5%90%88%E6%9B%9D%E5%85%89-222901170.html
- 事件3：薔琵颱風來襲若受災「9大稅目」可減免
  - 來源：Yahoo 台股；發布時間：2026-10-23T01:24:34Z；台北時間：2026-10-23 09:24
  - 摘要：薔琵颱風來襲，財政部提醒民眾留意颱風動態及豪雨影響，提前做好防災準備，若因風災或豪雨造成財產、營業損失，可依規定申請9大類稅目減免。受災後應把握「拍照存證、檢附文件、申請減免」三步驟，保留損失證明，以維護自身權益、減輕災害帶來的經濟負擔。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%96%94%E7%90%B5%E9%A2%B1%E9%A2%A8%E4%BE%86%E8%A5%B2%EF%BC%81%E7%B6%9C%E6%89%80%E7%A8%85%E3%80%81%E7%87%9F%E6%89%80%E7%A8%85%E3%80%8C9%E5%A4%A7%E7%A8%85%E7%9B%AE%E3%80%8D%E5%8F%AF%E6%B8%9B%E5%85%8D-%E7%94%B3%E8%AB%8B%E8%A6%8F%E5%AE%9A%E4%B8%80%E6%AC%A1%E7%9C%8B-012434751.html
- 事件4：上櫃一個月跌37%、一張虧蒸發203萬 漢測祭庫藏股自救
  - 來源：Yahoo 台股；發布時間：2026-10-22T10:54:53Z；台北時間：2026-10-22 18:54
  - 摘要：庫藏股自救！有「吸金怪獸」之稱的半導體廠漢測（7856）一度凍資台股8千多億元，還創下新股抽中一張賺245萬元紀錄，如今上櫃才一個月就需要「護盤」。股價從9月中5445元天價跌到剩3410元，等於一張帳面蒸發203萬元，一台豪華轎車沒了，跌
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%87%8D%E8%B3%87%E5%8F%B0%E8%82%A18%E5%8D%83%E5%84%84%E3%80%8C%E5%90%B8%E9%87%91%E6%80%AA%E7%8D%B8%E3%80%8D%E6%BC%A2%E6%B8%AC%E4%B8%8A%E6%AB%83%E4%B8%80%E5%80%8B%E6%9C%88%E5%B0%B1%E5%BA%AB%E8%97%8F%E8%82%A1%E8%87%AA%E6%95%91%EF%BC%81%E5%B0%87%E8%B2%B7%E5%9B%9E%E8%87%AA%E5%AE%B6%E8%82%A1%E7%A5%A830%E8%90%AC%E8%82%A1-001000138.html
- 事件5：美光台中廠勞資協議談妥 產線人員年薪逾200萬
  - 來源：Yahoo 台股；發布時間：2026-10-22T22:50:52Z；台北時間：2026-10-23 06:50
  - 摘要：台灣美光公司與台中工會達成勞資協議，提供總薪酬提升、勞退提撥加碼，以及輪班津貼調高等三大福利。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E5%85%89%E5%8F%B0%E4%B8%AD%E5%BB%A0%E9%81%94%E6%88%90%E5%8B%9E%E8%B3%87%E5%8D%94%E8%AD%B0-%E5%85%AC%E5%8F%B8%E6%89%BF%E8%AB%BE%E7%94%A2%E7%B7%9A%E4%BA%BA%E5%93%A1%E5%B9%B4%E8%96%AA%E9%80%BE200%E8%90%AC-225052080.html
- 事件6：誠美材連5紅、累漲近33% 登上強勢股王寶座
  - 來源：Yahoo 台股；發布時間：2026-10-23T00:00:00Z；台北時間：2026-10-23 08:00
  - 摘要：[FTNN新聞網]記者何亞軒／綜合報導昨（22）日台股加權指數收盤46,041.43點，跌846.34點，跌幅1.81%，觀察昨日表現強勢個股，誠美材受惠於將業務重心轉向車用...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%80%86%E5%8B%A2%E5%8F%B0%E8%82%A1%E5%99%B4%E5%87%BA32-91-%E9%80%99%E6%AA%94%E5%A6%96%E8%82%A1-%E8%BD%89%E5%9E%8B%E6%9C%89%E6%88%90-%E8%99%A7%E6%90%8D%E6%94%B6%E6%96%82-000000213.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：10-year Treasury yield tumbles below 5% to lowest level in nearly a month
  - 來源：CNBC；發布時間：Thu, 22 Oct 2026 20:05:13 GMT；台北時間：2026-10-23 04:05
  - 摘要：Treasury yields dove dramatically lower on Thursday as investors monitored a slump in stocks and surging oil prices.
  - 原文連結：https://www.cnbc.com/2026/10/22/treasurys-bonds-ai-yields.html
- 事件9：Japan core inflation in September surges to its highest this year at 2.1%
  - 來源：CNBC；發布時間：Fri, 23 Oct 2026 00:55:11 GMT；台北時間：2026-10-23 08:55
  - 摘要：Core inflation, which strips out prices of fresh food, was in line with the 2.1% forecast by economists polled by Reuters.
  - 原文連結：https://www.cnbc.com/2026/10/23/japan-inflation-september-highest-in-2026.html
- 事件10：Bill Ackman says 2027 will be an amazing year for stocks as wars, inflation ease
  - 來源：CNBC；發布時間：Thu, 22 Oct 2026 17:53:08 GMT；台北時間：2026-10-23 01:53
  - 摘要："We're going to have an amazing 2027," he said.
  - 原文連結：https://www.cnbc.com/2026/10/22/bill-ackman-talks-meta-and-markets-with-cnbc.html
- 事件11：CoreWeave’s market confidence erodes as bond yields spike and stock sinks
  - 來源：CNBC；發布時間：Thu, 22 Oct 2026 20:12:30 GMT；台北時間：2026-10-23 04:12
  - 摘要：CoreWeave shares are down 36% in October, and the spreads in its credit default swaps are widening.
  - 原文連結：https://www.cnbc.com/2026/10/21/coreweaves-market-confidence-erodes-as-bond-yields-spike-stock-sinks.html
- 事件12：Treasury yields log biggest drop since the 2023 banking crisis. Here's what's going on.
  - 來源：MarketWatch；發布時間：Thu, 22 Oct 2026 22:07:00 GMT；台北時間：2026-10-23 06:07
  - 摘要：&#x2018;It&#x2019;s a take-back trade,&#x2019; says PGIM&#x2019;s Tipp. &#x2018;Not an all-out fear of recession type of situation.&#x2019;
  - 原文連結：https://www.marketwatch.com/story/treasury-yields-see-extreme-plunge-why-investors-are-ducking-for-cover-60044c66?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-22

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,164 | TAIFEX Proxy |
| 最高價 | 47,337 | TAIFEX Proxy |
| 最低價 | 46,217 | TAIFEX Proxy |
| 收盤價 | 46,272 | TAIFEX Proxy |
| 漲跌點數 | -741 | TAIFEX Proxy |
| 漲跌幅 | -1.58 | TAIFEX Proxy |
| 成交量 | 55,226 | TAIFEX Proxy |
| 日盤高點及低點 | 47,337 / 46,217 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,270 | TAIFEX Proxy |
| 最高價 | 46,399 | TAIFEX Proxy |
| 最低價 | 45,523 | TAIFEX Proxy |
| 收盤價 | 45,654 | TAIFEX Proxy |
| 漲跌點數 | -580 | TAIFEX Proxy |
| 漲跌幅 | -1.25 | TAIFEX Proxy |
| 成交量 | 39,368 | TAIFEX Proxy |
| 夜盤高點及低點 | 46,399 / 45,523 | TAIFEX Proxy |
| 結算價 | 46,234 | TAIFEX Proxy |
| 未平倉量 | 115,258 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 8,126 | TAIFEX Proxy |
| 外資空方 OI | 95,423 | TAIFEX Proxy |
| 外資多空淨 OI | -87,297 | TAIFEX Proxy |
| 投信多方 OI | 86,375 | TAIFEX Proxy |
| 投信空方 OI | 2,774 | TAIFEX Proxy |
| 投信多空淨 OI | +83,601 | TAIFEX Proxy |
| 自營商多方 OI | 6,399 | TAIFEX Proxy |
| 自營商空方 OI | 3,139 | TAIFEX Proxy |
| 自營商多空淨 OI | +3,260 | TAIFEX Proxy |
| 三大法人合計多方 OI | 100,900 | TAIFEX Proxy |
| 三大法人合計空方 OI | 101,336 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -436 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,225 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -177 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,544 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-20→2026-10-22) | +4,121 | TAIFEX Proxy snapshots (2026-10-21) |
- 資料日期：2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 50,162 | TAIFEX Proxy |
| 外資日盤空單交易量 | 51,383 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,221 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 18,496 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 19,414 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -918 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -303 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -177 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -177 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,565 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +536 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,029 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +167 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -382 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +14.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -36.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,272 | TAIFEX Proxy |
| 加權指數價格 | 46,041.43 | twse-proxy |
| 台指期與加權指數價差 | +230.57 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.50 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +230.57 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -618 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,272 | 45,654 | +618 | TAIFEX Proxy |
| 成交量 | 55,226 | 39,368 | +15,858 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+142（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 50,162 | 51,383 | -1,221 | 18,496 | 19,414 | -918 | -303 | 8,126 | 95,423 | -87,297 | -1,225 | TAIFEX Proxy |
| 投信 | 568 | 745 | -177 | 0 | 0 | +0 | -177 | 86,375 | 2,774 | +83,601 | -177 | TAIFEX Proxy |
| 自營商 | 5,489 | 3,924 | +1,565 | 1,231 | 695 | +536 | +1,029 | 6,399 | 3,139 | +3,260 | +1,544 | TAIFEX Proxy |
| 三大法人合計 | 56,219 | 56,052 | +167 | 19,727 | 20,109 | -382 | +549 | 100,900 | 101,336 | -436 | +142 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-20→2026-10-22) | +4,121 | TAIFEX Proxy snapshots (2026-10-21) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 41.62% | TAIFEX Proxy |
| 夜盤漲跌點數 | -580 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -918 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-22 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-23 10:29:42 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 178,535 | TAIFEX Proxy |
| Call 總未平倉量 OI | 55,024 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 155,316 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,411 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.15 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.75 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-21→2026-10-22) | -25.67 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-21→2026-10-22) | 3.32 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 45,172 | TAIFEX Proxy |
| 外資 Call日賣 | 45,054 | TAIFEX Proxy |
| 外資 Call日淨 | +118 | TAIFEX Proxy |
| 外資 Put日買 | 52,064 | TAIFEX Proxy |
| 外資 Put日賣 | 52,245 | TAIFEX Proxy |
| 外資 Put日淨 | -181 | TAIFEX Proxy |
| 外資 Call夜買 | 31,148 | TAIFEX Proxy |
| 外資 Call夜賣 | 31,095 | TAIFEX Proxy |
| 外資 Call夜淨 | +53 | TAIFEX Proxy |
| 外資 Put夜買 | 45,050 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,680 | TAIFEX Proxy |
| 外資 Put夜淨 | +370 | TAIFEX Proxy |
| 外資 日盤淨總量 | +299 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +65 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -551 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 65,292 | TAIFEX Proxy |
| 自營商 Call日賣 | 64,470 | TAIFEX Proxy |
| 自營商 Call日淨 | +822 | TAIFEX Proxy |
| 自營商 Put日買 | 52,508 | TAIFEX Proxy |
| 自營商 Put日賣 | 54,441 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,933 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,115 | TAIFEX Proxy |
| 自營商 Call夜賣 | 25,696 | TAIFEX Proxy |
| 自營商 Call夜淨 | -581 | TAIFEX Proxy |
| 自營商 Put夜買 | 36,173 | TAIFEX Proxy |
| 自營商 Put夜賣 | 36,732 | TAIFEX Proxy |
| 自營商 Put夜淨 | -559 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +2,755 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,403 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,374 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 2,444 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 2,275 | TAIFEX Proxy |
| Call OI 第3大履約價 | 51,000 | 1,993 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 2,444 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 2,444 | 4.44% | TAIFEX Proxy |
| C2 | 47,000 | 2,275 | 4.13% | TAIFEX Proxy |
| C3 | 51,000 | 1,993 | 3.62% | TAIFEX Proxy |
| C4 | 48,000 | 1,851 | 3.36% | TAIFEX Proxy |
| C5 | 47,500 | 1,600 | 2.91% | TAIFEX Proxy |
| C6 | 48,350 | 1,591 | 2.89% | TAIFEX Proxy |
| C7 | 47,600 | 1,555 | 2.83% | TAIFEX Proxy |
| C8 | 48,500 | 1,424 | 2.59% | TAIFEX Proxy |
| C9 | 45,100 | 1,401 | 2.55% | TAIFEX Proxy |
| C10 | 47,200 | 1,139 | 2.07% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 1,829 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,500 | 1,537 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,500 | 1,531 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 1,829 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 1,829 | 5.82% | TAIFEX Proxy |
| P2 | 46,500 | 1,537 | 4.89% | TAIFEX Proxy |
| P3 | 45,500 | 1,531 | 4.87% | TAIFEX Proxy |
| P4 | 45,000 | 1,478 | 4.71% | TAIFEX Proxy |
| P5 | 44,000 | 1,106 | 3.52% | TAIFEX Proxy |
| P6 | 45,800 | 956 | 3.04% | TAIFEX Proxy |
| P7 | 45,900 | 854 | 2.72% | TAIFEX Proxy |
| P8 | 46,450 | 819 | 2.61% | TAIFEX Proxy |
| P9 | 45,400 | 768 | 2.45% | TAIFEX Proxy |
| P10 | 47,000 | 756 | 2.41% | TAIFEX Proxy |


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
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 45,920.93 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 97,417 | 97,118 | +299 | 39,477 | 39,037 | +440 | -141 | TAIFEX Proxy |
| 投信 | 0 | 2,000 | -2,000 | 0 | 0 | +0 | -2,000 | TAIFEX Proxy |
| 自營商 | 119,733 | 116,978 | +2,755 | 29,833 | 34,314 | -4,481 | +7,236 | TAIFEX Proxy |
| 三大法人合計 | 217,150 | 216,096 | +1,054 | 69,310 | 73,351 | -4,041 | +5,095 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.44 | 11.58 | -0.14 | 8.57 | 8.75 | -0.18 | +0.04 | TAIFEX Proxy |
| 投信 | 0.00 | 1.10 | -1.10 | 0.00 | 0.00 | +0 | -1.10 | TAIFEX Proxy |
| 自營商 | 12.75 | 14.01 | -1.26 | 7.08 | 7.52 | -0.44 | -0.82 | TAIFEX Proxy |
| 三大法人合計 | 24.18 | 26.69 | -2.51 | 15.64 | 16.26 | -0.62 | -1.89 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 7,058 | TAIFEX Proxy |
| 買權空方 OI | 8,732 | TAIFEX Proxy |
| 買權多空淨 OI | -1,674 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-20→2026-10-22) | +16,974 | TAIFEX Proxy snapshots (2026-10-21) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,763 | TAIFEX Proxy |
| 賣權空方 OI | 9,398 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,635 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-20→2026-10-22) | -8,431 | TAIFEX Proxy snapshots (2026-10-21) |
- 資料日期：買權 2026-10-22／賣權 2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +4,121 | 2026-10-20→2026-10-22 | TAIFEX Proxy snapshots (2026-10-21) |
| 買權前十大 | +16,974 | 2026-10-20→2026-10-22 | TAIFEX Proxy snapshots (2026-10-21) |
| 賣權前十大 | -8,431 | 2026-10-20→2026-10-22 | TAIFEX Proxy snapshots (2026-10-21) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-22；資料時間：2026-10-23 10:29:42；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：54 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (2)：options.chain_oi_change, options.wall_change
- 註記：gapfill 自動補登 L77 維持率＝176.99（wantgoo 2026-10-22）
- 註記：futures-price-after-hours 日期 2026-10-22 非今日 2026-10-23，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-27 非今日 2026-10-23，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-27 非今日 2026-10-23，視為無新節次，不採用
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202610→新202610F4），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：gapfill 補登 T0 真值 176.99 (wantgoo 2026-10-22)
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
| 外資 | -815.8 | -87,297 | -1,221 | -918 | +299 | +440 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +94.9 | +83,601 | -177 | +0 | -2,000 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -273.8 | +3,260 | +1,565 | +536 | +2,755 | -4,481 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
