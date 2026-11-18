# DATA_REPORT_20261117

- 報告日期：`2026-11-18`
- T0 交易日期：`2026-11-17`
- 資料產出時間：`2026-11-18 13:04:29`
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
| 加權指數 | 40,092.11 | 點 | twse-proxy |
| 開盤 | 40,546.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 41,533.84 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 39,786.45 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 40,092.11 | 點 | twse-proxy |
| 漲跌點數 | -947.97 | 點 | twse-proxy |
| 漲跌幅 | -2.31 | % | twse-proxy |
| 成交金額 | 10,128.7 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 234 | twse-proxy |
| 下跌家數 | 789 | twse-proxy |
| 平盤家數 | 61 | twse-proxy |
| 漲停家數 | 6 | twse-proxy |
| 跌停家數 | 30 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 162 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 651 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 54 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 5 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 43 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -380.9 | 億元 | twse-proxy /institutional |
| 投信 | -38.2 | 億元 | twse-proxy /institutional |
| 自營商 | -157.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -576.1 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 6,691.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -230.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 242,036 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -14,557 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 153.70 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,475,486 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 34,077 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -5,132 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,128.7 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,770.4 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,899.1 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,340.53 | -76.06 | -1.03 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,328.38 | -181.38 | -0.74 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,001.78 | -195.37 | -0.72 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,759.42 | -848.75 | -1.64 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,642.88 | 32.23 | +0.34 | Yahoo Finance Chart API |
| VIX | ^VIX | 25.46 | 2.55 | +11.13 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,030.04 | 169.61 | +0.29 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,033.07 | 64.59 | +1.30 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,241.48 | -266.69 | -1.13 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,570.21 | -14.36 | -0.40 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,558.59 | -79.93 | -0.75 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,359.00 | -80.00 | -1.08 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,075.50 | -208.75 | -0.77 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,815.00 | -855.00 | -1.65 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,711.20 | -40.20 | -1.46 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.10 | -0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.46 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.94 | -0.03 | -0.08 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.49 | -0.06 | -0.06 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.16 | -0.36 | -0.23 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,331.01 | -4.66 | -0.35 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 359.69 | -13.76 | -3.68 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.14 | -0.20 | -1.39 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 31.83 | -0.97 | -2.96 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 86.01 | 0.29 | +0.34 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,864.20 | 11.20 | +0.29 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,317.76 | -538.08 | -0.83 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：創意跌停打開能進嗎？分析師點名半年線支撐
  - 來源：Yahoo 台股；發布時間：2026-11-18T04:06:04Z；台北時間：2026-11-18 12:06
  - 摘要：「創意還有救嗎？」「糖漿來了？」「創意什麼爛東西」「創意打開又超越川湖」「糖漿死守4萬」「糖漿連跌停板都撬開 火力展示欸」「可悲啊 三根跌停」「其實創意沒跌多少，位階還很高，不用看太空」。
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E8%82%A1%E5%90%8E%E5%89%B5%E6%84%8F%E9%80%A3%E5%90%9E3%E6%A0%B9%E8%B7%8C%E5%81%9C%E7%B6%B2%E5%93%AD%E3%80%8C%E9%82%84%E6%9C%89%E6%95%91%E5%97%8E%EF%BC%9F%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E6%8F%AD%E6%94%AF%E6%92%90%E5%83%B9%E4%BD%8D-040604999.html
- 事件2：台股回測年線有撐 聯發科站回4千是關鍵
  - 來源：Yahoo 台股；發布時間：2026-11-18T04:17:39Z；台北時間：2026-11-18 12:17
  - 摘要：【財訊快報／黃啟乙】台股早盤在4萬點上下震盪拉鋸，盤中低點也恰好回測年線附近，顯示年線再度發揮支撐作用。在週三即將進行期貨結算的背景下，若年線支撐能夠持續守穩，不排除台股有機會在結算後逐步醞釀反彈行情。 多頭指標方面，可優先觀察聯發科(24
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%9B%9E%E6%B8%AC%E5%B9%B4%E7%B7%9A%E7%8D%B2%E6%94%AF%E6%92%90-%E8%81%AF%E7%99%BC%E7%A7%91%E7%AB%99%E5%9B%9E4-000%E5%85%83%E6%88%90%E5%8F%8D%E5%BD%88%E8%A7%80%E5%AF%9F%E6%8C%87%E6%A8%99-041739729.html
- 事件3：黃仁勳回鍋遭拒 林伯豐談台廠底氣與變數
  - 來源：Yahoo 台股；發布時間：2026-11-18T04:10:24Z；台北時間：2026-11-18 12:10
  - 摘要：輝達（Nvidia）創辦人黃仁勳昨（17）日首度發聲表態有意願回鍋擔任執行長，卻遭董事長瓊斯（Harvey Jones）在今（18）日清晨的財報會議中明確拒絕。對此，三三會理事長林伯豐今日受訪時指出，黃仁勳對產業的貢獻有目共睹，至於少了黃仁
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E5%9B%9E%E9%8D%8B%E8%BC%9D%E9%81%94%E9%81%AD%E6%8B%92%EF%BC%81%E5%8F%B0%E5%BB%A0%E4%BE%9B%E6%87%89%E9%8F%88%E6%9C%83%E5%8F%97%E6%B3%A2%E5%8F%8A%EF%BC%9F%E6%9E%97%E4%BC%AF%E8%B1%90%EF%BC%9A%E5%8F%B0%E7%81%A3%E6%87%89%E8%A9%B2%E8%83%BD%E9%81%8E%E9%97%9C-041024177.html
- 事件4：00406A殺到低點、年化配息率逾20% 分析師揭適合族群
  - 來源：Yahoo 台股；發布時間：2026-11-17T21:38:30Z；台北時間：2026-11-18 05:38
  - 摘要：千億規模的主動中信台灣收益(00406A)，已公告預估配息0.138元，雖然年化配息率超過20%，但股價昨（17日）跌到6.79元逼近前低，引發投資人擔憂「賺了股息、賠了價差」。分析師謝明哲指出，00406A能夠維持高配息，主要是採用掩護性
  - 原文連結：https://tw.stock.yahoo.com/news/1%E8%A1%A8%E6%87%82-00406a%E8%B7%8C%E5%88%B06-79%E5%85%83%E9%80%BC%E8%BF%91%E5%89%8D%E4%BD%8E-%E5%B9%B4%E5%8C%96%E9%85%8D%E6%81%AF%E7%8E%87%E9%A3%8624-%E8%B2%B7%E5%9C%A8%E9%AB%98%E9%BB%9E%E7%AC%91%E4%B8%8D%E5%87%BA%E4%BE%86-213830728.html
- 事件5：13家金控前10月賺出新高度 法人評四強「買進」
  - 來源：Yahoo 台股；發布時間：2026-11-17T22:00:30Z；台北時間：2026-11-18 06:00
  - 摘要：13家金控前10月成績放榜！合賺6680億元，再創同期新高，唯10月獲利受股災所累，僅國泰金月增，但今年證券受惠股市熱絡，獲利多達倍數成長，法人預估國泰金、玉山金、元大金、兆豐金、中信金、第一金等6檔評價、EPS和殖利率，喊買進國泰金、玉山
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E7%81%BD%E9%81%BF%E9%A2%A8%E6%B8%AF-%E5%9C%8B%E6%B3%B0%E9%87%91-%E5%85%83%E5%A4%A7%E9%87%91-%E5%85%86%E8%B1%90%E9%87%91-6%E5%A4%A7%E9%87%91%E6%8E%A7%E8%A9%95%E5%83%B9-220030851.html
- 事件6：蘇姿丰讚輝達「了不起的公司」產業雜音終究會消散
  - 來源：Yahoo 台股；發布時間：2026-11-18T01:20:06Z；台北時間：2026-11-18 09:20
  - 摘要：蘇姿丰稱輝達與黃仁勳「了不起」，但強調AMD應聚焦AI基礎設施商機與長期成長。 AMD第三季營收133.8億美元、年增45%；資料中心營收85.5億美元、年增97%，占總營收約64%。 AMD估資料中心營收占比2027年突破80%，全球伺服
  - 原文連結：https://tw.stock.yahoo.com/news/amd%E8%B3%87%E6%96%99%E4%B8%AD%E5%BF%83%E7%87%9F%E6%94%B6%E6%9A%B4%E5%A2%9E97-%E8%98%87%E5%A7%BF%E4%B8%B0%E5%96%8A2027%E5%B9%B4%E7%87%9F%E6%94%B6%E6%88%90%E9%95%B7%E9%80%BE80-%E8%AE%9A%E9%BB%83%E4%BB%81%E5%8B%B3%E4%BD%86%E5%B1%AC-%E7%94%A2%E6%A5%AD%E9%9B%9C%E9%9F%B3-012006015.html
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
- 事件10：Lisa Cook lawyer signals Fed governor won't attend Trump committee's hearing
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 16:03:38 GMT；台北時間：2026-11-18 00:03
  - 摘要：Cook's attorney sounded more hostile than ever in his first known letter to be sent in the matter since the GOP's drubbing in the Nov. 3 midterm elect
  - 原文連結：https://www.cnbc.com/2026/11/17/lisa-cook-trump-fed-committee-hearing.html
- 事件11：St. Louis Fed's Musalem says four more rate hikes may be needed in coming months
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 13:40:54 GMT；台北時間：2026-11-17 21:40
  - 摘要：The forecast represents one of the most hawkish views among policymakers.
  - 原文連結：https://www.cnbc.com/2026/11/17/alberto-musalem-fed-interest-rates.html
- 事件12：Want to earn 5% on shorter-term Treasurys again? Watch for this shift.
  - 來源：MarketWatch；發布時間：Tue, 17 Nov 2026 22:08:00 GMT；台北時間：2026-11-18 06:08
  - 摘要：Don&#x2019;t rule out a half-point interest-rate hike in December, BofA Global&#x2019;s rates team said.
  - 原文連結：https://www.marketwatch.com/story/want-to-earn-5-on-shorter-term-treasurys-again-watch-for-this-shift-d6ff42f2?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-17

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 40,590 | TAIFEX Proxy |
| 最高價 | 41,828 | TAIFEX Proxy |
| 最低價 | 39,761 | TAIFEX Proxy |
| 收盤價 | 40,073 | TAIFEX Proxy |
| 漲跌點數 | -708 | TAIFEX Proxy |
| 漲跌幅 | -1.74 | TAIFEX Proxy |
| 成交量 | 138,833 | TAIFEX Proxy |
| 日盤高點及低點 | 41,828 / 39,761 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 40,050 | TAIFEX Proxy |
| 最高價 | 40,451 | TAIFEX Proxy |
| 最低價 | 39,010 | TAIFEX Proxy |
| 收盤價 | 39,792 | TAIFEX Proxy |
| 漲跌點數 | -219 | TAIFEX Proxy |
| 漲跌幅 | -0.55 | TAIFEX Proxy |
| 成交量 | 48,144 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,451 / 39,010 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 17,052 | TAIFEX Proxy |
| 外資空方 OI | 114,948 | TAIFEX Proxy |
| 外資多空淨 OI | -97,896 | TAIFEX Proxy |
| 投信多方 OI | 94,566 | TAIFEX Proxy |
| 投信空方 OI | 3,340 | TAIFEX Proxy |
| 投信多空淨 OI | +91,226 | TAIFEX Proxy |
| 自營商多方 OI | 5,052 | TAIFEX Proxy |
| 自營商空方 OI | 5,488 | TAIFEX Proxy |
| 自營商多空淨 OI | -436 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,670 | TAIFEX Proxy |
| 三大法人合計空方 OI | 123,776 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,106 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,109 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -1,180 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,595 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 11,821 | TAIFEX Proxy |
| 前十大交易人空方 OI | 13,502 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,681 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-13→2026-11-17) | -21,237 | TAIFEX Proxy snapshots (2026-11-16) |
- 資料日期：2026-11-17 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 153,931 | TAIFEX Proxy |
| 外資日盤空單交易量 | 155,075 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,144 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 31,220 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 31,285 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -65 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,079 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -1,180 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -1,180 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,820 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -333 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,487 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -4,144 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -398 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -341.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -31.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,073 | TAIFEX Proxy |
| 加權指數價格 | 40,092.11 | twse-proxy |
| 台指期與加權指數價差 | -19.11 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.05 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -19.11 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -281 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,073 | 39,792 | +281 | TAIFEX Proxy |
| 成交量 | 138,833 | 48,144 | +90,689 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-3,884（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 153,931 | 155,075 | -1,144 | 31,220 | 31,285 | -65 | -1,079 | 17,052 | 114,948 | -97,896 | -1,109 | TAIFEX Proxy |
| 投信 | 33,611 | 34,791 | -1,180 | 0 | 0 | +0 | -1,180 | 94,566 | 3,340 | +91,226 | -1,180 | TAIFEX Proxy |
| 自營商 | 15,358 | 17,178 | -1,820 | 2,221 | 2,554 | -333 | -1,487 | 5,052 | 5,488 | -436 | -1,595 | TAIFEX Proxy |
| 三大法人合計 | 202,900 | 207,044 | -4,144 | 33,441 | 33,839 | -398 | -3,746 | 116,670 | 123,776 | -7,106 | -3,884 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 11,821 | TAIFEX Proxy |
| 前十大交易人空方 OI | 13,502 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,681 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-13→2026-11-17) | -21,237 | TAIFEX Proxy snapshots (2026-11-16) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 25.75% | TAIFEX Proxy |
| 夜盤漲跌點數 | -219 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -65 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-17 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-18 13:04:29 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 258,518 | TAIFEX Proxy |
| Call 總未平倉量 OI | 142,228 | TAIFEX Proxy |
| Call OI 增減 (2026-11-16→2026-11-17) | +29,237 | TAIFEX Proxy snapshots (2026-11-16) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 206,995 | TAIFEX Proxy |
| Put 總未平倉量 OI | 78,316 | TAIFEX Proxy |
| Put OI 增減 (2026-11-16→2026-11-17) | +18,610 | TAIFEX Proxy snapshots (2026-11-16) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.25 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.82 | TAIFEX Proxy |
| Put／Call Ratio | 0.55 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-16→2026-11-17) | -2.06 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-16→2026-11-17) | 0.29 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 66,734 | TAIFEX Proxy |
| 外資 Call日賣 | 64,552 | TAIFEX Proxy |
| 外資 Call日淨 | +2,182 | TAIFEX Proxy |
| 外資 Put日買 | 68,854 | TAIFEX Proxy |
| 外資 Put日賣 | 68,672 | TAIFEX Proxy |
| 外資 Put日淨 | +182 | TAIFEX Proxy |
| 外資 Call夜買 | 38,353 | TAIFEX Proxy |
| 外資 Call夜賣 | 38,714 | TAIFEX Proxy |
| 外資 Call夜淨 | -361 | TAIFEX Proxy |
| 外資 Put夜買 | 42,433 | TAIFEX Proxy |
| 外資 Put夜賣 | 43,290 | TAIFEX Proxy |
| 外資 Put夜淨 | -857 | TAIFEX Proxy |
| 外資 日盤淨總量 | +2,000 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2,543 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,039 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 69,887 | TAIFEX Proxy |
| 自營商 Call日賣 | 73,892 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,005 | TAIFEX Proxy |
| 自營商 Put日買 | 64,742 | TAIFEX Proxy |
| 自營商 Put日賣 | 64,997 | TAIFEX Proxy |
| 自營商 Put日淨 | -255 | TAIFEX Proxy |
| 自營商 Call夜買 | 16,423 | TAIFEX Proxy |
| 自營商 Call夜賣 | 21,018 | TAIFEX Proxy |
| 自營商 Call夜淨 | -4,595 | TAIFEX Proxy |
| 自營商 Put夜買 | 21,410 | TAIFEX Proxy |
| 自營商 Put夜賣 | 23,146 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,736 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -3,750 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +590 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +1,481 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,984 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,500 | 6,804 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 6,330 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,984 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,984 | 6.32% | TAIFEX Proxy |
| C2 | 43,500 | 6,804 | 4.78% | TAIFEX Proxy |
| C3 | 44,000 | 6,330 | 4.45% | TAIFEX Proxy |
| C4 | 45,000 | 4,173 | 2.93% | TAIFEX Proxy |
| C5 | 48,000 | 3,871 | 2.72% | TAIFEX Proxy |
| C6 | 43,000 | 3,538 | 2.49% | TAIFEX Proxy |
| C7 | 47,500 | 3,524 | 2.48% | TAIFEX Proxy |
| C8 | 46,500 | 3,464 | 2.44% | TAIFEX Proxy |
| C9 | 47,000 | 3,313 | 2.33% | TAIFEX Proxy |
| C10 | 44,500 | 2,816 | 1.98% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 11,788 | TAIFEX Proxy |
| Put OI 第2大履約價 | 38,000 | 2,997 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 2,889 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 11,788 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 11,788 | 15.05% | TAIFEX Proxy |
| P2 | 38,000 | 2,997 | 3.83% | TAIFEX Proxy |
| P3 | 40,000 | 2,889 | 3.69% | TAIFEX Proxy |
| P4 | 36,000 | 2,750 | 3.51% | TAIFEX Proxy |
| P5 | 37,000 | 2,241 | 2.86% | TAIFEX Proxy |
| P6 | 39,000 | 2,213 | 2.83% | TAIFEX Proxy |
| P7 | 42,000 | 1,959 | 2.5% | TAIFEX Proxy |
| P8 | 36,500 | 1,789 | 2.28% | TAIFEX Proxy |
| P9 | 35,000 | 1,568 | 2.0% | TAIFEX Proxy |
| P10 | 44,000 | 1,536 | 1.96% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 43,500 (+5,478) | TAIFEX Proxy snapshots (2026-11-16) |
| Call OI 減少最多的履約價 | 47,500 (-4,350) | TAIFEX Proxy snapshots (2026-11-16) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 33,700 (+3,323) | TAIFEX Proxy snapshots (2026-11-16) |
| Put OI 減少最多的履約價 | 40,600 (-406) | TAIFEX Proxy snapshots (2026-11-16) |

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
| Gamma Wall 價位 | 40,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-17 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 40,423.40 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-17 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,600 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | -1,500 | TAIFEX Proxy snapshots (2026-11-16) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 135,406 | 133,406 | +2,000 | 81,643 | 81,147 | +496 | +1,504 | TAIFEX Proxy |
| 投信 | 8,005 | 18,220 | -10,215 | 0 | 0 | +0 | -10,215 | TAIFEX Proxy |
| 自營商 | 134,884 | 138,634 | -3,750 | 39,569 | 42,428 | -2,859 | -891 | TAIFEX Proxy |
| 三大法人合計 | 278,295 | 290,260 | -11,965 | 121,212 | 123,575 | -2,363 | -9,602 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 24.03 | 21.58 | +2.45 | 11.33 | 10.97 | +0.35 | +2.10 | TAIFEX Proxy |
| 投信 | 0.17 | 11.21 | -11.04 | 0.00 | 0.00 | +0 | -11.04 | TAIFEX Proxy |
| 自營商 | 29.03 | 21.62 | +7.41 | 7.19 | 7.48 | -0.29 | +7.70 | TAIFEX Proxy |
| 三大法人合計 | 53.23 | 54.40 | -1.18 | 18.52 | 18.45 | +0.06 | -1.24 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 56,585 | TAIFEX Proxy |
| 買權空方 OI | 89,839 | TAIFEX Proxy |
| 買權多空淨 OI | -33,254 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-13→2026-11-17) | -26,342 | TAIFEX Proxy snapshots (2026-11-16) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 40,929 | TAIFEX Proxy |
| 賣權空方 OI | 36,173 | TAIFEX Proxy |
| 賣權多空淨 OI | +4,756 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-13→2026-11-17) | +2,345 | TAIFEX Proxy snapshots (2026-11-16) |
- 資料日期：買權 2026-11-17／賣權 2026-11-17 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -21,237 | 2026-11-13→2026-11-17 | TAIFEX Proxy snapshots (2026-11-16) |
| 買權前十大 | -26,342 | 2026-11-13→2026-11-17 | TAIFEX Proxy snapshots (2026-11-16) |
| 賣權前十大 | +2,345 | 2026-11-13→2026-11-17 | TAIFEX Proxy snapshots (2026-11-16) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-17；資料時間：2026-11-18 13:04:29；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：futures.gamma_wall, futures.gamma_flip
- 註記：futures-price-after-hours 日期 2026-11-17 非今日 2026-11-18，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
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
| 外資 | -380.9 | -97,896 | -1,144 | -65 | +2,000 | +496 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -38.2 | +91,226 | -1,180 | +0 | -10,215 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -157.0 | -436 | -1,820 | -333 | -3,750 | -2,859 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
