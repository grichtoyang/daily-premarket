# DATA_REPORT_20261126

- 報告日期：`2026-11-27`
- T0 交易日期：`2026-11-26`
- 首次資料產出時間：`2026-11-27 08:39:26`
- 本次更新開始時間：`2026-11-27 08:39:26`
- 時區：`Asia/Taipei`
- 產出盤別：`全日`
- 產出者：`actions`
- 排定班別：`manual`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 39,151.81 | 點 | twse-proxy |
| 開盤 | 38,435.99 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 39,459.95 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 38,435.99 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 39,151.81 | 點 | twse-proxy |
| 漲跌點數 | 956.38 | 點 | twse-proxy |
| 漲跌幅 | +2.50 | % | twse-proxy |
| 成交金額 | 8,453.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 971 | twse-proxy |
| 下跌家數 | 83 | twse-proxy |
| 平盤家數 | 32 | twse-proxy |
| 漲停家數 | 57 | twse-proxy |
| 跌停家數 | 3 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 666 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 157 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 57 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 36 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 3 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -491.8 | 億元 | twse-proxy /institutional |
| 投信 | +212.1 | 億元 | twse-proxy /institutional |
| 自營商 | +128.7 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -151.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-26；估值 1248 檔；1 檔採最近有效收盤價（價格日期 20261125 至 20261126）；Blave 同 T0 交叉驗證 159.6730%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 5,641.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | +21.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 194,854 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | 5,801 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 159.67 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-26；估值 1248 檔；1 檔採最近有效收盤價（價格日期 20261125 至 20261126）；Blave 同 T0 交叉驗證 159.6730%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 35,112,106 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,443,495.525 | 2,117,759.479 | 20,561,255.004 | 張 |
| 借券賣出增減 | -18,879 | -5,299.482 | -24,178.482 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261126`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-27T08:39:44+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261126`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-27T08:39:46+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 8,453.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,213.6 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 9,667.0 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,182.78 | -18.31 | -0.25 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,585.80 | -147.74 | -0.62 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,046.90 | -167.27 | -0.64 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,182.95 | 164.25 | +0.33 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 8,774.86 | -57.64 | -0.65 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 26.80 | -1.49 | -5.27 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 57,485.82 | 474.20 | +0.83 | 2026-11-27 | 2026-11-27T00:39:46+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,698.49 | 0.98 | +0.02 | 2026-11-27 | 2026-11-27T00:39:46+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-27T00:39:46+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 上海綜合 | 000001.SS | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-27T00:39:46+00:00 | Asia/Shanghai | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 深圳成分 | 399001.SZ | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-27T00:39:46+00:00 | Asia/Shanghai | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,241.00 | 45.25 | +0.63 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,234.00 | 133.75 | +0.51 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,483.00 | 255.00 | +0.51 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,720.00 | 13.90 | +0.51 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.61 | -0.02 | 25-NOV-26 | 2026-11-27T00:40:35+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.85 | -0.06 | 2026-11-25 | 2026-11-27T00:40:35+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.28 | -0.05 | 25-NOV-26 | 2026-11-27T00:40:35+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.24 | -0.06 | 2026-11-25 | 2026-11-27T00:40:35+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.94 | -0.25 | -0.76 | 2026-11-27 | 2026-11-27T00:39:46+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.78 | 0.11 | +0.10 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.35 | 0.14 | +0.09 | 2026-11-27 | 2026-11-27T00:39:46+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.02 | 0.05 | +0.00 | 2026-11-27 | 2026-11-27T00:39:46+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 342.34 | -6.86 | -1.96 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.19 | -0.21 | -1.57 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 29.49 | 0.16 | +0.55 | 2026-11-25 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.13 | 1.45 | +1.73 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,593.10 | 57.30 | +1.62 | 2026-11-26 | 2026-11-27T00:39:46+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 60,599.62 | 221.42 | +0.37 | 2026-11-27 | 2026-11-27T00:39:46+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：馬斯克太空AI計畫鳴槍 鴻海將成最大贏家
  - 來源：Yahoo 台股；發布時間：2026-11-26T22:40:33Z；台北時間：2026-11-27 06:40
  - 摘要：美國聯邦傳播委員會（FCC）昨（26）日宣布，已授權億萬富豪馬斯克旗下SpaceX部署由100萬顆衛星組成的星系，組建名為「Starmind」的AI算力星座，用於打造太空資料中心。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A6%AC%E6%96%AF%E5%85%8B%E5%A4%AA%E7%A9%BAai%E9%B3%B4%E6%A7%8D-%E9%B4%BB%E6%B5%B7%E8%B5%B7%E9%A3%9B-224033732.html
- 事件2：跟著台積電 聯合再生、中美晶將在德州設廠
  - 來源：Yahoo 台股；發布時間：2026-11-26T22:39:41Z；台北時間：2026-11-27 06:39
  - 摘要：台積電要在美國德州成立第二園區之際，太陽能廠聯合再生與中美晶將跟隨台積電，在德州設立太陽能模組廠，打造台灣太陽能業最大規模「美國製造」產能，並可望就近爭取台積電德州園區太陽能發電工程，大咬晶圓一哥綠能商機。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E5%90%88%E5%86%8D%E7%94%9F-%E4%B8%AD%E7%BE%8E%E6%99%B6%E5%BE%B7%E5%B7%9E%E8%A8%AD%E5%BB%A0-%E5%89%8D%E5%BE%80%E7%94%9F%E7%94%A2%E5%A4%AA%E9%99%BD%E8%83%BD%E6%A8%A1%E7%B5%84-%E5%A4%A7%E5%92%AC%E7%B6%A0%E8%83%BD%E5%95%86%E6%A9%9F-223941340.html
- 事件3：卸下華映案包袱 大同三箭轉型、430億建案明年陸續交屋
  - 來源：Yahoo 台股；發布時間：2026-11-26T22:31:00Z；台北時間：2026-11-27 06:31
  - 摘要：纏訟多年的華映案終於迎來轉折，大同11月19日與中國華映正式簽署和解文件，和解金額與帳列負債準備相差人民幣20.35億元，預計今年認列相關回沖利益；除了卸下歷史包袱，大同總經理張松鑌26日也在法說會上透露，總銷430億元的3大住宅建案將於明
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E5%90%8C%E8%BD%89%E5%9E%8B%E9%A9%97%E6%94%B62-%E8%8F%AF%E6%98%A0%E6%A1%88%E5%8D%B8%E4%B8%8B%E6%AD%B7%E5%8F%B2%E5%8C%85%E8%A2%B1-%E5%A4%A7%E5%90%8C430%E5%84%84%E5%BB%BA%E6%A1%88%E6%98%8E%E5%B9%B4%E8%B5%B7%E5%85%A5%E5%B8%B3-223100062.html
- 事件4：天瀚90天暴漲478%、川湖6天價差1215元 全列注意股
  - 來源：Yahoo 台股；發布時間：2026-11-27T00:20:00Z；台北時間：2026-11-27 08:20
  - 摘要：[FTNN新聞網]記者莊蕙如／綜合報導證交所公布11月26日共23檔注意股，伺服器滑軌大廠川湖（2059）、貿聯-KY（3665）、金像電（2368）、聯鈞（3450）及台玻（18...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%80%E7%8B%82%E4%B8%8D%E6%98%AF%E5%B7%9D%E6%B9%96-%E9%80%99%E6%AA%94-90%E5%A4%A9%E6%9A%B4%E6%BC%B2478-%E9%87%91%E5%83%8F%E9%9B%BB-%E8%81%AF%E9%88%9E%E5%85%A8%E4%B8%8A%E6%A6%9C-002000508.html
- 事件5：00406A人氣霸榜 國家隊反手提款、同步賣超00403A
  - 來源：Yahoo 台股；發布時間：2026-11-26T23:00:00Z；台北時間：2026-11-27 07:00
  - 摘要：[FTNN新聞網]記者陳思穎／綜合報導台股昨（26）日開高走揚，終場收39151.81點，上漲956.38點，漲幅2.50%，成交額8185.07億元。根據「玩股網」資料，「國家隊...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%88%86%E9%87%8F82%E8%90%AC%E5%BC%B5%E5%A5%AA%E6%88%90%E4%BA%A4%E7%8E%8B-%E5%9C%8B%E5%AE%B6%E9%9A%8A%E5%8F%8D%E6%89%8B%E5%87%BA%E8%84%AB-%E9%80%99%E6%AA%94%E4%B8%BB%E5%8B%95%E5%BC%8F-5472%E5%BC%B5-%E5%86%8D%E7%A0%8D00403a%E9%80%BE1-230000292.html
- 事件6：301關稅大致過關 半導體業備戰232條款
  - 來源：Yahoo 台股；發布時間：2026-11-26T22:39:41Z；台北時間：2026-11-27 06:39
  - 摘要：川普政府新一輪關稅方案出爐，科技業大致過關，AI伺服器、智慧手機、PC、晶片及大部分半導體設備均獲豁免，但耳機、印表機等未能倖免，蘋果、惠普旗下產品兩樣情。台灣半導體業雖躲過301關稅頭關，下一場大考則是232條款。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8D%8A%E5%B0%8E%E9%AB%94%E6%A5%AD%E9%97%96%E9%81%8E%E9%A0%AD%E9%97%9C-%E5%82%99%E6%88%B0232%E6%A2%9D%E6%AC%BE-223941219.html
- 事件7：Federal Reserve announces College Fed Challenge winners
  - 來源：Federal Reserve；發布時間：Fri, 20 Nov 2026 21:15:00 GMT；台北時間：2026-11-21 05:15
  - 摘要：Federal Reserve announces College Fed Challenge winners
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261120b.htm
- 事件8：Federal Reserve Board releases results from survey of senior financial officers at banks about their strategies and practices for managing reserve balances
  - 來源：Federal Reserve；發布時間：Fri, 20 Nov 2026 15:00:00 GMT；台北時間：2026-11-20 23:00
  - 摘要：Federal Reserve Board releases results from survey of senior financial officers at banks about their strategies and practices for managing reserve bal
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261120a.htm
- 事件9：Trump demands probe into ‘record setting error’ after third-quarter GDP data gets massive revision higher
  - 來源：CNBC；發布時間：Thu, 26 Nov 2026 21:13:17 GMT；台北時間：2026-11-27 05:13
  - 摘要：President Donald Trump on Thursday deemed the latest gross domestic product revision a mistake, claiming that it should be "immediately investigated."
  - 原文連結：https://www.cnbc.com/2026/11/26/trump-gdp-revision-investigation.html
- 事件10：U.S. tariff-hike threats pile pressure on partners to sign trade deals
  - 來源：CNBC；發布時間：Thu, 26 Nov 2026 12:46:55 GMT；台北時間：2026-11-26 20:46
  - 摘要：The U.S. planned a fresh tariff salvo on 14 trading partners, while offering some countries lower rates if they secure trade deals with Washington.
  - 原文連結：https://www.cnbc.com/2026/11/26/us-tariffs-hike-trade-agreement.html
- 事件11：How Trump’s latest tariff moves hand India an edge over rival Asian exporters
  - 來源：CNBC；發布時間：Thu, 26 Nov 2026 04:12:18 GMT；台北時間：2026-11-26 12:12
  - 摘要：Proposed tariffs of 18% on Bangladesh, Cambodia, Thailand, and 20% on China and Vietnam, subject to their respective trade deals, offer India a compet
  - 原文連結：https://www.cnbc.com/2026/11/26/trump-us-tariff-india-trade.html
- 事件12：Spain’s Pablo Hernández de Cos set to lead European Central Bank
  - 來源：CNBC；發布時間：Thu, 26 Nov 2026 15:28:26 GMT；台北時間：2026-11-26 23:28
  - 摘要：De Cos will lead the ECB into a period of political uncertainty and choppy growth, after winning the backing needed to succeed Christine Lagarde next 
  - 原文連結：https://www.cnbc.com/2026/11/26/pablo-hernandez-de-cos-ecb-president.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-26

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 38,990 | 點 | TAIFEX Proxy |
| 最高價 | 39,688 | 點 | TAIFEX Proxy |
| 最低價 | 38,473 | 點 | TAIFEX Proxy |
| 收盤價 | 39,455 | 點 | TAIFEX Proxy |
| 漲跌點數 | +1,332 | 點 | TAIFEX Proxy |
| 漲跌幅 | +3.49 | % | TAIFEX Proxy |
| 成交量 | 79,377 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 39,688 / 38,473 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 39,250 | 點 | TAIFEX Proxy |
| 最高價 | 39,559 | 點 | TAIFEX Proxy |
| 最低價 | 39,008 | 點 | TAIFEX Proxy |
| 收盤價 | 39,492 | 點 | TAIFEX Proxy |
| 漲跌點數 | +0 | 點 | TAIFEX Proxy |
| 漲跌幅 | +0.00 | % | TAIFEX Proxy |
| 成交量 | 25,940 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 39,559 / 39,008 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,083 | TAIFEX Proxy |
| 外資空方 OI | 115,358 | TAIFEX Proxy |
| 外資多空淨 OI | -106,275 | TAIFEX Proxy |
| 投信多方 OI | 108,341 | TAIFEX Proxy |
| 投信空方 OI | 3,421 | TAIFEX Proxy |
| 投信多空淨 OI | +104,920 | TAIFEX Proxy |
| 自營商多方 OI | 2,322 | TAIFEX Proxy |
| 自營商空方 OI | 4,732 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,410 | TAIFEX Proxy |
| 三大法人合計多方 OI | 119,746 | TAIFEX Proxy |
| 三大法人合計空方 OI | 123,511 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,765 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -566 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +4,002 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,759 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 110,339 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,591 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +16,748 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-25→2026-11-26) | +6,060 | TAIFEX Proxy snapshots (2026-11-25) |
- 資料日期：2026-11-26 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 103,678 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 104,261 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -583 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 14,678 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,258 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,580 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +997 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +4,002 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +4,002 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,550 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +121 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,671 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,869 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,459 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | +137.8 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -114.8 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 39,455 | TAIFEX Proxy |
| 加權指數價格 | 39,151.81 | twse-proxy |
| 台指期與加權指數價差 | +303.19 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +0.77 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +303.19 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +37 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,455 | 39,492 | -37 | TAIFEX Proxy |
| 成交量 | 79,377 | 25,940 | +53,437 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,677（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 103,678 | 104,261 | -583 | 14,678 | 16,258 | -1,580 | +997 | 9,083 | 115,358 | -106,275 | -566 | TAIFEX Proxy |
| 投信 | 4,492 | 490 | +4,002 | 0 | 0 | +0 | +4,002 | 108,341 | 3,421 | +104,920 | +4,002 | TAIFEX Proxy |
| 自營商 | 4,271 | 5,821 | -1,550 | 371 | 250 | +121 | -1,671 | 2,322 | 4,732 | -2,410 | -1,759 | TAIFEX Proxy |
| 三大法人合計 | 112,441 | 110,572 | +1,869 | 15,049 | 16,508 | -1,459 | +3,328 | 119,746 | 123,511 | -3,765 | +1,677 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 110,339 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,591 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +16,748 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-25→2026-11-26) | +6,060 | TAIFEX Proxy snapshots (2026-11-25) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 24.63% | TAIFEX Proxy |
| 夜盤漲跌點數 | +0 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,580 | TAIFEX Proxy |
| 劇本分類 | unavailable | 規則對應 |
| 劇本條件 | unavailable | 規則對應 |
| 劇本特徵 | unavailable | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-26 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F4 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-27 08:39:26 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 163,762 | TAIFEX Proxy |
| Call 總未平倉量 OI | 83,028 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-25→2026-11-26) | +45,692 | TAIFEX Proxy snapshot bundle (2026-11-25→2026-11-26) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 139,796 | TAIFEX Proxy |
| Put 總未平倉量 OI | 42,240 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-25→2026-11-26) | +34,260 | TAIFEX Proxy snapshot bundle (2026-11-25→2026-11-26) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.17 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.97 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.51 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-25→2026-11-26) | 1.78 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-25→2026-11-26) | 12.69 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 42,858 | TAIFEX Proxy |
| 外資 Call日賣 | 41,698 | TAIFEX Proxy |
| 外資 Call日淨 | +1,160 | TAIFEX Proxy |
| 外資 Put日買 | 36,549 | TAIFEX Proxy |
| 外資 Put日賣 | 36,027 | TAIFEX Proxy |
| 外資 Put日淨 | +522 | TAIFEX Proxy |
| 外資 Call夜買 | 14,859 | TAIFEX Proxy |
| 外資 Call夜賣 | 15,528 | TAIFEX Proxy |
| 外資 Call夜淨 | -669 | TAIFEX Proxy |
| 外資 Put夜買 | 21,136 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,840 | TAIFEX Proxy |
| 外資 Put夜淨 | +296 | TAIFEX Proxy |
| 外資 日盤淨總量 | +638 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,829 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +226 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 37,346 | TAIFEX Proxy |
| 自營商 Call日賣 | 35,880 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,466 | TAIFEX Proxy |
| 自營商 Put日買 | 37,624 | TAIFEX Proxy |
| 自營商 Put日賣 | 43,115 | TAIFEX Proxy |
| 自營商 Put日淨 | -5,491 | TAIFEX Proxy |
| 自營商 Call夜買 | 9,365 | TAIFEX Proxy |
| 自營商 Call夜賣 | 13,137 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,772 | TAIFEX Proxy |
| 自營商 Put夜買 | 14,140 | TAIFEX Proxy |
| 自營商 Put夜賣 | 15,648 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,508 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +6,957 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,238 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -3,983 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 42,000 | 12,554 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 9,405 | TAIFEX Proxy |
| Call OI 第3大履約價 | 37,600 | 3,656 | TAIFEX Proxy |
| Call OI 最大履約價 | 42,000 | 12,554 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 42,000 | 12,554 | 15.12% | TAIFEX Proxy |
| C2 | 43,000 | 9,405 | 11.33% | TAIFEX Proxy |
| C3 | 37,600 | 3,656 | 4.4% | TAIFEX Proxy |
| C4 | 37,800 | 3,442 | 4.15% | TAIFEX Proxy |
| C5 | 37,500 | 3,000 | 3.61% | TAIFEX Proxy |
| C6 | 41,000 | 2,946 | 3.55% | TAIFEX Proxy |
| C7 | 35,000 | 2,802 | 3.37% | TAIFEX Proxy |
| C8 | 35,200 | 2,505 | 3.02% | TAIFEX Proxy |
| C9 | 42,500 | 2,405 | 2.9% | TAIFEX Proxy |
| C10 | 40,000 | 2,203 | 2.65% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 34,000 | 4,499 | TAIFEX Proxy |
| Put OI 第2大履約價 | 32,400 | 4,170 | TAIFEX Proxy |
| Put OI 第3大履約價 | 36,000 | 3,109 | TAIFEX Proxy |
| Put OI 最大履約價 | 34,000 | 4,499 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 34,000 | 4,499 | 10.65% | TAIFEX Proxy |
| P2 | 32,400 | 4,170 | 9.87% | TAIFEX Proxy |
| P3 | 36,000 | 3,109 | 7.36% | TAIFEX Proxy |
| P4 | 35,000 | 2,854 | 6.76% | TAIFEX Proxy |
| P5 | 34,500 | 1,588 | 3.76% | TAIFEX Proxy |
| P6 | 38,000 | 1,531 | 3.62% | TAIFEX Proxy |
| P7 | 37,000 | 1,497 | 3.54% | TAIFEX Proxy |
| P8 | 35,500 | 1,027 | 2.43% | TAIFEX Proxy |
| P9 | 36,500 | 970 | 2.3% | TAIFEX Proxy |
| P10 | 33,000 | 870 | 2.06% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 42,000 (+11,649) | TAIFEX Proxy snapshot bundle (2026-11-25→2026-11-26) |
| Call OI 減少最多的履約價（共同合約） | 39,150 (-103) | TAIFEX Proxy snapshot bundle (2026-11-25→2026-11-26) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 34,000 (+4,175) | TAIFEX Proxy snapshot bundle (2026-11-25→2026-11-26) |
| Put OI 減少最多的履約價（共同合約） | 40,250 (-2) | TAIFEX Proxy snapshot bundle (2026-11-25→2026-11-26) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 42,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-25→2026-11-26) | -1,000 | TAIFEX Proxy snapshots (2026-11-25) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 34,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-25→2026-11-26) | +1,600 | TAIFEX Proxy snapshots (2026-11-25) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 40,000.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611F4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-27 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F4 | TAIFEX Proxy |
| 資料日期 | 2026-11-26 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 37,182.94 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611F4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-27 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F4 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 83,028 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 83,028 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 42,240 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 42,040 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-26 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：35,236.63～43,066.99
- 搜尋步長／計算次數：10.00／196
- 起點／終點 Net GEX：-2,301,591,373.51／5,814,976.51
- 搜尋區間最低／最高 Net GEX：-2,301,591,373.51／5,814,976.51
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-26","chain_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":364,"delta_rows":364},{"contract_month":"202612W2","expiry":"2026-12-09","chain_rows":286,"delta_rows":286},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：33,279.04～45,024.58
- 搜尋步長／計算次數：10.00／1176
- 起點／終點 Net GEX：-1,768,664,222.18／2,252,094,947.36
- 搜尋區間最低／最高 Net GEX：-2,412,045,970.65／11,372,912,867.86
- 正負號交叉次數：1
- 擴大區間診斷 Flip：37,182.94

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 3,687,106,556.82 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 7,922,202,701.21 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 257 | 資料日期：2026-11-26 |
| 正 Net GEX 最大履約價 | 40,000 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 38,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：40,000（385,633,717.26 NT$）、37,800（377,829,502.37 NT$）、37,600（369,325,832.73 NT$）、41,000（274,872,896.41 NT$）、37,500（252,609,547.82 NT$）
- 負 Net GEX Top 5：38,000（-151,274,003.39 NT$）、38,500（-84,088,822.73 NT$）、37,000（-76,456,079.06 NT$）、38,450（-42,397,133.19 NT$）、36,000（-41,859,103.26 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-26","underlying":39151.81,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":3687106556.8195047,"gross_gex_1pct":7922202701.214548,"gamma_diagnostics":{"chain_rows":516,"delta_rows":516,"matched_strike_keys":516,"positive_oi_settlement_eligible":416,"invalid_oi":100,"invalid_settlement":0,"below_intrinsic":46,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":370},"formal_flip_diagnostics":{"search_lower_underlying":35236.629,"search_upper_underlying":43066.991,"step":10,"evaluations":196,"start_net_gex_1pct":-2301591373.514929,"end_net_gex_1pct":5814976.50857743,"min_net_gex_1pct":-2301591373.514929,"max_net_gex_1pct":5814976.50857743,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":37179.038499999995,"upper_underlying":37189.038499999995,"estimated_underlying":37182.941904330655,"lower_net_gex_1pct":-6157341.226122954,"upper_net_gex_1pct":9616943.742922965},"wide_range_flip_diagnostics":{"search_lower_underlying":33279.038499999995,"search_upper_underlying":45024.58149999999,"reference_underlying":39151.81,"step":10,"evaluations":1176,"start_net_gex_1pct":-1768664222.1750016,"end_net_gex_1pct":2252094947.3592095,"min_net_gex_1pct":-2412045970.6515594,"max_net_gex_1pct":11372912867.861927,"zero_crossings":1,"found":true,"selected_crossing_distance":1968.8680956693424},"expiry_selection_diagnostics":{"requested_date":"2026-11-26","chain_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":364,"delta_rows":364},{"contract_month":"202612W2","expiry":"2026-12-09","chain_rows":286,"delta_rows":286},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":32400.0,"call_gex_1pct":19163.848991384384,"put_gex_1pct":-2476427.1112936805,"net_gex_1pct":-2457263.2623022962,"gross_gex_1pct":2495590.9602850648,"call_oi":1,"put_oi":4170},{"strike":32500.0,"call_gex_1pct":0.0,"put_gex_1pct":-293371.8965217221,"net_gex_1pct":-293371.8965217221,"gross_gex_1pct":293371.8965217221,"call_oi":0,"put_oi":480},{"strike":32600.0,"call_gex_1pct":0.0,"put_gex_1pct":-176821.1814138857,"net_gex_1pct":-176821.1814138857,"gross_gex_1pct":176821.1814138857,"call_oi":0,"put_oi":281},{"strike":32700.0,"call_gex_1pct":0.0,"put_gex_1pct":-106289.5364712933,"net_gex_1pct":-106289.5364712933,"gross_gex_1pct":106289.5364712933,"call_oi":0,"put_oi":164},{"strike":32800.0,"call_gex_1pct":0.0,"put_gex_1pct":-160269.14413927196,"net_gex_1pct":-160269.14413927196,"gross_gex_1pct":160269.14413927196,"call_oi":0,"put_oi":240},{"strike":32900.0,"call_gex_1pct":0.0,"put_gex_1pct":-139735.129783132,"net_gex_1pct":-139735.129783132,"gross_gex_1pct":139735.129783132,"call_oi":0,"put_oi":203},{"strike":33000.0,"call_gex_1pct":109579.44661627537,"put_gex_1pct":-617567.4722140611,"net_gex_1pct":-507988.0255977857,"gross_gex_1pct":727146.9188303364,"call_oi":5,"put_oi":870},{"strike":33100.0,"call_gex_1pct":0.0,"put_gex_1pct":-166240.72862919566,"net_gex_1pct":-166240.72862919566,"gross_gex_1pct":166240.72862919566,"call_oi":0,"put_oi":227},{"strike":33200.0,"call_gex_1pct":22966.829241361138,"put_gex_1pct":-196978.74547835597,"net_gex_1pct":-174011.91623699482,"gross_gex_1pct":219945.57471971711,"call_oi":1,"put_oi":212},{"strike":33300.0,"call_gex_1pct":0.0,"put_gex_1pct":-290673.01024020417,"net_gex_1pct":-290673.01024020417,"gross_gex_1pct":290673.01024020417,"call_oi":0,"put_oi":303},{"strike":33400.0,"call_gex_1pct":0.0,"put_gex_1pct":-170442.81484721944,"net_gex_1pct":-170442.81484721944,"gross_gex_1pct":170442.81484721944,"call_oi":0,"put_oi":172},{"strike":33500.0,"call_gex_1pct":0.0,"put_gex_1pct":-457786.4519398651,"net_gex_1pct":-457786.4519398651,"gross_gex_1pct":457786.4519398651,"call_oi":0,"put_oi":447},{"strike":33600.0,"call_gex_1pct":0.0,"put_gex_1pct":-482892.2002950208,"net_gex_1pct":-482892.2002950208,"gross_gex_1pct":482892.2002950208,"call_oi":0,"put_oi":456},{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-116132.59368467957,"net_gex_1pct":-116132.59368467957,"gross_gex_1pct":116132.59368467957,"call_oi":0,"put_oi":106},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-315908.84708614426,"net_gex_1pct":-315908.84708614426,"gross_gex_1pct":315908.84708614426,"call_oi":0,"put_oi":238},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-413753.95558659366,"net_gex_1pct":-413753.95558659366,"gross_gex_1pct":413753.95558659366,"call_oi":0,"put_oi":301},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-6408278.706283187,"net_gex_1pct":-6408278.706283187,"gross_gex_1pct":6408278.706283187,"call_oi":0,"put_oi":4499},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-386941.65176625975,"net_gex_1pct":-386941.65176625975,"gross_gex_1pct":386941.65176625975,"call_oi":0,"put_oi":262},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-855021.4112380304,"net_gex_1pct":-855021.4112380304,"gross_gex_1pct":855021.4112380304,"call_oi":0,"put_oi":558},{"strike":34300.0,"call_gex_1pct":30764.950159202504,"put_gex_1pct":-250963.36338167463,"net_gex_1pct":-220198.41322247213,"gross_gex_1pct":281728.31354087713,"call_oi":1,"put_oi":139},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-346975.0095304654,"net_gex_1pct":-346975.0095304654,"gross_gex_1pct":346975.0095304654,"call_oi":0,"put_oi":185},{"strike":34500.0,"call_gex_1pct":162607.8885887265,"put_gex_1pct":-3096153.421141944,"net_gex_1pct":-2933545.5325532174,"gross_gex_1pct":3258761.3097306704,"call_oi":5,"put_oi":1588},{"strike":34600.0,"call_gex_1pct":66918.85055241882,"put_gex_1pct":-574026.7122910634,"net_gex_1pct":-507107.86173864454,"gross_gex_1pct":640945.5628434822,"call_oi":2,"put_oi":283},{"strike":34700.0,"call_gex_1pct":206642.44623114832,"put_gex_1pct":-487836.22120784223,"net_gex_1pct":-281193.7749766939,"gross_gex_1pct":694478.6674389906,"call_oi":6,"put_oi":231},{"strike":34800.0,"call_gex_1pct":14718966.376992457,"put_gex_1pct":-666774.9653980762,"net_gex_1pct":14052191.41159438,"gross_gex_1pct":15385741.342390534,"call_oi":415,"put_oi":303},{"strike":34900.0,"call_gex_1pct":7710675.461171507,"put_gex_1pct":-410226.5011028477,"net_gex_1pct":7300448.960068659,"gross_gex_1pct":8120901.962274355,"call_oi":211,"put_oi":147},{"strike":35000.0,"call_gex_1pct":105557213.03060256,"put_gex_1pct":-8994190.121653125,"net_gex_1pct":96563022.90894943,"gross_gex_1pct":114551403.15225568,"call_oi":2802,"put_oi":2854},{"strike":35050.0,"call_gex_1pct":191286.20231839627,"put_gex_1pct":-257621.99781326443,"net_gex_1pct":-66335.79549486816,"gross_gex_1pct":448908.2001316607,"call_oi":5,"put_oi":80},{"strike":35100.0,"call_gex_1pct":5245685.75575058,"put_gex_1pct":-859057.6932289958,"net_gex_1pct":4386628.062521584,"gross_gex_1pct":6104743.448979575,"call_oi":135,"put_oi":261},{"strike":35150.0,"call_gex_1pct":0.0,"put_gex_1pct":-632608.620206272,"net_gex_1pct":-632608.620206272,"gross_gex_1pct":632608.620206272,"call_oi":0,"put_oi":188},{"strike":35200.0,"call_gex_1pct":100455643.80862427,"put_gex_1pct":-1056380.2746492876,"net_gex_1pct":99399263.53397498,"gross_gex_1pct":101512024.08327356,"call_oi":2505,"put_oi":307},{"strike":35250.0,"call_gex_1pct":0.0,"put_gex_1pct":-503308.8543400633,"net_gex_1pct":-503308.8543400633,"gross_gex_1pct":503308.8543400633,"call_oi":0,"put_oi":143},{"strike":35300.0,"call_gex_1pct":4928017.838509834,"put_gex_1pct":-648190.2550731117,"net_gex_1pct":4279827.583436723,"gross_gex_1pct":5576208.093582946,"call_oi":119,"put_oi":180},{"strike":35350.0,"call_gex_1pct":252555.79620679066,"put_gex_1pct":-909762.9758933175,"net_gex_1pct":-657207.1796865268,"gross_gex_1pct":1162318.7721001082,"call_oi":6,"put_oi":194},{"strike":35400.0,"call_gex_1pct":82929747.73949859,"put_gex_1pct":-1420634.0200372192,"net_gex_1pct":81509113.71946137,"gross_gex_1pct":84350381.7595358,"call_oi":1938,"put_oi":270},{"strike":35450.0,"call_gex_1pct":217544.64126148057,"put_gex_1pct":-1238792.131158295,"net_gex_1pct":-1021247.4898968146,"gross_gex_1pct":1456336.7724197756,"call_oi":5,"put_oi":230},{"strike":35500.0,"call_gex_1pct":3539673.5186445313,"put_gex_1pct":-5901150.941446394,"net_gex_1pct":-2361477.4228018625,"gross_gex_1pct":9440824.460090924,"call_oi":80,"put_oi":1027},{"strike":35550.0,"call_gex_1pct":225015.7036077329,"put_gex_1pct":-798796.6628491889,"net_gex_1pct":-573780.959241456,"gross_gex_1pct":1023812.3664569218,"call_oi":5,"put_oi":118},{"strike":35600.0,"call_gex_1pct":52190789.001138166,"put_gex_1pct":-2552280.62988065,"net_gex_1pct":49638508.371257514,"gross_gex_1pct":54743069.63101882,"call_oi":1140,"put_oi":329},{"strike":35650.0,"call_gex_1pct":232907.60357031674,"put_gex_1pct":-699936.1507890592,"net_gex_1pct":-467028.5472187425,"gross_gex_1pct":932843.7543593759,"call_oi":5,"put_oi":82},{"strike":35700.0,"call_gex_1pct":1611749.8812447467,"put_gex_1pct":-2198599.1656589527,"net_gex_1pct":-586849.2844142059,"gross_gex_1pct":3810349.0469036996,"call_oi":34,"put_oi":236},{"strike":35750.0,"call_gex_1pct":144752.9735267466,"put_gex_1pct":-1069031.1674973886,"net_gex_1pct":-924278.1939706419,"gross_gex_1pct":1213784.141024135,"call_oi":3,"put_oi":92},{"strike":35800.0,"call_gex_1pct":2996457.5508889784,"put_gex_1pct":-2068247.6127091541,"net_gex_1pct":928209.9381798243,"gross_gex_1pct":5064705.163598132,"call_oi":61,"put_oi":161},{"strike":35850.0,"call_gex_1pct":400153.9151529547,"put_gex_1pct":-652803.4380442613,"net_gex_1pct":-252649.5228913066,"gross_gex_1pct":1052957.353197216,"call_oi":8,"put_oi":49},{"strike":35900.0,"call_gex_1pct":916974.7653694774,"put_gex_1pct":-2710163.499319936,"net_gex_1pct":-1793188.7339504587,"gross_gex_1pct":3627138.264689414,"call_oi":18,"put_oi":194},{"strike":35950.0,"call_gex_1pct":51894.82446340069,"put_gex_1pct":-2894731.843570639,"net_gex_1pct":-2842837.0191072384,"gross_gex_1pct":2946626.6680340394,"call_oi":1,"put_oi":202},{"strike":36000.0,"call_gex_1pct":3859934.2756386846,"put_gex_1pct":-45719037.53935873,"net_gex_1pct":-41859103.26372004,"gross_gex_1pct":49578971.81499741,"call_oi":73,"put_oi":3109},{"strike":36050.0,"call_gex_1pct":808309.5498110283,"put_gex_1pct":-1795335.9952653195,"net_gex_1pct":-987026.4454542912,"gross_gex_1pct":2603645.545076348,"call_oi":15,"put_oi":101},{"strike":36100.0,"call_gex_1pct":1263405.4861898148,"put_gex_1pct":-3092029.4321355503,"net_gex_1pct":-1828623.9459457356,"gross_gex_1pct":4355434.918325365,"call_oi":23,"put_oi":160},{"strike":36150.0,"call_gex_1pct":392051.6544632499,"put_gex_1pct":-1541983.7153081123,"net_gex_1pct":-1149932.0608448624,"gross_gex_1pct":1934035.3697713623,"call_oi":7,"put_oi":73},{"strike":36200.0,"call_gex_1pct":2627472.4741059565,"put_gex_1pct":-5464004.625810458,"net_gex_1pct":-2836532.151704502,"gross_gex_1pct":8091477.099916415,"call_oi":46,"put_oi":241},{"strike":36250.0,"call_gex_1pct":990540.3149837367,"put_gex_1pct":-3774400.2502140086,"net_gex_1pct":-2783859.935230272,"gross_gex_1pct":4764940.565197745,"call_oi":17,"put_oi":158},{"strike":36300.0,"call_gex_1pct":3940194.095981389,"put_gex_1pct":-6310151.287045352,"net_gex_1pct":-2369957.1910639633,"gross_gex_1pct":10250345.383026741,"call_oi":66,"put_oi":251},{"strike":36350.0,"call_gex_1pct":121835.80717056616,"put_gex_1pct":-2010772.4108386475,"net_gex_1pct":-1888936.6036680813,"gross_gex_1pct":2132608.2180092135,"call_oi":2,"put_oi":73},{"strike":36400.0,"call_gex_1pct":1927495.7689696972,"put_gex_1pct":-10883062.533827279,"net_gex_1pct":-8955566.76485758,"gross_gex_1pct":12810558.302796977,"call_oi":31,"put_oi":377},{"strike":36450.0,"call_gex_1pct":190440.29540915627,"put_gex_1pct":-1451313.2234086054,"net_gex_1pct":-1260872.9279994492,"gross_gex_1pct":1641753.5188177617,"call_oi":3,"put_oi":48},{"strike":36500.0,"call_gex_1pct":4797311.662556984,"put_gex_1pct":-30179680.115142416,"net_gex_1pct":-25382368.452585433,"gross_gex_1pct":34976991.7776994,"call_oi":74,"put_oi":970},{"strike":36550.0,"call_gex_1pct":1192048.7011898044,"put_gex_1pct":-2458987.690993953,"net_gex_1pct":-1266938.9898041487,"gross_gex_1pct":3651036.3921837574,"call_oi":18,"put_oi":72},{"strike":36600.0,"call_gex_1pct":2977557.6960141174,"put_gex_1pct":-6778282.847599709,"net_gex_1pct":-3800725.151585592,"gross_gex_1pct":9755840.543613827,"call_oi":44,"put_oi":190},{"strike":36650.0,"call_gex_1pct":1798464.5833041053,"put_gex_1pct":-1277190.8793288688,"net_gex_1pct":521273.7039752365,"gross_gex_1pct":3075655.462632974,"call_oi":26,"put_oi":33},{"strike":36700.0,"call_gex_1pct":2903814.3427119097,"put_gex_1pct":-9519597.506190246,"net_gex_1pct":-6615783.163478336,"gross_gex_1pct":12423411.848902155,"call_oi":41,"put_oi":226},{"strike":36750.0,"call_gex_1pct":2027846.2987862185,"put_gex_1pct":-3805622.6537715346,"net_gex_1pct":-1777776.354985316,"gross_gex_1pct":5833468.952557753,"call_oi":28,"put_oi":83},{"strike":36800.0,"call_gex_1pct":4296781.321834086,"put_gex_1pct":-9029752.91741585,"net_gex_1pct":-4732971.595581763,"gross_gex_1pct":13326534.239249937,"call_oi":58,"put_oi":188},{"strike":36850.0,"call_gex_1pct":985480.9108585597,"put_gex_1pct":-2481817.2723911013,"net_gex_1pct":-1496336.3615325417,"gross_gex_1pct":3467298.183249661,"call_oi":13,"put_oi":48},{"strike":36900.0,"call_gex_1pct":5354270.40187323,"put_gex_1pct":-6179117.589084618,"net_gex_1pct":-824847.1872113878,"gross_gex_1pct":11533387.990957849,"call_oi":69,"put_oi":113},{"strike":36950.0,"call_gex_1pct":1191148.920944525,"put_gex_1pct":-4873290.053292008,"net_gex_1pct":-3682141.132347483,"gross_gex_1pct":6064438.974236533,"call_oi":15,"put_oi":84},{"strike":37000.0,"call_gex_1pct":14557302.698214784,"put_gex_1pct":-91013381.75765908,"net_gex_1pct":-76456079.0594443,"gross_gex_1pct":105570684.45587386,"call_oi":179,"put_oi":1497},{"strike":37050.0,"call_gex_1pct":3249501.421549909,"put_gex_1pct":-4404764.747324127,"net_gex_1pct":-1155263.325774218,"gross_gex_1pct":7654266.168874036,"call_oi":39,"put_oi":68},{"strike":37100.0,"call_gex_1pct":3757567.1525423694,"put_gex_1pct":-5615407.838703709,"net_gex_1pct":-1857840.6861613393,"gross_gex_1pct":9372974.991246078,"call_oi":44,"put_oi":82},{"strike":37150.0,"call_gex_1pct":4115650.852604078,"put_gex_1pct":-5751755.126189087,"net_gex_1pct":-1636104.2735850085,"gross_gex_1pct":9867405.978793165,"call_oi":47,"put_oi":78},{"strike":37200.0,"call_gex_1pct":6916875.933820246,"put_gex_1pct":-16737875.682426706,"net_gex_1pct":-9820999.74860646,"gross_gex_1pct":23654751.616246954,"call_oi":77,"put_oi":219},{"strike":37250.0,"call_gex_1pct":4871567.515546752,"put_gex_1pct":-5389748.170959948,"net_gex_1pct":-518180.6554131955,"gross_gex_1pct":10261315.6865067,"call_oi":53,"put_oi":67},{"strike":37300.0,"call_gex_1pct":3947810.617076218,"put_gex_1pct":-16024097.562191341,"net_gex_1pct":-12076286.945115123,"gross_gex_1pct":19971908.17926756,"call_oi":42,"put_oi":190},{"strike":37350.0,"call_gex_1pct":2219462.898477954,"put_gex_1pct":-8214407.80369094,"net_gex_1pct":-5994944.905212986,"gross_gex_1pct":10433870.702168893,"call_oi":23,"put_oi":93},{"strike":37400.0,"call_gex_1pct":30230788.61214433,"put_gex_1pct":-11344718.74126269,"net_gex_1pct":18886069.87088164,"gross_gex_1pct":41575507.35340702,"call_oi":305,"put_oi":124},{"strike":37450.0,"call_gex_1pct":12329123.72074019,"put_gex_1pct":-6881318.443255268,"net_gex_1pct":5447805.277484922,"gross_gex_1pct":19210442.16399546,"call_oi":123,"put_oi":71},{"strike":37500.0,"call_gex_1pct":308886922.9576002,"put_gex_1pct":-56277375.133102685,"net_gex_1pct":252609547.8244975,"gross_gex_1pct":365164298.0907029,"call_oi":3000,"put_oi":560},{"strike":37550.0,"call_gex_1pct":18941465.49448495,"put_gex_1pct":-4255187.123929121,"net_gex_1pct":14686278.37055583,"gross_gex_1pct":23196652.61841407,"call_oi":179,"put_oi":40},{"strike":37600.0,"call_gex_1pct":397823803.51271415,"put_gex_1pct":-28497970.784516655,"net_gex_1pct":369325832.7281975,"gross_gex_1pct":426321774.2972308,"call_oi":3656,"put_oi":256},{"strike":37650.0,"call_gex_1pct":16122198.867044432,"put_gex_1pct":-4076556.5069411932,"net_gex_1pct":12045642.360103238,"gross_gex_1pct":20198755.373985626,"call_oi":144,"put_oi":35},{"strike":37700.0,"call_gex_1pct":19941165.19440319,"put_gex_1pct":-15776373.863480253,"net_gex_1pct":4164791.330922937,"gross_gex_1pct":35717539.05788344,"call_oi":173,"put_oi":130},{"strike":37750.0,"call_gex_1pct":30396188.747670714,"put_gex_1pct":-4299737.072467338,"net_gex_1pct":26096451.675203376,"gross_gex_1pct":34695925.82013805,"call_oi":258,"put_oi":34},{"strike":37800.0,"call_gex_1pct":417881029.40784615,"put_gex_1pct":-40051527.04231877,"net_gex_1pct":377829502.3655274,"gross_gex_1pct":457932556.4501649,"call_oi":3442,"put_oi":303},{"strike":37850.0,"call_gex_1pct":22710365.12757938,"put_gex_1pct":-7986948.276988522,"net_gex_1pct":14723416.850590859,"gross_gex_1pct":30697313.4045679,"call_oi":183,"put_oi":58},{"strike":37900.0,"call_gex_1pct":63671245.216121644,"put_gex_1pct":-39707947.94656799,"net_gex_1pct":23963297.269553654,"gross_gex_1pct":103379193.16268963,"call_oi":502,"put_oi":277},{"strike":37950.0,"call_gex_1pct":5184657.774109583,"put_gex_1pct":-10725959.009939693,"net_gex_1pct":-5541301.23583011,"gross_gex_1pct":15910616.784049276,"call_oi":40,"put_oi":72},{"strike":38000.0,"call_gex_1pct":86297086.90362526,"put_gex_1pct":-237571090.2912188,"net_gex_1pct":-151274003.3875935,"gross_gex_1pct":323868177.19484407,"call_oi":645,"put_oi":1531},{"strike":38050.0,"call_gex_1pct":8206152.306635523,"put_gex_1pct":-5942785.814230148,"net_gex_1pct":2263366.4924053755,"gross_gex_1pct":14148938.120865671,"call_oi":60,"put_oi":37},{"strike":38100.0,"call_gex_1pct":15379017.142488573,"put_gex_1pct":-18124616.71461298,"net_gex_1pct":-2745599.5721244067,"gross_gex_1pct":33503633.857101552,"call_oi":110,"put_oi":109},{"strike":38150.0,"call_gex_1pct":9289835.33192703,"put_gex_1pct":-10845156.555183169,"net_gex_1pct":-1555321.223256139,"gross_gex_1pct":20134991.887110196,"call_oi":65,"put_oi":63},{"strike":38200.0,"call_gex_1pct":32436383.312717117,"put_gex_1pct":-34555785.81997645,"net_gex_1pct":-2119402.5072593316,"gross_gex_1pct":66992169.13269357,"call_oi":222,"put_oi":194},{"strike":38250.0,"call_gex_1pct":23602699.211344585,"put_gex_1pct":-4784265.889341248,"net_gex_1pct":18818433.322003335,"gross_gex_1pct":28386965.100685835,"call_oi":158,"put_oi":26},{"strike":38300.0,"call_gex_1pct":18788370.85976823,"put_gex_1pct":-20223040.323527195,"net_gex_1pct":-1434669.463758964,"gross_gex_1pct":39011411.18329543,"call_oi":123,"put_oi":106},{"strike":38350.0,"call_gex_1pct":5936289.0512324795,"put_gex_1pct":-29618957.670653526,"net_gex_1pct":-23682668.619421046,"gross_gex_1pct":35555246.72188601,"call_oi":38,"put_oi":151},{"strike":38400.0,"call_gex_1pct":19974250.221463412,"put_gex_1pct":-44273079.50305876,"net_gex_1pct":-24298829.28159535,"gross_gex_1pct":64247329.72452217,"call_oi":125,"put_oi":218},{"strike":38450.0,"call_gex_1pct":19781994.36588695,"put_gex_1pct":-62179127.552680485,"net_gex_1pct":-42397133.186793536,"gross_gex_1pct":81961121.91856743,"call_oi":121,"put_oi":299},{"strike":38500.0,"call_gex_1pct":91852333.5162019,"put_gex_1pct":-175941156.24685597,"net_gex_1pct":-84088822.73065408,"gross_gex_1pct":267793489.7630579,"call_oi":549,"put_oi":824},{"strike":38550.0,"call_gex_1pct":9762222.572991656,"put_gex_1pct":-8798306.138526581,"net_gex_1pct":963916.4344650749,"gross_gex_1pct":18560528.711518236,"call_oi":57,"put_oi":40},{"strike":38600.0,"call_gex_1pct":163707029.98602143,"put_gex_1pct":-35452148.46206378,"net_gex_1pct":128254881.52395764,"gross_gex_1pct":199159178.44808522,"call_oi":947,"put_oi":155},{"strike":38650.0,"call_gex_1pct":17924164.967632417,"put_gex_1pct":-19627768.313417155,"net_gex_1pct":-1703603.3457847387,"gross_gex_1pct":37551933.28104957,"call_oi":102,"put_oi":85},{"strike":38700.0,"call_gex_1pct":28940613.239903044,"put_gex_1pct":-25216156.37191154,"net_gex_1pct":3724456.8679915033,"gross_gex_1pct":54156769.61181459,"call_oi":162,"put_oi":107},{"strike":38750.0,"call_gex_1pct":15257064.25713046,"put_gex_1pct":-11830634.531826932,"net_gex_1pct":3426429.725303529,"gross_gex_1pct":27087698.788957395,"call_oi":84,"put_oi":49},{"strike":38800.0,"call_gex_1pct":49110944.98046752,"put_gex_1pct":-79484452.69781788,"net_gex_1pct":-30373507.717350356,"gross_gex_1pct":128595397.67828539,"call_oi":272,"put_oi":318},{"strike":38850.0,"call_gex_1pct":15214445.666229313,"put_gex_1pct":-34519742.01526713,"net_gex_1pct":-19305296.34903782,"gross_gex_1pct":49734187.68149645,"call_oi":81,"put_oi":133},{"strike":38900.0,"call_gex_1pct":40377682.96545867,"put_gex_1pct":-42175829.307620786,"net_gex_1pct":-1798146.3421621174,"gross_gex_1pct":82553512.27307945,"call_oi":213,"put_oi":165},{"strike":38950.0,"call_gex_1pct":15234364.907443233,"put_gex_1pct":-11408132.595072277,"net_gex_1pct":3826232.312370956,"gross_gex_1pct":26642497.50251551,"call_oi":79,"put_oi":44},{"strike":39000.0,"call_gex_1pct":240770949.8143206,"put_gex_1pct":-200178739.06823078,"net_gex_1pct":40592210.746089816,"gross_gex_1pct":440949688.8825514,"call_oi":1237,"put_oi":771},{"strike":39050.0,"call_gex_1pct":22200846.206446532,"put_gex_1pct":-25191855.36794562,"net_gex_1pct":-2991009.161499087,"gross_gex_1pct":47392701.574392155,"call_oi":113,"put_oi":94},{"strike":39100.0,"call_gex_1pct":35301429.450453505,"put_gex_1pct":-25415822.515997685,"net_gex_1pct":9885606.93445582,"gross_gex_1pct":60717251.96645119,"call_oi":178,"put_oi":92},{"strike":39150.0,"call_gex_1pct":21801491.867604084,"put_gex_1pct":-21080790.548876833,"net_gex_1pct":720701.3187272511,"gross_gex_1pct":42882282.416480914,"call_oi":108,"put_oi":75},{"strike":39200.0,"call_gex_1pct":80072698.8284371,"put_gex_1pct":-30052901.15230991,"net_gex_1pct":50019797.676127195,"gross_gex_1pct":110125599.98074701,"call_oi":406,"put_oi":109},{"strike":39250.0,"call_gex_1pct":18315627.904168826,"put_gex_1pct":-11117855.932291238,"net_gex_1pct":7197771.971877588,"gross_gex_1pct":29433483.83646006,"call_oi":92,"put_oi":40},{"strike":39300.0,"call_gex_1pct":83774250.99107455,"put_gex_1pct":-14489135.990526916,"net_gex_1pct":69285115.00054763,"gross_gex_1pct":98263386.98160146,"call_oi":410,"put_oi":51},{"strike":39350.0,"call_gex_1pct":17025381.303682636,"put_gex_1pct":-22129437.649130188,"net_gex_1pct":-5104056.345447551,"gross_gex_1pct":39154818.95281282,"call_oi":86,"put_oi":76},{"strike":39400.0,"call_gex_1pct":66829793.0263473,"put_gex_1pct":-21107922.958753802,"net_gex_1pct":45721870.0675935,"gross_gex_1pct":87937715.9851011,"call_oi":329,"put_oi":75},{"strike":39450.0,"call_gex_1pct":23826271.244501095,"put_gex_1pct":-10138989.634835232,"net_gex_1pct":13687281.609665863,"gross_gex_1pct":33965260.87933633,"call_oi":116,"put_oi":36},{"strike":39500.0,"call_gex_1pct":161430950.95399266,"put_gex_1pct":-109305836.36544304,"net_gex_1pct":52125114.58854963,"gross_gex_1pct":270736787.3194357,"call_oi":793,"put_oi":388},{"strike":39550.0,"call_gex_1pct":38069100.51771597,"put_gex_1pct":-11827411.839596307,"net_gex_1pct":26241688.67811966,"gross_gex_1pct":49896512.35731228,"call_oi":189,"put_oi":42},{"strike":39600.0,"call_gex_1pct":83114566.80984926,"put_gex_1pct":-32211153.90095409,"net_gex_1pct":50903412.90889517,"gross_gex_1pct":115325720.71080336,"call_oi":411,"put_oi":112},{"strike":39650.0,"call_gex_1pct":33341960.644095924,"put_gex_1pct":-5824507.75741164,"net_gex_1pct":27517452.886684284,"gross_gex_1pct":39166468.401507564,"call_oi":164,"put_oi":21},{"strike":39700.0,"call_gex_1pct":64132421.29961897,"put_gex_1pct":-9967959.167383697,"net_gex_1pct":54164462.13223527,"gross_gex_1pct":74100380.46700266,"call_oi":318,"put_oi":35},{"strike":39750.0,"call_gex_1pct":32148076.3576302,"put_gex_1pct":-2952662.6143813943,"net_gex_1pct":29195413.743248805,"gross_gex_1pct":35100738.972011596,"call_oi":161,"put_oi":11},{"strike":39800.0,"call_gex_1pct":68067618.0806608,"put_gex_1pct":-10496770.025246197,"net_gex_1pct":57570848.05541461,"gross_gex_1pct":78564388.10590701,"call_oi":353,"put_oi":41},{"strike":39850.0,"call_gex_1pct":27206445.91381974,"put_gex_1pct":-4681066.970169524,"net_gex_1pct":22525378.943650216,"gross_gex_1pct":31887512.883989267,"call_oi":140,"put_oi":18},{"strike":39900.0,"call_gex_1pct":42146313.1272259,"put_gex_1pct":-4413875.745524782,"net_gex_1pct":37732437.38170112,"gross_gex_1pct":46560188.87275068,"call_oi":219,"put_oi":18},{"strike":39950.0,"call_gex_1pct":27370839.86442802,"put_gex_1pct":-4009383.396118362,"net_gex_1pct":23361456.46830966,"gross_gex_1pct":31380223.260546383,"call_oi":146,"put_oi":17},{"strike":40000.0,"call_gex_1pct":403497140.1348019,"put_gex_1pct":-17863422.87217317,"net_gex_1pct":385633717.26262873,"gross_gex_1pct":421360563.0069751,"call_oi":2203,"put_oi":80},{"strike":40050.0,"call_gex_1pct":37313299.92387396,"put_gex_1pct":-2911305.4124249304,"net_gex_1pct":34401994.51144903,"gross_gex_1pct":40224605.33629889,"call_oi":204,"put_oi":14},{"strike":40100.0,"call_gex_1pct":54733807.32317632,"put_gex_1pct":-3567475.5944772325,"net_gex_1pct":51166331.72869909,"gross_gex_1pct":58301282.917653546,"call_oi":309,"put_oi":19},{"strike":40150.0,"call_gex_1pct":25051363.41472354,"put_gex_1pct":-1894910.4327617986,"net_gex_1pct":23156452.981961742,"gross_gex_1pct":26946273.84748534,"call_oi":143,"put_oi":11},{"strike":40200.0,"call_gex_1pct":78337100.87428145,"put_gex_1pct":-1831189.104783107,"net_gex_1pct":76505911.76949835,"gross_gex_1pct":80168289.97906455,"call_oi":460,"put_oi":15},{"strike":40250.0,"call_gex_1pct":34174962.27361162,"put_gex_1pct":-524191.3537908092,"net_gex_1pct":33650770.91982081,"gross_gex_1pct":34699153.62740243,"call_oi":205,"put_oi":11},{"strike":40300.0,"call_gex_1pct":57761070.25517107,"put_gex_1pct":0.0,"net_gex_1pct":57761070.25517107,"gross_gex_1pct":57761070.25517107,"call_oi":359,"put_oi":0},{"strike":40350.0,"call_gex_1pct":24251228.89914619,"put_gex_1pct":0.0,"net_gex_1pct":24251228.89914619,"gross_gex_1pct":24251228.89914619,"call_oi":154,"put_oi":0},{"strike":40400.0,"call_gex_1pct":52149388.087550536,"put_gex_1pct":0.0,"net_gex_1pct":52149388.087550536,"gross_gex_1pct":52149388.087550536,"call_oi":343,"put_oi":0},{"strike":40450.0,"call_gex_1pct":24766060.01321521,"put_gex_1pct":0.0,"net_gex_1pct":24766060.01321521,"gross_gex_1pct":24766060.01321521,"call_oi":168,"put_oi":0},{"strike":40500.0,"call_gex_1pct":170725505.04007196,"put_gex_1pct":0.0,"net_gex_1pct":170725505.04007196,"gross_gex_1pct":170725505.04007196,"call_oi":1200,"put_oi":0},{"strike":40550.0,"call_gex_1pct":21514765.16870474,"put_gex_1pct":0.0,"net_gex_1pct":21514765.16870474,"gross_gex_1pct":21514765.16870474,"call_oi":157,"put_oi":0},{"strike":40600.0,"call_gex_1pct":60194284.2982014,"put_gex_1pct":0.0,"net_gex_1pct":60194284.2982014,"gross_gex_1pct":60194284.2982014,"call_oi":455,"put_oi":0},{"strike":40650.0,"call_gex_1pct":11877304.818810247,"put_gex_1pct":0.0,"net_gex_1pct":11877304.818810247,"gross_gex_1pct":11877304.818810247,"call_oi":94,"put_oi":0},{"strike":40700.0,"call_gex_1pct":48038342.07074993,"put_gex_1pct":0.0,"net_gex_1pct":48038342.07074993,"gross_gex_1pct":48038342.07074993,"call_oi":394,"put_oi":0},{"strike":40750.0,"call_gex_1pct":10974666.129899427,"put_gex_1pct":0.0,"net_gex_1pct":10974666.129899427,"gross_gex_1pct":10974666.129899427,"call_oi":95,"put_oi":0},{"strike":40800.0,"call_gex_1pct":48800430.71391713,"put_gex_1pct":0.0,"net_gex_1pct":48800430.71391713,"gross_gex_1pct":48800430.71391713,"call_oi":437,"put_oi":0},{"strike":40850.0,"call_gex_1pct":12713767.701470457,"put_gex_1pct":0.0,"net_gex_1pct":12713767.701470457,"gross_gex_1pct":12713767.701470457,"call_oi":121,"put_oi":0},{"strike":40900.0,"call_gex_1pct":35271527.477115884,"put_gex_1pct":0.0,"net_gex_1pct":35271527.477115884,"gross_gex_1pct":35271527.477115884,"call_oi":347,"put_oi":0},{"strike":40950.0,"call_gex_1pct":19923356.21405767,"put_gex_1pct":0.0,"net_gex_1pct":19923356.21405767,"gross_gex_1pct":19923356.21405767,"call_oi":206,"put_oi":0},{"strike":41000.0,"call_gex_1pct":274872896.4064732,"put_gex_1pct":0.0,"net_gex_1pct":274872896.4064732,"gross_gex_1pct":274872896.4064732,"call_oi":2946,"put_oi":0},{"strike":41050.0,"call_gex_1pct":7832152.554345112,"put_gex_1pct":0.0,"net_gex_1pct":7832152.554345112,"gross_gex_1pct":7832152.554345112,"call_oi":89,"put_oi":0},{"strike":41100.0,"call_gex_1pct":21958464.906778645,"put_gex_1pct":0.0,"net_gex_1pct":21958464.906778645,"gross_gex_1pct":21958464.906778645,"call_oi":269,"put_oi":0},{"strike":41150.0,"call_gex_1pct":9541824.033528868,"put_gex_1pct":0.0,"net_gex_1pct":9541824.033528868,"gross_gex_1pct":9541824.033528868,"call_oi":121,"put_oi":0},{"strike":41200.0,"call_gex_1pct":30967866.049069494,"put_gex_1pct":0.0,"net_gex_1pct":30967866.049069494,"gross_gex_1pct":30967866.049069494,"call_oi":421,"put_oi":0},{"strike":41250.0,"call_gex_1pct":6284508.194861727,"put_gex_1pct":0.0,"net_gex_1pct":6284508.194861727,"gross_gex_1pct":6284508.194861727,"call_oi":93,"put_oi":0},{"strike":41300.0,"call_gex_1pct":15204488.84375922,"put_gex_1pct":0.0,"net_gex_1pct":15204488.84375922,"gross_gex_1pct":15204488.84375922,"call_oi":239,"put_oi":0},{"strike":41350.0,"call_gex_1pct":7658960.575677858,"put_gex_1pct":0.0,"net_gex_1pct":7658960.575677858,"gross_gex_1pct":7658960.575677858,"call_oi":136,"put_oi":0},{"strike":41400.0,"call_gex_1pct":18605061.766778957,"put_gex_1pct":0.0,"net_gex_1pct":18605061.766778957,"gross_gex_1pct":18605061.766778957,"call_oi":354,"put_oi":0},{"strike":41450.0,"call_gex_1pct":9288758.504633881,"put_gex_1pct":0.0,"net_gex_1pct":9288758.504633881,"gross_gex_1pct":9288758.504633881,"call_oi":184,"put_oi":0},{"strike":41500.0,"call_gex_1pct":52780303.55438197,"put_gex_1pct":0.0,"net_gex_1pct":52780303.55438197,"gross_gex_1pct":52780303.55438197,"call_oi":1143,"put_oi":0},{"strike":41550.0,"call_gex_1pct":11627970.546781022,"put_gex_1pct":0.0,"net_gex_1pct":11627970.546781022,"gross_gex_1pct":11627970.546781022,"call_oi":279,"put_oi":0},{"strike":41600.0,"call_gex_1pct":24963356.161277886,"put_gex_1pct":0.0,"net_gex_1pct":24963356.161277886,"gross_gex_1pct":24963356.161277886,"call_oi":650,"put_oi":0},{"strike":41650.0,"call_gex_1pct":8432262.269980662,"put_gex_1pct":0.0,"net_gex_1pct":8432262.269980662,"gross_gex_1pct":8432262.269980662,"call_oi":246,"put_oi":0},{"strike":41700.0,"call_gex_1pct":12776168.203629375,"put_gex_1pct":0.0,"net_gex_1pct":12776168.203629375,"gross_gex_1pct":12776168.203629375,"call_oi":389,"put_oi":0},{"strike":41750.0,"call_gex_1pct":6711719.480146121,"put_gex_1pct":0.0,"net_gex_1pct":6711719.480146121,"gross_gex_1pct":6711719.480146121,"call_oi":231,"put_oi":0},{"strike":41800.0,"call_gex_1pct":17352479.196446754,"put_gex_1pct":0.0,"net_gex_1pct":17352479.196446754,"gross_gex_1pct":17352479.196446754,"call_oi":657,"put_oi":0},{"strike":41850.0,"call_gex_1pct":3652124.2915045973,"put_gex_1pct":0.0,"net_gex_1pct":3652124.2915045973,"gross_gex_1pct":3652124.2915045973,"call_oi":154,"put_oi":0},{"strike":41900.0,"call_gex_1pct":9838337.780594606,"put_gex_1pct":0.0,"net_gex_1pct":9838337.780594606,"gross_gex_1pct":9838337.780594606,"call_oi":465,"put_oi":0},{"strike":41950.0,"call_gex_1pct":4984299.775570877,"put_gex_1pct":0.0,"net_gex_1pct":4984299.775570877,"gross_gex_1pct":4984299.775570877,"call_oi":253,"put_oi":0},{"strike":42000.0,"call_gex_1pct":232262979.1170032,"put_gex_1pct":0.0,"net_gex_1pct":232262979.1170032,"gross_gex_1pct":232262979.1170032,"call_oi":12554,"put_oi":0},{"strike":42050.0,"call_gex_1pct":7635804.863621561,"put_gex_1pct":0.0,"net_gex_1pct":7635804.863621561,"gross_gex_1pct":7635804.863621561,"call_oi":460,"put_oi":0},{"strike":42100.0,"call_gex_1pct":6434495.857532893,"put_gex_1pct":0.0,"net_gex_1pct":6434495.857532893,"gross_gex_1pct":6434495.857532893,"call_oi":496,"put_oi":0},{"strike":42150.0,"call_gex_1pct":4595011.726900203,"put_gex_1pct":0.0,"net_gex_1pct":4595011.726900203,"gross_gex_1pct":4595011.726900203,"call_oi":372,"put_oi":0},{"strike":42200.0,"call_gex_1pct":6039799.40904401,"put_gex_1pct":0.0,"net_gex_1pct":6039799.40904401,"gross_gex_1pct":6039799.40904401,"call_oi":574,"put_oi":0},{"strike":42250.0,"call_gex_1pct":2440015.0757039725,"put_gex_1pct":0.0,"net_gex_1pct":2440015.0757039725,"gross_gex_1pct":2440015.0757039725,"call_oi":273,"put_oi":0},{"strike":42300.0,"call_gex_1pct":3844880.797702367,"put_gex_1pct":0.0,"net_gex_1pct":3844880.797702367,"gross_gex_1pct":3844880.797702367,"call_oi":441,"put_oi":0},{"strike":42350.0,"call_gex_1pct":1492174.7686604236,"put_gex_1pct":0.0,"net_gex_1pct":1492174.7686604236,"gross_gex_1pct":1492174.7686604236,"call_oi":200,"put_oi":0},{"strike":42400.0,"call_gex_1pct":1328011.386990584,"put_gex_1pct":0.0,"net_gex_1pct":1328011.386990584,"gross_gex_1pct":1328011.386990584,"call_oi":216,"put_oi":0},{"strike":42450.0,"call_gex_1pct":588208.0540515231,"put_gex_1pct":0.0,"net_gex_1pct":588208.0540515231,"gross_gex_1pct":588208.0540515231,"call_oi":105,"put_oi":0},{"strike":42500.0,"call_gex_1pct":12171558.085812464,"put_gex_1pct":0.0,"net_gex_1pct":12171558.085812464,"gross_gex_1pct":12171558.085812464,"call_oi":2405,"put_oi":0},{"strike":42550.0,"call_gex_1pct":177967.01573382088,"put_gex_1pct":0.0,"net_gex_1pct":177967.01573382088,"gross_gex_1pct":177967.01573382088,"call_oi":36,"put_oi":0},{"strike":42600.0,"call_gex_1pct":608646.6442630683,"put_gex_1pct":0.0,"net_gex_1pct":608646.6442630683,"gross_gex_1pct":608646.6442630683,"call_oi":126,"put_oi":0},{"strike":42650.0,"call_gex_1pct":354128.64502736134,"put_gex_1pct":0.0,"net_gex_1pct":354128.64502736134,"gross_gex_1pct":354128.64502736134,"call_oi":75,"put_oi":0},{"strike":42700.0,"call_gex_1pct":530940.7411303362,"put_gex_1pct":0.0,"net_gex_1pct":530940.7411303362,"gross_gex_1pct":530940.7411303362,"call_oi":115,"put_oi":0},{"strike":42750.0,"call_gex_1pct":165186.0138366438,"put_gex_1pct":0.0,"net_gex_1pct":165186.0138366438,"gross_gex_1pct":165186.0138366438,"call_oi":40,"put_oi":0},{"strike":42800.0,"call_gex_1pct":905002.9696581737,"put_gex_1pct":0.0,"net_gex_1pct":905002.9696581737,"gross_gex_1pct":905002.9696581737,"call_oi":224,"put_oi":0},{"strike":42850.0,"call_gex_1pct":1079408.498494011,"put_gex_1pct":0.0,"net_gex_1pct":1079408.498494011,"gross_gex_1pct":1079408.498494011,"call_oi":273,"put_oi":0},{"strike":42900.0,"call_gex_1pct":870875.123648986,"put_gex_1pct":0.0,"net_gex_1pct":870875.123648986,"gross_gex_1pct":870875.123648986,"call_oi":225,"put_oi":0},{"strike":42950.0,"call_gex_1pct":390378.936864943,"put_gex_1pct":0.0,"net_gex_1pct":390378.936864943,"gross_gex_1pct":390378.936864943,"call_oi":103,"put_oi":0},{"strike":43000.0,"call_gex_1pct":34914521.59315379,"put_gex_1pct":0.0,"net_gex_1pct":34914521.59315379,"gross_gex_1pct":34914521.59315379,"call_oi":9405,"put_oi":0},{"strike":43050.0,"call_gex_1pct":147409.8161823634,"put_gex_1pct":0.0,"net_gex_1pct":147409.8161823634,"gross_gex_1pct":147409.8161823634,"call_oi":45,"put_oi":0},{"strike":43100.0,"call_gex_1pct":25680.439362699013,"put_gex_1pct":0.0,"net_gex_1pct":25680.439362699013,"gross_gex_1pct":25680.439362699013,"call_oi":8,"put_oi":0},{"strike":43150.0,"call_gex_1pct":106980.30594419666,"put_gex_1pct":0.0,"net_gex_1pct":106980.30594419666,"gross_gex_1pct":106980.30594419666,"call_oi":34,"put_oi":0},{"strike":43200.0,"call_gex_1pct":256051.04373223535,"put_gex_1pct":0.0,"net_gex_1pct":256051.04373223535,"gross_gex_1pct":256051.04373223535,"call_oi":83,"put_oi":0},{"strike":43250.0,"call_gex_1pct":124040.70904836338,"put_gex_1pct":0.0,"net_gex_1pct":124040.70904836338,"gross_gex_1pct":124040.70904836338,"call_oi":41,"put_oi":0},{"strike":43300.0,"call_gex_1pct":249285.70750970952,"put_gex_1pct":0.0,"net_gex_1pct":249285.70750970952,"gross_gex_1pct":249285.70750970952,"call_oi":84,"put_oi":0},{"strike":43350.0,"call_gex_1pct":26206.051436849433,"put_gex_1pct":0.0,"net_gex_1pct":26206.051436849433,"gross_gex_1pct":26206.051436849433,"call_oi":9,"put_oi":0},{"strike":43400.0,"call_gex_1pct":208604.55244271472,"put_gex_1pct":0.0,"net_gex_1pct":208604.55244271472,"gross_gex_1pct":208604.55244271472,"call_oi":73,"put_oi":0},{"strike":43450.0,"call_gex_1pct":25245.489330555014,"put_gex_1pct":0.0,"net_gex_1pct":25245.489330555014,"gross_gex_1pct":25245.489330555014,"call_oi":9,"put_oi":0},{"strike":43500.0,"call_gex_1pct":2638416.886411895,"put_gex_1pct":0.0,"net_gex_1pct":2638416.886411895,"gross_gex_1pct":2638416.886411895,"call_oi":958,"put_oi":0},{"strike":43550.0,"call_gex_1pct":4769.4766726417365,"put_gex_1pct":0.0,"net_gex_1pct":4769.4766726417365,"gross_gex_1pct":4769.4766726417365,"call_oi":2,"put_oi":0},{"strike":43600.0,"call_gex_1pct":49186.768802001345,"put_gex_1pct":0.0,"net_gex_1pct":49186.768802001345,"gross_gex_1pct":49186.768802001345,"call_oi":21,"put_oi":0},{"strike":43650.0,"call_gex_1pct":43718.099891999234,"put_gex_1pct":0.0,"net_gex_1pct":43718.099891999234,"gross_gex_1pct":43718.099891999234,"call_oi":19,"put_oi":0},{"strike":43700.0,"call_gex_1pct":92695.49829380265,"put_gex_1pct":0.0,"net_gex_1pct":92695.49829380265,"gross_gex_1pct":92695.49829380265,"call_oi":41,"put_oi":0},{"strike":43750.0,"call_gex_1pct":8887.679845455335,"put_gex_1pct":0.0,"net_gex_1pct":8887.679845455335,"gross_gex_1pct":8887.679845455335,"call_oi":4,"put_oi":0},{"strike":43800.0,"call_gex_1pct":24024.77774886022,"put_gex_1pct":0.0,"net_gex_1pct":24024.77774886022,"gross_gex_1pct":24024.77774886022,"call_oi":11,"put_oi":0},{"strike":43850.0,"call_gex_1pct":53681.89618775452,"put_gex_1pct":0.0,"net_gex_1pct":53681.89618775452,"gross_gex_1pct":53681.89618775452,"call_oi":25,"put_oi":0},{"strike":43900.0,"call_gex_1pct":8445.980976666278,"put_gex_1pct":0.0,"net_gex_1pct":8445.980976666278,"gross_gex_1pct":8445.980976666278,"call_oi":4,"put_oi":0},{"strike":43950.0,"call_gex_1pct":14536.834731248511,"put_gex_1pct":0.0,"net_gex_1pct":14536.834731248511,"gross_gex_1pct":14536.834731248511,"call_oi":7,"put_oi":0},{"strike":44000.0,"call_gex_1pct":1867142.7270524567,"put_gex_1pct":0.0,"net_gex_1pct":1867142.7270524567,"gross_gex_1pct":1867142.7270524567,"call_oi":914,"put_oi":0},{"strike":44050.0,"call_gex_1pct":124611.67647276787,"put_gex_1pct":0.0,"net_gex_1pct":124611.67647276787,"gross_gex_1pct":124611.67647276787,"call_oi":62,"put_oi":0},{"strike":44100.0,"call_gex_1pct":35508.590176915495,"put_gex_1pct":0.0,"net_gex_1pct":35508.590176915495,"gross_gex_1pct":35508.590176915495,"call_oi":21,"put_oi":0},{"strike":44150.0,"call_gex_1pct":48257.05779565711,"put_gex_1pct":0.0,"net_gex_1pct":48257.05779565711,"gross_gex_1pct":48257.05779565711,"call_oi":29,"put_oi":0},{"strike":44200.0,"call_gex_1pct":22930.406555696223,"put_gex_1pct":0.0,"net_gex_1pct":22930.406555696223,"gross_gex_1pct":22930.406555696223,"call_oi":14,"put_oi":0},{"strike":44250.0,"call_gex_1pct":14511.685681310615,"put_gex_1pct":0.0,"net_gex_1pct":14511.685681310615,"gross_gex_1pct":14511.685681310615,"call_oi":9,"put_oi":0},{"strike":44350.0,"call_gex_1pct":1563.3832156493052,"put_gex_1pct":0.0,"net_gex_1pct":1563.3832156493052,"gross_gex_1pct":1563.3832156493052,"call_oi":1,"put_oi":0},{"strike":44400.0,"call_gex_1pct":27716.20593672494,"put_gex_1pct":0.0,"net_gex_1pct":27716.20593672494,"gross_gex_1pct":27716.20593672494,"call_oi":18,"put_oi":0},{"strike":44450.0,"call_gex_1pct":12134.240267564017,"put_gex_1pct":0.0,"net_gex_1pct":12134.240267564017,"gross_gex_1pct":12134.240267564017,"call_oi":8,"put_oi":0},{"strike":44500.0,"call_gex_1pct":25403.70899749199,"put_gex_1pct":0.0,"net_gex_1pct":25403.70899749199,"gross_gex_1pct":25403.70899749199,"call_oi":17,"put_oi":0},{"strike":44550.0,"call_gex_1pct":7362.18800724037,"put_gex_1pct":0.0,"net_gex_1pct":7362.18800724037,"gross_gex_1pct":7362.18800724037,"call_oi":5,"put_oi":0},{"strike":44600.0,"call_gex_1pct":55140.55307523959,"put_gex_1pct":0.0,"net_gex_1pct":55140.55307523959,"gross_gex_1pct":55140.55307523959,"call_oi":38,"put_oi":0},{"strike":44650.0,"call_gex_1pct":5720.828642611209,"put_gex_1pct":0.0,"net_gex_1pct":5720.828642611209,"gross_gex_1pct":5720.828642611209,"call_oi":4,"put_oi":0},{"strike":44700.0,"call_gex_1pct":1409.840833655025,"put_gex_1pct":0.0,"net_gex_1pct":1409.840833655025,"gross_gex_1pct":1409.840833655025,"call_oi":1,"put_oi":0},{"strike":44750.0,"call_gex_1pct":2779.904406745015,"put_gex_1pct":0.0,"net_gex_1pct":2779.904406745015,"gross_gex_1pct":2779.904406745015,"call_oi":2,"put_oi":0},{"strike":44800.0,"call_gex_1pct":65785.24430770818,"put_gex_1pct":0.0,"net_gex_1pct":65785.24430770818,"gross_gex_1pct":65785.24430770818,"call_oi":48,"put_oi":0},{"strike":44850.0,"call_gex_1pct":2703.0945376653376,"put_gex_1pct":0.0,"net_gex_1pct":2703.0945376653376,"gross_gex_1pct":2703.0945376653376,"call_oi":2,"put_oi":0},{"strike":44900.0,"call_gex_1pct":9331.014763353904,"put_gex_1pct":0.0,"net_gex_1pct":9331.014763353904,"gross_gex_1pct":9331.014763353904,"call_oi":7,"put_oi":0},{"strike":44950.0,"call_gex_1pct":1314.8768758077827,"put_gex_1pct":0.0,"net_gex_1pct":1314.8768758077827,"gross_gex_1pct":1314.8768758077827,"call_oi":1,"put_oi":0},{"strike":45000.0,"call_gex_1pct":708248.5616127328,"put_gex_1pct":0.0,"net_gex_1pct":708248.5616127328,"gross_gex_1pct":708248.5616127328,"call_oi":546,"put_oi":0},{"strike":45100.0,"call_gex_1pct":13891.8224796825,"put_gex_1pct":0.0,"net_gex_1pct":13891.8224796825,"gross_gex_1pct":13891.8224796825,"call_oi":11,"put_oi":0},{"strike":45200.0,"call_gex_1pct":20911.885267308375,"put_gex_1pct":0.0,"net_gex_1pct":20911.885267308375,"gross_gex_1pct":20911.885267308375,"call_oi":17,"put_oi":0},{"strike":45300.0,"call_gex_1pct":3596.175022271067,"put_gex_1pct":0.0,"net_gex_1pct":3596.175022271067,"gross_gex_1pct":3596.175022271067,"call_oi":3,"put_oi":0},{"strike":45400.0,"call_gex_1pct":8180.580572999118,"put_gex_1pct":0.0,"net_gex_1pct":8180.580572999118,"gross_gex_1pct":8180.580572999118,"call_oi":7,"put_oi":0},{"strike":45500.0,"call_gex_1pct":5699.119742770378,"put_gex_1pct":0.0,"net_gex_1pct":5699.119742770378,"gross_gex_1pct":5699.119742770378,"call_oi":5,"put_oi":0},{"strike":45600.0,"call_gex_1pct":5560.820459677136,"put_gex_1pct":0.0,"net_gex_1pct":5560.820459677136,"gross_gex_1pct":5560.820459677136,"call_oi":5,"put_oi":0},{"strike":45700.0,"call_gex_1pct":4342.440202946185,"put_gex_1pct":0.0,"net_gex_1pct":4342.440202946185,"gross_gex_1pct":4342.440202946185,"call_oi":4,"put_oi":0},{"strike":45800.0,"call_gex_1pct":12721.218899137648,"put_gex_1pct":0.0,"net_gex_1pct":12721.218899137648,"gross_gex_1pct":12721.218899137648,"call_oi":12,"put_oi":0},{"strike":45900.0,"call_gex_1pct":9320.242838619231,"put_gex_1pct":0.0,"net_gex_1pct":9320.242838619231,"gross_gex_1pct":9320.242838619231,"call_oi":9,"put_oi":0},{"strike":46000.0,"call_gex_1pct":273240.161241036,"put_gex_1pct":0.0,"net_gex_1pct":273240.161241036,"gross_gex_1pct":273240.161241036,"call_oi":270,"put_oi":0},{"strike":46100.0,"call_gex_1pct":9893.068915373085,"put_gex_1pct":0.0,"net_gex_1pct":9893.068915373085,"gross_gex_1pct":9893.068915373085,"call_oi":10,"put_oi":0},{"strike":46200.0,"call_gex_1pct":5804.734566325383,"put_gex_1pct":0.0,"net_gex_1pct":5804.734566325383,"gross_gex_1pct":5804.734566325383,"call_oi":6,"put_oi":0},{"strike":46300.0,"call_gex_1pct":2839.2134913028162,"put_gex_1pct":0.0,"net_gex_1pct":2839.2134913028162,"gross_gex_1pct":2839.2134913028162,"call_oi":3,"put_oi":0},{"strike":46400.0,"call_gex_1pct":926.1131134728063,"put_gex_1pct":0.0,"net_gex_1pct":926.1131134728063,"gross_gex_1pct":926.1131134728063,"call_oi":1,"put_oi":0},{"strike":46500.0,"call_gex_1pct":11785.073799172897,"put_gex_1pct":0.0,"net_gex_1pct":11785.073799172897,"gross_gex_1pct":11785.073799172897,"call_oi":13,"put_oi":0},{"strike":46600.0,"call_gex_1pct":1775.3248499095453,"put_gex_1pct":0.0,"net_gex_1pct":1775.3248499095453,"gross_gex_1pct":1775.3248499095453,"call_oi":2,"put_oi":0},{"strike":46700.0,"call_gex_1pct":11302.65471582429,"put_gex_1pct":0.0,"net_gex_1pct":11302.65471582429,"gross_gex_1pct":11302.65471582429,"call_oi":13,"put_oi":0},{"strike":46800.0,"call_gex_1pct":1703.6615936968446,"put_gex_1pct":0.0,"net_gex_1pct":1703.6615936968446,"gross_gex_1pct":1703.6615936968446,"call_oi":2,"put_oi":0},{"strike":46900.0,"call_gex_1pct":2504.4621879486845,"put_gex_1pct":0.0,"net_gex_1pct":2504.4621879486845,"gross_gex_1pct":2504.4621879486845,"call_oi":3,"put_oi":0},{"strike":47000.0,"call_gex_1pct":20459.433519743798,"put_gex_1pct":0.0,"net_gex_1pct":20459.433519743798,"gross_gex_1pct":20459.433519743798,"call_oi":25,"put_oi":0},{"strike":47100.0,"call_gex_1pct":8024.747921586074,"put_gex_1pct":0.0,"net_gex_1pct":8024.747921586074,"gross_gex_1pct":8024.747921586074,"call_oi":10,"put_oi":0},{"strike":47200.0,"call_gex_1pct":12593.419657083976,"put_gex_1pct":0.0,"net_gex_1pct":12593.419657083976,"gross_gex_1pct":12593.419657083976,"call_oi":16,"put_oi":0},{"strike":47300.0,"call_gex_1pct":772.1961770841136,"put_gex_1pct":0.0,"net_gex_1pct":772.1961770841136,"gross_gex_1pct":772.1961770841136,"call_oi":1,"put_oi":0},{"strike":47400.0,"call_gex_1pct":4546.652715292502,"put_gex_1pct":0.0,"net_gex_1pct":4546.652715292502,"gross_gex_1pct":4546.652715292502,"call_oi":6,"put_oi":0},{"strike":47500.0,"call_gex_1pct":79587.2495849976,"put_gex_1pct":0.0,"net_gex_1pct":79587.2495849976,"gross_gex_1pct":79587.2495849976,"call_oi":107,"put_oi":0},{"strike":47600.0,"call_gex_1pct":730.2686692318224,"put_gex_1pct":0.0,"net_gex_1pct":730.2686692318224,"gross_gex_1pct":730.2686692318224,"call_oi":1,"put_oi":0},{"strike":47700.0,"call_gex_1pct":4302.86959310955,"put_gex_1pct":0.0,"net_gex_1pct":4302.86959310955,"gross_gex_1pct":4302.86959310955,"call_oi":6,"put_oi":0},{"strike":47800.0,"call_gex_1pct":5635.340190048744,"put_gex_1pct":0.0,"net_gex_1pct":5635.340190048744,"gross_gex_1pct":5635.340190048744,"call_oi":8,"put_oi":0},{"strike":47900.0,"call_gex_1pct":3460.3501221607,"put_gex_1pct":0.0,"net_gex_1pct":3460.3501221607,"gross_gex_1pct":3460.3501221607,"call_oi":5,"put_oi":0},{"strike":48000.0,"call_gex_1pct":28563.648663948225,"put_gex_1pct":0.0,"net_gex_1pct":28563.648663948225,"gross_gex_1pct":28563.648663948225,"call_oi":42,"put_oi":0},{"strike":48100.0,"call_gex_1pct":141712.1022257187,"put_gex_1pct":0.0,"net_gex_1pct":141712.1022257187,"gross_gex_1pct":141712.1022257187,"call_oi":212,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 37,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-25→2026-11-26) | +2,000 | TAIFEX Proxy snapshots (2026-11-25) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 78,885 | 78,247 | +638 | 35,699 | 36,664 | -965 | +1,603 | TAIFEX Proxy |
| 投信 | 0 | 2,010 | -2,010 | 0 | 0 | +0 | -2,010 | TAIFEX Proxy |
| 自營商 | 80,461 | 73,504 | +6,957 | 25,013 | 27,277 | -2,264 | +9,221 | TAIFEX Proxy |
| 三大法人合計 | 159,346 | 153,761 | +5,585 | 60,712 | 63,941 | -3,229 | +8,814 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.44 | 12.99 | +0.45 | 4.24 | 4.40 | -0.16 | +0.62 | TAIFEX Proxy |
| 投信 | 0.00 | 0.47 | -0.47 | 0.00 | 0.00 | +0 | -0.47 | TAIFEX Proxy |
| 自營商 | 15.65 | 15.41 | +0.25 | 3.03 | 3.05 | -0.01 | +0.26 | TAIFEX Proxy |
| 三大法人合計 | 29.10 | 28.87 | +0.23 | 7.28 | 7.45 | -0.17 | +0.40 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 16,759 | TAIFEX Proxy |
| 買權空方 OI | 19,131 | TAIFEX Proxy |
| 買權多空淨 OI | -2,372 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-25→2026-11-26) | +997 | TAIFEX Proxy snapshots (2026-11-25) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 13,068 | TAIFEX Proxy |
| 賣權空方 OI | 15,506 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,438 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-25→2026-11-26) | -362 | TAIFEX Proxy snapshots (2026-11-25) |
- 資料日期：買權 2026-11-26／賣權 2026-11-26 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +6,060 | 2026-11-25→2026-11-26 | TAIFEX Proxy snapshots (2026-11-25) |
| 買權前十大 | +997 | 2026-11-25→2026-11-26 | TAIFEX Proxy snapshots (2026-11-25) |
| 賣權前十大 | -362 | 2026-11-25→2026-11-26 | TAIFEX Proxy snapshots (2026-11-25) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-26；本次報告產製時間：2026-11-27 08:39:26；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 未取得欄位 (1)：options.pos_change

## 五、資料來源、時間與完整性

- 台股現貨、TAIFEX 期貨／選擇權以 T0 為基準；海外指數、匯率、ADR、原油、黃金與 Bitcoin 採各來源最新可得報價。各表格均列示實際資料日期；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- otc_breadth：`TPEx 歷史市場現況 highlight_result.php`
- otc_turnover：`TPEx 歷史市場現況 highlight_result.php`
- otc：`漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)`
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-26；估值 1248 檔；1 檔採最近有效收盤價（價格日期 20261125 至 20261126）；Blave 同 T0 交叉驗證 159.6730%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`
- sbl_bal：`TWSE TWT72U（SLBNLB；上市+上櫃）`
- sbl_sale_bal_listed：`TWSE TWT93U（上市）`
- sbl_sale_bal_otc：`TPEx S47（上櫃）`
- sbl_sale_chg_listed：`TWSE TWT93U（上市）`
- sbl_sale_chg_otc：`TPEx S47（上櫃）`
- sbl_sale_bal：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- sbl_sale_chg：`TWSE TWT93U（上市） + TPEX S47（上櫃）`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：亞洲主要指數資料日期落後 T0 2026-11-26，已將舊行情排除並標示 unavailable；原始資料日期：香港恆生 2026-11-25、上海綜合 2026-11-25、深圳成分 2026-11-25
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；1 檔採最近有效收盤價（價格日期 20261125 至 20261126）。Blave 同 T0 交叉驗證 159.6730%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-26 非今日 2026-11-27，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：主力到期月份已由 202611W4 換至 202611F4；僅比較前後快照中相同主力月份的共同合約，不跨月份相減
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -491.8 | -106,275 | -583 | -1,580 | +638 | -965 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +212.1 | +104,920 | +4,002 | +0 | -2,010 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +128.7 | -2,410 | -1,550 | +121 | +6,957 | -2,264 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
