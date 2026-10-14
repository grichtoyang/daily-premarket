# DATA_REPORT_20261013

- 報告日期：`2026-10-14`
- T0 交易日期：`2026-10-13`
- 資料產出時間：`2026-10-14 10:58:34`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,341.31 | 點 | twse-proxy |
| 開盤 | 49,126.27 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,126.27 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,066.36 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,341.31 | 點 | twse-proxy |
| 漲跌點數 | -960.65 | 點 | twse-proxy |
| 漲跌幅 | -1.95 | % | twse-proxy |
| 成交金額 | 12,018.6 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 269 | twse-proxy |
| 下跌家數 | 730 | twse-proxy |
| 平盤家數 | 78 | twse-proxy |
| 漲停家數 | 13 | twse-proxy |
| 跌停家數 | 5 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 175 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 610 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 83 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 11 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 8 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,652.9 | 億元 | twse-proxy /institutional |
| 投信 | +246.3 | 億元 | twse-proxy /institutional |
| 自營商 | -569.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,976.4 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,681.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -135.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 261,127 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 7,332 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 196.16 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-12；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,497,780 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 35,668 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,938 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 12,018.6 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,484.6 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,503.2 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,805.45 | -1.79 | -0.02 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,204.38 | -41.52 | -0.15 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,569.48 | -95.22 | -0.31 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,670.10 | -180.45 | -0.35 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,208.79 | -28.00 | -0.23 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.27 | 0.06 | +0.39 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 68,016.70 | -1,014.22 | -1.47 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,119.08 | -265.16 | -4.15 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,271.20 | 59.85 | +0.25 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,797.24 | -16.55 | -0.43 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,384.87 | -256.99 | -2.03 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,856.25 | -1.75 | -0.02 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,806.00 | -92.25 | -0.30 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,890.00 | -220.00 | -0.42 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,800.90 | -11.30 | -0.40 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.79 | -0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.22 | -0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.56 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.11 | 0.18 | +0.57 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.16 | -0.42 | -0.41 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.33 | -0.19 | -0.12 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,338.78 | 4.65 | +0.35 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 444.35 | -8.96 | -1.98 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 22.55 | -0.41 | -1.79 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.53 | 1.10 | +2.37 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 94.87 | 1.13 | +1.21 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,185.90 | -4.70 | -0.11 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,344.78 | 1,582.22 | +1.94 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：高點進場一張蒸發69萬⋯聯發科連6跌分析師點止跌訊號
  - 來源：Yahoo 台股；發布時間：2026-10-14T01:58:42Z；台北時間：2026-10-14 09:58
  - 摘要：「發哥」連跌六天，套在 5,165 元高點的學長姐還有救嗎？IC 設計大廠聯發科（2454）今（14）日盤中賣壓湧現，一度下跌50元至4,475元，寫下近一個月盤中新低。統計顯示聯發科已連續走跌六日；若先前進場的4.62萬名新股東買在5,1
  - 原文連結：https://tw.stock.yahoo.com/news/5165%E5%A5%97%E6%88%BF%E5%AD%B8%E9%95%B7%E5%A7%90%E9%82%84%E6%9C%89%E6%95%91%E5%97%8E%EF%BC%9F%E8%81%AF%E7%99%BC%E7%A7%91%E9%80%A36%E8%B7%8C%E3%80%8C%E6%9C%80%E6%85%98%E8%92%B8%E7%99%BC69-%E8%90%AC%E5%85%83%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E6%8F%AD%E6%AD%A2%E8%B7%8C%E8%A8%8A%E8%99%9F-020031052.html
- 事件2：台塑四寶亮三顆紅燈 市值暴增4400億相當於一家統一
  - 來源：Yahoo 台股；發布時間：2026-10-14T02:42:31Z；台北時間：2026-10-14 10:42
  - 摘要：台塑四寶「大象也起舞」引市場側目，今（14）日一飛衝天，其中台塑（1301）、南亞（1303）、台化（1326）3檔連袂亮燈漲停，台化有2萬多張排隊等買，台塑化（6505）一度大漲8%以上，以盤中最高價計，四寶市值從前一天的4.63兆元暴增
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E5%A1%91%E5%9B%9B%E5%AF%B6%E4%BA%AE3%E7%87%88-%E5%B8%82%E5%80%BC%E4%B8%80%E5%A4%A9%E7%88%86%E5%A2%9E4400%E5%84%84%E5%85%83%E7%9B%B8%E7%95%B6%E4%B8%80%E5%AE%B6%E7%B5%B1%E4%B8%80-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E8%A3%9C%E6%BC%B2%E3%80%8C%E4%B8%80%E9%BC%93%E4%BD%9C%E6%B0%A3%E3%80%8D-025018343.html
- 事件3：散熱四雄9月、Q3業績比一比 法人不推雙鴻有原因
  - 來源：Yahoo 台股；發布時間：2026-10-13T22:00:30Z；台北時間：2026-10-14 06:00
  - 摘要：AI強勁無法擋，輝達VR伺服器、Google TPU V8、亞馬遜AWS T3都將開始放量，法人看好VR200、ASIC伺服器和光模組出貨動能強勁，評析「散熱4雄」奇鋐、雙鴻、健策、富世達等，9月營收大致符合預期，健策新品TR Lid也將開
  - 原文連結：https://tw.stock.yahoo.com/news/9%E6%9C%88%E7%87%9F%E6%94%B61%E6%AC%A1%E8%A9%95-%E5%A5%87%E9%8B%90-%E9%9B%99%E9%B4%BB-%E5%81%A5%E7%AD%96-%E5%AF%8C%E4%B8%96%E9%81%94-220030598.html
- 事件4：外資目標喊上4410天價 台積電甩連4跌重返2500元
  - 來源：Yahoo 台股；發布時間：2026-10-14T01:27:46Z；台北時間：2026-10-14 09:27
  - 摘要：外資相繼上調台積電目標價，市場喊價甚至衝上3,088元至4,410元天價，台積電（2330）今（14）日一甩連四日下跌陰霾，盤中最高觸及2,510 元，上漲45元，來到2535元，成功重返2,500元關卡，分析師表示，台積電短線偏多看待，股
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%96%8A%E5%88%B04410%E5%85%83%E5%A4%A9%E5%83%B9%EF%BC%81%E5%8F%B0%E7%A9%8D%E9%9B%BB%E4%B8%80%E7%94%A9%E9%80%A34%E8%B7%8C-%E6%BC%B245%E5%85%83%E9%87%8D%E8%BF%942500%E5%85%83%E9%97%9C%E5%8D%A1-012746961.html
- 事件5：台玻攻頂鎖不住 金融、光電等表現較疲弱
  - 來源：Yahoo 台股；發布時間：2026-10-14T01:50:00Z；台北時間：2026-10-14 09:50
  - 摘要：[FTNN新聞網]記者薛明峻／台北報導美股四大指數周二全面收黑，但AI晶片龍頭輝達（NVDA-US）勁揚0.97%、台積電ADR則上漲0.17%，激勵台股今（14）日開高，開盤...
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%AD%E6%8E%A2%E9%87%9D-%E9%9A%B4%E8%8F%AF-%E9%9B%B7%E7%AC%9B%E5%85%8B%E5%85%89%E5%AD%B8%E5%86%8D%E9%A3%86%E6%BC%B2%E5%81%9C-%E9%9B%BB%E5%AD%90%E8%82%A1%E9%8A%98%E6%97%BA%E7%A7%91-%E4%BA%9E%E9%9B%BB%E9%BD%8A%E4%BA%AE%E7%87%88-015000524.html
- 事件6：黃仁勳捧450億幫赴美建廠 京元電利多不漲跌3%
  - 來源：Yahoo 台股；發布時間：2026-10-14T01:44:54Z；台北時間：2026-10-14 09:44
  - 摘要：利多不漲？AI教父黃仁勳創辦的輝達Nvidia「捧」450億元，首度以「預付款」方式支持京元電（2449）赴美國投資設廠，但今早不敵美科技下跌大環境，呈現利多不漲，股價反而下跌近3%，跌破300元整數關卡，一度跌到最低295元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%88%A9%E5%A4%9A%E4%B8%8D%E6%BC%B2%EF%BC%9F%E9%BB%83%E4%BB%81%E5%8B%B3%E6%8D%A7450%E5%84%84%E5%85%83%E5%B9%AB%E5%BB%BA%E5%BB%A0-%E4%BA%AC%E5%85%83%E9%9B%BB%E7%85%A7%E8%B7%8C3%E5%A4%B1%E5%AE%88300%E5%85%83-014454431.html
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
- 事件10：Singapore third-quarter GDP growth softens from four-year high but beats estimates
  - 來源：CNBC；發布時間：Wed, 14 Oct 2026 00:28:34 GMT；台北時間：2026-10-14 08:28
  - 摘要：The GDP print beat expectations of a 5% growth from economists polled by Reuters.
  - 原文連結：https://www.cnbc.com/2026/10/14/singapore-gdp-q3.html
- 事件11：The latest inflation data is expected to show price increases are accelerating
  - 來源：CNBC；發布時間：Tue, 13 Oct 2026 18:05:57 GMT；台北時間：2026-10-14 02:05
  - 摘要：Economists expect the consumer price index for September to rise 0.6% on the month and 3.6% year over year.
  - 原文連結：https://www.cnbc.com/2026/10/13/september-consumer-price-index-inflation.html
- 事件12：Don't let inflation bite — how to hedge with TIPS, commodities and infrastructure funds
  - 來源：CNBC；發布時間：Tue, 13 Oct 2026 20:52:22 GMT；台北時間：2026-10-14 04:52
  - 摘要：TIPS are looking attractive but they aren't the only way to get inflation protection.
  - 原文連結：https://www.cnbc.com/2026/10/13/inflation-hedge-tips-commodities-infrastructure.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-13

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,606 | TAIFEX Proxy |
| 最高價 | 48,793 | TAIFEX Proxy |
| 最低價 | 48,240 | TAIFEX Proxy |
| 收盤價 | 48,400 | TAIFEX Proxy |
| 漲跌點數 | -945 | TAIFEX Proxy |
| 漲跌幅 | -1.92 | TAIFEX Proxy |
| 成交量 | 78,260 | TAIFEX Proxy |
| 日盤高點及低點 | 48,793 / 48,240 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,433 | TAIFEX Proxy |
| 最高價 | 48,873 | TAIFEX Proxy |
| 最低價 | 48,357 | TAIFEX Proxy |
| 收盤價 | 48,755 | TAIFEX Proxy |
| 漲跌點數 | +363 | TAIFEX Proxy |
| 漲跌幅 | +0.75 | TAIFEX Proxy |
| 成交量 | 21,801 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,873 / 48,357 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,640 | TAIFEX Proxy |
| 外資空方 OI | 97,879 | TAIFEX Proxy |
| 外資多空淨 OI | -87,239 | TAIFEX Proxy |
| 投信多方 OI | 80,555 | TAIFEX Proxy |
| 投信空方 OI | 2,717 | TAIFEX Proxy |
| 投信多空淨 OI | +77,838 | TAIFEX Proxy |
| 自營商多方 OI | 5,311 | TAIFEX Proxy |
| 自營商空方 OI | 3,820 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,491 | TAIFEX Proxy |
| 三大法人合計多方 OI | 96,506 | TAIFEX Proxy |
| 三大法人合計空方 OI | 104,416 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,910 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -4,433 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +990 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,344 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,061 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,208 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,853 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-08→2026-10-13) | +1,229 | TAIFEX Proxy snapshots (2026-10-12) |
- 資料日期：2026-10-13 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 43,511 | TAIFEX Proxy |
| 外資日盤空單交易量 | 47,878 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,367 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 11,928 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 10,784 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,144 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -5,511 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +990 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +990 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,194 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -234 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,428 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,183 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +910 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -212.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +88.9 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,400 | TAIFEX Proxy |
| 加權指數價格 | 48,341.31 | twse-proxy |
| 台指期與加權指數價差 | +58.69 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.12 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +58.69 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +355 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,400 | 48,755 | -355 | TAIFEX Proxy |
| 成交量 | 58,479 | 21,801 | +36,678 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,099（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 43,511 | 47,878 | -4,367 | 11,928 | 10,784 | +1,144 | -5,511 | 10,640 | 97,879 | -87,239 | -4,433 | TAIFEX Proxy |
| 投信 | 1,192 | 202 | +990 | 0 | 0 | +0 | +990 | 80,555 | 2,717 | +77,838 | +990 | TAIFEX Proxy |
| 自營商 | 9,429 | 8,235 | +1,194 | 1,282 | 1,516 | -234 | +1,428 | 5,311 | 3,820 | +1,491 | +1,344 | TAIFEX Proxy |
| 三大法人合計 | 54,132 | 56,315 | -2,183 | 13,210 | 12,300 | +910 | -3,093 | 96,506 | 104,416 | -7,910 | -2,099 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,061 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,208 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,853 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-08→2026-10-13) | +1,229 | TAIFEX Proxy snapshots (2026-10-12) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 27.16% | TAIFEX Proxy |
| 夜盤漲跌點數 | +363 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,144 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-13 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-14 08:27:02 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 204,709 | TAIFEX Proxy |
| Call 總未平倉量 OI | 59,595 | TAIFEX Proxy |
| Call OI 增減 (2026-10-12→2026-10-13) | +33,721 | TAIFEX Proxy snapshots (2026-10-12) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 187,837 | TAIFEX Proxy |
| Put 總未平倉量 OI | 35,474 | TAIFEX Proxy |
| Put OI 增減 (2026-10-12→2026-10-13) | +17,812 | TAIFEX Proxy snapshots (2026-10-12) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.09 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.68 | TAIFEX Proxy |
| Put／Call Ratio | 0.60 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-12→2026-10-13) | -13.59 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-12→2026-10-13) | -15.83 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 55,263 | TAIFEX Proxy |
| 外資 Call日賣 | 54,937 | TAIFEX Proxy |
| 外資 Call日淨 | +326 | TAIFEX Proxy |
| 外資 Put日買 | 70,926 | TAIFEX Proxy |
| 外資 Put日賣 | 70,013 | TAIFEX Proxy |
| 外資 Put日淨 | +913 | TAIFEX Proxy |
| 外資 Call夜買 | 31,873 | TAIFEX Proxy |
| 外資 Call夜賣 | 31,834 | TAIFEX Proxy |
| 外資 Call夜淨 | +39 | TAIFEX Proxy |
| 外資 Put夜買 | 37,968 | TAIFEX Proxy |
| 外資 Put夜賣 | 38,043 | TAIFEX Proxy |
| 外資 Put夜淨 | -75 | TAIFEX Proxy |
| 外資 日盤淨總量 | -587 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +287 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +988 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 70,563 | TAIFEX Proxy |
| 自營商 Call日賣 | 65,811 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,752 | TAIFEX Proxy |
| 自營商 Put日買 | 58,294 | TAIFEX Proxy |
| 自營商 Put日賣 | 59,116 | TAIFEX Proxy |
| 自營商 Put日淨 | -822 | TAIFEX Proxy |
| 自營商 Call夜買 | 20,496 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,432 | TAIFEX Proxy |
| 自營商 Call夜淨 | +3,064 | TAIFEX Proxy |
| 自營商 Put夜買 | 20,295 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,627 | TAIFEX Proxy |
| 自營商 Put夜淨 | -332 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +5,574 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,688 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -490 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 50,500 | 3,690 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,000 | 2,743 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,500 | 2,277 | TAIFEX Proxy |
| Call OI 最大履約價 | 50,500 | 3,690 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 50,500 | 3,690 | 6.19% | TAIFEX Proxy |
| C2 | 49,000 | 2,743 | 4.6% | TAIFEX Proxy |
| C3 | 49,500 | 2,277 | 3.82% | TAIFEX Proxy |
| C4 | 52,500 | 2,030 | 3.41% | TAIFEX Proxy |
| C5 | 48,500 | 1,909 | 3.2% | TAIFEX Proxy |
| C6 | 50,000 | 1,818 | 3.05% | TAIFEX Proxy |
| C7 | 49,200 | 1,804 | 3.03% | TAIFEX Proxy |
| C8 | 48,900 | 1,676 | 2.81% | TAIFEX Proxy |
| C9 | 49,100 | 1,600 | 2.68% | TAIFEX Proxy |
| C10 | 48,800 | 1,582 | 2.65% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,000 | 2,116 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,000 | 1,760 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,500 | 1,561 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,000 | 2,116 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,000 | 2,116 | 5.96% | TAIFEX Proxy |
| P2 | 47,000 | 1,760 | 4.96% | TAIFEX Proxy |
| P3 | 48,500 | 1,561 | 4.4% | TAIFEX Proxy |
| P4 | 47,500 | 1,326 | 3.74% | TAIFEX Proxy |
| P5 | 48,200 | 1,320 | 3.72% | TAIFEX Proxy |
| P6 | 44,500 | 1,319 | 3.72% | TAIFEX Proxy |
| P7 | 48,300 | 1,227 | 3.46% | TAIFEX Proxy |
| P8 | 49,000 | 1,199 | 3.38% | TAIFEX Proxy |
| P9 | 48,400 | 1,082 | 3.05% | TAIFEX Proxy |
| P10 | 47,800 | 990 | 2.79% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 50,500 (+2,870) | TAIFEX Proxy snapshots (2026-10-12) |
| Call OI 減少最多的履約價 | 48,200 (-454) | TAIFEX Proxy snapshots (2026-10-12) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,000 (+1,206) | TAIFEX Proxy snapshots (2026-10-12) |
| Put OI 減少最多的履約價 | 46,200 (-60) | TAIFEX Proxy snapshots (2026-10-12) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 50,500 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-12→2026-10-13) | -2,900 | TAIFEX Proxy snapshots (2026-10-12) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-12→2026-10-13) | -1,350 | TAIFEX Proxy snapshots (2026-10-12) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 資料日期 | 2026-10-13 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,254.79 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 資料日期 | 2026-10-13 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,450 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-12→2026-10-13) | -800 | TAIFEX Proxy snapshots (2026-10-12) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 125,276 | 125,863 | -587 | 69,916 | 69,802 | +114 | -701 | TAIFEX Proxy |
| 投信 | 3,270 | 3,500 | -230 | 0 | 0 | +0 | -230 | TAIFEX Proxy |
| 自營商 | 129,679 | 124,105 | +5,574 | 41,123 | 37,727 | +3,396 | +2,178 | TAIFEX Proxy |
| 三大法人合計 | 258,225 | 253,468 | +4,757 | 111,039 | 107,529 | +3,510 | +1,247 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.50 | 9.47 | +0.04 | 4.59 | 4.55 | +0.04 | -0.00 | TAIFEX Proxy |
| 投信 | 0.76 | 2.74 | -1.99 | 0.00 | 0.00 | +0 | -1.99 | TAIFEX Proxy |
| 自營商 | 11.17 | 9.97 | +1.21 | 2.59 | 2.30 | +0.29 | +0.91 | TAIFEX Proxy |
| 三大法人合計 | 21.43 | 22.18 | -0.74 | 7.19 | 6.85 | +0.33 | -1.07 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 17,620 | TAIFEX Proxy |
| 買權空方 OI | 16,704 | TAIFEX Proxy |
| 買權多空淨 OI | +916 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-08→2026-10-13) | -606 | TAIFEX Proxy snapshots (2026-10-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,608 | TAIFEX Proxy |
| 賣權空方 OI | 10,282 | TAIFEX Proxy |
| 賣權多空淨 OI | +326 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-08→2026-10-13) | +232 | TAIFEX Proxy snapshots (2026-10-12) |
- 資料日期：買權 2026-10-13／賣權 2026-10-13 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,229 | 2026-10-08→2026-10-12 | TAIFEX Proxy snapshots (2026-10-12) |
| 買權前十大 | -606 | 2026-10-08→2026-10-13 | TAIFEX Proxy snapshots (2026-10-12) |
| 賣權前十大 | +232 | 2026-10-08→2026-10-13 | TAIFEX Proxy snapshots (2026-10-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-13；資料時間：2026-10-14 10:58:34；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：1 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 穩定：68 格新舊皆有值，沿用前版（不再靜默覆寫）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-13 非今日 2026-10-14，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-10-12；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-12)，非 T0 2026-10-13
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,652.9 | -87,239 | -4,367 | +1,144 | -587 | +114 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +246.3 | +77,838 | +990 | +0 | -230 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -569.8 | +1,491 | +1,194 | -234 | +5,574 | +3,396 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
