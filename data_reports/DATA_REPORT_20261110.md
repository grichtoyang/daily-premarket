# DATA_REPORT_20261110

- 報告日期：`2026-11-11`
- T0 交易日期：`2026-11-10`
- 資料產出時間：`2026-11-11 11:42:49`
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
| 加權指數 | 42,711.92 | 點 | twse-proxy |
| 開盤 | 42,130.33 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 43,135.92 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 41,930.03 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 42,711.92 | 點 | twse-proxy |
| 漲跌點數 | 1,050.22 | 點 | twse-proxy |
| 漲跌幅 | +2.52 | % | twse-proxy |
| 成交金額 | 10,340.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 526 | twse-proxy |
| 下跌家數 | 491 | twse-proxy |
| 平盤家數 | 68 | twse-proxy |
| 漲停家數 | 30 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 451 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 360 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 57 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 42 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 3 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -341.2 | 億元 | twse-proxy /institutional |
| 投信 | +398.9 | 億元 | twse-proxy /institutional |
| 自營商 | -175.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -117.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,059.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -40.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 243,888 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -9,060 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 168.00 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,477,877 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 32,757 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 1,835 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,340.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,088.3 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 12,428.4 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,520.93 | -29.01 | -0.38 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,065.88 | -187.27 | -0.74 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,740.79 | -166.84 | -0.60 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,231.89 | -157.86 | -0.30 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,998.33 | -35.60 | -0.35 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.46 | -0.46 | -2.31 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 60,942.48 | 482.90 | +0.80 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,336.12 | 96.99 | +1.85 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,344.96 | -212.08 | -0.86 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,657.67 | -6.05 | -0.17 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,264.12 | 22.58 | +0.20 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,586.00 | 41.75 | +0.55 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 28,175.25 | 340.00 | +1.22 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,457.00 | 142.00 | +0.27 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,838.40 | 9.50 | +0.34 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.73 | 0.17 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 4.98 | 0.12 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.35 | 0.09 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.84 | 0.05 | +0.14 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.26 | 0.03 | +0.03 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.85 | 0.87 | +0.55 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,337.63 | -6.21 | -0.46 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 396.48 | 7.86 | +2.02 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 15.04 | 0.15 | +1.01 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 35.48 | 1.12 | +3.26 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 86.59 | 0.55 | +0.64 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,053.30 | 23.10 | +0.57 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 73,662.89 | -1,560.26 | -2.07 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股盤中飆千點 分析師提醒：部分個股先減碼
  - 來源：Yahoo 台股；發布時間：2026-11-11T03:28:26Z；台北時間：2026-11-11 11:28
  - 摘要：「說好的雙十一特價呢？」「今天小兒該認錯了吧」「早上誰說要賣的 太壞心了」「確認V轉了，等站穩的可以進了」
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90hot%E5%8F%B0%E8%82%A1%E3%80%91%E5%A4%A7%E7%9B%A4%E5%8F%88%E9%A3%86%E5%8D%83%E9%BB%9E%E7%B6%B2%E7%AC%91%E3%80%8C%E8%AA%AA%E5%A5%BD%E7%9A%84%E9%9B%99%E5%8D%81%E4%B8%80%E7%89%B9%E5%83%B9%E5%91%A2%E3%80%8D-%E5%88%86%E6%9E%90%E5%B8%AB%E6%9B%9D%EF%BC%9A%E6%B8%9B%E7%A2%BC%E6%99%82%E6%A9%9F%E6%B5%AE%E7%8F%BE-032826781.html
- 事件2：半導體ETF全數紅盤 00830溢價近2.5%
  - 來源：Yahoo 台股；發布時間：2026-11-11T02:59:47Z；台北時間：2026-11-11 10:59
  - 摘要：半導體ETF絕地大反攻！10檔今（11日）早全數紅盤表現，有7檔以上漲幅超過2%，其中國泰費城半導體（00830）配息高達9元，獲買盤追捧，股價站上74.75%，出現最大溢價差近2.5%；台股型以兆豐洲際半導體（00911）漲幅2.68%最
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8D%8A%E5%B0%8E%E9%AB%94etf%E7%B5%95%E5%9C%B0%E5%8F%8D%E6%94%BB%EF%BC%81%E5%9C%8B%E6%B3%B0%E8%B2%BB%E5%8D%8A00830%E6%BA%A2%E5%83%B925-00891%E7%AD%897%E6%AA%94%E6%BC%B2%E5%B9%85%E7%A0%B42-025947390.html
- 事件3：10月營收小幅月減 聯發科多空交戰分析師點爆發時機
  - 來源：Yahoo 台股；發布時間：2026-11-11T02:40:07Z；台北時間：2026-11-11 10:40
  - 摘要：IC 設計龍頭聯發科（2454）公布 10 月營收達550.26億元，雖然月微減 0.67%，但年增 5.77% 仍穩健維持高檔。股價今（11）日盤中多空交戰劇烈，高低爆量拉鋸達140元；截至上午10點30分，股價維持上漲30元，於 3,8
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E7%99%BC%E7%A7%9110%E6%9C%88%E7%87%9F%E6%94%B6%E6%9C%88%E6%B8%9B%EF%BC%81%E7%9B%A4%E4%B8%AD%E9%AB%98%E4%BD%8E%E9%9C%87%E7%9B%AA140%E5%85%83-%E5%88%86%E6%9E%90%E5%B8%AB%EF%BC%9A%E6%94%B6%E7%B4%85%E6%A9%9F%E7%8E%87%E9%AB%98-024007514.html
- 事件4：PCB亮9顆紅燈 玻纖布類股富喬、德宏強勢演出
  - 來源：Yahoo 台股；發布時間：2026-11-11T02:42:00Z；台北時間：2026-11-11 10:42
  - 摘要：[FTNN新聞網]記者何亞軒／綜合報導今（11）日台股加權指數盤中暫報43,430.25點，漲718.33點，漲幅1.68%，觀察今日盤中PCB個股趨勢，受惠於台股跌深迎來大反彈...
  - 原文連結：https://tw.stock.yahoo.com/news/pcb%E6%90%96%E5%8F%8D%E6%94%BB%E5%A4%A7%E6%97%97-9%E6%AA%94%E6%A6%82%E5%BF%B5%E8%82%A1%E5%99%B4%E5%87%BA%E6%BC%B2%E5%81%9C-%E9%80%99%E7%8E%BB%E7%BA%96%E5%B8%83-10%E6%9C%88%E7%87%9F%E6%94%B6%E8%A1%9D%E7%A0%B410%E5%84%84%E5%85%83-%E7%9B%A4%E4%B8%AD%E5%BC%B7%E6%94%BB140%E5%85%83-024200129.html
- 事件5：美系外資開第一槍降評 多檔記憶體目標價幾乎腰斬
  - 來源：Yahoo 台股；發布時間：2026-11-11T02:04:01Z；台北時間：2026-11-11 10:04
  - 摘要：【財訊快報／記者劉居全報導】美系外資在最新出爐的報告率先開了第一槍，全面調降記憶體族群評等及目標價，而且多檔目標價幾乎都腰斬，其中群聯(8299)評等由原先的「中立」降至「減碼」，目標價由原先的2588元一口氣大幅下修至1357元，接近腰斬
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E7%B3%BB%E5%A4%96%E8%B3%87%E9%96%8B%E9%A6%96%E6%A7%8D-%E8%AA%BF%E9%99%8D%E8%A8%98%E6%86%B6%E9%AB%94%E6%97%8F%E7%BE%A4%E8%A9%95%E7%AD%89-%E7%9B%AE%E6%A8%99%E5%83%B9-%E7%BE%A4%E8%81%AF-%E8%8F%AF%E9%82%A6%E7%AD%89%E9%81%AD%E9%87%8D%E7%A0%8D-020401316.html
- 事件6：國安基金進場遭疑選舉操作 財長回應
  - 來源：Yahoo 台股；發布時間：2026-11-11T02:38:16Z；台北時間：2026-11-11 10:38
  - 摘要：國安基金上周五決議啟動第10次進場護盤，引發網友質疑是為年底選舉操作。財政部長莊翠雲今（11）於立法院財政委員會備詢時指出，上周五台股較今年高點下跌逾兩成，外資持續賣超，市場投資信心明顯不足；對於立委吳秉叡認為美國期中選舉帶來的非經濟性政治
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E9%80%B2%E5%A0%B4%E8%AD%B7%E7%9B%A4%E9%81%AD%E7%96%91%E7%82%BA%E9%81%B8%E7%A5%A8-%E8%B2%A1%E9%95%B7%E8%8E%8A%E7%BF%A0%E9%9B%B2%EF%BC%9A%E9%9D%9E%E7%B6%93%E6%BF%9F%E5%9B%A0%E7%B4%A0%E6%81%90%E6%85%8C%E6%AE%BA%E7%9B%A4%E7%AC%A6%E5%90%88%E6%A2%9D%E4%BB%B6-023740652.html
- 事件7：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件8：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件9：White House vows to press ahead with tariffs despite midterm backlash over rising prices
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 21:45:46 GMT；台北時間：2026-11-11 05:45
  - 摘要：Business executives warned at a Washington summit of rising costs and shifting supply chains as polls showed growing opposition to Trump's tariffs.
  - 原文連結：https://www.cnbc.com/2026/11/10/trump-tariffs-midterms-gary-cohn-inflation.html
- 事件10：Here's the inflation breakdown for October 2026 — in one chart
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 16:36:40 GMT；台北時間：2026-11-11 00:36
  - 摘要：The consumer price index rose 0.4% in October, a reduction from September but a level economists said is still uncomfortably high.
  - 原文連結：https://www.cnbc.com/2026/11/10/october-2026-cpi-inflation-breakdown.html
- 事件11：10-year Treasury yield races back to 5% as inflation data, Waller comments drive rate hike expectations
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 21:06:07 GMT；台北時間：2026-11-11 05:06
  - 摘要：Treasury yields moved higher after a hotter-than-expected CPI report.
  - 原文連結：https://www.cnbc.com/2026/11/10/us-bonds-treasurys-yields.html
- 事件12：GE Vernova sellers have it all wrong — plus, why Fed rate hike odds are soaring
  - 來源：CNBC；發布時間：Tue, 10 Nov 2026 21:36:13 GMT；台北時間：2026-11-11 05:36
  - 摘要：Every weekday, the Investing Club releases the Homestretch; an actionable afternoon update just in time for the last hour of trading.
  - 原文連結：https://www.cnbc.com/investingclub/2026/11/10/ge-vernova-sellers-have-it-all-wrong-plus-why-fed-rate-hike-odds-are-soaring.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-10

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 42,701 | TAIFEX Proxy |
| 最高價 | 43,108 | TAIFEX Proxy |
| 最低價 | 41,873 | TAIFEX Proxy |
| 收盤價 | 42,623 | TAIFEX Proxy |
| 漲跌點數 | +1,145 | TAIFEX Proxy |
| 漲跌幅 | +2.76 | TAIFEX Proxy |
| 成交量 | 85,124 | TAIFEX Proxy |
| 日盤高點及低點 | 43,108 / 41,873 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 42,503 | TAIFEX Proxy |
| 最高價 | 43,147 | TAIFEX Proxy |
| 最低價 | 42,030 | TAIFEX Proxy |
| 收盤價 | 42,522 | TAIFEX Proxy |
| 漲跌點數 | -124 | TAIFEX Proxy |
| 漲跌幅 | -0.29 | TAIFEX Proxy |
| 成交量 | 56,759 | TAIFEX Proxy |
| 夜盤高點及低點 | 43,147 / 42,030 | TAIFEX Proxy |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,875 | TAIFEX Proxy |
| 外資空方 OI | 113,348 | TAIFEX Proxy |
| 外資多空淨 OI | -103,473 | TAIFEX Proxy |
| 投信多方 OI | 101,353 | TAIFEX Proxy |
| 投信空方 OI | 2,834 | TAIFEX Proxy |
| 投信多空淨 OI | +98,519 | TAIFEX Proxy |
| 自營商多方 OI | 4,909 | TAIFEX Proxy |
| 自營商空方 OI | 4,824 | TAIFEX Proxy |
| 自營商多空淨 OI | +85 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,137 | TAIFEX Proxy |
| 三大法人合計空方 OI | 121,006 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -4,869 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,702 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +2,968 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -941 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,067 | TAIFEX Proxy |
| 前十大交易人空方 OI | 88,625 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +15,442 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-06→2026-11-10) | +6,552 | TAIFEX Proxy snapshots (2026-11-09) |
- 資料日期：2026-11-10 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 86,285 | TAIFEX Proxy |
| 外資日盤空單交易量 | 88,046 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,761 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 32,571 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 32,758 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -187 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,574 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,966 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +2,966 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -996 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -29 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -967 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +209 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -216 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +20.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -19.0 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 42,623 | TAIFEX Proxy |
| 加權指數價格 | 42,711.92 | twse-proxy |
| 台指期與加權指數價差 | -88.92 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | -0.21 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | -88.92 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -101 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 42,623 | 42,522 | +101 | TAIFEX Proxy |
| 成交量 | 85,124 | 56,759 | +28,365 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+325（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 86,285 | 88,046 | -1,761 | 32,571 | 32,758 | -187 | -1,574 | 9,875 | 113,348 | -103,473 | -1,702 | TAIFEX Proxy |
| 投信 | 2,986 | 20 | +2,966 | 0 | 0 | +0 | +2,966 | 101,353 | 2,834 | +98,519 | +2,968 | TAIFEX Proxy |
| 自營商 | 6,096 | 7,092 | -996 | 961 | 990 | -29 | -967 | 4,909 | 4,824 | +85 | -941 | TAIFEX Proxy |
| 三大法人合計 | 95,367 | 95,158 | +209 | 33,532 | 33,748 | -216 | +425 | 116,137 | 121,006 | -4,869 | +325 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 104,067 | TAIFEX Proxy |
| 前十大交易人空方 OI | 88,625 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +15,442 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-06→2026-11-10) | +6,552 | TAIFEX Proxy snapshots (2026-11-09) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 40.00% | TAIFEX Proxy |
| 夜盤漲跌點數 | -124 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -187 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-10 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-11 11:42:49 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 188,915 | TAIFEX Proxy |
| Call 總未平倉量 OI | 76,625 | TAIFEX Proxy |
| Call OI 增減 (2026-11-09→2026-11-10) | +8,528 | TAIFEX Proxy snapshots (2026-11-09) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 222,833 | TAIFEX Proxy |
| Put 總未平倉量 OI | 57,253 | TAIFEX Proxy |
| Put OI 增減 (2026-11-09→2026-11-10) | +25,829 | TAIFEX Proxy snapshots (2026-11-09) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.85 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.34 | TAIFEX Proxy |
| Put／Call Ratio | 0.75 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-09→2026-11-10) | 38.55 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-09→2026-11-10) | 15.35 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 60,395 | TAIFEX Proxy |
| 外資 Call日賣 | 59,918 | TAIFEX Proxy |
| 外資 Call日淨 | +477 | TAIFEX Proxy |
| 外資 Put日買 | 78,228 | TAIFEX Proxy |
| 外資 Put日賣 | 78,334 | TAIFEX Proxy |
| 外資 Put日淨 | -106 | TAIFEX Proxy |
| 外資 Call夜買 | 45,358 | TAIFEX Proxy |
| 外資 Call夜賣 | 46,232 | TAIFEX Proxy |
| 外資 Call夜淨 | -874 | TAIFEX Proxy |
| 外資 Put夜買 | 60,552 | TAIFEX Proxy |
| 外資 Put夜賣 | 59,808 | TAIFEX Proxy |
| 外資 Put夜淨 | +744 | TAIFEX Proxy |
| 外資 日盤淨總量 | +583 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,351 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -850 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 51,660 | TAIFEX Proxy |
| 自營商 Call日賣 | 50,158 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,502 | TAIFEX Proxy |
| 自營商 Put日買 | 57,067 | TAIFEX Proxy |
| 自營商 Put日賣 | 67,615 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,548 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,307 | TAIFEX Proxy |
| 自營商 Call夜賣 | 19,920 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,613 | TAIFEX Proxy |
| 自營商 Put夜買 | 23,322 | TAIFEX Proxy |
| 自營商 Put夜賣 | 28,361 | TAIFEX Proxy |
| 自營商 Put夜淨 | -5,039 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +12,050 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +4,115 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,509 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,841 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,300 | 3,403 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 3,222 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,841 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,841 | 11.54% | TAIFEX Proxy |
| C2 | 48,300 | 3,403 | 4.44% | TAIFEX Proxy |
| C3 | 45,000 | 3,222 | 4.2% | TAIFEX Proxy |
| C4 | 43,000 | 2,493 | 3.25% | TAIFEX Proxy |
| C5 | 44,000 | 2,352 | 3.07% | TAIFEX Proxy |
| C6 | 44,500 | 1,492 | 1.95% | TAIFEX Proxy |
| C7 | 41,000 | 1,453 | 1.9% | TAIFEX Proxy |
| C8 | 43,500 | 1,437 | 1.88% | TAIFEX Proxy |
| C9 | 46,500 | 1,423 | 1.86% | TAIFEX Proxy |
| C10 | 42,000 | 1,374 | 1.79% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 35,700 | 4,187 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 3,546 | TAIFEX Proxy |
| Put OI 第3大履約價 | 38,000 | 2,644 | TAIFEX Proxy |
| Put OI 最大履約價 | 35,700 | 4,187 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 35,700 | 4,187 | 7.31% | TAIFEX Proxy |
| P2 | 40,000 | 3,546 | 6.19% | TAIFEX Proxy |
| P3 | 38,000 | 2,644 | 4.62% | TAIFEX Proxy |
| P4 | 41,000 | 2,192 | 3.83% | TAIFEX Proxy |
| P5 | 37,400 | 2,134 | 3.73% | TAIFEX Proxy |
| P6 | 41,500 | 1,752 | 3.06% | TAIFEX Proxy |
| P7 | 42,000 | 1,651 | 2.88% | TAIFEX Proxy |
| P8 | 39,000 | 1,498 | 2.62% | TAIFEX Proxy |
| P9 | 40,500 | 1,466 | 2.56% | TAIFEX Proxy |
| P10 | 39,500 | 1,077 | 1.88% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 44,000 (+628) | TAIFEX Proxy snapshots (2026-11-09) |
| Call OI 減少最多的履約價 | 48,300 (-443) | TAIFEX Proxy snapshots (2026-11-09) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 35,700 (+2,431) | TAIFEX Proxy snapshots (2026-11-09) |
| Put OI 減少最多的履約價 | 37,400 (-124) | TAIFEX Proxy snapshots (2026-11-09) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-09→2026-11-10) | +0 | TAIFEX Proxy snapshots (2026-11-09) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 35,700 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-09→2026-11-10) | -1,700 | TAIFEX Proxy snapshots (2026-11-09) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-10 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,037.32 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 資料日期 | 2026-11-10 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-09→2026-11-10) | +1,000 | TAIFEX Proxy snapshots (2026-11-09) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 138,729 | 138,146 | +583 | 105,166 | 106,784 | -1,618 | +2,201 | TAIFEX Proxy |
| 投信 | 80 | 0 | +80 | 0 | 0 | +0 | +80 | TAIFEX Proxy |
| 自營商 | 119,275 | 107,225 | +12,050 | 45,668 | 43,242 | +2,426 | +9,624 | TAIFEX Proxy |
| 三大法人合計 | 258,084 | 245,371 | +12,713 | 150,834 | 150,026 | +808 | +11,905 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 18.42 | 18.52 | -0.10 | 9.26 | 9.42 | -0.16 | +0.06 | TAIFEX Proxy |
| 投信 | 0.02 | 0.00 | +0.02 | 0.00 | 0.00 | +0 | +0.02 | TAIFEX Proxy |
| 自營商 | 16.85 | 14.69 | +2.16 | 4.84 | 4.71 | +0.13 | +2.03 | TAIFEX Proxy |
| 三大法人合計 | 35.29 | 33.21 | +2.08 | 14.10 | 14.13 | -0.03 | +2.11 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 21,840 | TAIFEX Proxy |
| 買權空方 OI | 27,346 | TAIFEX Proxy |
| 買權多空淨 OI | -5,506 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-06→2026-11-10) | -213 | TAIFEX Proxy snapshots (2026-11-09) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 13,497 | TAIFEX Proxy |
| 賣權空方 OI | 16,623 | TAIFEX Proxy |
| 賣權多空淨 OI | -3,126 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-06→2026-11-10) | -121 | TAIFEX Proxy snapshots (2026-11-09) |
- 資料日期：買權 2026-11-10／賣權 2026-11-10 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +6,552 | 2026-11-06→2026-11-10 | TAIFEX Proxy snapshots (2026-11-09) |
| 買權前十大 | -213 | 2026-11-06→2026-11-10 | TAIFEX Proxy snapshots (2026-11-09) |
| 賣權前十大 | -121 | 2026-11-06→2026-11-10 | TAIFEX Proxy snapshots (2026-11-09) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-10；資料時間：2026-11-11 11:42:49；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (2)：futures.gamma_wall, futures.gamma_flip
- 註記：futures-price-after-hours 日期 2026-11-10 非今日 2026-11-11，視為無新節次，不採用
- 註記：Gamma Wall/Flip 端點不可用（上游 502），標 unavailable
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
| 外資 | -341.2 | -103,473 | -1,761 | -187 | +583 | -1,618 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +398.9 | +98,519 | +2,966 | +0 | +80 | +0 | 趨勢偏多 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
| 自營商 | -175.4 | +85 | -996 | -29 | +12,050 | +2,426 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
