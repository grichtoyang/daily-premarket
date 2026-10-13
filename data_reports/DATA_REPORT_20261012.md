# DATA_REPORT_20261012

- 報告日期：`2026-10-13`
- T0 交易日期：`2026-10-12`
- 資料產出時間：`2026-10-13 08:25:14`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,301.96 | 點 | twse-proxy |
| 開盤 | 49,272.08 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,412.90 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,768.82 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,301.96 | 點 | twse-proxy |
| 漲跌點數 | -11.48 | 點 | twse-proxy |
| 漲跌幅 | -0.02 | % | twse-proxy |
| 成交金額 | 8,945.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 538 | twse-proxy |
| 下跌家數 | 451 | twse-proxy |
| 平盤家數 | 86 | twse-proxy |
| 漲停家數 | 25 | twse-proxy |
| 跌停家數 | 2 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 330 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 467 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 71 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 28 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 10 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -522.0 | 億元 | twse-proxy /institutional |
| 投信 | +71.4 | 億元 | twse-proxy /institutional |
| 自營商 | -142.9 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -593.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,816.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +73.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 253,795 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 1,442 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 197.12 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-08；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,518,681 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,606 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -2,801 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,945.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,201.8 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,147.0 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,807.24 | -4.30 | -0.06 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,245.90 | -120.27 | -0.44 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,664.70 | -218.45 | -0.71 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,850.55 | 195.60 | +0.38 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,236.79 | -335.63 | -2.67 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.21 | 0.37 | +2.49 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 67,458.00 | -1,572.92 | -2.28 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,136.79 | -489.14 | -7.38 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,211.35 | 425.56 | +1.79 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,813.79 | 1.89 | +0.05 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,641.86 | 20.96 | +0.17 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,851.75 | -8.00 | -0.10 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,805.75 | -303.00 | -0.97 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,144.00 | 218.00 | +0.42 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,810.30 | -11.80 | -0.42 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.24 | -0.00 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.60 | -0.00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.92 | -0.00 | -0.00 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.55 | 0.34 | +0.33 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.46 | 0.40 | +0.25 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,334.67 | -8.32 | -0.62 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 453.31 | -4.68 | -1.02 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 22.96 | 0.14 | +0.61 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 46.43 | 1.17 | +2.59 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 92.98 | 1.13 | +1.23 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,189.20 | -27.10 | -0.64 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 81,346.55 | -2,332.92 | -2.79 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：337調查利空下險守49K 大立光揪金融海運當台股救生圈
  - 來源：Yahoo 台股；發布時間：2026-10-12T08:56:04Z；台北時間：2026-10-12 16:56
  - 摘要：金融、航運聯手救場，台股守住4萬9千點！今(12)日加權指數終場小跌11.48點、跌幅0.02%，收49,301.96點，成交金額8457.49億元。早盤受費半走弱、美國337專利調查及中東局勢升溫影響，一度重挫逾500點，隨後買盤進場拉抬
  - 原文連結：https://tw.stock.yahoo.com/news/337%E8%AA%BF%E6%9F%A5%E7%BD%A9%E9%A0%82%E5%8F%B0%E8%82%A1%E5%B0%BE%E7%9B%A4%E7%BF%BB%E9%BB%91%E5%AE%88%E4%BD%8F49k%EF%BC%81%E5%A4%A7%E7%AB%8B%E5%85%89%E4%BA%AE%E7%87%88%E7%95%B6%E9%9D%A0%E5%B1%B1-%E9%87%91%E8%9E%8D%E3%80%81%E6%B5%B7%E9%81%8B%E7%95%B6%E6%95%91%E6%8F%B4%E5%A4%A7%E9%9A%8A%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085604179.html
- 事件2：4.3萬股東等不到復牌 永冠-KY確定11/18下市
  - 來源：Yahoo 台股；發布時間：2026-10-12T10:25:20Z；台北時間：2026-10-12 18:25
  - 摘要：證交所今（12）日公告，離岸風電鑄件大廠永冠-KY（1589）因財報難產遭停止買賣滿 6 個月仍無法補正，已觸及強制下市規定，確定將於11月18日下市，根據最新統計，目前仍有逾 4.3 萬名股東受困，手中股票恐面臨淪為壁紙的危機。
  - 原文連結：https://tw.stock.yahoo.com/news/43%E8%90%AC%E8%82%A1%E6%9D%B1%E8%82%A1%E7%A5%A8%E5%B0%87%E6%B7%AA%E5%A3%81%E7%B4%99%EF%BC%81%E8%AD%89%E4%BA%A4%E6%89%80%EF%BC%9A%E6%B0%B8%E5%86%A0-ky-%E7%A2%BA%E5%AE%9A-1118-%E4%B8%8B%E5%B8%82-102539713.html
- 事件3：00878人氣大逆襲 月增2.45萬人擠下0056奪亞軍
  - 來源：Yahoo 台股；發布時間：2026-10-12T08:53:52Z；台北時間：2026-10-12 16:53
  - 摘要：證券交易所最新公布 9 月台股定期定額交易戶數統計，前 20 大人氣王出現顯著洗牌！國泰永續高股息（00878）單月暴增 2.45 萬人，榮登「單月吸金王」；這也是 00878 歷經 10 個月的沉潛後，成功擠下元大高股息（0056），強勢
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%909%E6%9C%88etf%E5%AE%9A%E6%9C%9F%E5%AE%9A%E9%A1%8D%E9%A2%A8%E9%9B%B2%E6%A6%9C%E3%80%91%E7%9D%BD%E9%81%9510%E5%80%8B%E6%9C%88%E6%93%A0%E6%8E%890056%EF%BC%81008781%E5%80%8B%E6%9C%88%E7%8B%82%E5%90%B8-245%E8%90%AC%E4%BA%BA-%E9%87%8D%E8%BF%94%E4%BA%BA%E6%B0%A3%E4%BA%9E%E8%BB%8D-085748897.html
- 事件4：輝達RTX5090傳停產惹議 若成真價格恐更難降
  - 來源：Yahoo 台股；發布時間：2026-10-12T10:09:00Z；台北時間：2026-10-12 18:09
  - 摘要：[FTNN新聞網]記者吳欣穎／綜合報導輝達（NVIDIA）最強遊戲顯示卡RTX5090傳出停產消息，根據硬體爆料人士MEGAsizeGPU透露，輝達可能將原本用於RTX5090的高階晶...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%AB%98%E9%9A%8E%E6%99%B6%E7%89%87%E4%B8%8D%E5%A4%A0%E5%88%86-%E8%BC%9D%E9%81%94rtx-5090%E5%82%B3%E5%81%9C%E7%94%A2-gb202%E6%99%B6%E7%89%87%E7%88%86%E5%84%AA%E5%85%88%E4%BE%9B%E6%87%89%E4%BC%81%E6%A5%AD%E7%AB%AF-100900306.html
- 事件5：外館系統疑混中國原始碼 3家科技公司捲採購案調查
  - 來源：Yahoo 台股；發布時間：2026-10-12T15:00:34Z；台北時間：2026-10-12 23:00
  - 摘要：[NOWNEWS今日新聞]外交部多處駐外館處的資訊資產管理系統疑似含有中國原始碼，台北地檢署指揮調查局新北市調查處追查後，懷疑安和科技透過其他公司名義投標、修改軟體介面等方式取得採購案，3年標案金額合...
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%AD%E5%9C%8B%E5%8E%9F%E5%A7%8B%E7%A2%BC%E5%85%A5%E4%BE%B5%E8%B3%87%E5%AE%89%E7%B3%BB%E7%B5%B1-3%E5%AE%B6%E7%A7%91%E6%8A%80%E5%85%AC%E5%8F%B8%E6%8D%B2%E5%85%A5-095121074.html
- 事件6：PCB被盯上！投信退貨「這4檔」3千多張　連砍欣興5刀帶走68.80億元
  - 來源：Yahoo 台股；發布時間：2026-10-12T11:30:00Z；台北時間：2026-10-12 19:30
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導台股加權指數今（12）日收在49301.96點，下跌11.48點，跌幅0.02%，成交量達8457億元。根據證交所資料，投信買超71.23億元，...
  - 原文連結：https://tw.stock.yahoo.com/news/pcb%E8%A2%AB%E7%9B%AF%E4%B8%8A-%E6%8A%95%E4%BF%A1%E9%80%80%E8%B2%A8-%E9%80%994%E6%AA%94-3%E5%8D%83%E5%A4%9A%E5%BC%B5-%E9%80%A3%E7%A0%8D%E6%AC%A3%E8%88%885%E5%88%80%E5%B8%B6%E8%B5%B068-113000337.html
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
- 事件10：Rep. Ilhan Omar blasts federal criminal raid on home: 'I will not be silenced'
  - 來源：CNBC；發布時間：Mon, 12 Oct 2026 18:29:28 GMT；台北時間：2026-10-13 02:29
  - 摘要：The Minnesota Democrat, a Muslim who was born in Somalia, has been targeted for criticism in the past by President Donald Trump.
  - 原文連結：https://www.cnbc.com/2026/10/12/ilhan-omar-home-raided-dhs-immigration-investigation.html
- 事件11：Higher rates could be needed to avoid 'inflationary mindset' taking hold, says Fed's Hammack
  - 來源：CNBC；發布時間：Mon, 12 Oct 2026 17:15:21 GMT；台北時間：2026-10-13 01:15
  - 摘要：The Cleveland Fed president said that tighter monetary policy would be needed to bring down inflation.
  - 原文連結：https://www.cnbc.com/2026/10/12/beth-hammack-fed-inflation-policy.html
- 事件12：Inflation likely peaked for 2026 but will remain sticky, according to prediction markets
  - 來源：CNBC；發布時間：Mon, 12 Oct 2026 15:37:26 GMT；台北時間：2026-10-12 23:37
  - 摘要：Traders think there's little chance core inflation, which excludes food and energy prices, will fall to 2.2% this year.
  - 原文連結：https://www.cnbc.com/2026/10/12/inflation-will-remain-sticky-in-2026-according-to-prediction-markets.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-12

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,975 | TAIFEX Proxy |
| 最高價 | 49,594 | TAIFEX Proxy |
| 最低價 | 48,910 | TAIFEX Proxy |
| 收盤價 | 49,309 | TAIFEX Proxy |
| 漲跌點數 | -48 | TAIFEX Proxy |
| 漲跌幅 | -0.10 | TAIFEX Proxy |
| 成交量 | 83,737 | TAIFEX Proxy |
| 日盤高點及低點 | 49,594 / 48,910 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,275 | TAIFEX Proxy |
| 最高價 | 49,422 | TAIFEX Proxy |
| 最低價 | 48,881 | TAIFEX Proxy |
| 收盤價 | 48,946 | TAIFEX Proxy |
| 漲跌點數 | -399 | TAIFEX Proxy |
| 漲跌幅 | -0.81 | TAIFEX Proxy |
| 成交量 | 19,781 | TAIFEX Proxy |
| 夜盤高點及低點 | 49,422 / 48,881 | TAIFEX Proxy |
| 結算價 | 49,345 | TAIFEX Proxy |
| 未平倉量 | 106,900 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,899 | TAIFEX Proxy |
| 外資空方 OI | 94,705 | TAIFEX Proxy |
| 外資多空淨 OI | -82,806 | TAIFEX Proxy |
| 投信多方 OI | 79,560 | TAIFEX Proxy |
| 投信空方 OI | 2,712 | TAIFEX Proxy |
| 投信多空淨 OI | +76,848 | TAIFEX Proxy |
| 自營商多方 OI | 4,783 | TAIFEX Proxy |
| 自營商空方 OI | 4,636 | TAIFEX Proxy |
| 自營商多空淨 OI | +147 | TAIFEX Proxy |
| 三大法人合計多方 OI | 96,242 | TAIFEX Proxy |
| 三大法人合計空方 OI | 102,053 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,811 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +388 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +509 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +681 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,609 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,985 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,624 | TAIFEX Proxy |
| 多空淨 OI 變化 | -2,918 | TAIFEX Proxy snapshots (2026-10-08) |
- 資料日期：unavailable (TypeOfTraders=0 全部交易人；契約月份 unavailable)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 47,775 | TAIFEX Proxy |
| 外資日盤空單交易量 | 47,132 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +643 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 10,314 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 11,428 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,114 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,757 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +509 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +509 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +667 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +221 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +446 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,819 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -893 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +177.6 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -87.8 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 49,309 | TAIFEX Proxy |
| 加權指數價格 | 49,301.96 | twse-proxy |
| 台指期與加權指數價差 | +7.04 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.01 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +7.04 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -363 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 49,309 | 48,946 | +363 | TAIFEX Proxy |
| 成交量 | 44,296 | 19,781 | +24,515 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,578（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 47,775 | 47,132 | +643 | 10,314 | 11,428 | -1,114 | +1,757 | 11,899 | 94,705 | -82,806 | +388 | TAIFEX Proxy |
| 投信 | 2,063 | 1,554 | +509 | 0 | 0 | +0 | +509 | 79,560 | 2,712 | +76,848 | +509 | TAIFEX Proxy |
| 自營商 | 5,473 | 4,806 | +667 | 776 | 555 | +221 | +446 | 4,783 | 4,636 | +147 | +681 | TAIFEX Proxy |
| 三大法人合計 | 55,311 | 53,492 | +1,819 | 11,090 | 11,983 | -893 | +2,712 | 96,242 | 102,053 | -5,811 | +1,578 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,609 | TAIFEX Proxy |
| 前十大交易人空方 OI | 77,985 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,624 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | -2,918 | TAIFEX Proxy snapshots (2026-10-08) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 30.87% | TAIFEX Proxy |
| 夜盤漲跌點數 | -399 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,114 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-12 | TAIFEX Proxy |
| 到期月份／到期日 | 202610F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-13 08:25:14 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 280,654 | TAIFEX Proxy |
| Call 總未平倉量 OI | 54,429 | TAIFEX Proxy |
| Call OI 增減 (2026-10-08→2026-10-12) | +12,161 | TAIFEX Proxy snapshots (2026-10-08) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 295,175 | TAIFEX Proxy |
| Put 總未平倉量 OI | 54,199 | TAIFEX Proxy |
| Put OI 增減 (2026-10-08→2026-10-12) | +27,438 | TAIFEX Proxy snapshots (2026-10-08) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.95 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.00 | TAIFEX Proxy |
| Put／Call Ratio | 1.00 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-08→2026-10-12) | 15.21 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-08→2026-10-12) | 4.60 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 95,635 | TAIFEX Proxy |
| 外資 Call日賣 | 95,307 | TAIFEX Proxy |
| 外資 Call日淨 | +328 | TAIFEX Proxy |
| 外資 Put日買 | 105,662 | TAIFEX Proxy |
| 外資 Put日賣 | 111,299 | TAIFEX Proxy |
| 外資 Put日淨 | -5,637 | TAIFEX Proxy |
| 外資 Call夜買 | 22,051 | TAIFEX Proxy |
| 外資 Call夜賣 | 22,463 | TAIFEX Proxy |
| 外資 Call夜淨 | -412 | TAIFEX Proxy |
| 外資 Put夜買 | 18,504 | TAIFEX Proxy |
| 外資 Put夜賣 | 18,397 | TAIFEX Proxy |
| 外資 Put夜淨 | +107 | TAIFEX Proxy |
| 外資 日盤淨總量 | +5,965 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +740 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -5,744 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 90,212 | TAIFEX Proxy |
| 自營商 Call日賣 | 92,681 | TAIFEX Proxy |
| 自營商 Call日淨 | -2,469 | TAIFEX Proxy |
| 自營商 Put日買 | 96,811 | TAIFEX Proxy |
| 自營商 Put日賣 | 95,561 | TAIFEX Proxy |
| 自營商 Put日淨 | +1,250 | TAIFEX Proxy |
| 自營商 Call夜買 | 16,037 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,065 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,028 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,153 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,847 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,306 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -3,719 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -1,441 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -56 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 53,400 | 3,632 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,400 | 3,228 | TAIFEX Proxy |
| Call OI 第3大履約價 | 50,000 | 2,417 | TAIFEX Proxy |
| Call OI 最大履約價 | 53,400 | 3,632 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 53,400 | 3,632 | 6.67% | TAIFEX Proxy |
| C2 | 49,400 | 3,228 | 5.93% | TAIFEX Proxy |
| C3 | 50,000 | 2,417 | 4.44% | TAIFEX Proxy |
| C4 | 49,500 | 2,143 | 3.94% | TAIFEX Proxy |
| C5 | 53,000 | 1,757 | 3.23% | TAIFEX Proxy |
| C6 | 49,200 | 1,690 | 3.1% | TAIFEX Proxy |
| C7 | 51,200 | 1,652 | 3.04% | TAIFEX Proxy |
| C8 | 49,300 | 1,609 | 2.96% | TAIFEX Proxy |
| C9 | 49,350 | 1,553 | 2.85% | TAIFEX Proxy |
| C10 | 49,900 | 1,507 | 2.77% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,350 | 3,520 | TAIFEX Proxy |
| Put OI 第2大履約價 | 49,200 | 3,425 | TAIFEX Proxy |
| Put OI 第3大履約價 | 49,000 | 3,299 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,350 | 3,520 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,350 | 3,520 | 6.49% | TAIFEX Proxy |
| P2 | 49,200 | 3,425 | 6.32% | TAIFEX Proxy |
| P3 | 49,000 | 3,299 | 6.09% | TAIFEX Proxy |
| P4 | 49,300 | 3,247 | 5.99% | TAIFEX Proxy |
| P5 | 49,100 | 2,832 | 5.23% | TAIFEX Proxy |
| P6 | 48,900 | 2,228 | 4.11% | TAIFEX Proxy |
| P7 | 49,150 | 2,189 | 4.04% | TAIFEX Proxy |
| P8 | 49,250 | 2,035 | 3.75% | TAIFEX Proxy |
| P9 | 48,700 | 1,983 | 3.66% | TAIFEX Proxy |
| P10 | 48,800 | 1,968 | 3.63% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 49,400 (+2,612) | TAIFEX Proxy snapshots (2026-10-08) |
| Call OI 減少最多的履約價 | 50,400 (-869) | TAIFEX Proxy snapshots (2026-10-08) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,350 (+3,282) | TAIFEX Proxy snapshots (2026-10-08) |
| Put OI 減少最多的履約價 | 46,800 (-393) | TAIFEX Proxy snapshots (2026-10-08) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 53,400 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-08→2026-10-12) | +0 | TAIFEX Proxy snapshots (2026-10-08) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,350 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-08→2026-10-12) | +350 | TAIFEX Proxy snapshots (2026-10-08) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 49,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,946.81 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 資料日期 | 2026-10-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 49,250 | TAIFEX Proxy |
| 對應到期月份 | 202610F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-08→2026-10-12) | +50 | TAIFEX Proxy snapshots (2026-10-08) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 206,934 | 200,969 | +5,965 | 40,448 | 40,967 | -519 | +6,484 | TAIFEX Proxy |
| 投信 | 0 | 5,030 | -5,030 | 0 | 0 | +0 | -5,030 | TAIFEX Proxy |
| 自營商 | 185,773 | 189,492 | -3,719 | 28,884 | 31,218 | -2,334 | -1,385 | TAIFEX Proxy |
| 三大法人合計 | 392,707 | 395,491 | -2,784 | 69,332 | 72,185 | -2,853 | +69 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.78 | 9.36 | +0.41 | 3.28 | 3.35 | -0.07 | +0.48 | TAIFEX Proxy |
| 投信 | 0.00 | 3.78 | -3.78 | 0.00 | 0.00 | +0 | -3.78 | TAIFEX Proxy |
| 自營商 | 12.81 | 10.14 | +2.66 | 1.80 | 2.30 | -0.50 | +3.17 | TAIFEX Proxy |
| 三大法人合計 | 22.58 | 23.28 | -0.70 | 5.08 | 5.65 | -0.57 | -0.13 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,045 | TAIFEX Proxy |
| 買權空方 OI | 12,523 | TAIFEX Proxy |
| 買權多空淨 OI | +1,522 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | -185 | TAIFEX Proxy snapshots (2026-10-08) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,630 | TAIFEX Proxy |
| 賣權空方 OI | 10,536 | TAIFEX Proxy |
| 賣權多空淨 OI | +94 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | +47 | TAIFEX Proxy snapshots (2026-10-08) |
- 資料日期：買權 unavailable／賣權 unavailable (TypeOfTraders=0 全部交易人；契約月份 unavailable)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -2,918 | — | TAIFEX Proxy snapshots (2026-10-08) |
| 買權前十大 | -185 | — | TAIFEX Proxy snapshots (2026-10-08) |
| 賣權前十大 | +47 | — | TAIFEX Proxy snapshots (2026-10-08) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-12；資料時間：2026-10-13 08:25:14；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 註記：同 T0 保護：21 格沿用前版有值（本次抓取缺失不覆寫）
- 未取得欄位 (2)：futures.top10_change, options.top10_change
- 註記：futures-price-after-hours 日期 2026-10-12 非今日 2026-10-13，視為無新節次，不採用
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
- margin_ratio：`wantgoo 大盤融資維持率 (資料日期 2026-10-08；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率資料日期 2026-10-08 (T0 2026-10-12 尚無，採最新可得)
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -522.0 | -82,806 | +643 | -1,114 | +5,965 | -519 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +71.4 | +76,848 | +509 | +0 | -5,030 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -142.9 | +147 | +667 | +221 | -3,719 | -2,334 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
