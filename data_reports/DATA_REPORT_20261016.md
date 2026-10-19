# DATA_REPORT_20261016

- 報告日期：`2026-10-19`
- T0 交易日期：`2026-10-16`
- 資料產出時間：`2026-10-19 10:20:59`
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
| 加權指數 | 47,111.26 | 點 | twse-proxy |
| 開盤 | 46,995.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 47,520.60 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,995.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,111.26 | 點 | twse-proxy |
| 漲跌點數 | 141.39 | 點 | twse-proxy |
| 漲跌幅 | +0.30 | % | twse-proxy |
| 成交金額 | 9,938.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 684 | twse-proxy |
| 下跌家數 | 286 | twse-proxy |
| 平盤家數 | 106 | twse-proxy |
| 漲停家數 | 19 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 542 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 247 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 76 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 21 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -461.5 | 億元 | twse-proxy /institutional |
| 投信 | +110.5 | 億元 | twse-proxy /institutional |
| 自營商 | -334.1 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -685.1 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,638.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -15.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 271,848 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 9,054 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 183.39 | % | wantgoo 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,554,216 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 38,246 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 4,602 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,938.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,218.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,156.7 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,659.44 | -84.62 | -1.09 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,140.03 | -573.00 | -2.15 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,187.55 | -748.05 | -2.50 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,002.41 | -175.28 | -0.34 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,137.29 | -443.92 | -3.83 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.99 | 3.53 | +21.45 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,324.29 | 898.34 | +1.39 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,668.05 | 113.83 | +2.05 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,186.83 | 124.11 | +0.52 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,716.28 | 8.81 | +0.24 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,802.46 | -14.33 | -0.12 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,704.25 | -86.75 | -1.11 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,391.50 | -752.25 | -2.50 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,214.00 | -216.00 | -0.41 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,735.50 | -46.30 | -1.66 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.74 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.10 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.44 | 0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.43 | 0.10 | +0.31 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.84 | -0.16 | -0.16 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.99 | -0.16 | -0.10 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,329.60 | -11.35 | -0.85 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 412.61 | -9.64 | -2.28 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.82 | -1.10 | -5.26 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.53 | -2.36 | -5.63 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 101.41 | 3.44 | +3.51 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,181.10 | 11.00 | +0.26 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,485.72 | -655.74 | -0.80 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：國巨3交易日慘跌15% 最大苦主身家蒸發138億
  - 來源：Yahoo 台股；發布時間：2026-10-19T01:45:16Z；台北時間：2026-10-19 09:45
  - 摘要：被動元件族群今日承壓下挫，其中坐擁近62萬股東的國巨（2327）再度吞下半根跌停，國巨近3日連日下挫，已經跌破600元大關，最低來到529元，波段跌幅高達15%，其中最大苦主也包含國巨創辦人暨現任董事長陳泰銘，短短3日身價蒸發138億元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BF%9162%E8%90%AC%E8%82%A1%E6%9D%B1%E5%BF%83%E9%85%B8%E5%9C%8B%E5%B7%A83%E5%A4%A9%E8%B5%B0%E8%B7%8C15-%E6%9C%80%E5%A4%A7%E8%8B%A6%E4%B8%BB%E9%99%B3%E6%B3%B0%E9%8A%98%E8%BA%AB%E5%AE%B6%E4%B9%9F%E8%92%B8%E7%99%BC138%E5%84%84%E5%85%83-014516419.html
- 事件2：千金股殺聲隆隆一度剩47檔 股王信驊一張蒸發98萬
  - 來源：Yahoo 台股；發布時間：2026-10-19T01:56:28Z；台北時間：2026-10-19 09:56
  - 摘要：油價與美債殖利率維持高檔，加上市場對AI龐大資本支出能否轉化為獲利的疑慮升溫，美股四大指數全面收黑，拖累台股今（19）日盤中補跌逾860點，最低下探46,243.55點，失守4萬7千點大關。千金股殺聲隆隆一度剩47檔，「股王」信驊（5274
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8D%83%E9%87%91%E8%82%A1%E6%AE%BA%E8%81%B2%E9%9A%86%E9%9A%86%E4%B8%80%E5%BA%A6%E5%89%A947%E6%AA%94-%E8%82%A1%E7%8E%8B%E4%BF%A1%E9%A9%8A%E8%B7%8C%E8%BF%916%E3%80%8C%E4%B8%80%E5%BC%B5%E8%92%B8%E7%99%BC98%E8%90%AC%E5%85%83%E3%80%8D-015520105.html
- 事件3：台積電破季線台股早盤跌668點 台塑化逆勢漲3%
  - 來源：Yahoo 台股；發布時間：2026-10-19T01:15:00Z；台北時間：2026-10-19 09:15
  - 摘要：受美股下跌、台指期夜盤重挫千點影響，台股今（19）日開低震盪，下跌668點，來到46354點失守47K關卡，跌幅1.56%，預估成交量9000億；櫃買指數則來到388.98點，下跌11.49點，跌幅2.96%。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E4%B8%8B%E8%B7%8C668%E9%BB%9E-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E7%A0%B4%E5%AD%A3%E7%B7%9A-%E5%8F%B0%E5%A1%91%E5%8C%96%E9%80%86%E5%8B%A2%E6%BC%B23-011500767.html
- 事件4：輝達傳指定「用台積3奈米製程晶粒」韓媒：三星點頭
  - 來源：Yahoo 台股；發布時間：2026-10-18T16:51:00Z；台北時間：2026-10-19 00:51
  - 摘要：三星在晶圓代工領域上正試圖追趕台積電，不過韓媒《首爾經濟日報》（Seoul Economic Daily）今（18）日最新報導指出，輝達（NVIDIA）為了自家產品的品質一致，已要求三星、SK海力士及美光，在輝達的客製化高頻寬記憶體（NVH
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%8C%87%E5%AE%9A-%E5%BE%8B%E5%BE%97%E7%94%A8%E5%8F%B0%E7%A9%8D%E9%9B%BB3%E5%A5%88%E7%B1%B3-%E8%A8%98%E6%86%B6%E9%AB%943%E5%A4%A7%E5%BB%A0%E9%83%BD%E8%A2%AB%E9%BB%9E%E5%90%8D-%E9%9F%93%E5%AA%92-%E4%B8%89%E6%98%9F%E9%BB%9E%E9%A0%AD%E4%BA%86-165100027.html
- 事件5：央行備妥銀彈應戰匯市 近期穩匯「規模恐有百億美元」
  - 來源：Yahoo 台股；發布時間：2026-10-18T22:24:03Z；台北時間：2026-10-19 06:24
  - 摘要：台北股匯市面臨壓力測試。美股四大指數十七日全面翻黑，台指期夜盤更是暴跌逾千點，台股今天偏空氛圍急遽升溫；而外資上周大舉賣超台股匯出資金，導致新台幣匯價重貶，據了解，中央銀行內部上周五開會因應，備妥銀彈做好本周持續穩匯的準備，避免匯價過度波動
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E5%8C%AF%E9%9B%99%E8%AD%A6%E5%A0%B1-%E5%A4%AE%E8%A1%8C%E5%82%99%E5%A6%A5%E9%8A%80%E5%BD%88%E6%87%89%E6%88%B0-222403673.html
- 事件6：新台幣再重貶逾1角 日圓兌美元早盤回升157
  - 來源：Yahoo 台股；發布時間：2026-10-19T01:28:25Z；台北時間：2026-10-19 09:28
  - 摘要：[NOWNEWS今日新聞]美元指數跌破102，不過，在台股走跌之下，新台幣兌美元今（19）日早盤再重貶逾1角，一度下探32.49元。就國際匯市來看，美元指數一度跌至101.58，之後反彈來到101.9...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E5%8C%AF%E9%BD%8A%E6%8C%AB-%E6%96%B0%E5%8F%B0%E5%B9%A3%E5%86%8D%E9%87%8D%E8%B2%B6%E9%80%BE1%E8%A7%92%E8%A6%8B32-49%E5%85%83-012825511.html
- 事件7：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 來源：Federal Reserve；發布時間：Fri, 16 Oct 2026 15:00:00 GMT；台北時間：2026-10-16 23:00
  - 摘要：Federal Reserve Board announces termination of enforcement actions with Gardner Bancshares, Inc. and Small Business Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261016a.htm
- 事件8：&#x2018;Some people did everything right': I lost my home in the Great Recession. I rent in my 50s. Why is that judged as failure?
  - 來源：MarketWatch；發布時間：Sun, 18 Oct 2026 16:15:00 GMT；台北時間：2026-10-19 00:15
  - 摘要：&#x201d;I earn $110,000 a year.&#x201d;
  - 原文連結：https://www.marketwatch.com/story/i-earn-110-000-a-year-i-lost-my-home-in-the-great-recession-im-renting-in-my-50s-why-is-that-judged-as-failure-d1371d67?mod=mw_rss_topstories
- 事件9：Top Wall Street analysts are bullish on the growth potential of these 3 stocks
  - 來源：CNBC；發布時間：Sun, 18 Oct 2026 12:34:51 GMT；台北時間：2026-10-18 20:34
  - 摘要：Amid fear of rate hikes and oil prices, investors can look past volatility and track Street analysts' stock picks with strong long-term growth potenti
  - 原文連結：https://www.cnbc.com/2026/10/18/top-analysts-are-bullish-on-the-growth-potential-of-these-3-stocks.html
- 事件10：Semiconductor market to remain solid ‘at least through next year,’ South Korea finance minister says
  - 來源：CNBC；發布時間：Sun, 18 Oct 2026 11:10:44 GMT；台北時間：2026-10-18 19:10
  - 摘要：South Korea's finance minister said semiconductor growth can last at least through 2027 as supply remains tight despite a global chip sell-off.
  - 原文連結：https://www.cnbc.com/2026/10/17/south-korea-semiconductor-outlook-lee-hyoung-il.html
- 事件11：These surprising stocks could be some of the biggest drivers of S&P 500 earnings growth
  - 來源：MarketWatch；發布時間：Sun, 18 Oct 2026 14:00:00 GMT；台北時間：2026-10-18 22:00
  - 摘要：Boeing, Meta and EchoStar recorded steep charges and expenses a year ago, which are expected to make this latest quarter&#x2019;s results look especia
  - 原文連結：https://www.marketwatch.com/story/these-surprising-stocks-could-be-some-of-the-biggest-drivers-of-s-p-500-earnings-growth-ea073a07?mod=mw_rss_topstories
- 事件12：Stocks are heading for a high-stakes showdown, as strong earnings collide with rising borrowing costs
  - 來源：MarketWatch；發布時間：Sun, 18 Oct 2026 13:00:00 GMT；台北時間：2026-10-18 21:00
  - 摘要：The idea that the AI trade has been mostly immune to rising bond yields isn&#x2019;t quite right, one strategist notes.
  - 原文連結：https://www.marketwatch.com/story/stocks-are-heading-for-a-high-stakes-showdown-as-strong-earnings-collide-with-rising-borrowing-costs-6f8ea5b8?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-16

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,228 | TAIFEX Proxy |
| 最高價 | 47,634 | TAIFEX Proxy |
| 最低價 | 47,140 | TAIFEX Proxy |
| 收盤價 | 47,242 | TAIFEX Proxy |
| 漲跌點數 | +311 | TAIFEX Proxy |
| 漲跌幅 | +0.66 | TAIFEX Proxy |
| 成交量 | 104,595 | TAIFEX Proxy |
| 日盤高點及低點 | 47,634 / 47,140 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,269 | TAIFEX Proxy |
| 最高價 | 47,380 | TAIFEX Proxy |
| 最低價 | 46,107 | TAIFEX Proxy |
| 收盤價 | 46,140 | TAIFEX Proxy |
| 漲跌點數 | -1,144 | TAIFEX Proxy |
| 漲跌幅 | -2.42 | TAIFEX Proxy |
| 成交量 | 41,046 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,380 / 46,107 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,812 | TAIFEX Proxy |
| 外資空方 OI | 103,487 | TAIFEX Proxy |
| 外資多空淨 OI | -93,675 | TAIFEX Proxy |
| 投信多方 OI | 85,208 | TAIFEX Proxy |
| 投信空方 OI | 2,744 | TAIFEX Proxy |
| 投信多空淨 OI | +82,464 | TAIFEX Proxy |
| 自營商多方 OI | 7,760 | TAIFEX Proxy |
| 自營商空方 OI | 4,563 | TAIFEX Proxy |
| 自營商多空淨 OI | +3,197 | TAIFEX Proxy |
| 三大法人合計多方 OI | 102,780 | TAIFEX Proxy |
| 三大法人合計空方 OI | 110,794 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -8,014 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +3,907 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +3,535 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -3,697 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 75,382 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,888 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +2,494 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-14→2026-10-16) | -1,577 | TAIFEX Proxy snapshots (2026-10-15) |
- 資料日期：2026-10-16 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 67,924 | TAIFEX Proxy |
| 外資日盤空單交易量 | 64,083 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +3,841 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 23,937 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 21,794 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,143 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,698 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +3,535 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +3,535 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -3,677 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +87 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -3,764 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +3,699 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +2,230 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +349.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +208.2 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 47,242 | TAIFEX Proxy |
| 加權指數價格 | 47,111.26 | twse-proxy |
| 台指期與加權指數價差 | +130.74 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.28 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +130.74 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -1,102 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 47,242 | 46,140 | +1,102 | TAIFEX Proxy |
| 成交量 | 63,312 | 41,046 | +22,266 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+3,745（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 67,924 | 64,083 | +3,841 | 23,937 | 21,794 | +2,143 | +1,698 | 9,812 | 103,487 | -93,675 | +3,907 | TAIFEX Proxy |
| 投信 | 9,852 | 6,317 | +3,535 | 0 | 0 | +0 | +3,535 | 85,208 | 2,744 | +82,464 | +3,535 | TAIFEX Proxy |
| 自營商 | 7,101 | 10,778 | -3,677 | 2,159 | 2,072 | +87 | -3,764 | 7,760 | 4,563 | +3,197 | -3,697 | TAIFEX Proxy |
| 三大法人合計 | 84,877 | 81,178 | +3,699 | 26,096 | 23,866 | +2,230 | +1,469 | 102,780 | 110,794 | -8,014 | +3,745 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 75,382 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,888 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +2,494 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-14→2026-10-16) | -1,577 | TAIFEX Proxy snapshots (2026-10-15) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 39.33% | TAIFEX Proxy |
| 夜盤漲跌點數 | -1,144 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,143 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-16 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F3 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-17 13:01:48 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 389,402 | TAIFEX Proxy |
| Call 總未平倉量 OI | 89,062 | TAIFEX Proxy |
| Call OI 增減 (2026-10-15→2026-10-16) | +19,916 | TAIFEX Proxy snapshots (2026-10-15) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 358,736 | TAIFEX Proxy |
| Put 總未平倉量 OI | 68,443 | TAIFEX Proxy |
| Put OI 增減 (2026-10-15→2026-10-16) | +35,066 | TAIFEX Proxy snapshots (2026-10-15) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.09 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.30 | TAIFEX Proxy |
| Put／Call Ratio | 0.77 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-15→2026-10-16) | 13.76 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-15→2026-10-16) | 6.76 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 130,253 | TAIFEX Proxy |
| 外資 Call日賣 | 133,320 | TAIFEX Proxy |
| 外資 Call日淨 | -3,067 | TAIFEX Proxy |
| 外資 Put日買 | 132,319 | TAIFEX Proxy |
| 外資 Put日賣 | 131,672 | TAIFEX Proxy |
| 外資 Put日淨 | +647 | TAIFEX Proxy |
| 外資 Call夜買 | 26,248 | TAIFEX Proxy |
| 外資 Call夜賣 | 26,357 | TAIFEX Proxy |
| 外資 Call夜淨 | -109 | TAIFEX Proxy |
| 外資 Put夜買 | 26,085 | TAIFEX Proxy |
| 外資 Put夜賣 | 25,181 | TAIFEX Proxy |
| 外資 Put夜淨 | +904 | TAIFEX Proxy |
| 外資 日盤淨總量 | -3,714 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -2,958 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -257 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 110,650 | TAIFEX Proxy |
| 自營商 Call日賣 | 108,651 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,999 | TAIFEX Proxy |
| 自營商 Put日買 | 92,031 | TAIFEX Proxy |
| 自營商 Put日賣 | 101,003 | TAIFEX Proxy |
| 自營商 Put日淨 | -8,972 | TAIFEX Proxy |
| 自營商 Call夜買 | 23,084 | TAIFEX Proxy |
| 自營商 Call夜賣 | 23,366 | TAIFEX Proxy |
| 自營商 Call夜淨 | -282 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,090 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,527 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,437 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +10,971 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,281 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -6,535 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,500 | 7,026 | TAIFEX Proxy |
| Call OI 第2大履約價 | 52,000 | 4,083 | TAIFEX Proxy |
| Call OI 第3大履約價 | 47,300 | 3,971 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,500 | 7,026 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,500 | 7,026 | 7.89% | TAIFEX Proxy |
| C2 | 52,000 | 4,083 | 4.58% | TAIFEX Proxy |
| C3 | 47,300 | 3,971 | 4.46% | TAIFEX Proxy |
| C4 | 47,500 | 3,618 | 4.06% | TAIFEX Proxy |
| C5 | 47,400 | 3,519 | 3.95% | TAIFEX Proxy |
| C6 | 49,000 | 3,005 | 3.37% | TAIFEX Proxy |
| C7 | 48,000 | 2,886 | 3.24% | TAIFEX Proxy |
| C8 | 47,600 | 2,558 | 2.87% | TAIFEX Proxy |
| C9 | 48,200 | 2,158 | 2.42% | TAIFEX Proxy |
| C10 | 48,600 | 2,083 | 2.34% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 44,500 | 4,129 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,200 | 3,442 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,000 | 3,360 | TAIFEX Proxy |
| Put OI 最大履約價 | 44,500 | 4,129 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 44,500 | 4,129 | 6.03% | TAIFEX Proxy |
| P2 | 47,200 | 3,442 | 5.03% | TAIFEX Proxy |
| P3 | 47,000 | 3,360 | 4.91% | TAIFEX Proxy |
| P4 | 47,250 | 3,069 | 4.48% | TAIFEX Proxy |
| P5 | 47,100 | 2,829 | 4.13% | TAIFEX Proxy |
| P6 | 46,000 | 2,704 | 3.95% | TAIFEX Proxy |
| P7 | 46,500 | 2,508 | 3.66% | TAIFEX Proxy |
| P8 | 47,300 | 2,254 | 3.29% | TAIFEX Proxy |
| P9 | 46,800 | 2,208 | 3.23% | TAIFEX Proxy |
| P10 | 47,150 | 2,098 | 3.07% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 47,300 (+3,285) | TAIFEX Proxy snapshots (2026-10-15) |
| Call OI 減少最多的履約價 | 50,000 (-580) | TAIFEX Proxy snapshots (2026-10-15) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,250 (+2,918) | TAIFEX Proxy snapshots (2026-10-15) |
| Put OI 減少最多的履約價 | 47,800 (-146) | TAIFEX Proxy snapshots (2026-10-15) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-15→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-15) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 44,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-15→2026-10-16) | +0 | TAIFEX Proxy snapshots (2026-10-15) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 資料日期 | 2026-10-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,906.04 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 資料日期 | 2026-10-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,300 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-15→2026-10-16) | -50 | TAIFEX Proxy snapshots (2026-10-15) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 261,925 | 265,639 | -3,714 | 51,429 | 52,442 | -1,013 | -2,701 | TAIFEX Proxy |
| 投信 | 60 | 8,200 | -8,140 | 0 | 0 | +0 | -8,140 | TAIFEX Proxy |
| 自營商 | 211,653 | 200,682 | +10,971 | 43,611 | 41,456 | +2,155 | +8,816 | TAIFEX Proxy |
| 三大法人合計 | 473,638 | 474,521 | -883 | 95,040 | 93,898 | +1,142 | -2,025 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.71 | 13.42 | +0.28 | 6.01 | 6.03 | -0.01 | +0.30 | TAIFEX Proxy |
| 投信 | 0.03 | 5.91 | -5.88 | 0.00 | 0.00 | +0 | -5.88 | TAIFEX Proxy |
| 自營商 | 17.24 | 11.32 | +5.91 | 4.75 | 4.32 | +0.43 | +5.48 | TAIFEX Proxy |
| 三大法人合計 | 30.97 | 30.65 | +0.31 | 10.76 | 10.35 | +0.41 | -0.10 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 35,177 | TAIFEX Proxy |
| 買權空方 OI | 40,526 | TAIFEX Proxy |
| 買權多空淨 OI | -5,349 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-14→2026-10-16) | -6,346 | TAIFEX Proxy snapshots (2026-10-15) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 19,028 | TAIFEX Proxy |
| 賣權空方 OI | 15,749 | TAIFEX Proxy |
| 賣權多空淨 OI | +3,279 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-14→2026-10-16) | +2,436 | TAIFEX Proxy snapshots (2026-10-15) |
- 資料日期：買權 2026-10-16／賣權 2026-10-16 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,577 | 2026-10-14→2026-10-16 | TAIFEX Proxy snapshots (2026-10-15) |
| 買權前十大 | -6,346 | 2026-10-14→2026-10-16 | TAIFEX Proxy snapshots (2026-10-15) |
| 賣權前十大 | +2,436 | 2026-10-14→2026-10-16 | TAIFEX Proxy snapshots (2026-10-15) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-16；資料時間：2026-10-19 10:20:59；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：2 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 穩定：46 格新舊皆有值，沿用前版（不再靜默覆寫）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-16 非今日 2026-10-19，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-10-15；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-15)，非 T0 2026-10-16
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -461.5 | -93,675 | +3,841 | +2,143 | -3,714 | -1,013 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +110.5 | +82,464 | +3,535 | +0 | -8,140 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -334.1 | +3,197 | -3,677 | +87 | +10,971 | +2,155 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
