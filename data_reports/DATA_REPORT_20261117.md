# DATA_REPORT_20261117

- 報告日期：`2026-11-17`
- T0 交易日期：`2026-11-17`
- 資料產出時間：`2026-11-17 04:46:51`
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
| 加權指數 | 43,675.12 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 43,675.12 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | 583.25 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | +1.35 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -701.9 | 億元 | twse-proxy /institutional |
| 投信 | -183.0 | 億元 | twse-proxy /institutional |
| 自營商 | -259.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,143.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 208,773 | 張 | HiStock |
| 融券增減 | 2,077 | 張 | HiStock |
| 融資維持率 | 170.70 | % | 前值遞補 (DATA 2026-11-13；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 300,364 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,409.30 | -152.37 | -2.02 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,495.78 | -640.49 | -2.55 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,189.47 | -754.27 | -2.70 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,549.60 | -797.95 | -1.52 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,620.79 | -525.53 | -5.18 | Yahoo Finance Chart API |
| VIX | ^VIX | 23.77 | 4.47 | +23.16 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,142.35 | 322.99 | +0.53 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,290.53 | -52.20 | -0.98 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,637.60 | -370.95 | -1.55 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,634.35 | -21.48 | -0.59 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,968.79 | -229.19 | -2.05 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,427.25 | -155.75 | -2.05 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,251.25 | -783.50 | -2.79 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,612.00 | -806.00 | -1.54 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,744.50 | -53.00 | -1.89 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.88 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.12 | -0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.94 | 0.01 | +0.02 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.57 | 0.16 | +0.16 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.48 | -0.40 | -0.25 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,335.78 | 2.00 | +0.15 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 373.72 | -25.01 | -6.27 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.36 | -1.03 | -6.72 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.88 | -2.67 | -7.50 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.52 | -3.04 | -3.43 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,856.50 | -29.80 | -0.77 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,923.48 | -381.58 | -0.58 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股摔出史上第二慘 資安股在綠海亮紅燈
  - 來源：Yahoo 台股；發布時間：2026-11-16T09:04:29Z；台北時間：2026-11-16 17:04
  - 摘要：台股重挫2635點，創史上第二大收盤跌點！今(16)日加權指數終場下跌2635.04點、跌幅6.03%，收在全日最低41040.08點，上市成交金額8467.41億元，接連失守4萬3千點與4萬2千點。電子類股重挫6.72%，金融類股下跌3.
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%89%E5%A4%A7%E6%B3%95%E4%BA%BA%E7%A0%8D%E5%8D%83%E5%84%84%E8%B3%A3%E5%A3%93%E5%8F%B0%E8%82%A1%E5%B4%A92635%E9%BB%9E%E5%8F%B2%E4%B8%8A%E7%AC%AC2%E6%85%98%EF%BC%81%E5%8F%B0%E7%A9%8D%E4%B8%80%E5%A4%A9%E8%B7%8C%E6%8E%893%E5%AE%B6%E8%81%AF%E9%9B%BB-%E8%B3%87%E5%AE%89%E8%82%A1%E6%88%90%E7%B6%A0%E6%B5%B7%E6%95%91%E7%94%9F%E5%9C%88%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090429579.html
- 事件2：科技圈力挺黃仁勳 101今晚起連兩日點燈
  - 來源：Yahoo 台股；發布時間：2026-11-16T10:13:00Z；台北時間：2026-11-16 18:13
  - 摘要：輝達前執行長黃仁勳請辭引發全球震撼，台灣科技大老與民間社群展現超高效率，僅花24小時緊急動員，聯手台北101董事長賈永婕促成跨海暖心點燈。台北101於今晚點亮四組跑馬燈，包含台灣AI共創未來與視黃仁勳為家人等感性字句，展現台灣供應鏈對科技之
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%BF%AB%E8%A8%8A-%E5%8F%B0%E7%81%A3-jensen-101%E9%BB%9E%E7%87%88%E7%99%BE%E8%90%AC%E6%87%89%E6%8F%B4-%E5%8A%9B%E6%8C%BA%E9%BB%83%E4%BB%81%E5%8B%B3-101300760.html
- 事件3：零股交易12月7日改版 三大風險一次看
  - 來源：Yahoo 台股；發布時間：2026-11-16T10:29:45Z；台北時間：2026-11-16 18:29
  - 摘要：台股零股族注意！臺灣證券交易所宣布，盤中零股交易新制將於2026年12月7日上路，委託時間從上午9點提前至8點30分，第一次撮合也由9點10分提前至9點，與整股同步開盤，並新增盤前試撮及暫緩開盤機制。不過，零股與整股仍屬不同市場，成交價格可
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9B%B6%E8%82%A1%E6%96%B0%E5%88%B612-7%E4%B8%8A%E8%B7%AF-%E4%BA%A4%E6%98%93%E6%99%82%E9%96%93%E5%A4%A7%E6%94%B9-%E8%83%BD%E7%95%B6%E6%B2%96%E5%97%8E-%E7%9B%A4%E5%89%8D%E8%A9%A6%E6%92%AE%E6%80%8E%E9%BA%BC%E7%9C%8B-102945029.html
- 事件4：股市暴跌匯市沒跟著跳水 新台幣守住33元
  - 來源：Yahoo 台股；發布時間：2026-11-16T10:13:05Z；台北時間：2026-11-16 18:13
  - 摘要：（中央社記者潘姿羽台北2026年11月16日電）輝達執行長黃仁勳辭職風波延燒，科技股賣壓沉重。台股今天崩跌2635.04點，為收盤第2大跌點，外資大舉賣超台股卻不急於匯出，甚至反手匯入，使得新台幣貶幅有限，收盤收32.886元，僅小貶4.8
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%89%B5%E5%8F%B2%E4%B8%8A%E7%AC%AC2%E5%A4%A7%E8%B7%8C%E9%BB%9E-%E5%A4%96%E8%B3%87%E5%8C%AF%E5%87%BA%E8%B6%A8%E7%B7%A9%E6%96%B0%E5%8F%B0%E5%B9%A3%E5%B0%8F%E8%B2%B64-8%E5%88%86-101305004.html
- 事件5：AI前景蒙陰影 證交所喊國際研調仍看好
  - 來源：Yahoo 台股；發布時間：2026-11-16T10:00:24Z；台北時間：2026-11-16 18:00
  - 摘要：台股今（16）日終場暴跌2,635.04點，收在41,040.08點，創下史上第二大單日跌點。針對市場震盪，證交所出面信心喊話，指出近期國際金融波動雖大，但輝達（NVIDIA）執行長黃仁勳請辭對台股實質影響有限；加上國際研究機構仍看好AI中
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%87%8D%E6%8C%AB2635%E9%BB%9E-%E8%AD%89%E4%BA%A4%E6%89%80%E4%BF%A1%E5%BF%83%E5%96%8A%E8%A9%B1%EF%BC%9Aai%E4%BE%9D%E7%84%B6%E7%9C%8B%E5%A5%BD-100024036.html
- 事件6：00939年終除息維持0.15元！全年殖利率逾8％　想領息最晚這天買
  - 來源：Yahoo 台股；發布時間：2026-11-16T16:02:00Z；台北時間：2026-11-17 00:02
  - 摘要：每月配息的統一台灣高息動能ETF (00939)，12月又將除息，預計每受益權單位配發0.15元，連2月維持掛牌以來的最高配息金額。本次除息交易日為12月1日，想領息的投資人，最晚要在11月30日買進，就能在12月23日領到錢。
  - 原文連結：https://tw.stock.yahoo.com/news/00939%E5%B9%B4%E7%B5%82%E9%99%A4%E6%81%AF%E7%B6%AD%E6%8C%810-15%E5%85%83-%E5%85%A8%E5%B9%B4%E6%AE%96%E5%88%A9%E7%8E%87%E9%80%BE8-%E6%83%B3%E9%A0%98%E6%81%AF%E6%9C%80%E6%99%9A%E9%80%99%E5%A4%A9%E8%B2%B7-160200700.html
- 事件7：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions, and changes to streamline and adjust their check services
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 18:30:00 GMT；台北時間：2026-11-13 02:30
  - 摘要：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions,
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261112a.htm
- 事件8：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 17:45:00 GMT；台北時間：2026-11-13 01:45
  - 摘要：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 16:00:00 GMT；台北時間：2026-11-13 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261112a.htm
- 事件10：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件11：Fed Chairman Kevin Warsh stresses importance of AI to economy, but says it could ‘disappoint’
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 18:46:07 GMT；台北時間：2026-11-17 02:46
  - 摘要：unavailable
  - 原文連結：https://www.cnbc.com/2026/11/16/fed-ai-task-force-kevin-warsh.html
- 事件12：Anthropic’s Wall Street whisperer: Meet CFO Krishna Rao
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 20:44:24 GMT；台北時間：2026-11-17 04:44
  - 摘要：Anthropic's upcoming IPO is putting finance chief Krishna Rao into the limelight.
  - 原文連結：https://www.cnbc.com/2026/11/16/anthropic-cfo-krishna-rao-ipo.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-17

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,656 | TAIFEX Proxy |
| 最高價 | 43,672 | TAIFEX Proxy |
| 最低價 | 40,714 | TAIFEX Proxy |
| 收盤價 | 40,885 | TAIFEX Proxy |
| 漲跌點數 | -2,954 | TAIFEX Proxy |
| 漲跌幅 | -6.74 | TAIFEX Proxy |
| 成交量 | 167,772 | TAIFEX Proxy |
| 日盤高點及低點 | 43,672 / 40,714 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 91,547 | TAIFEX Proxy |
| 前十大交易人空方 OI | 71,991 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,556 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-13→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-16) |
- 資料日期：2026-11-13 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 162,613 | TAIFEX Proxy |
| 外資日盤空單交易量 | 157,435 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +5,178 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -7,517 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +4,006 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,667 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +135.0 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,885 | TAIFEX Proxy |
| 加權指數價格 | 43,675.12 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -2,790.12 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -6.39 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -2,790.12 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,885 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 167,772 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 162,613 | 157,435 | +5,178 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 51,979 | 59,496 | -7,517 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 15,054 | 11,048 | +4,006 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 229,646 | 227,979 | +1,667 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 91,547 | TAIFEX Proxy |
| 前十大交易人空方 OI | 71,991 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,556 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-13→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

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
| 交易日期 | 2026-11-17 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-17 04:46:51 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 224,718 | TAIFEX Proxy |
| Call 總未平倉量 OI | 112,991 | TAIFEX Proxy |
| Call OI 增減 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 182,619 | TAIFEX Proxy |
| Put 總未平倉量 OI | 59,706 | TAIFEX Proxy |
| Put OI 增減 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.23 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.89 | TAIFEX Proxy |
| Put／Call Ratio | 0.53 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-12→2026-11-13) | 0.49 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-12→2026-11-13) | -8.94 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 54,791 | TAIFEX Proxy |
| 外資 Call日賣 | 55,135 | TAIFEX Proxy |
| 外資 Call日淨 | -344 | TAIFEX Proxy |
| 外資 Put日買 | 55,356 | TAIFEX Proxy |
| 外資 Put日賣 | 56,354 | TAIFEX Proxy |
| 外資 Put日淨 | -998 | TAIFEX Proxy |
| 外資 Call夜買 | 21,531 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,045 | TAIFEX Proxy |
| 外資 Call夜淨 | +486 | TAIFEX Proxy |
| 外資 Put夜買 | 18,972 | TAIFEX Proxy |
| 外資 Put夜賣 | 19,140 | TAIFEX Proxy |
| 外資 Put夜淨 | -168 | TAIFEX Proxy |
| 外資 日盤淨總量 | +654 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -830 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -830 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 52,481 | TAIFEX Proxy |
| 自營商 Call日賣 | 63,527 | TAIFEX Proxy |
| 自營商 Call日淨 | -11,046 | TAIFEX Proxy |
| 自營商 Put日買 | 56,914 | TAIFEX Proxy |
| 自營商 Put日賣 | 51,589 | TAIFEX Proxy |
| 自營商 Put日淨 | +5,325 | TAIFEX Proxy |
| 自營商 Call夜買 | 11,595 | TAIFEX Proxy |
| 自營商 Call夜賣 | 14,562 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,967 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,823 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,424 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,399 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -16,371 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -8,079 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +3,926 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 9,318 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,500 | 7,874 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 5,357 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 9,318 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 9,318 | 8.25% | TAIFEX Proxy |
| C2 | 47,500 | 7,874 | 6.97% | TAIFEX Proxy |
| C3 | 44,000 | 5,357 | 4.74% | TAIFEX Proxy |
| C4 | 48,000 | 5,068 | 4.49% | TAIFEX Proxy |
| C5 | 45,000 | 4,329 | 3.83% | TAIFEX Proxy |
| C6 | 46,500 | 3,724 | 3.3% | TAIFEX Proxy |
| C7 | 43,000 | 3,567 | 3.16% | TAIFEX Proxy |
| C8 | 47,000 | 3,385 | 3.0% | TAIFEX Proxy |
| C9 | 48,500 | 3,253 | 2.88% | TAIFEX Proxy |
| C10 | 50,000 | 2,700 | 2.39% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 8,465 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 2,741 | TAIFEX Proxy |
| Put OI 第3大履約價 | 42,000 | 1,970 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 8,465 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 8,465 | 14.18% | TAIFEX Proxy |
| P2 | 40,000 | 2,741 | 4.59% | TAIFEX Proxy |
| P3 | 42,000 | 1,970 | 3.3% | TAIFEX Proxy |
| P4 | 38,000 | 1,697 | 2.84% | TAIFEX Proxy |
| P5 | 41,000 | 1,614 | 2.7% | TAIFEX Proxy |
| P6 | 44,000 | 1,562 | 2.62% | TAIFEX Proxy |
| P7 | 41,500 | 1,528 | 2.56% | TAIFEX Proxy |
| P8 | 39,000 | 1,513 | 2.53% | TAIFEX Proxy |
| P9 | 43,000 | 1,464 | 2.45% | TAIFEX Proxy |
| P10 | 42,500 | 1,297 | 2.17% | TAIFEX Proxy |


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
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 40,000.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-17 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,380.47 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-17 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,100 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 111,145 | 110,491 | +654 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 83 | 716 | -633 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 104,070 | 120,441 | -16,371 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 215,298 | 231,648 | -16,350 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 18.66 | 17.98 | +0.68 | 6.23 | 5.88 | +0.35 | +0.33 | TAIFEX Proxy |
| 投信 | 0.01 | 0.55 | -0.54 | 0.00 | 0.00 | +0 | -0.54 | TAIFEX Proxy |
| 自營商 | 16.94 | 19.81 | -2.87 | 4.17 | 5.38 | -1.21 | -1.66 | TAIFEX Proxy |
| 三大法人合計 | 35.61 | 38.34 | -2.73 | 10.40 | 11.26 | -0.86 | -1.87 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 42,709 | TAIFEX Proxy |
| 買權空方 OI | 49,621 | TAIFEX Proxy |
| 買權多空淨 OI | -6,912 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-13→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | unavailable | TAIFEX OpenAPI |
| 賣權空方 OI | unavailable | TAIFEX OpenAPI |
| 賣權多空淨 OI | unavailable | TAIFEX OpenAPI |
| 賣權多空淨 OI 變化 | unavailable | 端點未提供 |
- 資料日期：買權 2026-11-13／賣權 unavailable (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-13→2026-11-13 | TAIFEX Proxy snapshots (2026-11-16) |
| 買權前十大 | +0 | 2026-11-13→2026-11-13 | TAIFEX Proxy snapshots (2026-11-16) |
| 賣權前十大 | unavailable | — | 端點未提供 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-17；資料時間：2026-11-17 04:46:51；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (21)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, options.top10_change
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-16，非 T0 2026-11-17)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-16 非今日 2026-11-17，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-16 非今日 2026-11-17，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-16 非今日 2026-11-17，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-16 (T0 2026-11-17 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-16 (T0 2026-11-17 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-13；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151116, T0=1151117)
- 註記：三大法人回傳日期 20261116 (T0 20261117)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-13)，非 T0 2026-11-17
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -701.9 | unavailable | +5,178 | unavailable | +654 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | -183.0 | unavailable | -7,517 | unavailable | -633 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -259.0 | unavailable | +4,006 | unavailable | -16,371 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
