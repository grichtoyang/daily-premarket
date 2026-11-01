# DATA_REPORT_20261030

- 報告日期：`2026-11-01`
- T0 交易日期：`2026-10-30`
- 資料產出時間：`2026-11-01 12:23:06`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 45,211.83 | 點 | twse-proxy |
| 開盤 | 46,139.79 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,139.79 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 44,726.26 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 45,211.83 | 點 | twse-proxy |
| 漲跌點數 | -1,156.50 | 點 | twse-proxy |
| 漲跌幅 | -2.49 | % | twse-proxy |
| 成交金額 | 9,396.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 92 | twse-proxy |
| 下跌家數 | 941 | twse-proxy |
| 平盤家數 | 45 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 11 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 127 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 691 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 56 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 14 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 7 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,124.7 | 億元 | twse-proxy /institutional |
| 投信 | +236.2 | 億元 | twse-proxy /institutional |
| 自營商 | -513.7 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,402.2 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `TWSE 上市自建估算（資料日期：2026-10-30；估值 1238 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）；Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,287.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -151.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 233,537 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 7,084 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 171.75 | % | TWSE 上市自建估算（資料日期：2026-10-30；估值 1238 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）；Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點） |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,651,514 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,178 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,273 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,396.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,987.7 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,383.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,580.07 | -140.32 | -1.82 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,437.00 | -747.72 | -2.86 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,384.85 | -1,017.66 | -3.46 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,770.31 | -572.25 | -1.09 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,688.80 | -829.40 | -7.20 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.42 | 2.22 | +12.91 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,290.11 | -1,369.36 | -2.12 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,730.74 | -206.92 | -3.48 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,294.42 | 335.77 | +1.46 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,599.02 | -52.42 | -1.44 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,833.78 | -304.42 | -2.73 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,614.00 | -140.25 | -1.81 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,534.00 | -1,028.00 | -3.48 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,918.00 | -594.00 | -1.13 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,821.30 | -46.00 | -1.60 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.56 | -0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.93 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.31 | -0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.57 | 0.18 | +0.57 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.88 | -0.16 | -0.16 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.80 | -0.03 | -0.02 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,335.10 | -2.88 | -0.22 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 406.13 | -25.68 | -5.95 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.68 | -1.36 | -7.54 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.50 | -5.05 | -11.34 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 104.12 | 2.12 | +2.08 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,898.90 | -132.50 | -3.29 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 77,661.14 | 462.93 | +0.60 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：「地方創生利他行動168專案」獎勵金最高68萬 國發會助青年團隊持續扎根
  - 來源：Yahoo 台股；發布時間：2026-10-31T14:34:06Z；台北時間：2026-10-31 22:34
  - 摘要：68萬元是國發會「地方創生利他行動168專案」的最高獎勵金，提供給地方創生團隊申請一年期的執行計畫在今年11月底截止前，國發會一起邀請更多地方創生團隊，10月31日至11月1日於華山文創園區舉辦成果發表會暨市集活動，由青年團隊交流利他倡議行
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%B0%E6%96%B9%E5%89%B5%E7%94%9F%E5%88%A9%E4%BB%96%E8%A1%8C%E5%8B%95168%E5%B0%88%E6%A1%88-%E7%8D%8E%E5%8B%B5%E9%87%91%E6%9C%80%E9%AB%9868%E8%90%AC-%E5%9C%8B%E7%99%BC%E6%9C%83%E5%8A%A9%E9%9D%92%E5%B9%B4%E5%9C%98%E9%9A%8A%E6%8C%81%E7%BA%8C%E6%89%8E%E6%A0%B9-143406311.html
- 事件2：二哥神話破滅？聯電兩天慘崩近13%、股民嘆「準備回60元」　不敗教主曝觀點：還是可以買
  - 來源：Yahoo 台股；發布時間：2026-10-31T04:25:00Z；台北時間：2026-10-31 12:25
  - 摘要：[FTNN新聞網]記者陳宣穎／綜合報導晶圓二哥聯電（2303）法說會後股價狂跌，繼29日收在跌停價115.5元，30日再跌3.46%、收在111.5元，連2天跌幅達12.89%，此情...
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BA%8C%E5%93%A5%E7%A5%9E%E8%A9%B1%E7%A0%B4%E6%BB%85-%E8%81%AF%E9%9B%BB%E5%85%A9%E5%A4%A9%E6%85%98%E5%B4%A9%E8%BF%9113-%E8%82%A1%E6%B0%91%E5%98%86-%E6%BA%96%E5%82%99%E5%9B%9E60%E5%85%83-%E4%B8%8D%E6%95%97%E6%95%99%E4%B8%BB%E6%9B%9D%E8%A7%80%E9%BB%9E-042500633.html
- 事件3：大三生靠打工存近百萬！鎖定006208拚100張　聽長輩喊「第一桶金300萬」急問致富秘訣
  - 來源：Yahoo 台股；發布時間：2026-10-30T13:45:00Z；台北時間：2026-10-30 21:45
  - 摘要：[FTNN新聞網]記者林欣愉／綜合報導一名大三學生靠著打工、兼職家教，累積近100萬元資產，目前主要投資市值型ETF「富邦台50」（006208），長期目標是存滿100張...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E4%B8%89%E7%94%9F%E9%9D%A0%E6%89%93%E5%B7%A5%E5%AD%98%E8%BF%91%E7%99%BE%E8%90%AC-%E9%8E%96%E5%AE%9A006208%E6%8B%9A100%E5%BC%B5-%E8%81%BD%E9%95%B7%E8%BC%A9%E5%96%8A-%E7%AC%AC-%E6%A1%B6%E9%87%91300%E8%90%AC-134500368.html
- 事件4：26歲男炒股獲利！「賺400⭢340萬」快崩潰 網揭痛苦真相
  - 來源：Yahoo 台股；發布時間：2026-10-30T11:10:00Z；台北時間：2026-10-30 19:10
  - 摘要：上半年台股漲勢頻頻，近期卻屢屢震盪，投資人的心態也隨之起伏。有網友透露，上半年總資產衝到400萬，但近期因修正獲利回吐60萬，雖然仍是賺錢，感覺卻難以接受。
  - 原文連結：https://tw.stock.yahoo.com/news/26%E6%AD%B2%E7%94%B7%E7%82%92%E8%82%A1%E7%8D%B2%E5%88%A9-%E8%B3%BA400-340%E8%90%AC-%E5%BF%AB%E5%B4%A9%E6%BD%B0-%E7%B6%B2%E6%8F%AD%E7%97%9B%E8%8B%A6%E7%9C%9F%E7%9B%B8-111000895.html
- 事件5：9歲已買0050「每天看漲跌」！ 網驚：比巴菲特更早
  - 來源：Yahoo 台股；發布時間：2026-10-30T10:52:00Z；台北時間：2026-10-30 18:52
  - 摘要：近年來投資理財觀念普及，開始投資的年齡也有下降趨勢，有網友表示家中孩子雖然只有9歲，但已買了10股0050，且每天都關注動態，之後還想買台積電，引發眾人熱議。
  - 原文連結：https://tw.stock.yahoo.com/news/9%E6%AD%B2%E5%B7%B2%E8%B2%B70050-%E6%AF%8F%E5%A4%A9%E7%9C%8B%E6%BC%B2%E8%B7%8C-%E7%B6%B2%E9%A9%9A-%E6%AF%94%E5%B7%B4%E8%8F%B2%E7%89%B9%E6%9B%B4%E6%97%A9-105200516.html
- 事件6：低軌衛星綠油油！「這2檔」一度跌停暴跌8%　國巨、群創、騰輝也殺破7%
  - 來源：Yahoo 台股；發布時間：2026-10-30T10:04:00Z；台北時間：2026-10-30 18:04
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導受美股科技股重跌、市場預期聯準會升息等因素影響，台股大盤今（30）明顯殺低，加權指數收45211.33點，下跌1156.20點，跌幅...
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BD%8E%E8%BB%8C%E8%A1%9B%E6%98%9F%E7%B6%A0%E6%B2%B9%E6%B2%B9-%E9%80%992%E6%AA%94-%E5%BA%A6%E8%B7%8C%E5%81%9C%E6%9A%B4%E8%B7%8C8-%E5%9C%8B%E5%B7%A8-%E7%BE%A4%E5%89%B5-100400048.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Treasury Department announces new Series I bond rate of 5.51% for the next six months
  - 來源：CNBC；發布時間：Fri, 30 Oct 2026 17:15:53 GMT；台北時間：2026-10-31 01:15
  - 摘要：The U.S. Department of the Treasury has announced new Series I bond rates through April 2027.
  - 原文連結：https://www.cnbc.com/2026/10/30/treasury-i-bond-rate-through-april-2027.html
- 事件10：We're in our 70s. Should we pay off our 2.5% mortgage &#x2014; or put the money in a high-yield savings account?
  - 來源：MarketWatch；發布時間：Sat, 31 Oct 2026 19:00:00 GMT；台北時間：2026-11-01 03:00
  - 摘要：&#x201c;Let&#x2019;s say 10 years from now, when I&#x2019;m 84, we need a substantial amount of cash.&#x201d;
  - 原文連結：https://www.marketwatch.com/story/we-are-in-our-70s-should-we-pay-off-our-2-5-mortgage-or-build-up-our-savings-5a35e9c1?mod=mw_rss_topstories
- 事件11：Anthropic's path to the Nasdaq just got a lot bumpier
  - 來源：CNBC；發布時間：Sat, 31 Oct 2026 11:00:01 GMT；台北時間：2026-10-31 19:00
  - 摘要：Concerning projections from hyperscalers this week punished tech stocks and pushed the Nasdaq to its first three-week losing streak since March.
  - 原文連結：https://www.cnbc.com/2026/10/31/anthropic-ipo-ai-spending.html
- 事件12：Trump called out Big Oil profits. Here’s how much their refining earnings have surged since
  - 來源：CNBC；發布時間：Sat, 31 Oct 2026 06:00:02 GMT；台北時間：2026-10-31 14:00
  - 摘要：Trump criticized Big Oil for making “too much money,” but oil majors have since reported surging refining earnings as fuel supplies tightened.
  - 原文連結：https://www.cnbc.com/2026/10/31/trump-big-oil-refining-profits.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-30

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,410 | TAIFEX Proxy |
| 最高價 | 45,597 | TAIFEX Proxy |
| 最低價 | 44,908 | TAIFEX Proxy |
| 收盤價 | 45,301 | TAIFEX Proxy |
| 漲跌點數 | -1,268 | TAIFEX Proxy |
| 漲跌幅 | -2.72 | TAIFEX Proxy |
| 成交量 | 73,987 | TAIFEX Proxy |
| 日盤高點及低點 | 45,597 / 44,908 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,395 | TAIFEX Proxy |
| 最高價 | 45,420 | TAIFEX Proxy |
| 最低價 | 44,052 | TAIFEX Proxy |
| 收盤價 | 44,433 | TAIFEX Proxy |
| 漲跌點數 | -867 | TAIFEX Proxy |
| 漲跌幅 | -1.91 | TAIFEX Proxy |
| 成交量 | 44,305 | TAIFEX Proxy |
| 夜盤高點及低點 | 45,420 / 44,052 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 6,528 | TAIFEX Proxy |
| 外資空方 OI | 98,769 | TAIFEX Proxy |
| 外資多空淨 OI | -92,241 | TAIFEX Proxy |
| 投信多方 OI | 92,025 | TAIFEX Proxy |
| 投信空方 OI | 2,814 | TAIFEX Proxy |
| 投信多空淨 OI | +89,211 | TAIFEX Proxy |
| 自營商多方 OI | 6,106 | TAIFEX Proxy |
| 自營商空方 OI | 4,370 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,736 | TAIFEX Proxy |
| 三大法人合計多方 OI | 104,659 | TAIFEX Proxy |
| 三大法人合計空方 OI | 105,953 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -1,294 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,719 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,993 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +225 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 93,812 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,190 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,622 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-28→2026-10-30) | -3,281 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：2026-10-30 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 61,741 | TAIFEX Proxy |
| 外資日盤空單交易量 | 63,521 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,780 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 26,142 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 24,777 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,365 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,145 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,993 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,993 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +105 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +246 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -141 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +318 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,611 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +30.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +144.1 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 45,301 | TAIFEX Proxy |
| 加權指數價格 | 45,211.83 | twse-proxy |
| 台指期與加權指數價差 | +89.17 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.20 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +89.17 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -868 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 45,301 | 44,433 | +868 | TAIFEX Proxy |
| 成交量 | 73,987 | 44,305 | +29,682 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-501（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 61,741 | 63,521 | -1,780 | 26,142 | 24,777 | +1,365 | -3,145 | 6,528 | 98,769 | -92,241 | -2,719 | TAIFEX Proxy |
| 投信 | 2,233 | 240 | +1,993 | 0 | 0 | +0 | +1,993 | 92,025 | 2,814 | +89,211 | +1,993 | TAIFEX Proxy |
| 自營商 | 10,424 | 10,319 | +105 | 887 | 641 | +246 | -141 | 6,106 | 4,370 | +1,736 | +225 | TAIFEX Proxy |
| 三大法人合計 | 74,398 | 74,080 | +318 | 27,029 | 25,418 | +1,611 | -1,293 | 104,659 | 105,953 | -1,294 | -501 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 93,812 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,190 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,622 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-28→2026-10-30) | -3,281 | TAIFEX Proxy snapshots (2026-10-29) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 37.45% | TAIFEX Proxy |
| 夜盤漲跌點數 | -867 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,365 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-30 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F5 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-01 12:23:06 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 397,427 | TAIFEX Proxy |
| Call 總未平倉量 OI | 98,551 | TAIFEX Proxy |
| Call OI 增減 (2026-10-29→2026-10-30) | +36,035 | TAIFEX Proxy snapshots (2026-10-29) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 376,322 | TAIFEX Proxy |
| Put 總未平倉量 OI | 59,945 | TAIFEX Proxy |
| Put OI 增減 (2026-10-29→2026-10-30) | +24,893 | TAIFEX Proxy snapshots (2026-10-29) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.06 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.64 | TAIFEX Proxy |
| Put／Call Ratio | 0.61 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-29→2026-10-30) | 9.95 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-29→2026-10-30) | -1.87 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 125,368 | TAIFEX Proxy |
| 外資 Call日賣 | 124,716 | TAIFEX Proxy |
| 外資 Call日淨 | +652 | TAIFEX Proxy |
| 外資 Put日買 | 135,930 | TAIFEX Proxy |
| 外資 Put日賣 | 141,902 | TAIFEX Proxy |
| 外資 Put日淨 | -5,972 | TAIFEX Proxy |
| 外資 Call夜買 | 21,396 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,563 | TAIFEX Proxy |
| 外資 Call夜淨 | -167 | TAIFEX Proxy |
| 外資 Put夜買 | 20,402 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,475 | TAIFEX Proxy |
| 外資 Put夜淨 | -73 | TAIFEX Proxy |
| 外資 日盤淨總量 | +6,624 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +819 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -5,899 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 116,320 | TAIFEX Proxy |
| 自營商 Call日賣 | 124,878 | TAIFEX Proxy |
| 自營商 Call日淨 | -8,558 | TAIFEX Proxy |
| 自營商 Put日買 | 100,000 | TAIFEX Proxy |
| 自營商 Put日賣 | 109,900 | TAIFEX Proxy |
| 自營商 Put日淨 | -9,900 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,028 | TAIFEX Proxy |
| 自營商 Call夜賣 | 11,963 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,935 | TAIFEX Proxy |
| 自營商 Put夜買 | 11,254 | TAIFEX Proxy |
| 自營商 Put夜賣 | 11,798 | TAIFEX Proxy |
| 自營商 Put夜淨 | -544 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +1,342 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -6,623 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -9,356 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 4,116 | TAIFEX Proxy |
| Call OI 第2大履約價 | 45,300 | 4,005 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,200 | 3,905 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 4,116 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 4,116 | 4.18% | TAIFEX Proxy |
| C2 | 45,300 | 4,005 | 4.06% | TAIFEX Proxy |
| C3 | 49,200 | 3,905 | 3.96% | TAIFEX Proxy |
| C4 | 45,400 | 3,662 | 3.72% | TAIFEX Proxy |
| C5 | 45,200 | 3,499 | 3.55% | TAIFEX Proxy |
| C6 | 45,500 | 3,446 | 3.5% | TAIFEX Proxy |
| C7 | 47,000 | 3,364 | 3.41% | TAIFEX Proxy |
| C8 | 46,000 | 3,188 | 3.23% | TAIFEX Proxy |
| C9 | 45,600 | 2,845 | 2.89% | TAIFEX Proxy |
| C10 | 46,600 | 2,271 | 2.3% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 45,000 | 3,910 | TAIFEX Proxy |
| Put OI 第2大履約價 | 45,200 | 3,659 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,250 | 2,871 | TAIFEX Proxy |
| Put OI 最大履約價 | 45,000 | 3,910 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 45,000 | 3,910 | 6.52% | TAIFEX Proxy |
| P2 | 45,200 | 3,659 | 6.1% | TAIFEX Proxy |
| P3 | 45,250 | 2,871 | 4.79% | TAIFEX Proxy |
| P4 | 45,100 | 2,653 | 4.43% | TAIFEX Proxy |
| P5 | 44,500 | 2,484 | 4.14% | TAIFEX Proxy |
| P6 | 46,000 | 2,336 | 3.9% | TAIFEX Proxy |
| P7 | 45,300 | 2,128 | 3.55% | TAIFEX Proxy |
| P8 | 44,800 | 1,875 | 3.13% | TAIFEX Proxy |
| P9 | 44,900 | 1,792 | 2.99% | TAIFEX Proxy |
| P10 | 44,000 | 1,542 | 2.57% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 45,300 (+3,205) | TAIFEX Proxy snapshots (2026-10-29) |
| Call OI 減少最多的履約價 | 47,300 (-587) | TAIFEX Proxy snapshots (2026-10-29) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 45,200 (+2,632) | TAIFEX Proxy snapshots (2026-10-29) |
| Put OI 減少最多的履約價 | 45,500 (-958) | TAIFEX Proxy snapshots (2026-10-29) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-10-29) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | -1,000 | TAIFEX Proxy snapshots (2026-10-29) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 44,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 44,049.22 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 資料日期 | 2026-10-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 45,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F5 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-29→2026-10-30) | -600 | TAIFEX Proxy snapshots (2026-10-29) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 267,270 | 260,646 | +6,624 | 41,871 | 41,965 | -94 | +6,718 | TAIFEX Proxy |
| 投信 | 3,634 | 8,571 | -4,937 | 0 | 0 | +0 | -4,937 | TAIFEX Proxy |
| 自營商 | 226,220 | 224,878 | +1,342 | 21,826 | 23,217 | -1,391 | +2,733 | TAIFEX Proxy |
| 三大法人合計 | 497,124 | 494,095 | +3,029 | 63,697 | 65,182 | -1,485 | +4,514 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 16.67 | 15.79 | +0.88 | 4.88 | 4.94 | -0.06 | +0.94 | TAIFEX Proxy |
| 投信 | 0.76 | 4.37 | -3.62 | 0.00 | 0.00 | +0 | -3.62 | TAIFEX Proxy |
| 自營商 | 21.19 | 17.82 | +3.37 | 2.81 | 3.35 | -0.54 | +3.90 | TAIFEX Proxy |
| 三大法人合計 | 38.61 | 37.98 | +0.63 | 7.70 | 8.29 | -0.60 | +1.23 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 9,881 | TAIFEX Proxy |
| 買權空方 OI | 12,037 | TAIFEX Proxy |
| 買權多空淨 OI | -2,156 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-28→2026-10-30) | -1,024 | TAIFEX Proxy snapshots (2026-10-29) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,631 | TAIFEX Proxy |
| 賣權空方 OI | 10,961 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,330 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-28→2026-10-30) | -278 | TAIFEX Proxy snapshots (2026-10-29) |
- 資料日期：買權 2026-10-30／賣權 2026-10-30 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -3,281 | 2026-10-28→2026-10-30 | TAIFEX Proxy snapshots (2026-10-29) |
| 買權前十大 | -1,024 | 2026-10-28→2026-10-30 | TAIFEX Proxy snapshots (2026-10-29) |
| 賣權前十大 | -278 | 2026-10-28→2026-10-30 | TAIFEX Proxy snapshots (2026-10-29) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-30；資料時間：2026-11-01 12:23:06；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 覆蓋：4 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-30 非今日 2026-11-02，視為無新節次，不採用
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
- margin_ratio：`TWSE 上市自建估算（資料日期：2026-10-30；估值 1238 檔；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）；Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點）`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市市場維持率以 TWSE 自建計算為主；4 檔採最近有效收盤價（價格日期 20260402 至 20261030）。Blave 同 T0 交叉驗證 171.7540%，差異 0.007 個百分點。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,124.7 | -92,241 | -1,780 | +1,365 | +6,624 | -94 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +236.2 | +89,211 | +1,993 | +0 | -4,937 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -513.7 | +1,736 | +105 | +246 | +1,342 | -1,391 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
