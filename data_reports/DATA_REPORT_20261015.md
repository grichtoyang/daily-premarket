# DATA_REPORT_20261015

- 報告日期：`2026-10-16`
- T0 交易日期：`2026-10-15`
- 資料產出時間：`2026-10-16 10:33:08`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 46,969.87 | 點 | twse-proxy |
| 開盤 | 48,382.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,382.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 46,795.38 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 46,969.87 | 點 | twse-proxy |
| 漲跌點數 | -1,655.96 | 點 | twse-proxy |
| 漲跌幅 | -3.41 | % | twse-proxy |
| 成交金額 | 14,357.6 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 200 | twse-proxy |
| 下跌家數 | 805 | twse-proxy |
| 平盤家數 | 72 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 21 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 104 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 709 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 59 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 5 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 14 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -3,025.6 | 億元 | twse-proxy /institutional |
| 投信 | +292.8 | 億元 | twse-proxy /institutional |
| 自營商 | -958.2 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -3,691.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,653.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -117.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 262,794 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -1,216 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 191.61 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-14；民間估算；官方無每日序列；gapfill 自動補登) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,496,284 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 33,644 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,713 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 14,357.6 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,445.6 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 16,803.2 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,726.58 | 7.64 | +0.10 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,599.83 | -93.04 | -0.35 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 29,773.76 | -177.06 | -0.59 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,131.01 | 509.53 | +0.99 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 11,441.93 | -242.45 | -2.07 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.67 | -0.20 | -1.19 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 67,744.29 | -33.23 | -0.05 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,008.81 | -26.54 | -0.44 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,062.72 | -251.45 | -1.03 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,707.48 | -59.75 | -1.59 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,816.79 | -293.80 | -2.43 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,778.50 | 8.25 | +0.11 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,019.25 | -163.50 | -0.54 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,423.00 | 565.00 | +1.09 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,770.80 | 25.80 | +0.94 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.82 | 0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.09 | -0.10 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.42 | -0.10 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.38 | 0.27 | +0.85 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.15 | -0.40 | -0.39 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.15 | -0.17 | -0.11 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.24 | 2.93 | +0.22 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 419.73 | -10.27 | -2.39 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 20.66 | -0.74 | -3.46 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 41.49 | -2.84 | -6.40 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 95.96 | 0.87 | +0.91 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,178.80 | 70.90 | +1.73 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 82,201.67 | 639.18 | +0.78 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：00919花了20天填息達陣 近142萬受益人息利雙收
  - 來源：Yahoo 台股；發布時間：2026-10-16T01:59:28Z；台北時間：2026-10-16 09:59
  - 摘要：擁有逾百萬受益人的群益台灣精選高息ETF（00919）第14次除息，今（16）日順利完成盤中填息，本次耗時20天，年化配息率達13.77%。受惠大盤開高，00919早盤以32.5元開出後持續走揚，隨即攀上32.74元填息價位，完成盤中填息；
  - 原文連結：https://tw.stock.yahoo.com/news/00919%E5%A1%AB%E6%81%AF%E4%BA%86%EF%BC%81%E6%AD%B7%E6%99%8220%E5%A4%A9-%E8%BF%91142%E8%90%AC%E6%8A%95%E8%B3%87%E4%BA%BA%E6%81%AF%E5%88%A9%E9%9B%99%E6%94%B6-015928107.html
- 事件2：台郡又亮紅燈、3天暴衝32% 軟板概念股士氣旺
  - 來源：Yahoo 台股；發布時間：2026-10-16T01:44:31Z；台北時間：2026-10-16 09:44
  - 摘要：輝達題材加身「紅燈三連閃」！軟板大廠台郡（6269）在輝達PTFE高速傳輸材料題材續燒下，繼前2日亮燈漲停之後，今天再度在開盤不久即鎖上紅燈，鎖死漲停價82元，三天以來大漲32%，吸引2萬張買單排隊，同樣受惠PTFE題材的台虹（8039）也
  - 原文連結：https://tw.stock.yahoo.com/news/3%E5%A4%A9%E7%8B%82%E5%99%B432%EF%BC%81%E8%BC%9D%E9%81%94%E9%A1%8C%E6%9D%90%E5%8A%A0%E8%BA%AB%E5%8F%B0%E9%83%A1%E5%86%8D%E5%A5%94%E6%BC%B2%E5%81%9C-%E5%8F%B0%E8%99%B9%E7%AD%89%E8%BB%9F%E6%9D%BF%E6%A6%82%E5%BF%B5%E8%82%A1%E5%85%A8%E5%99%B4%E5%87%BA-014431043.html
- 事件3：繼Google後再拚大單 聯發科連7跌止步企圖收復季線
  - 來源：Yahoo 台股；發布時間：2026-10-16T02:05:59Z；台北時間：2026-10-16 10:05
  - 摘要：IC設計龍頭聯發科（2454）傳出接獲字節跳動（TikTok母公司）AI ASIC（客製化晶片）訂單，成為聯發科繼Google之後，第二家大型CSP（雲端服務供應商）客戶，外電報導字節跳動繼與博通（Broadcom）及高通（Qualcomm
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%84%A6%E9%BB%9E%E8%82%A1-%E8%81%AF%E7%99%BC%E7%A7%91-%E6%8E%A5%E7%8D%B2%E5%AD%97%E7%AF%80%E8%B7%B3%E5%8B%95asic%E5%A4%A7%E5%96%AE-%E8%82%A1%E5%83%B9%E7%B5%82%E6%AD%A2%E9%80%A37%E8%B7%8C-020559574.html
- 事件4：玉山金併購效應爆發 稅後淨利大幅攀升總資產破6.6兆
  - 來源：Yahoo 台股；發布時間：2026-10-16T00:20:00Z；台北時間：2026-10-16 08:20
  - 摘要：玉山金控發布併入三商美邦人壽後的首份獲利成果報告。根據其公告的2026年9月自結營運狀況，金控9月單月稅後淨利來到38.1億元，前9月累計稅後淨利則大幅攀升至318.5億元，相比去年同期成長21.54%，推升每股稅後盈餘（EPS）達到1.9
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BD%B5%E8%B3%BC%E6%95%88%E6%87%89%E7%88%86%E7%99%BC-%E7%8E%89%E5%B1%B1%E9%87%91%E5%89%8D%E4%B8%89%E5%AD%A3%E7%8D%B2%E5%88%A9%E7%8B%82%E5%A2%9E21-%E7%B8%BD%E8%B3%87%E7%94%A2%E7%A0%B46-6%E5%85%86%E5%AF%AB%E6%96%B0%E7%AF%87%E7%AB%A0-002000356.html
- 事件5：「瑤池金母」昨加入抄底一張不賣 反手加碼金像電等3檔
  - 來源：Yahoo 台股；發布時間：2026-10-15T16:23:50Z；台北時間：2026-10-16 00:23
  - 摘要：台股今（15）日重挫1655點，指數收在46969點，其中外資更一口氣賣超3025.55億元，創下歷史最大單日賣超紀錄；散戶則是掀起一波抄底潮，資金湧入0050與正2。而由經理人「瑤池金母」陳釧瑤操盤的主動式ETF 00981A，今日也一張
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%91%A4%E6%B1%A0%E9%87%91%E6%AF%8D-%E5%8B%87%E6%95%A2%E6%8A%84%E5%BA%95-%E5%8F%B0%E8%82%A1%E5%A4%A7%E8%B7%8C00981a-%E5%BC%B5%E4%B8%8D%E8%B3%A3-%E5%8F%8D%E6%89%8B%E5%8A%A0%E7%A2%BC-162350378.html
- 事件6：美科技巨頭回穩 台股早盤反彈漲逾250點重返47K
  - 來源：Yahoo 台股；發布時間：2026-10-16T01:16:12Z；台北時間：2026-10-16 09:16
  - 摘要：據《中時新聞網》報導，摩爾投顧分析師林漢偉針對台股後市指出，台股短線有機會出現跌深反彈，主要受到美股科技巨頭股價回穩，以及台指期夜盤上漲493點等因素帶動，電子權值股有望出現止跌訊號。不過，台積電ADR已跌破季線，加上外資大舉賣超現貨、期貨
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1-%E5%8F%B2%E8%A9%A9%E7%B4%9A%E5%B4%A9%E8%B7%8C-%E5%BE%8C%E5%8F%8D%E5%BD%88-%E6%BC%B2%E9%80%BE250%E9%BB%9E%E9%87%8D%E8%BF%9447k-011612697.html
- 事件7：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into the economic condition of American families
  - 來源：Federal Reserve；發布時間：Fri, 9 Oct 2026 14:00:00 GMT；台北時間：2026-10-09 22:00
  - 摘要：Federal Reserve Board releases results of the 2025 Survey of Consumer Finances, which provides the public and policymakers with detailed insights into
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261009a.htm
- 事件8：Economists: Hot PPI shows Fed's work is not done
  - 來源：CNBC；發布時間：Thu, 15 Oct 2026 15:37:59 GMT；台北時間：2026-10-15 23:37
  - 摘要：'We see real risks the Fed will deliver another rate hike in two weeks' time,' one Fedwatcher warns
  - 原文連結：https://www.cnbc.com/2026/10/15/pce-ppi-september-fed-reserve-rate-hike.html
- 事件9：&#x2018;Some people did everything right': I lost my home in the Great Recession. I rent in my 50s. Why is that judged as failure?
  - 來源：MarketWatch；發布時間：Thu, 15 Oct 2026 22:31:00 GMT；台北時間：2026-10-16 06:31
  - 摘要：&#x201d;I earn $110,000 a year.&#x201d;
  - 原文連結：https://www.marketwatch.com/story/i-earn-110-000-a-year-i-lost-my-home-in-the-great-recession-im-renting-in-my-50s-why-is-that-judged-as-failure-d1371d67?mod=mw_rss_topstories
- 事件10：India's rupee forecast to weaken toward 100-per-dollar level even as RBI pushes back
  - 來源：CNBC；發布時間：Fri, 16 Oct 2026 00:54:25 GMT；台北時間：2026-10-16 08:54
  - 摘要：The RBI's latest moves have helped the rupee recover from 96.79 rupees per dollar to the 95-level over recent days.
  - 原文連結：https://www.cnbc.com/2026/10/16/india-rupee-rbi-dollar-iran-war.html
- 事件11：Here's our monthly update on our 32 stocks, including 2 more names to buy
  - 來源：CNBC；發布時間：Thu, 15 Oct 2026 19:08:05 GMT；台北時間：2026-10-16 03:08
  - 摘要：Jim Cramer identified two of his favorite stocks to buy and the names he's not willing to touch just yet.
  - 原文連結：https://www.cnbc.com/investingclub/2026/10/15/heres-our-monthly-update-on-our-32-stocks-including-2-more-names-to-buy.html
- 事件12：Nvidia and Cisco confirm multimillion-dollar donations to Trump's White House ballroom
  - 來源：CNBC；發布時間：Thu, 15 Oct 2026 22:48:12 GMT；台北時間：2026-10-16 06:48
  - 摘要：Big Tech gave millions to Trump's White House ballroom, documents show
  - 原文連結：https://www.cnbc.com/2026/10/15/trump-ballroom-nvidia-cisco-donations.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-15

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 47,716 | TAIFEX Proxy |
| 最高價 | 47,720 | TAIFEX Proxy |
| 最低價 | 46,883 | TAIFEX Proxy |
| 收盤價 | 46,979 | TAIFEX Proxy |
| 漲跌點數 | -1,819 | TAIFEX Proxy |
| 漲跌幅 | -3.73 | TAIFEX Proxy |
| 成交量 | 123,182 | TAIFEX Proxy |
| 日盤高點及低點 | 47,720 / 46,883 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 46,926 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 最高價 | 47,417 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 最低價 | 46,456 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 收盤價 | 47,366 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 漲跌點數 | +435 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 漲跌幅 | +0.93 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 成交量 | 41,283 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 夜盤高點及低點 | 47,417 / 46,456 | 期交所官網盤後行情 (用户截圖補登＋TAIFEX Proxy 10-16 交叉一致） |
| 結算價 | unavailable | TAIFEX Proxy |
| 未平倉量 | unavailable | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,171 | TAIFEX Proxy |
| 外資空方 OI | 106,753 | TAIFEX Proxy |
| 外資多空淨 OI | -97,582 | TAIFEX Proxy |
| 投信多方 OI | 81,728 | TAIFEX Proxy |
| 投信空方 OI | 2,799 | TAIFEX Proxy |
| 投信多空淨 OI | +78,929 | TAIFEX Proxy |
| 自營商多方 OI | 10,619 | TAIFEX Proxy |
| 自營商空方 OI | 3,725 | TAIFEX Proxy |
| 自營商多空淨 OI | +6,894 | TAIFEX Proxy |
| 三大法人合計多方 OI | 101,518 | TAIFEX Proxy |
| 三大法人合計空方 OI | 113,277 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -11,759 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -10,768 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +512 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +4,580 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 81,741 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,670 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,071 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-13→2026-10-15) | -45 | TAIFEX Proxy snapshots (2026-10-14) |
- 資料日期：2026-10-15 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 67,510 | TAIFEX Proxy |
| 外資日盤空單交易量 | 77,347 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -9,837 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 19,698 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 21,801 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -2,103 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -7,734 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +512 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +512 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +4,498 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +872 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +3,626 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -4,827 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,231 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -460.0 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -119.9 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 46,979 | TAIFEX Proxy |
| 加權指數價格 | 46,969.87 | twse-proxy |
| 台指期與加權指數價差 | +9.13 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.02 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +9.13 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +387 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 46,979 | 47,366 | -387 | TAIFEX Proxy |
| 成交量 | 84,911 | 41,283 | +43,628 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-5,676（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 67,510 | 77,347 | -9,837 | 19,698 | 21,801 | -2,103 | -7,734 | 9,171 | 106,753 | -97,582 | -10,768 | TAIFEX Proxy |
| 投信 | 2,783 | 2,271 | +512 | 0 | 0 | +0 | +512 | 81,728 | 2,799 | +78,929 | +512 | TAIFEX Proxy |
| 自營商 | 16,318 | 11,820 | +4,498 | 2,156 | 1,284 | +872 | +3,626 | 10,619 | 3,725 | +6,894 | +4,580 | TAIFEX Proxy |
| 三大法人合計 | 86,611 | 91,438 | -4,827 | 21,854 | 23,085 | -1,231 | -3,596 | 101,518 | 113,277 | -11,759 | -5,676 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 81,741 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,670 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,071 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-13→2026-10-15) | -45 | TAIFEX Proxy snapshots (2026-10-14) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 32.71% | TAIFEX Proxy |
| 夜盤漲跌點數 | +435 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -2,103 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-15 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F3 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-15 23:32:37 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 222,115 | TAIFEX Proxy |
| Call 總未平倉量 OI | 69,146 | TAIFEX Proxy |
| Call OI 增減 (2026-10-14→2026-10-15) | +51,279 | TAIFEX Proxy snapshots (2026-10-14) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 165,368 | TAIFEX Proxy |
| Put 總未平倉量 OI | 33,377 | TAIFEX Proxy |
| Put OI 增減 (2026-10-14→2026-10-15) | +23,370 | TAIFEX Proxy snapshots (2026-10-14) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.34 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.07 | TAIFEX Proxy |
| Put／Call Ratio | 0.48 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-14→2026-10-15) | 14.71 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-14→2026-10-15) | 5.49 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 63,639 | TAIFEX Proxy |
| 外資 Call日賣 | 63,453 | TAIFEX Proxy |
| 外資 Call日淨 | +186 | TAIFEX Proxy |
| 外資 Put日買 | 63,572 | TAIFEX Proxy |
| 外資 Put日賣 | 59,403 | TAIFEX Proxy |
| 外資 Put日淨 | +4,169 | TAIFEX Proxy |
| 外資 Call夜買 | 26,812 | TAIFEX Proxy |
| 外資 Call夜賣 | 26,873 | TAIFEX Proxy |
| 外資 Call夜淨 | -61 | TAIFEX Proxy |
| 外資 Put夜買 | 24,348 | TAIFEX Proxy |
| 外資 Put夜賣 | 24,333 | TAIFEX Proxy |
| 外資 Put夜淨 | +15 | TAIFEX Proxy |
| 外資 日盤淨總量 | -3,983 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +247 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +4,154 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 65,276 | TAIFEX Proxy |
| 自營商 Call日賣 | 66,718 | TAIFEX Proxy |
| 自營商 Call日淨 | -1,442 | TAIFEX Proxy |
| 自營商 Put日買 | 47,834 | TAIFEX Proxy |
| 自營商 Put日賣 | 49,713 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,879 | TAIFEX Proxy |
| 自營商 Call夜買 | 18,262 | TAIFEX Proxy |
| 自營商 Call夜賣 | 21,040 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,778 | TAIFEX Proxy |
| 自營商 Put夜買 | 16,926 | TAIFEX Proxy |
| 自營商 Put夜賣 | 16,819 | TAIFEX Proxy |
| 自營商 Put夜淨 | +107 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +437 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +1,336 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,986 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 49,500 | 5,051 | TAIFEX Proxy |
| Call OI 第2大履約價 | 52,000 | 4,562 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,000 | 3,015 | TAIFEX Proxy |
| Call OI 最大履約價 | 49,500 | 5,051 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 49,500 | 5,051 | 7.3% | TAIFEX Proxy |
| C2 | 52,000 | 4,562 | 6.6% | TAIFEX Proxy |
| C3 | 49,000 | 3,015 | 4.36% | TAIFEX Proxy |
| C4 | 48,000 | 2,970 | 4.3% | TAIFEX Proxy |
| C5 | 50,000 | 2,457 | 3.55% | TAIFEX Proxy |
| C6 | 48,300 | 2,188 | 3.16% | TAIFEX Proxy |
| C7 | 48,200 | 1,775 | 2.57% | TAIFEX Proxy |
| C8 | 48,500 | 1,713 | 2.48% | TAIFEX Proxy |
| C9 | 54,000 | 1,484 | 2.15% | TAIFEX Proxy |
| C10 | 48,800 | 1,193 | 1.73% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 44,500 | 3,763 | TAIFEX Proxy |
| Put OI 第2大履約價 | 46,000 | 1,285 | TAIFEX Proxy |
| Put OI 第3大履約價 | 45,000 | 1,208 | TAIFEX Proxy |
| Put OI 最大履約價 | 44,500 | 3,763 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 44,500 | 3,763 | 11.27% | TAIFEX Proxy |
| P2 | 46,000 | 1,285 | 3.85% | TAIFEX Proxy |
| P3 | 45,000 | 1,208 | 3.62% | TAIFEX Proxy |
| P4 | 47,000 | 1,208 | 3.62% | TAIFEX Proxy |
| P5 | 46,500 | 1,092 | 3.27% | TAIFEX Proxy |
| P6 | 45,500 | 924 | 2.77% | TAIFEX Proxy |
| P7 | 48,000 | 900 | 2.7% | TAIFEX Proxy |
| P8 | 45,400 | 891 | 2.67% | TAIFEX Proxy |
| P9 | 47,300 | 886 | 2.65% | TAIFEX Proxy |
| P10 | 45,300 | 783 | 2.35% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 49,500 (+4,665) | TAIFEX Proxy snapshots (2026-10-14) |
| Call OI 減少最多的履約價 | 50,350 (-58) | TAIFEX Proxy snapshots (2026-10-14) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 44,500 (+2,578) | TAIFEX Proxy snapshots (2026-10-14) |
| Put OI 減少最多的履約價 | 48,500 (-116) | TAIFEX Proxy snapshots (2026-10-14) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 49,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-14→2026-10-15) | +500 | TAIFEX Proxy snapshots (2026-10-14) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 44,500 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-14→2026-10-15) | -4,300 | TAIFEX Proxy snapshots (2026-10-14) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 48,000.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 資料日期 | 2026-10-14 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,426.84 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 資料日期 | 2026-10-14 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 47,350 | TAIFEX Proxy |
| 對應到期月份 | 202610F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-14→2026-10-15) | -1,450 | TAIFEX Proxy snapshots (2026-10-14) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 123,042 | 127,025 | -3,983 | 51,145 | 51,221 | -76 | -3,907 | TAIFEX Proxy |
| 投信 | 3,362 | 8,424 | -5,062 | 0 | 0 | +0 | -5,062 | TAIFEX Proxy |
| 自營商 | 114,989 | 114,552 | +437 | 35,081 | 37,966 | -2,885 | +3,322 | TAIFEX Proxy |
| 三大法人合計 | 241,393 | 250,001 | -8,608 | 86,226 | 89,187 | -2,961 | -5,647 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 11.89 | 12.23 | -0.34 | 4.94 | 4.97 | -0.02 | -0.32 | TAIFEX Proxy |
| 投信 | 0.61 | 5.98 | -5.37 | 0.00 | 0.00 | +0 | -5.37 | TAIFEX Proxy |
| 自營商 | 16.44 | 12.78 | +3.67 | 3.23 | 3.67 | -0.45 | +4.11 | TAIFEX Proxy |
| 三大法人合計 | 28.94 | 30.99 | -2.04 | 8.17 | 8.64 | -0.47 | -1.57 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 22,175 | TAIFEX OpenAPI |
| 買權空方 OI | 25,773 | TAIFEX OpenAPI |
| 買權多空淨 OI | -3,598 | TAIFEX OpenAPI |
| 買權多空淨 OI 變化 (2026-10-13→2026-10-15) | -4,514 | 端點未提供 |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 13,668 | TAIFEX OpenAPI |
| 賣權空方 OI | 12,300 | TAIFEX OpenAPI |
| 賣權多空淨 OI | +1,368 | TAIFEX OpenAPI |
| 賣權多空淨 OI 變化 (2026-10-13→2026-10-15) | +1,042 | 端點未提供 |
- 資料日期：買權 2026-10-15／賣權 2026-10-15 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -45 | 2026-10-13→2026-10-14 | TAIFEX Proxy snapshots (2026-10-14) |
| 買權前十大 | -4,514 | — | 端點未提供 |
| 賣權前十大 | +1,042 | — | 端點未提供 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-15；資料時間：2026-10-16 10:33:08；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：2 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 穩定：183 格新舊皆有值，沿用前版（不再靜默覆寫）
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-15 非今日 2026-10-16，視為無新節次，不採用
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：夜盤 OHLC 手動補登（官網 10-16 盤後終值：開46,926/高47,417/低46,456/收47,366/+435/量41,283；結算價/OI 官網未公布維持 unavailable；原 23:32 快照為前一節次；SOP 3.5）
- 註記：法人夜盤交易拆分 session 歸屬待驗（OHLC 已更正，拆分端點無日期可驗；劇本以外資夜盤-2,103 為準保留）

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-10-14；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-14)，非 T0 2026-10-15
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -3,025.6 | -97,582 | -9,837 | -2,103 | -3,983 | -76 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +292.8 | +78,929 | +512 | +0 | -5,062 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -958.2 | +6,894 | +4,498 | +872 | +437 | -2,885 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
