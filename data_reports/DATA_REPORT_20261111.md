# DATA_REPORT_20261111

- 報告日期：`2026-11-11`
- T0 交易日期：`2026-11-11`
- 資料產出時間：`2026-11-11 02:26:18`
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
| 加權指數 | 41,661.70 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 41,661.70 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | 1,960.06 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | +4.94 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -341.2 | 億元 | twse-proxy /institutional |
| 投信 | +398.9 | 億元 | twse-proxy /institutional |
| 自營商 | -175.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -117.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 222,076 | 張 | HiStock |
| 融券增減 | 13,693 | 張 | HiStock |
| 融資維持率 | 151.90 | % | 前值遞補 (DATA 2026-11-10；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 282,754 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,480.69 | -69.25 | -0.92 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,875.37 | -377.77 | -1.50 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,495.55 | -412.08 | -1.48 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,058.10 | -331.65 | -0.63 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,840.87 | -193.06 | -1.92 | Yahoo Finance Chart API |
| VIX | ^VIX | 20.88 | 0.96 | +4.82 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 58,775.50 | 1,340.73 | +2.33 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,018.85 | -40.84 | -0.81 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,448.95 | -32.91 | -0.13 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,660.79 | 11.61 | +0.32 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,145.49 | -30.29 | -0.27 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,507.00 | -67.25 | -0.89 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,621.25 | -393.25 | -1.40 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,159.00 | -339.00 | -0.65 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,819.20 | -29.50 | -1.04 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.56 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.01 | 0.14 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.37 | 0.11 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.97 | 0.21 | +0.66 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.32 | 0.67 | +0.66 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.82 | 0.53 | +0.34 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.48 | -19.22 | -1.41 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 389.64 | 1.02 | +0.26 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.84 | -0.05 | -0.33 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 34.91 | 0.55 | +1.60 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 86.31 | -0.54 | -0.62 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,025.50 | -89.00 | -2.16 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 73,140.11 | -2,083.04 | -2.77 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：外資連9賣台股照樣大漲千點 PCB矽光子紅燈連發
  - 來源：Yahoo 台股；發布時間：2026-11-10T08:55:48Z；台北時間：2026-11-10 16:55
  - 摘要：台股連兩天強彈，收漲1050點站回4萬2，再衝兆元行情！今(10)日加權指數盤中一度大漲1474.22點、衝上43135.92點，隨後遭遇獲利了結賣壓，午盤後買盤回流，終場上漲1050.22點、漲幅2.52%，收42711.92點，上市成交
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E9%80%A39%E8%B3%A3%E7%A0%8D8298%E5%84%84%EF%BC%81%E5%8F%B0%E8%82%A1%E7%88%86%E5%85%86%E5%85%83%E6%88%90%E4%BA%A4%E5%86%8D%E6%BC%B2%E5%8D%83%E9%BB%9E%E6%94%B6%E5%BE%A942k-%E7%9F%BD%E5%85%89%E5%AD%90pcb%E4%B8%8A%E6%BC%94%E7%B4%85%E7%87%88%E6%8E%A5%E5%8A%9B%E7%A7%80%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085548762.html
- 事件2：國安基金第10次救援登場 六檔護盤老班底曝光
  - 來源：Yahoo 台股；發布時間：2026-11-10T10:00:00Z；台北時間：2026-11-10 18:00
  - 摘要：國安基金護盤列車鳴笛，9日台股就飆出1960點、創史上次高漲點，為市場與股民打了一劑強心針！回顧國安基金過往的戰績「八勝一敗」，但台股也曾在護盤後跌破當時低點。國安基金出手，台股就見底了嗎？國安基金的錢從哪來？歷次又實際用了多少？Yahoo
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E7%AC%AC%E5%8D%81%E6%AC%A1%E9%80%B2%E5%A0%B4-%E9%81%8E%E5%BE%80%E6%88%B0%E7%B8%BE%E3%80%8C%E5%85%AB%E5%8B%9D%E4%B8%80%E6%95%97%E3%80%8D%E4%B8%80%E6%AC%A1%E7%9C%8B%EF%BC%816%E6%AA%94%E7%86%9F%E9%9D%A2%E5%AD%94%E6%98%AF%E8%AD%B7%E7%9B%A4%E8%80%81%E7%8F%AD%E5%BA%95%EF%BC%81%E5%87%BA%E6%89%8B%E5%BE%8C%E5%8F%B0%E8%82%A1%E9%82%84%E6%9C%83%E7%A0%B4%E5%BA%95%E5%97%8E%EF%BC%9F%EF%BD%9C%E7%9C%8B%E5%9C%96%E8%AA%AA%E8%82%A1%E5%B8%82-100000799.html
- 事件3：無辜帳戶被凍生活卡關 卓榮泰允研議解除期限
  - 來源：Yahoo 台股；發布時間：2026-11-10T09:55:29Z；台北時間：2026-11-10 17:55
  - 摘要：立法院10日繼續進行施政總質詢，林淑芬在質詢中表示，行政院近年將打擊詐騙提升至國家安全層級，警示帳戶數量也逐漸下降。她指出，2025年全國約有15萬個警示帳戶，今年3月後已降至14萬戶以下，顯示政府持續推動相關防詐措施。不過，林淑芬表示，部
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%84%A1%E8%BE%9C%E6%B0%91%E7%9C%BE%E5%B8%B3%E6%88%B6%E9%81%AD%E5%87%8D%E7%B5%90%E6%95%B8%E6%9C%88-%E5%8D%93%E6%A6%AE%E6%B3%B0%E5%85%81%E5%BB%BA%E7%AB%8B%E8%AD%A6%E7%A4%BA%E5%B8%B3%E6%88%B6%E9%99%90%E6%9C%9F%E8%A7%A3%E9%99%A4%E6%A9%9F%E5%88%B6-095529779.html
- 事件4：電信三雄EPS揭曉 台灣大奪單月累計雙冠 中華電緊追
  - 來源：Yahoo 台股；發布時間：2026-11-10T09:37:32Z；台北時間：2026-11-10 17:37
  - 摘要：三大電信10月獲利出爐！電信三雄前三季獲利成績今（10）日全數出爐，台灣大（3045）則以單月EPS 0.48元，守穩單月獲利王；中華電信（2412）再度以單月EPS 0.46元的亮眼成績緊追在後；遠傳（4904）獲利表現同樣強勁，單月EP
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%89%E5%A4%A7%E9%9B%BB%E4%BF%A110%E6%9C%88%E7%8D%B2%E5%88%A9%E5%87%BA%E7%88%90%EF%BC%81%E5%8F%B0%E7%81%A3%E5%A4%A7%E5%86%8D%E8%B6%85%E8%BB%8A%E8%80%81%E5%A4%A7%E5%93%A5%E7%99%BB%E5%96%AE%E6%9C%88%E3%80%81%E7%B4%AF%E8%A8%88%E7%8D%B2%E5%88%A9%E7%8E%8B-093732611.html
- 事件5：國人日均嗶掉1226元 非現金支付前3季衝7.7兆
  - 來源：Yahoo 台股；發布時間：2026-11-10T09:24:41Z；台北時間：2026-11-10 17:24
  - 摘要：國內非現金社會快來臨了嗎？隨著嗶支付科技愈來愈方便，金管會今（10）日最新發布前三季非現金支付統計，累計支付交易筆數約70.64億筆、非現金支付交易金額為7.7兆元，等於平均每一筆「嗶」消費為1090元，若以273個日子來算，平均2300萬
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E4%BA%BA%E5%B9%B3%E5%9D%87%E6%AF%8F%E5%A4%A9%E5%97%B6%E6%94%AF%E4%BB%981226%E5%85%83%EF%BC%81%E9%9D%9E%E7%8F%BE%E9%87%91%E7%A4%BE%E6%9C%83%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E7%8E%8777-092441228.html
- 事件6：四大國際社團後援會成立　張嘉郡允諾：捐出選舉補助款
  - 來源：Yahoo 台股；發布時間：2026-11-10T14:16:00Z；台北時間：2026-11-10 22:16
  - 摘要：國民黨雲林縣長候選人張嘉郡今（10日）出席「四大國際社團後援會」成立大會，國際扶輪社、國際獅子會、國際同濟會與國際青年商會的眾多會兄、會姊到場支持。張嘉郡在會中承諾將捐出每票30元的選舉補助款，除延續雲林縣長張麗善對於監護兒少的關懷與照顧，
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9B%9B%E5%A4%A7%E5%9C%8B%E9%9A%9B%E7%A4%BE%E5%9C%98%E5%BE%8C%E6%8F%B4%E6%9C%83%E6%88%90%E7%AB%8B-%E5%BC%B5%E5%98%89%E9%83%A1%E5%85%81%E8%AB%BE-%E6%8D%90%E5%87%BA%E9%81%B8%E8%88%89%E8%A3%9C%E5%8A%A9%E6%AC%BE-141600190.html
- 事件7：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件8：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件9：Here's the inflation breakdown for October 2026 — in one chart
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 16:36:40 GMT；台北時間：2026-11-11 00:36
  - 摘要：The consumer price index rose 0.4% in October, a reduction from September but a level economists said is still uncomfortably high.
  - 原文連結：https://www.cnbc.com/2026/11/10/october-2026-cpi-inflation-breakdown.html
- 事件10：10-year Treasury yield races back to 5% as inflation data, Waller comments drive rate hike expectations
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 17:49:39 GMT；台北時間：2026-11-11 01:49
  - 摘要：Treasury yields moved higher after hotter-than-expected CPI report.
  - 原文連結：https://www.cnbc.com/2026/11/10/us-bonds-treasurys-yields.html
- 事件11：Credit card debt climbs to a record $1.29 trillion, New York Fed research finds
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 18:08:40 GMT；台北時間：2026-11-11 02:08
  - 摘要：As high prices continue to strain household budgets, many consumers have turned to credit cards to help make ends meet.
  - 原文連結：https://www.cnbc.com/2026/11/10/credit-card-debt-record.html
- 事件12：Stocks fall as the 10-year Treasury yield reclaims 5%
  - 來源：MarketWatch；發布時間：Tue, 10 Nov 2026 17:34:00 GMT；台北時間：2026-11-11 01:34
  - 摘要：&#x201c;I don&#x2019;t think they should be raising another 25 basis points,&#x201d; one portfolio manager said about the Federal Reserve&#x2019;s ben
  - 原文連結：https://www.marketwatch.com/story/why-stocks-are-falling-and-10-year-yields-are-climbing-back-near-5-after-tuesdays-inflation-report-389b8392?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-11

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 42,701 | TAIFEX Proxy |
| 最高價 | 43,108 | TAIFEX Proxy |
| 最低價 | 41,873 | TAIFEX Proxy |
| 收盤價 | 42,623 | TAIFEX Proxy |
| 漲跌點數 | +1,145 | TAIFEX Proxy |
| 漲跌幅 | +2.76 | TAIFEX Proxy |
| 成交量 | 85,124 | TAIFEX Proxy |
| 日盤高點及低點 | 43,108 / 41,873 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 104,429 | TAIFEX Proxy |
| 前十大交易人空方 OI | 91,257 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,172 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-09→2026-11-09) | +0 | TAIFEX Proxy snapshots (2026-11-10) |
- 資料日期：2026-11-09 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 86,285 | TAIFEX Proxy |
| 外資日盤空單交易量 | 88,046 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,761 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,966 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -996 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +209 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +20.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 42,623 | TAIFEX Proxy |
| 加權指數價格 | 41,661.70 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +961.30 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +2.31 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +961.30 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 42,623 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 85,124 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 86,285 | 88,046 | -1,761 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 2,986 | 20 | +2,966 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 6,096 | 7,092 | -996 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 95,367 | 95,158 | +209 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,429 | TAIFEX Proxy |
| 前十大交易人空方 OI | 91,257 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,172 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-09→2026-11-09) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

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
| 交易日期 | 2026-11-11 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-11 02:26:18 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 188,915 | TAIFEX Proxy |
| Call 總未平倉量 OI | 76,625 | TAIFEX Proxy |
| Call OI 增減 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 222,833 | TAIFEX Proxy |
| Put 總未平倉量 OI | 57,253 | TAIFEX Proxy |
| Put OI 增減 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.85 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.34 | TAIFEX Proxy |
| Put／Call Ratio | 0.75 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-06→2026-11-09) | 3.96 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-06→2026-11-09) | 11.46 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 60,395 | TAIFEX Proxy |
| 外資 Call日賣 | 59,918 | TAIFEX Proxy |
| 外資 Call日淨 | +477 | TAIFEX Proxy |
| 外資 Put日買 | 78,228 | TAIFEX Proxy |
| 外資 Put日賣 | 78,334 | TAIFEX Proxy |
| 外資 Put日淨 | -106 | TAIFEX Proxy |
| 外資 Call夜買 | 24,117 | TAIFEX Proxy |
| 外資 Call夜賣 | 24,396 | TAIFEX Proxy |
| 外資 Call夜淨 | -279 | TAIFEX Proxy |
| 外資 Put夜買 | 34,810 | TAIFEX Proxy |
| 外資 Put夜賣 | 34,999 | TAIFEX Proxy |
| 外資 Put夜淨 | -189 | TAIFEX Proxy |
| 外資 日盤淨總量 | +583 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +756 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +83 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 51,660 | TAIFEX Proxy |
| 自營商 Call日賣 | 50,158 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,502 | TAIFEX Proxy |
| 自營商 Put日買 | 57,067 | TAIFEX Proxy |
| 自營商 Put日賣 | 67,615 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,548 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,475 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,956 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,481 | TAIFEX Proxy |
| 自營商 Put夜買 | 21,276 | TAIFEX Proxy |
| 自營商 Put夜賣 | 21,756 | TAIFEX Proxy |
| 自營商 Put夜淨 | -480 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +12,050 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,983 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -10,068 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,841 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,300 | 3,403 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 3,222 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,841 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,841 | 11.54% | TAIFEX Proxy |
| C2 | 48,300 | 3,403 | 4.44% | TAIFEX Proxy |
| C3 | 45,000 | 3,222 | 4.2% | TAIFEX Proxy |
| C4 | 43,000 | 2,493 | 3.25% | TAIFEX Proxy |
| C5 | 44,000 | 2,352 | 3.07% | TAIFEX Proxy |
| C6 | 44,500 | 1,492 | 1.95% | TAIFEX Proxy |
| C7 | 41,000 | 1,453 | 1.9% | TAIFEX Proxy |
| C8 | 43,500 | 1,437 | 1.88% | TAIFEX Proxy |
| C9 | 46,500 | 1,423 | 1.86% | TAIFEX Proxy |
| C10 | 42,000 | 1,374 | 1.79% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 35,700 | 4,187 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 3,546 | TAIFEX Proxy |
| Put OI 第3大履約價 | 38,000 | 2,644 | TAIFEX Proxy |
| Put OI 最大履約價 | 35,700 | 4,187 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 35,700 | 4,187 | 7.31% | TAIFEX Proxy |
| P2 | 40,000 | 3,546 | 6.19% | TAIFEX Proxy |
| P3 | 38,000 | 2,644 | 4.62% | TAIFEX Proxy |
| P4 | 41,000 | 2,192 | 3.83% | TAIFEX Proxy |
| P5 | 37,400 | 2,134 | 3.73% | TAIFEX Proxy |
| P6 | 41,500 | 1,752 | 3.06% | TAIFEX Proxy |
| P7 | 42,000 | 1,651 | 2.88% | TAIFEX Proxy |
| P8 | 39,000 | 1,498 | 2.62% | TAIFEX Proxy |
| P9 | 40,500 | 1,466 | 2.56% | TAIFEX Proxy |
| P10 | 39,500 | 1,077 | 1.88% | TAIFEX Proxy |


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
| 與前一交易日的變化 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 35,700 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-11 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,037.32 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-11 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-10→2026-11-11) | +0 | TAIFEX Proxy snapshots (2026-11-10) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 138,729 | 138,146 | +583 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 80 | 0 | +80 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 119,275 | 107,225 | +12,050 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 258,084 | 245,371 | +12,713 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 18.42 | 18.52 | -0.10 | 7.92 | 8.09 | -0.16 | +0.06 | TAIFEX Proxy |
| 投信 | 0.02 | 0.00 | +0.02 | 0.00 | 0.00 | +0 | +0.02 | TAIFEX Proxy |
| 自營商 | 16.85 | 14.69 | +2.16 | 6.05 | 5.86 | +0.19 | +1.98 | TAIFEX Proxy |
| 三大法人合計 | 35.29 | 33.21 | +2.08 | 13.97 | 13.95 | +0.02 | +2.06 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 20,765 | TAIFEX Proxy |
| 買權空方 OI | 27,337 | TAIFEX Proxy |
| 買權多空淨 OI | -6,572 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | 端點未提供 |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 11,322 | TAIFEX Proxy |
| 賣權空方 OI | 15,768 | TAIFEX Proxy |
| 賣權多空淨 OI | -4,446 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：買權 2026-11-09／賣權 2026-11-09 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-09→2026-11-09 | TAIFEX Proxy snapshots (2026-11-10) |
| 買權前十大 | unavailable | — | 端點未提供 |
| 賣權前十大 | unavailable | — | 端點未提供 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-11；資料時間：2026-11-11 02:26:18；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (21)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, options.top10_change
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-10，非 T0 2026-11-11)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-10 非今日 2026-11-11，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-10 非今日 2026-11-11，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-10 非今日 2026-11-11，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-10 (T0 2026-11-11 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-10 (T0 2026-11-11 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-10；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151110, T0=1151111)
- 註記：三大法人回傳日期 20261110 (T0 20261111)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-10)，非 T0 2026-11-11
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -341.2 | unavailable | -1,761 | unavailable | +583 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +398.9 | unavailable | +2,966 | unavailable | +80 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -175.4 | unavailable | -996 | unavailable | +12,050 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
