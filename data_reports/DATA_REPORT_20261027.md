# DATA_REPORT_20261027

- 報告日期：`2026-10-28`
- T0 交易日期：`2026-10-27`
- 資料產出時間：`2026-10-28 08:58:47`
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
| 加權指數 | 46,096.23 | 點 | twse-proxy |
| 開盤 | 46,211.20 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 46,585.45 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 45,676.67 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,096.23 | 點 | twse-proxy |
| 漲跌點數 | 54.80 | 點 | twse-proxy |
| 漲跌幅 | +0.12 | % | twse-proxy |
| 成交金額 | 10,316.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 464 | twse-proxy |
| 下跌家數 | 523 | twse-proxy |
| 平盤家數 | 89 | twse-proxy |
| 漲停家數 | 9 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 307 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 491 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 74 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 13 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 9 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -80.4 | 億元 | twse-proxy /institutional |
| 投信 | +236.0 | 億元 | twse-proxy /institutional |
| 自營商 | -124.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +31.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,326.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -138.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 255,075 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 1,645 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 176.99 | % | 前值遞補 (DATA 2026-10-23；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,598,566 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,367 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 476 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,316.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,764.7 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,081.6 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,722.60 | 45.83 | +0.60 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,477.81 | 308.43 | +1.18 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,651.44 | 378.04 | +1.29 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,377.57 | 15.99 | +0.03 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,482.50 | 399.04 | +3.60 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.52 | -0.87 | -4.73 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,926.58 | 1,736.93 | +2.79 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,835.43 | 365.96 | +6.69 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,211.81 | 118.44 | +0.51 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,697.52 | 7.04 | +0.19 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,534.38 | -139.45 | -1.19 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,761.75 | 47.25 | +0.61 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,844.75 | 407.50 | +1.38 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,585.00 | 35.00 | +0.07 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,825.80 | 28.30 | +1.01 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.70 | 0.02 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.99 | 0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | 0.00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.42 | -0.11 | -0.35 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.37 | 0.41 | +0.40 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.83 | 0.30 | +0.19 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,331.98 | 7.21 | +0.54 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 424.37 | 5.86 | +1.40 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.18 | 0.29 | +1.54 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.91 | 1.22 | +3.15 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 100.40 | -1.36 | -1.34 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,073.80 | 35.40 | +0.88 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,625.57 | 618.91 | +0.77 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：日本月底起祭不銹鋼板反傾銷稅 台灣、中國都在列
  - 來源：Yahoo 台股；發布時間：2026-10-27T14:41:07Z；台北時間：2026-10-27 22:41
  - 摘要：日本政府週二（10/27）決定，將對以不正當低價出口的中國、台灣等產地的鎳系不銹鋼板徵收反傾銷稅，自本月31日起徵稅，為期5年。稅率方面，中國大陸產為27.7%或42.1%，台灣產為3.6%或20.1%。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%BF%AB%E8%A8%8A-%E8%AA%8D%E5%AE%9A%E6%A7%8B%E6%88%90%E5%82%BE%E9%8A%B7-%E6%97%A5%E6%9C%AC%E6%94%BF%E5%BA%9C%E6%9C%88%E5%BA%95%E8%B5%B7%E5%B0%8D%E5%8F%B0%E8%A3%BD%E4%B8%8D%E9%8A%B9%E9%8B%BC%E6%9D%BF%E9%96%8B%E5%BE%B5%E5%8F%8D%E5%82%BE%E9%8A%B7%E7%A8%85-144107880.html
- 事件2：注意股出列 冠西電90天飆498%、川飛本益比2500倍
  - 來源：Yahoo 台股；發布時間：2026-10-28T00:20:00Z；台北時間：2026-10-28 08:20
  - 摘要：[FTNN新聞網]記者莊蕙如／綜合報導證交所公布10月27日共22檔注意股，熱門股玉晶光（3406）、高力（8996）、禾伸堂（3026）、聯茂（6213）全數入列，其中冠西...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%80%E7%8B%82%E4%B8%8D%E6%98%AF%E8%A2%AB%E5%8B%95%E5%85%83%E4%BB%B6-%E9%80%99%E6%AA%94-90%E5%A4%A9%E6%9A%B4%E6%BC%B2498-%E7%8E%89%E6%99%B6%E5%85%8960%E5%A4%A9%E9%A3%86159-22%E6%AA%94%E6%B3%A8%E6%84%8F%E8%82%A1-002000787.html
- 事件3：半導體、記憶體族群走強 美股收高費半漲3.6%
  - 來源：Yahoo 台股；發布時間：2026-10-27T21:26:49Z；台北時間：2026-10-28 05:26
  - 摘要：美股週二收高，標普連2日上漲；那指漲1.18%，費半勁揚3.6%，道瓊僅小漲16點，油價下跌提振情緒。 Anthropic申請上市、Meta 250億美元發行認購超額5倍，AI熱度回溫；博通、AMD領漲晶片股。 財報與Fed成焦點，Alph
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E7%9B%A4%E5%BE%8C-anthropic-ipo%E7%86%B1%E6%BD%AE%E5%BB%B6%E7%87%92-%E8%B2%BB%E5%8D%8A%E6%BC%B23-6-212649535.html
- 事件4：欣興長交期設備採購 再增509億
  - 來源：Yahoo 台股；發布時間：2026-10-27T13:07:36Z；台北時間：2026-10-27 21:07
  - 摘要：IC載板龍頭欣興（3037）因國際大客戶需求強勁，今年7月大幅上修資本支出，由原規劃的340億元再向上追加197億元，總金額增加至537億元，欣興公告董事會今日決議通過長交期設備採購訂單金額再增加約新台幣509億元，資金來源為自有資金及銀行
  - 原文連結：https://tw.stock.yahoo.com/news/abf%E8%BC%89%E6%9D%BF%E9%9C%80%E6%B1%82%E5%A4%AA%E5%BC%B7-%E6%AC%A3%E8%88%88-%E9%95%B7%E4%BA%A4%E6%9C%9F%E8%A8%AD%E5%82%99%E6%8E%A1%E8%B3%BC%E5%86%8D%E5%A2%9E509%E5%84%84%E5%85%83-130736597.html
- 事件5：輝達Vera Rubin放量 鴻海訂單占比可望挑戰五成
  - 來源：Yahoo 台股；發布時間：2026-10-27T22:46:49Z；台北時間：2026-10-28 06:46
  - 摘要：業界傳出，輝達Vera Rubin新平台逐步放量，鴻海訂單占比可望挑戰五成，傲視群雄；ASIC伺服器訂單也有突破，取得更多Google與Meta訂單，帶動今、明年業績衝鋒。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94vr%E5%B9%B3%E5%8F%B0%E9%B4%BB%E6%B5%B7%E8%A8%82%E5%96%AE%E8%BA%8D%E5%A2%9E-%E6%A5%AD%E7%95%8C%E5%82%B3%E5%87%BA%E5%8D%A0%E6%AF%94%E6%8C%91%E6%88%B0%E4%BA%94%E6%88%90-224649157.html
- 事件6：中鋼前3季轉盈賺43億 9月淨利月減近2成原因曝
  - 來源：Yahoo 台股；發布時間：2026-10-27T12:15:00Z；台北時間：2026-10-27 20:15
  - 摘要：[FTNN新聞網]實習記者藍彥欣／台北報導中鋼（2002）公布最新自結損益財報，受惠於鋼鐵業銷售量增加，以及礦業投資股利的大力挹注，累計前3季合併營收達2566.7...
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%AD%E9%8B%BC%E5%89%8D3%E5%AD%A3%E7%8B%82%E8%B3%BA43%E5%84%84%E5%85%83-%E9%9B%99%E9%87%8D%E5%8E%9F%E5%9B%A0%E6%9B%9D%E5%85%89-%E8%BD%89%E8%99%A7%E7%82%BA%E7%9B%88%E4%BA%A4%E4%BA%AE%E7%9C%BC%E6%88%90%E7%B8%BE%E5%96%AE-%E6%8F%AD%E5%A4%9A%E5%9C%8B%E9%8B%BC%E5%BB%A0%E7%9B%A4%E5%83%B9%E6%8F%90%E6%BC%B2-121500285.html
- 事件7：Honda warns 50% Canada auto tariffs would be catastrophic for industry
  - 來源：CNBC；發布時間：Tue, 27 Oct 2026 17:53:47 GMT；台北時間：2026-10-28 01:53
  - 摘要：President Donald Trump has threatened to double tariffs on Canadian vehicles and parts from 25% to 50% if a trade deal is not reached between the two 
  - 原文連結：https://www.cnbc.com/2026/10/27/honda-warns-50percent-canada-auto-tariffs-would-be-catastrophic.html
- 事件8：Indian investors rush to Nvidia, SpaceX, Apple as local trading apps roll out access to U.S. stocks
  - 來源：CNBC；發布時間：Wed, 28 Oct 2026 00:14:24 GMT；台北時間：2026-10-28 08:14
  - 摘要：Major Indian brokerages are providing retail investors access to U.S. stocks at a time when the local market has been battered.
  - 原文連結：https://www.cnbc.com/2026/10/28/india-us-stocks-retail-access.html
- 事件9：From Wall Street to Silicon Valley, Anthropic IPO poised to have massive 'trickle-down effect'
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 22:50:07 GMT；台北時間：2026-10-27 06:50
  - 摘要：With the AI trade sputtering of late and interest rates on the rise, Anthropic's IPO is taking on outsized importance.
  - 原文連結：https://www.cnbc.com/2026/10/26/anthropic-ipo-might-trigger-tech-reset-if-ipo-underperforms.html
- 事件10：Retail traders buy the dip on chip stocks &#x2014; but Robinhood gets burned by the crypto market
  - 來源：MarketWatch；發布時間：Tue, 27 Oct 2026 22:51:00 GMT；台北時間：2026-10-28 06:51
  - 摘要：Robinhood CFO says market volatility didn&#x2019;t scare traders away from buying chip stocks &#x201c;that they had really done research on.&#x201d;
  - 原文連結：https://www.marketwatch.com/story/retail-traders-buy-the-dip-on-chip-stocks-but-robinhood-gets-burned-by-the-crypto-market-33cea913?mod=mw_rss_topstories
- 事件11：CoreWeave and other AI stocks rise as Anthropic restores the market's faith in sustained spending
  - 來源：MarketWatch；發布時間：Tue, 27 Oct 2026 21:41:00 GMT；台北時間：2026-10-28 05:41
  - 摘要：Now that investors have been able to dive further into Anthropic&#x2019;s IPO filing, they&#x2019;re seeing the same sorts of trends that helped buoy 
  - 原文連結：https://www.marketwatch.com/story/coreweave-and-other-ai-stocks-rise-as-anthropic-restores-the-markets-faith-in-sustained-spending-c71d7186?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-27

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,505 | TAIFEX Proxy |
| 最高價 | 46,846 | TAIFEX Proxy |
| 最低價 | 46,050 | TAIFEX Proxy |
| 收盤價 | 46,081 | TAIFEX Proxy |
| 漲跌點數 | -153 | TAIFEX Proxy |
| 漲跌幅 | -0.33 | TAIFEX Proxy |
| 成交量 | 61,110 | TAIFEX Proxy |
| 日盤高點及低點 | 46,846 / 46,050 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,080 | TAIFEX Proxy |
| 最高價 | 47,000 | TAIFEX Proxy |
| 最低價 | 46,006 | TAIFEX Proxy |
| 收盤價 | 46,880 | TAIFEX Proxy |
| 漲跌點數 | +774 | TAIFEX Proxy |
| 漲跌幅 | +1.68 | TAIFEX Proxy |
| 成交量 | 27,131 | TAIFEX Proxy |
| 夜盤高點及低點 | 47,000 / 46,006 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,755 | TAIFEX Proxy |
| 外資空方 OI | 95,798 | TAIFEX Proxy |
| 外資多空淨 OI | -86,043 | TAIFEX Proxy |
| 投信多方 OI | 87,803 | TAIFEX Proxy |
| 投信空方 OI | 2,751 | TAIFEX Proxy |
| 投信多空淨 OI | +85,052 | TAIFEX Proxy |
| 自營商多方 OI | 5,615 | TAIFEX Proxy |
| 自營商空方 OI | 4,161 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,454 | TAIFEX Proxy |
| 三大法人合計多方 OI | 103,173 | TAIFEX Proxy |
| 三大法人合計空方 OI | 102,710 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | +463 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +1,254 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,451 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,806 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 91,253 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,451 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,802 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-22→2026-10-27) | +1,778 | TAIFEX Proxy snapshots (2026-10-26) |
- 資料日期：2026-10-27 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 59,401 | TAIFEX Proxy |
| 外資日盤空單交易量 | 58,180 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,221 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 14,739 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 14,055 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +684 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +537 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,451 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,451 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,794 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +296 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -2,090 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +878 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +980 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +81.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +91.2 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,081 | TAIFEX Proxy |
| 加權指數價格 | 46,096.23 | twse-proxy |
| 台指期與加權指數價差 | -15.23 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.03 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -15.23 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +799 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,081 | 46,880 | -799 | TAIFEX Proxy |
| 成交量 | 61,110 | 27,131 | +33,979 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+899（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 59,401 | 58,180 | +1,221 | 14,739 | 14,055 | +684 | +537 | 9,755 | 95,798 | -86,043 | +1,254 | TAIFEX Proxy |
| 投信 | 1,554 | 103 | +1,451 | 0 | 0 | +0 | +1,451 | 87,803 | 2,751 | +85,052 | +1,451 | TAIFEX Proxy |
| 自營商 | 5,810 | 7,604 | -1,794 | 1,075 | 779 | +296 | -2,090 | 5,615 | 4,161 | +1,454 | -1,806 | TAIFEX Proxy |
| 三大法人合計 | 66,765 | 65,887 | +878 | 15,814 | 14,834 | +980 | -102 | 103,173 | 102,710 | +463 | +899 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 91,253 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,451 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,802 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-22→2026-10-27) | +1,778 | TAIFEX Proxy snapshots (2026-10-26) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 30.75% | TAIFEX Proxy |
| 夜盤漲跌點數 | +774 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +684 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-27 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-28 08:58:47 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 57,078 | TAIFEX Proxy |
| Call 總未平倉量 OI | 33,918 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 38,698 | TAIFEX Proxy |
| Put 總未平倉量 OI | 15,638 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.47 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.17 | TAIFEX Proxy |
| Put／Call Ratio | 0.46 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-22→2026-10-27) | 3.68 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-22→2026-10-27) | -4.22 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 103,334 | TAIFEX Proxy |
| 外資 Call日賣 | 105,869 | TAIFEX Proxy |
| 外資 Call日淨 | -2,535 | TAIFEX Proxy |
| 外資 Put日買 | 110,982 | TAIFEX Proxy |
| 外資 Put日賣 | 114,987 | TAIFEX Proxy |
| 外資 Put日淨 | -4,005 | TAIFEX Proxy |
| 外資 Call夜買 | 35,753 | TAIFEX Proxy |
| 外資 Call夜賣 | 35,804 | TAIFEX Proxy |
| 外資 Call夜淨 | -51 | TAIFEX Proxy |
| 外資 Put夜買 | 40,236 | TAIFEX Proxy |
| 外資 Put夜賣 | 40,754 | TAIFEX Proxy |
| 外資 Put夜淨 | -518 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,470 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -2,484 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -3,487 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 101,409 | TAIFEX Proxy |
| 自營商 Call日賣 | 104,219 | TAIFEX Proxy |
| 自營商 Call日淨 | -2,810 | TAIFEX Proxy |
| 自營商 Put日買 | 92,583 | TAIFEX Proxy |
| 自營商 Put日賣 | 96,369 | TAIFEX Proxy |
| 自營商 Put日淨 | -3,786 | TAIFEX Proxy |
| 自營商 Call夜買 | 26,290 | TAIFEX Proxy |
| 自營商 Call夜賣 | 25,220 | TAIFEX Proxy |
| 自營商 Call夜淨 | +1,070 | TAIFEX Proxy |
| 自營商 Put夜買 | 26,522 | TAIFEX Proxy |
| 自營商 Put夜賣 | 25,210 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,312 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +976 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -3,880 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,098 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,600 | 1,972 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,500 | 1,589 | TAIFEX Proxy |
| Call OI 第3大履約價 | 53,500 | 1,560 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,600 | 1,972 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,600 | 1,972 | 5.81% | TAIFEX Proxy |
| C2 | 48,500 | 1,589 | 4.68% | TAIFEX Proxy |
| C3 | 53,500 | 1,560 | 4.6% | TAIFEX Proxy |
| C4 | 47,000 | 1,544 | 4.55% | TAIFEX Proxy |
| C5 | 47,700 | 1,194 | 3.52% | TAIFEX Proxy |
| C6 | 48,200 | 1,095 | 3.23% | TAIFEX Proxy |
| C7 | 52,500 | 980 | 2.89% | TAIFEX Proxy |
| C8 | 46,900 | 888 | 2.62% | TAIFEX Proxy |
| C9 | 46,000 | 836 | 2.46% | TAIFEX Proxy |
| C10 | 45,000 | 801 | 2.36% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 45,000 | 1,592 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,000 | 787 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,300 | 682 | TAIFEX Proxy |
| Put OI 最大履約價 | 45,000 | 1,592 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 45,000 | 1,592 | 10.18% | TAIFEX Proxy |
| P2 | 46,000 | 787 | 5.03% | TAIFEX Proxy |
| P3 | 45,300 | 682 | 4.36% | TAIFEX Proxy |
| P4 | 44,000 | 672 | 4.3% | TAIFEX Proxy |
| P5 | 42,200 | 634 | 4.05% | TAIFEX Proxy |
| P6 | 45,800 | 629 | 4.02% | TAIFEX Proxy |
| P7 | 45,400 | 614 | 3.93% | TAIFEX Proxy |
| P8 | 45,500 | 600 | 3.84% | TAIFEX Proxy |
| P9 | 45,700 | 489 | 3.13% | TAIFEX Proxy |
| P10 | 43,000 | 471 | 3.01% | TAIFEX Proxy |


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
| Call Wall 價位 | 48,600 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 46,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 資料日期 | 2026-10-27 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 45,793.12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 資料日期 | 2026-10-27 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 45,400 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 218,321 | 216,851 | +1,470 | 76,507 | 76,040 | +467 | +1,003 | TAIFEX Proxy |
| 投信 | 0 | 4,736 | -4,736 | 0 | 0 | +0 | -4,736 | TAIFEX Proxy |
| 自營商 | 197,778 | 196,802 | +976 | 51,500 | 51,742 | -242 | +1,218 | TAIFEX Proxy |
| 三大法人合計 | 416,099 | 418,389 | -2,290 | 128,007 | 127,782 | +225 | -2,515 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.85 | 13.88 | -0.03 | 5.41 | 5.28 | +0.12 | -0.15 | TAIFEX Proxy |
| 投信 | 0.00 | 2.39 | -2.39 | 0.00 | 0.00 | +0 | -2.39 | TAIFEX Proxy |
| 自營商 | 14.98 | 13.56 | +1.42 | 3.29 | 3.32 | -0.04 | +1.46 | TAIFEX Proxy |
| 三大法人合計 | 28.83 | 29.83 | -1.00 | 8.69 | 8.61 | +0.09 | -1.09 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 7,391 | TAIFEX Proxy |
| 買權空方 OI | 9,133 | TAIFEX Proxy |
| 買權多空淨 OI | -1,742 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-22→2026-10-27) | -68 | TAIFEX Proxy snapshots (2026-10-26) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,919 | TAIFEX Proxy |
| 賣權空方 OI | 9,773 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,854 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-22→2026-10-27) | -219 | TAIFEX Proxy snapshots (2026-10-26) |
- 資料日期：買權 2026-10-27／賣權 2026-10-27 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,778 | 2026-10-22→2026-10-27 | TAIFEX Proxy snapshots (2026-10-26) |
| 買權前十大 | -68 | 2026-10-22→2026-10-27 | TAIFEX Proxy snapshots (2026-10-26) |
| 賣權前十大 | -219 | 2026-10-22→2026-10-27 | TAIFEX Proxy snapshots (2026-10-26) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-27；資料時間：2026-10-28 08:58:47；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (1)：options.chain_oi_change
- 註記：futures-price-after-hours 日期 2026-10-27 非今日 2026-10-28，視為無新節次，不採用
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
- margin_ratio：`前值遞補 (DATA 2026-10-23；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-23)，非 T0 2026-10-27
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -80.4 | -86,043 | +1,221 | +684 | +1,470 | +467 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +236.0 | +85,052 | +1,451 | +0 | -4,736 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -124.0 | +1,454 | -1,794 | +296 | +976 | -242 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
