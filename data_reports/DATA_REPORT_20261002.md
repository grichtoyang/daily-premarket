# DATA_REPORT_20261002

- 報告日期：`2026-10-05`
- T0 交易日期：`2026-10-02`
- 資料產出時間：`2026-10-05 08:08:32`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,475.74 | 點 | twse-proxy |
| 開盤 | 48,390.65 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,491.62 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,205.81 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,475.74 | 點 | twse-proxy |
| 漲跌點數 | 122.25 | 點 | twse-proxy |
| 漲跌幅 | +0.25 | % | twse-proxy |
| 成交金額 | 9,382.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 483 | twse-proxy |
| 下跌家數 | 506 | twse-proxy |
| 平盤家數 | 91 | twse-proxy |
| 漲停家數 | 24 | twse-proxy |
| 跌停家數 | 1 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 452 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 331 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 85 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 31 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +26.2 | 億元 | twse-proxy /institutional |
| 投信 | +57.7 | 億元 | twse-proxy /institutional |
| 自營商 | +20.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +104.2 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,566.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +79.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 269,762 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -22 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 195.13 | % | 前值遞補 (DATA 2026-10-01；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,087,838 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,776 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 1,314 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,382.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,731.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,114.1 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,722.72 | 56.27 | +0.73 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,190.86 | 319.26 | +1.19 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,807.93 | 306.37 | +1.00 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,176.96 | 250.40 | +0.49 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 13,136.67 | 307.67 | +2.40 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.31 | -1.08 | -6.59 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 68,309.46 | -647.26 | -0.94 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,003.74 | 32.39 | +0.46 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,972.29 | -640.98 | -2.60 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,784.25 | 7.00 | +0.09 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 31,129.50 | 67.75 | +0.22 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,517.00 | 40.00 | +0.08 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,855.10 | 4.20 | +0.15 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.28 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.63 | 0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.83 | -0.05 | -0.16 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.90 | -0.03 | -0.03 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.64 | -0.29 | -0.18 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.82 | -17.77 | -1.31 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 472.78 | 13.58 | +2.96 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 26.27 | 1.06 | +4.20 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.45 | 2.72 | +6.08 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 90.83 | -0.28 | -0.31 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,170.80 | 8.50 | +0.20 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 86,414.57 | 1,650.99 | +1.95 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股「雙龍頭」法說會 一文掌握一週財經重點
  - 來源：Yahoo 台股；發布時間：2026-10-04T04:47:20Z；台北時間：2026-10-04 12:47
  - 摘要：本周【投資早知道】聚焦在台股首檔中小股本主動ETF！台新00416A 10月5日開募；雙龍頭法說行情！台達電大立光接連登場；中國大陸股市復市！外匯儲備信貸數據同步公布 牽動港股與新興市場走向；以及中油宣布油價凍漲！政府補貼累計突破253億。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%A6%96%E6%AA%94%E4%B8%AD%E5%B0%8F%E8%82%A1%E6%9C%AC%E4%B8%BB%E5%8B%95etf%E9%96%8B%E5%8B%9F-%E9%9B%99%E9%BE%8D%E9%A0%AD%E6%B3%95%E8%AA%AA%E8%A1%8C%E6%83%85%EF%BC%81%E5%8F%B0%E9%81%94%E9%9B%BB%E5%A4%A7%E7%AB%8B%E5%85%89%E6%8E%A5%E9%80%A3%E7%99%BB%E5%A0%B4-%E4%B8%AD%E5%9C%8B%E5%A4%A7%E9%99%B8%E8%82%A1%E5%B8%82%E5%BE%A9%E5%B8%82%EF%BC%81%E5%A4%96%E5%8C%AF%E5%84%B2%E5%82%99%E4%BF%A1%E8%B2%B8%E6%95%B8%E6%93%9A%E5%90%8C%E6%AD%A5%E5%85%AC%E5%B8%83-%E7%89%BD%E5%8B%95%E6%B8%AF%E8%82%A1%E8%88%87%E6%96%B0%E8%88%88%E5%B8%82%E5%A0%B4%E8%B5%B0%E5%90%91-%E4%B8%AD%E6%B2%B9%E5%AE%A3%E5%B8%83%E6%B2%B9%E5%83%B9%E5%87%8D%E6%BC%B2%EF%BD%9C%E6%8A%95%E8%B3%87%E6%97%A9%E7%9F%A5%E9%81%93-044720123.html
- 事件2：婚假14日新制上路！竹縣提醒30人以上企業盡速修正工作規則
  - 來源：Yahoo 台股；發布時間：2026-10-05T00:00:46Z；台北時間：2026-10-05 08:00
  - 摘要：【互傳媒／記者 宋旭志／新竹 報導】婚假14日新制10月1日正式上路!為保障勞工權益並協助企業落實最新勞動法令
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A9%9A%E5%81%8714%E6%97%A5%E6%96%B0%E5%88%B6%E4%B8%8A%E8%B7%AF-%E7%AB%B9%E7%B8%A3%E6%8F%90%E9%86%9230%E4%BA%BA%E4%BB%A5%E4%B8%8A%E4%BC%81%E6%A5%AD%E7%9B%A1%E9%80%9F%E4%BF%AE%E6%AD%A3%E5%B7%A5%E4%BD%9C%E8%A6%8F%E5%89%87-000046871.html
- 事件3：PCB股太熱遭盯上！「這檔」6日狂飆39%、尖點本益比衝111倍　23檔入列注意股名單
  - 來源：Yahoo 台股；發布時間：2026-10-05T00:00:00Z；台北時間：2026-10-05 08:00
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導台股加權指數週五（2日）終場收48,475.74點，上漲122.25點或0.25%，成交金額達8997.1億元，證交所公布23檔注意股，PCB供應...
  - 原文連結：https://tw.stock.yahoo.com/news/pcb%E8%82%A1%E5%A4%AA%E7%86%B1%E9%81%AD%E7%9B%AF%E4%B8%8A-%E9%80%99%E6%AA%94-6%E6%97%A5%E7%8B%82%E9%A3%8639-%E5%B0%96%E9%BB%9E%E6%9C%AC%E7%9B%8A%E6%AF%94%E8%A1%9D111%E5%80%8D-23%E6%AA%94%E5%85%A5%E5%88%97%E6%B3%A8%E6%84%8F%E8%82%A1%E5%90%8D%E5%96%AE-000000092.html
- 事件4：四貸同堂｜房貸、增貸、信貸再加股票質借　10月底銀行券商開始跨業查信用
  - 來源：Yahoo 台股；發布時間：2026-10-04T23:45:00Z；台北時間：2026-10-05 07:45
  - 摘要：金管會已經宣布，銀行與券商的跨業信用查詢機制預計在2026年10月底上線。

簡單來說，以前銀行主要看銀行這一端的借款，券商主要掌握證券端的融資。新制度上線後，在取得客戶同意的情況下，雙方可以增加掌握另一端的借款資訊。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9B%9B%E8%B2%B8%E5%90%8C%E5%A0%82%EF%BD%9C%E6%88%BF%E8%B2%B8%E3%80%81%E5%A2%9E%E8%B2%B8%E3%80%81%E4%BF%A1%E8%B2%B8%E5%86%8D%E5%8A%A0%E8%82%A1%E7%A5%A8%E8%B3%AA%E5%80%9F-10%E6%9C%88%E5%BA%95%E9%8A%80%E8%A1%8C%E5%88%B8%E5%95%86%E9%96%8B%E5%A7%8B%E8%B7%A8%E6%A5%AD%E6%9F%A5%E4%BF%A1%E7%94%A8-234500001.html
- 事件5：PCB同步勁揚！「這檔」飆連7漲37.7%創高　欣興、景碩也收連3紅寫新天價
  - 來源：Yahoo 台股；發布時間：2026-10-04T23:45:00Z；台北時間：2026-10-05 07:45
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導PCB中的載板族群上週股價表現亮眼，南電（8046）週五（2）飆出連7漲37.74%的好成績，收在1460元，創歷史新高，欣興（3037）...
  - 原文連結：https://tw.stock.yahoo.com/news/pcb%E5%90%8C%E6%AD%A5%E5%8B%81%E6%8F%9A-%E9%80%99%E6%AA%94-%E9%A3%86%E9%80%A37%E6%BC%B237-7-%E5%89%B5%E9%AB%98-234500251.html
- 事件6：與152萬股民作對！外資9月暴賣0050撤資207億元　00919共4檔高息ETF同挨刀砍出破17萬張
  - 來源：Yahoo 台股；發布時間：2026-10-04T23:30:00Z；台北時間：2026-10-05 07:30
  - 摘要：[FTNN新聞網]記者薛明峻／台北報導台股9月一度衝上48601.53點寫歷史新高，加權指數9月30日收在47940.13點，月線狂漲1811.66點，漲幅達3.93%。根據證交所公布...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%88%87152%E8%90%AC%E8%82%A1%E6%B0%91%E4%BD%9C%E5%B0%8D-%E5%A4%96%E8%B3%879%E6%9C%88%E6%9A%B4%E8%B3%A30050%E6%92%A4%E8%B3%87207%E5%84%84%E5%85%83-00919%E5%85%B14%E6%AA%94%E9%AB%98%E6%81%AFetf%E5%90%8C%E6%8C%A8%E5%88%80%E7%A0%8D%E5%87%BA%E7%A0%B417%E8%90%AC%E5%BC%B5-233000117.html
- 事件7：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:45:00 GMT；台北時間：2026-10-03 04:45
  - 摘要：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261002a.htm
- 事件8：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:00:00 GMT；台北時間：2026-10-03 04:00
  - 摘要：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261002a.htm
- 事件9：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 15:00:00 GMT；台北時間：2026-10-02 23:00
  - 摘要：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261002a.htm
- 事件10：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress test-related capital requirements
  - 來源：Federal Reserve；發布時間：Wed, 30 Sep 2026 13:00:00 GMT；台北時間：2026-09-30 21:00
  - 摘要：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress t
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm
- 事件11：Treasury Sec. Bessent, IRS crack down on ETF strategy the wealthy are using to avoid capital gains taxes
  - 來源：CNBC；發布時間：Fri, 02 Oct 2026 13:48:40 GMT；台北時間：2026-10-02 21:48
  - 摘要：The IRS and Treasury issued a warning this week on an ETF strategy wealthy investors have been using to shield capital gains income from taxes.
  - 原文連結：https://www.cnbc.com/2026/10/02/treasury-irs-capital-gains-income-tax-section-351-warning.html
- 事件12：Fed minutes coming this week could give markets important clues about future rate hikes
  - 來源：MarketWatch；發布時間：Sun, 04 Oct 2026 12:00:00 GMT；台北時間：2026-10-04 20:00
  - 摘要：Minutes from the September meeting may provide extra context, as the real fed-funds rate is now surprisingly low.
  - 原文連結：https://www.marketwatch.com/story/fed-minutes-coming-this-week-could-give-markets-important-clues-about-future-rate-hikes-31bfba5b?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-02

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,552 | TAIFEX Proxy |
| 最高價 | 48,802 | TAIFEX Proxy |
| 最低價 | 48,472 | TAIFEX Proxy |
| 收盤價 | 48,671 | TAIFEX Proxy |
| 漲跌點數 | -27 | TAIFEX Proxy |
| 漲跌幅 | -0.06 | TAIFEX Proxy |
| 成交量 | 71,568 | TAIFEX Proxy |
| 日盤高點及低點 | 48,802 / 48,472 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,622 | TAIFEX Proxy |
| 最高價 | 48,661 | TAIFEX Proxy |
| 最低價 | 48,210 | TAIFEX Proxy |
| 收盤價 | 48,475 | TAIFEX Proxy |
| 漲跌點數 | -223 | TAIFEX Proxy |
| 漲跌幅 | -0.46 | TAIFEX Proxy |
| 成交量 | 37,554 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,661 / 48,210 | TAIFEX Proxy |
| 結算價 | 48,669 | TAIFEX Proxy |
| 未平倉量 | 106,691 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,893 | TAIFEX Proxy |
| 外資空方 OI | 92,197 | TAIFEX Proxy |
| 外資多空淨 OI | -80,304 | TAIFEX Proxy |
| 投信多方 OI | 77,530 | TAIFEX Proxy |
| 投信空方 OI | 2,861 | TAIFEX Proxy |
| 投信多空淨 OI | +74,669 | TAIFEX Proxy |
| 自營商多方 OI | 3,340 | TAIFEX Proxy |
| 自營商空方 OI | 4,346 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,006 | TAIFEX Proxy |
| 三大法人合計多方 OI | 92,763 | TAIFEX Proxy |
| 三大法人合計空方 OI | 99,404 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -6,641 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -750 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +54 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +434 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,719 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,942 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +3,777 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-30→2026-10-02) | -2,752 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：2026-10-02 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 39,654 | TAIFEX Proxy |
| 外資日盤空單交易量 | 40,456 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -802 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 18,921 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,325 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,596 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,398 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +54 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +54 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +428 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -779 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +1,207 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -320 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,817 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -30.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +178.3 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,671 | TAIFEX Proxy |
| 加權指數價格 | 48,475.74 | twse-proxy |
| 台指期與加權指數價差 | +195.26 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.40 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +195.26 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -196 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,671 | 48,475 | +196 | TAIFEX Proxy |
| 成交量 | 34,014 | 37,554 | -3,540 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-262（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 39,654 | 40,456 | -802 | 18,921 | 16,325 | +2,596 | -3,398 | 11,893 | 92,197 | -80,304 | -750 | TAIFEX Proxy |
| 投信 | 111 | 57 | +54 | 0 | 0 | +0 | +54 | 77,530 | 2,861 | +74,669 | +54 | TAIFEX Proxy |
| 自營商 | 3,841 | 3,413 | +428 | 548 | 1,327 | -779 | +1,207 | 3,340 | 4,346 | -1,006 | +434 | TAIFEX Proxy |
| 三大法人合計 | 43,606 | 43,926 | -320 | 19,469 | 17,652 | +1,817 | -2,137 | 92,763 | 99,404 | -6,641 | -262 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,719 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,942 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +3,777 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-30→2026-10-02) | -2,752 | TAIFEX Proxy snapshots (2026-10-01) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 52.47% | TAIFEX Proxy |
| 夜盤漲跌點數 | -223 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,596 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-02 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-05 08:08:32 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 309,089 | TAIFEX Proxy |
| Call 總未平倉量 OI | 61,225 | TAIFEX Proxy |
| Call OI 增減 (2026-10-01→2026-10-02) | +21,707 | TAIFEX Proxy snapshots (2026-10-01) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 274,213 | TAIFEX Proxy |
| Put 總未平倉量 OI | 54,441 | TAIFEX Proxy |
| Put OI 增減 (2026-10-01→2026-10-02) | +23,623 | TAIFEX Proxy snapshots (2026-10-01) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.13 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.12 | TAIFEX Proxy |
| Put／Call Ratio | 0.89 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-01→2026-10-02) | -1.95 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-01→2026-10-02) | -1.70 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 110,844 | TAIFEX Proxy |
| 外資 Call日賣 | 111,325 | TAIFEX Proxy |
| 外資 Call日淨 | -481 | TAIFEX Proxy |
| 外資 Put日買 | 100,159 | TAIFEX Proxy |
| 外資 Put日賣 | 104,402 | TAIFEX Proxy |
| 外資 Put日淨 | -4,243 | TAIFEX Proxy |
| 外資 Call夜買 | 23,312 | TAIFEX Proxy |
| 外資 Call夜賣 | 23,420 | TAIFEX Proxy |
| 外資 Call夜淨 | -108 | TAIFEX Proxy |
| 外資 Put夜買 | 20,240 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,479 | TAIFEX Proxy |
| 外資 Put夜淨 | -239 | TAIFEX Proxy |
| 外資 日盤淨總量 | +3,762 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -373 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,004 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 71,525 | TAIFEX Proxy |
| 自營商 Call日賣 | 77,521 | TAIFEX Proxy |
| 自營商 Call日淨 | -5,996 | TAIFEX Proxy |
| 自營商 Put日買 | 75,505 | TAIFEX Proxy |
| 自營商 Put日賣 | 75,627 | TAIFEX Proxy |
| 自營商 Put日淨 | -122 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,504 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,489 | TAIFEX Proxy |
| 自營商 Call夜淨 | -985 | TAIFEX Proxy |
| 自營商 Put夜買 | 15,539 | TAIFEX Proxy |
| 自營商 Put夜賣 | 17,245 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,706 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -5,874 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -5,011 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +1,584 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,500 | 6,284 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,450 | 4,895 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,600 | 3,156 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,500 | 6,284 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,500 | 6,284 | 10.26% | TAIFEX Proxy |
| C2 | 48,450 | 4,895 | 8.0% | TAIFEX Proxy |
| C3 | 48,600 | 3,156 | 5.15% | TAIFEX Proxy |
| C4 | 49,000 | 3,135 | 5.12% | TAIFEX Proxy |
| C5 | 48,800 | 2,656 | 4.34% | TAIFEX Proxy |
| C6 | 48,550 | 2,627 | 4.29% | TAIFEX Proxy |
| C7 | 48,400 | 2,207 | 3.6% | TAIFEX Proxy |
| C8 | 48,700 | 2,137 | 3.49% | TAIFEX Proxy |
| C9 | 52,000 | 1,690 | 2.76% | TAIFEX Proxy |
| C10 | 50,500 | 1,649 | 2.69% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,400 | 4,590 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,350 | 4,143 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,300 | 3,838 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,400 | 4,590 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,400 | 4,590 | 8.43% | TAIFEX Proxy |
| P2 | 48,350 | 4,143 | 7.61% | TAIFEX Proxy |
| P3 | 48,300 | 3,838 | 7.05% | TAIFEX Proxy |
| P4 | 48,000 | 3,079 | 5.66% | TAIFEX Proxy |
| P5 | 48,450 | 2,756 | 5.06% | TAIFEX Proxy |
| P6 | 47,900 | 2,537 | 4.66% | TAIFEX Proxy |
| P7 | 48,200 | 2,456 | 4.51% | TAIFEX Proxy |
| P8 | 48,100 | 1,990 | 3.66% | TAIFEX Proxy |
| P9 | 47,500 | 1,918 | 3.52% | TAIFEX Proxy |
| P10 | 47,000 | 1,835 | 3.37% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 48,500 (+4,741) | TAIFEX Proxy snapshots (2026-10-01) |
| Call OI 減少最多的履約價 | 49,500 (-230) | TAIFEX Proxy snapshots (2026-10-01) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 48,400 (+4,146) | TAIFEX Proxy snapshots (2026-10-01) |
| Put OI 減少最多的履約價 | 47,600 (-913) | TAIFEX Proxy snapshots (2026-10-01) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 48,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-02) | -500 | TAIFEX Proxy snapshots (2026-10-01) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-02) | +400 | TAIFEX Proxy snapshots (2026-10-01) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 49,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-10-02 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,062.03 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 資料日期 | 2026-10-02 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,350 | TAIFEX Proxy |
| 對應到期月份 | 202610F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-02) | +400 | TAIFEX Proxy snapshots (2026-10-01) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 215,246 | 211,484 | +3,762 | 43,791 | 43,660 | +131 | +3,631 | TAIFEX Proxy |
| 投信 | 0 | 3,100 | -3,100 | 0 | 0 | +0 | -3,100 | TAIFEX Proxy |
| 自營商 | 147,152 | 153,026 | -5,874 | 32,749 | 32,028 | +721 | -6,595 | TAIFEX Proxy |
| 三大法人合計 | 362,398 | 367,610 | -5,212 | 76,540 | 75,688 | +852 | -6,064 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 10.14 | 9.97 | +0.17 | 4.29 | 4.25 | +0.04 | +0.13 | TAIFEX Proxy |
| 投信 | 0.00 | 2.32 | -2.32 | 0.00 | 0.00 | +0 | -2.32 | TAIFEX Proxy |
| 自營商 | 8.73 | 6.69 | +2.04 | 3.00 | 2.71 | +0.29 | +1.74 | TAIFEX Proxy |
| 三大法人合計 | 18.87 | 18.98 | -0.11 | 7.29 | 6.96 | +0.33 | -0.44 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,559 | TAIFEX Proxy |
| 買權空方 OI | 11,762 | TAIFEX Proxy |
| 買權多空淨 OI | +797 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-30→2026-10-02) | -249 | TAIFEX Proxy snapshots (2026-10-01) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,179 | TAIFEX Proxy |
| 賣權空方 OI | 9,295 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,116 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-30→2026-10-02) | -492 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：買權 2026-10-02／賣權 2026-10-02 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -2,752 | 2026-09-30→2026-10-02 | TAIFEX Proxy snapshots (2026-10-01) |
| 買權前十大 | -249 | 2026-09-30→2026-10-02 | TAIFEX Proxy snapshots (2026-10-01) |
| 賣權前十大 | -492 | 2026-09-30→2026-10-02 | TAIFEX Proxy snapshots (2026-10-01) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-02；資料時間：2026-10-05 08:08:32；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
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
- margin_ratio：`前值遞補 (DATA 2026-10-01；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-01)，非 T0 2026-10-02
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +26.2 | -80,304 | -802 | +2,596 | +3,762 | +131 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +57.7 | +74,669 | +54 | +0 | -3,100 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +20.3 | -1,006 | +428 | -779 | -5,874 | +721 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
