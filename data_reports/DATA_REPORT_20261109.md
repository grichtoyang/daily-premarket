# DATA_REPORT_20261109

- 報告日期：`2026-11-10`
- T0 交易日期：`2026-11-09`
- 資料產出時間：`2026-11-10 13:10:15`
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
| 加權指數 | 41,661.70 | 點 | twse-proxy |
| 開盤 | 40,347.28 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 42,349.36 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 40,347.28 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 41,661.70 | 點 | twse-proxy |
| 漲跌點數 | 1,960.06 | 點 | twse-proxy |
| 漲跌幅 | +4.94 | % | twse-proxy |
| 成交金額 | 8,770.3 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 804 | twse-proxy |
| 下跌家數 | 229 | twse-proxy |
| 平盤家數 | 52 | twse-proxy |
| 漲停家數 | 121 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 727 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 122 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 34 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 116 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 2 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -900.6 | 億元 | twse-proxy /institutional |
| 投信 | +313.1 | 億元 | twse-proxy /institutional |
| 自營商 | -312.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -899.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,100.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +60.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 252,998 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -19,750 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 162.50 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,475,327 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 30,922 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 940 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,770.3 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,306.8 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 10,077.0 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,549.94 | 173.08 | +2.35 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,253.14 | 673.71 | +2.74 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,907.63 | 917.64 | +3.40 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,389.75 | 1,104.02 | +2.15 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,033.93 | 643.68 | +6.85 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.92 | -5.72 | -22.31 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 60,303.35 | 1,527.85 | +2.60 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,218.04 | 199.19 | +3.97 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,518.87 | 69.92 | +0.29 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,662.81 | 2.02 | +0.06 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,229.66 | 84.17 | +0.76 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,574.25 | 172.25 | +2.33 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,014.50 | 929.25 | +3.43 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,671.00 | 173.00 | +0.33 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,848.70 | 88.20 | +3.20 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.56 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.86 | 0.00 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.26 | -0.00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.86 | 0.10 | +0.30 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.64 | -0.01 | -0.01 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.99 | -0.30 | -0.19 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.56 | -20.14 | -1.48 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 388.62 | 13.18 | +3.51 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.89 | 1.04 | +7.51 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 34.36 | 2.73 | +8.63 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.84 | -1.01 | -1.16 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,123.00 | 8.50 | +0.21 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 74,712.75 | 128.10 | +0.17 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：AI衛星軍工三路商機齊發 廣達華通躍法人關注焦點
  - 來源：Yahoo 台股；發布時間：2026-11-10T04:36:37Z；台北時間：2026-11-10 12:36
  - 摘要：[Newtalk新聞] AI需求持續升溫，半導體、AI伺服器、液冷散熱到低軌衛星及軍工產業，成為市場關注的成長主軸。國泰證期顧問最新報告點名7大布局焦點，其中世界先進受惠AI伺服器電源管理晶片需求，稼動率可望進一步提升；祥碩、高力、崇越也各
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%BB%A3%E9%81%94%E8%A8%82%E5%96%AE%E7%9C%8B%E5%88%B02028%E5%B9%B4-%E8%8F%AF%E9%80%9A%E5%90%83spacex%E5%A4%A7%E5%96%AE-%E6%B3%95%E4%BA%BA%E9%BB%9E%E5%90%8D%E7%84%A1%E4%BA%BA%E6%A9%9F%E5%95%86%E6%A9%9F-043637802.html
- 事件2：ETF定期定額20強有5檔縮水 00878減戶最多讓出亞軍
  - 來源：Yahoo 台股；發布時間：2026-11-10T04:24:16Z；台北時間：2026-11-10 12:24
  - 摘要：證交所今（10）日公布的10月ETF定期定額統計！10月台股大盤面臨高檔震盪，前20大熱門台股ETF雖有逾半數獲得散戶「越跌越撿」逢低卡位，但仍有5檔標的人氣出現逆風縮水。其中，最受矚目的，莫過於國泰永續高股息（00878）才剛在9月奪回的
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%9010%E6%9C%88%E5%AE%9A%E6%9C%9F%E5%AE%9A%E9%A1%8Detf%E9%A2%A8%E9%9B%B2%E6%A6%9C%E3%80%9120%E5%BC%B7%E6%9C%895%E6%AA%94%E7%B8%AE%E6%B0%B4%EF%BC%8100878%E6%B8%9B%E6%9C%80%E5%85%87-%E3%80%8C%E4%BA%8C%E5%93%A5%E5%AF%B6%E5%BA%A7%E3%80%8D%E5%8F%AA%E5%9D%901%E5%80%8B%E6%9C%88%E5%8F%88%E5%A4%B1%E5%AE%88-042537593.html
- 事件3：光學股紅燈有人亮有人滅 耀穎漲停先進光開高翻黑
  - 來源：Yahoo 台股；發布時間：2026-11-10T04:25:00Z；台北時間：2026-11-10 12:25
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導美股四大指數周一全數收紅，唯輝達（NVDA-US）因黃仁勛傳出婚外情重挫收黑。台股今（10）日持續上漲，開盤上漲468.63點至42...
  - 原文連結：https://tw.stock.yahoo.com/news/10%E6%9C%88%E7%87%9F%E6%94%B6%E5%B9%B4-%E6%9C%88%E9%9B%99%E6%B8%9B-%E5%85%89%E5%AD%B8%E5%85%83%E4%BB%B6-%E9%80%99%E6%AA%94-%E6%BC%B2%E5%81%9C%E6%89%93%E9%96%8B900%E5%85%83%E5%A4%A7%E9%97%9C%E6%B2%92%E5%AE%88%E4%BD%8F-042500037.html
- 事件4：台股一度漲1400點 正2雙雄爆量瑤池金母也嗨翻
  - 來源：Yahoo 台股；發布時間：2026-11-10T04:15:00Z；台北時間：2026-11-10 12:15
  - 摘要：[FTNN新聞網]記者張書翰／綜合報導台股加權指數今（10）日股價再度上揚，一度狂飆逾1400點、攻上4萬3大關，截至11時55分，漲勢則有所收斂，暫報42397.13點，...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1-%E5%BA%A6%E6%94%B6%E5%BE%A94%E8%90%AC3%E9%97%9C%E5%8D%A1-%E7%91%A4%E6%B1%A0%E9%87%91%E6%AF%8D-%E6%BC%B2%E7%A0%B44-%E9%A3%8633%E8%90%AC-041500809.html
- 事件5：輝達重挫對手撿到槍 博通AMD一天市值大暴衝
  - 來源：Yahoo 台股；發布時間：2026-11-10T04:06:21Z；台北時間：2026-11-10 12:06
  - 摘要：「AI教父」黃仁勳身陷女間諜風暴遭調查，輝達Nvidia股價暴跌，但競爭對手AMD與博通Broadcom「撿到槍」，股價卻飆漲13%與8.8%，博通市值一天暴增台幣4.4兆元，超車Tesla特斯拉，一舉躋身全球前十大市值排行榜，而AMD也一
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E9%81%87%E9%9B%A3%E5%AE%83%E5%80%86%E3%80%8C%E6%92%BF%E5%88%B0%E6%A7%8D%E3%80%8D%EF%BC%9F-%E5%8D%9A%E9%80%9A%E6%93%A0%E9%80%B2%E5%85%A8%E7%90%83%E5%89%8D10%E5%BC%B7-%E8%88%87amd%E5%B8%82%E5%80%BC%E4%B8%80%E5%A4%A9%E6%9A%B4%E5%A2%9E76%E5%85%86%E5%85%83-040621476.html
- 事件6：19千金紅燈高掛！南電、萬潤股價重返四位數 股王卻黯然
  - 來源：Yahoo 台股；發布時間：2026-11-10T03:07:59Z；台北時間：2026-11-10 11:07
  - 摘要：美股科技股強彈，加上國安基金護盤消息提振信心，台股今（10）日延續漲勢，千金股掀起漲停潮，台達電（2308）、世芯-KY（3661）率先亮燈點火，創意（3443）、旺矽（6223）、聯亞（3081）等接棒衝鋒，盤中多達19檔千金股攻上漲停。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%89%B5%E6%84%8F%E5%8F%B0%E9%81%94%E9%9B%BB%E7%AD%8919%E6%AA%94%E5%8D%83%E9%87%91%E8%82%A1%E9%96%83%E7%B4%85%E7%87%88%EF%BC%81%E5%8D%97%E9%9B%BB%E8%90%AC%E6%BD%A4%E4%BA%AE%E7%87%88%E6%BC%B2%E5%81%9C%E9%87%8D%E8%BF%94%E5%8D%83%E5%85%83%E4%BF%B1%E6%A8%82%E9%83%A8-030759236.html
- 事件7：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件8：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件9：A key report for where inflation stood in October comes out Tuesday. Here's what to expect
  - 來源：CNBC；發布時間：Mon, 09 Nov 2026 21:03:55 GMT；台北時間：2026-11-10 05:03
  - 摘要：The CPI headline reading is expected to show an increase of 0.3% while the core is forecast to increase 0.2%.
  - 原文連結：https://www.cnbc.com/2026/11/09/october-cpi-report-2026-inflation.html
- 事件10：Trump administration proposes stricter work-search rules for unemployment benefits
  - 來源：CNBC；發布時間：Mon, 09 Nov 2026 19:59:55 GMT；台北時間：2026-11-10 03:59
  - 摘要：A Labor Department proposal would require unemployment claimants to report at least five qualifying work-search activities each week.
  - 原文連結：https://www.cnbc.com/2026/11/09/trump-unemployment-work-search-rule.html
- 事件11：The stock-market rally keeps spreading beyond Big Tech. October inflation data could put it to the test.
  - 來源：MarketWatch；發布時間：Mon, 09 Nov 2026 21:24:00 GMT；台北時間：2026-11-10 05:24
  - 摘要：Tuesday&#x2019;s CPI inflation report and a heavy lineup of Federal Reserve speakers could test the rotation trade&#x2019;s resilience
  - 原文連結：https://www.marketwatch.com/story/the-stock-market-rally-keeps-spreading-beyond-big-tech-october-inflation-data-could-put-it-to-the-test-c1b87dcd?mod=mw_rss_topstories
- 事件12：SoftBank Group shares surge 13% as Asian tech stocks track Wall Street rebound
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 03:58:46 GMT；台北時間：2026-11-10 11:58
  - 摘要：A sharp decline in oil prices lifted sentiment while renewed buying in semiconductor names overnight spilled over into Asia, following last week's bru
  - 原文連結：https://www.cnbc.com/2026/11/10/ai-softbank-sk-hynix-samsung-wall-street-tech-stocks.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-09

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 40,099 | TAIFEX Proxy |
| 最高價 | 42,317 | TAIFEX Proxy |
| 最低價 | 39,996 | TAIFEX Proxy |
| 收盤價 | 41,423 | TAIFEX Proxy |
| 漲跌點數 | +1,771 | TAIFEX Proxy |
| 漲跌幅 | +4.47 | TAIFEX Proxy |
| 成交量 | 94,766 | TAIFEX Proxy |
| 日盤高點及低點 | 42,317 / 39,996 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 41,240 | TAIFEX Proxy |
| 最高價 | 42,657 | TAIFEX Proxy |
| 最低價 | 40,715 | TAIFEX Proxy |
| 收盤價 | 42,542 | TAIFEX Proxy |
| 漲跌點數 | +1,064 | TAIFEX Proxy |
| 漲跌幅 | +2.57 | TAIFEX Proxy |
| 成交量 | 55,081 | TAIFEX Proxy |
| 夜盤高點及低點 | 42,657 / 40,715 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,571 | TAIFEX Proxy |
| 外資空方 OI | 113,342 | TAIFEX Proxy |
| 外資多空淨 OI | -101,771 | TAIFEX Proxy |
| 投信多方 OI | 98,979 | TAIFEX Proxy |
| 投信空方 OI | 3,428 | TAIFEX Proxy |
| 投信多空淨 OI | +95,551 | TAIFEX Proxy |
| 自營商多方 OI | 5,813 | TAIFEX Proxy |
| 自營商空方 OI | 4,787 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,026 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,363 | TAIFEX Proxy |
| 三大法人合計空方 OI | 121,557 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,194 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,841 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +5,114 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -654 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,429 | TAIFEX Proxy |
| 前十大交易人空方 OI | 91,257 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,172 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-04→2026-11-09) | -90 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：2026-11-09 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 99,731 | TAIFEX Proxy |
| 外資日盤空單交易量 | 102,516 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,785 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 31,794 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 32,959 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,165 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,620 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +5,114 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | -1 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +5,115 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -696 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +370 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,066 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,633 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -796 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +136.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -66.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 41,423 | TAIFEX Proxy |
| 加權指數價格 | 41,661.70 | twse-proxy |
| 台指期與加權指數價差 | -238.70 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.57 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -238.70 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +1,119 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 41,423 | 42,542 | -1,119 | TAIFEX Proxy |
| 成交量 | 94,766 | 55,081 | +39,685 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+2,619（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 99,731 | 102,516 | -2,785 | 31,794 | 32,959 | -1,165 | -1,620 | 11,571 | 113,342 | -101,771 | -1,841 | TAIFEX Proxy |
| 投信 | 5,134 | 20 | +5,114 | 0 | 1 | -1 | +5,115 | 98,979 | 3,428 | +95,551 | +5,114 | TAIFEX Proxy |
| 自營商 | 7,672 | 8,368 | -696 | 1,426 | 1,056 | +370 | -1,066 | 5,813 | 4,787 | +1,026 | -654 | TAIFEX Proxy |
| 三大法人合計 | 112,537 | 110,904 | +1,633 | 33,220 | 34,016 | -796 | +2,429 | 116,363 | 121,557 | -5,194 | +2,619 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,429 | TAIFEX Proxy |
| 前十大交易人空方 OI | 91,257 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,172 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-04→2026-11-09) | -90 | TAIFEX Proxy snapshots (2026-11-05) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 36.76% | TAIFEX Proxy |
| 夜盤漲跌點數 | +1,064 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,165 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-09 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-10 13:10:15 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 136,615 | TAIFEX Proxy |
| Call 總未平倉量 OI | 68,097 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 109,360 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,424 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.25 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.17 | TAIFEX Proxy |
| Put／Call Ratio | 0.46 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-06→2026-11-09) | 3.96 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-06→2026-11-09) | 11.46 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 32,589 | TAIFEX Proxy |
| 外資 Call日賣 | 30,109 | TAIFEX Proxy |
| 外資 Call日淨 | +2,480 | TAIFEX Proxy |
| 外資 Put日買 | 33,416 | TAIFEX Proxy |
| 外資 Put日賣 | 32,877 | TAIFEX Proxy |
| 外資 Put日淨 | +539 | TAIFEX Proxy |
| 外資 Call夜買 | 24,117 | TAIFEX Proxy |
| 外資 Call夜賣 | 24,396 | TAIFEX Proxy |
| 外資 Call夜淨 | -279 | TAIFEX Proxy |
| 外資 Put夜買 | 34,810 | TAIFEX Proxy |
| 外資 Put夜賣 | 34,999 | TAIFEX Proxy |
| 外資 Put夜淨 | -189 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,941 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2,759 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +728 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 54,273 | TAIFEX Proxy |
| 自營商 Call日賣 | 48,638 | TAIFEX Proxy |
| 自營商 Call日淨 | +5,635 | TAIFEX Proxy |
| 自營商 Put日買 | 38,984 | TAIFEX Proxy |
| 自營商 Put日賣 | 45,295 | TAIFEX Proxy |
| 自營商 Put日淨 | -6,311 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,475 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,956 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,481 | TAIFEX Proxy |
| 自營商 Put夜買 | 21,276 | TAIFEX Proxy |
| 自營商 Put夜賣 | 21,756 | TAIFEX Proxy |
| 自營商 Put夜淨 | -480 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +11,946 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +7,116 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,831 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,692 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,300 | 3,846 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 2,981 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,692 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,692 | 12.76% | TAIFEX Proxy |
| C2 | 48,300 | 3,846 | 5.65% | TAIFEX Proxy |
| C3 | 45,000 | 2,981 | 4.38% | TAIFEX Proxy |
| C4 | 43,000 | 2,509 | 3.68% | TAIFEX Proxy |
| C5 | 44,000 | 1,724 | 2.53% | TAIFEX Proxy |
| C6 | 44,500 | 1,692 | 2.48% | TAIFEX Proxy |
| C7 | 41,000 | 1,616 | 2.37% | TAIFEX Proxy |
| C8 | 46,500 | 1,429 | 2.1% | TAIFEX Proxy |
| C9 | 42,000 | 1,246 | 1.83% | TAIFEX Proxy |
| C10 | 40,700 | 1,140 | 1.67% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 37,400 | 2,258 | TAIFEX Proxy |
| Put OI 第2大履約價 | 38,000 | 2,008 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 1,887 | TAIFEX Proxy |
| Put OI 最大履約價 | 37,400 | 2,258 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 37,400 | 2,258 | 7.19% | TAIFEX Proxy |
| P2 | 38,000 | 2,008 | 6.39% | TAIFEX Proxy |
| P3 | 40,000 | 1,887 | 6.0% | TAIFEX Proxy |
| P4 | 35,700 | 1,756 | 5.59% | TAIFEX Proxy |
| P5 | 39,000 | 1,290 | 4.11% | TAIFEX Proxy |
| P6 | 41,000 | 1,114 | 3.55% | TAIFEX Proxy |
| P7 | 39,500 | 924 | 2.94% | TAIFEX Proxy |
| P8 | 40,900 | 835 | 2.66% | TAIFEX Proxy |
| P9 | 40,500 | 755 | 2.4% | TAIFEX Proxy |
| P10 | 37,500 | 750 | 2.39% | TAIFEX Proxy |


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
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 37,400 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-09 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 40,506.19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-09 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 65,466 | 63,525 | +1,941 | 59,116 | 59,206 | -90 | +2,031 | TAIFEX Proxy |
| 投信 | 347 | 280 | +67 | 0 | 0 | +0 | +67 | TAIFEX Proxy |
| 自營商 | 99,568 | 87,622 | +11,946 | 37,231 | 38,232 | -1,001 | +12,947 | TAIFEX Proxy |
| 三大法人合計 | 165,381 | 151,427 | +13,954 | 96,347 | 97,438 | -1,091 | +15,045 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 28.80 | 28.30 | +0.50 | 7.92 | 8.09 | -0.16 | +0.66 | TAIFEX Proxy |
| 投信 | 0.13 | 0.05 | +0.08 | 0.00 | 0.00 | +0 | +0.08 | TAIFEX Proxy |
| 自營商 | 19.47 | 17.73 | +1.75 | 6.05 | 5.86 | +0.19 | +1.56 | TAIFEX Proxy |
| 三大法人合計 | 48.41 | 46.08 | +2.32 | 13.97 | 13.95 | +0.02 | +2.30 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 20,765 | TAIFEX Proxy |
| 買權空方 OI | 27,337 | TAIFEX Proxy |
| 買權多空淨 OI | -6,572 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-04→2026-11-09) | -2,446 | TAIFEX Proxy snapshots (2026-11-05) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 11,322 | TAIFEX Proxy |
| 賣權空方 OI | 15,768 | TAIFEX Proxy |
| 賣權多空淨 OI | -4,446 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-04→2026-11-09) | -1,727 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：買權 2026-11-09／賣權 2026-11-09 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -90 | 2026-11-04→2026-11-09 | TAIFEX Proxy snapshots (2026-11-05) |
| 買權前十大 | -2,446 | 2026-11-04→2026-11-09 | TAIFEX Proxy snapshots (2026-11-05) |
| 賣權前十大 | -1,727 | 2026-11-04→2026-11-09 | TAIFEX Proxy snapshots (2026-11-05) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-09；資料時間：2026-11-10 13:10:15；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (4)：futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-11-09 非今日 2026-11-10，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：跨到期換月（舊202611F1→新202611W2），日對日 OI/Walls 變化不適用

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`stockintelli 大盤融資維持率 (民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -900.6 | -101,771 | -2,785 | -1,165 | +1,941 | -90 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +313.1 | +95,551 | +5,114 | -1 | +67 | +0 | 趨勢偏多 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
| 自營商 | -312.2 | +1,026 | -696 | +370 | +11,946 | -1,001 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
