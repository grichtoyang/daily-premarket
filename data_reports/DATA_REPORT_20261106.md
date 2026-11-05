# DATA_REPORT_20261106

- 報告日期：`2026-11-06`
- T0 交易日期：`2026-11-06`
- 資料產出時間：`2026-11-06 02:28:24`
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
| 加權指數 | 42,948.91 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 開盤 | unavailable | 點 | FinMind |
| 最高 | unavailable | 點 | FinMind |
| 最低 | unavailable | 點 | FinMind |
| 收盤 | 42,948.91 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌點數 | -358.63 | 點 | TWSE OpenAPI MI_INDEX (備援) |
| 漲跌幅 | -0.83 | % | TWSE OpenAPI MI_INDEX (備援) |
| 成交金額 | unavailable | 億元 | twse-proxy |

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
| 外資 | -1,024.6 | 億元 | twse-proxy /institutional |
| 投信 | +225.9 | 億元 | twse-proxy /institutional |
| 自營商 | -435.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,233.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 246,812 | 張 | HiStock |
| 融券增減 | -10,370 | 張 | HiStock |
| 融資維持率 | 171.80 | % | 前值遞補 (DATA 2026-11-05；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,652,630 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | unavailable | 億元 | twse-proxy |
| 上櫃成交金額 | unavailable | 億元 | TPEX |
| 上市櫃成交金額合計 | unavailable | 億元 | twse-proxy+TPEX |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,391.12 | -297.50 | -3.87 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,415.09 | -1,321.42 | -5.13 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,807.45 | -1,629.72 | -5.73 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,778.03 | -1,578.09 | -2.96 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,220.43 | -1,048.22 | -10.21 | Yahoo Finance Chart API |
| VIX | ^VIX | 26.09 | 9.48 | +57.07 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 62,188.63 | -893.23 | -1.42 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,683.80 | 35.01 | +0.62 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,919.50 | 393.53 | +1.67 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,686.17 | 78.08 | +2.16 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,335.69 | 458.70 | +4.22 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,412.50 | -308.00 | -3.99 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,898.25 | -1,668.50 | -5.84 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,844.00 | -1,659.00 | -3.10 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,740.90 | -125.00 | -4.36 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.58 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.83 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.25 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 33.04 | 0.31 | +0.95 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.44 | -0.07 | -0.07 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.70 | -0.77 | -0.49 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,355.35 | 12.45 | +0.93 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 358.17 | -37.58 | -9.50 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.53 | -2.53 | -15.74 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 30.71 | -6.80 | -18.13 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 90.63 | 2.51 | +2.85 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,107.10 | 34.10 | +0.84 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 76,009.69 | -4,395.60 | -5.47 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：台股殺逾千點成交榜綠油油 金融航空逆勢收紅
  - 來源：Yahoo 台股；發布時間：2026-11-05T08:54:34Z；台北時間：2026-11-05 16:54
  - 摘要：台股重挫1374點、失守4萬2！今(5)日加權指數開低走低，盤中最多下挫1435.34點，終場下跌1374.19點、跌幅3.20%，收41,574.72點。本周前四個交易日、也是11月以來，累計下跌3637.11點、跌幅8.04%，成交金額
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%8D%83%E5%84%84%E8%B3%A3%E5%96%AE%E7%A0%B8%E5%A0%B4%EF%BC%81%E5%8F%B0%E8%82%A1%E6%91%9C%E7%A0%B442k%E5%AF%AB%E7%AC%AC13%E5%A4%A7%E8%B7%8C%E9%BB%9E-%E9%9B%BB%E5%AD%90%E6%BB%BF%E7%9B%A4%E7%B6%A0-%E9%87%91%E8%9E%8D%E6%8F%AA%E8%88%AA%E7%A9%BA%E6%92%90%E4%BD%8F%E4%B8%80%E7%89%87%E5%A4%A9%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085434111.html
- 事件3：外匯存底6千億防線失守 央行點名三大變動因素
  - 來源：Yahoo 台股；發布時間：2026-11-05T10:18:35Z；台北時間：2026-11-05 18:18
  - 摘要：中央銀行今（5）日公布最新數據，10 月外資淨匯出280億美元，約新台幣超過9千億元，我國外匯存底金額連兩個月下滑，10月為5,964.37億美元，較上月大幅減少 43.08 億美元，跌破6000美元的整數大關。
  - 原文連結：https://tw.stock.yahoo.com/news/10%E6%9C%88%E5%A4%96%E8%B3%87%E7%8B%82%E6%8F%90%E6%AC%BE%EF%BC%81%E6%88%91%E5%9C%8B%E5%A4%96%E5%8C%AF%E5%AD%98%E5%BA%95%E9%80%A32%E6%B8%9B%E3%80%81%E5%A4%B1%E5%AE%886000%E5%84%84%E7%BE%8E%E5%85%83%E5%A4%A7%E9%97%9C-101835137.html
- 事件4：台股跌掉8千點救市首招來了 證交所喊話穩信心
  - 來源：Yahoo 台股；發布時間：2026-11-05T10:00:26Z；台北時間：2026-11-05 18:00
  - 摘要：台股跌跌不休，美期中選後隔天今（5）日再跌1374點，一個月跌掉8千點，股民哀鴻遍野，期待「國家隊」救市！過去金管會被戲稱有「救市18套劇本」，除了「限空令」外今日金管會已祭出第一招：請台灣證交所信心喊話。證期局局長黃仲豪也證實證交所會密切
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E7%AE%A1%E6%9C%83%E6%95%91%E5%B8%8218%E5%A5%97%E5%8A%87%E6%9C%AC%E7%AC%AC%E4%B8%80%E6%8B%9B%E5%87%BA%E6%89%8B%E4%BA%86%EF%BC%9A%E8%AD%89%E4%BA%A4%E6%89%80%E5%96%8A%E8%A9%B1%E6%B3%95%E8%AA%AA%E6%9C%83-100157073.html
- 事件5：權證成交量掛零就賣不掉？看懂造市商報價才是關鍵
  - 來源：Yahoo 台股；發布時間：2026-11-05T03:28:01Z；台北時間：2026-11-05 11:28
  - 摘要：許多初接觸權證的新手投資人，會習慣把買賣股票的邏輯直接搬到權證市場，當看到畫面上成交量只有「0」或「幾張」的權證，常下意識認為這是乏人問津的冷門商品，擔心買了會賣不掉。

然而，權證市場有一套特殊的機制「造市商制度」，在正常盤中時段，即使沒
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%AC%8A%E8%AD%89%E6%88%90%E4%BA%A4%E9%87%8F%E6%98%AF%E3%80%8C0%E3%80%8D%E9%82%84%E8%83%BD%E8%B2%B7%E5%97%8E%EF%BC%9F%E4%B8%80%E6%AC%A1%E7%9C%8B%E6%87%82%E9%80%A0%E5%B8%82%E5%95%86%E3%80%81%E8%B2%B7%E8%B3%A3%E5%83%B9%E5%B7%AE%E8%88%87%E6%B5%81%E5%8B%95%E6%80%A7-032801991.html
- 事件6：遺產贈與免稅額可望雙漲 財部預計年底前公布金額
  - 來源：Yahoo 台股；發布時間：2026-11-05T09:59:02Z；台北時間：2026-11-05 17:59
  - 摘要：行政院主計總處今（5）日公布10月消費者物價指數（CPI）年增2.33%，依累計漲幅估算，明年遺產稅免稅額可望增加159萬元、提高至1492萬元；贈與稅免稅額則有望增加29萬元、調高至273萬元。實際調整幅度仍待財政部精算，預計年底前正式公
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B8%9B%E7%A8%85%E7%B4%85%E5%8C%85%E4%BE%86%E4%BA%86%EF%BC%81%E6%98%8E%E5%B9%B4%E8%B4%88%E8%88%87273%E8%90%AC%E5%85%83%E3%80%81%E9%81%BA%E7%94%A21492%E8%90%AC%E5%85%83%E5%85%8D%E7%A8%85-095902433.html
- 事件7：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件8：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件9：Barkin sees interest rate hikes ahead, but at a gradual pace
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 16:34:33 GMT；台北時間：2026-11-06 00:34
  - 摘要：In a CNBC interview, the policymaker expressed concern over inflation and said monetary policy will need to adjust.
  - 原文連結：https://www.cnbc.com/2026/11/05/barkin-sees-interest-rate-hikes-ahead-but-at-a-gradual-pace.html
- 事件10：Banks are turning cautious on lending, according to the Fed. What it means for the economy
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 13:52:38 GMT；台北時間：2026-11-05 21:52
  - 摘要：The Fed’s October bank lending survey shows tighter standards for small firms and commercial real estate, while subprime borrowers face tougher credit
  - 原文連結：https://www.cnbc.com/2026/11/05/fed-bank-lending-standards-small-business.html
- 事件11：Wall Street's fear gauge surges the most since April. Why traders think it should be even higher
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 17:34:16 GMT；台北時間：2026-11-06 01:34
  - 摘要：From its intraday low to high Thursday, VIX moved more than 11 points, the biggest one-day move since April 9.
  - 原文連結：https://www.cnbc.com/2026/11/05/wall-streets-fear-gauge-surges-the-most-since-april-why-traders-think-it-should-be-even-higher.html
- 事件12：What Wall Street billionaires are saying about Democrats' midterm sweep
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 13:44:27 GMT；台北時間：2026-11-05 21:44
  - 摘要：Billionaire political spending met criticism from ... billionaires in the wake of Tuesday's blue wave election.
  - 原文連結：https://www.cnbc.com/2026/11/04/billionaires-musk-branson-democrats-midterms-ai-wall-street.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-06

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,013 | TAIFEX Proxy |
| 最高價 | 43,114 | TAIFEX Proxy |
| 最低價 | 41,666 | TAIFEX Proxy |
| 收盤價 | 41,915 | TAIFEX Proxy |
| 漲跌點數 | -1,288 | TAIFEX Proxy |
| 漲跌幅 | -2.98 | TAIFEX Proxy |
| 成交量 | 98,430 | TAIFEX Proxy |
| 日盤高點及低點 | 43,114 / 41,666 | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-04→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 98,413 | TAIFEX Proxy |
| 外資日盤空單交易量 | 101,388 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,975 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +783 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -650 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,842 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -243.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 41,915 | TAIFEX Proxy |
| 加權指數價格 | 42,948.91 | TWSE OpenAPI MI_INDEX (備援) |
| 台指期與加權指數價差 | -1,033.91 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 價差百分比 | -2.41 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 日盤基差 | -1,033.91 | TAIFEX Proxy+TWSE OpenAPI MI_INDEX (備援) |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 41,915 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 98,430 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：+0（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 98,413 | 101,388 | -2,975 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 1,088 | 305 | +783 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 9,911 | 10,561 | -650 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 109,412 | 112,254 | -2,842 | unavailable | unavailable | unavailable | unavailable | 0 | 0 | +0 | +0 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-04→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

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
| 交易日期 | 2026-11-06 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-06 02:28:24 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 304,899 | TAIFEX Proxy |
| Call 總未平倉量 OI | 90,160 | TAIFEX Proxy |
| Call OI 增減 (2026-11-05→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 229,988 | TAIFEX Proxy |
| Put 總未平倉量 OI | 33,429 | TAIFEX Proxy |
| Put OI 增減 (2026-11-05→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.33 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.70 | TAIFEX Proxy |
| Put／Call Ratio | 0.37 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-03→2026-11-04) | 5.01 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-03→2026-11-04) | 1.60 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 94,675 | TAIFEX Proxy |
| 外資 Call日賣 | 96,232 | TAIFEX Proxy |
| 外資 Call日淨 | -1,557 | TAIFEX Proxy |
| 外資 Put日買 | 81,143 | TAIFEX Proxy |
| 外資 Put日賣 | 81,059 | TAIFEX Proxy |
| 外資 Put日淨 | +84 | TAIFEX Proxy |
| 外資 Call夜買 | 39,947 | TAIFEX Proxy |
| 外資 Call夜賣 | 40,962 | TAIFEX Proxy |
| 外資 Call夜淨 | -1,015 | TAIFEX Proxy |
| 外資 Put夜買 | 34,664 | TAIFEX Proxy |
| 外資 Put夜賣 | 34,763 | TAIFEX Proxy |
| 外資 Put夜淨 | -99 | TAIFEX Proxy |
| 外資 日盤淨總量 | -1,641 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -542 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +183 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 81,577 | TAIFEX Proxy |
| 自營商 Call日賣 | 86,731 | TAIFEX Proxy |
| 自營商 Call日淨 | -5,154 | TAIFEX Proxy |
| 自營商 Put日買 | 64,287 | TAIFEX Proxy |
| 自營商 Put日賣 | 65,015 | TAIFEX Proxy |
| 自營商 Put日淨 | -728 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,062 | TAIFEX Proxy |
| 自營商 Call夜賣 | 26,325 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,263 | TAIFEX Proxy |
| 自營商 Put夜買 | 19,833 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,869 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,036 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -4,426 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -3,891 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +308 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,500 | 6,589 | TAIFEX Proxy |
| Call OI 第2大履約價 | 46,000 | 5,323 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 3,933 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,500 | 6,589 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,500 | 6,589 | 7.31% | TAIFEX Proxy |
| C2 | 46,000 | 5,323 | 5.9% | TAIFEX Proxy |
| C3 | 44,000 | 3,933 | 4.36% | TAIFEX Proxy |
| C4 | 44,500 | 3,874 | 4.3% | TAIFEX Proxy |
| C5 | 45,000 | 3,769 | 4.18% | TAIFEX Proxy |
| C6 | 43,000 | 2,876 | 3.19% | TAIFEX Proxy |
| C7 | 43,500 | 2,350 | 2.61% | TAIFEX Proxy |
| C8 | 42,500 | 2,184 | 2.42% | TAIFEX Proxy |
| C9 | 44,200 | 2,027 | 2.25% | TAIFEX Proxy |
| C10 | 44,300 | 1,876 | 2.08% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 40,000 | 1,932 | TAIFEX Proxy |
| Put OI 第2大履約價 | 41,000 | 1,562 | TAIFEX Proxy |
| Put OI 第3大履約價 | 42,000 | 1,506 | TAIFEX Proxy |
| Put OI 最大履約價 | 40,000 | 1,932 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 40,000 | 1,932 | 5.78% | TAIFEX Proxy |
| P2 | 41,000 | 1,562 | 4.67% | TAIFEX Proxy |
| P3 | 42,000 | 1,506 | 4.51% | TAIFEX Proxy |
| P4 | 41,500 | 1,224 | 3.66% | TAIFEX Proxy |
| P5 | 38,900 | 1,216 | 3.64% | TAIFEX Proxy |
| P6 | 40,500 | 1,134 | 3.39% | TAIFEX Proxy |
| P7 | 40,900 | 1,048 | 3.14% | TAIFEX Proxy |
| P8 | 38,600 | 1,027 | 3.07% | TAIFEX Proxy |
| P9 | 39,500 | 909 | 2.72% | TAIFEX Proxy |
| P10 | 40,400 | 906 | 2.71% | TAIFEX Proxy |


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
| Call Wall 價位 | 46,500 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 42,500.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,950 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 175,734 | 177,375 | -1,641 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 2,760 | 4,247 | -1,487 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 146,592 | 151,018 | -4,426 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 325,086 | 332,640 | -7,554 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 22.08 | 22.27 | -0.19 | 8.79 | 8.93 | -0.14 | -0.05 | TAIFEX Proxy |
| 投信 | 0.08 | 0.49 | -0.41 | 0.00 | 0.00 | +0 | -0.41 | TAIFEX Proxy |
| 自營商 | 20.17 | 19.18 | +0.99 | 7.45 | 6.28 | +1.18 | -0.19 | TAIFEX Proxy |
| 三大法人合計 | 42.33 | 41.94 | +0.39 | 16.25 | 15.21 | +1.04 | -0.65 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,926 | TAIFEX Proxy |
| 買權空方 OI | 16,052 | TAIFEX Proxy |
| 買權多空淨 OI | -4,126 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-04→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-05) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,715 | TAIFEX Proxy |
| 賣權空方 OI | 11,434 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,719 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-04→2026-11-04) | +0 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：買權 2026-11-04／賣權 2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +0 | 2026-11-04→2026-11-04 | TAIFEX Proxy snapshots (2026-11-05) |
| 買權前十大 | +0 | 2026-11-04→2026-11-04 | TAIFEX Proxy snapshots (2026-11-05) |
| 賣權前十大 | +0 | 2026-11-04→2026-11-04 | TAIFEX Proxy snapshots (2026-11-05) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-06；資料時間：2026-11-06 02:28:24；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (20)：taiex.open, taiex.high, taiex.low, listed_breadth.up, listed_breadth.down, listed_breadth.flat, listed_breadth.limit_up, listed_breadth.limit_down, otc_breadth.up, otc_breadth.down, otc_breadth.flat, otc_breadth.limit_up, otc_breadth.limit_down, margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, turnover.listed, turnover.otc, turnover.total
- 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-05，非 T0 2026-11-06)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- 註記：futures-price-after-hours 日期 2026-11-05 非今日 2026-11-06，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-05 非今日 2026-11-06，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-05 非今日 2026-11-06，視為無新節次，不採用
- 註記：Call/Put Wall 與 Max Pain 資料日期 2026-11-05 (T0 2026-11-06 端點不穩，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人 OI 未取得
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：選擇權 chain 資料日期 2026-11-05 (T0 2026-11-06 端點不穩，採最新可得)

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`TWSE OpenAPI MI_INDEX (備援)`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-11-05；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：twse-proxy 連線失敗，TAIEX 改用 MI_INDEX 備援
- 註記：大盤開高低未取得 (FinMind 失敗；MI_INDEX 無此欄)
- 註記：twtazu_od 備援日期不符 (回傳舊資料)，上市漲跌標 unavailable
- 註記：上櫃 highlight 日期不符或缺值 (回傳 1151105, T0=1151106)
- 註記：三大法人回傳日期 20261105 (T0 20261106)，採用最新可得
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-11-05)，非 T0 2026-11-06
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,024.6 | unavailable | -2,975 | unavailable | -1,641 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 投信 | +225.9 | unavailable | +783 | unavailable | -1,487 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
| 自營商 | -435.3 | unavailable | -650 | unavailable | -4,426 | unavailable | 資料不足 | 資料不足 | twse-proxy／TAIFEX Proxy |
