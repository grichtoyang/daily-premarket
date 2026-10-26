# DATA_REPORT_20261027

- 報告日期：`2026-10-27`
- T0 交易日期：`2026-10-27`
- 資料產出時間：`2026-10-27 01:06:31`
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
| 融資維持率 | 176.99 | % | 前值遞補 (DATA 2026-10-23；當日三源皆失敗；民間估算；官方無每日序列) |

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
| S&P 500 | ^GSPC | 7,681.70 | 58.02 | +0.76 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,229.90 | 274.56 | +1.06 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,341.53 | 384.00 | +1.33 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,335.66 | 120.50 | +0.23 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,127.67 | 348.21 | +3.23 | Yahoo Finance Chart API |
| VIX | ^VIX | 18.54 | -0.91 | -4.68 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 62,693.16 | -214.68 | -0.34 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,550.30 | 16.53 | +0.30 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,093.37 | 158.69 | +0.69 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,690.48 | 32.45 | +0.89 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,673.83 | 316.51 | +2.79 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,711.00 | 51.25 | +0.67 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,453.25 | 335.50 | +1.15 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,500.00 | 106.00 | +0.20 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,804.90 | 20.40 | +0.73 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.69 | 0.04 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.98 | -0.01 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.02 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.56 | -0.03 | -0.10 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.96 | 0.15 | +0.15 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.47 | 0.97 | +0.62 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,325.38 | -0.61 | -0.05 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 426.86 | 8.35 | +1.99 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.25 | 0.36 | +1.88 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.99 | 1.31 | +3.37 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 102.70 | -0.57 | -0.55 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,032.20 | 24.30 | +0.61 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,298.11 | 274.10 | +0.34 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：股價退守年線！自營商加碼「面板大廠」4.2億　華邦電、友達也在補貨名單
  - 來源：Yahoo 台股；發布時間：2026-10-25T23:40:00Z；台北時間：2026-10-26 07:40
  - 摘要：[FTNN新聞網]記者陳宣穎／綜合報導台股上週遇到颱風假交易日僅4天，加權指數（10/19~10/22）收在46041.43點，下跌1069.83點或2.27%。據證交所盤後公布籌碼動...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E5%83%B9%E9%80%80%E5%AE%88%E5%B9%B4%E7%B7%9A-%E8%87%AA%E7%87%9F%E5%95%86%E5%8A%A0%E7%A2%BC-%E9%9D%A2%E6%9D%BF%E5%A4%A7%E5%BB%A0-4-2%E5%84%84-234000563.html
- 事件2：創新板1476萬戶投資人將解禁！明年買股免簽風險預告書
  - 來源：Yahoo 台股；發布時間：2026-10-25T10:50:00Z；台北時間：2026-10-25 18:50
  - 摘要：台灣創新板迎來重大制度變革！證交所規劃自2027年元旦起，取消投資人首次買進創新板股票須簽署風險預告書的規定，潛在投資戶數可望擴大至1476萬戶。隨著交易制度逐步接軌一般上市市場，證交所也將目光轉向國際，力拚打造「亞洲那斯達克」，吸引更多國
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%89%B5%E6%96%B0%E6%9D%BF1476%E8%90%AC%E6%88%B6%E6%8A%95%E8%B3%87%E4%BA%BA%E5%B0%87%E8%A7%A3%E7%A6%81-%E6%98%8E%E5%B9%B4%E8%B2%B7%E8%82%A1%E5%85%8D%E7%B0%BD%E9%A2%A8%E9%9A%AA%E9%A0%90%E5%91%8A%E6%9B%B8-105000811.html
- 事件3：台股重挫近3800點！「財經作家」罕見不敢逢低買　點出「這訊號」最令人不安
  - 來源：Yahoo 台股；發布時間：2026-10-25T08:20:00Z；台北時間：2026-10-25 16:20
  - 摘要：[FTNN新聞網]實習記者周宗怡／綜合報導台股10月初才創下歷史收盤新高49822.55點，如今卻快速拉回，上周四（22日）下跌至46041.43點，讓投資人情緒轉趨謹慎。...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%87%8D%E6%8C%AB%E8%BF%913800%E9%BB%9E-%E8%B2%A1%E7%B6%93%E4%BD%9C%E5%AE%B6-%E7%BD%95%E8%A6%8B%E4%B8%8D%E6%95%A2%E9%80%A2%E4%BD%8E%E8%B2%B7-%E9%BB%9E%E5%87%BA-%E9%80%99%E8%A8%8A%E8%99%9F-082000694.html
- 事件4：少賺比賠錢更難受？26歲股民資產縮水60萬　親曝「帳面戰績」：是不是該先停利
  - 來源：Yahoo 台股；發布時間：2026-10-24T13:15:00Z；台北時間：2026-10-24 21:15
  - 摘要：[FTNN新聞網]實習記者林妤蓁／綜合報導台股近期震盪，一名26歲網友在Dcard股票板發文表示，今年初總資產約200萬元，隨著股市上漲及工作存款，一度累積至400萬...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%B0%91%E8%B3%BA%E6%AF%94%E8%B3%A0%E9%8C%A2%E6%9B%B4%E9%9B%A3%E5%8F%97-26%E6%AD%B2%E8%82%A1%E6%B0%91%E8%B3%87%E7%94%A2%E7%B8%AE%E6%B0%B460%E8%90%AC-%E8%A6%AA%E6%9B%9D-%E5%B8%B3%E9%9D%A2%E6%88%B0%E7%B8%BE-%E6%98%AF%E4%B8%8D%E6%98%AF%E8%A9%B2%E5%85%88%E5%81%9C%E5%88%A9-131500406.html
- 事件5：500萬「放10年不賣」買0050還是00662？網友選邊站：這檔更有潛力
  - 來源：Yahoo 台股；發布時間：2026-10-24T06:02:16Z；台北時間：2026-10-24 14:02
  - 摘要：如果手上突然有500萬元，打算投入股市並長期持有10年，究竟該選台股還是美股？近日一名網友在Threads發文，提出將500萬元全數投入元大台灣50（0050），或富邦NASDAQ（00662）的選擇題，好奇哪一檔更適合長期投資，引發網友熱
  - 原文連結：https://tw.stock.yahoo.com/news/500%E8%90%AC-%E6%94%BE10%E5%B9%B4%E4%B8%8D%E8%B3%A3-%E8%B2%B70050%E9%82%84%E6%98%AF00662-%E7%B6%B2%E5%8F%8B%E9%81%B8%E9%82%8A%E7%AB%99-%E9%80%99%E6%AA%94%E6%9B%B4%E6%9C%89%E6%BD%9B%E5%8A%9B-060216470.html
- 事件6：影響選舉成敗？紐時：台灣縣市首長宣布放颱風假、選舉年增加31%
  - 來源：Yahoo 台股；發布時間：2026-10-23T12:04:02Z；台北時間：2026-10-23 20:04
  - 摘要：中度颱風薔琵來襲，台灣全島週五（10/23）皆停班停課，暴風圈傍晚已籠罩台灣大部分地區。美國《紐約時報》引述專家分析報導，在選舉年，台灣縣市首長因颱風而宣布放假的可能性會增加31%。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%BD%B1%E9%9F%BF%E9%81%B8%E8%88%89%E6%88%90%E6%95%97-%E7%B4%90%E6%99%82-%E5%8F%B0%E7%81%A3%E7%B8%A3%E5%B8%82%E9%A6%96%E9%95%B7%E5%AE%A3%E5%B8%83%E6%94%BE%E9%A2%B1%E9%A2%A8%E5%81%87-%E9%81%B8%E8%88%89%E5%B9%B4%E5%A2%9E%E5%8A%A031-120402710.html
- 事件7：Federal Reserve is likely to hold interest rates steady in October. Here's what that means for consumers
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 16:03:57 GMT；台北時間：2026-10-27 00:03
  - 摘要：The Federal Reserve is expected to keep its overnight rate unchanged at the conclusion of its October meeting this week.
  - 原文連結：https://www.cnbc.com/2026/10/26/fed-decision-expectations-october-meeting.html
- 事件8：Audi defends plans for a $4 billion Georgia plant amid VW restructuring, tariffs
  - 來源：CNBC；發布時間：Sun, 25 Oct 2026 16:42:42 GMT；台北時間：2026-10-26 00:42
  - 摘要：Audi's CEO defended the company's plans for a $4 billion plant in Georgia, calling it a business decision to grow sales and reduce exposure to U.S. ta
  - 原文連結：https://www.cnbc.com/2026/10/25/audi-georgia-us-plant-tariffs-volkswagen.html
- 事件9：America by the numbers: How voters feel about the economy, inflation, AI and Trump
  - 來源：CNBC；發布時間：Sat, 24 Oct 2026 10:58:30 GMT；台北時間：2026-10-24 18:58
  - 摘要：With the U.S. midterm elections looming, Americans are nearly as gloomy about the economy as they were when the nation was emerging from the pandemic.
  - 原文連結：https://www.cnbc.com/2026/10/23/america-by-the-numbers-how-voters-feel-about-the-economy-inflation-ai-and-trump.html
- 事件10：Some Republicans are opposing Trump on tariffs. Maine's Susan Collins just got him to back down on Canadian levies.
  - 來源：MarketWatch；發布時間：Mon, 26 Oct 2026 16:01:00 GMT；台北時間：2026-10-27 00:01
  - 摘要：As she faces a tough midterm race, the five-term GOP senator is touting her successful lobbying effort against certain tariffs on Canada
  - 原文連結：https://www.marketwatch.com/story/some-republicans-are-opposing-trump-on-tariffs-maines-susan-collins-just-got-him-to-back-down-on-canadian-levies-02b202ae?mod=mw_rss_topstories
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

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-27

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
| 多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-26) |
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
| 前十大交易人多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-26) |

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
| 交易日期 | 2026-10-27 | TAIFEX Proxy |
| 到期月份／到期日 | unavailable | TAIFEX Proxy |
| 資料更新時間 | 2026-10-27 01:06:31 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 0 | TAIFEX Proxy |
| Call 總未平倉量 OI | 0 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 0 | TAIFEX Proxy |
| Put 總未平倉量 OI | 0 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | unavailable | TAIFEX Proxy |
| Call／Put 未平倉量比例 | unavailable | TAIFEX Proxy |
| Put／Call Ratio | unavailable | TAIFEX Proxy |
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
| Call OI 最大履約價 | unavailable | unavailable | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 unavailable)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| unavailable | unavailable | unavailable | unavailable | 端點未提供 |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 最大履約價 | unavailable | unavailable | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 unavailable)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| unavailable | unavailable | unavailable | unavailable | 端點未提供 |


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
| Call Wall 價位 | unavailable | TAIFEX Proxy |
| 對應到期月份 | unavailable | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | unavailable | TAIFEX Proxy |
| 對應到期月份 | unavailable | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | unavailable | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | unavailable | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | unavailable | TAIFEX Proxy |
| 對應到期月份 | unavailable | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

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
| 買權多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-26) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,763 | TAIFEX Proxy |
| 賣權空方 OI | 9,398 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,635 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-26) |
- 資料日期：買權 2026-10-22／賣權 2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-10-22→2026-10-22 | TAIFEX Proxy snapshots (2026-10-26) |
| 買權前十大 | +0 | 2026-10-22→2026-10-22 | TAIFEX Proxy snapshots (2026-10-26) |
| 賣權前十大 | +0 | 2026-10-22→2026-10-22 | TAIFEX Proxy snapshots (2026-10-26) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-27；資料時間：2026-10-27 01:06:31；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (23)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, futures.gamma_wall, futures.gamma_flip, options.chain_oi_change
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-10-26，非 T0 2026-10-27)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-10-22 非今日 2026-10-27，視為無新節次，不採用
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 未取得，總量/OI/集中區 unavailable
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-23；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151022, T0=1151027)
- 註記：三大法人回傳日期 20261022 (T0 20261027)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-23)，非 T0 2026-10-27
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -815.8 | unavailable | -1,221 | +1,049 | +299 | -317 | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +94.9 | unavailable | -177 | +0 | -2,000 | +0 | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -273.8 | unavailable | +1,565 | +251 | +2,755 | -22 | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
