# DATA_REPORT_20260924

- 報告日期：`2026-09-24`
- T0 交易日期：`2026-09-24`
- 資料產出時間：`2026-09-24 19:14:13`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,024.60 | 點 | twse-proxy |
| 開盤 | 48,075.39 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,117.54 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,754.72 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,024.60 | 點 | twse-proxy |
| 漲跌點數 | -132.69 | 點 | twse-proxy |
| 漲跌幅 | -0.28 | % | twse-proxy |
| 成交金額 | 7,755.9 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 386 | twse-proxy |
| 下跌家數 | 546 | twse-proxy |
| 平盤家數 | 140 | twse-proxy |
| 漲停家數 | 11 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 389 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 380 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 101 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 12 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -338.0 | 億元 | twse-proxy /institutional |
| 投信 | -114.1 | 億元 | twse-proxy /institutional |
| 自營商 | +13.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -438.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 213,059 | 張 | HiStock |
| 融券增減 | -3,685 | 張 | HiStock |
| 融資維持率 | unavailable | % | istock.tw |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,461,727 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 7,755.9 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,950.1 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 9,706.1 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,706.03 | -58.67 | -0.76 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,936.04 | -186.05 | -0.69 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,470.29 | -12.06 | -0.04 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,511.59 | -537.24 | -1.03 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,534.28 | 101.11 | +0.81 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.09 | 0.91 | +5.99 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,513.99 | 495.04 | +0.76 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,080.92 | 73.20 | +1.04 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,761.13 | -72.99 | -0.29 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,888.37 | -48.15 | -1.22 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 13,316.97 | -319.10 | -2.34 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,731.00 | -41.50 | -0.53 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,487.00 | -277.75 | -0.90 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,707.00 | -166.00 | -0.32 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,851.30 | -8.90 | -0.31 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.85 | 0.14 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.11 | 0.15 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.40 | 0.11 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.80 | 0.12 | +0.36 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.24 | 0.14 | +0.14 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.71 | 1.24 | +0.79 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,369.49 | 19.13 | +1.42 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 446.57 | -5.43 | -1.20 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.68 | -1.09 | -4.23 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 43.93 | 0.20 | +0.46 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 93.08 | 0.92 | +1.00 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,290.80 | -27.60 | -0.64 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,541.61 | -841.40 | -1.00 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：外資提款去過中秋 聯發科領載板散熱撐住4萬8
  - 來源：Yahoo 台股；發布時間：2026-09-24T08:48:36Z；台北時間：2026-09-24 16:48
  - 摘要：神山壓盤，台股中秋節前驚險守住4萬8！今（24）日受到美債殖利率攀高、美股科技股回檔及連假前獲利了結賣壓影響，加權指數盤中一度下挫逾400點，尾盤低接買盤進場收斂跌幅，終場下跌132.69點或0.28%，收48,024.60點，成交金額7,
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%80%92%E8%B2%A8338%E5%84%84%E9%81%8E%E4%B8%AD%E7%A7%8B%E5%8F%B0%E8%82%A1%E9%A9%9A%E5%AE%884%E8%90%AC8-%E8%81%AF%E7%99%BC%E7%A7%91%E6%BC%B2%E7%99%BE%E5%85%83%E6%95%91%E6%8F%B4%E9%A0%98%E8%BC%89%E6%9D%BF%E6%95%A3%E7%86%B1%E8%A1%9D%E9%8B%92%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-084836092.html
- 事件2：波音、空巴訂單塞爆！勇鷹號完成交機 漢翔轉向民航與無人機佈局
  - 來源：Yahoo 台股；發布時間：2026-09-24T11:00:24Z；台北時間：2026-09-24 19:00
  - 摘要：國機國造指標機種─勇鷹號高級教練機，歷時9年餘的新式高教機研發及量產任務畫下句點，漢翔總經理莊秀美今（24）日強調，漢翔過去的營收一半是國防，一半是民用航空，因為民用航空的蓬勃發展，所以漢翔預期民用航空的營收會不斷創新高，不管是波音或者空中
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B3%A2%E9%9F%B3-%E7%A9%BA%E5%B7%B4%E8%A8%82%E5%96%AE%E5%A1%9E%E7%88%86-%E5%8B%87%E9%B7%B9%E8%99%9F%E5%AE%8C%E6%88%90%E4%BA%A4%E6%A9%9F-%E6%BC%A2%E7%BF%94%E8%BD%89%E5%90%91%E6%B0%91%E8%88%AA%E8%88%87%E7%84%A1%E4%BA%BA%E6%A9%9F%E4%BD%88%E5%B1%80-110024050.html
- 事件3：無畏金融股跌勢！投信進貨「這4檔」8千多張　投80.6億元連36日敲進玉山金
  - 來源：Yahoo 台股；發布時間：2026-09-24T11:00:00Z；台北時間：2026-09-24 19:00
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導台股加權指數今（24）日收在48024.60點，下跌132.69點，跌幅0.28%，成交量達7382億元。根據證交所資料，投信賣超114.09億元...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%84%A1%E7%95%8F%E9%87%91%E8%9E%8D%E8%82%A1%E8%B7%8C%E5%8B%A2-%E6%8A%95%E4%BF%A1%E9%80%B2%E8%B2%A8-%E9%80%994%E6%AA%94-8%E5%8D%83%E5%A4%9A%E5%BC%B5-%E6%8A%9580-110000578.html
- 事件4：長假前外資撤退！新台幣盤中重貶逾1角  收盤守住31.7價位
  - 來源：Yahoo 台股；發布時間：2026-09-24T10:50:35Z；台北時間：2026-09-24 18:50
  - 摘要：長假前外資撤退，加上市場對聯準會（Fed）升息預期再起，美元指數重返101大關，主要亞幣普遍承壓。新台幣兌美元匯率24日盤中一度跌破31.8元、重貶逾1角，尾盤在央行進場調節下收斂跌幅，終場收在31.78元、貶6.4分，匯價連2黑，成交量略
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%95%B7%E5%81%87%E5%89%8D%E5%A4%96%E8%B3%87%E6%92%A4%E9%80%80-%E6%96%B0%E5%8F%B0%E5%B9%A3%E7%9B%A4%E4%B8%AD%E9%87%8D%E8%B2%B6%E9%80%BE1%E8%A7%92-%E6%94%B6%E7%9B%A4%E5%AE%88%E4%BD%8F31-7%E5%83%B9%E4%BD%8D-105035092.html
- 事件5：聯茂8月獲利暴衝853%超預期！大摩喊話：第3季財測太保守　 再喊買「2檔CCL台廠」
  - 來源：Yahoo 台股；發布時間：2026-09-24T10:45:00Z；台北時間：2026-09-24 18:45
  - 摘要：[FTNN新聞網]記者周雅琦／綜合報導銅箔基板（CCL）大廠聯茂（6213）8月自結財報呈現爆發性成長，單月稅後淨利達9.24億元、年增852.58%，每股稅後純益（EPS）...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E8%8C%828%E6%9C%88%E7%8D%B2%E5%88%A9%E6%9A%B4%E8%A1%9D853-%E8%B6%85%E9%A0%90%E6%9C%9F-%E5%A4%A7%E6%91%A9%E5%96%8A%E8%A9%B1-%E7%AC%AC3%E5%AD%A3%E8%B2%A1%E6%B8%AC%E5%A4%AA%E4%BF%9D%E5%AE%88-%E5%86%8D%E5%96%8A%E8%B2%B7-104500825.html
- 事件6：當沖虧了好痛苦！ 他崩潰「晚上都睡不著」 過來人勸退：贏不了
  - 來源：Yahoo 台股；發布時間：2026-09-24T10:43:00Z；台北時間：2026-09-24 18:43
  - 摘要：當沖的刺激感與快速獲利的機會吸引部分投資人，但實際操作卻並不容易。有網友表示，自己因當沖虧損心情大受影響，甚至晚上都睡不著，不少過來人都勸他「別沖了」。
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%95%B6%E6%B2%96%E8%99%A7%E4%BA%86%E5%A5%BD%E7%97%9B%E8%8B%A6-%E4%BB%96%E5%B4%A9%E6%BD%B0-%E6%99%9A%E4%B8%8A%E9%83%BD%E7%9D%A1%E4%B8%8D%E8%91%97-%E9%81%8E%E4%BE%86%E4%BA%BA%E5%8B%B8%E9%80%80-%E8%B4%8F%E4%B8%8D%E4%BA%86-104300007.html
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
- 事件10：30-year Treasury yield hits highest level since 2004
  - 來源：CNBC；發布時間：Thu, 24 Sep 2026 09:36:19 GMT；台北時間：2026-09-24 17:36
  - 摘要：U.S. Treasury yields continued their upward momentum after hitting a 19-year high on Wednesday.
  - 原文連結：https://www.cnbc.com/2026/09/24/us-treasury-yields-bonds-fed-inflation.html
- 事件11：New York Fed’s Williams says it's 'reasonable' to expect another rate hike by year-end
  - 來源：CNBC；發布時間：Thu, 24 Sep 2026 09:06:18 GMT；台北時間：2026-09-24 17:06
  - 摘要：John Williams was speaking at the London Macro Policy Forum on Thursday.
  - 原文連結：https://www.cnbc.com/2026/09/24/feds-williams-another-rate-hike-by-year-end.html
- 事件12：Historic day for global bonds as 10-year Treasury and JGB yields hit highest in decades
  - 來源：CNBC；發布時間：Thu, 24 Sep 2026 04:06:54 GMT；台北時間：2026-09-24 12:06
  - 摘要：Japanese 10-year government bond yield rose to a 30-year high on Thursday, following a surge in Treasury yields.
  - 原文連結：https://www.cnbc.com/2026/09/24/japan-jgb-bond-yield-treasurys.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-24

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,850 | TAIFEX Proxy |
| 最高價 | 48,275 | TAIFEX Proxy |
| 最低價 | 47,797 | TAIFEX Proxy |
| 收盤價 | 48,123 | TAIFEX Proxy |
| 漲跌點數 | -189 | TAIFEX Proxy |
| 漲跌幅 | -0.39 | TAIFEX Proxy |
| 成交量 | 66,143 | TAIFEX Proxy |
| 日盤高點及低點 | 48,275 / 47,797 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,400 | TAIFEX Proxy |
| 最高價 | 48,404 | TAIFEX Proxy |
| 最低價 | 47,783 | TAIFEX Proxy |
| 收盤價 | 47,909 | TAIFEX Proxy |
| 漲跌點數 | -403 | TAIFEX Proxy |
| 漲跌幅 | -0.83 | TAIFEX Proxy |
| 成交量 | 28,947 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,404 / 47,783 | TAIFEX Proxy |
| 結算價 | 48,125 | TAIFEX Proxy |
| 未平倉量 | 101,311 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,675 | TAIFEX Proxy |
| 外資空方 OI | 86,706 | TAIFEX Proxy |
| 外資多空淨 OI | -77,031 | TAIFEX Proxy |
| 投信多方 OI | 75,780 | TAIFEX Proxy |
| 投信空方 OI | 2,916 | TAIFEX Proxy |
| 投信多空淨 OI | +72,864 | TAIFEX Proxy |
| 自營商多方 OI | 3,312 | TAIFEX Proxy |
| 自營商空方 OI | 4,832 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,520 | TAIFEX Proxy |
| 三大法人合計多方 OI | 88,767 | TAIFEX Proxy |
| 三大法人合計空方 OI | 94,454 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,687 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -947 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -695 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,536 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,256 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,149 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,107 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-22→2026-09-23) | -1,776 | TAIFEX Proxy snapshots (2026-09-23) |
- 資料日期：2026-09-23 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 36,223 | TAIFEX Proxy |
| 外資日盤空單交易量 | 37,132 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -909 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 14,742 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 15,652 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -910 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -695 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -695 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,450 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +509 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +941 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -154 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -401 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -14.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -39.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,123 | TAIFEX Proxy |
| 加權指數價格 | 48,024.60 | twse-proxy |
| 台指期與加權指數價差 | +98.40 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.20 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +98.40 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -214 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,123 | 47,909 | +214 | TAIFEX Proxy |
| 成交量 | 37,196 | 28,947 | +8,249 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-106（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 36,223 | 37,132 | -909 | 14,742 | 15,652 | -910 | +1 | 9,675 | 86,706 | -77,031 | -947 | TAIFEX Proxy |
| 投信 | 125 | 820 | -695 | 0 | 0 | +0 | -695 | 75,780 | 2,916 | +72,864 | -695 | TAIFEX Proxy |
| 自營商 | 4,020 | 2,570 | +1,450 | 930 | 421 | +509 | +941 | 3,312 | 4,832 | -1,520 | +1,536 | TAIFEX Proxy |
| 三大法人合計 | 40,368 | 40,522 | -154 | 15,672 | 16,073 | -401 | +247 | 88,767 | 94,454 | -5,687 | -106 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,256 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,149 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,107 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-22→2026-09-23) | -1,776 | TAIFEX Proxy snapshots (2026-09-23) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 43.76% | TAIFEX Proxy |
| 夜盤漲跌點數 | -403 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -910 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-24 | TAIFEX Proxy |
| 到期月份／到期日 | 202609F4 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-24 19:14:13 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 90,216 | TAIFEX Proxy |
| Call 總未平倉量 OI | 31,654 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 113,949 | TAIFEX Proxy |
| Put 總未平倉量 OI | 25,184 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.79 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.26 | TAIFEX Proxy |
| Put／Call Ratio | 0.80 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-22→2026-09-23) | -5.56 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-22→2026-09-23) | -7.50 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 29,907 | TAIFEX Proxy |
| 外資 Call日賣 | 29,903 | TAIFEX Proxy |
| 外資 Call日淨 | +4 | TAIFEX Proxy |
| 外資 Put日買 | 47,563 | TAIFEX Proxy |
| 外資 Put日賣 | 46,827 | TAIFEX Proxy |
| 外資 Put日淨 | +736 | TAIFEX Proxy |
| 外資 Call夜買 | 16,065 | TAIFEX Proxy |
| 外資 Call夜賣 | 16,078 | TAIFEX Proxy |
| 外資 Call夜淨 | -13 | TAIFEX Proxy |
| 外資 Put夜買 | 13,512 | TAIFEX Proxy |
| 外資 Put夜賣 | 13,526 | TAIFEX Proxy |
| 外資 Put夜淨 | -14 | TAIFEX Proxy |
| 外資 日盤淨總量 | -732 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +17 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +750 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 26,239 | TAIFEX Proxy |
| 自營商 Call日賣 | 26,536 | TAIFEX Proxy |
| 自營商 Call日淨 | -297 | TAIFEX Proxy |
| 自營商 Put日買 | 38,901 | TAIFEX Proxy |
| 自營商 Put日賣 | 38,840 | TAIFEX Proxy |
| 自營商 Put日淨 | +61 | TAIFEX Proxy |
| 自營商 Call夜買 | 8,442 | TAIFEX Proxy |
| 自營商 Call夜賣 | 10,919 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,477 | TAIFEX Proxy |
| 自營商 Put夜買 | 10,753 | TAIFEX Proxy |
| 自營商 Put夜賣 | 8,882 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,871 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -358 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +2,180 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,810 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 51,900 | 2,455 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,500 | 2,149 | TAIFEX Proxy |
| Call OI 第3大履約價 | 51,000 | 1,774 | TAIFEX Proxy |
| Call OI 最大履約價 | 51,900 | 2,455 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 51,900 | 2,455 | 7.76% | TAIFEX Proxy |
| C2 | 50,500 | 2,149 | 6.79% | TAIFEX Proxy |
| C3 | 51,000 | 1,774 | 5.6% | TAIFEX Proxy |
| C4 | 49,000 | 1,351 | 4.27% | TAIFEX Proxy |
| C5 | 50,000 | 1,146 | 3.62% | TAIFEX Proxy |
| C6 | 51,500 | 1,110 | 3.51% | TAIFEX Proxy |
| C7 | 49,500 | 995 | 3.14% | TAIFEX Proxy |
| C8 | 50,300 | 909 | 2.87% | TAIFEX Proxy |
| C9 | 49,400 | 891 | 2.81% | TAIFEX Proxy |
| C10 | 48,500 | 842 | 2.66% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 47,800 | 1,832 | TAIFEX Proxy |
| Put OI 第2大履約價 | 43,000 | 1,552 | TAIFEX Proxy |
| Put OI 第3大履約價 | 47,700 | 1,333 | TAIFEX Proxy |
| Put OI 最大履約價 | 47,800 | 1,832 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 47,800 | 1,832 | 7.27% | TAIFEX Proxy |
| P2 | 43,000 | 1,552 | 6.16% | TAIFEX Proxy |
| P3 | 47,700 | 1,333 | 5.29% | TAIFEX Proxy |
| P4 | 47,000 | 1,061 | 4.21% | TAIFEX Proxy |
| P5 | 46,000 | 1,042 | 4.14% | TAIFEX Proxy |
| P6 | 41,500 | 982 | 3.9% | TAIFEX Proxy |
| P7 | 46,500 | 822 | 3.26% | TAIFEX Proxy |
| P8 | 44,800 | 677 | 2.69% | TAIFEX Proxy |
| P9 | 46,900 | 663 | 2.63% | TAIFEX Proxy |
| P10 | 47,500 | 660 | 2.62% | TAIFEX Proxy |


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
| Call Wall 價位 | 51,900 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 47,800 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,300.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 資料日期 | 2026-09-23 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,621.40 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 資料日期 | 2026-09-23 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,700 | TAIFEX Proxy |
| 對應到期月份 | 202609F4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 76,734 | 77,466 | -732 | 29,591 | 29,590 | +1 | -733 | TAIFEX Proxy |
| 投信 | 0 | 650 | -650 | 0 | 0 | +0 | -650 | TAIFEX Proxy |
| 自營商 | 65,079 | 65,437 | -358 | 17,324 | 21,672 | -4,348 | +3,990 | TAIFEX Proxy |
| 三大法人合計 | 141,813 | 143,553 | -1,740 | 46,915 | 51,262 | -4,347 | +2,607 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 7.69 | 7.67 | +0.02 | 2.99 | 2.99 | +0.00 | +0.02 | TAIFEX Proxy |
| 投信 | 0.00 | 0.44 | -0.44 | 0.00 | 0.00 | +0 | -0.44 | TAIFEX Proxy |
| 自營商 | 5.86 | 6.13 | -0.28 | 1.62 | 2.33 | -0.71 | +0.43 | TAIFEX Proxy |
| 三大法人合計 | 13.55 | 14.24 | -0.70 | 4.61 | 5.32 | -0.70 | +0.01 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,021 | TAIFEX Proxy |
| 買權空方 OI | 10,428 | TAIFEX Proxy |
| 買權多空淨 OI | +1,593 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-22→2026-09-23) | +187 | TAIFEX Proxy snapshots (2026-09-23) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,245 | TAIFEX Proxy |
| 賣權空方 OI | 8,111 | TAIFEX Proxy |
| 賣權多空淨 OI | -866 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-22→2026-09-23) | +107 | TAIFEX Proxy snapshots (2026-09-23) |
- 資料日期：買權 2026-09-23／賣權 2026-09-23 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,776 | 2026-09-22→2026-09-23 | TAIFEX Proxy snapshots (2026-09-23) |
| 買權前十大 | +187 | 2026-09-22→2026-09-23 | TAIFEX Proxy snapshots (2026-09-23) |
| 賣權前十大 | +107 | 2026-09-22→2026-09-23 | TAIFEX Proxy snapshots (2026-09-23) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-24；資料時間：2026-09-24 19:14:13；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (6)：margin.fin_yi, margin.fin_chg_yi, margin.ratio, sbl.sale_bal, sbl.sale_chg, options.chain_oi_change
- 註記：Gamma 資料日期 2026-09-23 (T0 2026-09-24 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-09-23 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo / 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (wantgoo+istock 均失敗；官方無每日序列)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -338.0 | -77,031 | -909 | -910 | -732 | +1 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -114.1 | +72,864 | -695 | +0 | -650 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +13.4 | -1,520 | +1,450 | +509 | -358 | -4,348 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
