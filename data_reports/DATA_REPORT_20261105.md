# DATA_REPORT_20261105

- 報告日期：`2026-11-06`
- T0 交易日期：`2026-11-05`
- 資料產出時間：`2026-11-06 12:08:23`
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

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,604.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -274.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 313,119 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 31,898 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 155.70 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,882,568 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 36,068 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 1,659 | 張 | TWSE TWT93U + TPEX margin_sbl |

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
| S&P 500 | ^GSPC | 7,353.73 | -334.89 | -4.36 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,315.00 | -1,421.51 | -5.52 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,629.81 | -1,807.36 | -6.36 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,523.06 | -1,833.06 | -3.44 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,011.14 | -1,257.51 | -12.25 | Yahoo Finance Chart API |
| VIX | ^VIX | 28.18 | 11.57 | +69.66 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 57,439.87 | -3,638.03 | -5.96 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,108.08 | -275.72 | -5.12 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,527.36 | -269.62 | -1.09 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,647.90 | -42.01 | -1.14 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,216.95 | -254.14 | -2.22 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,386.75 | 3.75 | +0.05 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,977.50 | 225.50 | +0.84 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,162.00 | -453.00 | -0.88 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,726.90 | -8.50 | -0.31 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.46 | -0.12 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.84 | -0.06 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.25 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.95 | 0.12 | +0.38 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.75 | 0.19 | +0.19 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.84 | -0.52 | -0.33 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,358.18 | 18.11 | +1.35 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 353.10 | -42.65 | -10.78 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.38 | -2.68 | -16.69 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 29.72 | -7.79 | -20.77 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 91.77 | 1.25 | +1.38 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,053.60 | -59.90 | -1.46 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 75,590.27 | -4,815.02 | -5.99 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：金管會下午將宣布首波救市措施 市場猜限空令先上陣
  - 來源：Yahoo 台股；發布時間：2026-11-06T03:27:00Z；台北時間：2026-11-06 11:27
  - 摘要：台股今（6）日遭遇史詩級賣壓，加權指數盤中一度狂瀉3737.67點，跌幅達8.99%，創下史上最大盤中跌點紀錄，台積電、聯發科、台達電等權值股重挫，市場恐慌情緒急遽升高。行政院長卓榮泰已指示金管會密切關注國內外股市變化，金管會主委彭金隆今天
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E7%AE%A1%E6%9C%83%E6%93%AC%E5%AE%A3%E5%B8%83%E9%A6%96%E6%B3%A2%E6%95%91%E5%B8%82%E6%8E%AA%E6%96%BD-%E5%B8%82%E5%A0%B4%E7%8B%82%E7%8C%9C-%E6%98%AF%E9%80%99%E5%80%8B-032700958.html
- 事件3：富喬開盤跌停拚到翻紅又跳水 分析師：不急著追價
  - 來源：Yahoo 台股；發布時間：2026-11-06T03:40:47Z；台北時間：2026-11-06 11:40
  - 摘要：今日社群台股最Hot議題

「富喬：我的一天20%是從跌停到平盤再跌停」、「富喬幹上去了」、「哇靠 富喬太扯」、「富喬好猛」、「富喬這啥鬼」。
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E5%AF%8C%E5%96%AC%E4%B8%8A%E6%BC%94%E5%A4%A7%E6%80%92%E7%A5%9E%E5%BE%8C%E5%8F%88%E7%BF%BB%E9%BB%91%EF%BC%81%E7%B6%B2%E5%96%8A%E3%80%8C%E4%B8%80%E5%A4%A920%E5%BE%9E%E8%B7%8C%E5%81%9C%E5%88%B0%E5%B9%B3%E7%9B%A4%E5%86%8D%E8%B7%8C%E5%81%9C%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E5%8B%B8%E5%85%88%E8%A7%80%E6%9C%9B-034150027.html
- 事件4：台積狂跌 外資帳上一度蒸發10兆
  - 來源：Yahoo 台股；發布時間：2026-11-06T03:39:20Z；台北時間：2026-11-06 11:39
  - 摘要：台股今（6）日遭遇極端恐慌性賣壓，盤中狂瀉近4,000點創下歷史最大跌點，權王台積電更一度被打入2,020 元跌停價、重跌220元，儘管外資持股比例已砍近20年新低，但手中仍握有1,770多萬張龐大部位，隨著今日台積電股價崩跌，外資持股市值
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%A4%A7%E8%B7%8C%E3%80%81%E5%A4%96%E8%B3%87%E4%B9%9F%E8%99%A7%E5%A4%A7%E4%BA%86%EF%BC%81%E5%B8%82%E5%80%BC1%E5%80%8B%E6%9C%88%E8%92%B8%E7%99%BC10%E5%85%86%E5%85%83-%E6%98%AF%E9%AD%8F%E5%93%B2%E5%AE%B6%E7%9A%842100%E5%80%8D-033920583.html
- 事件5：今再加碼0050、接連投入2億 郭哲榮：真的沒錢了
  - 來源：Yahoo 台股；發布時間：2026-11-06T03:13:00Z；台北時間：2026-11-06 11:13
  - 摘要：台股今（6）日遭遇史詩級賣壓，加權指數開盤跳空跌破4萬點，盤中一度狂瀉3737.67點、跌幅達8.99%，創下史上最大盤中跌點紀錄。日前多次看好台股年底上看5萬點的分析師郭哲榮，面對市場急殺不僅沒有退場，反而在社群平台Threads自曝再投
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9A%B4%E8%B7%8C3737%E9%BB%9E%E6%B2%92%E5%9C%A8%E6%80%95-%E9%83%AD%E5%93%B2%E6%A6%AE%E5%86%8D%E7%A0%B85%E5%8D%83%E8%90%AC%E8%B2%B70050-%E7%9C%9F%E7%9A%84%E6%B2%92%E9%8C%A2%E4%BA%86-031300025.html
- 事件6：路透：輝達60萬顆H200囤積在香港 等北京批准
  - 來源：Yahoo 台股；發布時間：2026-11-06T03:18:20Z；台北時間：2026-11-06 11:18
  - 摘要：中美科技角力越演越烈，《路透社》披露，輝達高階AI晶片H200有多達60萬顆囤積在香港，等待運往大陸，但北京至今仍未批准大規模進口。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%9460%E8%90%AC%E9%A1%86h200%E6%99%B6%E7%89%87%E8%A2%AB%E7%88%86-%E5%9B%A4%E7%A9%8D%E5%9C%A8%E9%A6%99%E6%B8%AF-%E5%8C%97%E4%BA%AC%E9%81%B2%E9%81%B2%E4%B8%8D%E6%94%BE%E8%A1%8C-031820040.html
- 事件7：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件8：IRS announces new federal income tax brackets for 2027
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 01:21:08 GMT；台北時間：2026-11-06 09:21
  - 摘要：The IRS has announced higher federal income tax brackets and standard deductions for 2027. Here's what taxpayers need to know.
  - 原文連結：https://www.cnbc.com/2026/11/05/2027-federal-tax-brackets.html
- 事件9：Barkin sees interest rate hikes ahead, but at a gradual pace
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 16:34:33 GMT；台北時間：2026-11-06 00:34
  - 摘要：In a CNBC interview, the policymaker expressed concern over inflation and said monetary policy will need to adjust.
  - 原文連結：https://www.cnbc.com/2026/11/05/barkin-sees-interest-rate-hikes-ahead-but-at-a-gradual-pace.html
- 事件10：Nasdaq sell-off batters Asian chip stocks as SK Hynix, Samsung, Softbank, TSMC tumble
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 02:40:15 GMT；台北時間：2026-11-06 10:40
  - 摘要：Asian technology stocks tumbled Friday, tracking a sharp sell-off on Wall Street overnight that sent the tech-heavy Nasdaq Composite into correction t
  - 原文連結：https://www.cnbc.com/2026/11/06/tech-stocks-sk-hynix-samsung-softbank.html
- 事件11：Wall Street's fear gauge surges the most since April. Why traders think it should be even higher
  - 來源：CNBC；發布時間：Thu, 05 Nov 2026 19:20:21 GMT；台北時間：2026-11-06 03:20
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
| 開盤價 | 41,990 | TAIFEX Proxy |
| 最高價 | 42,298 | TAIFEX Proxy |
| 最低價 | 38,799 | TAIFEX Proxy |
| 收盤價 | 38,936 | TAIFEX Proxy |
| 漲跌點數 | -2,946 | TAIFEX Proxy |
| 漲跌幅 | -7.03 | TAIFEX Proxy |
| 成交量 | 89,296 | TAIFEX Proxy |
| 夜盤高點及低點 | 42,298 / 38,799 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

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
| 前十大交易人多方 OI | 100,370 | TAIFEX Proxy |
| 前十大交易人空方 OI | 86,653 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,717 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-03→2026-11-05) | +2,149 | TAIFEX Proxy snapshots (2026-11-04) |
- 資料日期：2026-11-05 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 98,413 | TAIFEX Proxy |
| 外資日盤空單交易量 | 101,388 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,975 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 51,736 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 51,088 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +648 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,623 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +783 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +783 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -650 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +918 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,568 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,842 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,566 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -243.3 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +129.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 41,915 | TAIFEX Proxy |
| 加權指數價格 | 41,574.72 | twse-proxy |
| 台指期與加權指數價差 | +340.28 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.82 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +340.28 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -2,979 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 41,915 | 38,936 | +2,979 | TAIFEX Proxy |
| 成交量 | 98,430 | 89,296 | +9,134 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,852（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 98,413 | 101,388 | -2,975 | 51,736 | 51,088 | +648 | -3,623 | 13,388 | 109,039 | -95,651 | -2,004 | TAIFEX Proxy |
| 投信 | 1,088 | 305 | +783 | 0 | 0 | +0 | +783 | 93,279 | 2,996 | +90,283 | +783 | TAIFEX Proxy |
| 自營商 | 9,911 | 10,561 | -650 | 5,014 | 4,096 | +918 | -1,568 | 6,279 | 3,949 | +2,330 | -631 | TAIFEX Proxy |
| 三大法人合計 | 109,412 | 112,254 | -2,842 | 56,750 | 55,184 | +1,566 | -4,408 | 112,946 | 115,984 | -3,038 | -1,852 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,370 | TAIFEX Proxy |
| 前十大交易人空方 OI | 86,653 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,717 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-03→2026-11-05) | +2,149 | TAIFEX Proxy snapshots (2026-11-04) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 47.57% | TAIFEX Proxy |
| 夜盤漲跌點數 | -2,946 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +648 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-05 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F1 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-06 12:08:23 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 304,899 | TAIFEX Proxy |
| Call 總未平倉量 OI | 90,160 | TAIFEX Proxy |
| Call OI 增減 | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 229,988 | TAIFEX Proxy |
| Put 總未平倉量 OI | 33,429 | TAIFEX Proxy |
| Put OI 增減 | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.33 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.70 | TAIFEX Proxy |
| Put／Call Ratio | 0.37 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-04→2026-11-05) | -12.37 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-04→2026-11-05) | -5.28 | TAIFEX Proxy |
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
| 外資 Call夜買 | 48,207 | TAIFEX Proxy |
| 外資 Call夜賣 | 48,365 | TAIFEX Proxy |
| 外資 Call夜淨 | -158 | TAIFEX Proxy |
| 外資 Put夜買 | 39,168 | TAIFEX Proxy |
| 外資 Put夜賣 | 39,090 | TAIFEX Proxy |
| 外資 Put夜淨 | +78 | TAIFEX Proxy |
| 外資 日盤淨總量 | -1,641 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -1,399 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +6 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 81,577 | TAIFEX Proxy |
| 自營商 Call日賣 | 86,731 | TAIFEX Proxy |
| 自營商 Call日淨 | -5,154 | TAIFEX Proxy |
| 自營商 Put日買 | 64,287 | TAIFEX Proxy |
| 自營商 Put日賣 | 65,015 | TAIFEX Proxy |
| 自營商 Put日淨 | -728 | TAIFEX Proxy |
| 自營商 Call夜買 | 25,180 | TAIFEX Proxy |
| 自營商 Call夜賣 | 36,118 | TAIFEX Proxy |
| 自營商 Call夜淨 | -10,938 | TAIFEX Proxy |
| 自營商 Put夜買 | 30,288 | TAIFEX Proxy |
| 自營商 Put夜賣 | 26,194 | TAIFEX Proxy |
| 自營商 Put夜淨 | +4,094 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -4,426 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,784 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -4,822 | TAIFEX Proxy |

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
| 與前一交易日的變化 | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 42,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,102.53 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-05 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,950 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 | +0 | TAIFEX Proxy snapshots (2026-11-04) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 175,734 | 177,375 | -1,641 | 87,297 | 87,533 | -236 | -1,405 | TAIFEX Proxy |
| 投信 | 2,760 | 4,247 | -1,487 | 0 | 0 | +0 | -1,487 | TAIFEX Proxy |
| 自營商 | 146,592 | 151,018 | -4,426 | 51,374 | 66,406 | -15,032 | +10,606 | TAIFEX Proxy |
| 三大法人合計 | 325,086 | 332,640 | -7,554 | 138,671 | 153,939 | -15,268 | +7,714 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 22.08 | 22.27 | -0.19 | 10.21 | 10.14 | +0.07 | -0.25 | TAIFEX Proxy |
| 投信 | 0.08 | 0.49 | -0.41 | 0.00 | 0.00 | +0 | -0.41 | TAIFEX Proxy |
| 自營商 | 20.17 | 19.18 | +0.99 | 10.47 | 13.12 | -2.65 | +3.64 | TAIFEX Proxy |
| 三大法人合計 | 42.33 | 41.94 | +0.39 | 20.68 | 23.27 | -2.59 | +2.98 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 13,429 | TAIFEX Proxy |
| 買權空方 OI | 18,160 | TAIFEX Proxy |
| 買權多空淨 OI | -4,731 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-03→2026-11-05) | -1,684 | TAIFEX Proxy snapshots (2026-11-04) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,834 | TAIFEX Proxy |
| 賣權空方 OI | 11,619 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,785 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-03→2026-11-05) | -493 | TAIFEX Proxy snapshots (2026-11-04) |
- 資料日期：買權 2026-11-05／賣權 2026-11-05 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +2,149 | 2026-11-03→2026-11-05 | TAIFEX Proxy snapshots (2026-11-04) |
| 買權前十大 | -1,684 | 2026-11-03→2026-11-05 | TAIFEX Proxy snapshots (2026-11-04) |
| 賣權前十大 | -493 | 2026-11-03→2026-11-05 | TAIFEX Proxy snapshots (2026-11-04) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-05；資料時間：2026-11-06 12:08:23；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：5 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (4)：futures.gamma_wall, futures.gamma_flip, options.chain_oi_change, options.wall_change
- 註記：futures-price-after-hours 日期 2026-11-05 非今日 2026-11-06，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
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
| 外資 | -1,024.6 | -95,651 | -2,975 | +648 | -1,641 | -236 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +225.9 | +90,283 | +783 | +0 | -1,487 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -435.3 | +2,330 | -650 | +918 | -4,426 | -15,032 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
