# DATA_REPORT_20260923

- 報告日期：`2026-09-23`
- T0 交易日期：`2026-09-23`
- 資料產出時間：`2026-09-23 22:06:21`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,157.29 | 點 | twse-proxy |
| 開盤 | 47,894.77 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,341.56 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,894.77 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,157.29 | 點 | twse-proxy |
| 漲跌點數 | 357.12 | 點 | twse-proxy |
| 漲跌幅 | +0.75 | % | twse-proxy |
| 成交金額 | 8,946.5 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 388 | twse-proxy |
| 下跌家數 | 562 | twse-proxy |
| 平盤家數 | 123 | twse-proxy |
| 漲停家數 | 15 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 344 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 412 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 112 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 16 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 3 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +373.1 | 億元 | twse-proxy /institutional |
| 投信 | -47.6 | 億元 | twse-proxy /institutional |
| 自營商 | +58.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +383.8 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,172.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +38.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 246,733 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -7,889 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 193.13 | % | wantgoo 大盤融資維持率 (資料日期 2026-09-22；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,587,321 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 33,674 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -2,109 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,946.5 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,517.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,464.4 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,733.20 | -31.50 | -0.41 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,052.89 | -69.20 | -0.26 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,519.09 | 36.74 | +0.12 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,729.03 | -319.80 | -0.61 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,508.68 | 75.51 | +0.61 | Yahoo Finance Chart API |
| VIX | ^VIX | 14.31 | -0.56 | -3.77 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,018.95 | 882.70 | +1.38 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,080.92 | 73.20 | +1.04 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,834.12 | -208.59 | -0.83 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,936.52 | -13.39 | -0.34 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,636.07 | -93.95 | -0.68 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,800.50 | -31.25 | -0.40 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,836.50 | -192.00 | -0.62 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,062.00 | -217.00 | -0.42 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,880.30 | -33.80 | -1.16 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.71 | -0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.03 | 0.07 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.35 | 0.05 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.75 | 0.01 | +0.05 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.05 | 0.62 | +0.61 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.19 | 0.82 | +0.52 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,367.09 | -6.59 | -0.48 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 447.64 | 2.49 | +0.56 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.81 | -0.62 | -2.46 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.84 | 0.11 | +0.25 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 92.05 | -2.54 | -2.69 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,320.00 | -56.40 | -1.29 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 85,662.92 | -509.36 | -0.59 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股站上4萬8新高度 台積2500元率載板散熱闖關
  - 來源：Yahoo 台股；發布時間：2026-09-23T09:15:14Z；台北時間：2026-09-23 17:15
  - 摘要：神山領軍，台股首度收上4萬8！今（23）日受美股科技與記憶體股走強激勵，加權指數早盤最高衝上48,341.56點，盤中雖因上櫃指數翻黑、部分熱門股拉回及連假前調節賣壓而收斂漲幅，終場仍上漲357.12點，收48,157.29點，創歷史收盤新
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%A6%96%E5%BA%A6%E6%94%B6%E7%9B%A4%E7%AB%99%E4%B8%8A4%E8%90%AC8%E5%A4%A7%E9%97%9C%EF%BC%81%E5%8F%B0%E7%A9%8D%E9%9B%BB2500%E5%85%83%E7%A5%9E%E5%8A%A9%E6%94%BB%E3%80%81%E8%BC%89%E6%9D%BF%E6%95%A3%E7%86%B1%E9%BD%8A%E5%BF%83%E6%8E%80%E9%96%8B%E6%94%B6%E7%9B%A4%E5%A4%A9%E8%8A%B1%E6%9D%BF%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091514719.html
- 事件2：散戶信心衝史上最強 8月證券劃撥餘額暴增近4千億
  - 來源：Yahoo 台股；發布時間：2026-09-23T09:16:46Z；台北時間：2026-09-23 17:16
  - 摘要：散戶信心強勁！8月台股上漲逾3千點，史上最強，中央銀行今（23）日公布8月金融情況，象徵散戶信心風向球的證券劃撥存款餘額飆升至近4.6兆元，一舉創下歷史新高，單月大增3,889億元也寫下史上最大增幅。此外，融資餘額同步由6,735億元推升至
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%95%A3%E6%88%B6%E4%BF%A1%E5%BF%83%E3%80%8C%E5%8F%B2%E4%B8%8A%E6%9C%80%E5%BC%B7%E3%80%8D%EF%BC%818%E6%9C%88%E8%AD%89%E5%88%B8%E5%8A%83%E6%92%A5%E9%A4%98%E9%A1%8D-%E4%B8%80%E5%8F%A3%E6%B0%A3%E5%A2%9E%E8%BF%914%E5%8D%83%E5%84%84%E5%85%83-091646472.html
- 事件3：友達昨漲停今跳水還能抱嗎？分析師揭主力防守價
  - 來源：Yahoo 台股；發布時間：2026-09-23T09:09:36Z；台北時間：2026-09-23 17:09
  - 摘要：台股熱門股，友達今（23日）出現劇烈震盪，盤中一度重挫超過8%觸及33.40元，散戶投資人哀鴻遍野，主要原因包括短線漲幅已大，籌碼面較為混亂且題材面並未實現於實際營收，乖離拉大出現回檔。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%8B%E9%81%94%E7%82%BA%E4%BD%95-%E5%BA%A6%E9%87%8D%E6%8C%AB8-%E6%95%A3%E6%88%B6%E4%B8%8D%E7%94%A8%E6%80%95-%E5%BE%8C%E5%B8%82-%E4%B8%BB%E5%8A%9B%E6%88%90%E6%9C%AC%E6%9B%9D%E5%85%89-090936650.html
- 事件4：玉山金壽險版圖推進 併購三商壽公平會點頭放行
  - 來源：Yahoo 台股；發布時間：2026-09-23T09:21:16Z；台北時間：2026-09-23 17:21
  - 摘要：公平會今天委員會議決議，玉山金融控股股份有限公司與三商美邦保險代理人股份有限公司結合案，考量沒有顯著的限制競爭疑慮，因此不禁止結合。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8E%89%E5%B1%B1%E9%87%91%E6%8E%A7%E4%BD%B5%E4%B8%89%E5%95%86%E7%BE%8E%E9%82%A6%E4%BA%BA%E5%A3%BD-%E5%85%AC%E5%B9%B3%E6%9C%83%E9%BB%9E%E9%A0%AD%E6%94%BE%E8%A1%8C-092116077.html
- 事件5：新鮮人連健保費都卡關 官方推代償專案來解圍
  - 來源：Yahoo 台股；發布時間：2026-09-23T09:17:11Z；台北時間：2026-09-23 17:17
  - 摘要：國內社會新鮮人初入社會，薪資普遍偏低，有時就連健保費都無力繳納。健保署今（23）日表示，健保署南區業務組與雲林、嘉義縣、嘉義市及台南市等4縣市社政單位合作，今年（2026）首度推動「陪青年再走一哩路」關懷專案，跨域合作與健保愛心資源，主動發
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BF%912%E8%90%AC%E6%96%B0%E9%AE%AE%E4%BA%BA-%E7%B9%B3%E4%B8%8D%E8%B5%B7%E5%81%A5%E4%BF%9D%E8%B2%BB-%E5%81%A5%E4%BF%9D%E7%BD%B2%E9%A6%96%E6%8E%A8%E4%BB%A3%E5%84%9F%E5%B0%88%E6%A1%88-%E7%B4%AF%E8%A8%88%E8%A3%9C%E5%8A%A9189%E8%90%AC-091711336.html
- 事件6：散戶恐慌下車、外資低檔狂撿？「載板大廠」遭恐慌錯殺　 內外資齊喊買進、目標價上看1575元
  - 來源：Yahoo 台股；發布時間：2026-09-23T14:00:00Z；台北時間：2026-09-23 22:00
  - 摘要：[FTNN新聞網]記者周雅琦／綜合報導載板大廠欣興（3037）日前因「洗產地」風波遭遇恐慌性賣壓，8月底一度摔出千金股行列，不過隨著事件逐步明朗，股價快速落底...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%95%A3%E6%88%B6%E6%81%90%E6%85%8C%E4%B8%8B%E8%BB%8A-%E5%A4%96%E8%B3%87%E4%BD%8E%E6%AA%94%E7%8B%82%E6%92%BF-%E8%BC%89%E6%9D%BF%E5%A4%A7%E5%BB%A0-%E9%81%AD%E6%81%90%E6%85%8C%E9%8C%AF%E6%AE%BA-%E5%85%A7%E5%A4%96%E8%B3%87%E9%BD%8A%E5%96%8A%E8%B2%B7%E9%80%B2-140000718.html
- 事件7：Federal Reserve Board announces approval of application by BancFirst Corporation
  - 來源：Federal Reserve；發布時間：Tue, 22 Sep 2026 20:30:00 GMT；台北時間：2026-09-23 04:30
  - 摘要：Federal Reserve Board announces approval of application by BancFirst Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260922a.htm
- 事件8：Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services Company, Inc., and former employee of Regions Bank
  - 來源：Federal Reserve；發布時間：Fri, 18 Sep 2026 15:00:00 GMT；台北時間：2026-09-18 23:00
  - 摘要：Federal Reserve Board issues enforcement actions with former employee of Northstar Bank, former employee of American Express Travel Related Services C
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260918a.htm
- 事件9：Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula
  - 來源：Federal Reserve；發布時間：Fri, 18 Sep 2026 15:00:00 GMT；台北時間：2026-09-18 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with SNB Bancshares and Bank of Eufaula
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260918b.htm
- 事件10：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm
- 事件11：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 來源：Federal Reserve；發布時間：Wed, 16 Sep 2026 18:00:00 GMT；台北時間：2026-09-17 02:00
  - 摘要：Federal Reserve Board and Federal Open Market Committee release economic projections from the September 15-16 FOMC meeting
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916b.htm
- 事件12：Fed's Collins warns inflation could be 'notably' higher after backing rate hike
  - 來源：CNBC；發布時間：Wed, 23 Sep 2026 07:33:14 GMT；台北時間：2026-09-23 15:33
  - 摘要：There is "an increased likelihood" of inflation staying "notably" above the Federal Reserve's 2% target, Boston Federal Reserve President Susan Collin
  - 原文連結：https://www.cnbc.com/2026/09/23/federal-reserve-inflation-interest-rates-ecb.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-23

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,529 | TAIFEX Proxy |
| 最高價 | 48,623 | TAIFEX Proxy |
| 最低價 | 48,223 | TAIFEX Proxy |
| 收盤價 | 48,336 | TAIFEX Proxy |
| 漲跌點數 | +111 | TAIFEX Proxy |
| 漲跌幅 | +0.23 | TAIFEX Proxy |
| 成交量 | 64,050 | TAIFEX Proxy |
| 日盤高點及低點 | 48,623 / 48,223 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,186 | TAIFEX Proxy |
| 最高價 | 48,647 | TAIFEX Proxy |
| 最低價 | 47,876 | TAIFEX Proxy |
| 收盤價 | 48,497 | TAIFEX Proxy |
| 漲跌點數 | +272 | TAIFEX Proxy |
| 漲跌幅 | +0.56 | TAIFEX Proxy |
| 成交量 | 31,121 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,647 / 47,876 | TAIFEX Proxy |
| 結算價 | 48,312 | TAIFEX Proxy |
| 未平倉量 | 103,311 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 10,855 | TAIFEX Proxy |
| 外資空方 OI | 86,939 | TAIFEX Proxy |
| 外資多空淨 OI | -76,084 | TAIFEX Proxy |
| 投信多方 OI | 76,472 | TAIFEX Proxy |
| 投信空方 OI | 2,913 | TAIFEX Proxy |
| 投信多空淨 OI | +73,559 | TAIFEX Proxy |
| 自營商多方 OI | 2,381 | TAIFEX Proxy |
| 自營商空方 OI | 5,437 | TAIFEX Proxy |
| 自營商多空淨 OI | -3,056 | TAIFEX Proxy |
| 三大法人合計多方 OI | 89,708 | TAIFEX Proxy |
| 三大法人合計空方 OI | 95,289 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,581 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -516 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -418 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +402 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 81,106 | TAIFEX Proxy |
| 前十大交易人空方 OI | 71,223 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,883 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-21→2026-09-22) | -880 | TAIFEX Proxy snapshots (2026-09-22) |
- 資料日期：2026-09-22 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 36,860 | TAIFEX Proxy |
| 外資日盤空單交易量 | 37,378 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -518 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 18,033 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 17,830 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +203 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -721 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -418 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -418 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +441 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +67 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +374 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -495 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +270 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -47.7 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +26.2 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,336 | TAIFEX Proxy |
| 加權指數價格 | 48,157.29 | twse-proxy |
| 台指期與加權指數價差 | +178.71 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.37 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +178.71 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +161 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,336 | 48,497 | -161 | TAIFEX Proxy |
| 成交量 | 32,929 | 31,121 | +1,808 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-532（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 36,860 | 37,378 | -518 | 18,033 | 17,830 | +203 | -721 | 10,855 | 86,939 | -76,084 | -516 | TAIFEX Proxy |
| 投信 | 15 | 433 | -418 | 0 | 0 | +0 | -418 | 76,472 | 2,913 | +73,559 | -418 | TAIFEX Proxy |
| 自營商 | 3,676 | 3,235 | +441 | 752 | 685 | +67 | +374 | 2,381 | 5,437 | -3,056 | +402 | TAIFEX Proxy |
| 三大法人合計 | 40,551 | 41,046 | -495 | 18,785 | 18,515 | +270 | -765 | 89,708 | 95,289 | -5,581 | -532 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 81,106 | TAIFEX Proxy |
| 前十大交易人空方 OI | 71,223 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,883 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-21→2026-09-22) | -880 | TAIFEX Proxy snapshots (2026-09-22) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 48.59% | TAIFEX Proxy |
| 夜盤漲跌點數 | +272 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +203 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-23 | TAIFEX Proxy |
| 到期月份／到期日 | 202609W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-23 22:06:21 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 331,766 | TAIFEX Proxy |
| Call 總未平倉量 OI | 76,151 | TAIFEX Proxy |
| Call OI 增減 (2026-09-22→2026-09-23) | +23,409 | TAIFEX Proxy snapshots (2026-09-22) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 320,315 | TAIFEX Proxy |
| Put 總未平倉量 OI | 69,699 | TAIFEX Proxy |
| Put OI 增減 (2026-09-22→2026-09-23) | +22,229 | TAIFEX Proxy snapshots (2026-09-22) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.04 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.09 | TAIFEX Proxy |
| Put／Call Ratio | 0.92 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-21→2026-09-22) | -23.70 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-21→2026-09-22) | -8.87 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 116,139 | TAIFEX Proxy |
| 外資 Call日賣 | 120,542 | TAIFEX Proxy |
| 外資 Call日淨 | -4,403 | TAIFEX Proxy |
| 外資 Put日買 | 124,642 | TAIFEX Proxy |
| 外資 Put日賣 | 124,722 | TAIFEX Proxy |
| 外資 Put日淨 | -80 | TAIFEX Proxy |
| 外資 Call夜買 | 44,859 | TAIFEX Proxy |
| 外資 Call夜賣 | 44,331 | TAIFEX Proxy |
| 外資 Call夜淨 | +528 | TAIFEX Proxy |
| 外資 Put夜買 | 46,574 | TAIFEX Proxy |
| 外資 Put夜賣 | 46,498 | TAIFEX Proxy |
| 外資 Put夜淨 | +76 | TAIFEX Proxy |
| 外資 日盤淨總量 | -4,323 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -4,931 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -156 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 77,111 | TAIFEX Proxy |
| 自營商 Call日賣 | 82,868 | TAIFEX Proxy |
| 自營商 Call日淨 | -5,757 | TAIFEX Proxy |
| 自營商 Put日買 | 73,699 | TAIFEX Proxy |
| 自營商 Put日賣 | 84,386 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,687 | TAIFEX Proxy |
| 自營商 Call夜買 | 26,508 | TAIFEX Proxy |
| 自營商 Call夜賣 | 24,150 | TAIFEX Proxy |
| 自營商 Call夜淨 | +2,358 | TAIFEX Proxy |
| 自營商 Put夜買 | 23,340 | TAIFEX Proxy |
| 自營商 Put夜賣 | 24,470 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,130 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +4,930 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -8,115 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -9,557 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,200 | 5,489 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,100 | 4,930 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,500 | 4,787 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,200 | 5,489 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,200 | 5,489 | 7.21% | TAIFEX Proxy |
| C2 | 48,100 | 4,930 | 6.47% | TAIFEX Proxy |
| C3 | 48,500 | 4,787 | 6.29% | TAIFEX Proxy |
| C4 | 48,300 | 3,675 | 4.83% | TAIFEX Proxy |
| C5 | 48,400 | 3,228 | 4.24% | TAIFEX Proxy |
| C6 | 48,150 | 3,193 | 4.19% | TAIFEX Proxy |
| C7 | 50,000 | 2,994 | 3.93% | TAIFEX Proxy |
| C8 | 49,000 | 2,899 | 3.81% | TAIFEX Proxy |
| C9 | 48,600 | 2,521 | 3.31% | TAIFEX Proxy |
| C10 | 50,500 | 2,454 | 3.22% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,000 | 6,354 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,050 | 4,120 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,800 | 3,217 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,000 | 6,354 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,000 | 6,354 | 9.12% | TAIFEX Proxy |
| P2 | 48,050 | 4,120 | 5.91% | TAIFEX Proxy |
| P3 | 47,800 | 3,217 | 4.62% | TAIFEX Proxy |
| P4 | 47,500 | 2,983 | 4.28% | TAIFEX Proxy |
| P5 | 47,900 | 2,648 | 3.8% | TAIFEX Proxy |
| P6 | 47,700 | 2,570 | 3.69% | TAIFEX Proxy |
| P7 | 48,100 | 2,247 | 3.22% | TAIFEX Proxy |
| P8 | 47,950 | 2,040 | 2.93% | TAIFEX Proxy |
| P9 | 47,000 | 1,975 | 2.83% | TAIFEX Proxy |
| P10 | 47,600 | 1,847 | 2.65% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,200 (+4,047) | TAIFEX Proxy snapshots (2026-09-22) |
| Call OI 減少最多的履約價 | 49,300 (-219) | TAIFEX Proxy snapshots (2026-09-22) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 48,000 (+4,875) | TAIFEX Proxy snapshots (2026-09-22) |
| Put OI 減少最多的履約價 | 46,400 (-967) | TAIFEX Proxy snapshots (2026-09-22) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,200 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-22→2026-09-23) | -800 | TAIFEX Proxy snapshots (2026-09-22) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-22→2026-09-23) | +500 | TAIFEX Proxy snapshots (2026-09-22) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,300.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 資料日期 | 2026-09-22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,358.07 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 資料日期 | 2026-09-22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-09-22→2026-09-23) | +300 | TAIFEX Proxy snapshots (2026-09-22) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 240,861 | 245,184 | -4,323 | 91,357 | 90,905 | +452 | -4,775 | TAIFEX Proxy |
| 投信 | 0 | 3,350 | -3,350 | 0 | 0 | +0 | -3,350 | TAIFEX Proxy |
| 自營商 | 161,497 | 156,567 | +4,930 | 50,978 | 47,490 | +3,488 | +1,442 | TAIFEX Proxy |
| 三大法人合計 | 402,358 | 405,101 | -2,743 | 142,335 | 138,395 | +3,940 | -6,683 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.46 | 11.59 | -0.13 | 5.98 | 5.93 | +0.05 | -0.19 | TAIFEX Proxy |
| 投信 | 0.00 | 2.56 | -2.56 | 0.00 | 0.00 | +0 | -2.56 | TAIFEX Proxy |
| 自營商 | 10.42 | 7.94 | +2.47 | 3.50 | 3.01 | +0.50 | +1.97 | TAIFEX Proxy |
| 三大法人合計 | 21.87 | 22.09 | -0.22 | 9.49 | 8.94 | +0.55 | -0.77 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,378 | TAIFEX Proxy |
| 買權空方 OI | 9,972 | TAIFEX Proxy |
| 買權多空淨 OI | +1,406 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-21→2026-09-22) | +129 | TAIFEX Proxy snapshots (2026-09-22) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 6,768 | TAIFEX Proxy |
| 賣權空方 OI | 7,741 | TAIFEX Proxy |
| 賣權多空淨 OI | -973 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-21→2026-09-22) | +99 | TAIFEX Proxy snapshots (2026-09-22) |
- 資料日期：買權 2026-09-22／賣權 2026-09-22 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -880 | 2026-09-21→2026-09-22 | TAIFEX Proxy snapshots (2026-09-22) |
| 買權前十大 | +129 | 2026-09-21→2026-09-22 | TAIFEX Proxy snapshots (2026-09-22) |
| 賣權前十大 | +99 | 2026-09-21→2026-09-22 | TAIFEX Proxy snapshots (2026-09-22) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-23；資料時間：2026-09-23 22:06:21；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
- 註記：Gamma 資料日期 2026-09-22 (T0 2026-09-23 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-09-22 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`wantgoo 大盤融資維持率 (資料日期 2026-09-22；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率資料日期 2026-09-22 (T0 2026-09-23 尚無，採最新可得)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +373.1 | -76,084 | -518 | +203 | -4,323 | +452 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -47.6 | +73,559 | -418 | +0 | -3,350 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +58.2 | -3,056 | +441 | +67 | +4,930 | +3,488 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
