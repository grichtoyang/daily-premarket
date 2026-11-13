# DATA_REPORT_20261112

- 報告日期：`2026-11-13`
- T0 交易日期：`2026-11-12`
- 資料產出時間：`2026-11-13 12:02:12`
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
| 加權指數 | 43,091.87 | 點 | twse-proxy |
| 開盤 | 44,180.46 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 44,525.24 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 42,943.50 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 43,091.87 | 點 | twse-proxy |
| 漲跌點數 | -1,165.28 | 點 | twse-proxy |
| 漲跌幅 | -2.63 | % | twse-proxy |
| 成交金額 | 10,568.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 277 | twse-proxy |
| 下跌家數 | 730 | twse-proxy |
| 平盤家數 | 75 | twse-proxy |
| 漲停家數 | 12 | twse-proxy |
| 跌停家數 | 10 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 241 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 570 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 58 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 23 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 8 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -6.8 | 億元 | twse-proxy /institutional |
| 投信 | +125.7 | 億元 | twse-proxy /institutional |
| 自營商 | -65.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +53.4 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,035.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -94.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 246,470 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 471 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 167.20 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,489,327 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 35,948 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,032 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,568.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,760.8 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 13,329.2 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,592.40 | -26.98 | -0.35 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,366.09 | -100.10 | -0.39 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,289.19 | -85.06 | -0.30 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,297.09 | -189.40 | -0.36 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,506.67 | -57.44 | -0.54 | Yahoo Finance Chart API |
| VIX | ^VIX | 18.70 | 1.21 | +6.92 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,360.71 | 541.35 | +0.89 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,332.12 | -10.61 | -0.20 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,805.46 | -203.09 | -0.85 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,663.71 | 7.88 | +0.22 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,135.40 | -62.58 | -0.56 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,624.00 | 8.75 | +0.11 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,370.50 | -14.00 | -0.05 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,498.00 | 108.00 | +0.21 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,809.10 | 1.80 | +0.06 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.86 | 0.13 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.10 | 0.10 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.43 | 0.08 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.84 | -0.02 | -0.07 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.15 | -0.02 | -0.02 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.89 | 0.16 | +0.10 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,332.32 | -3.94 | -0.29 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 405.49 | -7.86 | -1.90 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 15.76 | -0.32 | -1.99 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 36.29 | -1.53 | -4.05 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 88.18 | -0.56 | -0.63 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,922.60 | 37.30 | +0.96 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 68,652.08 | -5,312.39 | -7.18 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：11千金亮紅燈 創意超車川湖登股后
  - 來源：Yahoo 台股；發布時間：2026-11-13T03:20:16Z；台北時間：2026-11-13 11:20
  - 摘要：不甩輝達風波！台股今（13）日盤中強彈近1,400點、重返4萬4千點，千金股掀起漲停潮，創意（3443）、大立光（3008）、穎崴（6515）、聯發科（2454）、世芯-KY（3661）等11檔亮燈，其中創意衝上8,645元，一舉超越川湖（
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E5%90%8E%E6%8F%9B%E4%BA%BA%E7%95%B6%EF%BC%81%E5%89%B5%E6%84%8F%E6%93%A0%E4%B8%8B%E5%B7%9D%E6%B9%96%E8%A1%9D8645%E5%85%83%E6%BC%B2%E5%81%9C-11%E5%8D%83%E9%87%91%E5%90%8C%E6%AD%A5%E4%BA%AE%E7%87%88-032016249.html
- 事件2：3檔人氣ETF本周賺大盤 00981A最猛漲近12%
  - 來源：Yahoo 台股；發布時間：2026-11-13T03:23:04Z；台北時間：2026-11-13 11:23
  - 摘要：台股今(13)日即將收週線，截至昨日，加權指數漲超過8%，今天持續反彈千點，週線可望終結四連黑。在這樣的反彈行情中，上週新增受益人最多的五檔ETF中，入手的投資人本周雖然全數賺錢，但只有0050、00981A、00406A三檔跑贏大盤，其中
  - 原文連結：https://tw.stock.yahoo.com/news/0050%E3%80%8100981a%E7%AD%89%E3%80%8C3%E6%AA%94%E4%BA%BA%E6%B0%A3etf%E3%80%8D%E8%B4%8F%E9%81%8E%E5%A4%A7%E7%9B%A4-%E6%9C%80%E5%BC%B7%E4%B8%80%E5%91%A8%E9%A3%86%E8%BF%9112%E5%A4%A7%E8%B4%8F%E5%AE%B6-032304524.html
- 事件3：今年EPS估飆132元 法人看威剛：明年營收與獲利分歧
  - 來源：Yahoo 台股；發布時間：2026-11-12T22:55:30Z；台北時間：2026-11-13 06:55
  - 摘要：台股12日震盪重挫1,165.28點，收在43,091.87點，記憶體族群也難逃賣壓。南亞科(2408)收379.5元、下跌3.68%；華邦電(2344)跌6.59%至127.5元；群聯(8299)收1,670元、下跌3.47%；威剛(32
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A8%81%E5%89%9B%E4%BB%8A%E5%B9%B4eps%E4%BC%B0%E9%A3%86132%E5%85%83-%E6%98%8E%E5%B9%B4dram%E7%BC%BA%E8%B2%A8%E6%9B%B4%E5%9A%B4%E9%87%8D-%E6%B3%95%E4%BA%BA%E5%8D%BB%E7%9C%8B%E7%8D%B2%E5%88%A9%E7%B8%AE%E6%B0%B4-%E6%AF%9B%E5%88%A9%E7%8E%87%E6%81%90%E8%B7%8C%E7%A0%B43%E6%88%90-225530617.html
- 事件4：黃仁勳請辭 86檔「概念股」一片紅5檔飆漲停
  - 來源：Yahoo 台股；發布時間：2026-11-13T01:53:30Z；台北時間：2026-11-13 09:53
  - 摘要：美股四大指數全數收低，輝達宣布黃仁勳請辭執行長後，股價下跌4.34%，台積電ADR也跌1.9%，不過超微與博通逆勢上漲逾5%，半導體股表現分歧。台股股民原先擔憂黃仁勳下台將衝擊今（13）日行情，未料台股早盤反而飆漲近1,400點，來到44,
  - 原文連結：https://tw.stock.yahoo.com/news/86%E6%AA%94%E3%80%8C%E9%BB%83%E4%BB%81%E5%8B%B3%E6%A6%82%E5%BF%B5%E8%82%A1%E3%80%8D%E4%B8%80%E7%89%87%E7%B4%85%EF%BC%81%E5%89%B5%E6%84%8F%E8%81%AF%E7%99%BC%E7%A7%915%E6%AA%94%E9%A3%86%E6%BC%B2%E5%81%9C-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E4%B8%8D%E7%A2%BA%E5%AE%9A%E6%80%A7%E9%99%8D%E6%BA%AB-014832138.html
- 事件5：買單排隊！聯發科一字鎖漲停 分析師教戰空手策略
  - 來源：Yahoo 台股；發布時間：2026-11-13T02:40:14Z；台北時間：2026-11-13 10:40
  - 摘要：IC設計大廠聯發科（2454）今（13）日表現強勢，早盤跳空一字鎖漲停，股價大漲385元、衝上4,235元，改寫10月29日以來近一個月新高，盤中更吸引逾3千張買單高掛排隊。市場看好聯發科受惠AI ASIC客製化晶片需求與輝達事件後的資金轉
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E8%BE%AD%E8%81%B7%E8%B3%87%E9%87%91%E5%A4%A7%E6%90%AC%E9%A2%A8%EF%BC%81%E8%81%AF%E7%99%BC%E7%A7%91%E8%A2%AB%E6%90%B6%E8%B2%B7%E9%A3%86%E6%BC%B2%E5%81%9C-3%E5%8D%83%E5%A4%9A%E5%BC%B5%E6%8E%92%E9%9A%8A%E7%AD%89%E8%B2%B7-024632378.html
- 事件6：買盤押注ASIC三雄 經理人點出「成長最根本動能」
  - 來源：Yahoo 台股；發布時間：2026-11-13T01:52:00Z；台北時間：2026-11-13 09:52
  - 摘要：黃仁勳請辭輝達執行長後，台股首個交易日反彈逾千點，創意、世芯-KY、聯發科早盤齊攻漲停。3檔強勢股有個共通點，都做客製化晶片生意。當市場還在猜輝達由誰接班，台股買盤已先一步押注，雲端大廠花在自研晶片上的錢，會進到哪些台廠的口袋？
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%8F%9B%E5%B8%A5%E8%AE%8A%E5%B1%80-%E9%BB%83%E4%BB%81%E5%8B%B3%E4%B8%8B%E5%8F%B0%E8%AA%B0%E5%8F%97%E6%83%A0-%E5%8F%B0%E8%82%A1asic%E4%B8%89%E9%9B%84%E4%BA%AE%E7%87%88%E6%BC%B2%E5%81%9C-%E5%89%B5%E6%84%8F-%E4%B8%96%E8%8A%AF-015200987.html
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
- 事件11：In a policy switch, the Fed says its October 2027 meeting will not see a vote on interest rates
  - 來源：CNBC；發布時間：Thu, 12 Nov 2026 19:05:25 GMT；台北時間：2026-11-13 03:05
  - 摘要：There will be seven voting meetings next year, with the October session set up as extra time for policy deliberation without a formal vote or post-mee
  - 原文連結：https://www.cnbc.com/2026/11/12/in-policy-switch-fed-says-its-october-2027-meeting-will-not-see-a-vote-on-interest-rates.html
- 事件12：Analysis: Nvidia’s leadership crisis tests the chipmaker’s role as the ‘central bank of AI’
  - 來源：CNBC；發布時間：Thu, 12 Nov 2026 23:08:50 GMT；台北時間：2026-11-13 07:08
  - 摘要：The tech giant's web of ties to other companies is raising the possibility that it could do far-reaching economic and financial damage.
  - 原文連結：https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-ai-financial-system-risk.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-12

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 44,166 | TAIFEX Proxy |
| 最高價 | 44,555 | TAIFEX Proxy |
| 最低價 | 43,057 | TAIFEX Proxy |
| 收盤價 | 43,178 | TAIFEX Proxy |
| 漲跌點數 | -958 | TAIFEX Proxy |
| 漲跌幅 | -2.17 | TAIFEX Proxy |
| 成交量 | 87,240 | TAIFEX Proxy |
| 日盤高點及低點 | 44,555 / 43,057 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,180 | TAIFEX Proxy |
| 最高價 | 44,034 | TAIFEX Proxy |
| 最低價 | 42,371 | TAIFEX Proxy |
| 收盤價 | 43,676 | TAIFEX Proxy |
| 漲跌點數 | +548 | TAIFEX Proxy |
| 漲跌幅 | +1.27 | TAIFEX Proxy |
| 成交量 | 79,972 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,034 / 42,371 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 7,218 | TAIFEX Proxy |
| 外資空方 OI | 106,791 | TAIFEX Proxy |
| 外資多空淨 OI | -99,573 | TAIFEX Proxy |
| 投信多方 OI | 102,096 | TAIFEX Proxy |
| 投信空方 OI | 3,195 | TAIFEX Proxy |
| 投信多空淨 OI | +98,901 | TAIFEX Proxy |
| 自營商多方 OI | 4,034 | TAIFEX Proxy |
| 自營商空方 OI | 4,221 | TAIFEX Proxy |
| 自營商多空淨 OI | -187 | TAIFEX Proxy |
| 三大法人合計多方 OI | 113,348 | TAIFEX Proxy |
| 三大法人合計空方 OI | 114,207 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -859 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +4,698 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -2,969 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -220 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,792 | TAIFEX Proxy |
| 前十大交易人空方 OI | 78,453 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,339 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-10→2026-11-12) | +3,897 | TAIFEX Proxy snapshots (2026-11-11) |
- 資料日期：2026-11-12 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 84,418 | TAIFEX Proxy |
| 外資日盤空單交易量 | 79,685 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +4,733 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 45,780 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 45,356 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +424 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +4,309 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -2,969 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -2,969 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -214 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -292 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +78 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,550 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +132 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +136.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +9.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,178 | TAIFEX Proxy |
| 加權指數價格 | 43,091.87 | twse-proxy |
| 台指期與加權指數價差 | +86.13 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.20 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +86.13 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +498 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,178 | 43,676 | -498 | TAIFEX Proxy |
| 成交量 | 87,240 | 79,972 | +7,268 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,509（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 84,418 | 79,685 | +4,733 | 45,780 | 45,356 | +424 | +4,309 | 7,218 | 106,791 | -99,573 | +4,698 | TAIFEX Proxy |
| 投信 | 2,499 | 5,468 | -2,969 | 0 | 0 | +0 | -2,969 | 102,096 | 3,195 | +98,901 | -2,969 | TAIFEX Proxy |
| 自營商 | 5,159 | 5,373 | -214 | 2,390 | 2,682 | -292 | +78 | 4,034 | 4,221 | -187 | -220 | TAIFEX Proxy |
| 三大法人合計 | 92,076 | 90,526 | +1,550 | 48,170 | 48,038 | +132 | +1,418 | 113,348 | 114,207 | -859 | +1,509 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,792 | TAIFEX Proxy |
| 前十大交易人空方 OI | 78,453 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,339 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-10→2026-11-12) | +3,897 | TAIFEX Proxy snapshots (2026-11-11) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 47.83% | TAIFEX Proxy |
| 夜盤漲跌點數 | +548 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +424 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-12 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-13 12:02:12 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 193,627 | TAIFEX Proxy |
| Call 總未平倉量 OI | 53,656 | TAIFEX Proxy |
| Call OI 增減 | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 189,184 | TAIFEX Proxy |
| Put 總未平倉量 OI | 36,473 | TAIFEX Proxy |
| Put OI 增減 | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.02 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.47 | TAIFEX Proxy |
| Put／Call Ratio | 0.68 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-11→2026-11-12) | -8.91 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-11→2026-11-12) | 1.52 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 58,933 | TAIFEX Proxy |
| 外資 Call日賣 | 57,152 | TAIFEX Proxy |
| 外資 Call日淨 | +1,781 | TAIFEX Proxy |
| 外資 Put日買 | 66,840 | TAIFEX Proxy |
| 外資 Put日賣 | 67,404 | TAIFEX Proxy |
| 外資 Put日淨 | -564 | TAIFEX Proxy |
| 外資 Call夜買 | 43,033 | TAIFEX Proxy |
| 外資 Call夜賣 | 43,937 | TAIFEX Proxy |
| 外資 Call夜淨 | -904 | TAIFEX Proxy |
| 外資 Put夜買 | 47,843 | TAIFEX Proxy |
| 外資 Put夜賣 | 47,165 | TAIFEX Proxy |
| 外資 Put夜淨 | +678 | TAIFEX Proxy |
| 外資 日盤淨總量 | +2,345 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2,685 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -1,242 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 55,099 | TAIFEX Proxy |
| 自營商 Call日賣 | 53,952 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,147 | TAIFEX Proxy |
| 自營商 Put日買 | 47,742 | TAIFEX Proxy |
| 自營商 Put日賣 | 50,455 | TAIFEX Proxy |
| 自營商 Put日淨 | -2,713 | TAIFEX Proxy |
| 自營商 Call夜買 | 31,800 | TAIFEX Proxy |
| 自營商 Call夜賣 | 32,878 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,078 | TAIFEX Proxy |
| 自營商 Put夜買 | 30,368 | TAIFEX Proxy |
| 自營商 Put夜賣 | 34,312 | TAIFEX Proxy |
| 自營商 Put夜淨 | -3,944 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +3,860 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,225 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +1,231 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 4,909 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 3,136 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 2,567 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 4,909 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 4,909 | 9.15% | TAIFEX Proxy |
| C2 | 47,000 | 3,136 | 5.84% | TAIFEX Proxy |
| C3 | 45,000 | 2,567 | 4.78% | TAIFEX Proxy |
| C4 | 44,000 | 2,028 | 3.78% | TAIFEX Proxy |
| C5 | 44,500 | 1,462 | 2.72% | TAIFEX Proxy |
| C6 | 46,500 | 1,403 | 2.61% | TAIFEX Proxy |
| C7 | 45,700 | 1,288 | 2.4% | TAIFEX Proxy |
| C8 | 48,000 | 1,098 | 2.05% | TAIFEX Proxy |
| C9 | 45,500 | 1,096 | 2.04% | TAIFEX Proxy |
| C10 | 44,600 | 1,031 | 1.92% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 43,000 | 1,804 | TAIFEX Proxy |
| Put OI 第2大履約價 | 42,000 | 1,646 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 1,635 | TAIFEX Proxy |
| Put OI 最大履約價 | 43,000 | 1,804 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 43,000 | 1,804 | 4.95% | TAIFEX Proxy |
| P2 | 42,000 | 1,646 | 4.51% | TAIFEX Proxy |
| P3 | 40,000 | 1,635 | 4.48% | TAIFEX Proxy |
| P4 | 39,000 | 1,434 | 3.93% | TAIFEX Proxy |
| P5 | 41,000 | 1,390 | 3.81% | TAIFEX Proxy |
| P6 | 42,500 | 1,300 | 3.56% | TAIFEX Proxy |
| P7 | 35,700 | 1,218 | 3.34% | TAIFEX Proxy |
| P8 | 42,400 | 944 | 2.59% | TAIFEX Proxy |
| P9 | 42,800 | 853 | 2.34% | TAIFEX Proxy |
| P10 | 41,500 | 839 | 2.3% | TAIFEX Proxy |


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
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 43,236.34 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 42,950 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 | +0 | TAIFEX Proxy snapshots (2026-11-11) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 126,337 | 123,992 | +2,345 | 90,198 | 91,780 | -1,582 | +3,927 | TAIFEX Proxy |
| 投信 | 595 | 668 | -73 | 5 | 0 | +5 | -78 | TAIFEX Proxy |
| 自營商 | 105,554 | 101,694 | +3,860 | 66,112 | 63,246 | +2,866 | +994 | TAIFEX Proxy |
| 三大法人合計 | 232,486 | 226,354 | +6,132 | 156,315 | 155,026 | +1,289 | +4,843 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 15.56 | 15.16 | +0.40 | 9.01 | 9.38 | -0.37 | +0.77 | TAIFEX Proxy |
| 投信 | 0.03 | 0.27 | -0.24 | 0.00 | 0.00 | +0.00 | -0.25 | TAIFEX Proxy |
| 自營商 | 11.95 | 12.58 | -0.64 | 8.16 | 7.29 | +0.87 | -1.51 | TAIFEX Proxy |
| 三大法人合計 | 27.53 | 28.01 | -0.48 | 17.18 | 16.67 | +0.50 | -0.98 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 27,143 | TAIFEX Proxy |
| 買權空方 OI | 32,423 | TAIFEX Proxy |
| 買權多空淨 OI | -5,280 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-10→2026-11-12) | +226 | TAIFEX Proxy snapshots (2026-11-11) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 16,219 | TAIFEX Proxy |
| 賣權空方 OI | 17,769 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,550 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-10→2026-11-12) | +1,576 | TAIFEX Proxy snapshots (2026-11-11) |
- 資料日期：買權 2026-11-12／賣權 2026-11-12 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +3,897 | 2026-11-10→2026-11-12 | TAIFEX Proxy snapshots (2026-11-11) |
| 買權前十大 | +226 | 2026-11-10→2026-11-12 | TAIFEX Proxy snapshots (2026-11-11) |
| 賣權前十大 | +1,576 | 2026-11-10→2026-11-12 | TAIFEX Proxy snapshots (2026-11-11) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-12；資料時間：2026-11-13 12:02:12；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：5 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (4)：futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-11-12 非今日 2026-11-13，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202611W2→新202611F2），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`stockintelli 大盤融資維持率 (民間估算；官方無每日序列)`
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
| 外資 | -6.8 | -99,573 | +4,733 | +424 | +2,345 | -1,582 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +125.7 | +98,901 | -2,969 | +0 | -73 | +5 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -65.4 | -187 | -214 | -292 | +3,860 | +2,866 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
