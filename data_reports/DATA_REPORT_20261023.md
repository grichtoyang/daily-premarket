# DATA_REPORT_20261023

- 報告日期：`2026-10-27`
- T0 交易日期：`2026-10-23`
- 資料產出時間：`2026-10-27 10:51:52`
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
| 加權指數 | 46,041.43 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 46,041.43 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -846.34 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -1.81 | % | TWSE OpenAPI MI_INDEX (備援) |
| 成交金額 | unavailable | 億元 | twse-proxy market_statistics |

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
| 外資 | -815.8 | 億元 | twse-proxy /institutional |
| 投信 | +94.9 | 億元 | twse-proxy /institutional |
| 自營商 | -273.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -994.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 216,539 | 張 | HiStock |
| 融券增減 | 24,702 | 張 | HiStock |
| 融資維持率 | 176.99 | % | 前值遞補 (DATA 2026-10-22；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,465,395 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | unavailable | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | unavailable | 億元 | twse-proxy market_statistics+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,676.77 | 53.09 | +0.70 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,169.38 | 214.04 | +0.82 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,273.40 | 315.88 | +1.09 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,361.58 | 146.42 | +0.28 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,083.47 | 304.01 | +2.82 | Yahoo Finance Chart API |
| VIX | ^VIX | 18.39 | -1.06 | -5.45 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 63,381.29 | 1,191.64 | +1.92 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,690.82 | 221.35 | +4.05 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,159.67 | -52.14 | -0.22 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,695.61 | -1.91 | -0.05 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,512.48 | -21.90 | -0.19 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,724.75 | 10.25 | +0.13 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,464.50 | 27.25 | +0.09 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,664.00 | 114.00 | +0.22 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,800.90 | 3.40 | +0.12 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.68 | -0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.99 | -0.00 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.51 | -0.06 | -0.19 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.04 | 0.08 | +0.08 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.69 | 0.86 | +0.55 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,324.98 | 3.22 | +0.24 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 100.86 | -0.90 | -0.88 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,027.10 | -11.30 | -0.28 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 79,778.94 | -245.07 | -0.31 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：景碩翻黑失千金 ABF載板三雄股價大怒神
  - 來源：Yahoo 台股；發布時間：2026-10-27T02:26:38Z；台北時間：2026-10-27 10:26
  - 摘要：載板三雄今日股價一度強漲成為盤面領頭羊，南電更是衝上漲停板成為指標，不過早盤過後漲勢明顯收斂，南電紅燈熄滅漲幅只剩3%，欣興、景碩也由紅翻黑，景碩更摔破千金關，盤勢豬羊變色。
  - 原文連結：https://tw.stock.yahoo.com/news/abf%E8%BC%89%E6%9D%BF%E4%B8%89%E9%9B%84%E5%A4%A7%E6%80%92%E7%A5%9E%EF%BC%9F%E5%8D%97%E9%9B%BB%E7%B4%85%E7%87%88%E7%86%84%E6%BC%B2%E5%B9%85%E5%89%A92-%E6%99%AF%E7%A2%A9%E7%BF%BB%E9%BB%91%E9%80%80%E5%87%BA%E5%8D%83%E9%87%91%E4%BF%B1%E6%A8%82%E9%83%A8-022638089.html
- 事件2：雙虎不同調！友達衝高又翻黑群創一度漲逾4%
  - 來源：Yahoo 台股；發布時間：2026-10-27T01:56:24Z；台北時間：2026-10-27 09:56
  - 摘要：面板雙虎今（27）日早盤走勢不同調！友達（2409）開高走低，盤中一度漲逾3%，隨後賣壓出籠，由紅翻黑；反觀群創（3481）則維持紅盤，一度漲逾4%。資深台股分析師江慶財表示，友達先前漲幅已反映部分題材，目前技術面仍在整理築底階段，不排除進
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9D%A2%E6%9D%BF%E9%9B%99%E8%99%8E%E4%B8%8D%E5%90%8C%E8%AA%BF%EF%BC%81%E5%8F%8B%E9%81%94%E8%A1%9D%E9%AB%98%E7%BF%BB%E9%BB%91-%E7%BE%A4%E5%89%B5%E4%B8%80%E5%BA%A6%E6%BC%B2%E9%80%BE4-%E5%88%86%E6%9E%90%E5%B8%AB%E5%BB%BA%E8%AD%B0%E5%85%88%E8%A7%80%E6%9C%9B-021112493.html
- 事件3：市場獲利了結 比特幣跌破8萬美元
  - 來源：Yahoo 台股；發布時間：2026-10-26T22:58:13Z；台北時間：2026-10-27 06:58
  - 摘要：商傳媒｜方承業／綜合外電報導在美國聯準會（Federal Reserve）即將公布利率決策之際，加密貨幣市場昨（26）日延續跌勢，投資人風險胃納降低，比特幣（Bitcoin）盤中一度跌破 8 萬美元關卡。 根據《The Motley Foo
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E6%BA%96%E6%9C%83%E6%B1%BA%E7%AD%96%E5%89%8D%E5%A4%95%E6%B0%A3%E6%B0%9B%E5%87%9D%E9%87%8D-%E6%AF%94%E7%89%B9%E5%B9%A3%E8%B7%8C%E7%A0%B4-8-%E8%90%AC%E7%BE%8E%E5%85%83%E9%97%9C%E5%8D%A1-225813248.html
- 事件4：力積電南亞科強彈5% 分析師：抄底要再等等
  - 來源：Yahoo 台股；發布時間：2026-10-27T01:51:50Z；台北時間：2026-10-27 09:51
  - 摘要：韓股漲4%，記憶體四雄大反攻！受韓大廠SK-海力士反彈7%帶動，力積電（6770）、南亞科（2408）今（27日）早結束光復節加颱風四天連假就展開強勁漲勢，力積電一度漲5.7%站回70元大關，南亞科同漲幅站上444元，華邦電（2344）、旺
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%A8%98%E6%86%B6%E9%AB%94%E5%9B%9B%E9%9B%84%E5%A4%A7%E5%8F%8D%E6%94%BB%EF%BC%81%E5%8A%9B%E7%A9%8D%E9%9B%BB%E5%8D%97%E4%BA%9E%E7%A7%91%E5%BC%B7%E5%BD%885-%E5%8F%AF%E6%8A%84%E5%BA%95%E4%BA%86%E5%97%8E%EF%BC%9F%E5%88%86%E6%9E%90%E5%B8%AB%E5%96%8A%E5%86%8D%E7%AD%89%E7%AD%89-015150189.html
- 事件5：宏達電「VIVEE」年底將上市股價應聲登40元大關
  - 來源：Yahoo 台股；發布時間：2026-10-27T01:54:25Z；台北時間：2026-10-27 09:54
  - 摘要：全球智慧型手機與虛擬實境平台和生態系統創新設計領導者 hTC宏達電（2498），今（27）日正式揭曉全新個人AI產品VIVEE。目前已於美國開放預購，後續亦規劃拓展至台灣、日本及歐洲等市場；台灣及日本市場亦預計於今年底前陸續上市。消息一出今
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%AE%8F%E9%81%94%E9%9B%BBai%E6%96%B0%E5%93%81%E3%80%8Cvivee%E3%80%8D%E4%BA%AE%E7%9B%B8%EF%BC%81%E5%8F%B0%E7%81%A3%E6%97%A5%E6%9C%AC%E5%B9%B4%E5%BA%95%E4%B8%8A%E5%B8%82-%E4%BB%8A%E8%82%A1%E5%83%B9%E6%BC%B2%E8%BF%913%E9%87%8D%E7%99%BB40%E5%85%83%E5%A4%A7%E9%97%9C-015516070.html
- 事件6：童子賢「金孫」掛牌上市首日跌逾14% 摔破承銷價
  - 來源：Yahoo 台股；發布時間：2026-10-27T01:58:00Z；台北時間：2026-10-27 09:58
  - 摘要：和碩（4938）董事長童子賢「金孫」、旗下華擎（3515）子公司東擎科技（7710）今（27）以每股承銷價138元掛牌上市，但一開盤就跌破承銷價，盤中更一度下滑至117.5元，跌幅達14.86%，中籤的投資人慘套，若不幸賣在阿呆谷恐現賠2萬
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%80%E5%BC%B5%E8%B3%A02%E8%90%AC%E5%85%83%EF%BC%81%E7%AB%A5%E5%AD%90%E8%B3%A2%E3%80%8C%E9%87%91%E5%AD%AB%E3%80%8D%E6%9D%B1%E6%93%8E%E6%8E%9B%E7%89%8C%E4%B8%8A%E5%B8%82%E9%A6%96%E6%97%A5%E6%8C%AB%E9%80%BE14%E8%B7%8C%E7%A0%B4%E6%89%BF%E9%8A%B7%E5%83%B9-015800916.html
- 事件7：Federal Reserve is likely to hold interest rates steady in October. Here's what that means for consumers
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 18:51:23 GMT；台北時間：2026-10-27 02:51
  - 摘要：The Federal Reserve is expected to keep its overnight rate unchanged at the conclusion of its October meeting this week.
  - 原文連結：https://www.cnbc.com/2026/10/26/fed-decision-expectations-october-meeting.html
- 事件8：From Wall Street to Silicon Valley, Anthropic IPO poised to have massive 'trickle-down effect'
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 22:50:07 GMT；台北時間：2026-10-27 06:50
  - 摘要：With the AI trade sputtering of late and interest rates on the rise, Anthropic's IPO is taking on outsized importance.
  - 原文連結：https://www.cnbc.com/2026/10/26/anthropic-ipo-might-trigger-tech-reset-if-ipo-underperforms.html
- 事件9：Meta, SpaceX, Anthropic stoke the AI funding frenzy. What it means for our stocks
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 20:26:26 GMT；台北時間：2026-10-27 04:26
  - 摘要：unavailable
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/26/meta-spacex-anthropic-stoke-the-ai-funding-frenzy-what-it-means-for-our-stocks.html
- 事件10：FTC and 20 states sue Dollar General, alleging retailer overcharged shoppers
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 18:37:01 GMT；台北時間：2026-10-27 02:37
  - 摘要：The Federal Trade Commission and 20 states have filed a lawsuit against Dollar General, claiming the retailer has charged customers more than advertis
  - 原文連結：https://www.cnbc.com/2026/10/26/ftc-dollar-general-lawsuit.html
- 事件11：Brazilian stocks rocked as Lula wins presidential election, Bolsonaro reportedly refuses to concede
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 14:09:38 GMT；台北時間：2026-10-26 22:09
  - 摘要：It's the first time since Brazil returned to direct elections in 1989 that a candidate has won the final runoff after losing in the first round.
  - 原文連結：https://www.cnbc.com/2026/10/26/brazil-lula-win-presidential-election-runoff-vote.html
- 事件12：Cracking AI trade has Wall Street looking for a hedge. An ex-Citadel quant may have the answer
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 12:08:13 GMT；台北時間：2026-10-26 20:08
  - 摘要：Jasper Zhang runs Hyperbolic, a GPU exchange building a software for "physical" AI futures
  - 原文連結：https://www.cnbc.com/2026/10/26/gpu-futures-ai-hedge-hyperbolic.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-23

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,164 | TAIFEX Proxy |
| 最高價 | 47,337 | TAIFEX Proxy |
| 最低價 | 46,217 | TAIFEX Proxy |
| 收盤價 | 46,272 | TAIFEX Proxy |
| 漲跌點數 | -741 | TAIFEX Proxy |
| 漲跌幅 | -1.58 | TAIFEX Proxy |
| 成交量 | 55,226 | TAIFEX Proxy |
| 日盤高點及低點 | 47,337 / 46,217 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,270 | TAIFEX Proxy |
| 最高價 | 46,399 | TAIFEX Proxy |
| 最低價 | 45,523 | TAIFEX Proxy |
| 收盤價 | 45,654 | TAIFEX Proxy |
| 漲跌點數 | -580 | TAIFEX Proxy |
| 漲跌幅 | -1.25 | TAIFEX Proxy |
| 成交量 | 39,368 | TAIFEX Proxy |
| 夜盤高點及低點 | 46,399 / 45,523 | TAIFEX Proxy |
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
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-21→2026-10-22) | +1,334 | TAIFEX Proxy snapshots (2026-10-22) |
- 資料日期：2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 50,162 | TAIFEX Proxy |
| 外資日盤空單交易量 | 51,383 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,221 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 22,127 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 21,078 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,049 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -2,270 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -177 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -177 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,565 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +251 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,314 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +167 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,300 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +14.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +119.6 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,272 | TAIFEX Proxy |
| 加權指數價格 | 46,041.43 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +230.57 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +0.50 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +230.57 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | -618 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,272 | 45,654 | +618 | TAIFEX Proxy |
| 成交量 | 55,226 | 39,368 | +15,858 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 50,162 | 51,383 | -1,221 | 22,127 | 21,078 | +1,049 | -2,270 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 568 | 745 | -177 | 0 | 0 | +0 | -177 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 5,489 | 3,924 | +1,565 | 1,117 | 866 | +251 | +1,314 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 56,219 | 56,052 | +167 | 23,244 | 21,944 | +1,300 | -1,133 | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-21→2026-10-22) | +1,334 | TAIFEX Proxy snapshots (2026-10-22) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 41.62% | TAIFEX Proxy |
| 夜盤漲跌點數 | -580 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,049 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-23 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-27 10:51:52 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 178,535 | TAIFEX Proxy |
| Call 總未平倉量 OI | 55,024 | TAIFEX Proxy |
| Call OI 增減 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 155,316 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,411 | TAIFEX Proxy |
| Put OI 增減 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.15 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.75 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-21→2026-10-22) | -25.67 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-21→2026-10-22) | 3.32 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 45,172 | TAIFEX Proxy |
| 外資 Call日賣 | 45,054 | TAIFEX Proxy |
| 外資 Call日淨 | +118 | TAIFEX Proxy |
| 外資 Put日買 | 52,064 | TAIFEX Proxy |
| 外資 Put日賣 | 52,245 | TAIFEX Proxy |
| 外資 Put日淨 | -181 | TAIFEX Proxy |
| 外資 Call夜買 | 31,148 | TAIFEX Proxy |
| 外資 Call夜賣 | 31,095 | TAIFEX Proxy |
| 外資 Call夜淨 | +53 | TAIFEX Proxy |
| 外資 Put夜買 | 45,050 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,680 | TAIFEX Proxy |
| 外資 Put夜淨 | +370 | TAIFEX Proxy |
| 外資 日盤淨總量 | +299 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +65 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -551 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 65,292 | TAIFEX Proxy |
| 自營商 Call日賣 | 64,470 | TAIFEX Proxy |
| 自營商 Call日淨 | +822 | TAIFEX Proxy |
| 自營商 Put日買 | 52,508 | TAIFEX Proxy |
| 自營商 Put日賣 | 54,441 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,933 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,115 | TAIFEX Proxy |
| 自營商 Call夜賣 | 25,696 | TAIFEX Proxy |
| 自營商 Call夜淨 | -581 | TAIFEX Proxy |
| 自營商 Put夜買 | 36,173 | TAIFEX Proxy |
| 自營商 Put夜賣 | 36,732 | TAIFEX Proxy |
| 自營商 Put夜淨 | -559 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +2,755 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,403 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,374 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 2,444 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,000 | 2,275 | TAIFEX Proxy |
| Call OI 第3大履約價 | 51,000 | 1,993 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 2,444 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 2,444 | 4.44% | TAIFEX Proxy |
| C2 | 47,000 | 2,275 | 4.13% | TAIFEX Proxy |
| C3 | 51,000 | 1,993 | 3.62% | TAIFEX Proxy |
| C4 | 48,000 | 1,851 | 3.36% | TAIFEX Proxy |
| C5 | 47,500 | 1,600 | 2.91% | TAIFEX Proxy |
| C6 | 48,350 | 1,591 | 2.89% | TAIFEX Proxy |
| C7 | 47,600 | 1,555 | 2.83% | TAIFEX Proxy |
| C8 | 48,500 | 1,424 | 2.59% | TAIFEX Proxy |
| C9 | 45,100 | 1,401 | 2.55% | TAIFEX Proxy |
| C10 | 47,200 | 1,139 | 2.07% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 46,000 | 1,829 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,500 | 1,537 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,500 | 1,531 | TAIFEX Proxy |
| Put OI 最大履約價 | 46,000 | 1,829 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 46,000 | 1,829 | 5.82% | TAIFEX Proxy |
| P2 | 46,500 | 1,537 | 4.89% | TAIFEX Proxy |
| P3 | 45,500 | 1,531 | 4.87% | TAIFEX Proxy |
| P4 | 45,000 | 1,478 | 4.71% | TAIFEX Proxy |
| P5 | 44,000 | 1,106 | 3.52% | TAIFEX Proxy |
| P6 | 45,800 | 956 | 3.04% | TAIFEX Proxy |
| P7 | 45,900 | 854 | 2.72% | TAIFEX Proxy |
| P8 | 46,450 | 819 | 2.61% | TAIFEX Proxy |
| P9 | 45,400 | 768 | 2.45% | TAIFEX Proxy |
| P10 | 47,000 | 756 | 2.41% | TAIFEX Proxy |


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
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,174.50 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 資料日期 | 2026-10-21 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202610F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-22→2026-10-23) | +0 | TAIFEX Proxy snapshots (2026-10-22) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 97,417 | 97,118 | +299 | 75,828 | 76,145 | -317 | +616 | TAIFEX Proxy |
| 投信 | 0 | 2,000 | -2,000 | 0 | 0 | +0 | -2,000 | TAIFEX Proxy |
| 自營商 | 119,733 | 116,978 | +2,755 | 61,847 | 61,869 | -22 | +2,777 | TAIFEX Proxy |
| 三大法人合計 | 217,150 | 216,096 | +1,054 | 137,675 | 138,014 | -339 | +1,393 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.44 | 11.58 | -0.14 | 8.57 | 8.75 | -0.18 | +0.04 | TAIFEX Proxy |
| 投信 | 0.00 | 1.10 | -1.10 | 0.00 | 0.00 | +0 | -1.10 | TAIFEX Proxy |
| 自營商 | 12.75 | 14.01 | -1.26 | 7.08 | 7.52 | -0.44 | -0.82 | TAIFEX Proxy |
| 三大法人合計 | 24.18 | 26.69 | -2.51 | 15.64 | 16.26 | -0.62 | -1.89 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 7,058 | TAIFEX Proxy |
| 買權空方 OI | 8,732 | TAIFEX Proxy |
| 買權多空淨 OI | -1,674 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-21→2026-10-22) | -215 | TAIFEX Proxy snapshots (2026-10-22) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,763 | TAIFEX Proxy |
| 賣權空方 OI | 9,398 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,635 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-21→2026-10-22) | -350 | TAIFEX Proxy snapshots (2026-10-22) |
- 資料日期：買權 2026-10-22／賣權 2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,334 | 2026-10-21→2026-10-22 | TAIFEX Proxy snapshots (2026-10-22) |
| 買權前十大 | -215 | 2026-10-21→2026-10-22 | TAIFEX Proxy snapshots (2026-10-22) |
| 賣權前十大 | -350 | 2026-10-21→2026-10-22 | TAIFEX Proxy snapshots (2026-10-22) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-23；資料時間：2026-10-27 10:51:52；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 覆蓋：52 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-10-26，非 T0 2026-10-23)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-10-22 非今日 2026-10-27，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-10-22 (T0 2026-10-23 端點不穩，採最新可得)
- 註記：Gamma 資料日期 2026-10-21 (T0 2026-10-23 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-10-22 (T0 2026-10-23 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 資料日期 2026-10-21 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-22；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151022, T0=1151023)
- 註記：三大法人回傳日期 20261022 (T0 20261023)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-22)，非 T0 2026-10-23
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -815.8 | unavailable | -1,221 | +1,049 | +299 | -317 | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +94.9 | unavailable | -177 | +0 | -2,000 | +0 | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -273.8 | unavailable | +1,565 | +251 | +2,755 | -22 | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
