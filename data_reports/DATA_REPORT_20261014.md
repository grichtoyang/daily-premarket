# DATA_REPORT_20261014

- 報告日期：`2026-10-14`
- T0 交易日期：`2026-10-14`
- 資料產出時間：`2026-10-14 23:45:25`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,625.83 | 點 | twse-proxy |
| 開盤 | 48,382.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,059.12 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,382.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,625.83 | 點 | twse-proxy |
| 漲跌點數 | 284.52 | 點 | twse-proxy |
| 漲跌幅 | +0.59 | % | twse-proxy |
| 成交金額 | 9,781.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 741 | twse-proxy |
| 下跌家數 | 240 | twse-proxy |
| 平盤家數 | 99 | twse-proxy |
| 漲停家數 | 26 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 557 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 222 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 89 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 23 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 3 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -200.4 | 億元 | twse-proxy /institutional |
| 投信 | +160.3 | 億元 | twse-proxy /institutional |
| 自營商 | -114.7 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -154.8 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,771.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +89.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 264,010 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 2,883 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 189.94 | % | 前值遞補 (DATA 2026-10-13；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,510,214 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 35,357 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -311 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,781.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,277.1 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,058.5 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,731.61 | -73.84 | -0.95 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,843.48 | -360.90 | -1.33 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,116.06 | -453.42 | -1.48 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,574.66 | -95.44 | -0.18 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,803.74 | -405.05 | -3.32 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.93 | 0.66 | +4.32 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 67,777.52 | -1,253.40 | -1.82 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,035.35 | -348.89 | -5.46 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,314.17 | -31.05 | -0.13 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,767.23 | -33.64 | -0.89 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,110.59 | -243.11 | -1.97 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,790.25 | -65.50 | -0.83 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,385.75 | -405.75 | -1.32 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,908.00 | -27.00 | -0.05 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,756.30 | -43.80 | -1.56 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.79 | -0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.25 | 0.03 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.57 | 0.01 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.16 | 0.23 | +0.73 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.88 | 0.70 | +0.69 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.68 | 0.16 | +0.10 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.24 | 8.11 | +0.61 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 433.89 | -11.23 | -2.52 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 21.71 | -0.68 | -3.04 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 44.89 | -2.71 | -5.69 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 94.95 | 0.81 | +0.86 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,111.40 | -65.90 | -1.58 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,639.58 | -1,455.55 | -1.75 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股反攻卻遇神山殺尾盤 南亞、國巨帶隊吸金
  - 來源：Yahoo 台股；發布時間：2026-10-14T09:03:43Z；台北時間：2026-10-14 17:03
  - 摘要：塑化、電子題材撐場，台股反彈284點仍未站回4萬9！今(14)日加權指數終場上漲284.52點、漲幅0.59%，收48,625.83點，成交金額9302.50億元。盤中一度強彈逾700點、重返49K，尾盤賣壓使漲幅收斂；櫃買指數上漲1.40
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%A5%9E%E5%B1%B1%E5%B0%BE%E7%9B%A4%E9%81%AD%E6%8F%90%E6%AC%BE200%E5%84%84%E5%8F%B0%E8%82%A1%E4%BB%8D%E6%BC%B2284%E9%BB%9E%EF%BC%81%E5%8D%97%E4%BA%9E%E7%8B%82%E9%A3%86%E5%A5%AA%E5%90%B8%E9%87%91%E7%8E%8B-%E5%9C%8B%E5%B7%A8%E9%A0%98%E8%A2%AB%E5%8B%95%E5%85%83%E4%BB%B6%E6%90%B6%E9%8B%92%E9%A0%AD%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090343717.html
- 事件2：0056盤中飆新高股民嗨翻 前兩大持股成助攻關鍵
  - 來源：Yahoo 台股；發布時間：2026-10-14T10:19:00Z；台北時間：2026-10-14 18:19
  - 摘要：元大高股息（0056）盤中衝上59.7元刷新歷史新高，吸引168萬名股東關注。受惠持股南亞搭上AI轉型浪潮股價強勢，以及華南金亮眼獲利推升，0056展現強勁爆發力，近三個月績效達15.3%。加上本季祭出創高配息，推升市場買氣，引發網友熱烈討
  - 原文連結：https://tw.stock.yahoo.com/news/168%E8%90%AC%E8%82%A1%E6%9D%B1%E7%88%BD%E7%BF%BB-0056%E5%88%B7%E6%96%B0%E9%AB%98%E7%8B%82%E5%8B%9D%E5%A4%A7%E7%9B%A4-%E6%8E%A8%E6%89%8B%E6%98%AF%E9%80%992%E6%AA%94-101900591.html
- 事件3：晶心科一張價差逾12萬 特力屋和暢16日同步申購
  - 來源：Yahoo 台股；發布時間：2026-10-14T09:07:50Z；台北時間：2026-10-14 17:07
  - 摘要：新的一輪台股紅包抽籤接力登場！本周共有晶心科（6533）、和暢科技（6825）等 3 檔即將開放申購，若再加上目前正在申購中的股票，累計已有6檔可試手氣。其中，最受矚目的晶心科若幸運抽中一張，潛在獲利預計高達12萬元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%8A%BD%E4%B8%AD1%E5%BC%B5%E7%88%BD%E8%B3%BA12%E8%90%AC%EF%BC%81%E7%89%B9%E5%8A%9B%E5%B1%8B%E3%80%81%E6%99%B6%E5%BF%83%E7%A7%91%E7%AD%893%E6%AA%94%E5%8F%B0%E8%82%A1%E7%B4%85%E5%8C%85%E7%94%B3%E8%B3%BC%E5%80%92%E6%95%B8%E4%B8%AD-090750172.html
- 事件4：高息ETF不是只會配息 3檔今年跑贏大盤冠軍漲近8成
  - 來源：Yahoo 台股；發布時間：2026-10-14T10:24:00Z；台北時間：2026-10-14 18:24
  - 摘要：高股息ETF今年也有亮眼表現！股添樂分析，00929、00939、00878今年以來漲幅超越大盤，00918、00929等ETF年化配息率也受關注。0056、00878、00919如何比較？投資人應留意總報酬與配息風險。（記者唐家興）
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%AB%98%E8%82%A1%E6%81%AFetf%E4%BB%8A%E5%B9%B4%E8%AA%B0%E6%9C%80%E8%B3%BA-%E8%A1%A8%E7%9C%8B%E6%87%82-3%E6%AA%94%E8%B3%BA%E8%B4%8F%E5%A4%A7%E7%9B%A4-%E7%AC%AC1%E5%90%8D%E7%8C%9B%E6%BC%B2%E8%BF%918%E6%88%90-100400095.html
- 事件5：美債殖利率衝高股市也震盪 利率匯率風險一次看懂
  - 來源：Yahoo 台股；發布時間：2026-10-13T10:00:00Z；台北時間：2026-10-13 18:00
  - 摘要：美債是市場判斷經濟前景與走向的重要參考指標，近來，美國10年、20年、30年公債殖利率接連觸及24年來高點，牽動全球金融市場震盪。市場看法眾說紛紜，有人擔憂美債殖利率會持續高漲，也有人認為會有回落空間。美債究竟是什麼？美債殖利率又是怎麼算出
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E5%82%B5%E6%AE%96%E5%88%A9%E7%8E%87%E5%89%B520%E5%A4%9A%E5%B9%B4%E4%BE%86%E6%96%B0%E9%AB%98%E2%8B%AF%E7%BE%8E%E8%82%A1%E3%80%81%E5%8F%B0%E8%82%A1%E9%83%BD%E5%8F%97%E5%BD%B1%E9%9F%BF%EF%BC%81%E7%BE%8E%E5%82%B5%E6%AE%96%E5%88%A9%E7%8E%87%E6%80%8E%E9%BA%BC%E7%AE%97%EF%BC%9F%E5%B9%BE%E4%B9%8E%E6%B2%92%E6%9C%89%E4%BF%A1%E7%94%A8%E9%A2%A8%E9%9A%AA%E4%B8%8D%E7%AD%89%E6%96%BC%E6%B2%92%E6%9C%89%E9%A2%A8%E9%9A%AA%EF%BC%9F%EF%BD%9C%E7%9C%8B%E5%9C%96%E8%AA%AA%E8%82%A1%E5%B8%82-100000569.html
- 事件6：光通訊股回神強彈！「這封測廠」亮燈連收6紅飆55%、華星光、眾達都漲停　聯亞、聯鈞噴逾半根、立碁漲7%
  - 來源：Yahoo 台股；發布時間：2026-10-14T09:50:00Z；台北時間：2026-10-14 17:50
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導台股加權指數今（14）日開高走高，盤中一度站回4萬9大關，奈何漲幅收斂，終場收在48625.83點，上漲284.52點，漲幅0.59%，成...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%89%E9%80%9A%E8%A8%8A%E8%82%A1%E5%9B%9E%E7%A5%9E%E5%BC%B7%E5%BD%88-%E9%80%99%E5%B0%81%E6%B8%AC%E5%BB%A0-%E4%BA%AE%E7%87%88%E9%80%A3%E6%94%B66%E7%B4%85%E9%A3%8655-%E8%8F%AF%E6%98%9F%E5%85%89-%E7%9C%BE%E9%81%94%E9%83%BD%E6%BC%B2%E5%81%9C-095000673.html
- 事件7：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into the economic condition of American families
  - 來源：Federal Reserve；發布時間：Fri, 9 Oct 2026 14:00:00 GMT；台北時間：2026-10-09 22:00
  - 摘要：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261009a.htm
- 事件8：Federal Reserve Board announces enforcement action against American Express Company to address, among other things, the firmâs failure to sufficiently detect and report certain suspicious activity related to money laundering
  - 來源：Federal Reserve；發布時間：Thu, 8 Oct 2026 20:30:00 GMT；台北時間：2026-10-09 04:30
  - 摘要：Federal Reserve Board announces enforcement action against American Express Company to address, among other things, the firmâs failure to sufficient
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261008a.htm
- 事件9：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 來源：Federal Reserve；發布時間：Wed, 7 Oct 2026 18:00:00 GMT；台北時間：2026-10-08 02:00
  - 摘要：Minutes of the Federal Open Market Committee, September 15-16, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261007a.htm
- 事件10：Here's the inflation breakdown for September 2026 — in one chart
  - 來源：CNBC；發布時間：Wed, 14 Oct 2026 14:56:25 GMT；台北時間：2026-10-14 22:56
  - 摘要：The consumer price index rose by 3.7% in September, on the back of higher gasoline and energy prices largely due to the Iran war.
  - 原文連結：https://www.cnbc.com/2026/10/14/cpi-inflation-breakdown-september-2026.html
- 事件11：BlackRock's Larry Fink warns a data center moratorium could trigger a recession
  - 來源：CNBC；發布時間：Wed, 14 Oct 2026 15:19:08 GMT；台北時間：2026-10-14 23:19
  - 摘要：Local opposition to data center construction has been a feature of the midterm elections set for Tuesday, Nov. 3.
  - 原文連結：https://www.cnbc.com/2026/10/14/blackrocks-fink-warns-data-center-moratorium-could-spark-a-recession.html
- 事件12：10-year Treasury yield jumps as September core inflation comes in hotter than expected
  - 來源：CNBC；發布時間：Wed, 14 Oct 2026 13:48:01 GMT；台北時間：2026-10-14 21:48
  - 摘要：Treasury yields moved higher after the latest inflation reading.
  - 原文連結：https://www.cnbc.com/2026/10/14/us-treasury-yields-cpi-inflation-report.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-14

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,789 | TAIFEX Proxy |
| 最高價 | 49,200 | TAIFEX Proxy |
| 最低價 | 48,650 | TAIFEX Proxy |
| 收盤價 | 48,792 | TAIFEX Proxy |
| 漲跌點數 | +400 | TAIFEX Proxy |
| 漲跌幅 | +0.83 | TAIFEX Proxy |
| 成交量 | 66,408 | TAIFEX Proxy |
| 日盤高點及低點 | 49,200 / 48,650 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,433 | TAIFEX Proxy |
| 最高價 | 48,873 | TAIFEX Proxy |
| 最低價 | 48,357 | TAIFEX Proxy |
| 收盤價 | 48,755 | TAIFEX Proxy |
| 漲跌點數 | +363 | TAIFEX Proxy |
| 漲跌幅 | +0.75 | TAIFEX Proxy |
| 成交量 | 21,801 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,873 / 48,357 | TAIFEX Proxy |
| 結算價 | 48,798 | TAIFEX Proxy |
| 未平倉量 | 105,601 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,352 | TAIFEX Proxy |
| 外資空方 OI | 98,166 | TAIFEX Proxy |
| 外資多空淨 OI | -86,814 | TAIFEX Proxy |
| 投信多方 OI | 81,091 | TAIFEX Proxy |
| 投信空方 OI | 2,674 | TAIFEX Proxy |
| 投信多空淨 OI | +78,417 | TAIFEX Proxy |
| 自營商多方 OI | 6,449 | TAIFEX Proxy |
| 自營商空方 OI | 4,135 | TAIFEX Proxy |
| 自營商多空淨 OI | +2,314 | TAIFEX Proxy |
| 三大法人合計多方 OI | 98,892 | TAIFEX Proxy |
| 三大法人合計空方 OI | 104,975 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -6,083 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +425 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +579 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +823 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 81,651 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,535 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,116 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-12→2026-10-13) | -1,737 | TAIFEX Proxy snapshots (2026-10-13) |
- 資料日期：2026-10-13 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 39,351 | TAIFEX Proxy |
| 外資日盤空單交易量 | 38,613 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +738 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 11,928 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 10,784 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,144 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -406 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +579 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +579 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +896 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -234 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,130 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,213 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +910 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +216.5 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +88.9 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,792 | TAIFEX Proxy |
| 加權指數價格 | 48,625.83 | twse-proxy |
| 台指期與加權指數價差 | +166.17 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.34 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +166.17 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -37 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,792 | 48,755 | +37 | TAIFEX Proxy |
| 成交量 | 44,607 | 21,801 | +22,806 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,827（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 39,351 | 38,613 | +738 | 11,928 | 10,784 | +1,144 | -406 | 11,352 | 98,166 | -86,814 | +425 | TAIFEX Proxy |
| 投信 | 1,339 | 760 | +579 | 0 | 0 | +0 | +579 | 81,091 | 2,674 | +78,417 | +579 | TAIFEX Proxy |
| 自營商 | 5,972 | 5,076 | +896 | 1,282 | 1,516 | -234 | +1,130 | 6,449 | 4,135 | +2,314 | +823 | TAIFEX Proxy |
| 三大法人合計 | 46,662 | 44,449 | +2,213 | 13,210 | 12,300 | +910 | +1,303 | 98,892 | 104,975 | -6,083 | +1,827 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 81,651 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,535 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,116 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-12→2026-10-13) | -1,737 | TAIFEX Proxy snapshots (2026-10-13) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 32.83% | TAIFEX Proxy |
| 夜盤漲跌點數 | +363 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,144 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-14 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-14 23:45:25 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 295,053 | TAIFEX Proxy |
| Call 總未平倉量 OI | 70,030 | TAIFEX Proxy |
| Call OI 增減 (2026-10-13→2026-10-14) | +10,435 | TAIFEX Proxy snapshots (2026-10-13) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 308,377 | TAIFEX Proxy |
| Put 總未平倉量 OI | 65,057 | TAIFEX Proxy |
| Put OI 增減 (2026-10-13→2026-10-14) | +29,583 | TAIFEX Proxy snapshots (2026-10-13) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.96 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.08 | TAIFEX Proxy |
| Put／Call Ratio | 0.93 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-12→2026-10-13) | -13.59 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-12→2026-10-13) | -15.83 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 100,608 | TAIFEX Proxy |
| 外資 Call日賣 | 105,616 | TAIFEX Proxy |
| 外資 Call日淨 | -5,008 | TAIFEX Proxy |
| 外資 Put日買 | 103,663 | TAIFEX Proxy |
| 外資 Put日賣 | 105,113 | TAIFEX Proxy |
| 外資 Put日淨 | -1,450 | TAIFEX Proxy |
| 外資 Call夜買 | 31,873 | TAIFEX Proxy |
| 外資 Call夜賣 | 31,834 | TAIFEX Proxy |
| 外資 Call夜淨 | +39 | TAIFEX Proxy |
| 外資 Put夜買 | 37,968 | TAIFEX Proxy |
| 外資 Put夜賣 | 38,043 | TAIFEX Proxy |
| 外資 Put夜淨 | -75 | TAIFEX Proxy |
| 外資 日盤淨總量 | -3,558 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -5,047 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -1,375 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 74,050 | TAIFEX Proxy |
| 自營商 Call日賣 | 71,213 | TAIFEX Proxy |
| 自營商 Call日淨 | +2,837 | TAIFEX Proxy |
| 自營商 Put日買 | 79,476 | TAIFEX Proxy |
| 自營商 Put日賣 | 86,989 | TAIFEX Proxy |
| 自營商 Put日淨 | -7,513 | TAIFEX Proxy |
| 自營商 Call夜買 | 20,496 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,432 | TAIFEX Proxy |
| 自營商 Call夜淨 | +3,064 | TAIFEX Proxy |
| 自營商 Put夜買 | 20,295 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,627 | TAIFEX Proxy |
| 自營商 Put夜淨 | -332 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +10,350 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -227 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -7,181 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,000 | 5,775 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,900 | 4,516 | TAIFEX Proxy |
| Call OI 第3大履約價 | 50,500 | 3,826 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,000 | 5,775 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,000 | 5,775 | 8.25% | TAIFEX Proxy |
| C2 | 48,900 | 4,516 | 6.45% | TAIFEX Proxy |
| C3 | 50,500 | 3,826 | 5.46% | TAIFEX Proxy |
| C4 | 48,950 | 3,504 | 5.0% | TAIFEX Proxy |
| C5 | 49,100 | 2,940 | 4.2% | TAIFEX Proxy |
| C6 | 49,300 | 2,552 | 3.64% | TAIFEX Proxy |
| C7 | 49,200 | 2,099 | 3.0% | TAIFEX Proxy |
| C8 | 50,000 | 2,032 | 2.9% | TAIFEX Proxy |
| C9 | 52,500 | 2,030 | 2.9% | TAIFEX Proxy |
| C10 | 48,850 | 1,666 | 2.38% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,800 | 4,091 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,850 | 4,066 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,000 | 3,906 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,800 | 4,091 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,800 | 4,091 | 6.29% | TAIFEX Proxy |
| P2 | 48,850 | 4,066 | 6.25% | TAIFEX Proxy |
| P3 | 48,000 | 3,906 | 6.0% | TAIFEX Proxy |
| P4 | 48,500 | 3,394 | 5.22% | TAIFEX Proxy |
| P5 | 48,300 | 2,493 | 3.83% | TAIFEX Proxy |
| P6 | 48,700 | 2,465 | 3.79% | TAIFEX Proxy |
| P7 | 48,600 | 2,195 | 3.37% | TAIFEX Proxy |
| P8 | 48,200 | 2,131 | 3.28% | TAIFEX Proxy |
| P9 | 48,900 | 2,071 | 3.18% | TAIFEX Proxy |
| P10 | 48,400 | 1,979 | 3.04% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,950 (+3,142) | TAIFEX Proxy snapshots (2026-10-13) |
| Call OI 減少最多的履約價 | 48,500 (-980) | TAIFEX Proxy snapshots (2026-10-13) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 48,850 (+3,938) | TAIFEX Proxy snapshots (2026-10-13) |
| Put OI 減少最多的履約價 | 46,400 (-238) | TAIFEX Proxy snapshots (2026-10-13) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-13→2026-10-14) | -1,500 | TAIFEX Proxy snapshots (2026-10-13) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,800 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-13→2026-10-14) | +800 | TAIFEX Proxy snapshots (2026-10-13) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,600.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 資料日期 | 2026-10-13 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,129.71 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 資料日期 | 2026-10-13 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,800 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-13→2026-10-14) | +350 | TAIFEX Proxy snapshots (2026-10-13) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 205,721 | 209,279 | -3,558 | 69,916 | 69,802 | +114 | -3,672 | TAIFEX Proxy |
| 投信 | 0 | 2,540 | -2,540 | 0 | 0 | +0 | -2,540 | TAIFEX Proxy |
| 自營商 | 161,039 | 150,689 | +10,350 | 41,123 | 37,727 | +3,396 | +6,954 | TAIFEX Proxy |
| 三大法人合計 | 366,760 | 362,508 | +4,252 | 111,039 | 107,529 | +3,510 | +742 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.74 | 9.38 | +0.36 | 4.59 | 4.55 | +0.04 | +0.32 | TAIFEX Proxy |
| 投信 | 0.00 | 1.69 | -1.69 | 0.00 | 0.00 | +0 | -1.69 | TAIFEX Proxy |
| 自營商 | 9.68 | 7.83 | +1.84 | 2.59 | 2.30 | +0.29 | +1.55 | TAIFEX Proxy |
| 三大法人合計 | 19.42 | 18.90 | +0.52 | 7.19 | 6.85 | +0.33 | +0.18 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 17,620 | TAIFEX Proxy |
| 買權空方 OI | 16,704 | TAIFEX Proxy |
| 買權多空淨 OI | +916 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-12→2026-10-13) | -299 | TAIFEX Proxy snapshots (2026-10-13) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,608 | TAIFEX Proxy |
| 賣權空方 OI | 10,282 | TAIFEX Proxy |
| 賣權多空淨 OI | +326 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-12→2026-10-13) | +332 | TAIFEX Proxy snapshots (2026-10-13) |
- 資料日期：買權 2026-10-13／賣權 2026-10-13 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,737 | 2026-10-12→2026-10-13 | TAIFEX Proxy snapshots (2026-10-13) |
| 買權前十大 | -299 | 2026-10-12→2026-10-13 | TAIFEX Proxy snapshots (2026-10-13) |
| 賣權前十大 | +332 | 2026-10-12→2026-10-13 | TAIFEX Proxy snapshots (2026-10-13) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-14；資料時間：2026-10-14 23:45:25；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
- 註記：Gamma 資料日期 2026-10-13 (T0 2026-10-14 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-13 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-10-13；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-13)，非 T0 2026-10-14
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -200.4 | -86,814 | +738 | +1,144 | -3,558 | +114 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +160.3 | +78,417 | +579 | +0 | -2,540 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -114.7 | +2,314 | +896 | -234 | +10,350 | +3,396 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
