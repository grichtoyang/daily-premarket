# DATA_REPORT_20261028

- 報告日期：`2026-10-28`
- T0 交易日期：`2026-10-28`
- 資料產出時間：`2026-10-28 00:19:39`
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
| 外資 | -80.4 | 億元 | twse-proxy /institutional |
| 投信 | +236.0 | 億元 | twse-proxy /institutional |
| 自營商 | -124.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +31.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 216,539 | 張 | HiStock |
| 融券增減 | 24,702 | 張 | HiStock |
| 融資維持率 | 176.99 | % | 前值遞補 (DATA 2026-10-27；當日三源皆失敗；民間估算；官方無每日序列) |

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
| S&P 500 | ^GSPC | 7,727.96 | 51.19 | +0.67 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,507.08 | 337.70 | +1.29 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,680.49 | 407.09 | +1.39 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,403.75 | 42.17 | +0.08 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,443.97 | 360.50 | +3.25 | Yahoo Finance Chart API |
| VIX | ^VIX | 17.55 | -0.84 | -4.57 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 62,189.65 | -503.51 | -0.80 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,469.47 | -80.83 | -1.46 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,211.81 | 118.44 | +0.51 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,697.52 | 7.04 | +0.19 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,534.38 | -139.45 | -1.19 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,763.75 | 49.25 | +0.64 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 29,844.50 | 407.25 | +1.38 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,614.00 | 64.00 | +0.12 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,827.00 | 29.50 | +1.05 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.68 | -0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.99 | 0.00 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | 0.00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.40 | -0.17 | -0.52 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.28 | 0.32 | +0.32 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.88 | 1.05 | +0.67 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,326.26 | 4.50 | +0.34 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 437.10 | 12.73 | +3.00 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 19.40 | 0.22 | +1.12 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 41.69 | 1.78 | +4.46 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 100.04 | -1.72 | -1.69 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,071.60 | 33.20 | +0.82 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 80,460.85 | 454.20 | +0.57 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股震盪900點還能收紅 台積機器人記憶體守住46K
  - 來源：Yahoo 台股；發布時間：2026-10-27T09:16:01Z；台北時間：2026-10-27 17:16
  - 摘要：台積電尾盤拉抬，台股震盪逾900點、收紅54點守住4萬6！今(27)日加權指數終場上漲54.80點、漲幅0.12%，收46,096.23點，成交金額9,782.87億元。大盤早盤一度上漲544點，隨後賣壓出籠，最低下探45,676.67點，
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E5%B0%BE%E7%9B%A4%E6%8B%89%E4%B8%80%E6%8A%8A%EF%BC%81%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%87%BA%E6%8B%B3%E3%80%81%E8%A8%98%E6%86%B6%E9%AB%94%E8%A3%9C%E8%A1%80-%E5%8F%B0%E8%82%A1%E9%9C%87%E7%9B%AA900%E9%BB%9E%E6%94%B6%E7%B4%85%E4%BF%9D%E4%BD%8F46000%E9%BB%9E%E5%A4%A7%E9%97%9C%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091601634.html
- 事件2：台股整理何時能解套 科技巨頭財報成焦點
  - 來源：Yahoo 台股；發布時間：2026-10-27T10:12:41Z；台北時間：2026-10-27 18:12
  - 摘要：台股今開高走低，電子族群漲勢無力，銅箔基板、高階PCB等9檔焦點股面臨重挫。法人指出短線格局偏弱，建議投資人不宜追高，下檔看半年線支撐。本週將迎來多家大型科技巨頭財報公布，將成盤勢關鍵變局，操作應適度調節減碼。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%9F%AD%E7%B7%9A%E6%B2%89%E9%87%8D%E9%99%B7%E5%BC%B1%E5%8B%A2%E6%95%B4%E7%90%86-9%E6%AA%94-%E5%A3%93%E5%8A%9B%E5%B1%B1%E5%A4%A7-095600900.html
- 事件3：河口湖案是否詐保仍待查 金管會揭保險業四道防線
  - 來源：Yahoo 台股；發布時間：2026-10-27T09:11:33Z；台北時間：2026-10-27 17:11
  - 摘要：台籍女子井雲蓉赴日獨旅慘遭同團旅客楊閔涵持刀刺殺，慘死河口湖飯店轟動台日，今（27）案情出現驚人「反轉」，死者一個月前曾透過電話，懷疑自己遭丈夫殺害詐保，質疑全案恐為買兇殺人案。金管會今（27）日被問保險業要嗎？保險局副局長蔡火炎今（27）
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B2%B3%E5%8F%A3%E6%B9%96%E5%91%BD%E6%A1%88%E8%AE%8A%E3%80%8C%E8%A9%90%E4%BF%9D%E3%80%8D%E8%B2%B7%E5%85%87%EF%BC%9F-%E4%BF%9D%E9%9A%AA%E6%A5%AD%E8%A6%81%E8%B3%A0%E5%97%8E%EF%BC%9F%E9%87%91%E7%AE%A1%E6%9C%83%EF%BC%9A4%E6%8B%9B%E5%8F%AF%E5%8F%8D%E5%88%B6%EF%BC%81%E9%98%B2%E7%AF%84%E9%81%93%E5%BE%B7%E9%A2%A8%E9%9A%AA-091133315.html
- 事件4：新台幣一直貶別只怪外資 台企海外投資藏線索
  - 來源：Yahoo 台股；發布時間：2026-10-27T08:05:36Z；台北時間：2026-10-27 16:05
  - 摘要：10月以來，新台幣對美元匯率貶值超過7角，近期頻傳交易爆量，單日盤中一度重貶逾2角。央行罕見在盤中發聲穩軍心，搭配台股震盪下行的「股匯雙殺」走勢，市場熱議是外資的熱錢匯出影響了匯價。事實上，台灣企業今年對外投資金額大爆發，出口商也未必急著將
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%96%B0%E5%8F%B0%E5%B9%A3%E4%B8%80%E7%9B%B4%E8%B2%B6-%E4%B8%8D%E5%85%A8%E6%98%AF%E5%A4%96%E8%B3%87%E6%83%B9%E7%9A%84%E7%A6%8D%EF%BC%9F%E5%8F%B0%E4%BC%81%E8%B3%BA%E7%9A%84%E9%8C%A2%E7%82%BA%E4%BD%95%E4%B8%8D%E5%8C%AF%E5%9B%9E-%E5%BE%9E%E6%A0%B8%E5%87%86%E5%B0%8D%E5%A4%96%E6%8A%95%E8%B3%87%E9%87%91%E9%A1%8D%E6%89%BE%E7%AB%AF%E5%80%AA%EF%BC%81%EF%BD%9C%E7%9C%8B%E5%9C%96%E8%AA%AA%E8%82%A1%E5%B8%82-080536229.html
- 事件5：移工請假照顧空窗誰補位 衛福部回應
  - 來源：Yahoo 台股；發布時間：2026-10-27T09:44:06Z；台北時間：2026-10-27 17:44
  - 摘要：日前發生外籍看護工來台便懷孕，凸顯一旦移工因故暫時無法照顧被照顧者，衍生的空窗期該如何解決？今（27）日台灣身心障礙者自立生活聯盟等數個移工及勞工團體，集結近數十人在衛福部門前陳情，訴求「請假是移工權利，空窗期是衛福部責任」。對此衛福部長期
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B3%B4%E6%B8%85%E5%BE%B7%E8%AA%A0%E4%BF%A1%E6%9C%89%E6%9C%9F%E9%99%90-%E6%9E%97%E6%BF%81%E6%B0%B4-%E8%94%A1%E8%8B%B1%E6%96%87%E7%95%B6%E5%B9%B4%E4%B8%8D%E5%86%8D%E5%BF%A0%E8%AA%A0%E6%96%BC%E6%89%81-%E6%B0%91%E9%80%B2%E9%BB%A8%E6%89%8D%E6%85%A2%E6%85%A2%E7%88%AC%E8%B5%B7%E4%BE%86-032701204.html
- 事件6：晶片股大漲帶動　美股週二開高上揚
  - 來源：Yahoo 台股；發布時間：2026-10-27T14:01:21Z；台北時間：2026-10-27 22:01
  - 摘要：受晶片股買氣持續推升影響，美國股市週二（27日）開盤上揚。除了半導體類股延續強勁走勢外，交易員亦關注油價回落、評估一系列企業財報，並密切緊盯聯準會（Fed）為期兩天的利率政策會議。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%99%B6%E7%89%87%E8%82%A1%E5%A4%A7%E6%BC%B2%E5%B8%B6%E5%8B%95-%E7%BE%8E%E8%82%A1%E9%80%B1%E4%BA%8C%E9%96%8B%E9%AB%98%E4%B8%8A%E6%8F%9A-140121370.html
- 事件7：Fed expected to hold rates steady, but Warsh may point way to more hikes
  - 來源：CNBC；發布時間：Tue, 27 Oct 2026 15:52:26 GMT；台北時間：2026-10-27 23:52
  - 摘要：Markets overwhelmingly expect no change in benchmark interest rates following September's increase.
  - 原文連結：https://www.cnbc.com/2026/10/27/federal-reserve-rates-kevin-warsh.html
- 事件8：Honda warns 50% Canada auto tariffs would be catastrophic for auto industry
  - 來源：CNBC；發布時間：Tue, 27 Oct 2026 15:48:32 GMT；台北時間：2026-10-27 23:48
  - 摘要：President Donald Trump has threatened to double tariffs on Canadian vehicles and parts from 25% to 50% if a trade deal is not reached between the two 
  - 原文連結：https://www.cnbc.com/2026/10/27/honda-warns-50percent-canada-auto-tariffs-would-be-catastrophic.html
- 事件9：How to use I-bonds to create guaranteed, inflation-proof income in retirement
  - 來源：MarketWatch；發布時間：Tue, 27 Oct 2026 15:25:00 GMT；台北時間：2026-10-27 23:25
  - 摘要：The new I-bond interest rate could be 5.5% or 5.4%, but that shouldn&#x2019;t change your strategy.
  - 原文連結：https://www.marketwatch.com/story/how-to-use-i-bonds-to-create-guaranteed-inflation-proof-income-in-retirement-50753fea?mod=mw_rss_topstories
- 事件10：Ripple strikes deal with Robinhood to expand its RLUSD digital dollar
  - 來源：CNBC；發布時間：Tue, 27 Oct 2026 14:18:16 GMT；台北時間：2026-10-27 22:18
  - 摘要：As crypto evolves past its trading roots, and global markets shift to 24/7 liquidity, stablecoins are becoming essential financial infrastructure.
  - 原文連結：https://www.cnbc.com/2026/10/27/ripple-strikes-deal-with-robinhood-to-expand-its-rlusd-digital-dollar.html
- 事件11：From Wall Street to Silicon Valley, Anthropic IPO poised to have massive 'trickle-down effect'
  - 來源：CNBC；發布時間：Mon, 26 Oct 2026 22:50:07 GMT；台北時間：2026-10-27 06:50
  - 摘要：With the AI trade sputtering of late and interest rates on the rise, Anthropic's IPO is taking on outsized importance.
  - 原文連結：https://www.cnbc.com/2026/10/26/anthropic-ipo-might-trigger-tech-reset-if-ipo-underperforms.html
- 事件12：GM will switch to Nasdaq from the NYSE on Nov. 17
  - 來源：CNBC；發布時間：Tue, 27 Oct 2026 10:49:45 GMT；台北時間：2026-10-27 18:49
  - 摘要：GM expects to keep its “GM” ticker symbol, and the company says shareholders do not need to take action because of the transfer.
  - 原文連結：https://www.cnbc.com/2026/10/27/gm-nasdaq-nyse-stock-listing.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-10-28

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
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-27) |
- 資料日期：2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 59,401 | TAIFEX Proxy |
| 外資日盤空單交易量 | 58,180 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,221 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,451 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,794 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +878 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +81.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,081 | TAIFEX Proxy |
| 加權指數價格 | 46,041.43 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +39.57 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +0.09 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +39.57 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,081 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 61,110 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 59,401 | 58,180 | +1,221 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 1,554 | 103 | +1,451 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 5,810 | 7,604 | -1,794 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 66,765 | 65,887 | +878 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 89,928 | TAIFEX Proxy |
| 前十大交易人空方 OI | 80,904 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,024 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

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
| 交易日期 | 2026-10-28 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W4 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-28 00:19:39 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 57,078 | TAIFEX Proxy |
| Call 總未平倉量 OI | 33,918 | TAIFEX Proxy |
| Call OI 增減 (2026-10-27→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 38,698 | TAIFEX Proxy |
| Put 總未平倉量 OI | 15,638 | TAIFEX Proxy |
| Put OI 增減 (2026-10-27→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.47 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.17 | TAIFEX Proxy |
| Put／Call Ratio | 0.46 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-21→2026-10-22) | -25.67 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-21→2026-10-22) | 3.32 | TAIFEX Proxy |
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
| 外資 Call夜買 | 31,148 | TAIFEX Proxy |
| 外資 Call夜賣 | 31,095 | TAIFEX Proxy |
| 外資 Call夜淨 | +53 | TAIFEX Proxy |
| 外資 Put夜買 | 45,050 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,680 | TAIFEX Proxy |
| 外資 Put夜淨 | +370 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,470 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -2,588 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,375 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 101,409 | TAIFEX Proxy |
| 自營商 Call日賣 | 104,219 | TAIFEX Proxy |
| 自營商 Call日淨 | -2,810 | TAIFEX Proxy |
| 自營商 Put日買 | 92,583 | TAIFEX Proxy |
| 自營商 Put日賣 | 96,369 | TAIFEX Proxy |
| 自營商 Put日淨 | -3,786 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,115 | TAIFEX Proxy |
| 自營商 Call夜賣 | 25,696 | TAIFEX Proxy |
| 自營商 Call夜淨 | -581 | TAIFEX Proxy |
| 自營商 Put夜買 | 36,173 | TAIFEX Proxy |
| 自營商 Put夜賣 | 36,732 | TAIFEX Proxy |
| 自營商 Put夜淨 | -559 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +976 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -2,229 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -3,227 | TAIFEX Proxy |

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
| 與前一交易日的變化 (2026-10-27→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-27→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 45,400 | TAIFEX Proxy |
| 對應到期月份 | 202610W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-27→2026-10-28) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 218,321 | 216,851 | +1,470 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 0 | 4,736 | -4,736 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 197,778 | 196,802 | +976 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 416,099 | 418,389 | -2,290 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.85 | 13.88 | -0.03 | 8.57 | 8.75 | -0.18 | +0.15 | TAIFEX Proxy |
| 投信 | 0.00 | 2.39 | -2.39 | 0.00 | 0.00 | +0 | -2.39 | TAIFEX Proxy |
| 自營商 | 14.98 | 13.56 | +1.42 | 7.08 | 7.52 | -0.44 | +1.86 | TAIFEX Proxy |
| 三大法人合計 | 28.83 | 29.83 | -1.00 | 15.64 | 16.26 | -0.62 | -0.38 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 7,058 | TAIFEX Proxy |
| 買權空方 OI | 8,732 | TAIFEX Proxy |
| 買權多空淨 OI | -1,674 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-27) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,763 | TAIFEX Proxy |
| 賣權空方 OI | 9,398 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,635 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-22→2026-10-22) | +0 | TAIFEX Proxy snapshots (2026-10-27) |
- 資料日期：買權 2026-10-22／賣權 2026-10-22 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-10-22→2026-10-22 | TAIFEX Proxy snapshots (2026-10-27) |
| 買權前十大 | +0 | 2026-10-22→2026-10-22 | TAIFEX Proxy snapshots (2026-10-27) |
| 賣權前十大 | +0 | 2026-10-22→2026-10-22 | TAIFEX Proxy snapshots (2026-10-27) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-28；資料時間：2026-10-28 00:19:39；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (22)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, futures.gamma_wall, futures.gamma_flip
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-10-27，非 T0 2026-10-28)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-10-27 非今日 2026-10-28，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-27 非今日 2026-10-28，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-27 非今日 2026-10-28，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-10-27 (T0 2026-10-28 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-10-27 (T0 2026-10-28 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-27；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151027, T0=1151028)
- 註記：三大法人回傳日期 20261027 (T0 20261028)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-27)，非 T0 2026-10-28
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -80.4 | unavailable | +1,221 | unavailable | +1,470 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +236.0 | unavailable | +1,451 | unavailable | -4,736 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -124.0 | unavailable | -1,794 | unavailable | +976 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
