# DATA_REPORT_20261113

- 報告日期：`2026-11-14`
- T0 交易日期：`2026-11-13`
- 資料產出時間：`2026-11-14 02:21:19`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`evening`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 43,675.12 | 點 | twse-proxy |
| 開盤 | 43,719.75 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 44,489.48 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 43,534.12 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 43,675.12 | 點 | twse-proxy |
| 漲跌點數 | 583.25 | 點 | twse-proxy |
| 漲跌幅 | +1.35 | % | twse-proxy |
| 成交金額 | 9,515.8 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 811 | twse-proxy |
| 下跌家數 | 199 | twse-proxy |
| 平盤家數 | 74 | twse-proxy |
| 漲停家數 | 28 | twse-proxy |
| 跌停家數 | 3 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 584 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 230 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 62 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 41 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +288.4 | 億元 | twse-proxy /institutional |
| 投信 | +95.4 | 億元 | twse-proxy /institutional |
| 自營商 | +68.9 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +452.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,086.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +50.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 245,881 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | -589 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 170.70 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,491,973 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 37,108 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 1,160 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,515.8 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,183.5 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,699.3 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,537.85 | -54.55 | -0.72 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 25,059.44 | -306.65 | -1.21 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,826.44 | -462.75 | -1.64 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 52,229.20 | -67.89 | -0.13 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 10,040.44 | -466.23 | -4.44 | Yahoo Finance Chart API |
| VIX | ^VIX | 19.81 | 1.11 | +5.94 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 60,819.36 | -429.23 | -0.70 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,342.73 | -32.63 | -0.61 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,008.55 | -307.37 | -1.26 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,655.83 | -24.81 | -0.67 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,197.98 | -191.76 | -1.68 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,553.00 | -62.25 | -0.82 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,879.00 | -505.50 | -1.78 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 52,283.00 | -107.00 | -0.20 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,785.80 | -21.50 | -0.77 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.86 | 0.13 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.14 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | 0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.86 | 0.00 | +0.01 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.37 | 0.20 | +0.20 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.59 | -0.15 | -0.09 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,336.57 | 0.31 | +0.02 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 396.23 | -9.26 | -2.28 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 15.31 | -0.45 | -2.89 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 35.25 | -1.04 | -2.87 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 88.77 | 0.03 | +0.03 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,886.10 | 0.80 | +0.02 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 68,885.62 | -2,457.35 | -3.44 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：「黃天鵝」沒壓倒台股 聯發科扛大旗創意超車川湖戴后冠
  - 來源：Yahoo 台股；發布時間：2026-11-13T08:59:02Z；台北時間：2026-11-13 16:59
  - 摘要：台股反彈583點，周線終結連四黑大漲近4千點！今(13)日加權指數終場上漲583.25點、漲幅1.35%，收43675.12點，單周大漲3973.48點，上市成交金額9177.54億元。盤中一度強彈近1400點、收復4萬4千點，隨後漲幅收斂
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E9%96%83%E9%81%8E%E3%80%8C%E9%BB%83%E5%A4%A9%E9%B5%9D%E3%80%8D%E5%BC%B7%E5%BD%88%EF%BC%81%E5%91%A8%E7%B7%9A%E7%B5%82%E6%AD%A2%E9%80%A3%E5%9B%9B%E9%BB%91%E5%A4%A7%E6%BC%B23973%E9%BB%9E-%E8%81%AF%E7%99%BC%E7%A7%91%E5%BC%B7%E6%94%BB%E9%A0%98asic%E8%A1%9D%E9%8B%92-%E5%89%B5%E6%84%8F%E8%B6%85%E8%BB%8A%E5%B7%9D%E6%B9%96%E9%A6%96%E7%99%BB%E8%82%A1%E5%90%8E%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-085902124.html
- 事件2：想抱股10年！「0050 vs. 0052」怎選 網推這檔：永遠火車頭
  - 來源：Yahoo 台股；發布時間：2026-11-13T11:15:00Z；台北時間：2026-11-13 19:15
  - 摘要：元大台灣50（0050）與富邦科技（0052）都是投資新手青睞的熱門標的。一名剛開證券戶的網友表示，打算定期定額長期投資10年，不知二者該如何選擇，引發討論。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%83%B3%E6%8A%B1%E8%82%A110%E5%B9%B4-0050-vs-0052-%E6%80%8E%E9%81%B8-111500414.html
- 事件3：光電股盤面紅通通！「這4檔」齊亮紅燈、友達股價站回3字頭　大立光噴半根、冠西電止步連4漲停墜至跌停
  - 來源：Yahoo 台股；發布時間：2026-11-13T10:45:00Z；台北時間：2026-11-13 18:45
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導輝達執行長黃仁勳昨（12）日宣布辭去三大要職震撼市場，美股四大指數全數收黑，然而，台股加權指數今（13）日未明顯受影響...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%89%E9%9B%BB%E8%82%A1%E7%9B%A4%E9%9D%A2%E7%B4%85%E9%80%9A%E9%80%9A-%E9%80%994%E6%AA%94-%E9%BD%8A%E4%BA%AE%E7%B4%85%E7%87%88-%E5%8F%8B%E9%81%94%E8%82%A1%E5%83%B9%E7%AB%99%E5%9B%9E3%E5%AD%97%E9%A0%AD-%E5%A4%A7%E7%AB%8B%E5%85%89%E5%99%B4%E5%8D%8A%E6%A0%B9-104500682.html
- 事件4：他四貸同堂買「這檔」！ 狂賺4727萬不願賣 網勸：見好就收
  - 來源：Yahoo 台股；發布時間：2026-11-13T09:13:00Z；台北時間：2026-11-13 17:13
  - 摘要：高槓桿融資操作向來伴隨巨大風險，但當精準押中千金飆股時，所創造的財富爆發力卻令人瞠目結舌。近日有網友曬出自己融資買進14張創意（3443）的對帳單，帳面狂賺高達4727萬元，他不僅拒絕獲利了結，更喊出目標價14000元並自嘲已四貸同堂，引爆
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BB%96%E5%9B%9B%E8%B2%B8%E5%90%8C%E5%A0%82%E8%B2%B7-%E9%80%99%E6%AA%94-%E7%8B%82%E8%B3%BA4727%E8%90%AC%E4%B8%8D%E9%A1%98%E8%B3%A3-%E7%B6%B2%E5%8B%B8-%E8%A6%8B%E5%A5%BD%E5%B0%B1%E6%94%B6-091300251.html
- 事件5：光通訊股也閃紅光！「這檔」另握衛星題材猛飆漲停、光聖噴半根　穎崴又站回4000元、台星科、眾達大漲5%
  - 來源：Yahoo 台股；發布時間：2026-11-13T08:45:00Z；台北時間：2026-11-13 16:45
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導輝達執行長黃仁勳昨（12）日宣布辭去三大要職震撼市場，美股四大指數全數收黑，然而，台股加權指數今（13）日未明顯受影響...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%85%89%E9%80%9A%E8%A8%8A%E8%82%A1%E4%B9%9F%E9%96%83%E7%B4%85%E5%85%89-%E9%80%99%E6%AA%94-%E5%8F%A6%E6%8F%A1%E8%A1%9B%E6%98%9F%E9%A1%8C%E6%9D%90%E7%8C%9B%E9%A3%86%E6%BC%B2%E5%81%9C-%E5%85%89%E8%81%96%E5%99%B4%E5%8D%8A%E6%A0%B9-%E7%A9%8E%E5%B4%B4%E5%8F%88%E7%AB%99%E5%9B%9E4000%E5%85%83-084500583.html
- 事件6：黃仁勳閃辭執行長代價曝！ 身家蒸發逾60億美元  1.08億獎酬也作廢
  - 來源：Yahoo 台股；發布時間：2026-11-13T08:27:00Z；台北時間：2026-11-13 16:27
  - 摘要：科技巨頭掌門人因私德風波突然卸下重擔，不僅撼動全球AI產業版圖，更直接牽動千億美元等級的個人財富與股價表現。近日輝達（Nvidia）共同創辦人黃仁勳在兩段婚外情曝光後辭去執行長一職，不僅失去1.08億美元未歸屬股權獎酬，股價重挫更讓他身家再
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E9%96%83%E8%BE%AD%E5%9F%B7%E8%A1%8C%E9%95%B7%E4%BB%A3%E5%83%B9%E6%9B%9D-%E8%BA%AB%E5%AE%B6%E8%92%B8%E7%99%BC%E9%80%BE60%E5%84%84%E7%BE%8E%E5%85%83-1-08%E5%84%84%E7%8D%8E%E9%85%AC%E4%B9%9F%E4%BD%9C%E5%BB%A2-082700350.html
- 事件7：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions, and changes to streamline and adjust their check services
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 18:30:00 GMT；台北時間：2026-11-13 02:30
  - 摘要：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions,
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261112a.htm
- 事件8：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 17:45:00 GMT；台北時間：2026-11-13 01:45
  - 摘要：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 16:00:00 GMT；台北時間：2026-11-13 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261112a.htm
- 事件10：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 來源：Federal Reserve；發布時間：Mon, 9 Nov 2026 21:00:00 GMT；台北時間：2026-11-10 05:00
  - 摘要：Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261109a.htm
- 事件11：Chicago Fed's Goolsbee says central bank 'has definitely got work to do' on inflation
  - 來源：CNBC；發布時間：Fri, 13 Nov 2026 14:22:07 GMT；台北時間：2026-11-13 22:22
  - 摘要：The policymaker expressed concern about the latest inflation data, telling CNBC that the central bank likely will need to take action.
  - 原文連結：https://www.cnbc.com/2026/11/13/chicago-feds-goolsbee-says-central-bank-has-definitely-got-work-to-do-on-inflation.html
- 事件12：10-year Treasury yield moves to 5.17% as traders weigh producer price report
  - 來源：CNBC；發布時間：Fri, 13 Nov 2026 17:39:48 GMT；台北時間：2026-11-14 01:39
  - 摘要：Treasury yields moved higher as investor expectations for a December rate hike by the Federal Reserve gain strength.
  - 原文連結：https://www.cnbc.com/2026/11/13/treasury-yields-fed-rates.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-13

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 43,925 | TAIFEX Proxy |
| 最高價 | 44,824 | TAIFEX Proxy |
| 最低價 | 43,692 | TAIFEX Proxy |
| 收盤價 | 43,834 | TAIFEX Proxy |
| 漲跌點數 | +706 | TAIFEX Proxy |
| 漲跌幅 | +1.64 | TAIFEX Proxy |
| 成交量 | 94,919 | TAIFEX Proxy |
| 日盤高點及低點 | 44,824 / 43,692 | TAIFEX Proxy |

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
| 外資多方 OI | 6,186 | TAIFEX Proxy |
| 外資空方 OI | 107,056 | TAIFEX Proxy |
| 外資多空淨 OI | -100,870 | TAIFEX Proxy |
| 投信多方 OI | 103,019 | TAIFEX Proxy |
| 投信空方 OI | 3,096 | TAIFEX Proxy |
| 投信多空淨 OI | +99,923 | TAIFEX Proxy |
| 自營商多方 OI | 3,733 | TAIFEX Proxy |
| 自營商空方 OI | 6,504 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,771 | TAIFEX Proxy |
| 三大法人合計多方 OI | 112,938 | TAIFEX Proxy |
| 三大法人合計空方 OI | 116,656 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,718 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,297 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,022 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -2,584 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,792 | TAIFEX Proxy |
| 前十大交易人空方 OI | 78,453 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,339 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-11→2026-11-12) | -409 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：2026-11-12 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 104,183 | TAIFEX Proxy |
| 外資日盤空單交易量 | 105,480 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,297 | TAIFEX Proxy |
| 外資夜盤多單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤空單交易量 | unavailable | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,022 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -2,523 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | unavailable | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,798 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | unavailable | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | -248.6 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | unavailable | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 43,834 | TAIFEX Proxy |
| 加權指數價格 | 43,675.12 | twse-proxy |
| 台指期與加權指數價差 | +158.88 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.36 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +158.88 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | unavailable | 端點未提供 |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 43,834 | unavailable | unavailable | TAIFEX Proxy |
| 成交量 | 94,919 | unavailable | unavailable | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,859（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 104,183 | 105,480 | -1,297 | unavailable | unavailable | unavailable | unavailable | 6,186 | 107,056 | -100,870 | -1,297 | TAIFEX Proxy |
| 投信 | 9,181 | 8,159 | +1,022 | unavailable | unavailable | unavailable | unavailable | 103,019 | 3,096 | +99,923 | +1,022 | TAIFEX Proxy |
| 自營商 | 8,904 | 11,427 | -2,523 | unavailable | unavailable | unavailable | unavailable | 3,733 | 6,504 | -2,771 | -2,584 | TAIFEX Proxy |
| 三大法人合計 | 122,268 | 125,066 | -2,798 | unavailable | unavailable | unavailable | unavailable | 112,938 | 116,656 | -3,718 | -2,859 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 97,792 | TAIFEX Proxy |
| 前十大交易人空方 OI | 78,453 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +19,339 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-11→2026-11-12) | -409 | TAIFEX Proxy snapshots (2026-11-12) |

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
| 交易日期 | 2026-11-13 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F2 | TAIFEX Proxy |
| 資料更新時間 | 2026-11-14 02:21:19 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 419,770 | TAIFEX Proxy |
| Call 總未平倉量 OI | 83,365 | TAIFEX Proxy |
| Call OI 增減 (2026-11-12→2026-11-13) | +29,709 | TAIFEX Proxy snapshots (2026-11-12) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 430,162 | TAIFEX Proxy |
| Put 總未平倉量 OI | 74,992 | TAIFEX Proxy |
| Put OI 增減 (2026-11-12→2026-11-13) | +38,519 | TAIFEX Proxy snapshots (2026-11-12) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.98 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.11 | TAIFEX Proxy |
| Put／Call Ratio | 0.90 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-11-11→2026-11-12) | -8.91 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-11-11→2026-11-12) | 1.52 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 140,200 | TAIFEX Proxy |
| 外資 Call日賣 | 140,699 | TAIFEX Proxy |
| 外資 Call日淨 | -499 | TAIFEX Proxy |
| 外資 Put日買 | 151,226 | TAIFEX Proxy |
| 外資 Put日賣 | 150,457 | TAIFEX Proxy |
| 外資 Put日淨 | +769 | TAIFEX Proxy |
| 外資 Call夜買 | 43,033 | TAIFEX Proxy |
| 外資 Call夜賣 | 43,937 | TAIFEX Proxy |
| 外資 Call夜淨 | -904 | TAIFEX Proxy |
| 外資 Put夜買 | 47,843 | TAIFEX Proxy |
| 外資 Put夜賣 | 47,165 | TAIFEX Proxy |
| 外資 Put夜淨 | +678 | TAIFEX Proxy |
| 外資 日盤淨總量 | -1,268 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +405 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +91 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 122,287 | TAIFEX Proxy |
| 自營商 Call日賣 | 118,011 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,276 | TAIFEX Proxy |
| 自營商 Put日買 | 103,902 | TAIFEX Proxy |
| 自營商 Put日賣 | 120,492 | TAIFEX Proxy |
| 自營商 Put日淨 | -16,590 | TAIFEX Proxy |
| 自營商 Call夜買 | 31,800 | TAIFEX Proxy |
| 自營商 Call夜賣 | 32,878 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,078 | TAIFEX Proxy |
| 自營商 Put夜買 | 30,368 | TAIFEX Proxy |
| 自營商 Put夜賣 | 34,312 | TAIFEX Proxy |
| 自營商 Put夜淨 | -3,944 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +20,866 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,354 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -12,646 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 44,000 | 4,861 | TAIFEX Proxy |
| Call OI 第2大履約價 | 46,000 | 4,603 | TAIFEX Proxy |
| Call OI 第3大履約價 | 45,000 | 4,321 | TAIFEX Proxy |
| Call OI 最大履約價 | 44,000 | 4,861 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 44,000 | 4,861 | 5.83% | TAIFEX Proxy |
| C2 | 46,000 | 4,603 | 5.52% | TAIFEX Proxy |
| C3 | 45,000 | 4,321 | 5.18% | TAIFEX Proxy |
| C4 | 43,800 | 3,483 | 4.18% | TAIFEX Proxy |
| C5 | 47,000 | 3,084 | 3.7% | TAIFEX Proxy |
| C6 | 44,500 | 2,626 | 3.15% | TAIFEX Proxy |
| C7 | 44,600 | 2,551 | 3.06% | TAIFEX Proxy |
| C8 | 43,850 | 2,455 | 2.94% | TAIFEX Proxy |
| C9 | 43,900 | 2,434 | 2.92% | TAIFEX Proxy |
| C10 | 44,200 | 2,025 | 2.43% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 43,000 | 3,916 | TAIFEX Proxy |
| Put OI 第2大履約價 | 39,000 | 3,474 | TAIFEX Proxy |
| Put OI 第3大履約價 | 43,500 | 3,020 | TAIFEX Proxy |
| Put OI 最大履約價 | 43,000 | 3,916 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F2)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 43,000 | 3,916 | 5.22% | TAIFEX Proxy |
| P2 | 39,000 | 3,474 | 4.63% | TAIFEX Proxy |
| P3 | 43,500 | 3,020 | 4.03% | TAIFEX Proxy |
| P4 | 42,000 | 2,975 | 3.97% | TAIFEX Proxy |
| P5 | 43,700 | 2,709 | 3.61% | TAIFEX Proxy |
| P6 | 43,750 | 2,690 | 3.59% | TAIFEX Proxy |
| P7 | 43,600 | 2,500 | 3.33% | TAIFEX Proxy |
| P8 | 43,800 | 2,395 | 3.19% | TAIFEX Proxy |
| P9 | 40,000 | 2,303 | 3.07% | TAIFEX Proxy |
| P10 | 41,000 | 1,795 | 2.39% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 43,800 (+3,043) | TAIFEX Proxy snapshots (2026-11-12) |
| Call OI 減少最多的履約價 | 49,500 (-400) | TAIFEX Proxy snapshots (2026-11-12) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 43,750 (+2,607) | TAIFEX Proxy snapshots (2026-11-12) |
| Put OI 減少最多的履約價 | 42,800 (-89) | TAIFEX Proxy snapshots (2026-11-12) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 44,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | -2,000 | TAIFEX Proxy snapshots (2026-11-12) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 43,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +0 | TAIFEX Proxy snapshots (2026-11-12) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 43,600.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,826.92 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 資料日期 | 2026-11-13 | TAIFEX Proxy (options-gamma-levels) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,700 | TAIFEX Proxy |
| 對應到期月份 | 202611F2 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-12→2026-11-13) | +750 | TAIFEX Proxy snapshots (2026-11-12) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 290,657 | 291,925 | -1,268 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 投信 | 165 | 18,964 | -18,799 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 自營商 | 242,779 | 221,913 | +20,866 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
| 三大法人合計 | 533,601 | 532,802 | +799 | unavailable | unavailable | unavailable | unavailable | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 22.02 | 21.22 | +0.80 | 9.01 | 9.38 | -0.37 | +1.17 | TAIFEX Proxy |
| 投信 | 0.01 | 10.28 | -10.27 | 0.00 | 0.00 | +0.00 | -10.27 | TAIFEX Proxy |
| 自營商 | 29.85 | 19.66 | +10.20 | 8.16 | 7.29 | +0.87 | +9.32 | TAIFEX Proxy |
| 三大法人合計 | 51.88 | 51.15 | +0.73 | 17.18 | 16.67 | +0.50 | +0.23 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 27,143 | TAIFEX Proxy |
| 買權空方 OI | 32,423 | TAIFEX Proxy |
| 買權多空淨 OI | -5,280 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-11→2026-11-12) | -303 | TAIFEX Proxy snapshots (2026-11-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 16,219 | TAIFEX Proxy |
| 賣權空方 OI | 17,769 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,550 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-11→2026-11-12) | +957 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：買權 2026-11-12／賣權 2026-11-12 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -409 | 2026-11-11→2026-11-12 | TAIFEX Proxy snapshots (2026-11-12) |
| 買權前十大 | -303 | 2026-11-11→2026-11-12 | TAIFEX Proxy snapshots (2026-11-12) |
| 賣權前十大 | +957 | 2026-11-11→2026-11-12 | TAIFEX Proxy snapshots (2026-11-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-13；資料時間：2026-11-14 02:21:19；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (0)：無
- 註記：futures-price-after-hours 日期 2026-11-13 非今日 2026-11-16，視為無新節次，不採用
- 註記：futures-institutional-after-hours 日期 2026-11-13 非今日 2026-11-16，視為無新節次，不採用
- 註記：options-institutional-after-hours 日期 2026-11-13 非今日 2026-11-16，視為無新節次，不採用
- 註記：夜盤開高低收未取得 (proxy 與官方皆無)，僅成交量/OI/結算價
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
| 外資 | +288.4 | -100,870 | -1,297 | unavailable | -1,268 | unavailable | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +95.4 | +99,923 | +1,022 | unavailable | -18,799 | unavailable | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +68.9 | -2,771 | -2,523 | unavailable | +20,866 | unavailable | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
