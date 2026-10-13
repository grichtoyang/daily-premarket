# DATA_REPORT_20261013

- 報告日期：`2026-10-14`
- T0 交易日期：`2026-10-13`
- 資料產出時間：`2026-10-14 02:03:46`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 48,341.31 | 點 | twse-proxy |
| 開盤 | 49,126.27 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,126.27 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,066.36 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 48,341.31 | 點 | twse-proxy |
| 漲跌點數 | -960.65 | 點 | twse-proxy |
| 漲跌幅 | -1.95 | % | twse-proxy |
| 成交金額 | 12,018.6 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 269 | twse-proxy |
| 下跌家數 | 730 | twse-proxy |
| 平盤家數 | 78 | twse-proxy |
| 漲停家數 | 13 | twse-proxy |
| 跌停家數 | 5 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 175 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 610 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 83 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 11 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 8 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,652.9 | 億元 | twse-proxy /institutional |
| 投信 | +246.3 | 億元 | twse-proxy /institutional |
| 自營商 | -569.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,976.4 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,681.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | -135.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 261,127 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 7,332 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 196.16 | % | 前值遞補 (DATA 2026-10-12；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,520,207 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 35,668 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | -1,938 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 12,018.6 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,484.6 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,503.2 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,795.68 | -11.56 | -0.15 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,167.14 | -78.76 | -0.29 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,491.67 | -173.03 | -0.56 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,612.06 | -238.49 | -0.46 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,088.09 | -148.70 | -1.22 | Yahoo Finance Chart API |
| VIX | ^VIX | 15.47 | 0.26 | +1.71 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 69,030.92 | -11.19 | -0.02 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,384.24 | -241.69 | -3.65 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,271.20 | 59.85 | +0.25 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,797.24 | -16.55 | -0.43 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,384.87 | -256.99 | -2.03 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,843.25 | -14.75 | -0.19 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,705.50 | -192.75 | -0.62 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,847.00 | -263.00 | -0.50 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,794.40 | -17.80 | -0.63 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.22 | -0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.57 | -0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.17 | 0.24 | +0.76 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.24 | -0.34 | -0.33 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.35 | 0.29 | +0.18 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,341.28 | -1.71 | -0.13 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 442.65 | -1.70 | -0.38 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 22.18 | -0.36 | -1.62 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.05 | -0.48 | -1.01 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 94.09 | 0.35 | +0.37 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,172.20 | -18.40 | -0.44 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,029.42 | 1,266.86 | +1.55 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：近2千億賣壓砸掉台股960點 台塑化、國泰金逆勢亮紅光
  - 來源：Yahoo 台股；發布時間：2026-10-13T09:08:33Z；台北時間：2026-10-13 17:08
  - 摘要：電子股賣壓沉重，台股重挫960點失守4萬9！今(13)日加權指數終場下跌960.65點、跌幅1.95%，收48,341.31點，成交金額放大至1兆1272.56億元。受國際半導體股走弱與中東局勢升溫影響，盤中一度重挫1235.60點，回測4
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%B8%89%E5%A4%A7%E6%B3%95%E4%BA%BA%E7%A0%8D%E8%BF%912%E5%8D%83%E5%84%84%E5%8F%B0%E8%82%A1%E6%91%94960%E9%BB%9E%E7%97%9B%E5%A4%B149k%EF%BC%81%E5%8F%B0%E5%A1%91%E5%8C%96%E3%80%81%E5%9C%8B%E6%B3%B0%E9%87%91%E6%8F%AA%E5%9C%98%E6%92%90%E4%BD%8F%E7%9B%A4%E9%9D%A2%E7%B4%85%E5%85%89%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090833666.html
- 事件2：金融業「養龍蝦」先看三步驟 金管會提醒4大風險
  - 來源：Yahoo 台股；發布時間：2026-10-13T10:05:39Z；台北時間：2026-10-13 18:05
  - 摘要：AI會有幻覺！AI演進太快，從GAI（聊天式AI）邁入超級助理的AI代理人（Agentic AI）時代，金融業積極導入「養龍蝦」恐爆發四大風險，金管會今（13）日發布安全諮詢文件，以尋求未來達成具共識的安全指引。資訊服務處處長林裕泰今發布「
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%93%94%E5%BF%83%E9%87%91%E8%9E%8D%E6%A5%AD%E3%80%8C%E9%A4%8A%E9%BE%8D%E8%9D%A6%E3%80%8D%E6%81%90%E7%88%864%E5%A4%A7%E9%A2%A8%E9%9A%AA%EF%BC%81%E9%87%91%E7%AE%A1%E6%9C%83%E7%99%BC%E5%B8%83ai%E4%BB%A3%E7%90%86%E4%BA%BA%E5%AE%89%E5%85%A8%E6%8C%87%E5%BC%95-100539818.html
- 事件3：留才工具再+1 外籍員工可參與持股信託擬Q4上路
  - 來源：Yahoo 台股；發布時間：2026-10-13T10:09:02Z；台北時間：2026-10-13 18:09
  - 摘要：為協助企業走向國際化並吸引國外優秀人才，金管會今天(13日)宣布將於近日發布令釋，明定上市櫃公司及其具有控制與從屬關係的企業外籍員工未來都可以參與「員工持股信託」，並預計於今年第四季實施。金管會表示，此舉將可以深化企業與跨國人才的長期夥伴關
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E7%AE%A1%E6%9C%83%E5%AE%A3%E5%B8%83%E7%95%99%E6%89%8D%E5%88%A9%E5%A4%9A-%E5%A4%96%E7%B1%8D%E5%93%A1%E5%B7%A5%E5%8F%AF%E5%8F%83%E8%88%87%E6%8C%81%E8%82%A1%E4%BF%A1%E8%A8%97q4%E4%B8%8A%E8%B7%AF-100902971.html
- 事件4：租金補貼溢領要還錢 國土署曝2.8萬件共4億元追討中
  - 來源：Yahoo 台股；發布時間：2026-10-13T10:08:00Z；台北時間：2026-10-13 18:08
  - 摘要：針對租金補貼溢領爭議，國土署表示截至今年9月底已追回6.6萬餘件共5億元，尚有2.8萬件依法追討中，占整體核定戶約1%。溢領主因多為核定後購屋或退租等資格異動未即時通報，政府提供彈性分期返還機制。未來將擴充數據比對系統與地方合作，從源頭降低
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%94%BF%E5%BA%9C%E4%BE%86%E8%A8%8E%E9%8C%A2%E4%BA%86-%E5%85%A8%E5%8F%B04%E5%84%84%E5%85%83-%E6%B6%89%E5%8F%8A%E4%B8%8A%E8%90%AC%E4%BB%B6-%E4%BE%9D%E6%B3%95%E8%BF%BD%E5%9B%9E%E4%B8%AD-100800628.html
- 事件5：台股ETF高息四強比一比 預估年化配息率逾20%
  - 來源：Yahoo 台股；發布時間：2026-10-13T10:17:33Z；台北時間：2026-10-13 18:17
  - 摘要：【記者柯安聰台北報導】今年來台股漲勢凌厲，以逾70%的漲幅傲視全球股市，人氣滾滾的台股ETF績效也跟著水漲船高，而資本利得的挹注，也讓台股ETF的配息率越配越高。觀察投信ETF的配息概況，以預估年化配...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1etf%E6%AF%94-%E6%AF%94-4%E6%AA%94%E5%B9%B4%E5%8C%96%E9%85%8D%E6%81%AF%E7%8E%87%E9%80%BE20-101733310.html
- 事件6：光通訊台、美股雙殺！「這指標股」跌停摔破3000元、全新、前鼎也亮綠燈　IET、上詮暴跌逾9%、「這封測廠」卻逆勢收紅
  - 來源：Yahoo 台股；發布時間：2026-10-13T10:25:00Z；台北時間：2026-10-13 18:25
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導台股加權指數今（13）日開低走低，盤中一度下殺逾1200點，隨後跌幅收斂，終場收在48341.31點，下跌960.65點，跌幅1.95%，成...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%89%E9%80%9A%E8%A8%8A%E5%8F%B0-%E7%BE%8E%E8%82%A1%E9%9B%99%E6%AE%BA-%E9%80%99%E6%8C%87%E6%A8%99%E8%82%A1-%E8%B7%8C%E5%81%9C%E6%91%94%E7%A0%B43000%E5%85%83-%E5%85%A8%E6%96%B0-102500283.html
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
- 事件11：IMF warns bond yields could see a 'disorderly' spike as debt, inflation risks worsen
  - 來源：CNBC；發布時間：Tue, 13 Oct 2026 04:54:07 GMT；台北時間：2026-10-13 12:54
  - 摘要：The IMF says risks in the government bond market have worsened and that yields could jump sharply and disorderly.
  - 原文連結：https://www.cnbc.com/2026/10/13/treasury-yields-imf-debt-inflation-.html
- 事件12：Paul Tudor Jones is bullish on oil, says it could rally another $20-$25 because of Iran conflict
  - 來源：CNBC；發布時間：Tue, 13 Oct 2026 15:52:09 GMT；台北時間：2026-10-13 23:52
  - 摘要：unavailable
  - 原文連結：https://www.cnbc.com/2026/10/13/paul-tudor-jones-oil-iran.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-13

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,606 | TAIFEX Proxy |
| 最高價 | 48,793 | TAIFEX Proxy |
| 最低價 | 48,240 | TAIFEX Proxy |
| 收盤價 | 48,400 | TAIFEX Proxy |
| 漲跌點數 | -945 | TAIFEX Proxy |
| 漲跌幅 | -1.92 | TAIFEX Proxy |
| 成交量 | 78,260 | TAIFEX Proxy |
| 日盤高點及低點 | 48,793 / 48,240 | TAIFEX Proxy |

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
| 外資多方 OI | 10,640 | TAIFEX Proxy |
| 外資空方 OI | 97,879 | TAIFEX Proxy |
| 外資多空淨 OI | -87,239 | TAIFEX Proxy |
| 投信多方 OI | 80,555 | TAIFEX Proxy |
| 投信空方 OI | 2,717 | TAIFEX Proxy |
| 投信多空淨 OI | +77,838 | TAIFEX Proxy |
| 自營商多方 OI | 5,311 | TAIFEX Proxy |
| 自營商空方 OI | 3,820 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,491 | TAIFEX Proxy |
| 三大法人合計多方 OI | 96,506 | TAIFEX Proxy |
| 三大法人合計空方 OI | 104,416 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,910 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -4,433 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +990 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,344 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,061 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,208 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,853 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-10-08→2026-10-12) | +1,229 | TAIFEX Proxy snapshots (2026-10-12) |
- 資料日期：2026-10-12 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 43,511 | TAIFEX Proxy |
| 外資日盤空單交易量 | 47,878 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,367 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +990 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,194 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,183 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -212.8 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,400 | TAIFEX Proxy |
| 加權指數價格 | 48,341.31 | twse-proxy |
| 台指期與加權指數價差 | +58.69 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.12 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +58.69 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,400 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 58,479 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,099（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 43,511 | 47,878 | -4,367 | unavailable | unavailable | unavailable | unavailable | 10,640 | 97,879 | -87,239 | -4,433 | TAIFEX Proxy |
| 投信 | 1,192 | 202 | +990 | unavailable | unavailable | unavailable | unavailable | 80,555 | 2,717 | +77,838 | +990 | TAIFEX Proxy |
| 自營商 | 9,429 | 8,235 | +1,194 | unavailable | unavailable | unavailable | unavailable | 5,311 | 3,820 | +1,491 | +1,344 | TAIFEX Proxy |
| 三大法人合計 | 54,132 | 56,315 | -2,183 | unavailable | unavailable | unavailable | unavailable | 96,506 | 104,416 | -7,910 | -2,099 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 82,061 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,208 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,853 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-10-08→2026-10-12) | +1,229 | TAIFEX Proxy snapshots (2026-10-12) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | unavailable | TAIFEX Proxy |
| 夜盤漲跌點數 | unavailable | TAIFEX Proxy+twse-proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 劇本分類 | unavailable | 規則對應 |
| 劇本條件 | unavailable | 規則對應 |
| 劇本特徵 | unavailable | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-13 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W2 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-14 02:03:46 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 204,709 | TAIFEX Proxy |
| Call 總未平倉量 OI | 59,595 | TAIFEX Proxy |
| Call OI 增減 (2026-10-12→2026-10-13) | +33,721 | TAIFEX Proxy snapshots (2026-10-12) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 187,837 | TAIFEX Proxy |
| Put 總未平倉量 OI | 35,474 | TAIFEX Proxy |
| Put OI 增減 (2026-10-12→2026-10-13) | +17,812 | TAIFEX Proxy snapshots (2026-10-12) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.09 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.68 | TAIFEX Proxy |
| Put／Call Ratio | 0.60 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-08→2026-10-12) | 15.21 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-08→2026-10-12) | 4.60 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 55,263 | TAIFEX Proxy |
| 外資 Call日賣 | 54,937 | TAIFEX Proxy |
| 外資 Call日淨 | +326 | TAIFEX Proxy |
| 外資 Put日買 | 70,926 | TAIFEX Proxy |
| 外資 Put日賣 | 70,013 | TAIFEX Proxy |
| 外資 Put日淨 | +913 | TAIFEX Proxy |
| 外資 Call夜買 | 22,051 | TAIFEX Proxy |
| 外資 Call夜賣 | 22,463 | TAIFEX Proxy |
| 外資 Call夜淨 | -412 | TAIFEX Proxy |
| 外資 Put夜買 | 18,504 | TAIFEX Proxy |
| 外資 Put夜賣 | 18,397 | TAIFEX Proxy |
| 外資 Put夜淨 | +107 | TAIFEX Proxy |
| 外資 日盤淨總量 | -587 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +738 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +806 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 70,563 | TAIFEX Proxy |
| 自營商 Call日賣 | 65,811 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,752 | TAIFEX Proxy |
| 自營商 Put日買 | 58,294 | TAIFEX Proxy |
| 自營商 Put日賣 | 59,116 | TAIFEX Proxy |
| 自營商 Put日淨 | -822 | TAIFEX Proxy |
| 自營商 Call夜買 | 16,037 | TAIFEX Proxy |
| 自營商 Call夜賣 | 17,065 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,028 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,153 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,847 | TAIFEX Proxy |
| 自營商 Put夜淨 | +1,306 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +5,574 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,780 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -2,128 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 50,500 | 3,690 | TAIFEX Proxy |
| Call OI 第2大履約價 | 49,000 | 2,743 | TAIFEX Proxy |
| Call OI 第3大履約價 | 49,500 | 2,277 | TAIFEX Proxy |
| Call OI 最大履約價 | 50,500 | 3,690 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 50,500 | 3,690 | 6.19% | TAIFEX Proxy |
| C2 | 49,000 | 2,743 | 4.6% | TAIFEX Proxy |
| C3 | 49,500 | 2,277 | 3.82% | TAIFEX Proxy |
| C4 | 52,500 | 2,030 | 3.41% | TAIFEX Proxy |
| C5 | 48,500 | 1,909 | 3.2% | TAIFEX Proxy |
| C6 | 50,000 | 1,818 | 3.05% | TAIFEX Proxy |
| C7 | 49,200 | 1,804 | 3.03% | TAIFEX Proxy |
| C8 | 48,900 | 1,676 | 2.81% | TAIFEX Proxy |
| C9 | 49,100 | 1,600 | 2.68% | TAIFEX Proxy |
| C10 | 48,800 | 1,582 | 2.65% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,000 | 2,116 | TAIFEX Proxy |
| Put OI 第2大履約價 | 47,000 | 1,760 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,500 | 1,561 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,000 | 2,116 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,000 | 2,116 | 5.96% | TAIFEX Proxy |
| P2 | 47,000 | 1,760 | 4.96% | TAIFEX Proxy |
| P3 | 48,500 | 1,561 | 4.4% | TAIFEX Proxy |
| P4 | 47,500 | 1,326 | 3.74% | TAIFEX Proxy |
| P5 | 48,200 | 1,320 | 3.72% | TAIFEX Proxy |
| P6 | 44,500 | 1,319 | 3.72% | TAIFEX Proxy |
| P7 | 48,300 | 1,227 | 3.46% | TAIFEX Proxy |
| P8 | 49,000 | 1,199 | 3.38% | TAIFEX Proxy |
| P9 | 48,400 | 1,082 | 3.05% | TAIFEX Proxy |
| P10 | 47,800 | 990 | 2.79% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 50,500 (+2,870) | TAIFEX Proxy snapshots (2026-10-12) |
| Call OI 減少最多的履約價 | 48,200 (-454) | TAIFEX Proxy snapshots (2026-10-12) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 47,000 (+1,206) | TAIFEX Proxy snapshots (2026-10-12) |
| Put OI 減少最多的履約價 | 46,200 (-60) | TAIFEX Proxy snapshots (2026-10-12) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 50,500 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-12→2026-10-13) | -2,900 | TAIFEX Proxy snapshots (2026-10-12) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-12→2026-10-13) | -1,350 | TAIFEX Proxy snapshots (2026-10-12) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 49,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 資料日期 | 2026-10-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 48,946.81 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 資料日期 | 2026-10-12 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,450 | TAIFEX Proxy |
| 對應到期月份 | 202610W2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-12→2026-10-13) | -800 | TAIFEX Proxy snapshots (2026-10-12) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 125,276 | 125,863 | -587 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 3,270 | 3,500 | -230 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 129,679 | 124,105 | +5,574 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 258,225 | 253,468 | +4,757 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.50 | 9.47 | +0.04 | 3.28 | 3.35 | -0.07 | +0.10 | TAIFEX Proxy |
| 投信 | 0.76 | 2.74 | -1.99 | 0.00 | 0.00 | +0 | -1.99 | TAIFEX Proxy |
| 自營商 | 11.17 | 9.97 | +1.21 | 1.80 | 2.30 | -0.50 | +1.71 | TAIFEX Proxy |
| 三大法人合計 | 21.43 | 22.18 | -0.74 | 5.08 | 5.65 | -0.57 | -0.17 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 13,946 | TAIFEX Proxy |
| 買權空方 OI | 12,731 | TAIFEX Proxy |
| 買權多空淨 OI | +1,215 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-10-08→2026-10-12) | -307 | TAIFEX Proxy snapshots (2026-10-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,922 | TAIFEX Proxy |
| 賣權空方 OI | 10,928 | TAIFEX Proxy |
| 賣權多空淨 OI | -6 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-10-08→2026-10-12) | -100 | TAIFEX Proxy snapshots (2026-10-12) |
- 資料日期：買權 2026-10-12／賣權 2026-10-12 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +1,229 | 2026-10-08→2026-10-12 | TAIFEX Proxy snapshots (2026-10-12) |
| 買權前十大 | -307 | 2026-10-08→2026-10-12 | TAIFEX Proxy snapshots (2026-10-12) |
| 賣權前十大 | -100 | 2026-10-08→2026-10-12 | TAIFEX Proxy snapshots (2026-10-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-13；資料時間：2026-10-14 02:03:46；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-10-13 非今日 2026-10-14，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-10-13 非今日 2026-10-14，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-10-13 非今日 2026-10-14，視為無新節次，不採用
- 註記：Gamma 資料日期 2026-10-12 (T0 2026-10-13 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-10-12 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-10-12；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-12)，非 T0 2026-10-13
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,652.9 | -87,239 | -4,367 | unavailable | -587 | unavailable | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +246.3 | +77,838 | +990 | unavailable | -230 | unavailable | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -569.8 | +1,491 | +1,194 | unavailable | +5,574 | unavailable | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
