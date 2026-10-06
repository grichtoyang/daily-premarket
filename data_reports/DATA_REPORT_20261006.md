# DATA_REPORT_20261006

- 報告日期：`2026-10-06`
- T0 交易日期：`2026-10-06`
- 資料產出時間：`2026-10-06 19:14:52`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,822.55 | 點 | twse-proxy |
| 開盤 | 49,736.37 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,968.92 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 49,479.69 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,822.55 | 點 | twse-proxy |
| 漲跌點數 | 110.51 | 點 | twse-proxy |
| 漲跌幅 | +0.22 | % | twse-proxy |
| 成交金額 | 10,262.0 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 462 | twse-proxy |
| 下跌家數 | 519 | twse-proxy |
| 平盤家數 | 100 | twse-proxy |
| 漲停家數 | 10 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 300 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 475 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 90 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 20 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -66.6 | 億元 | twse-proxy /institutional |
| 投信 | -158.5 | 億元 | twse-proxy /institutional |
| 自營商 | +17.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -207.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 218,458 | 張 | HiStock |
| 融券增減 | 1,114 | 張 | HiStock |
| 融資維持率 | 200.67 | % | 前值遞補 (DATA 2026-10-05；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,388,446 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,262.0 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,775.2 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 13,037.2 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

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
| VIX | ^VIX | 15.35 | -0.17 | -1.10 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 70,683.98 | 737.12 | +1.05 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,941.39 | -62.35 | -0.89 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,280.56 | 240.22 | +1.00 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,849.25 | 23.00 | +0.29 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 31,444.50 | 126.75 | +0.40 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,797.00 | 239.00 | +0.46 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,872.20 | 4.40 | +0.15 | Yahoo Finance Chart API |

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
| USD/TWD | TWD=X | 31.75 | -0.08 | -0.25 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.02 | -0.15 | -0.14 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.15 | 0.42 | +0.27 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,338.77 | -3.79 | -0.28 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 485.80 | 13.02 | +2.75 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 23.92 | -2.35 | -8.95 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.53 | 0.08 | +0.17 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 87.80 | -1.63 | -1.82 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,184.70 | 27.90 | +0.67 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 86,162.63 | 376.04 | +0.44 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股創高法人先踩剎車 台塑與CCL接棒續向5萬叩關
  - 來源：Yahoo 台股；發布時間：2026-10-06T09:13:37Z；台北時間：2026-10-06 17:13
  - 摘要：台積攜題材股撐場，台股漲110點再創高！今(6)日加權指數終場上漲110.51點、漲幅0.22%，收49,822.55點，成交金額9,779.96億元；盤中最高衝上49,968.92點，距五萬點僅約31點，隨後獲利了結賣壓出籠、一度翻黑，尾
  - 原文連結：https://tw.stock.yahoo.com/news/5%E8%90%AC%E9%BB%9E%E5%89%8D%E6%B3%95%E4%BA%BA%E5%85%88%E4%B8%8B%E8%BB%8A%EF%BC%81%E5%8F%B0%E8%82%A1%E5%AE%88%E4%BD%8F110%E9%BB%9E%E6%BC%B2%E5%8B%A2%E5%86%8D%E5%88%B7%E6%96%B0%E9%AB%98-%E5%8F%B0%E5%A1%91%E9%9B%86%E5%9C%98%E3%80%81%E5%8F%B0%E5%85%89%E9%9B%BB%E9%A0%98ccl%E5%BC%B7%E6%94%BB%E6%95%91%E5%A0%B4%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091337867.html
- 事件2：蔡明興曝資本實力遭打臉 金管會直指揭露不符規定
  - 來源：Yahoo 台股；發布時間：2026-10-06T10:02:12Z；台北時間：2026-10-06 18:02
  - 摘要：富邦金控（2881）董事長蔡明興昨（5）日在一場記者會中首度透露，富邦人壽上半年TIS（新制資本適足率）已高達177%，高於金管會要求的揭露上限140%，正考慮2027年向金管會遞件申請、提前結束過渡期間，意謂邦壽資本好棒棒。不過對此金管會
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%94%A1%E6%98%8E%E8%88%88%E8%AA%AA%E5%AF%8C%E9%82%A6%E5%A3%BD%E8%B3%87%E6%9C%AC%E5%A5%BD%E6%A3%92%E6%A3%92%EF%BC%81%E9%87%91%E7%AE%A1%E6%9C%83%E6%89%93%E8%87%89%E8%AA%AA%E9%87%8D%E8%A9%B1%E3%80%8C%E4%B8%8D%E7%AC%A6%E8%A6%8F%E5%AE%9A%E3%80%8D-100212206.html
- 事件3：聯茂股價衝太快拉警報 最快後天恐遭抓去關
  - 來源：Yahoo 台股；發布時間：2026-10-06T10:15:40Z；台北時間：2026-10-06 18:15
  - 摘要：銅箔基板廠聯茂（6213）因獲利與營收不斷衝高，股價一路驚驚漲，今日盤中一度來到818元，再創掛牌天價，近一週股價大漲26.94%，根據證交所最新公告，聯茂已連續兩個交易日吃下短線漲幅太多的警告，最快後天可能面臨2分鐘分盤處置。今日3大法人
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A3%86%E8%82%A1%E8%81%AF%E8%8C%82%E6%BC%B2%E5%A4%AA%E5%BF%AB-%E6%9C%80%E5%BF%AB%E5%BE%8C%E5%A4%A9-%E6%8A%93%E5%8E%BB%E9%97%9C-101540487.html
- 事件4：636億授權金有望敲門「生技黑馬」獲法人喊價225元
  - 來源：Yahoo 台股；發布時間：2026-10-06T10:15:00Z；台北時間：2026-10-06 18:15
  - 摘要：[FTNN新聞網]記者周雅琦／綜合報導生技大廠廠長聖（6712）受惠細胞儲存及CDMO業務穩健成長，加上實體癌異體CAR-T新藥CAR001開發進度明朗，9月營收及第三季營...
  - 原文連結：https://tw.stock.yahoo.com/news/636%E5%84%84%E5%85%83%E6%8E%88%E6%AC%8A%E9%87%91%E5%8F%AF%E6%9C%9F-%E7%94%9F%E6%8A%80%E9%BB%91%E9%A6%AC-%E6%96%B0%E8%97%A5%E9%80%B2%E5%BA%A6%E5%A0%B1%E5%96%9C-%E6%B3%95%E4%BA%BA%E5%96%8A%E5%83%B9225%E5%85%83-%E6%BD%9B%E5%9C%A8%E6%BC%B2%E5%B9%85%E9%80%BE4%E6%88%90-101500895.html
- 事件5：瑤池金母大減碼臻鼎 單日砍3482張幾乎出清持股
  - 來源：Yahoo 台股；發布時間：2026-10-06T10:13:56Z；台北時間：2026-10-06 18:13
  - 摘要：台股今日兵臨5萬點城下，加權指數上漲110.51點，收在49822.55點，再創收盤新高，投信卻反手大賣台股158.51億元，重量級台股主動式ETF─主動統一台股增長（00981A）今日加碼3檔個股，減碼10檔個股，賣多買少，更幾乎出清手中
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%91%A4%E6%B1%A0%E9%87%91%E6%AF%8D%E5%B9%BE%E4%B9%8E%E5%87%BA%E6%B8%85%E8%87%BB%E9%BC%8E-%E4%BB%8A%E6%97%A5%E5%A4%A7%E7%A0%8D3482%E5%BC%B5-101356559.html
- 事件6：投信狂吹空頭號角也買它！南亞合作題材獲喊310元目標價登買超王　「這檔」迎亞馬遜入股得1630元目標價成亮點
  - 來源：Yahoo 台股；發布時間：2026-10-06T11:00:00Z；台北時間：2026-10-06 19:00
  - 摘要：[FTNN新聞網]記者邱梓欣／綜合報導美股前一交易日全面噴漲，促使台股今（6）日再度開高走高，加權指數終場上漲111點，以49823點作收，漲幅0.22％，成交量9759...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8A%95%E4%BF%A1%E7%8B%82%E5%90%B9%E7%A9%BA%E9%A0%AD%E8%99%9F%E8%A7%92%E4%B9%9F%E8%B2%B7%E5%AE%83-%E5%8D%97%E4%BA%9E%E5%90%88%E4%BD%9C%E9%A1%8C%E6%9D%90%E7%8D%B2%E5%96%8A310%E5%85%83%E7%9B%AE%E6%A8%99%E5%83%B9%E7%99%BB%E8%B2%B7%E8%B6%85%E7%8E%8B-%E9%80%99%E6%AA%94-%E8%BF%8E%E4%BA%9E%E9%A6%AC%E9%81%9C%E5%85%A5%E8%82%A1%E5%BE%971630%E5%85%83%E7%9B%AE%E6%A8%99%E5%83%B9%E6%88%90%E4%BA%AE%E9%BB%9E-110000481.html
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
- 事件12：Russian gold floods Hong Kong as Western sanctions redraw bullion trade
  - 來源：CNBC；發布時間：Mon, 05 Oct 2026 23:14:39 GMT；台北時間：2026-10-06 07:14
  - 摘要：The surge underscores how Russia's gold trade has been rerouted after its invasion of Ukraine in 2022 shut its producers out of major Western markets.
  - 原文連結：https://www.cnbc.com/2026/10/06/russia-gold-hong-kong-china-western-sanctions.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-06

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 50,180 | TAIFEX Proxy |
| 最高價 | 50,194 | TAIFEX Proxy |
| 最低價 | 49,720 | TAIFEX Proxy |
| 收盤價 | 50,060 | TAIFEX Proxy |
| 漲跌點數 | +116 | TAIFEX Proxy |
| 漲跌幅 | +0.23 | TAIFEX Proxy |
| 成交量 | 52,122 | TAIFEX Proxy |
| 日盤高點及低點 | 50,194 / 49,720 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,960 | TAIFEX Proxy |
| 最高價 | 50,247 | TAIFEX Proxy |
| 最低價 | 49,933 | TAIFEX Proxy |
| 收盤價 | 50,118 | TAIFEX Proxy |
| 漲跌點數 | +174 | TAIFEX Proxy |
| 漲跌幅 | +0.35 | TAIFEX Proxy |
| 成交量 | 18,979 | TAIFEX Proxy |
| 夜盤高點及低點 | 50,247 / 49,933 | TAIFEX Proxy |
| 結算價 | 50,082 | TAIFEX Proxy |
| 未平倉量 | 108,230 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,968 | TAIFEX Proxy |
| 外資空方 OI | 92,485 | TAIFEX Proxy |
| 外資多空淨 OI | -79,517 | TAIFEX Proxy |
| 投信多方 OI | 78,956 | TAIFEX Proxy |
| 投信空方 OI | 2,748 | TAIFEX Proxy |
| 投信多空淨 OI | +76,208 | TAIFEX Proxy |
| 自營商多方 OI | 3,067 | TAIFEX Proxy |
| 自營商空方 OI | 4,951 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,884 | TAIFEX Proxy |
| 三大法人合計多方 OI | 94,991 | TAIFEX Proxy |
| 三大法人合計空方 OI | 100,184 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,193 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,513 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,064 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +271 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,796 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,120 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,676 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-02→2026-10-05) | +2,899 | TAIFEX Proxy snapshots (2026-10-05) |
- 資料日期：2026-10-05 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 28,633 | TAIFEX Proxy |
| 外資日盤空單交易量 | 31,112 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,479 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 10,020 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 11,047 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,027 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,452 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,064 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,064 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +243 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +417 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -174 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,172 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -610 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -117.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -61.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 50,060 | TAIFEX Proxy |
| 加權指數價格 | 49,822.55 | twse-proxy |
| 台指期與加權指數價差 | +237.45 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.48 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +237.45 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +58 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 50,060 | 50,118 | -58 | TAIFEX Proxy |
| 成交量 | 33,143 | 18,979 | +14,164 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,178（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 28,633 | 31,112 | -2,479 | 10,020 | 11,047 | -1,027 | -1,452 | 12,968 | 92,485 | -79,517 | -2,513 | TAIFEX Proxy |
| 投信 | 1,099 | 35 | +1,064 | 0 | 0 | +0 | +1,064 | 78,956 | 2,748 | +76,208 | +1,064 | TAIFEX Proxy |
| 自營商 | 3,339 | 3,096 | +243 | 835 | 418 | +417 | -174 | 3,067 | 4,951 | -1,884 | +271 | TAIFEX Proxy |
| 三大法人合計 | 33,071 | 34,243 | -1,172 | 10,855 | 11,465 | -610 | -562 | 94,991 | 100,184 | -5,193 | -1,178 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,796 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,120 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,676 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-02→2026-10-05) | +2,899 | TAIFEX Proxy snapshots (2026-10-05) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 36.41% | TAIFEX Proxy |
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
| 交易日期 | 2026-10-06 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-06 19:14:52 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 150,675 | TAIFEX Proxy |
| Call 總未平倉量 OI | 50,052 | TAIFEX Proxy |
| Call OI 增減 (2026-10-05→2026-10-06) | +13,806 | TAIFEX Proxy snapshots (2026-10-05) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 157,739 | TAIFEX Proxy |
| Put 總未平倉量 OI | 48,604 | TAIFEX Proxy |
| Put OI 增減 (2026-10-05→2026-10-06) | +13,137 | TAIFEX Proxy snapshots (2026-10-05) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.96 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.03 | TAIFEX Proxy |
| Put／Call Ratio | 0.97 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-02→2026-10-05) | 12.60 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-02→2026-10-05) | 11.11 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 49,590 | TAIFEX Proxy |
| 外資 Call日賣 | 49,616 | TAIFEX Proxy |
| 外資 Call日淨 | -26 | TAIFEX Proxy |
| 外資 Put日買 | 60,511 | TAIFEX Proxy |
| 外資 Put日賣 | 59,708 | TAIFEX Proxy |
| 外資 Put日淨 | +803 | TAIFEX Proxy |
| 外資 Call夜買 | 19,938 | TAIFEX Proxy |
| 外資 Call夜賣 | 20,232 | TAIFEX Proxy |
| 外資 Call夜淨 | -294 | TAIFEX Proxy |
| 外資 Put夜買 | 22,303 | TAIFEX Proxy |
| 外資 Put夜賣 | 22,157 | TAIFEX Proxy |
| 外資 Put夜淨 | +146 | TAIFEX Proxy |
| 外資 日盤淨總量 | -829 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +268 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +657 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 39,768 | TAIFEX Proxy |
| 自營商 Call日賣 | 40,462 | TAIFEX Proxy |
| 自營商 Call日淨 | -694 | TAIFEX Proxy |
| 自營商 Put日買 | 47,080 | TAIFEX Proxy |
| 自營商 Put日賣 | 46,691 | TAIFEX Proxy |
| 自營商 Put日淨 | +389 | TAIFEX Proxy |
| 自營商 Call夜買 | 11,724 | TAIFEX Proxy |
| 自營商 Call夜賣 | 13,361 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,637 | TAIFEX Proxy |
| 自營商 Put夜買 | 16,657 | TAIFEX Proxy |
| 自營商 Put夜賣 | 16,348 | TAIFEX Proxy |
| 自營商 Put夜淨 | +309 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -1,083 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +943 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +80 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 50,000 | 3,247 | TAIFEX Proxy |
| Call OI 第2大履約價 | 52,000 | 2,903 | TAIFEX Proxy |
| Call OI 第3大履約價 | 52,500 | 2,882 | TAIFEX Proxy |
| Call OI 最大履約價 | 50,000 | 3,247 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 50,000 | 3,247 | 6.49% | TAIFEX Proxy |
| C2 | 52,000 | 2,903 | 5.8% | TAIFEX Proxy |
| C3 | 52,500 | 2,882 | 5.76% | TAIFEX Proxy |
| C4 | 51,500 | 2,095 | 4.19% | TAIFEX Proxy |
| C5 | 50,300 | 1,823 | 3.64% | TAIFEX Proxy |
| C6 | 50,500 | 1,766 | 3.53% | TAIFEX Proxy |
| C7 | 50,200 | 1,738 | 3.47% | TAIFEX Proxy |
| C8 | 50,400 | 1,447 | 2.89% | TAIFEX Proxy |
| C9 | 50,700 | 1,406 | 2.81% | TAIFEX Proxy |
| C10 | 49,700 | 1,321 | 2.64% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,000 | 3,319 | TAIFEX Proxy |
| Put OI 第2大履約價 | 49,200 | 2,162 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,800 | 2,039 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,000 | 3,319 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,000 | 3,319 | 6.83% | TAIFEX Proxy |
| P2 | 49,200 | 2,162 | 4.45% | TAIFEX Proxy |
| P3 | 48,800 | 2,039 | 4.2% | TAIFEX Proxy |
| P4 | 48,700 | 1,805 | 3.71% | TAIFEX Proxy |
| P5 | 49,300 | 1,790 | 3.68% | TAIFEX Proxy |
| P6 | 48,000 | 1,704 | 3.51% | TAIFEX Proxy |
| P7 | 48,900 | 1,552 | 3.19% | TAIFEX Proxy |
| P8 | 49,500 | 1,551 | 3.19% | TAIFEX Proxy |
| P9 | 48,300 | 1,480 | 3.05% | TAIFEX Proxy |
| P10 | 49,100 | 1,300 | 2.67% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 51,500 (+1,726) | TAIFEX Proxy snapshots (2026-10-05) |
| Call OI 減少最多的履約價 | 50,700 (-366) | TAIFEX Proxy snapshots (2026-10-05) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,200 (+1,434) | TAIFEX Proxy snapshots (2026-10-05) |
| Put OI 減少最多的履約價 | 48,500 (-496) | TAIFEX Proxy snapshots (2026-10-05) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 50,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-05→2026-10-06) | -2,500 | TAIFEX Proxy snapshots (2026-10-05) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-05→2026-10-06) | +0 | TAIFEX Proxy snapshots (2026-10-05) |

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
| Max Pain 價位 | 49,250 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-05→2026-10-06) | +450 | TAIFEX Proxy snapshots (2026-10-05) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 109,298 | 110,127 | -829 | 42,095 | 42,535 | -440 | -389 | TAIFEX Proxy |
| 投信 | 0 | 180 | -180 | 0 | 0 | +0 | -180 | TAIFEX Proxy |
| 自營商 | 86,459 | 87,542 | -1,083 | 28,072 | 30,018 | -1,946 | +863 | TAIFEX Proxy |
| 三大法人合計 | 195,757 | 197,849 | -2,092 | 70,167 | 72,553 | -2,386 | +294 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.49 | 11.57 | -0.09 | 3.51 | 3.55 | -0.04 | -0.05 | TAIFEX Proxy |
| 投信 | 0.00 | 0.13 | -0.13 | 0.00 | 0.00 | +0 | -0.13 | TAIFEX Proxy |
| 自營商 | 5.62 | 6.41 | -0.79 | 2.04 | 2.51 | -0.47 | -0.32 | TAIFEX Proxy |
| 三大法人合計 | 17.10 | 18.11 | -1.01 | 5.54 | 6.05 | -0.51 | -0.50 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 13,465 | TAIFEX Proxy |
| 買權空方 OI | 11,904 | TAIFEX Proxy |
| 買權多空淨 OI | +1,561 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-02→2026-10-05) | +764 | TAIFEX Proxy snapshots (2026-10-05) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,331 | TAIFEX Proxy |
| 賣權空方 OI | 9,219 | TAIFEX Proxy |
| 賣權多空淨 OI | -888 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-02→2026-10-05) | +228 | TAIFEX Proxy snapshots (2026-10-05) |
- 資料日期：買權 2026-10-05／賣權 2026-10-05 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +2,899 | 2026-10-02→2026-10-05 | TAIFEX Proxy snapshots (2026-10-05) |
| 買權前十大 | +764 | 2026-10-02→2026-10-05 | TAIFEX Proxy snapshots (2026-10-05) |
| 賣權前十大 | +228 | 2026-10-02→2026-10-05 | TAIFEX Proxy snapshots (2026-10-05) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-06；資料時間：2026-10-06 19:14:52；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg
- 註記：Gamma 資料日期 2026-10-05 (T0 2026-10-06 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-05 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-05；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-05)，非 T0 2026-10-06
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -66.6 | -79,517 | -2,479 | -1,027 | -829 | -440 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -158.5 | +76,208 | +1,064 | +0 | -180 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +17.2 | -1,884 | +243 | +417 | -1,083 | -1,946 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
