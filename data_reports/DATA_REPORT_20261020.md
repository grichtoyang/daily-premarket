# DATA_REPORT_20261020

- 報告日期：`2026-10-20`
- T0 交易日期：`2026-10-20`
- 資料產出時間：`2026-10-20 23:32:21`
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
| 加權指數 | 46,292.93 | 點 | twse-proxy |
| 開盤 | 46,712.57 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,967.91 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,163.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,292.93 | 點 | twse-proxy |
| 漲跌點數 | -529.15 | 點 | twse-proxy |
| 漲跌幅 | -1.13 | % | twse-proxy |
| 成交金額 | 8,029.5 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 269 | twse-proxy |
| 下跌家數 | 701 | twse-proxy |
| 平盤家數 | 104 | twse-proxy |
| 漲停家數 | 8 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 316 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 451 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 102 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 24 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 0 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -795.4 | 億元 | twse-proxy /institutional |
| 投信 | +187.6 | 億元 | twse-proxy /institutional |
| 自營商 | -355.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -963.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,531.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -27.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 254,996 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 16,098 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 183.39 | % | 前值遞補 (DATA 2026-10-19；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,559,562 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 39,084 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 2,097 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,029.5 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,067.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,096.9 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,714.92 | 24.19 | +0.31 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,460.00 | 29.11 | +0.11 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,545.51 | 16.16 | +0.05 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,430.96 | 464.93 | +0.89 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,350.08 | 33.74 | +0.30 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.80 | -0.64 | -3.47 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 64,916.70 | -407.59 | -0.62 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,768.01 | 99.96 | +1.76 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,867.74 | -319.09 | -1.32 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,735.37 | 4.45 | +0.12 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,801.29 | -16.13 | -0.14 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,763.00 | 28.50 | +0.37 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,757.75 | 35.25 | +0.12 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,704.00 | 522.00 | +1.00 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,790.00 | 47.70 | +1.74 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.77 | 0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.11 | -0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.43 | -0.05 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.63 | 0.24 | +0.74 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.70 | -0.28 | -0.28 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.18 | 0.37 | +0.23 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,327.15 | -6.28 | -0.47 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 425.62 | 5.40 | +1.29 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.80 | -0.28 | -1.39 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 40.93 | 0.13 | +0.32 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 97.18 | -6.48 | -6.25 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,155.00 | -5.10 | -0.12 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 82,330.81 | 477.27 | +0.58 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股V轉沒力仍有抗跌大隊 緯創強彈光學雙雄亮燈
  - 來源：Yahoo 台股；發布時間：2026-10-20T09:12:48Z；台北時間：2026-10-20 17:12
  - 摘要：權值股尾盤賣壓加重，台股反攻無力、下跌529點！今(20)日加權指數終場下跌529.15點、跌幅1.13%，收46,292.93點，成交金額縮至7,600.30億元。大盤早盤一度翻紅、上探46,967.91點，午盤後隨新台幣走貶及權值股賣壓
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%8D%81%E9%80%A3%E7%A0%8D%E5%8F%B0%E8%82%A1v%E8%BD%89%E6%B2%92%E5%8A%9B%E6%91%94529%E9%BB%9E%EF%BC%81%E7%B7%AF%E5%89%B5%E6%8B%89%E5%8D%8A%E6%A0%B9%E6%BC%B2%E5%81%9C%E3%80%8C%E5%85%89%E5%AD%B8%E9%9B%99%E9%9B%84%E3%80%8D%E4%BA%AE%E7%87%88%E6%94%BE%E9%96%83%E9%A0%98%E6%97%8F%E7%BE%A4%E9%96%8B%E8%B6%B4%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091248471.html
- 事件2：高雄楠梓台積電廠區傳工安意外 4工人送醫、原因待釐清
  - 來源：Yahoo 台股；發布時間：2026-10-20T10:19:00Z；台北時間：2026-10-20 18:19
  - 摘要：高雄楠梓區台積電F22廠區20日下午驚傳工安意外，吊車司機在吊掛鋼樑時不慎掉落，砸中下方正在焊接的4名工人，造成3人OHCA失去生命跡象、1人意識清楚，緊急送醫搶救。南科管理局與台積電獲報後已勒令現場停工並配合調查，針對違反職業安全衛生法部
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%AB%98%E9%9B%84%E6%A5%A0%E6%A2%93%E5%8F%B0%E7%A9%8D%E9%9B%BBf22%E5%BB%A0%E5%8D%80%E5%B7%A5%E5%AE%89%E6%84%8F%E5%A4%96-%E9%8B%BC%E6%A8%91%E6%8E%89%E8%90%BD%E7%A0%B84%E5%B7%A5%E4%BA%BA-3%E4%BA%BAohca%E9%80%81%E9%86%AB%E6%90%B6%E6%95%91-101900732.html
- 事件3：台泥、亞泥連續配息43年⋯昔日的存股資優生還能存嗎？
  - 來源：Yahoo 台股；發布時間：2026-10-20T10:00:00Z；台北時間：2026-10-20 18:00
  - 摘要：台泥（1101）是許多傳統存股族的心頭好，日前召開股東臨時會通過歐洲子公司Cimpor International Holdings海外上市案，近期股價衝上16個月新高。不只台泥，10月15日台股狂瀉1655點，水泥族群卻表現抗跌，日前亞泥
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E6%B3%A5%E3%80%81%E4%BA%9E%E6%B3%A5%E9%80%A3%E7%BA%8C%E9%85%8D%E6%81%AF43%E5%B9%B4%E2%8B%AF%E6%98%94%E6%97%A5%E7%9A%84%E5%AD%98%E8%82%A1%E8%B3%87%E5%84%AA%E7%94%9F%E7%8F%BE%E5%9C%A8%E9%82%84%E8%83%BD%E5%AD%98%E5%97%8E%EF%BC%9F%E6%B0%B4%E6%B3%A5%E6%97%8F%E7%BE%A4%E7%9A%84%E7%BE%8E%E9%BA%97%E8%88%87%E5%93%80%E6%84%81-%E5%90%84%E5%AE%B6%E6%8B%9A%E8%BD%89%E5%9E%8B%E5%90%84%E9%A1%AF%E7%A5%9E%E9%80%9A%EF%BC%81%EF%BD%9C%E7%9B%A4%E9%BB%9E%E6%A6%82%E5%BF%B5%E8%82%A1-100000179.html
- 事件4：AI大浪來了誰先準備好？PCB五大佬揭擴產藍圖與缺料挑戰
  - 來源：Yahoo 台股；發布時間：2026-10-20T09:19:14Z；台北時間：2026-10-20 17:19
  - 摘要：2026年台北國際印刷電路板展（TPCA Show）盛大登場，隨著AI伺服器、高效能運算與次世代通訊需求進入爆發期，台灣印刷電路板（PCB）與銅箔基板（CCL）產業鏈正迎來史上最猛烈的升級大浪。本次展會包括金居、聯茂、台光電、臻鼎-KY與欣
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%AC%A3%E8%88%88%E7%B0%A1%E5%B1%B1%E5%82%91%E3%80%81%E8%87%BB%E9%BC%8E%E6%B2%88%E6%85%B6%E8%8A%B3%E3%80%81%E5%8F%B0%E5%85%89%E9%9B%BB%E8%91%A3%E5%AE%9A%E5%AE%87%E9%BD%8A%E8%81%9A%E9%96%8B%E9%87%91%E5%8F%A3-tpca%E5%A4%A7%E4%BD%AC%E8%AB%87%E8%A9%B1%E4%B8%80%E6%AC%A1%E7%9C%8B-091914953.html
- 事件5：股價猛衝換來處置令 隴華律勝明起關至28日
  - 來源：Yahoo 台股；發布時間：2026-10-20T10:35:07Z；台北時間：2026-10-20 18:35
  - 摘要：證交所與櫃買中心公告最新處置股名單，上市股隴華（2424）與上櫃股律勝（3354）因近期股價漲幅過大，自21日起雙雙遭列處置股至10月28日。隴華改為每25分鐘撮合一次，律勝則每2分鐘撮合一次。投資人操作應審慎評估風險。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A2%9E2%E6%AA%94%E6%8A%93%E5%8E%BB%E9%97%9C-%E9%80%99%E6%AA%94-6%E5%A4%A9%E6%BC%B235-%E6%85%98%E5%8F%9725%E5%88%86%E9%90%98%E6%92%AE%E5%90%88-102000888.html
- 事件6：股匯雙殺台幣爆量貶1.72角 專家示警短線恐探33元
  - 來源：Yahoo 台股；發布時間：2026-10-20T09:51:28Z；台北時間：2026-10-20 17:51
  - 摘要：台北外匯市場今（20）日上演「股匯雙殺」！新台幣兌美元盤中最低觸及 32.672 元，終場以32.617元作收，貶1.72角，創下自2025年4月14日以來、逾一年半的收盤新低紀錄，成交量爆42.32億美元，今年第六大，約新台幣1380億元
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E5%8F%B0%E5%B9%A3%E7%88%86%E9%87%8F%E8%B2%B6172%E8%A7%92%EF%BC%81%E5%A4%96%E8%B3%87%E9%80%A310%E8%B3%A3-%E5%8C%AF%E5%B8%82%E6%88%90%E4%BA%A4%E9%87%8F%E5%B7%B2%E7%A0%B413%E5%85%86%E5%85%83-095128849.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：Investors look to earnings to reset the bull market. The key level to watch on the S&P 500
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 12:52:29 GMT；台北時間：2026-10-20 20:52
  - 摘要：The key level traders are watching on the S&P 500 that could mean an even bigger decline is ahead.
  - 原文連結：https://www.cnbc.com/2026/10/20/santoli-key-sp-500-level-to-watch.html
- 事件9：Anthropic in talks with neocloud Nscale over second multibillion-dollar deal, source tells CNBC
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 14:12:38 GMT；台北時間：2026-10-20 22:12
  - 摘要：Anthropic and Nscale previously inked a similar deal for a data center on the same site in the U.S.
  - 原文連結：https://www.cnbc.com/2026/10/20/anthropic-nscale-data-center-deal.html
- 事件10：Data center stocks slide as Korea IPO plunges 30%, pressuring tech sentiment
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 13:50:24 GMT；台北時間：2026-10-20 21:50
  - 摘要：Neocloud stocks are falling again following the sector's troubles last week
  - 原文連結：https://www.cnbc.com/2026/10/20/data-center-stocks-slide-as-korea-ipo-plunges-30percent-pressuring-tech-sentiment.html
- 事件11：Oil prices fall as traders hope for diplomatic progress in Middle East
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 15:31:48 GMT；台北時間：2026-10-20 23:31
  - 摘要：Developments in the Middle East remain in focus, with attacks on commercial ships transiting the Strait of Hormuz escalating in recent weeks.
  - 原文連結：https://www.cnbc.com/2026/10/20/oil-price-wti-brent-crude.html
- 事件12：General Motors beats Wall Street's Q3 earnings expectations, narrows full-year guidance
  - 來源：CNBC；發布時間：Tue, 20 Oct 2026 15:23:57 GMT；台北時間：2026-10-20 23:23
  - 摘要：GM narrowed its 2026 earnings guidance and raised its adjusted automotive free cash flow outlook after beating Wall Street’s third-quarter estimates.
  - 原文連結：https://www.cnbc.com/2026/10/20/general-motors-gm-earnings-q3-2026.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-20

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,434 | TAIFEX Proxy |
| 最高價 | 46,920 | TAIFEX Proxy |
| 最低價 | 46,162 | TAIFEX Proxy |
| 收盤價 | 46,384 | TAIFEX Proxy |
| 漲跌點數 | -385 | TAIFEX Proxy |
| 漲跌幅 | -0.82 | TAIFEX Proxy |
| 成交量 | 122,189 | TAIFEX Proxy |
| 日盤高點及低點 | 46,920 / 46,162 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,842 | TAIFEX Proxy |
| 最高價 | 47,033 | TAIFEX Proxy |
| 最低價 | 46,497 | TAIFEX Proxy |
| 收盤價 | 46,691 | TAIFEX Proxy |
| 漲跌點數 | -78 | TAIFEX Proxy |
| 漲跌幅 | -0.17 | TAIFEX Proxy |
| 成交量 | 26,868 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,033 / 46,497 | TAIFEX Proxy |
| 結算價 | 46,341 | TAIFEX Proxy |
| 未平倉量 | 16,625 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,524 | TAIFEX Proxy |
| 外資空方 OI | 101,272 | TAIFEX Proxy |
| 外資多空淨 OI | -89,748 | TAIFEX Proxy |
| 投信多方 OI | 87,171 | TAIFEX Proxy |
| 投信空方 OI | 2,782 | TAIFEX Proxy |
| 投信多空淨 OI | +84,389 | TAIFEX Proxy |
| 自營商多方 OI | 7,105 | TAIFEX Proxy |
| 自營商空方 OI | 4,405 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,700 | TAIFEX Proxy |
| 三大法人合計多方 OI | 105,800 | TAIFEX Proxy |
| 三大法人合計空方 OI | 108,459 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -2,659 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +1,397 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +289 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -129 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 40,132 | TAIFEX Proxy |
| 前十大交易人空方 OI | 41,382 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,250 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-16→2026-10-19) | -3,744 | TAIFEX Proxy snapshots (2026-10-19) |
- 資料日期：2026-10-19 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 95,138 | TAIFEX Proxy |
| 外資日盤空單交易量 | 93,688 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,450 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 15,798 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 15,848 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -50 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,500 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +289 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +289 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,521 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +210 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,311 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +3,260 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +160 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +304.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +14.7 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,384 | TAIFEX Proxy |
| 加權指數價格 | 46,292.93 | twse-proxy |
| 台指期與加權指數價差 | +91.07 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.20 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +91.07 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +307 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,384 | 46,691 | -307 | TAIFEX Proxy |
| 成交量 | 95,321 | 26,868 | +68,453 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,557（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 95,138 | 93,688 | +1,450 | 15,798 | 15,848 | -50 | +1,500 | 11,524 | 101,272 | -89,748 | +1,397 | TAIFEX Proxy |
| 投信 | 35,516 | 35,227 | +289 | 0 | 0 | +0 | +289 | 87,171 | 2,782 | +84,389 | +289 | TAIFEX Proxy |
| 自營商 | 10,196 | 8,675 | +1,521 | 1,474 | 1,264 | +210 | +1,311 | 7,105 | 4,405 | +2,700 | -129 | TAIFEX Proxy |
| 三大法人合計 | 140,850 | 137,590 | +3,260 | 17,272 | 17,112 | +160 | +3,100 | 105,800 | 108,459 | -2,659 | +1,557 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 40,132 | TAIFEX Proxy |
| 前十大交易人空方 OI | 41,382 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,250 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-16→2026-10-19) | -3,744 | TAIFEX Proxy snapshots (2026-10-19) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 21.99% | TAIFEX Proxy |
| 夜盤漲跌點數 | -78 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -50 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-20 | TAIFEX Proxy |
| 到期月份／到期日 | 202610 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-20 23:32:21 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 213,460 | TAIFEX Proxy |
| Call 總未平倉量 OI | 106,703 | TAIFEX Proxy |
| Call OI 增減 (2026-10-19→2026-10-20) | +12,811 | TAIFEX Proxy snapshots (2026-10-19) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 279,705 | TAIFEX Proxy |
| Put 總未平倉量 OI | 68,220 | TAIFEX Proxy |
| Put OI 增減 (2026-10-19→2026-10-20) | +12,972 | TAIFEX Proxy snapshots (2026-10-19) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.76 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.56 | TAIFEX Proxy |
| Put／Call Ratio | 0.64 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-16→2026-10-19) | 5.79 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-16→2026-10-19) | -6.00 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 59,878 | TAIFEX Proxy |
| 外資 Call日賣 | 60,428 | TAIFEX Proxy |
| 外資 Call日淨 | -550 | TAIFEX Proxy |
| 外資 Put日買 | 119,704 | TAIFEX Proxy |
| 外資 Put日賣 | 118,554 | TAIFEX Proxy |
| 外資 Put日淨 | +1,150 | TAIFEX Proxy |
| 外資 Call夜買 | 26,047 | TAIFEX Proxy |
| 外資 Call夜賣 | 25,804 | TAIFEX Proxy |
| 外資 Call夜淨 | +243 | TAIFEX Proxy |
| 外資 Put夜買 | 44,272 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,228 | TAIFEX Proxy |
| 外資 Put夜淨 | +44 | TAIFEX Proxy |
| 外資 日盤淨總量 | -1,700 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -793 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,106 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 61,142 | TAIFEX Proxy |
| 自營商 Call日賣 | 60,075 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,067 | TAIFEX Proxy |
| 自營商 Put日買 | 74,895 | TAIFEX Proxy |
| 自營商 Put日賣 | 80,857 | TAIFEX Proxy |
| 自營商 Put日淨 | -5,962 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,608 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,147 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,539 | TAIFEX Proxy |
| 自營商 Put夜買 | 22,511 | TAIFEX Proxy |
| 自營商 Put夜賣 | 22,474 | TAIFEX Proxy |
| 自營商 Put夜淨 | +37 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +7,029 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,606 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,999 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,500 | 6,380 | TAIFEX Proxy |
| Call OI 第2大履約價 | 54,000 | 5,734 | TAIFEX Proxy |
| Call OI 第3大履約價 | 52,000 | 5,159 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,500 | 6,380 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,500 | 6,380 | 5.98% | TAIFEX Proxy |
| C2 | 54,000 | 5,734 | 5.37% | TAIFEX Proxy |
| C3 | 52,000 | 5,159 | 4.83% | TAIFEX Proxy |
| C4 | 47,000 | 3,789 | 3.55% | TAIFEX Proxy |
| C5 | 49,000 | 3,655 | 3.43% | TAIFEX Proxy |
| C6 | 48,000 | 3,622 | 3.39% | TAIFEX Proxy |
| C7 | 53,000 | 2,501 | 2.34% | TAIFEX Proxy |
| C8 | 47,900 | 2,485 | 2.33% | TAIFEX Proxy |
| C9 | 47,500 | 2,370 | 2.22% | TAIFEX Proxy |
| C10 | 47,200 | 2,265 | 2.12% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 4,486 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,000 | 4,104 | TAIFEX Proxy |
| Put OI 第3大履約價 | 46,500 | 2,041 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 4,486 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 4,486 | 6.58% | TAIFEX Proxy |
| P2 | 45,000 | 4,104 | 6.02% | TAIFEX Proxy |
| P3 | 46,500 | 2,041 | 2.99% | TAIFEX Proxy |
| P4 | 45,500 | 1,891 | 2.77% | TAIFEX Proxy |
| P5 | 44,000 | 1,890 | 2.77% | TAIFEX Proxy |
| P6 | 46,200 | 1,853 | 2.72% | TAIFEX Proxy |
| P7 | 47,000 | 1,820 | 2.67% | TAIFEX Proxy |
| P8 | 44,500 | 1,775 | 2.6% | TAIFEX Proxy |
| P9 | 45,800 | 1,614 | 2.37% | TAIFEX Proxy |
| P10 | 45,700 | 1,376 | 2.02% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 49,000 (+1,757) | TAIFEX Proxy snapshots (2026-10-19) |
| Call OI 減少最多的履約價 | 48,200 (-698) | TAIFEX Proxy snapshots (2026-10-19) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 45,800 (+961) | TAIFEX Proxy snapshots (2026-10-19) |
| Put OI 減少最多的履約價 | 44,300 (-372) | TAIFEX Proxy snapshots (2026-10-19) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +1,000 | TAIFEX Proxy snapshots (2026-10-19) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,487.74 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 資料日期 | 2026-10-19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,500 | TAIFEX Proxy |
| 對應到期月份 | 202610 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-19→2026-10-20) | +0 | TAIFEX Proxy snapshots (2026-10-19) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 178,432 | 180,132 | -1,700 | 70,275 | 70,076 | +199 | -1,899 | TAIFEX Proxy |
| 投信 | 3 | 1,700 | -1,697 | 3 | 0 | +3 | -1,700 | TAIFEX Proxy |
| 自營商 | 141,999 | 134,970 | +7,029 | 33,082 | 34,658 | -1,576 | +8,605 | TAIFEX Proxy |
| 三大法人合計 | 320,434 | 316,802 | +3,632 | 103,360 | 104,734 | -1,374 | +5,006 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 15.89 | 16.21 | -0.32 | 6.70 | 6.73 | -0.03 | -0.29 | TAIFEX Proxy |
| 投信 | 0.00 | 1.25 | -1.25 | 0.00 | 0.00 | +0.00 | -1.25 | TAIFEX Proxy |
| 自營商 | 12.25 | 9.62 | +2.63 | 3.15 | 3.13 | +0.02 | +2.61 | TAIFEX Proxy |
| 三大法人合計 | 28.14 | 27.08 | +1.06 | 9.86 | 9.87 | -0.01 | +1.07 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 47,479 | TAIFEX Proxy |
| 買權空方 OI | 58,250 | TAIFEX Proxy |
| 買權多空淨 OI | -10,771 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-16→2026-10-19) | -5,422 | TAIFEX Proxy snapshots (2026-10-19) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 22,782 | TAIFEX Proxy |
| 賣權空方 OI | 19,527 | TAIFEX Proxy |
| 賣權多空淨 OI | +3,255 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-16→2026-10-19) | -24 | TAIFEX Proxy snapshots (2026-10-19) |
- 資料日期：買權 2026-10-19／賣權 2026-10-19 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -3,744 | 2026-10-16→2026-10-19 | TAIFEX Proxy snapshots (2026-10-19) |
| 買權前十大 | -5,422 | 2026-10-16→2026-10-19 | TAIFEX Proxy snapshots (2026-10-19) |
| 賣權前十大 | -24 | 2026-10-16→2026-10-19 | TAIFEX Proxy snapshots (2026-10-19) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-20；資料時間：2026-10-20 23:32:21；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 覆蓋：361 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (0)：無
- 註記：Gamma 資料日期 2026-10-19 (T0 2026-10-20 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-19 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-10-19；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-19)，非 T0 2026-10-20
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -795.4 | -89,748 | +1,450 | -50 | -1,700 | +199 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +187.6 | +84,389 | +289 | +0 | -1,697 | +3 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -355.8 | +2,700 | +1,521 | +210 | +7,029 | -1,576 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
