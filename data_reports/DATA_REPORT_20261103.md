# DATA_REPORT_20261103

- 報告日期：`2026-11-03`
- T0 交易日期：`2026-11-03`
- 資料產出時間：`2026-11-03 04:36:54`
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
| 加權指數 | 45,211.83 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 45,211.83 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -1,156.50 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -2.49 | % | TWSE OpenAPI MI_INDEX (備援) |
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
| 外資 | -735.2 | 億元 | twse-proxy /institutional |
| 投信 | +338.2 | 億元 | twse-proxy /institutional |
| 自營商 | -152.9 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -549.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 197,359 | 張 | HiStock |
| 融券增減 | 9,581 | 張 | HiStock |
| 融資維持率 | 171.80 | % | 前值遞補 (DATA 2026-10-30；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,525,241 | 張 | TWSE TWT93U + TPEX margin_sbl |
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
| S&P 500 | ^GSPC | 7,554.56 | -25.51 | -0.34 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,216.92 | -220.08 | -0.87 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,031.24 | -353.61 | -1.25 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,080.61 | 310.30 | +0.60 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,326.90 | -361.90 | -3.39 | Yahoo Finance Chart API |
| VIX | ^VIX | 20.83 | 1.41 | +7.26 | Yahoo Finance Chart API |

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
| S&P500期貨 | ES=F | 7,600.25 | -13.75 | -0.18 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,278.00 | -256.00 | -0.90 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,269.00 | 351.00 | +0.68 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,828.10 | 6.80 | +0.24 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.56 | -0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.27 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.59 | 0.03 | +0.08 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.76 | -0.12 | -0.12 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.87 | 0.07 | +0.04 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,344.83 | 6.85 | +0.51 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 399.84 | -6.29 | -1.55 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.39 | -0.29 | -1.74 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 39.33 | -0.17 | -0.44 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 96.15 | -7.97 | -7.65 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,952.20 | 53.30 | +1.37 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,796.40 | -1,452.05 | -1.86 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：聯發科台達電救駕也難翻紅 台股11月首日失守4萬5
  - 來源：Yahoo 台股；發布時間：2026-11-02T17:45:28Z；台北時間：2026-11-03 01:45
  - 摘要：權值股救火仍失守4萬5，台股11月首戰收跌291點！今(2)日加權指數終場下跌291.69點、跌幅0.65%，收44,920.14點，成交金額7,603.44億元。受到上周五美國半導體股重挫拖累，早盤一度急殺812.73點，隨後低接買盤進場
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A111%E6%9C%88%E9%A6%96%E6%97%A5%E6%94%B6%E9%BB%91291%E9%BB%9E%EF%BC%81%E8%81%AF%E7%99%BC%E7%A7%91%E3%80%81%E5%8F%B0%E9%81%94%E9%9B%BB%E7%8E%87%E9%9A%8A%E6%95%91%E9%A7%95%E4%BB%8D%E5%AE%88%E4%B8%8D%E4%BD%8F4%E8%90%AC5%E5%A4%A7%E9%97%9C%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090317512.html
- 事件2：171萬股民荷包有喜 00878配息創新高
  - 來源：Yahoo 台股；發布時間：2026-11-02T09:42:52Z；台北時間：2026-11-02 17:42
  - 摘要：擁有171.1萬股民、國泰永續高股息（00878）公布最近一季配息，配息金額1.25元，創下新高，以今（2）日34.8元收盤價計算，單次配發率為3.59%，換算年化分配率14.37%，除息日在11月17日、最後買進日11月16日，發息日12
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B6%85171%E8%90%AC%E8%82%A1%E6%B0%91%E9%A0%90%E6%9C%9F%EF%BC%81%E5%9C%8B%E6%B0%91etf-00878%E9%85%8D%E6%81%AF125%E5%85%83%E6%96%B0%E9%AB%98-%E5%B9%B4%E6%81%AF%E7%8E%87%E9%A3%86%E7%A0%B414-094307394.html
- 事件3：0050唯一生技股跌到剩65元 專家曝選股機制漏洞
  - 來源：Yahoo 台股；發布時間：2026-11-02T09:30:39Z；台北時間：2026-11-02 17:30
  - 摘要：受到美股科技股重挫影響，台股今（2）日早盤一度狂洩812點，不過隨後低檔承接買盤積極進場，跌勢收斂，終場僅下跌291點、0.65%，收在44920點。而財經作家葉育碩提到，國民ETF 0050的選股機制，其實有個問題存在，「這一檔」更曾經是
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%80%99%E6%AA%940050-%E6%9B%BE%E7%B6%93%E5%94%AF-%E7%94%9F%E6%8A%80%E8%82%A1-%E8%B7%8C%E5%88%B0%E5%8F%AA%E5%89%A965%E5%85%83-%E5%B0%88%E5%AE%B6%E6%8F%AD%E5%9C%8B%E6%B0%91etf%E6%BC%8F%E6%B4%9E-093039250.html
- 事件4：台灣PMI與NMI雙降 中經院點名新瓶頸
  - 來源：Yahoo 台股；發布時間：2026-11-02T08:49:08Z；台北時間：2026-11-02 16:49
  - 摘要：中華經濟研究院今（2）日公布10月台灣製造業採購經理人指數（PMI），由上月63.4%降至62.5%，非製造業經理人指數（NMI）也從56.9%降至55.4%，雙雙呈現擴張速度放緩。中經院院長連賢明表示，目前景氣仍處於擴張階段，但受到關鍵原
  - 原文連結：https://tw.stock.yahoo.com/news/10%E6%9C%88%E8%A3%BD%E9%80%A0%E6%A5%AD%E6%8C%87%E6%95%B8%E5%BE%AE%E5%B9%85%E4%B8%8B%E9%99%8D%EF%BC%81%E4%B8%8D%E5%8F%AA%E8%A8%98%E6%86%B6%E9%AB%94%E7%BC%BA%E6%96%99-%E4%B8%AD%E7%B6%93%E9%99%A2%E9%80%A3%E8%B3%A2%E6%98%8E%E9%BB%9E%E5%90%8D%E3%80%8C%E8%BC%89%E6%9D%BF%E3%80%8D%E6%88%90%E6%96%B0%E7%93%B6%E9%A0%B8-084908391.html
- 事件5：看空不是把認購賣掉就好 權證新手別踩3大雷區
  - 來源：Yahoo 台股；發布時間：2026-11-02T17:46:35Z；台北時間：2026-11-03 01:46
  - 摘要：股票有漲就有跌，一般散戶習慣「買進股票等它漲」（做多），但當市場面臨回檔或個股利空時，只能眼睜睜看著資產縮水。但權證不同，看多與看空，都可以透過權證有對應的操作。認購權證（Call）與認售權證（Put）究竟差在哪？如何用小資金實現多空雙向的
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%AA%8D%E8%B3%BC%E6%AC%8A%E8%AD%89%E3%80%81%E8%AA%8D%E5%94%AE%E6%AC%8A%E8%AD%89%E5%B7%AE%E5%9C%A8%E5%93%AA%EF%BC%9F%E7%9C%8B%E5%A4%9A%E8%88%87%E7%9C%8B%E7%A9%BA%E7%9A%84%E7%8D%B2%E5%88%A9%E9%82%8F%E8%BC%AF%E4%B8%80%E6%AC%A1%E7%9C%8B%E6%87%82-100000713.html
- 事件6：00900、00892分紅囉！富邦4檔ETF同日除息　配息初估一次看
  - 來源：Yahoo 台股；發布時間：2026-11-02T11:12:48Z；台北時間：2026-11-02 19:12
  - 摘要：領息族請留意！富邦投信旗下3檔台股ETF、1檔主動式債券ETF，都將在17日同步除息，初估的配息數字，已經出爐，一起來看《品觀點》整理的配息資訊。
  - 原文連結：https://tw.stock.yahoo.com/news/00900-00892%E5%88%86%E7%B4%85%E5%9B%89-%E5%AF%8C%E9%82%A64%E6%AA%94etf%E5%90%8C%E6%97%A5%E9%99%A4%E6%81%AF-%E9%85%8D%E6%81%AF%E5%88%9D%E4%BC%B0-%E6%AC%A1%E7%9C%8B-111248836.html
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Federal Reserve issues FOMC statement
  - 來源：Federal Reserve；發布時間：Wed, 28 Oct 2026 18:00:00 GMT；台北時間：2026-10-29 02:00
  - 摘要：Federal Reserve issues FOMC statement
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 事件9：Fed will vote on rates less often. What that could mean for borrowers
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 19:21:15 GMT；台北時間：2026-11-03 03:21
  - 摘要：Fed Chairman Kevin Warsh said he plans to reduce the number of rate-setting votes, a move some economists say could delay relief for borrowers.
  - 原文連結：https://www.cnbc.com/2026/11/02/fed-rate-votes-consumer-borrowing-costs.html
- 事件10：Stock market after midterm elections: What S&P 500 history shows
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 17:57:35 GMT；台北時間：2026-11-03 01:57
  - 摘要：Midterms historically precede a strong year for the S&P 500. What to know if Democrats win back Congress
  - 原文連結：https://www.cnbc.com/2026/11/02/stock-market-after-midterm-elections-sp-500-history.html
- 事件11：Crude oil prices sell off more than 7% on Iran peace talk hopes ahead of U.S. midterms
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 20:19:25 GMT；台北時間：2026-11-03 04:19
  - 摘要：Oil fell Monday, amid news that both the U.S. and Iran are pursuing diplomacy amid ongoing Mideast tensions
  - 原文連結：https://www.cnbc.com/2026/11/02/oil-prices-fall-as-iran-us-pursue-diplomacy.html
- 事件12：Wall Street's Fear Index is doing something strange. Here's what it means for stocks
  - 來源：CNBC；發布時間：Mon, 02 Nov 2026 15:30:41 GMT；台北時間：2026-11-02 23:30
  - 摘要：VIX deemed "unreactive" by options traders
  - 原文連結：https://www.cnbc.com/2026/11/02/wall-streets-fear-index-is-doing-something-strange-heres-what-it-means-for-stocks.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-03

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 45,000 | TAIFEX Proxy |
| 最高價 | 45,332 | TAIFEX Proxy |
| 最低價 | 44,700 | TAIFEX Proxy |
| 收盤價 | 45,256 | TAIFEX Proxy |
| 漲跌點數 | -44 | TAIFEX Proxy |
| 漲跌幅 | -0.10 | TAIFEX Proxy |
| 成交量 | 52,221 | TAIFEX Proxy |
| 日盤高點及低點 | 45,332 / 44,700 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 93,812 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,190 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,622 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-30→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-11-02) |
- 資料日期：2026-10-30 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 57,787 | TAIFEX Proxy |
| 外資日盤空單交易量 | 54,986 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +2,801 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -72 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -457 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,272 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +203.5 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 45,256 | TAIFEX Proxy |
| 加權指數價格 | 45,211.83 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | +44.17 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | +0.10 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | +44.17 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 45,256 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 52,221 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 57,787 | 54,986 | +2,801 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 121 | 193 | -72 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 4,663 | 5,120 | -457 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 62,571 | 60,299 | +2,272 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 93,812 | TAIFEX Proxy |
| 前十大交易人空方 OI | 82,190 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +11,622 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-30→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

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
| 交易日期 | 2026-11-03 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-03 04:36:54 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 140,350 | TAIFEX Proxy |
| Call 總未平倉量 OI | 61,578 | TAIFEX Proxy |
| Call OI 增減 (2026-11-02→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 135,722 | TAIFEX Proxy |
| Put 總未平倉量 OI | 34,887 | TAIFEX Proxy |
| Put OI 增減 (2026-11-02→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.03 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.77 | TAIFEX Proxy |
| Put／Call Ratio | 0.57 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-29→2026-10-30) | 9.95 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-29→2026-10-30) | -1.87 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 43,372 | TAIFEX Proxy |
| 外資 Call日賣 | 43,672 | TAIFEX Proxy |
| 外資 Call日淨 | -300 | TAIFEX Proxy |
| 外資 Put日買 | 47,746 | TAIFEX Proxy |
| 外資 Put日賣 | 47,879 | TAIFEX Proxy |
| 外資 Put日淨 | -133 | TAIFEX Proxy |
| 外資 Call夜買 | 21,396 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,563 | TAIFEX Proxy |
| 外資 Call夜淨 | -167 | TAIFEX Proxy |
| 外資 Put夜買 | 20,402 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,475 | TAIFEX Proxy |
| 外資 Put夜淨 | -73 | TAIFEX Proxy |
| 外資 日盤淨總量 | -167 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -133 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -60 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 41,575 | TAIFEX Proxy |
| 自營商 Call日賣 | 35,503 | TAIFEX Proxy |
| 自營商 Call日淨 | +6,072 | TAIFEX Proxy |
| 自營商 Put日買 | 36,775 | TAIFEX Proxy |
| 自營商 Put日賣 | 38,102 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,327 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,028 | TAIFEX Proxy |
| 自營商 Call夜賣 | 11,963 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,935 | TAIFEX Proxy |
| 自營商 Put夜買 | 11,254 | TAIFEX Proxy |
| 自營商 Put夜賣 | 11,798 | TAIFEX Proxy |
| 自營商 Put夜淨 | -544 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +7,399 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +8,007 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -783 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,000 | 4,503 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,400 | 4,384 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,500 | 2,534 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,000 | 4,503 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,000 | 4,503 | 7.31% | TAIFEX Proxy |
| C2 | 49,400 | 4,384 | 7.12% | TAIFEX Proxy |
| C3 | 44,500 | 2,534 | 4.12% | TAIFEX Proxy |
| C4 | 51,000 | 2,336 | 3.79% | TAIFEX Proxy |
| C5 | 46,000 | 2,072 | 3.36% | TAIFEX Proxy |
| C6 | 46,500 | 1,877 | 3.05% | TAIFEX Proxy |
| C7 | 44,300 | 1,731 | 2.81% | TAIFEX Proxy |
| C8 | 44,000 | 1,685 | 2.74% | TAIFEX Proxy |
| C9 | 44,100 | 1,672 | 2.72% | TAIFEX Proxy |
| C10 | 43,900 | 1,643 | 2.67% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 44,000 | 2,661 | TAIFEX Proxy |
| Put OI 第2大履約價 | 43,000 | 2,543 | TAIFEX Proxy |
| Put OI 第3大履約價 | 41,400 | 1,756 | TAIFEX Proxy |
| Put OI 最大履約價 | 44,000 | 2,661 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 44,000 | 2,661 | 7.63% | TAIFEX Proxy |
| P2 | 43,000 | 2,543 | 7.29% | TAIFEX Proxy |
| P3 | 41,400 | 1,756 | 5.03% | TAIFEX Proxy |
| P4 | 42,000 | 1,461 | 4.19% | TAIFEX Proxy |
| P5 | 43,500 | 1,274 | 3.65% | TAIFEX Proxy |
| P6 | 40,600 | 1,250 | 3.58% | TAIFEX Proxy |
| P7 | 42,500 | 1,220 | 3.5% | TAIFEX Proxy |
| P8 | 45,000 | 1,178 | 3.38% | TAIFEX Proxy |
| P9 | 44,500 | 1,105 | 3.17% | TAIFEX Proxy |
| P10 | 43,300 | 841 | 2.41% | TAIFEX Proxy |


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
| Call Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-02→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-02→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 44,400 | TAIFEX Proxy |
| 對應到期月份 | 202611W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-02→2026-11-03) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 91,251 | 91,418 | -167 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 0 | 6,362 | -6,362 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 79,677 | 72,278 | +7,399 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 170,928 | 170,058 | +870 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.36 | 11.17 | +0.18 | 4.88 | 4.94 | -0.06 | +0.24 | TAIFEX Proxy |
| 投信 | 0.00 | 3.01 | -3.01 | 0.00 | 0.00 | +0 | -3.01 | TAIFEX Proxy |
| 自營商 | 10.22 | 8.40 | +1.82 | 2.81 | 3.35 | -0.54 | +2.35 | TAIFEX Proxy |
| 三大法人合計 | 21.57 | 22.58 | -1.01 | 7.70 | 8.29 | -0.60 | -0.41 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 9,881 | TAIFEX Proxy |
| 買權空方 OI | 12,037 | TAIFEX Proxy |
| 買權多空淨 OI | -2,156 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-30→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-11-02) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,631 | TAIFEX Proxy |
| 賣權空方 OI | 10,961 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,330 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-30→2026-10-30) | +0 | TAIFEX Proxy snapshots (2026-11-02) |
- 資料日期：買權 2026-10-30／賣權 2026-10-30 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-10-30→2026-10-30 | TAIFEX Proxy snapshots (2026-11-02) |
| 買權前十大 | +0 | 2026-10-30→2026-10-30 | TAIFEX Proxy snapshots (2026-11-02) |
| 賣權前十大 | +0 | 2026-10-30→2026-10-30 | TAIFEX Proxy snapshots (2026-11-02) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-03；資料時間：2026-11-03 04:36:54；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (24)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total, futures.gamma_wall, futures.gamma_flip, futures.gamma_wall, futures.gamma_flip
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-02，非 T0 2026-11-03)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-02 非今日 2026-11-03，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-02 非今日 2026-11-03，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-02 非今日 2026-11-03，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-02 (T0 2026-11-03 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-02 (T0 2026-11-03 端點不穩，採最新可得)
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-30；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy taiex 缺值，改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151102, T0=1151103)
- 註記：三大法人回傳日期 20261102 (T0 20261103)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-30)，非 T0 2026-11-03
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -735.2 | unavailable | +2,801 | unavailable | -167 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +338.2 | unavailable | -72 | unavailable | -6,362 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -152.9 | unavailable | -457 | unavailable | +7,399 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
