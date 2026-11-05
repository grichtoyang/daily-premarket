# DATA_REPORT_20261105

- 報告日期：`2026-11-05`
- T0 交易日期：`2026-11-05`
- 資料產出時間：`2026-11-05 20:45:58`
- 時區：`Asia/Taipei`
- 產出盤別：`日盤`
- 產出者：`actions`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 41,574.72 | 點 | twse-proxy |
| 開盤 | 42,666.13 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 42,873.81 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 41,513.57 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 41,574.72 | 點 | twse-proxy |
| 漲跌點數 | -1,374.19 | 點 | twse-proxy |
| 漲跌幅 | -3.20 | % | twse-proxy |
| 成交金額 | 9,871.0 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 167 | twse-proxy |
| 下跌家數 | 857 | twse-proxy |
| 平盤家數 | 61 | twse-proxy |
| 漲停家數 | 5 | twse-proxy |
| 跌停家數 | 56 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 120 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 715 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 47 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 5 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 59 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,024.6 | 億元 | twse-proxy /institutional |
| 投信 | +225.9 | 億元 | twse-proxy /institutional |
| 自營商 | -435.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,233.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 246,812 | 張 | HiStock |
| 融券增減 | -10,370 | 張 | HiStock |
| 融資維持率 | unavailable | % | unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 31,935,921 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |
| 借券賣出餘額 | 20,053,370 | 張 | TWSE TWT93U（上市） + TPEX S47（上櫃） |
| 借券賣出增減 | 320,786 | 張 | TWSE TWT93U（上市） + TPEX S47（上櫃） |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,871.0 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,785.8 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,656.8 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,688.62 | 119.70 | +1.58 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,736.51 | 364.50 | +1.44 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 28,437.17 | 256.91 | +0.91 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 53,356.12 | 1,569.40 | +3.03 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,268.65 | -331.75 | -3.13 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.91 | 0.30 | +1.81 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 61,077.90 | -1,110.73 | -1.79 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,383.80 | -300.00 | -5.28 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,796.98 | 877.48 | +3.67 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,689.91 | 3.74 | +0.10 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,471.09 | 135.40 | +1.19 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,722.75 | 2.25 | +0.03 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,333.00 | -233.75 | -0.82 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 53,747.00 | 244.00 | +0.46 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,872.70 | 6.80 | +0.24 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.58 | -0.03 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.06 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.30 | -0.05 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.28 | -0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.93 | 0.19 | +0.59 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.61 | 0.10 | +0.10 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.46 | -0.00 | -0.00 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.84 | 0.94 | +0.07 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 395.75 | -9.05 | -2.24 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 16.06 | -0.34 | -2.07 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 37.51 | -1.54 | -3.94 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 89.53 | 1.41 | +1.60 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,128.00 | 55.00 | +1.35 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 79,680.01 | -725.28 | -0.90 | Yahoo Finance Chart API |

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
- 事件7：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 來源：Federal Reserve；發布時間：Thu, 29 Oct 2026 20:30:00 GMT；台北時間：2026-10-30 04:30
  - 摘要：Federal Reserve Board announces approval of application by The Bank of Nova Scotia
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261029a.htm
- 事件8：Bank of England hikes interest rate for the first time since Iran war, warns inflation will near 5%
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 12:37:57 GMT；台北時間：2026-11-05 20:37
  - 摘要：One policymaker voted to raise the bank's key interest rate to 4.25%.
  - 原文連結：https://www.cnbc.com/2026/11/05/interest-rates-inflation-uk.html
- 事件9：White House panel delays hearing on Fed's Lisa Cook to Dec. 14
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 01:11:26 GMT；台北時間：2026-11-05 09:11
  - 摘要：President Donald Trump first tried to fire Lisa Cook in August 2025, but the Supreme Court in June blocked him from doing so, for now.
  - 原文連結：https://www.cnbc.com/2026/11/04/trump-federal-reserve-lisa-cook-hearing.html
- 事件10：What Wall Street billionaires are saying about Democrats' midterm sweep
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 23:17:56 GMT；台北時間：2026-11-05 07:17
  - 摘要：Billionaire political spending met criticism from ... billionaires in the wake of Tuesday's blue wave election.
  - 原文連結：https://www.cnbc.com/2026/11/04/billionaires-musk-branson-democrats-midterms-ai-wall-street.html
- 事件11：World's largest olive oil company plummets 18% after rivals agree to takeover deal
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 11:42:28 GMT；台北時間：2026-11-05 19:42
  - 摘要：The world's largest olive oil company, Deoleo, plummeted in early trading after two of its rivals announced plans to acquire the firm.
  - 原文連結：https://www.cnbc.com/2026/11/05/deoleo-olive-oil-takeover-dcoop-acesur.html
- 事件12：Jim Cramer warns investors may be reading too much into Wall Street's post-election rally
  - 來源：CNBC；發布時間：Wed, 04 Nov 2026 23:18:56 GMT；台北時間：2026-11-05 07:18
  - 摘要：Cramer warned that Wall Street may be getting ahead of itself following the midterm elections.
  - 原文連結：https://www.cnbc.com/2026/11/04/cramer-midterms-ai-stocks.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-05

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
| 開盤價 | 43,430 | TAIFEX Proxy |
| 最高價 | 44,274 | TAIFEX Proxy |
| 最低價 | 43,141 | TAIFEX Proxy |
| 收盤價 | 43,404 | TAIFEX Proxy |
| 漲跌點數 | +201 | TAIFEX Proxy |
| 漲跌幅 | +0.47 | TAIFEX Proxy |
| 成交量 | 66,939 | TAIFEX Proxy |
| 夜盤高點及低點 | 44,274 / 43,141 | TAIFEX Proxy |
| 結算價 | 41,882 | TAIFEX Proxy |
| 未平倉量 | 123,826 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 13,388 | TAIFEX Proxy |
| 外資空方 OI | 109,039 | TAIFEX Proxy |
| 外資多空淨 OI | -95,651 | TAIFEX Proxy |
| 投信多方 OI | 93,279 | TAIFEX Proxy |
| 投信空方 OI | 2,996 | TAIFEX Proxy |
| 投信多空淨 OI | +90,283 | TAIFEX Proxy |
| 自營商多方 OI | 6,279 | TAIFEX Proxy |
| 自營商空方 OI | 3,949 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,330 | TAIFEX Proxy |
| 三大法人合計多方 OI | 112,946 | TAIFEX Proxy |
| 三大法人合計空方 OI | 115,984 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,038 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,004 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +783 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -631 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-03→2026-11-04) | +1,694 | TAIFEX Proxy snapshots (2026-11-04) |
- 資料日期：2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 98,413 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 101,388 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,975 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 38,711 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 39,180 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -469 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -2,506 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +783 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +783 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -650 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -310 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -340 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,842 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -779 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -243.3 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -69.7 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 41,915 | TAIFEX Proxy |
| 加權指數價格 | 41,574.72 | twse-proxy |
| 台指期與加權指數價差 | +340.28 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.82 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +340.28 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +1,489 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 41,915 | 43,404 | -1,489 | TAIFEX Proxy |
| 成交量 | 98,430 | 66,939 | +31,491 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,852（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 98,413 | 101,388 | -2,975 | 38,711 | 39,180 | -469 | -2,506 | 13,388 | 109,039 | -95,651 | -2,004 | TAIFEX Proxy |
| 投信 | 1,088 | 305 | +783 | 0 | 0 | +0 | +783 | 93,279 | 2,996 | +90,283 | +783 | TAIFEX Proxy |
| 自營商 | 9,911 | 10,561 | -650 | 1,328 | 1,638 | -310 | -340 | 6,279 | 3,949 | +2,330 | -631 | TAIFEX Proxy |
| 三大法人合計 | 109,412 | 112,254 | -2,842 | 40,039 | 40,818 | -779 | -2,063 | 112,946 | 115,984 | -3,038 | -1,852 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,829 | TAIFEX Proxy |
| 前十大交易人空方 OI | 84,567 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,262 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-03→2026-11-04) | +1,694 | TAIFEX Proxy snapshots (2026-11-04) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 40.48% | TAIFEX Proxy |
| 夜盤漲跌點數 | +201 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -469 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-05 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-05 20:45:58 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 304,899 | TAIFEX Proxy |
| Call 總未平倉量 OI | 90,160 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 229,988 | TAIFEX Proxy |
| Put 總未平倉量 OI | 33,429 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.33 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.70 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.37 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-03→2026-11-04) | 5.01 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-03→2026-11-04) | 1.60 | 百分點（pp） | TAIFEX Proxy |
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
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 42,500.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-gamma-levels) |

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 2,012,945,029.48 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 13,625,438,503.68 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 履約價資料筆數 | 191 | 資料日期：2026-11-05 |
| 正 Net GEX 最大履約價 | 42,500 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 41,500 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：42,500（494,767,680.58 NT$）、43,000（407,409,463.38 NT$）、42,100（256,762,281.98 NT$）、42,300（254,231,112.45 NT$）、42,800（226,001,378.95 NT$）
- 負 Net GEX Top 5：41,500（-432,857,814.61 NT$）、42,000（-364,212,011.26 NT$）、40,000（-237,449,280.55 NT$）、41,400（-212,229,226.23 NT$）、41,000（-209,119,439.36 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-05","underlying":41574.72,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":2012945029.480298,"gross_gex_1pct":13625438503.684158,"levels":[{"strike":38600.0,"call_gex_1pct":0.0,"put_gex_1pct":-41836495.048114136,"net_gex_1pct":-41836495.048114136,"gross_gex_1pct":41836495.048114136,"call_oi":0,"put_oi":1027},{"strike":38700.0,"call_gex_1pct":0.0,"put_gex_1pct":-9126700.649333818,"net_gex_1pct":-9126700.649333818,"gross_gex_1pct":9126700.649333818,"call_oi":0,"put_oi":205},{"strike":38800.0,"call_gex_1pct":0.0,"put_gex_1pct":-7256819.362592263,"net_gex_1pct":-7256819.362592263,"gross_gex_1pct":7256819.362592263,"call_oi":0,"put_oi":149},{"strike":38900.0,"call_gex_1pct":0.0,"put_gex_1pct":-62386826.90730102,"net_gex_1pct":-62386826.90730102,"gross_gex_1pct":62386826.90730102,"call_oi":0,"put_oi":1216},{"strike":39000.0,"call_gex_1pct":75261.4363983866,"put_gex_1pct":-34657276.6827236,"net_gex_1pct":-34582015.24632521,"gross_gex_1pct":34732538.11912198,"call_oi":1,"put_oi":628},{"strike":39100.0,"call_gex_1pct":0.0,"put_gex_1pct":-23341205.004036754,"net_gex_1pct":-23341205.004036754,"gross_gex_1pct":23341205.004036754,"call_oi":0,"put_oi":387},{"strike":39200.0,"call_gex_1pct":0.0,"put_gex_1pct":-27777612.562694892,"net_gex_1pct":-27777612.562694892,"gross_gex_1pct":27777612.562694892,"call_oi":0,"put_oi":432},{"strike":39300.0,"call_gex_1pct":0.0,"put_gex_1pct":-9235454.666611392,"net_gex_1pct":-9235454.666611392,"gross_gex_1pct":9235454.666611392,"call_oi":0,"put_oi":135},{"strike":39400.0,"call_gex_1pct":91018.92550616503,"put_gex_1pct":-12963565.915322863,"net_gex_1pct":-12872546.989816697,"gross_gex_1pct":13054584.840829028,"call_oi":1,"put_oi":170},{"strike":39500.0,"call_gex_1pct":0.0,"put_gex_1pct":-73905779.29105644,"net_gex_1pct":-73905779.29105644,"gross_gex_1pct":73905779.29105644,"call_oi":0,"put_oi":909},{"strike":39600.0,"call_gex_1pct":0.0,"put_gex_1pct":-19585819.43924557,"net_gex_1pct":-19585819.43924557,"gross_gex_1pct":19585819.43924557,"call_oi":0,"put_oi":221},{"strike":39700.0,"call_gex_1pct":318359.7523869714,"put_gex_1pct":-21880005.53772013,"net_gex_1pct":-21561645.785333157,"gross_gex_1pct":22198365.2901071,"call_oi":3,"put_oi":227},{"strike":39800.0,"call_gex_1pct":336260.2029322484,"put_gex_1pct":-25125088.482236847,"net_gex_1pct":-24788828.279304598,"gross_gex_1pct":25461348.685169097,"call_oi":3,"put_oi":240},{"strike":39900.0,"call_gex_1pct":118174.15459907988,"put_gex_1pct":-28065794.87205469,"net_gex_1pct":-27947620.717455607,"gross_gex_1pct":28183969.02665377,"call_oi":1,"put_oi":247},{"strike":40000.0,"call_gex_1pct":0.0,"put_gex_1pct":-237449280.55103177,"net_gex_1pct":-237449280.55103177,"gross_gex_1pct":237449280.55103177,"call_oi":0,"put_oi":1932},{"strike":40100.0,"call_gex_1pct":132370.01285327104,"put_gex_1pct":-34951916.44880384,"net_gex_1pct":-34819546.43595057,"gross_gex_1pct":35084286.461657114,"call_oi":1,"put_oi":261},{"strike":40200.0,"call_gex_1pct":0.0,"put_gex_1pct":-47383310.13571784,"net_gex_1pct":-47383310.13571784,"gross_gex_1pct":47383310.13571784,"call_oi":0,"put_oi":325},{"strike":40300.0,"call_gex_1pct":1344284.2115742045,"put_gex_1pct":-83358079.17591974,"net_gex_1pct":-82013794.96434553,"gross_gex_1pct":84702363.38749395,"call_oi":9,"put_oi":525},{"strike":40400.0,"call_gex_1pct":1425918.250854899,"put_gex_1pct":-156681500.39966068,"net_gex_1pct":-155255582.14880577,"gross_gex_1pct":158107418.6505156,"call_oi":9,"put_oi":906},{"strike":40500.0,"call_gex_1pct":171477403.01990655,"put_gex_1pct":-213421915.1830967,"net_gex_1pct":-41944512.163190156,"gross_gex_1pct":384899318.2030033,"call_oi":1008,"put_oi":1134},{"strike":40600.0,"call_gex_1pct":179809693.933286,"put_gex_1pct":-156095233.29215303,"net_gex_1pct":23714460.64113298,"gross_gex_1pct":335904927.2254391,"call_oi":1004,"put_oi":761},{"strike":40700.0,"call_gex_1pct":191168732.88224298,"put_gex_1pct":-116282811.03078482,"net_gex_1pct":74885921.85145816,"gross_gex_1pct":307451543.91302776,"call_oi":1001,"put_oi":524},{"strike":40800.0,"call_gex_1pct":201665240.78286868,"put_gex_1pct":-184536478.3128233,"net_gex_1pct":17128762.470045388,"gross_gex_1pct":386201719.095692,"call_oi":1002,"put_oi":761},{"strike":40900.0,"call_gex_1pct":284646974.4535531,"put_gex_1pct":-275435383.64763975,"net_gex_1pct":9211590.80591333,"gross_gex_1pct":560082358.1011928,"call_oi":1331,"put_oi":1048},{"strike":41000.0,"call_gex_1pct":232058867.26475152,"put_gex_1pct":-441178306.6235499,"net_gex_1pct":-209119439.35879835,"gross_gex_1pct":673237173.8883014,"call_oi":1019,"put_oi":1562},{"strike":41100.0,"call_gex_1pct":14334462.028292732,"put_gex_1pct":-122141123.3704439,"net_gex_1pct":-107806661.34215117,"gross_gex_1pct":136475585.39873663,"call_oi":60,"put_oi":404},{"strike":41200.0,"call_gex_1pct":255225941.19689342,"put_gex_1pct":-238402313.48933324,"net_gex_1pct":16823627.70756018,"gross_gex_1pct":493628254.68622667,"call_oi":1008,"put_oi":736},{"strike":41300.0,"call_gex_1pct":271458015.1159747,"put_gex_1pct":-137039093.64165252,"net_gex_1pct":134418921.4743222,"gross_gex_1pct":408497108.75762725,"call_oi":1019,"put_oi":398},{"strike":41400.0,"call_gex_1pct":10430336.975226643,"put_gex_1pct":-222659563.2072142,"net_gex_1pct":-212229226.23198757,"gross_gex_1pct":233089900.18244085,"call_oi":36,"put_oi":612},{"strike":41500.0,"call_gex_1pct":23323626.731960025,"put_gex_1pct":-456181441.34332675,"net_gex_1pct":-432857814.61136675,"gross_gex_1pct":479505068.07528675,"call_oi":82,"put_oi":1224},{"strike":41600.0,"call_gex_1pct":269153923.48990387,"put_gex_1pct":-268782479.69673115,"net_gex_1pct":371443.7931727171,"gross_gex_1pct":537936403.186635,"call_oi":899,"put_oi":696},{"strike":41700.0,"call_gex_1pct":83729098.58194332,"put_gex_1pct":-161624222.47400042,"net_gex_1pct":-77895123.8920571,"gross_gex_1pct":245353321.05594373,"call_oi":279,"put_oi":407},{"strike":41750.0,"call_gex_1pct":23725842.954018097,"put_gex_1pct":-33376541.622495018,"net_gex_1pct":-9650698.66847692,"gross_gex_1pct":57102384.57651311,"call_oi":80,"put_oi":83},{"strike":41800.0,"call_gex_1pct":284295619.2187594,"put_gex_1pct":-260582648.6778559,"net_gex_1pct":23712970.54090351,"gross_gex_1pct":544878267.8966153,"call_oi":935,"put_oi":657},{"strike":41850.0,"call_gex_1pct":37066336.57470947,"put_gex_1pct":-28578939.11696979,"net_gex_1pct":8487397.457739677,"gross_gex_1pct":65645275.691679254,"call_oi":121,"put_oi":70},{"strike":41900.0,"call_gex_1pct":110832827.36174871,"put_gex_1pct":-282531060.19612664,"net_gex_1pct":-171698232.83437794,"gross_gex_1pct":393363887.55787534,"call_oi":364,"put_oi":721},{"strike":41950.0,"call_gex_1pct":29441838.0702743,"put_gex_1pct":-47420373.415121116,"net_gex_1pct":-17978535.344846815,"gross_gex_1pct":76862211.48539542,"call_oi":99,"put_oi":118},{"strike":42000.0,"call_gex_1pct":221428527.6039301,"put_gex_1pct":-585640538.863487,"net_gex_1pct":-364212011.2595569,"gross_gex_1pct":807069066.4674171,"call_oi":748,"put_oi":1506},{"strike":42050.0,"call_gex_1pct":27088641.06844258,"put_gex_1pct":-61244531.489481434,"net_gex_1pct":-34155890.42103885,"gross_gex_1pct":88333172.55792402,"call_oi":92,"put_oi":163},{"strike":42100.0,"call_gex_1pct":388048930.53252,"put_gex_1pct":-131286648.54885544,"net_gex_1pct":256762281.98366457,"gross_gex_1pct":519335579.0813754,"call_oi":1348,"put_oi":351},{"strike":42150.0,"call_gex_1pct":55033526.62868669,"put_gex_1pct":-48187610.94658255,"net_gex_1pct":6845915.6821041405,"gross_gex_1pct":103221137.57526924,"call_oi":193,"put_oi":135},{"strike":42200.0,"call_gex_1pct":112082957.91489519,"put_gex_1pct":-95222716.97725798,"net_gex_1pct":16860240.93763721,"gross_gex_1pct":207305674.89215317,"call_oi":402,"put_oi":285},{"strike":42250.0,"call_gex_1pct":48875377.29492728,"put_gex_1pct":-35051026.943405844,"net_gex_1pct":13824350.351521432,"gross_gex_1pct":83926404.23833312,"call_oi":182,"put_oi":112},{"strike":42300.0,"call_gex_1pct":376445629.91093886,"put_gex_1pct":-122214517.46003577,"net_gex_1pct":254231112.4509031,"gross_gex_1pct":498660147.37097466,"call_oi":1441,"put_oi":421},{"strike":42350.0,"call_gex_1pct":59717724.997115076,"put_gex_1pct":-37268044.97195088,"net_gex_1pct":22449680.025164194,"gross_gex_1pct":96985769.96906596,"call_oi":235,"put_oi":150},{"strike":42400.0,"call_gex_1pct":54090420.35759308,"put_gex_1pct":-86892641.42737769,"net_gex_1pct":-32802221.069784604,"gross_gex_1pct":140983061.78497076,"call_oi":221,"put_oi":430},{"strike":42450.0,"call_gex_1pct":26205654.646360543,"put_gex_1pct":0.0,"net_gex_1pct":26205654.646360543,"gross_gex_1pct":26205654.646360543,"call_oi":111,"put_oi":0},{"strike":42500.0,"call_gex_1pct":494767680.58219635,"put_gex_1pct":0.0,"net_gex_1pct":494767680.58219635,"gross_gex_1pct":494767680.58219635,"call_oi":2184,"put_oi":0},{"strike":42550.0,"call_gex_1pct":35525702.92537008,"put_gex_1pct":0.0,"net_gex_1pct":35525702.92537008,"gross_gex_1pct":35525702.92537008,"call_oi":163,"put_oi":0},{"strike":42600.0,"call_gex_1pct":122016645.73124585,"put_gex_1pct":0.0,"net_gex_1pct":122016645.73124585,"gross_gex_1pct":122016645.73124585,"call_oi":585,"put_oi":0},{"strike":42650.0,"call_gex_1pct":62841326.497783564,"put_gex_1pct":0.0,"net_gex_1pct":62841326.497783564,"gross_gex_1pct":62841326.497783564,"call_oi":315,"put_oi":0},{"strike":42700.0,"call_gex_1pct":127744880.71975388,"put_gex_1pct":0.0,"net_gex_1pct":127744880.71975388,"gross_gex_1pct":127744880.71975388,"call_oi":671,"put_oi":0},{"strike":42750.0,"call_gex_1pct":53973256.415564895,"put_gex_1pct":0.0,"net_gex_1pct":53973256.415564895,"gross_gex_1pct":53973256.415564895,"call_oi":297,"put_oi":0},{"strike":42800.0,"call_gex_1pct":226001378.9529078,"put_gex_1pct":0.0,"net_gex_1pct":226001378.9529078,"gross_gex_1pct":226001378.9529078,"call_oi":1306,"put_oi":0},{"strike":42850.0,"call_gex_1pct":60607665.26213445,"put_gex_1pct":0.0,"net_gex_1pct":60607665.26213445,"gross_gex_1pct":60607665.26213445,"call_oi":368,"put_oi":0},{"strike":42900.0,"call_gex_1pct":112118335.34020846,"put_gex_1pct":0.0,"net_gex_1pct":112118335.34020846,"gross_gex_1pct":112118335.34020846,"call_oi":715,"put_oi":0},{"strike":42950.0,"call_gex_1pct":27889887.48767185,"put_gex_1pct":0.0,"net_gex_1pct":27889887.48767185,"gross_gex_1pct":27889887.48767185,"call_oi":187,"put_oi":0},{"strike":43000.0,"call_gex_1pct":407409463.3773768,"put_gex_1pct":0.0,"net_gex_1pct":407409463.3773768,"gross_gex_1pct":407409463.3773768,"call_oi":2876,"put_oi":0},{"strike":43050.0,"call_gex_1pct":38681592.6798084,"put_gex_1pct":0.0,"net_gex_1pct":38681592.6798084,"gross_gex_1pct":38681592.6798084,"call_oi":288,"put_oi":0},{"strike":43100.0,"call_gex_1pct":95637505.55304892,"put_gex_1pct":0.0,"net_gex_1pct":95637505.55304892,"gross_gex_1pct":95637505.55304892,"call_oi":751,"put_oi":0},{"strike":43150.0,"call_gex_1pct":20902187.273902334,"put_gex_1pct":0.0,"net_gex_1pct":20902187.273902334,"gross_gex_1pct":20902187.273902334,"call_oi":173,"put_oi":0},{"strike":43200.0,"call_gex_1pct":87166702.62633118,"put_gex_1pct":0.0,"net_gex_1pct":87166702.62633118,"gross_gex_1pct":87166702.62633118,"call_oi":755,"put_oi":0},{"strike":43250.0,"call_gex_1pct":32564760.58577552,"put_gex_1pct":0.0,"net_gex_1pct":32564760.58577552,"gross_gex_1pct":32564760.58577552,"call_oi":297,"put_oi":0},{"strike":43300.0,"call_gex_1pct":117486299.24715826,"put_gex_1pct":0.0,"net_gex_1pct":117486299.24715826,"gross_gex_1pct":117486299.24715826,"call_oi":1147,"put_oi":0},{"strike":43350.0,"call_gex_1pct":40765198.466675214,"put_gex_1pct":0.0,"net_gex_1pct":40765198.466675214,"gross_gex_1pct":40765198.466675214,"call_oi":414,"put_oi":0},{"strike":43400.0,"call_gex_1pct":68619769.72095113,"put_gex_1pct":0.0,"net_gex_1pct":68619769.72095113,"gross_gex_1pct":68619769.72095113,"call_oi":741,"put_oi":0},{"strike":43450.0,"call_gex_1pct":23601690.028986882,"put_gex_1pct":0.0,"net_gex_1pct":23601690.028986882,"gross_gex_1pct":23601690.028986882,"call_oi":265,"put_oi":0},{"strike":43500.0,"call_gex_1pct":199294888.427968,"put_gex_1pct":0.0,"net_gex_1pct":199294888.427968,"gross_gex_1pct":199294888.427968,"call_oi":2350,"put_oi":0},{"strike":43550.0,"call_gex_1pct":19651166.44726308,"put_gex_1pct":0.0,"net_gex_1pct":19651166.44726308,"gross_gex_1pct":19651166.44726308,"call_oi":245,"put_oi":0},{"strike":43600.0,"call_gex_1pct":70483704.50620107,"put_gex_1pct":0.0,"net_gex_1pct":70483704.50620107,"gross_gex_1pct":70483704.50620107,"call_oi":925,"put_oi":0},{"strike":43650.0,"call_gex_1pct":17840131.587238323,"put_gex_1pct":0.0,"net_gex_1pct":17840131.587238323,"gross_gex_1pct":17840131.587238323,"call_oi":245,"put_oi":0},{"strike":43700.0,"call_gex_1pct":83047134.76550911,"put_gex_1pct":0.0,"net_gex_1pct":83047134.76550911,"gross_gex_1pct":83047134.76550911,"call_oi":1203,"put_oi":0},{"strike":43750.0,"call_gex_1pct":22119331.69830319,"put_gex_1pct":0.0,"net_gex_1pct":22119331.69830319,"gross_gex_1pct":22119331.69830319,"call_oi":333,"put_oi":0},{"strike":43800.0,"call_gex_1pct":62696287.56898901,"put_gex_1pct":0.0,"net_gex_1pct":62696287.56898901,"gross_gex_1pct":62696287.56898901,"call_oi":989,"put_oi":0},{"strike":43850.0,"call_gex_1pct":14771150.596390286,"put_gex_1pct":0.0,"net_gex_1pct":14771150.596390286,"gross_gex_1pct":14771150.596390286,"call_oi":249,"put_oi":0},{"strike":43900.0,"call_gex_1pct":27664923.467144355,"put_gex_1pct":0.0,"net_gex_1pct":27664923.467144355,"gross_gex_1pct":27664923.467144355,"call_oi":485,"put_oi":0},{"strike":43950.0,"call_gex_1pct":17039019.285403512,"put_gex_1pct":0.0,"net_gex_1pct":17039019.285403512,"gross_gex_1pct":17039019.285403512,"call_oi":314,"put_oi":0},{"strike":44000.0,"call_gex_1pct":205164209.41220868,"put_gex_1pct":0.0,"net_gex_1pct":205164209.41220868,"gross_gex_1pct":205164209.41220868,"call_oi":3933,"put_oi":0},{"strike":44050.0,"call_gex_1pct":20108967.357267927,"put_gex_1pct":0.0,"net_gex_1pct":20108967.357267927,"gross_gex_1pct":20108967.357267927,"call_oi":401,"put_oi":0},{"strike":44100.0,"call_gex_1pct":70507361.23597836,"put_gex_1pct":0.0,"net_gex_1pct":70507361.23597836,"gross_gex_1pct":70507361.23597836,"call_oi":1501,"put_oi":0},{"strike":44150.0,"call_gex_1pct":11025244.555333309,"put_gex_1pct":0.0,"net_gex_1pct":11025244.555333309,"gross_gex_1pct":11025244.555333309,"call_oi":248,"put_oi":0},{"strike":44200.0,"call_gex_1pct":86442222.66014624,"put_gex_1pct":0.0,"net_gex_1pct":86442222.66014624,"gross_gex_1pct":86442222.66014624,"call_oi":2027,"put_oi":0},{"strike":44250.0,"call_gex_1pct":12172617.422693761,"put_gex_1pct":0.0,"net_gex_1pct":12172617.422693761,"gross_gex_1pct":12172617.422693761,"call_oi":293,"put_oi":0},{"strike":44300.0,"call_gex_1pct":74769645.34824139,"put_gex_1pct":0.0,"net_gex_1pct":74769645.34824139,"gross_gex_1pct":74769645.34824139,"call_oi":1876,"put_oi":0},{"strike":44350.0,"call_gex_1pct":10630256.022922631,"put_gex_1pct":0.0,"net_gex_1pct":10630256.022922631,"gross_gex_1pct":10630256.022922631,"call_oi":283,"put_oi":0},{"strike":44400.0,"call_gex_1pct":22341940.680781856,"put_gex_1pct":0.0,"net_gex_1pct":22341940.680781856,"gross_gex_1pct":22341940.680781856,"call_oi":646,"put_oi":0},{"strike":44450.0,"call_gex_1pct":7034799.6368758725,"put_gex_1pct":0.0,"net_gex_1pct":7034799.6368758725,"gross_gex_1pct":7034799.6368758725,"call_oi":213,"put_oi":0},{"strike":44500.0,"call_gex_1pct":122071859.56543016,"put_gex_1pct":0.0,"net_gex_1pct":122071859.56543016,"gross_gex_1pct":122071859.56543016,"call_oi":3874,"put_oi":0},{"strike":44550.0,"call_gex_1pct":9880416.155939141,"put_gex_1pct":0.0,"net_gex_1pct":9880416.155939141,"gross_gex_1pct":9880416.155939141,"call_oi":329,"put_oi":0},{"strike":44600.0,"call_gex_1pct":22285188.95550391,"put_gex_1pct":0.0,"net_gex_1pct":22285188.95550391,"gross_gex_1pct":22285188.95550391,"call_oi":801,"put_oi":0},{"strike":44650.0,"call_gex_1pct":10434925.721759195,"put_gex_1pct":0.0,"net_gex_1pct":10434925.721759195,"gross_gex_1pct":10434925.721759195,"call_oi":384,"put_oi":0},{"strike":44700.0,"call_gex_1pct":24569168.677525245,"put_gex_1pct":0.0,"net_gex_1pct":24569168.677525245,"gross_gex_1pct":24569168.677525245,"call_oi":947,"put_oi":0},{"strike":44750.0,"call_gex_1pct":9395302.287997331,"put_gex_1pct":0.0,"net_gex_1pct":9395302.287997331,"gross_gex_1pct":9395302.287997331,"call_oi":395,"put_oi":0},{"strike":44800.0,"call_gex_1pct":18322755.50606183,"put_gex_1pct":0.0,"net_gex_1pct":18322755.50606183,"gross_gex_1pct":18322755.50606183,"call_oi":788,"put_oi":0},{"strike":44850.0,"call_gex_1pct":5813026.1053326335,"put_gex_1pct":0.0,"net_gex_1pct":5813026.1053326335,"gross_gex_1pct":5813026.1053326335,"call_oi":265,"put_oi":0},{"strike":44900.0,"call_gex_1pct":8570523.951205352,"put_gex_1pct":0.0,"net_gex_1pct":8570523.951205352,"gross_gex_1pct":8570523.951205352,"call_oi":412,"put_oi":0},{"strike":44950.0,"call_gex_1pct":6418153.190122084,"put_gex_1pct":0.0,"net_gex_1pct":6418153.190122084,"gross_gex_1pct":6418153.190122084,"call_oi":326,"put_oi":0},{"strike":45000.0,"call_gex_1pct":70063506.1894725,"put_gex_1pct":0.0,"net_gex_1pct":70063506.1894725,"gross_gex_1pct":70063506.1894725,"call_oi":3769,"put_oi":0},{"strike":45050.0,"call_gex_1pct":4306243.205921395,"put_gex_1pct":0.0,"net_gex_1pct":4306243.205921395,"gross_gex_1pct":4306243.205921395,"call_oi":246,"put_oi":0},{"strike":45100.0,"call_gex_1pct":11978679.874069836,"put_gex_1pct":0.0,"net_gex_1pct":11978679.874069836,"gross_gex_1pct":11978679.874069836,"call_oi":729,"put_oi":0},{"strike":45150.0,"call_gex_1pct":3073230.503322047,"put_gex_1pct":0.0,"net_gex_1pct":3073230.503322047,"gross_gex_1pct":3073230.503322047,"call_oi":200,"put_oi":0},{"strike":45200.0,"call_gex_1pct":8725900.446990183,"put_gex_1pct":0.0,"net_gex_1pct":8725900.446990183,"gross_gex_1pct":8725900.446990183,"call_oi":636,"put_oi":0},{"strike":45250.0,"call_gex_1pct":2540377.0645292997,"put_gex_1pct":0.0,"net_gex_1pct":2540377.0645292997,"gross_gex_1pct":2540377.0645292997,"call_oi":189,"put_oi":0},{"strike":45300.0,"call_gex_1pct":9350799.84220481,"put_gex_1pct":0.0,"net_gex_1pct":9350799.84220481,"gross_gex_1pct":9350799.84220481,"call_oi":743,"put_oi":0},{"strike":45350.0,"call_gex_1pct":2984487.1031390876,"put_gex_1pct":0.0,"net_gex_1pct":2984487.1031390876,"gross_gex_1pct":2984487.1031390876,"call_oi":250,"put_oi":0},{"strike":45400.0,"call_gex_1pct":4116668.4559570774,"put_gex_1pct":0.0,"net_gex_1pct":4116668.4559570774,"gross_gex_1pct":4116668.4559570774,"call_oi":371,"put_oi":0},{"strike":45450.0,"call_gex_1pct":1569015.1825579964,"put_gex_1pct":0.0,"net_gex_1pct":1569015.1825579964,"gross_gex_1pct":1569015.1825579964,"call_oi":153,"put_oi":0},{"strike":45500.0,"call_gex_1pct":13742513.20285669,"put_gex_1pct":0.0,"net_gex_1pct":13742513.20285669,"gross_gex_1pct":13742513.20285669,"call_oi":1427,"put_oi":0},{"strike":45550.0,"call_gex_1pct":2505297.1052034553,"put_gex_1pct":0.0,"net_gex_1pct":2505297.1052034553,"gross_gex_1pct":2505297.1052034553,"call_oi":278,"put_oi":0},{"strike":45600.0,"call_gex_1pct":15494141.58117897,"put_gex_1pct":0.0,"net_gex_1pct":15494141.58117897,"gross_gex_1pct":15494141.58117897,"call_oi":1845,"put_oi":0},{"strike":45650.0,"call_gex_1pct":1306627.4664425184,"put_gex_1pct":0.0,"net_gex_1pct":1306627.4664425184,"gross_gex_1pct":1306627.4664425184,"call_oi":163,"put_oi":0},{"strike":45700.0,"call_gex_1pct":3372412.8987381123,"put_gex_1pct":0.0,"net_gex_1pct":3372412.8987381123,"gross_gex_1pct":3372412.8987381123,"call_oi":455,"put_oi":0},{"strike":45750.0,"call_gex_1pct":1007330.2189877611,"put_gex_1pct":0.0,"net_gex_1pct":1007330.2189877611,"gross_gex_1pct":1007330.2189877611,"call_oi":143,"put_oi":0},{"strike":45800.0,"call_gex_1pct":2004172.7142270876,"put_gex_1pct":0.0,"net_gex_1pct":2004172.7142270876,"gross_gex_1pct":2004172.7142270876,"call_oi":311,"put_oi":0},{"strike":45850.0,"call_gex_1pct":779159.421714601,"put_gex_1pct":0.0,"net_gex_1pct":779159.421714601,"gross_gex_1pct":779159.421714601,"call_oi":128,"put_oi":0},{"strike":45900.0,"call_gex_1pct":3532845.4890703955,"put_gex_1pct":0.0,"net_gex_1pct":3532845.4890703955,"gross_gex_1pct":3532845.4890703955,"call_oi":616,"put_oi":0},{"strike":45950.0,"call_gex_1pct":786573.5991984962,"put_gex_1pct":0.0,"net_gex_1pct":786573.5991984962,"gross_gex_1pct":786573.5991984962,"call_oi":146,"put_oi":0},{"strike":46000.0,"call_gex_1pct":26846733.385333944,"put_gex_1pct":0.0,"net_gex_1pct":26846733.385333944,"gross_gex_1pct":26846733.385333944,"call_oi":5323,"put_oi":0},{"strike":46050.0,"call_gex_1pct":893476.8835773788,"put_gex_1pct":0.0,"net_gex_1pct":893476.8835773788,"gross_gex_1pct":893476.8835773788,"call_oi":190,"put_oi":0},{"strike":46100.0,"call_gex_1pct":3628803.521941055,"put_gex_1pct":0.0,"net_gex_1pct":3628803.521941055,"gross_gex_1pct":3628803.521941055,"call_oi":886,"put_oi":0},{"strike":46150.0,"call_gex_1pct":390501.6996854552,"put_gex_1pct":0.0,"net_gex_1pct":390501.6996854552,"gross_gex_1pct":390501.6996854552,"call_oi":97,"put_oi":0},{"strike":46200.0,"call_gex_1pct":811371.4007804266,"put_gex_1pct":0.0,"net_gex_1pct":811371.4007804266,"gross_gex_1pct":811371.4007804266,"call_oi":220,"put_oi":0},{"strike":46250.0,"call_gex_1pct":261093.163624717,"put_gex_1pct":0.0,"net_gex_1pct":261093.163624717,"gross_gex_1pct":261093.163624717,"call_oi":72,"put_oi":0},{"strike":46300.0,"call_gex_1pct":2378676.3913721642,"put_gex_1pct":0.0,"net_gex_1pct":2378676.3913721642,"gross_gex_1pct":2378676.3913721642,"call_oi":667,"put_oi":0},{"strike":46350.0,"call_gex_1pct":417867.2434725221,"put_gex_1pct":0.0,"net_gex_1pct":417867.2434725221,"gross_gex_1pct":417867.2434725221,"call_oi":129,"put_oi":0},{"strike":46400.0,"call_gex_1pct":1002231.2662379858,"put_gex_1pct":0.0,"net_gex_1pct":1002231.2662379858,"gross_gex_1pct":1002231.2662379858,"call_oi":383,"put_oi":0},{"strike":46450.0,"call_gex_1pct":159612.1857679982,"put_gex_1pct":0.0,"net_gex_1pct":159612.1857679982,"gross_gex_1pct":159612.1857679982,"call_oi":62,"put_oi":0},{"strike":46500.0,"call_gex_1pct":16690682.379074365,"put_gex_1pct":0.0,"net_gex_1pct":16690682.379074365,"gross_gex_1pct":16690682.379074365,"call_oi":6589,"put_oi":0},{"strike":46550.0,"call_gex_1pct":289178.7317736552,"put_gex_1pct":0.0,"net_gex_1pct":289178.7317736552,"gross_gex_1pct":289178.7317736552,"call_oi":116,"put_oi":0},{"strike":46600.0,"call_gex_1pct":645342.057218896,"put_gex_1pct":0.0,"net_gex_1pct":645342.057218896,"gross_gex_1pct":645342.057218896,"call_oi":263,"put_oi":0},{"strike":46650.0,"call_gex_1pct":253209.43390915243,"put_gex_1pct":0.0,"net_gex_1pct":253209.43390915243,"gross_gex_1pct":253209.43390915243,"call_oi":119,"put_oi":0},{"strike":46700.0,"call_gex_1pct":182259.04609489124,"put_gex_1pct":0.0,"net_gex_1pct":182259.04609489124,"gross_gex_1pct":182259.04609489124,"call_oi":87,"put_oi":0},{"strike":46750.0,"call_gex_1pct":92829.83540207638,"put_gex_1pct":0.0,"net_gex_1pct":92829.83540207638,"gross_gex_1pct":92829.83540207638,"call_oi":45,"put_oi":0},{"strike":46800.0,"call_gex_1pct":550575.1263807295,"put_gex_1pct":0.0,"net_gex_1pct":550575.1263807295,"gross_gex_1pct":550575.1263807295,"call_oi":271,"put_oi":0},{"strike":46850.0,"call_gex_1pct":110064.67413522654,"put_gex_1pct":0.0,"net_gex_1pct":110064.67413522654,"gross_gex_1pct":110064.67413522654,"call_oi":55,"put_oi":0},{"strike":46900.0,"call_gex_1pct":100544.40551903725,"put_gex_1pct":0.0,"net_gex_1pct":100544.40551903725,"gross_gex_1pct":100544.40551903725,"call_oi":51,"put_oi":0},{"strike":46950.0,"call_gex_1pct":160981.65640782882,"put_gex_1pct":0.0,"net_gex_1pct":160981.65640782882,"gross_gex_1pct":160981.65640782882,"call_oi":97,"put_oi":0},{"strike":47000.0,"call_gex_1pct":1733432.3001712733,"put_gex_1pct":0.0,"net_gex_1pct":1733432.3001712733,"gross_gex_1pct":1733432.3001712733,"call_oi":1060,"put_oi":0},{"strike":47050.0,"call_gex_1pct":27397.293884462495,"put_gex_1pct":0.0,"net_gex_1pct":27397.293884462495,"gross_gex_1pct":27397.293884462495,"call_oi":17,"put_oi":0},{"strike":47100.0,"call_gex_1pct":55596.15732994876,"put_gex_1pct":0.0,"net_gex_1pct":55596.15732994876,"gross_gex_1pct":55596.15732994876,"call_oi":35,"put_oi":0},{"strike":47150.0,"call_gex_1pct":14092.77122022949,"put_gex_1pct":0.0,"net_gex_1pct":14092.77122022949,"gross_gex_1pct":14092.77122022949,"call_oi":9,"put_oi":0},{"strike":47200.0,"call_gex_1pct":103434.15797479343,"put_gex_1pct":0.0,"net_gex_1pct":103434.15797479343,"gross_gex_1pct":103434.15797479343,"call_oi":67,"put_oi":0},{"strike":47250.0,"call_gex_1pct":27400.221795516092,"put_gex_1pct":0.0,"net_gex_1pct":27400.221795516092,"gross_gex_1pct":27400.221795516092,"call_oi":18,"put_oi":0},{"strike":47300.0,"call_gex_1pct":1196433.0330687594,"put_gex_1pct":0.0,"net_gex_1pct":1196433.0330687594,"gross_gex_1pct":1196433.0330687594,"call_oi":797,"put_oi":0},{"strike":47350.0,"call_gex_1pct":5922.345005335694,"put_gex_1pct":0.0,"net_gex_1pct":5922.345005335694,"gross_gex_1pct":5922.345005335694,"call_oi":4,"put_oi":0},{"strike":47400.0,"call_gex_1pct":32085.724571000137,"put_gex_1pct":0.0,"net_gex_1pct":32085.724571000137,"gross_gex_1pct":32085.724571000137,"call_oi":27,"put_oi":0},{"strike":47450.0,"call_gex_1pct":4689.043115847129,"put_gex_1pct":0.0,"net_gex_1pct":4689.043115847129,"gross_gex_1pct":4689.043115847129,"call_oi":4,"put_oi":0},{"strike":47500.0,"call_gex_1pct":119121.55101184055,"put_gex_1pct":0.0,"net_gex_1pct":119121.55101184055,"gross_gex_1pct":119121.55101184055,"call_oi":103,"put_oi":0},{"strike":47550.0,"call_gex_1pct":10270.139766451386,"put_gex_1pct":0.0,"net_gex_1pct":10270.139766451386,"gross_gex_1pct":10270.139766451386,"call_oi":9,"put_oi":0},{"strike":47600.0,"call_gex_1pct":21395.338622279774,"put_gex_1pct":0.0,"net_gex_1pct":21395.338622279774,"gross_gex_1pct":21395.338622279774,"call_oi":19,"put_oi":0},{"strike":47650.0,"call_gex_1pct":26672.189861948198,"put_gex_1pct":0.0,"net_gex_1pct":26672.189861948198,"gross_gex_1pct":26672.189861948198,"call_oi":24,"put_oi":0},{"strike":47700.0,"call_gex_1pct":122856.08016106785,"put_gex_1pct":0.0,"net_gex_1pct":122856.08016106785,"gross_gex_1pct":122856.08016106785,"call_oi":112,"put_oi":0},{"strike":47750.0,"call_gex_1pct":152678.3564491608,"put_gex_1pct":0.0,"net_gex_1pct":152678.3564491608,"gross_gex_1pct":152678.3564491608,"call_oi":141,"put_oi":0},{"strike":47800.0,"call_gex_1pct":80176.5030954952,"put_gex_1pct":0.0,"net_gex_1pct":80176.5030954952,"gross_gex_1pct":80176.5030954952,"call_oi":75,"put_oi":0},{"strike":47850.0,"call_gex_1pct":202656.9723701372,"put_gex_1pct":0.0,"net_gex_1pct":202656.9723701372,"gross_gex_1pct":202656.9723701372,"call_oi":192,"put_oi":0},{"strike":47900.0,"call_gex_1pct":32310.429936005894,"put_gex_1pct":0.0,"net_gex_1pct":32310.429936005894,"gross_gex_1pct":32310.429936005894,"call_oi":31,"put_oi":0},{"strike":47950.0,"call_gex_1pct":1029.3125934472635,"put_gex_1pct":0.0,"net_gex_1pct":1029.3125934472635,"gross_gex_1pct":1029.3125934472635,"call_oi":1,"put_oi":0},{"strike":48000.0,"call_gex_1pct":201290.61757161052,"put_gex_1pct":0.0,"net_gex_1pct":201290.61757161052,"gross_gex_1pct":201290.61757161052,"call_oi":198,"put_oi":0},{"strike":48050.0,"call_gex_1pct":6025.107056780684,"put_gex_1pct":0.0,"net_gex_1pct":6025.107056780684,"gross_gex_1pct":6025.107056780684,"call_oi":6,"put_oi":0},{"strike":48100.0,"call_gex_1pct":5952.006363031806,"put_gex_1pct":0.0,"net_gex_1pct":5952.006363031806,"gross_gex_1pct":5952.006363031806,"call_oi":6,"put_oi":0},{"strike":48150.0,"call_gex_1pct":1960.1239386030759,"put_gex_1pct":0.0,"net_gex_1pct":1960.1239386030759,"gross_gex_1pct":1960.1239386030759,"call_oi":2,"put_oi":0},{"strike":48200.0,"call_gex_1pct":11620.326183987198,"put_gex_1pct":0.0,"net_gex_1pct":11620.326183987198,"gross_gex_1pct":11620.326183987198,"call_oi":12,"put_oi":0},{"strike":48250.0,"call_gex_1pct":2870.6706354073913,"put_gex_1pct":0.0,"net_gex_1pct":2870.6706354073913,"gross_gex_1pct":2870.6706354073913,"call_oi":3,"put_oi":0},{"strike":48300.0,"call_gex_1pct":945.6447957940134,"put_gex_1pct":0.0,"net_gex_1pct":945.6447957940134,"gross_gex_1pct":945.6447957940134,"call_oi":1,"put_oi":0},{"strike":48400.0,"call_gex_1pct":7390.437109839323,"put_gex_1pct":0.0,"net_gex_1pct":7390.437109839323,"gross_gex_1pct":7390.437109839323,"call_oi":8,"put_oi":0},{"strike":48500.0,"call_gex_1pct":65001.17346719433,"put_gex_1pct":0.0,"net_gex_1pct":65001.17346719433,"gross_gex_1pct":65001.17346719433,"call_oi":72,"put_oi":0},{"strike":48600.0,"call_gex_1pct":14422.858954419937,"put_gex_1pct":0.0,"net_gex_1pct":14422.858954419937,"gross_gex_1pct":14422.858954419937,"call_oi":22,"put_oi":0},{"strike":48700.0,"call_gex_1pct":1923.0265796360197,"put_gex_1pct":0.0,"net_gex_1pct":1923.0265796360197,"gross_gex_1pct":1923.0265796360197,"call_oi":3,"put_oi":0},{"strike":48800.0,"call_gex_1pct":5015.730367232998,"put_gex_1pct":0.0,"net_gex_1pct":5015.730367232998,"gross_gex_1pct":5015.730367232998,"call_oi":8,"put_oi":0},{"strike":48900.0,"call_gex_1pct":10428.314130359973,"put_gex_1pct":0.0,"net_gex_1pct":10428.314130359973,"gross_gex_1pct":10428.314130359973,"call_oi":17,"put_oi":0},{"strike":49000.0,"call_gex_1pct":115272.15377700522,"put_gex_1pct":0.0,"net_gex_1pct":115272.15377700522,"gross_gex_1pct":115272.15377700522,"call_oi":192,"put_oi":0},{"strike":49200.0,"call_gex_1pct":4029.3380833138513,"put_gex_1pct":0.0,"net_gex_1pct":4029.3380833138513,"gross_gex_1pct":4029.3380833138513,"call_oi":7,"put_oi":0},{"strike":49300.0,"call_gex_1pct":7894.257540943604,"put_gex_1pct":0.0,"net_gex_1pct":7894.257540943604,"gross_gex_1pct":7894.257540943604,"call_oi":14,"put_oi":0},{"strike":49400.0,"call_gex_1pct":552.5276529560788,"put_gex_1pct":0.0,"net_gex_1pct":552.5276529560788,"gross_gex_1pct":552.5276529560788,"call_oi":1,"put_oi":0},{"strike":49500.0,"call_gex_1pct":11914.271922516926,"put_gex_1pct":0.0,"net_gex_1pct":11914.271922516926,"gross_gex_1pct":11914.271922516926,"call_oi":22,"put_oi":0},{"strike":49600.0,"call_gex_1pct":1592.8464810139897,"put_gex_1pct":0.0,"net_gex_1pct":1592.8464810139897,"gross_gex_1pct":1592.8464810139897,"call_oi":3,"put_oi":0},{"strike":49700.0,"call_gex_1pct":520.6844774760735,"put_gex_1pct":0.0,"net_gex_1pct":520.6844774760735,"gross_gex_1pct":520.6844774760735,"call_oi":1,"put_oi":0},{"strike":49900.0,"call_gex_1pct":6013.5523662787355,"put_gex_1pct":0.0,"net_gex_1pct":6013.5523662787355,"gross_gex_1pct":6013.5523662787355,"call_oi":12,"put_oi":0},{"strike":50000.0,"call_gex_1pct":9628.880606648012,"put_gex_1pct":0.0,"net_gex_1pct":9628.880606648012,"gross_gex_1pct":9628.880606648012,"call_oi":33,"put_oi":0},{"strike":50100.0,"call_gex_1pct":3150.0389926035623,"put_gex_1pct":0.0,"net_gex_1pct":3150.0389926035623,"gross_gex_1pct":3150.0389926035623,"call_oi":11,"put_oi":0},{"strike":50300.0,"call_gex_1pct":1656.1587494521893,"put_gex_1pct":0.0,"net_gex_1pct":1656.1587494521893,"gross_gex_1pct":1656.1587494521893,"call_oi":6,"put_oi":0},{"strike":50400.0,"call_gex_1pct":3253.0698230540374,"put_gex_1pct":0.0,"net_gex_1pct":3253.0698230540374,"gross_gex_1pct":3253.0698230540374,"call_oi":12,"put_oi":0},{"strike":50500.0,"call_gex_1pct":798.8961078870357,"put_gex_1pct":0.0,"net_gex_1pct":798.8961078870357,"gross_gex_1pct":798.8961078870357,"call_oi":3,"put_oi":0},{"strike":50600.0,"call_gex_1pct":261.6491386155069,"put_gex_1pct":0.0,"net_gex_1pct":261.6491386155069,"gross_gex_1pct":261.6491386155069,"call_oi":1,"put_oi":0},{"strike":50700.0,"call_gex_1pct":4114.156703264884,"put_gex_1pct":0.0,"net_gex_1pct":4114.156703264884,"gross_gex_1pct":4114.156703264884,"call_oi":16,"put_oi":0},{"strike":50800.0,"call_gex_1pct":1263.7514485747026,"put_gex_1pct":0.0,"net_gex_1pct":1263.7514485747026,"gross_gex_1pct":1263.7514485747026,"call_oi":5,"put_oi":0},{"strike":50900.0,"call_gex_1pct":248.49051655116162,"put_gex_1pct":0.0,"net_gex_1pct":248.49051655116162,"gross_gex_1pct":248.49051655116162,"call_oi":1,"put_oi":0},{"strike":51000.0,"call_gex_1pct":13927.985249993442,"put_gex_1pct":0.0,"net_gex_1pct":13927.985249993442,"gross_gex_1pct":13927.985249993442,"call_oi":57,"put_oi":0},{"strike":51300.0,"call_gex_1pct":930.4204173600868,"put_gex_1pct":0.0,"net_gex_1pct":930.4204173600868,"gross_gex_1pct":930.4204173600868,"call_oi":4,"put_oi":0},{"strike":51500.0,"call_gex_1pct":225.2952094901492,"put_gex_1pct":0.0,"net_gex_1pct":225.2952094901492,"gross_gex_1pct":225.2952094901492,"call_oi":1,"put_oi":0},{"strike":51800.0,"call_gex_1pct":1935.3308965950196,"put_gex_1pct":0.0,"net_gex_1pct":1935.3308965950196,"gross_gex_1pct":1935.3308965950196,"call_oi":9,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,950 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 175,734 | 177,375 | -1,641 | 74,710 | 75,626 | -916 | -725 | TAIFEX Proxy |
| 投信 | 2,760 | 4,247 | -1,487 | 0 | 0 | +0 | -1,487 | TAIFEX Proxy |
| 自營商 | 146,592 | 151,018 | -4,426 | 45,931 | 46,158 | -227 | -4,199 | TAIFEX Proxy |
| 三大法人合計 | 325,086 | 332,640 | -7,554 | 120,641 | 121,784 | -1,143 | -6,411 | TAIFEX Proxy |
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
| 買權多空淨 OI 變化 (2026-11-03→2026-11-04) | -1,079 | TAIFEX Proxy snapshots (2026-11-04) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,715 | TAIFEX Proxy |
| 賣權空方 OI | 11,434 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,719 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-03→2026-11-04) | -427 | TAIFEX Proxy snapshots (2026-11-04) |
- 資料日期：買權 2026-11-04／賣權 2026-11-04 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,694 | 2026-11-03→2026-11-04 | TAIFEX Proxy snapshots (2026-11-04) |
| 買權前十大 | -1,079 | 2026-11-03→2026-11-04 | TAIFEX Proxy snapshots (2026-11-04) |
| 賣權前十大 | -427 | 2026-11-03→2026-11-04 | TAIFEX Proxy snapshots (2026-11-04) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-05；資料時間：2026-11-05 20:45:58；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (5)：margin.fin_yi, margin.fin_chg_yi, margin.ratio, options.chain_oi_change, options.wall_change
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202611W1→新202611F1），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`unavailable（TWSE 自建、Blave、同 T0 人工輸入皆不可用）`
- sbl_bal：`TWSE TWT72U（SLBNLB；上市+上櫃）`
- sbl_sale_bal：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- sbl_sale_chg：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：上市融資維持率 unavailable；自建計算：ValueError: listed securities missing T0 close: ['1589']；Blave：exact T0 2026-11-05 not found。不影響其他融資融券欄位、DATA_REPORT、JSON 與 Dashboard 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,024.6 | -95,651 | -2,975 | -469 | -1,641 | -916 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +225.9 | +90,283 | +783 | +0 | -1,487 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -435.3 | +2,330 | -650 | -310 | -4,426 | -227 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
