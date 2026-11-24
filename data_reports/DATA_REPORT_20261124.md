# DATA_REPORT_20261124

- 報告日期：`2026-11-25`
- T0 交易日期：`2026-11-24`
- 首次資料產出時間：`2026-11-25 07:48:22`
- 本次更新開始時間：`2026-11-25 07:48:22`
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
| 加權指數 | 40,122.35 | 點 | twse-proxy |
| 開盤 | 39,148.91 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 40,180.38 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 39,148.91 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 40,122.35 | 點 | twse-proxy |
| 漲跌點數 | 3,310.46 | 點 | twse-proxy |
| 漲跌幅 | +8.99 | % | twse-proxy |
| 成交金額 | 4,325.6 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 1,053 | twse-proxy |
| 下跌家數 | 26 | twse-proxy |
| 平盤家數 | 6 | twse-proxy |
| 漲停家數 | 335 | twse-proxy |
| 跌停家數 | 4 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 840 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 34 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 15 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 286 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 2 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -503.9 | 億元 | twse-proxy /institutional |
| 投信 | +97.6 | 億元 | twse-proxy /institutional |
| 自營商 | -810.3 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,216.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-24；估值 1247 檔；1 檔採最近有效收盤價（價格日期 20261123 至 20261124）；Blave 同 T0 交叉驗證 162.0710%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 5,823.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | +207.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 208,662 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | 13,773 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 162.07 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-24；估值 1247 檔；1 檔採最近有效收盤價（價格日期 20261123 至 20261124）；Blave 同 T0 交叉驗證 162.0710%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 34,833,134 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,479,035.224 | 2,130,412.26 | 20,609,447.484 | 張 |
| 借券賣出增減 | +38,166.881 | -11,629.303 | +26,537.578 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261124`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-25T07:48:34+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261124`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-25T07:48:35+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 4,325.6 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 432.7 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 4,758.3 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,201.09 | -36.08 | -0.50 | 2026-11-24 | 2026-11-24T23:48:35+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,733.54 | -356.03 | -1.48 | 2026-11-24 | 2026-11-24T23:48:35+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,214.17 | -531.93 | -1.99 | 2026-11-24 | 2026-11-24T23:48:35+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,018.70 | 423.39 | +0.85 | 2026-11-24 | 2026-11-24T23:48:35+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 8,832.50 | -755.55 | -7.88 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 26.36 | -0.26 | -0.98 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | unavailable | unavailable | unavailable | 2026-11-20 | 2026-11-24T23:48:36+00:00 | Asia/Tokyo | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 韓國KOSPI | ^KS11 | unavailable | unavailable | unavailable | 2026-11-23 | 2026-11-24T23:48:36+00:00 | Asia/Seoul | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 香港恆生 | ^HSI | unavailable | unavailable | unavailable | 2026-11-23 | 2026-11-24T23:48:36+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 上海綜合 | 000001.SS | unavailable | unavailable | unavailable | 2026-11-23 | 2026-11-24T23:48:36+00:00 | Asia/Shanghai | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 深圳成分 | 399001.SZ | unavailable | unavailable | unavailable | 2026-11-23 | 2026-11-24T23:48:36+00:00 | Asia/Shanghai | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,204.75 | -49.75 | -0.69 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,220.00 | -588.00 | -2.19 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,005.00 | 328.00 | +0.66 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,685.60 | 11.50 | +0.43 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.63 | 0.00 | 24-NOV-26 | 2026-11-24T23:48:57+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.90 | -0.01 | 2026-11-24 | 2026-11-24T23:48:57+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.33 | 0.00 | 24-NOV-26 | 2026-11-24T23:48:57+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.29 | -0.00 | 2026-11-24 | 2026-11-24T23:48:57+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.92 | -0.03 | -0.11 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.85 | -0.47 | -0.45 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.28 | 0.35 | +0.22 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.28 | -1.03 | -0.08 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 349.20 | -14.40 | -3.96 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.40 | -0.99 | -6.88 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 29.33 | -2.55 | -8.00 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 81.61 | 1.44 | +1.80 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,558.50 | -92.90 | -2.54 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 59,693.88 | -1,517.11 | -2.48 | 2026-11-24 | 2026-11-24T23:48:36+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：大盤飆3310點創紀錄 台積領621檔齊亮漲停燈
  - 來源：Yahoo 台股；發布時間：2026-11-24T09:24:17Z；台北時間：2026-11-24 17:24
  - 摘要：台股飆漲3310點重返四萬大關，改寫史上最大收盤漲點！黃仁勳回任輝達執行長，帶動台股今(24)日強彈，加權指數終場上漲3310.46點、漲幅8.99%，收40122.35點，上市成交金額縮至4203.07億元，創今年新低量。大盤開盤跳空上漲
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E9%87%8D%E7%A3%85%E5%9B%9E%E6%AD%B8%E5%8F%B0%E8%82%A1%E9%A3%863310%E5%8F%B2%E4%B8%8A%E6%9C%80%E5%A4%A7%E6%BC%B2%E9%BB%9E%EF%BC%81%E5%8F%B0%E7%A9%8D%E9%9B%BB%E9%A0%98%E4%B8%8A%E5%B8%82%E6%AB%83621%E6%AA%94%E6%BC%B2%E5%81%9C%E3%80%8C%E7%91%A4%E6%B1%A0%E9%87%91%E6%AF%8D%E3%80%8D%E6%8B%BF%E4%B8%8B%E5%90%B8%E9%87%91%E7%8E%8B%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-092417776.html
- 事件2：0050反1也翻車 爆違約交割近4千萬
  - 來源：Yahoo 台股；發布時間：2026-11-24T10:14:46Z；台北時間：2026-11-24 18:14
  - 摘要：雖然台股暴漲3310點站回4萬點，但違約交割潮還沒結束！台股上周五（11月20日）下跌 2,393.60點，創下台股史上單日第三大收盤跌點紀錄，「T+2」交割餘震仍在發酵。證交所今（24）日盤後公布最新違約交割資訊，元大台灣50反1（006
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%9F%AD%E8%8F%9C%E7%BF%BB%E8%BB%8A%E6%BD%AE1%EF%BC%81%E5%8F%B0%E8%82%A1%E6%9A%B4%E6%BC%B2%E5%89%8D%E8%B2%B70050%E5%8F%8D1-%E9%81%95%E7%B4%84%E4%BA%A4%E5%89%B2%E8%BF%914%E5%8D%83%E8%90%AC%E5%85%83-104658511.html
- 事件3：台股上演V型大反攻 金管會談限空令去留
  - 來源：Yahoo 台股；發布時間：2026-11-24T10:19:22Z；台北時間：2026-11-24 18:19
  - 摘要：AI教父黃仁勳回鍋任輝達執行長和董事，台股今（24日）天V型反彈，金管會先前祭出三波限空令，隨著股市回穩，市場關注救市措施是否退場？金管會表示，將觀察相關數據變化，持續觀察資本市場變化，適時調整或恢復。金管會也統計，台股先前重挫，今年前1…
  - 原文連結：https://tw.stock.yahoo.com/news/ai%E6%95%99%E7%88%B6%E5%A4%A7%E5%8F%8D%E6%94%BB-%E9%99%90%E7%A9%BA%E4%BB%A4%E9%80%80%E5%A0%B4-%E9%87%91%E7%AE%A1%E6%9C%83%E6%B2%92%E9%AC%86%E5%8F%A3-101922892.html
- 事件4：吳東亮喊鬆綁處置股 證交所周五聚焦4大方向
  - 來源：Yahoo 台股；發布時間：2026-11-24T09:43:38Z；台北時間：2026-11-24 17:43
  - 摘要：行政院長卓榮泰23日召開產業座談會，據轉述，工商協進會理事長吳東亮提出建言，表示現行處置股票制度要求買方預收款項，在股市下跌時，可能使市場買盤減少，甚至引發流動性問題，呼籲證交所檢討台股大跌時放寬。金管會證期局副局長黃仲豪今（24）日下午證
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%90%B3%E6%9D%B1%E4%BA%AE%E5%BB%BA%E8%AD%B0%E6%94%BE%E5%AF%AC%E8%99%95%E7%BD%AE%E8%82%A1%E7%A5%A8-%E9%87%91%E7%AE%A1%E6%9C%83%EF%BC%9A%E5%91%A8%E4%BA%94%E9%96%8B%E6%9C%834%E6%96%B9%E5%90%91%E8%A8%8E%E8%AB%96-094338102.html
- 事件5：AI疑慮未散 陳俊聖看應用「需求一定會上去」
  - 來源：Yahoo 台股；發布時間：2026-11-24T10:05:43Z；台北時間：2026-11-24 18:05
  - 摘要：（中央社記者江明晏台北2026年11月24日電）針對輝達（NVIDIA）執行長黃仁勳回任，宏碁(2353)董事長陳俊聖表示，歡迎他回歸產業，也歡迎他明年再到台灣來參加COMPUTEX，對這件事最好的形容就是「非常戲劇化」，AI應用端肯定持續
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%AB%87%E9%BB%83%E4%BB%81%E5%8B%B3%E5%9B%9E%E4%BB%BB%E8%BC%9D%E9%81%94-%E9%99%B3%E4%BF%8A%E8%81%96-%E9%9D%9E%E5%B8%B8%E6%88%B2%E5%8A%87%E5%8C%96-ai%E9%9C%80%E6%B1%82-%E5%AE%9A%E6%9C%83%E4%B8%8A%E5%8E%BB-100543246.html
- 事件6：台股反攻拚打第二隻腳 法人：短線還會震盪 年底挑戰46,000點
  - 來源：Yahoo 台股；發布時間：2026-11-24T22:35:38Z；台北時間：2026-11-25 06:35
  - 摘要：黃仁勳重掌輝達（NVIDIA）執行長震撼全球科技業，激勵台股昨（24）日飆漲3,310點收40,122點，創史上最大漲點，漲幅8.99%史上次高，一口氣收復5日線、年線及4萬點大關。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%8F%8D%E6%94%BB%E6%8B%9A%E6%89%93%E7%AC%AC%E4%BA%8C%E9%9A%BB%E8%85%B3-%E6%B3%95%E4%BA%BA-%E7%9F%AD%E7%B7%9A%E9%82%84%E6%9C%83%E9%9C%87%E7%9B%AA-%E5%B9%B4%E5%BA%95%E6%8C%91%E6%88%B046-000%E9%BB%9E-223538591.html
- 事件7：Federal Reserve announces College Fed Challenge winners
  - 來源：Federal Reserve；發布時間：Fri, 20 Nov 2026 21:15:00 GMT；台北時間：2026-11-21 05:15
  - 摘要：Federal Reserve announces College Fed Challenge winners
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261120b.htm
- 事件8：Federal Reserve Board releases results from survey of senior financial officers at banks about their strategies and practices for managing reserve balances
  - 來源：Federal Reserve；發布時間：Fri, 20 Nov 2026 15:00:00 GMT；台北時間：2026-11-20 23:00
  - 摘要：Federal Reserve Board releases results from survey of senior financial officers at banks about their strategies and practices for managing reserve bal
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261120a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of First Security Bancorp
  - 來源：Federal Reserve；發布時間：Thu, 19 Nov 2026 16:00:00 GMT；台北時間：2026-11-20 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of First Security Bancorp
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261119a.htm
- 事件10：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 來源：Federal Reserve；發布時間：Wed, 18 Nov 2026 19:00:00 GMT；台北時間：2026-11-19 03:00
  - 摘要：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm
- 事件11：Consumer confidence shoots up after Democrats' midterm victories — though inflation worries persist
  - 來源：CNBC；發布時間：Tue, 24 Nov 2026 18:34:43 GMT；台北時間：2026-11-25 02:34
  - 摘要：The Conference Board survey released Tuesday showed improvement across the board, with the headline confidence index jumping to 103.3.
  - 原文連結：https://www.cnbc.com/2026/11/24/consumer-confidence-november-election-midterm.html
- 事件12：Trump Account contributions from friends and family pass $1 billion mark, Treasury says
  - 來源：CNBC；發布時間：Tue, 24 Nov 2026 22:18:47 GMT；台北時間：2026-11-25 06:18
  - 摘要：Trump Account contributions from friends and family have passed $1 billion, according to the Treasury Department. Here's what families need to know.
  - 原文連結：https://www.cnbc.com/2026/11/24/trump-accounts-family-contributions-billion.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-24

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,124 | 點 | TAIFEX Proxy |
| 最高價 | 40,324 | 點 | TAIFEX Proxy |
| 最低價 | 39,966 | 點 | TAIFEX Proxy |
| 收盤價 | 40,324 | 點 | TAIFEX Proxy |
| 漲跌點數 | +3,665 | 點 | TAIFEX Proxy |
| 漲跌幅 | +10.00 | % | TAIFEX Proxy |
| 成交量 | 18,862 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 40,324 / 39,966 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,772 | 點 | TAIFEX Proxy |
| 最高價 | 40,900 | 點 | TAIFEX Proxy |
| 最低價 | 37,730 | 點 | TAIFEX Proxy |
| 收盤價 | 38,482 | 點 | TAIFEX Proxy |
| 漲跌點數 | -1,842 | 點 | TAIFEX Proxy |
| 漲跌幅 | -4.57 | % | TAIFEX Proxy |
| 成交量 | 95,642 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,900 / 37,730 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,852 | TAIFEX Proxy |
| 外資空方 OI | 116,034 | TAIFEX Proxy |
| 外資多空淨 OI | -103,182 | TAIFEX Proxy |
| 投信多方 OI | 101,301 | TAIFEX Proxy |
| 投信空方 OI | 3,287 | TAIFEX Proxy |
| 投信多空淨 OI | +98,014 | TAIFEX Proxy |
| 自營商多方 OI | 4,666 | TAIFEX Proxy |
| 自營商空方 OI | 4,899 | TAIFEX Proxy |
| 自營商多空淨 OI | -233 | TAIFEX Proxy |
| 三大法人合計多方 OI | 118,819 | TAIFEX Proxy |
| 三大法人合計空方 OI | 124,220 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,401 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +250 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +4,449 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,551 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 106,016 | TAIFEX Proxy |
| 前十大交易人空方 OI | 96,213 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,803 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-23→2026-11-24) | +5,084 | TAIFEX Proxy snapshots (2026-11-23) |
- 資料日期：2026-11-24 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 68,962 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 69,654 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -692 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 55,873 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 59,765 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -3,892 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +3,200 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +4,449 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +754 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +3,695 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,214 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +2,026 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -3,240 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,543 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,112 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | +201.8 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -96.7 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,324 | TAIFEX Proxy |
| 加權指數價格 | 40,122.35 | twse-proxy |
| 台指期與加權指數價差 | +201.65 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +0.50 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +201.65 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -1,842 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,324 | 38,482 | +1,842 | TAIFEX Proxy |
| 成交量 | 18,862 | 95,642 | -76,780 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+3,148（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 68,962 | 69,654 | -692 | 55,873 | 59,765 | -3,892 | +3,200 | 12,852 | 116,034 | -103,182 | +250 | TAIFEX Proxy |
| 投信 | 4,449 | 0 | +4,449 | 754 | 0 | +754 | +3,695 | 101,301 | 3,287 | +98,014 | +4,449 | TAIFEX Proxy |
| 自營商 | 4,552 | 5,766 | -1,214 | 3,841 | 1,815 | +2,026 | -3,240 | 4,666 | 4,899 | -233 | -1,551 | TAIFEX Proxy |
| 三大法人合計 | 77,963 | 75,420 | +2,543 | 60,468 | 61,580 | -1,112 | +3,655 | 118,819 | 124,220 | -5,401 | +3,148 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 106,016 | TAIFEX Proxy |
| 前十大交易人空方 OI | 96,213 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +9,803 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-23→2026-11-24) | +5,084 | TAIFEX Proxy snapshots (2026-11-23) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 83.53% | TAIFEX Proxy |
| 夜盤漲跌點數 | -1,842 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -3,892 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-24 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W4 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-25 07:48:22 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 159,760 | TAIFEX Proxy |
| Call 總未平倉量 OI | 104,473 | TAIFEX Proxy |
| Call OI 增減（共同合約） | unavailable | unavailable |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 104,072 | TAIFEX Proxy |
| Put 總未平倉量 OI | 47,405 | TAIFEX Proxy |
| Put OI 增減（共同合約） | unavailable | unavailable |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.54 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.20 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.45 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-23→2026-11-24) | 11.09 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-23→2026-11-24) | 15.06 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 23,479 | TAIFEX Proxy |
| 外資 Call日賣 | 24,716 | TAIFEX Proxy |
| 外資 Call日淨 | -1,237 | TAIFEX Proxy |
| 外資 Put日買 | 16,909 | TAIFEX Proxy |
| 外資 Put日賣 | 15,933 | TAIFEX Proxy |
| 外資 Put日淨 | +976 | TAIFEX Proxy |
| 外資 Call夜買 | 47,719 | TAIFEX Proxy |
| 外資 Call夜賣 | 49,570 | TAIFEX Proxy |
| 外資 Call夜淨 | -1,851 | TAIFEX Proxy |
| 外資 Put夜買 | 49,608 | TAIFEX Proxy |
| 外資 Put夜賣 | 44,631 | TAIFEX Proxy |
| 外資 Put夜淨 | +4,977 | TAIFEX Proxy |
| 外資 日盤淨總量 | -2,213 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +614 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -4,001 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 38,760 | TAIFEX Proxy |
| 自營商 Call日賣 | 51,825 | TAIFEX Proxy |
| 自營商 Call日淨 | -13,065 | TAIFEX Proxy |
| 自營商 Put日買 | 27,493 | TAIFEX Proxy |
| 自營商 Put日賣 | 29,478 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,985 | TAIFEX Proxy |
| 自營商 Call夜買 | 27,583 | TAIFEX Proxy |
| 自營商 Call夜賣 | 32,621 | TAIFEX Proxy |
| 自營商 Call夜淨 | -5,038 | TAIFEX Proxy |
| 自營商 Put夜買 | 30,089 | TAIFEX Proxy |
| 自營商 Put夜賣 | 34,572 | TAIFEX Proxy |
| 自營商 Put夜淨 | -4,483 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,080 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -8,027 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +2,498 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 41,000 | 11,563 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 9,141 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 6,577 | TAIFEX Proxy |
| Call OI 最大履約價 | 41,000 | 11,563 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 41,000 | 11,563 | 11.07% | TAIFEX Proxy |
| C2 | 43,000 | 9,141 | 8.75% | TAIFEX Proxy |
| C3 | 44,000 | 6,577 | 6.3% | TAIFEX Proxy |
| C4 | 42,000 | 4,327 | 4.14% | TAIFEX Proxy |
| C5 | 42,500 | 3,305 | 3.16% | TAIFEX Proxy |
| C6 | 35,700 | 3,076 | 2.94% | TAIFEX Proxy |
| C7 | 40,000 | 2,849 | 2.73% | TAIFEX Proxy |
| C8 | 35,800 | 2,635 | 2.52% | TAIFEX Proxy |
| C9 | 35,300 | 2,531 | 2.42% | TAIFEX Proxy |
| C10 | 45,000 | 2,361 | 2.26% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 32,400 | 3,635 | TAIFEX Proxy |
| Put OI 第2大履約價 | 34,500 | 2,487 | TAIFEX Proxy |
| Put OI 第3大履約價 | 38,000 | 2,476 | TAIFEX Proxy |
| Put OI 最大履約價 | 32,400 | 3,635 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 32,400 | 3,635 | 7.67% | TAIFEX Proxy |
| P2 | 34,500 | 2,487 | 5.25% | TAIFEX Proxy |
| P3 | 38,000 | 2,476 | 5.22% | TAIFEX Proxy |
| P4 | 39,000 | 2,439 | 5.15% | TAIFEX Proxy |
| P5 | 36,000 | 2,112 | 4.46% | TAIFEX Proxy |
| P6 | 37,000 | 2,003 | 4.23% | TAIFEX Proxy |
| P7 | 35,000 | 1,444 | 3.05% | TAIFEX Proxy |
| P8 | 40,000 | 1,384 | 2.92% | TAIFEX Proxy |
| P9 | 39,500 | 1,151 | 2.43% | TAIFEX Proxy |
| P10 | 35,500 | 1,135 | 2.39% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | unavailable | unavailable |
| Call OI 減少最多的履約價（共同合約） | unavailable | unavailable |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | unavailable | unavailable |
| Put OI 減少最多的履約價（共同合約） | unavailable | unavailable |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 41,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 前日同月份 Chain 不完整（primary_expiry_chain_empty） |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 32,400 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 前日同月份 Chain 不完整（primary_expiry_chain_empty） |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 41,000.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611W4 | TAIFEX Proxy |
| 資料日期 | 2026-11-24 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 37,924.75 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611W4 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 104,473 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 104,473 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 47,405 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 46,581 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-24 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：36,110.11～44,134.58
- 搜尋步長／計算次數：10.00／183
- 起點／終點 Net GEX：-1,738,715,206.79／7,584,880.34
- 搜尋區間最低／最高 Net GEX：-1,738,715,206.79／7,584,880.34
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-24","chain_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":540,"delta_rows":540},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":292,"delta_rows":292},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：34,104.00～46,140.70
- 搜尋步長／計算次數：10.00／1205
- 起點／終點 Net GEX：-1,169,955,189.72／4,946,741,030.63
- 搜尋區間最低／最高 Net GEX：-1,817,522,022.15／10,554,293,715.41
- 正負號交叉次數：1
- 擴大區間診斷 Flip：37,924.76

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 4,341,556,486.98 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 10,075,150,859.20 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 270 | 資料日期：2026-11-24 |
| 正 Net GEX 最大履約價 | 41,000 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 39,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：41,000（1,480,664,222.88 NT$）、43,000（553,739,688.89 NT$）、42,000（458,637,672.81 NT$）、42,500（280,965,332.47 NT$）、41,500（199,246,965.30 NT$）
- 負 Net GEX Top 5：39,000（-301,550,161.38 NT$）、39,500（-131,590,830.32 NT$）、38,000（-87,194,949.34 NT$）、40,000（-65,567,267.20 NT$）、37,800（-46,715,400.05 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-24","underlying":40122.35,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":4341556486.975351,"gross_gex_1pct":10075150859.197054,"gamma_diagnostics":{"chain_rows":540,"delta_rows":540,"matched_strike_keys":540,"positive_oi_settlement_eligible":465,"invalid_oi":75,"invalid_settlement":0,"below_intrinsic":63,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":402},"formal_flip_diagnostics":{"search_lower_underlying":36110.115,"search_upper_underlying":44134.585,"step":10,"evaluations":183,"start_net_gex_1pct":-1738715206.7881386,"end_net_gex_1pct":7584880.33761047,"min_net_gex_1pct":-1738715206.7881386,"max_net_gex_1pct":7584880.33761047,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":37923.9975,"upper_underlying":37933.9975,"estimated_underlying":37924.75732734563,"lower_net_gex_1pct":-1076339.4924467748,"upper_net_gex_1pct":13089240.341362631},"wide_range_flip_diagnostics":{"search_lower_underlying":34103.9975,"search_upper_underlying":46140.70249999999,"reference_underlying":40122.35,"step":10,"evaluations":1205,"start_net_gex_1pct":-1169955189.72342,"end_net_gex_1pct":4946741030.634797,"min_net_gex_1pct":-1817522022.1535165,"max_net_gex_1pct":10554293715.405218,"zero_crossings":1,"found":true,"selected_crossing_distance":2197.5926726543694},"expiry_selection_diagnostics":{"requested_date":"2026-11-24","chain_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":540,"delta_rows":540},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":292,"delta_rows":292},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":32400.0,"call_gex_1pct":0.0,"put_gex_1pct":-773878.1715792073,"net_gex_1pct":-773878.1715792073,"gross_gex_1pct":773878.1715792073,"call_oi":0,"put_oi":3635},{"strike":32500.0,"call_gex_1pct":0.0,"put_gex_1pct":-131748.06875869774,"net_gex_1pct":-131748.06875869774,"gross_gex_1pct":131748.06875869774,"call_oi":0,"put_oi":603},{"strike":32600.0,"call_gex_1pct":0.0,"put_gex_1pct":-85903.48862963248,"net_gex_1pct":-85903.48862963248,"gross_gex_1pct":85903.48862963248,"call_oi":0,"put_oi":383},{"strike":32700.0,"call_gex_1pct":0.0,"put_gex_1pct":-39384.28803084306,"net_gex_1pct":-39384.28803084306,"gross_gex_1pct":39384.28803084306,"call_oi":0,"put_oi":171},{"strike":32800.0,"call_gex_1pct":18492.67059023236,"put_gex_1pct":-31701.508485634615,"net_gex_1pct":-13208.837895402256,"gross_gex_1pct":50194.179075866974,"call_oi":1,"put_oi":134},{"strike":32900.0,"call_gex_1pct":0.0,"put_gex_1pct":-21148.508846440007,"net_gex_1pct":-21148.508846440007,"gross_gex_1pct":21148.508846440007,"call_oi":0,"put_oi":87},{"strike":33000.0,"call_gex_1pct":58528.11769482998,"put_gex_1pct":-267843.85223024443,"net_gex_1pct":-209315.73453541443,"gross_gex_1pct":326371.96992507443,"call_oi":3,"put_oi":1072},{"strike":33100.0,"call_gex_1pct":20146.835087058145,"put_gex_1pct":-45727.59846018992,"net_gex_1pct":-25580.763373131773,"gross_gex_1pct":65874.43354724806,"call_oi":1,"put_oi":178},{"strike":33200.0,"call_gex_1pct":20564.486140864246,"put_gex_1pct":-98292.90243431051,"net_gex_1pct":-77728.41629344627,"gross_gex_1pct":118857.38857517476,"call_oi":1,"put_oi":372},{"strike":33300.0,"call_gex_1pct":21215.709395070524,"put_gex_1pct":-34255.02969939269,"net_gex_1pct":-13039.320304322166,"gross_gex_1pct":55470.73909446321,"call_oi":1,"put_oi":126},{"strike":33400.0,"call_gex_1pct":0.0,"put_gex_1pct":-65199.26188199697,"net_gex_1pct":-65199.26188199697,"gross_gex_1pct":65199.26188199697,"call_oi":0,"put_oi":233},{"strike":33500.0,"call_gex_1pct":67559.35713118438,"put_gex_1pct":-101708.5843990983,"net_gex_1pct":-34149.22726791391,"gross_gex_1pct":169267.94153028267,"call_oi":3,"put_oi":353},{"strike":33600.0,"call_gex_1pct":69524.32664765969,"put_gex_1pct":-91410.90249563259,"net_gex_1pct":-21886.575847972897,"gross_gex_1pct":160935.2291432923,"call_oi":3,"put_oi":308},{"strike":33700.0,"call_gex_1pct":47666.077271304384,"put_gex_1pct":-43428.36700358947,"net_gex_1pct":4237.710267714916,"gross_gex_1pct":91094.44427489385,"call_oi":2,"put_oi":142},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-45400.907643328945,"net_gex_1pct":-45400.907643328945,"gross_gex_1pct":45400.907643328945,"call_oi":0,"put_oi":144},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-48449.57694529633,"net_gex_1pct":-48449.57694529633,"gross_gex_1pct":48449.57694529633,"call_oi":0,"put_oi":149},{"strike":34000.0,"call_gex_1pct":258363.6273408765,"put_gex_1pct":-342212.9289631383,"net_gex_1pct":-83849.30162226182,"gross_gex_1pct":600576.5563040148,"call_oi":10,"put_oi":1020},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-54719.61618369954,"net_gex_1pct":-54719.61618369954,"gross_gex_1pct":54719.61618369954,"call_oi":0,"put_oi":158},{"strike":34200.0,"call_gex_1pct":54600.7149806886,"put_gex_1pct":-56511.47141178997,"net_gex_1pct":-1910.7564311013703,"gross_gex_1pct":111112.18639247857,"call_oi":2,"put_oi":158},{"strike":34300.0,"call_gex_1pct":224513.87694896918,"put_gex_1pct":-50629.60399497078,"net_gex_1pct":173884.2729539984,"gross_gex_1pct":275143.48094393994,"call_oi":8,"put_oi":137},{"strike":34400.0,"call_gex_1pct":143749.61455791295,"put_gex_1pct":-79463.91522623166,"net_gex_1pct":64285.69933168129,"gross_gex_1pct":223213.5297841446,"call_oi":5,"put_oi":208},{"strike":34500.0,"call_gex_1pct":4896727.050760717,"put_gex_1pct":-982722.8307471445,"net_gex_1pct":3914004.220013573,"gross_gex_1pct":5879449.881507861,"call_oi":166,"put_oi":2487},{"strike":34600.0,"call_gex_1pct":2479195.444618852,"put_gex_1pct":-169701.67621051276,"net_gex_1pct":2309493.768408339,"gross_gex_1pct":2648897.1208293648,"call_oi":82,"put_oi":415},{"strike":34700.0,"call_gex_1pct":743025.9184227732,"put_gex_1pct":-105006.27103043173,"net_gex_1pct":638019.6473923415,"gross_gex_1pct":848032.189453205,"call_oi":24,"put_oi":248},{"strike":34800.0,"call_gex_1pct":1900579.5630592592,"put_gex_1pct":-78961.13976155099,"net_gex_1pct":1821618.4232977082,"gross_gex_1pct":1979540.7028208103,"call_oi":60,"put_oi":180},{"strike":34900.0,"call_gex_1pct":64255017.847672075,"put_gex_1pct":-102320.39145831096,"net_gex_1pct":64152697.456213765,"gross_gex_1pct":64357338.239130385,"call_oi":1984,"put_oi":225},{"strike":35000.0,"call_gex_1pct":71180290.97740492,"put_gex_1pct":-681172.6624039075,"net_gex_1pct":70499118.31500101,"gross_gex_1pct":71861463.63980883,"call_oi":2152,"put_oi":1444},{"strike":35050.0,"call_gex_1pct":133593.9523188325,"put_gex_1pct":-32197.723146175947,"net_gex_1pct":101396.22917265656,"gross_gex_1pct":165791.67546500845,"call_oi":4,"put_oi":67},{"strike":35100.0,"call_gex_1pct":3171461.1832795762,"put_gex_1pct":-64633.34048573003,"net_gex_1pct":3106827.842793846,"gross_gex_1pct":3236094.5237653065,"call_oi":94,"put_oi":132},{"strike":35150.0,"call_gex_1pct":306386.7082243182,"put_gex_1pct":-17963.49748876118,"net_gex_1pct":288423.210735557,"gross_gex_1pct":324350.2057130794,"call_oi":9,"put_oi":36},{"strike":35200.0,"call_gex_1pct":70834208.40316546,"put_gex_1pct":-73237.16338956829,"net_gex_1pct":70760971.2397759,"gross_gex_1pct":70907445.56655502,"call_oi":2058,"put_oi":144},{"strike":35250.0,"call_gex_1pct":348015.1375600769,"put_gex_1pct":-25405.173277324393,"net_gex_1pct":322609.9642827525,"gross_gex_1pct":373420.3108374013,"call_oi":10,"put_oi":49},{"strike":35300.0,"call_gex_1pct":88834606.18551628,"put_gex_1pct":-63965.60646255769,"net_gex_1pct":88770640.57905373,"gross_gex_1pct":88898571.79197884,"call_oi":2531,"put_oi":121},{"strike":35350.0,"call_gex_1pct":0.0,"put_gex_1pct":-306213.403847503,"net_gex_1pct":-306213.403847503,"gross_gex_1pct":306213.403847503,"call_oi":0,"put_oi":568},{"strike":35400.0,"call_gex_1pct":3031225.4266810156,"put_gex_1pct":-558683.1820721087,"net_gex_1pct":2472542.244608907,"gross_gex_1pct":3589908.6087531243,"call_oi":85,"put_oi":1016},{"strike":35450.0,"call_gex_1pct":0.0,"put_gex_1pct":-47694.96989561475,"net_gex_1pct":-47694.96989561475,"gross_gex_1pct":47694.96989561475,"call_oi":0,"put_oi":51},{"strike":35500.0,"call_gex_1pct":5277243.192184365,"put_gex_1pct":-1082853.3070171822,"net_gex_1pct":4194389.885167183,"gross_gex_1pct":6360096.499201547,"call_oi":145,"put_oi":1135},{"strike":35550.0,"call_gex_1pct":109983.35771738688,"put_gex_1pct":-48674.39960892476,"net_gex_1pct":61308.958108462124,"gross_gex_1pct":158657.75732631164,"call_oi":3,"put_oi":50},{"strike":35600.0,"call_gex_1pct":3728852.204820646,"put_gex_1pct":-225528.08714028783,"net_gex_1pct":3503324.1176803582,"gross_gex_1pct":3954380.2919609337,"call_oi":101,"put_oi":227},{"strike":35650.0,"call_gex_1pct":334530.22893860337,"put_gex_1pct":-43609.057484880796,"net_gex_1pct":290921.1714537226,"gross_gex_1pct":378139.28642348415,"call_oi":9,"put_oi":43},{"strike":35700.0,"call_gex_1pct":115348302.71670736,"put_gex_1pct":-164638.01586171525,"net_gex_1pct":115183664.70084564,"gross_gex_1pct":115512940.73256908,"call_oi":3076,"put_oi":159},{"strike":35750.0,"call_gex_1pct":303347.2152260286,"put_gex_1pct":-48114.39390137302,"net_gex_1pct":255232.82132465555,"gross_gex_1pct":351461.6091274016,"call_oi":8,"put_oi":34},{"strike":35800.0,"call_gex_1pct":101038761.31193458,"put_gex_1pct":-303503.26978754415,"net_gex_1pct":100735258.04214703,"gross_gex_1pct":101342264.58172213,"call_oi":2635,"put_oi":210},{"strike":35850.0,"call_gex_1pct":930698.0137552468,"put_gex_1pct":-62006.631041900095,"net_gex_1pct":868691.3827133466,"gross_gex_1pct":992704.6447971469,"call_oi":24,"put_oi":42},{"strike":35900.0,"call_gex_1pct":6824491.640276909,"put_gex_1pct":-386164.75556269736,"net_gex_1pct":6438326.884714211,"gross_gex_1pct":7210656.395839606,"call_oi":174,"put_oi":256},{"strike":35950.0,"call_gex_1pct":833101.3131138267,"put_gex_1pct":-179402.01807338206,"net_gex_1pct":653699.2950404446,"gross_gex_1pct":1012503.3311872088,"call_oi":21,"put_oi":95},{"strike":36000.0,"call_gex_1pct":39126875.58160441,"put_gex_1pct":-4076557.811502163,"net_gex_1pct":35050317.77010225,"gross_gex_1pct":43203433.39310658,"call_oi":975,"put_oi":2112},{"strike":36050.0,"call_gex_1pct":1055531.308163576,"put_gex_1pct":-258101.36685538772,"net_gex_1pct":797429.9413081884,"gross_gex_1pct":1313632.6750189639,"call_oi":26,"put_oi":112},{"strike":36100.0,"call_gex_1pct":7064627.496902775,"put_gex_1pct":-1293160.3193334732,"net_gex_1pct":5771467.177569302,"gross_gex_1pct":8357787.816236248,"call_oi":172,"put_oi":436},{"strike":36150.0,"call_gex_1pct":1412990.6170885295,"put_gex_1pct":-281057.69426544267,"net_gex_1pct":1131932.9228230868,"gross_gex_1pct":1694048.3113539722,"call_oi":34,"put_oi":73},{"strike":36200.0,"call_gex_1pct":8680871.728731697,"put_gex_1pct":-1471208.3721824752,"net_gex_1pct":7209663.356549222,"gross_gex_1pct":10152080.100914173,"call_oi":207,"put_oi":300},{"strike":36250.0,"call_gex_1pct":1442858.422413684,"put_gex_1pct":-817601.9679235697,"net_gex_1pct":625256.4544901142,"gross_gex_1pct":2260460.390337254,"call_oi":34,"put_oi":144},{"strike":36300.0,"call_gex_1pct":4552403.202501447,"put_gex_1pct":-1923340.1824276268,"net_gex_1pct":2629063.02007382,"gross_gex_1pct":6475743.384929074,"call_oi":106,"put_oi":299},{"strike":36350.0,"call_gex_1pct":1347490.0790493467,"put_gex_1pct":-480810.91426034615,"net_gex_1pct":866679.1647890005,"gross_gex_1pct":1828300.993309693,"call_oi":31,"put_oi":67},{"strike":36400.0,"call_gex_1pct":7171669.051188962,"put_gex_1pct":-1725396.5233301818,"net_gex_1pct":5446272.52785878,"gross_gex_1pct":8897065.574519143,"call_oi":163,"put_oi":218},{"strike":36450.0,"call_gex_1pct":668087.1929560377,"put_gex_1pct":-683520.0528203441,"net_gex_1pct":-15432.859864306403,"gross_gex_1pct":1351607.2457763818,"call_oi":15,"put_oi":79},{"strike":36500.0,"call_gex_1pct":17269955.074351877,"put_gex_1pct":-5635400.762583796,"net_gex_1pct":11634554.311768081,"gross_gex_1pct":22905355.836935673,"call_oi":383,"put_oi":600},{"strike":36550.0,"call_gex_1pct":1734877.007171158,"put_gex_1pct":-948260.6975397657,"net_gex_1pct":786616.3096313922,"gross_gex_1pct":2683137.7047109236,"call_oi":38,"put_oi":92},{"strike":36600.0,"call_gex_1pct":6657071.271270525,"put_gex_1pct":-2906283.7891177856,"net_gex_1pct":3750787.482152739,"gross_gex_1pct":9563355.06038831,"call_oi":144,"put_oi":259},{"strike":36650.0,"call_gex_1pct":1638582.1078005019,"put_gex_1pct":-3010394.512750323,"net_gex_1pct":-1371812.404949821,"gross_gex_1pct":4648976.620550824,"call_oi":35,"put_oi":248},{"strike":36700.0,"call_gex_1pct":6685647.170910138,"put_gex_1pct":-3017654.062008304,"net_gex_1pct":3667993.1089018336,"gross_gex_1pct":9703301.232918441,"call_oi":141,"put_oi":231},{"strike":36750.0,"call_gex_1pct":3554069.2853639578,"put_gex_1pct":-1527955.1970469553,"net_gex_1pct":2026114.0883170024,"gross_gex_1pct":5082024.482410913,"call_oi":74,"put_oi":108},{"strike":36800.0,"call_gex_1pct":10217153.12816398,"put_gex_1pct":-12297096.877522478,"net_gex_1pct":-2079943.7493584976,"gross_gex_1pct":22514250.00568646,"call_oi":210,"put_oi":807},{"strike":36850.0,"call_gex_1pct":1922380.0264137608,"put_gex_1pct":-1638181.8260160158,"net_gex_1pct":284198.200397745,"gross_gex_1pct":3560561.8524297765,"call_oi":39,"put_oi":97},{"strike":36900.0,"call_gex_1pct":8440612.932368036,"put_gex_1pct":-3727378.7177078906,"net_gex_1pct":4713234.214660145,"gross_gex_1pct":12167991.650075927,"call_oi":169,"put_oi":200},{"strike":36950.0,"call_gex_1pct":1164065.5060257162,"put_gex_1pct":-1079162.7844178646,"net_gex_1pct":84902.72160785156,"gross_gex_1pct":2243228.2904435806,"call_oi":23,"put_oi":55},{"strike":37000.0,"call_gex_1pct":33494678.79379971,"put_gex_1pct":-41573330.46668137,"net_gex_1pct":-8078651.672881659,"gross_gex_1pct":75068009.26048107,"call_oi":653,"put_oi":2003},{"strike":37050.0,"call_gex_1pct":1871673.360260166,"put_gex_1pct":-2607172.994928526,"net_gex_1pct":-735499.6346683602,"gross_gex_1pct":4478846.355188692,"call_oi":36,"put_oi":121},{"strike":37100.0,"call_gex_1pct":11120593.51929663,"put_gex_1pct":-5435545.817112455,"net_gex_1pct":5685047.702184174,"gross_gex_1pct":16556139.336409084,"call_oi":211,"put_oi":243},{"strike":37150.0,"call_gex_1pct":2618266.059736425,"put_gex_1pct":-1984826.711347144,"net_gex_1pct":633439.348389281,"gross_gex_1pct":4603092.771083569,"call_oi":49,"put_oi":82},{"strike":37200.0,"call_gex_1pct":26711130.797842212,"put_gex_1pct":-7552096.851801578,"net_gex_1pct":19159033.946040634,"gross_gex_1pct":34263227.64964379,"call_oi":493,"put_oi":290},{"strike":37250.0,"call_gex_1pct":2079428.3717270228,"put_gex_1pct":-7618864.459460534,"net_gex_1pct":-5539436.087733511,"gross_gex_1pct":9698292.831187557,"call_oi":38,"put_oi":268},{"strike":37300.0,"call_gex_1pct":13541313.772143973,"put_gex_1pct":-4328825.442425226,"net_gex_1pct":9212488.329718746,"gross_gex_1pct":17870139.2145692,"call_oi":244,"put_oi":143},{"strike":37350.0,"call_gex_1pct":2927141.9583552917,"put_gex_1pct":-5417047.557809624,"net_gex_1pct":-2489905.599454332,"gross_gex_1pct":8344189.516164916,"call_oi":52,"put_oi":166},{"strike":37400.0,"call_gex_1pct":7080955.475958798,"put_gex_1pct":-7697637.638662249,"net_gex_1pct":-616682.1627034508,"gross_gex_1pct":14778593.114621047,"call_oi":124,"put_oi":223},{"strike":37450.0,"call_gex_1pct":4577082.504121053,"put_gex_1pct":-2086618.3812638507,"net_gex_1pct":2490464.1228572023,"gross_gex_1pct":6663700.885384904,"call_oi":79,"put_oi":58},{"strike":37500.0,"call_gex_1pct":23281532.220019884,"put_gex_1pct":-20306214.802610867,"net_gex_1pct":2975317.4174090177,"gross_gex_1pct":43587747.02263075,"call_oi":396,"put_oi":535},{"strike":37550.0,"call_gex_1pct":2386689.466723658,"put_gex_1pct":-3391575.857275514,"net_gex_1pct":-1004886.3905518558,"gross_gex_1pct":5778265.323999172,"call_oi":40,"put_oi":83},{"strike":37600.0,"call_gex_1pct":10972089.68679778,"put_gex_1pct":-19298210.157228243,"net_gex_1pct":-8326120.470430462,"gross_gex_1pct":30270299.84402602,"call_oi":182,"put_oi":413},{"strike":37650.0,"call_gex_1pct":3488276.105929777,"put_gex_1pct":-2422999.604161644,"net_gex_1pct":1065276.5017681331,"gross_gex_1pct":5911275.710091421,"call_oi":57,"put_oi":49},{"strike":37700.0,"call_gex_1pct":17376256.189793624,"put_gex_1pct":-7160798.106700254,"net_gex_1pct":10215458.083093371,"gross_gex_1pct":24537054.296493877,"call_oi":281,"put_oi":132},{"strike":37750.0,"call_gex_1pct":4206740.362713101,"put_gex_1pct":-3385222.6639677524,"net_gex_1pct":821517.698745349,"gross_gex_1pct":7591963.026680853,"call_oi":67,"put_oi":57},{"strike":37800.0,"call_gex_1pct":10278637.95559705,"put_gex_1pct":-56994038.0056087,"net_gex_1pct":-46715400.05001165,"gross_gex_1pct":67272675.96120575,"call_oi":162,"put_oi":887},{"strike":37850.0,"call_gex_1pct":4897370.270631895,"put_gex_1pct":-2926981.553001054,"net_gex_1pct":1970388.7176308413,"gross_gex_1pct":7824351.82363295,"call_oi":76,"put_oi":44},{"strike":37900.0,"call_gex_1pct":16953253.41664886,"put_gex_1pct":-21202996.37069268,"net_gex_1pct":-4249742.9540438205,"gross_gex_1pct":38156249.78734154,"call_oi":259,"put_oi":307},{"strike":37950.0,"call_gex_1pct":5453160.714477529,"put_gex_1pct":-3147119.2855473137,"net_gex_1pct":2306041.428930215,"gross_gex_1pct":8600280.000024842,"call_oi":82,"put_oi":44},{"strike":38000.0,"call_gex_1pct":96259525.00102799,"put_gex_1pct":-183454474.33759618,"net_gex_1pct":-87194949.33656819,"gross_gex_1pct":279713999.3386242,"call_oi":1432,"put_oi":2476},{"strike":38050.0,"call_gex_1pct":7924274.799648277,"put_gex_1pct":-4569504.1500331145,"net_gex_1pct":3354770.649615163,"gross_gex_1pct":12493778.949681392,"call_oi":116,"put_oi":59},{"strike":38100.0,"call_gex_1pct":9304438.275655812,"put_gex_1pct":-10513544.103354735,"net_gex_1pct":-1209105.8276989236,"gross_gex_1pct":19817982.379010547,"call_oi":134,"put_oi":130},{"strike":38150.0,"call_gex_1pct":3650448.571636206,"put_gex_1pct":-7885088.159176953,"net_gex_1pct":-4234639.587540748,"gross_gex_1pct":11535536.730813159,"call_oi":52,"put_oi":92},{"strike":38200.0,"call_gex_1pct":17558661.466456782,"put_gex_1pct":-22625917.53286466,"net_gex_1pct":-5067256.066407878,"gross_gex_1pct":40184578.999321446,"call_oi":246,"put_oi":253},{"strike":38250.0,"call_gex_1pct":6458531.205501129,"put_gex_1pct":-4449143.283730204,"net_gex_1pct":2009387.9217709247,"gross_gex_1pct":10907674.489231333,"call_oi":90,"put_oi":47},{"strike":38300.0,"call_gex_1pct":14003677.660285559,"put_gex_1pct":-20593936.94167627,"net_gex_1pct":-6590259.281390712,"gross_gex_1pct":34597614.60196183,"call_oi":193,"put_oi":207},{"strike":38350.0,"call_gex_1pct":5460963.595917144,"put_gex_1pct":-12385282.440888666,"net_gex_1pct":-6924318.844971522,"gross_gex_1pct":17846246.03680581,"call_oi":74,"put_oi":120},{"strike":38400.0,"call_gex_1pct":15671621.058743136,"put_gex_1pct":-32326927.10001421,"net_gex_1pct":-16655306.041271074,"gross_gex_1pct":47998548.158757344,"call_oi":210,"put_oi":303},{"strike":38450.0,"call_gex_1pct":5922253.478675356,"put_gex_1pct":-12169558.55722901,"net_gex_1pct":-6247305.078553654,"gross_gex_1pct":18091812.035904367,"call_oi":78,"put_oi":110},{"strike":38500.0,"call_gex_1pct":48136823.778878175,"put_gex_1pct":-81873068.5558788,"net_gex_1pct":-33736244.77700063,"gross_gex_1pct":130009892.33475697,"call_oi":623,"put_oi":712},{"strike":38550.0,"call_gex_1pct":5592388.673304004,"put_gex_1pct":-8328366.649285435,"net_gex_1pct":-2735977.975981431,"gross_gex_1pct":13920755.322589438,"call_oi":72,"put_oi":70},{"strike":38600.0,"call_gex_1pct":18934312.618521784,"put_gex_1pct":-36032259.923725866,"net_gex_1pct":-17097947.305204082,"gross_gex_1pct":54966572.54224765,"call_oi":241,"put_oi":293},{"strike":38650.0,"call_gex_1pct":7118445.508753758,"put_gex_1pct":-11569902.500276992,"net_gex_1pct":-4451456.991523234,"gross_gex_1pct":18688348.009030752,"call_oi":89,"put_oi":91},{"strike":38700.0,"call_gex_1pct":99609752.26887612,"put_gex_1pct":-24458531.948025826,"net_gex_1pct":75151220.3208503,"gross_gex_1pct":124068284.21690194,"call_oi":1231,"put_oi":186},{"strike":38750.0,"call_gex_1pct":6345506.638382405,"put_gex_1pct":-7344152.411599797,"net_gex_1pct":-998645.7732173922,"gross_gex_1pct":13689659.049982201,"call_oi":77,"put_oi":54},{"strike":38800.0,"call_gex_1pct":31565304.839339692,"put_gex_1pct":-45469594.25697297,"net_gex_1pct":-13904289.417633276,"gross_gex_1pct":77034899.09631266,"call_oi":376,"put_oi":323},{"strike":38850.0,"call_gex_1pct":20645689.75349615,"put_gex_1pct":-7576175.2726973295,"net_gex_1pct":13069514.480798822,"gross_gex_1pct":28221865.02619348,"call_oi":243,"put_oi":52},{"strike":38900.0,"call_gex_1pct":64421159.67470005,"put_gex_1pct":-32130147.565622564,"net_gex_1pct":32291012.109077487,"gross_gex_1pct":96551307.24032262,"call_oi":744,"put_oi":213},{"strike":38950.0,"call_gex_1pct":31729620.919264156,"put_gex_1pct":-24373844.495962854,"net_gex_1pct":7355776.423301302,"gross_gex_1pct":56103465.41522701,"call_oi":362,"put_oi":156},{"strike":39000.0,"call_gex_1pct":94373565.8676264,"put_gex_1pct":-395923727.2447769,"net_gex_1pct":-301550161.37715054,"gross_gex_1pct":490297293.1124033,"call_oi":1056,"put_oi":2439},{"strike":39050.0,"call_gex_1pct":11401602.807189884,"put_gex_1pct":-32534514.3773066,"net_gex_1pct":-21132911.570116714,"gross_gex_1pct":43936117.184496485,"call_oi":126,"put_oi":194},{"strike":39100.0,"call_gex_1pct":88615006.17156796,"put_gex_1pct":-31665859.87257567,"net_gex_1pct":56949146.29899229,"gross_gex_1pct":120280866.04414363,"call_oi":960,"put_oi":183},{"strike":39150.0,"call_gex_1pct":8974983.13808491,"put_gex_1pct":-12315934.780346753,"net_gex_1pct":-3340951.6422618423,"gross_gex_1pct":21290917.918431662,"call_oi":96,"put_oi":69},{"strike":39200.0,"call_gex_1pct":16666477.697748192,"put_gex_1pct":-43065076.244524784,"net_gex_1pct":-26398598.546776593,"gross_gex_1pct":59731553.942272976,"call_oi":176,"put_oi":236},{"strike":39250.0,"call_gex_1pct":4220820.94048454,"put_gex_1pct":-8508938.70083986,"net_gex_1pct":-4288117.760355321,"gross_gex_1pct":12729759.6413244,"call_oi":44,"put_oi":45},{"strike":39300.0,"call_gex_1pct":14006146.587401886,"put_gex_1pct":-20140281.003475484,"net_gex_1pct":-6134134.416073598,"gross_gex_1pct":34146427.59087737,"call_oi":143,"put_oi":102},{"strike":39350.0,"call_gex_1pct":10241059.772468193,"put_gex_1pct":-8696261.67926312,"net_gex_1pct":1544798.093205072,"gross_gex_1pct":18937321.451731313,"call_oi":104,"put_oi":43},{"strike":39400.0,"call_gex_1pct":27640742.913680207,"put_gex_1pct":-46374616.194651954,"net_gex_1pct":-18733873.280971747,"gross_gex_1pct":74015359.10833216,"call_oi":277,"put_oi":224},{"strike":39450.0,"call_gex_1pct":19607217.258190658,"put_gex_1pct":-7813329.759367786,"net_gex_1pct":11793887.498822872,"gross_gex_1pct":27420547.017558444,"call_oi":197,"put_oi":37},{"strike":39500.0,"call_gex_1pct":116623915.4325071,"put_gex_1pct":-248214745.75701094,"net_gex_1pct":-131590830.32450384,"gross_gex_1pct":364838661.18951803,"call_oi":1147,"put_oi":1151},{"strike":39550.0,"call_gex_1pct":10100180.38119232,"put_gex_1pct":-10339576.213475063,"net_gex_1pct":-239395.83228274435,"gross_gex_1pct":20439756.594667383,"call_oi":98,"put_oi":46},{"strike":39600.0,"call_gex_1pct":49621931.62655068,"put_gex_1pct":-54528184.64747399,"net_gex_1pct":-4906253.020923309,"gross_gex_1pct":104150116.27402467,"call_oi":471,"put_oi":232},{"strike":39650.0,"call_gex_1pct":9216334.811801992,"put_gex_1pct":-5863388.405053739,"net_gex_1pct":3352946.406748253,"gross_gex_1pct":15079723.21685573,"call_oi":87,"put_oi":24},{"strike":39700.0,"call_gex_1pct":37920713.8957138,"put_gex_1pct":-32208267.13649531,"net_gex_1pct":5712446.759218488,"gross_gex_1pct":70128981.03220911,"call_oi":356,"put_oi":134},{"strike":39750.0,"call_gex_1pct":11018106.101158496,"put_gex_1pct":-10907771.933334766,"net_gex_1pct":110334.16782373004,"gross_gex_1pct":21925878.03449326,"call_oi":102,"put_oi":44},{"strike":39800.0,"call_gex_1pct":58573380.099549666,"put_gex_1pct":-86479380.54739664,"net_gex_1pct":-27906000.44784698,"gross_gex_1pct":145052760.6469463,"call_oi":530,"put_oi":338},{"strike":39850.0,"call_gex_1pct":10704262.562535752,"put_gex_1pct":-12358994.250662042,"net_gex_1pct":-1654731.6881262902,"gross_gex_1pct":23063256.81319779,"call_oi":98,"put_oi":49},{"strike":39900.0,"call_gex_1pct":67141896.25397626,"put_gex_1pct":-50555071.7499507,"net_gex_1pct":16586824.504025556,"gross_gex_1pct":117696968.00392696,"call_oi":606,"put_oi":193},{"strike":39950.0,"call_gex_1pct":21694062.774013754,"put_gex_1pct":-15559388.486614134,"net_gex_1pct":6134674.28739962,"gross_gex_1pct":37253451.26062789,"call_oi":193,"put_oi":57},{"strike":40000.0,"call_gex_1pct":327882971.0719508,"put_gex_1pct":-393450238.26853997,"net_gex_1pct":-65567267.19658917,"gross_gex_1pct":721333209.3404908,"call_oi":2849,"put_oi":1384},{"strike":40050.0,"call_gex_1pct":44272431.88795526,"put_gex_1pct":-18174188.177904394,"net_gex_1pct":26098243.71005087,"gross_gex_1pct":62446620.06585966,"call_oi":379,"put_oi":62},{"strike":40100.0,"call_gex_1pct":55419129.85505231,"put_gex_1pct":-75444917.01581757,"net_gex_1pct":-20025787.16076526,"gross_gex_1pct":130864046.87086987,"call_oi":476,"put_oi":260},{"strike":40150.0,"call_gex_1pct":16246042.167362215,"put_gex_1pct":-27291391.61862445,"net_gex_1pct":-11045349.451262234,"gross_gex_1pct":43537433.78598666,"call_oi":140,"put_oi":95},{"strike":40200.0,"call_gex_1pct":45889388.485702366,"put_gex_1pct":-75617038.6326915,"net_gex_1pct":-29727650.146989137,"gross_gex_1pct":121506427.11839387,"call_oi":386,"put_oi":257},{"strike":40250.0,"call_gex_1pct":13388505.400583854,"put_gex_1pct":-18090046.265910838,"net_gex_1pct":-4701540.865326984,"gross_gex_1pct":31478551.66649469,"call_oi":113,"put_oi":60},{"strike":40300.0,"call_gex_1pct":57772549.58348765,"put_gex_1pct":-63822178.18887465,"net_gex_1pct":-6049628.605386995,"gross_gex_1pct":121594727.77236229,"call_oi":478,"put_oi":204},{"strike":40350.0,"call_gex_1pct":22493221.525571357,"put_gex_1pct":-29798521.710805647,"net_gex_1pct":-7305300.18523429,"gross_gex_1pct":52291743.236377,"call_oi":185,"put_oi":94},{"strike":40400.0,"call_gex_1pct":48530198.365111984,"put_gex_1pct":-15543904.352877846,"net_gex_1pct":32986294.012234136,"gross_gex_1pct":64074102.71798983,"call_oi":393,"put_oi":46},{"strike":40450.0,"call_gex_1pct":19877321.146026704,"put_gex_1pct":-23274475.868907895,"net_gex_1pct":-3397154.7228811905,"gross_gex_1pct":43151797.0149346,"call_oi":160,"put_oi":68},{"strike":40500.0,"call_gex_1pct":146233199.84615558,"put_gex_1pct":-38277746.42175437,"net_gex_1pct":107955453.42440122,"gross_gex_1pct":184510946.26790994,"call_oi":1170,"put_oi":112},{"strike":40550.0,"call_gex_1pct":33055973.956787806,"put_gex_1pct":-8637206.816319274,"net_gex_1pct":24418767.14046853,"gross_gex_1pct":41693180.77310708,"call_oi":268,"put_oi":26},{"strike":40600.0,"call_gex_1pct":40256967.93506561,"put_gex_1pct":-14989405.817002201,"net_gex_1pct":25267562.118063413,"gross_gex_1pct":55246373.75206781,"call_oi":326,"put_oi":47},{"strike":40650.0,"call_gex_1pct":15700854.383368472,"put_gex_1pct":-8832882.878412347,"net_gex_1pct":6867971.504956124,"gross_gex_1pct":24533737.26178082,"call_oi":127,"put_oi":27},{"strike":40700.0,"call_gex_1pct":49232925.83965639,"put_gex_1pct":-12108304.768991837,"net_gex_1pct":37124621.070664555,"gross_gex_1pct":61341230.608648226,"call_oi":394,"put_oi":37},{"strike":40750.0,"call_gex_1pct":22557738.816056944,"put_gex_1pct":-8824264.299054807,"net_gex_1pct":13733474.517002137,"gross_gex_1pct":31382003.115111753,"call_oi":176,"put_oi":28},{"strike":40800.0,"call_gex_1pct":48784938.13954092,"put_gex_1pct":-26737707.156791583,"net_gex_1pct":22047230.982749335,"gross_gex_1pct":75522645.29633251,"call_oi":384,"put_oi":97},{"strike":40850.0,"call_gex_1pct":17592082.30426825,"put_gex_1pct":0.0,"net_gex_1pct":17592082.30426825,"gross_gex_1pct":17592082.30426825,"call_oi":137,"put_oi":0},{"strike":40900.0,"call_gex_1pct":32998975.396581102,"put_gex_1pct":0.0,"net_gex_1pct":32998975.396581102,"gross_gex_1pct":32998975.396581102,"call_oi":253,"put_oi":0},{"strike":40950.0,"call_gex_1pct":15324998.152011316,"put_gex_1pct":0.0,"net_gex_1pct":15324998.152011316,"gross_gex_1pct":15324998.152011316,"call_oi":118,"put_oi":0},{"strike":41000.0,"call_gex_1pct":1480664222.8845716,"put_gex_1pct":0.0,"net_gex_1pct":1480664222.8845716,"gross_gex_1pct":1480664222.8845716,"call_oi":11563,"put_oi":0},{"strike":41050.0,"call_gex_1pct":62304868.59080886,"put_gex_1pct":0.0,"net_gex_1pct":62304868.59080886,"gross_gex_1pct":62304868.59080886,"call_oi":484,"put_oi":0},{"strike":41100.0,"call_gex_1pct":58889634.11561118,"put_gex_1pct":0.0,"net_gex_1pct":58889634.11561118,"gross_gex_1pct":58889634.11561118,"call_oi":464,"put_oi":0},{"strike":41150.0,"call_gex_1pct":23638283.483729277,"put_gex_1pct":0.0,"net_gex_1pct":23638283.483729277,"gross_gex_1pct":23638283.483729277,"call_oi":188,"put_oi":0},{"strike":41200.0,"call_gex_1pct":54441019.44106848,"put_gex_1pct":0.0,"net_gex_1pct":54441019.44106848,"gross_gex_1pct":54441019.44106848,"call_oi":431,"put_oi":0},{"strike":41250.0,"call_gex_1pct":25488864.422485355,"put_gex_1pct":0.0,"net_gex_1pct":25488864.422485355,"gross_gex_1pct":25488864.422485355,"call_oi":200,"put_oi":0},{"strike":41300.0,"call_gex_1pct":31048777.127651982,"put_gex_1pct":0.0,"net_gex_1pct":31048777.127651982,"gross_gex_1pct":31048777.127651982,"call_oi":247,"put_oi":0},{"strike":41350.0,"call_gex_1pct":24922158.790319096,"put_gex_1pct":0.0,"net_gex_1pct":24922158.790319096,"gross_gex_1pct":24922158.790319096,"call_oi":201,"put_oi":0},{"strike":41400.0,"call_gex_1pct":29840226.100391965,"put_gex_1pct":0.0,"net_gex_1pct":29840226.100391965,"gross_gex_1pct":29840226.100391965,"call_oi":241,"put_oi":0},{"strike":41450.0,"call_gex_1pct":19261856.80939635,"put_gex_1pct":0.0,"net_gex_1pct":19261856.80939635,"gross_gex_1pct":19261856.80939635,"call_oi":156,"put_oi":0},{"strike":41500.0,"call_gex_1pct":199246965.29713956,"put_gex_1pct":0.0,"net_gex_1pct":199246965.29713956,"gross_gex_1pct":199246965.29713956,"call_oi":1648,"put_oi":0},{"strike":41550.0,"call_gex_1pct":9110945.851617968,"put_gex_1pct":0.0,"net_gex_1pct":9110945.851617968,"gross_gex_1pct":9110945.851617968,"call_oi":76,"put_oi":0},{"strike":41600.0,"call_gex_1pct":49546659.86593821,"put_gex_1pct":0.0,"net_gex_1pct":49546659.86593821,"gross_gex_1pct":49546659.86593821,"call_oi":417,"put_oi":0},{"strike":41650.0,"call_gex_1pct":9512324.044591092,"put_gex_1pct":0.0,"net_gex_1pct":9512324.044591092,"gross_gex_1pct":9512324.044591092,"call_oi":81,"put_oi":0},{"strike":41700.0,"call_gex_1pct":32603529.31685972,"put_gex_1pct":0.0,"net_gex_1pct":32603529.31685972,"gross_gex_1pct":32603529.31685972,"call_oi":281,"put_oi":0},{"strike":41750.0,"call_gex_1pct":9281259.414493324,"put_gex_1pct":0.0,"net_gex_1pct":9281259.414493324,"gross_gex_1pct":9281259.414493324,"call_oi":81,"put_oi":0},{"strike":41800.0,"call_gex_1pct":24090242.503365465,"put_gex_1pct":0.0,"net_gex_1pct":24090242.503365465,"gross_gex_1pct":24090242.503365465,"call_oi":213,"put_oi":0},{"strike":41850.0,"call_gex_1pct":10449411.545875268,"put_gex_1pct":0.0,"net_gex_1pct":10449411.545875268,"gross_gex_1pct":10449411.545875268,"call_oi":94,"put_oi":0},{"strike":41900.0,"call_gex_1pct":27165293.46976416,"put_gex_1pct":0.0,"net_gex_1pct":27165293.46976416,"gross_gex_1pct":27165293.46976416,"call_oi":247,"put_oi":0},{"strike":41950.0,"call_gex_1pct":14040865.586499639,"put_gex_1pct":0.0,"net_gex_1pct":14040865.586499639,"gross_gex_1pct":14040865.586499639,"call_oi":130,"put_oi":0},{"strike":42000.0,"call_gex_1pct":458637672.8134506,"put_gex_1pct":0.0,"net_gex_1pct":458637672.8134506,"gross_gex_1pct":458637672.8134506,"call_oi":4327,"put_oi":0},{"strike":42050.0,"call_gex_1pct":12921674.120791169,"put_gex_1pct":0.0,"net_gex_1pct":12921674.120791169,"gross_gex_1pct":12921674.120791169,"call_oi":124,"put_oi":0},{"strike":42100.0,"call_gex_1pct":30934642.467143346,"put_gex_1pct":0.0,"net_gex_1pct":30934642.467143346,"gross_gex_1pct":30934642.467143346,"call_oi":303,"put_oi":0},{"strike":42150.0,"call_gex_1pct":13356829.857396193,"put_gex_1pct":0.0,"net_gex_1pct":13356829.857396193,"gross_gex_1pct":13356829.857396193,"call_oi":133,"put_oi":0},{"strike":42200.0,"call_gex_1pct":55850966.620059624,"put_gex_1pct":0.0,"net_gex_1pct":55850966.620059624,"gross_gex_1pct":55850966.620059624,"call_oi":567,"put_oi":0},{"strike":42250.0,"call_gex_1pct":7324126.5146282,"put_gex_1pct":0.0,"net_gex_1pct":7324126.5146282,"gross_gex_1pct":7324126.5146282,"call_oi":76,"put_oi":0},{"strike":42300.0,"call_gex_1pct":22395388.45376217,"put_gex_1pct":0.0,"net_gex_1pct":22395388.45376217,"gross_gex_1pct":22395388.45376217,"call_oi":238,"put_oi":0},{"strike":42350.0,"call_gex_1pct":8333891.588445549,"put_gex_1pct":0.0,"net_gex_1pct":8333891.588445549,"gross_gex_1pct":8333891.588445549,"call_oi":91,"put_oi":0},{"strike":42400.0,"call_gex_1pct":18627565.0536952,"put_gex_1pct":0.0,"net_gex_1pct":18627565.0536952,"gross_gex_1pct":18627565.0536952,"call_oi":208,"put_oi":0},{"strike":42450.0,"call_gex_1pct":5237487.519342945,"put_gex_1pct":0.0,"net_gex_1pct":5237487.519342945,"gross_gex_1pct":5237487.519342945,"call_oi":60,"put_oi":0},{"strike":42500.0,"call_gex_1pct":280965332.46813476,"put_gex_1pct":0.0,"net_gex_1pct":280965332.46813476,"gross_gex_1pct":280965332.46813476,"call_oi":3305,"put_oi":0},{"strike":42550.0,"call_gex_1pct":7588239.014843144,"put_gex_1pct":0.0,"net_gex_1pct":7588239.014843144,"gross_gex_1pct":7588239.014843144,"call_oi":92,"put_oi":0},{"strike":42600.0,"call_gex_1pct":19291413.221309118,"put_gex_1pct":0.0,"net_gex_1pct":19291413.221309118,"gross_gex_1pct":19291413.221309118,"call_oi":239,"put_oi":0},{"strike":42650.0,"call_gex_1pct":5043100.340775905,"put_gex_1pct":0.0,"net_gex_1pct":5043100.340775905,"gross_gex_1pct":5043100.340775905,"call_oi":65,"put_oi":0},{"strike":42700.0,"call_gex_1pct":11391463.30364079,"put_gex_1pct":0.0,"net_gex_1pct":11391463.30364079,"gross_gex_1pct":11391463.30364079,"call_oi":150,"put_oi":0},{"strike":42750.0,"call_gex_1pct":3478738.7170694787,"put_gex_1pct":0.0,"net_gex_1pct":3478738.7170694787,"gross_gex_1pct":3478738.7170694787,"call_oi":47,"put_oi":0},{"strike":42800.0,"call_gex_1pct":17999410.237093832,"put_gex_1pct":0.0,"net_gex_1pct":17999410.237093832,"gross_gex_1pct":17999410.237093832,"call_oi":250,"put_oi":0},{"strike":42850.0,"call_gex_1pct":4667071.33289305,"put_gex_1pct":0.0,"net_gex_1pct":4667071.33289305,"gross_gex_1pct":4667071.33289305,"call_oi":68,"put_oi":0},{"strike":42900.0,"call_gex_1pct":16369041.377642382,"put_gex_1pct":0.0,"net_gex_1pct":16369041.377642382,"gross_gex_1pct":16369041.377642382,"call_oi":246,"put_oi":0},{"strike":42950.0,"call_gex_1pct":8184671.404491153,"put_gex_1pct":0.0,"net_gex_1pct":8184671.404491153,"gross_gex_1pct":8184671.404491153,"call_oi":129,"put_oi":0},{"strike":43000.0,"call_gex_1pct":553739688.8946396,"put_gex_1pct":0.0,"net_gex_1pct":553739688.8946396,"gross_gex_1pct":553739688.8946396,"call_oi":9141,"put_oi":0},{"strike":43050.0,"call_gex_1pct":4669122.21489417,"put_gex_1pct":0.0,"net_gex_1pct":4669122.21489417,"gross_gex_1pct":4669122.21489417,"call_oi":79,"put_oi":0},{"strike":43100.0,"call_gex_1pct":7986136.71203548,"put_gex_1pct":0.0,"net_gex_1pct":7986136.71203548,"gross_gex_1pct":7986136.71203548,"call_oi":141,"put_oi":0},{"strike":43150.0,"call_gex_1pct":2596832.5674739517,"put_gex_1pct":0.0,"net_gex_1pct":2596832.5674739517,"gross_gex_1pct":2596832.5674739517,"call_oi":48,"put_oi":0},{"strike":43200.0,"call_gex_1pct":19816018.57390112,"put_gex_1pct":0.0,"net_gex_1pct":19816018.57390112,"gross_gex_1pct":19816018.57390112,"call_oi":378,"put_oi":0},{"strike":43250.0,"call_gex_1pct":6866354.717500396,"put_gex_1pct":0.0,"net_gex_1pct":6866354.717500396,"gross_gex_1pct":6866354.717500396,"call_oi":137,"put_oi":0},{"strike":43300.0,"call_gex_1pct":10172476.9825178,"put_gex_1pct":0.0,"net_gex_1pct":10172476.9825178,"gross_gex_1pct":10172476.9825178,"call_oi":213,"put_oi":0},{"strike":43350.0,"call_gex_1pct":5396736.8333690455,"put_gex_1pct":0.0,"net_gex_1pct":5396736.8333690455,"gross_gex_1pct":5396736.8333690455,"call_oi":123,"put_oi":0},{"strike":43400.0,"call_gex_1pct":8472337.81257329,"put_gex_1pct":0.0,"net_gex_1pct":8472337.81257329,"gross_gex_1pct":8472337.81257329,"call_oi":200,"put_oi":0},{"strike":43450.0,"call_gex_1pct":4486378.239138467,"put_gex_1pct":0.0,"net_gex_1pct":4486378.239138467,"gross_gex_1pct":4486378.239138467,"call_oi":108,"put_oi":0},{"strike":43500.0,"call_gex_1pct":79465752.95227098,"put_gex_1pct":0.0,"net_gex_1pct":79465752.95227098,"gross_gex_1pct":79465752.95227098,"call_oi":2157,"put_oi":0},{"strike":43550.0,"call_gex_1pct":4766390.7943684785,"put_gex_1pct":0.0,"net_gex_1pct":4766390.7943684785,"gross_gex_1pct":4766390.7943684785,"call_oi":141,"put_oi":0},{"strike":43600.0,"call_gex_1pct":9977971.716334758,"put_gex_1pct":0.0,"net_gex_1pct":9977971.716334758,"gross_gex_1pct":9977971.716334758,"call_oi":359,"put_oi":0},{"strike":43650.0,"call_gex_1pct":1717268.6305674652,"put_gex_1pct":0.0,"net_gex_1pct":1717268.6305674652,"gross_gex_1pct":1717268.6305674652,"call_oi":64,"put_oi":0},{"strike":43700.0,"call_gex_1pct":5929379.957341318,"put_gex_1pct":0.0,"net_gex_1pct":5929379.957341318,"gross_gex_1pct":5929379.957341318,"call_oi":229,"put_oi":0},{"strike":43750.0,"call_gex_1pct":2683710.031094034,"put_gex_1pct":0.0,"net_gex_1pct":2683710.031094034,"gross_gex_1pct":2683710.031094034,"call_oi":121,"put_oi":0},{"strike":43800.0,"call_gex_1pct":8840230.362923155,"put_gex_1pct":0.0,"net_gex_1pct":8840230.362923155,"gross_gex_1pct":8840230.362923155,"call_oi":467,"put_oi":0},{"strike":43850.0,"call_gex_1pct":1725058.1438472036,"put_gex_1pct":0.0,"net_gex_1pct":1725058.1438472036,"gross_gex_1pct":1725058.1438472036,"call_oi":98,"put_oi":0},{"strike":43900.0,"call_gex_1pct":2857262.990283861,"put_gex_1pct":0.0,"net_gex_1pct":2857262.990283861,"gross_gex_1pct":2857262.990283861,"call_oi":173,"put_oi":0},{"strike":43950.0,"call_gex_1pct":2637674.0193473133,"put_gex_1pct":0.0,"net_gex_1pct":2637674.0193473133,"gross_gex_1pct":2637674.0193473133,"call_oi":174,"put_oi":0},{"strike":44000.0,"call_gex_1pct":72808116.39842027,"put_gex_1pct":0.0,"net_gex_1pct":72808116.39842027,"gross_gex_1pct":72808116.39842027,"call_oi":6577,"put_oi":0},{"strike":44050.0,"call_gex_1pct":1454332.3718718193,"put_gex_1pct":0.0,"net_gex_1pct":1454332.3718718193,"gross_gex_1pct":1454332.3718718193,"call_oi":146,"put_oi":0},{"strike":44100.0,"call_gex_1pct":2770269.6632472347,"put_gex_1pct":0.0,"net_gex_1pct":2770269.6632472347,"gross_gex_1pct":2770269.6632472347,"call_oi":634,"put_oi":0},{"strike":44150.0,"call_gex_1pct":687588.0443486427,"put_gex_1pct":0.0,"net_gex_1pct":687588.0443486427,"gross_gex_1pct":687588.0443486427,"call_oi":190,"put_oi":0},{"strike":44200.0,"call_gex_1pct":855267.1949158432,"put_gex_1pct":0.0,"net_gex_1pct":855267.1949158432,"gross_gex_1pct":855267.1949158432,"call_oi":241,"put_oi":0},{"strike":44250.0,"call_gex_1pct":238181.17983892772,"put_gex_1pct":0.0,"net_gex_1pct":238181.17983892772,"gross_gex_1pct":238181.17983892772,"call_oi":76,"put_oi":0},{"strike":44300.0,"call_gex_1pct":451958.7029509248,"put_gex_1pct":0.0,"net_gex_1pct":451958.7029509248,"gross_gex_1pct":451958.7029509248,"call_oi":147,"put_oi":0},{"strike":44350.0,"call_gex_1pct":401256.87878517585,"put_gex_1pct":0.0,"net_gex_1pct":401256.87878517585,"gross_gex_1pct":401256.87878517585,"call_oi":133,"put_oi":0},{"strike":44400.0,"call_gex_1pct":598151.4245099233,"put_gex_1pct":0.0,"net_gex_1pct":598151.4245099233,"gross_gex_1pct":598151.4245099233,"call_oi":202,"put_oi":0},{"strike":44450.0,"call_gex_1pct":427329.8513035558,"put_gex_1pct":0.0,"net_gex_1pct":427329.8513035558,"gross_gex_1pct":427329.8513035558,"call_oi":147,"put_oi":0},{"strike":44500.0,"call_gex_1pct":1754308.8694048675,"put_gex_1pct":0.0,"net_gex_1pct":1754308.8694048675,"gross_gex_1pct":1754308.8694048675,"call_oi":697,"put_oi":0},{"strike":44550.0,"call_gex_1pct":3465458.0596597753,"put_gex_1pct":0.0,"net_gex_1pct":3465458.0596597753,"gross_gex_1pct":3465458.0596597753,"call_oi":1402,"put_oi":0},{"strike":44600.0,"call_gex_1pct":917772.5279260883,"put_gex_1pct":0.0,"net_gex_1pct":917772.5279260883,"gross_gex_1pct":917772.5279260883,"call_oi":378,"put_oi":0},{"strike":44650.0,"call_gex_1pct":47708.210704504265,"put_gex_1pct":0.0,"net_gex_1pct":47708.210704504265,"gross_gex_1pct":47708.210704504265,"call_oi":20,"put_oi":0},{"strike":44700.0,"call_gex_1pct":91418.67766232985,"put_gex_1pct":0.0,"net_gex_1pct":91418.67766232985,"gross_gex_1pct":91418.67766232985,"call_oi":39,"put_oi":0},{"strike":44750.0,"call_gex_1pct":20735.068194517404,"put_gex_1pct":0.0,"net_gex_1pct":20735.068194517404,"gross_gex_1pct":20735.068194517404,"call_oi":9,"put_oi":0},{"strike":44800.0,"call_gex_1pct":557152.792158146,"put_gex_1pct":0.0,"net_gex_1pct":557152.792158146,"gross_gex_1pct":557152.792158146,"call_oi":246,"put_oi":0},{"strike":44850.0,"call_gex_1pct":155881.77488323543,"put_gex_1pct":0.0,"net_gex_1pct":155881.77488323543,"gross_gex_1pct":155881.77488323543,"call_oi":70,"put_oi":0},{"strike":44900.0,"call_gex_1pct":186146.3264877965,"put_gex_1pct":0.0,"net_gex_1pct":186146.3264877965,"gross_gex_1pct":186146.3264877965,"call_oi":85,"put_oi":0},{"strike":44950.0,"call_gex_1pct":53850.81553226896,"put_gex_1pct":0.0,"net_gex_1pct":53850.81553226896,"gross_gex_1pct":53850.81553226896,"call_oi":25,"put_oi":0},{"strike":45000.0,"call_gex_1pct":5003131.065910395,"put_gex_1pct":0.0,"net_gex_1pct":5003131.065910395,"gross_gex_1pct":5003131.065910395,"call_oi":2361,"put_oi":0},{"strike":45050.0,"call_gex_1pct":123017.48706007111,"put_gex_1pct":0.0,"net_gex_1pct":123017.48706007111,"gross_gex_1pct":123017.48706007111,"call_oi":59,"put_oi":0},{"strike":45100.0,"call_gex_1pct":36934.32035148965,"put_gex_1pct":0.0,"net_gex_1pct":36934.32035148965,"gross_gex_1pct":36934.32035148965,"call_oi":18,"put_oi":0},{"strike":45150.0,"call_gex_1pct":32314.14822098607,"put_gex_1pct":0.0,"net_gex_1pct":32314.14822098607,"gross_gex_1pct":32314.14822098607,"call_oi":16,"put_oi":0},{"strike":45200.0,"call_gex_1pct":43740.27100538034,"put_gex_1pct":0.0,"net_gex_1pct":43740.27100538034,"gross_gex_1pct":43740.27100538034,"call_oi":22,"put_oi":0},{"strike":45250.0,"call_gex_1pct":13702.898562744203,"put_gex_1pct":0.0,"net_gex_1pct":13702.898562744203,"gross_gex_1pct":13702.898562744203,"call_oi":7,"put_oi":0},{"strike":45300.0,"call_gex_1pct":19769.661843513906,"put_gex_1pct":0.0,"net_gex_1pct":19769.661843513906,"gross_gex_1pct":19769.661843513906,"call_oi":12,"put_oi":0},{"strike":45350.0,"call_gex_1pct":6489.865569583158,"put_gex_1pct":0.0,"net_gex_1pct":6489.865569583158,"gross_gex_1pct":6489.865569583158,"call_oi":4,"put_oi":0},{"strike":45400.0,"call_gex_1pct":9588.500766991789,"put_gex_1pct":0.0,"net_gex_1pct":9588.500766991789,"gross_gex_1pct":9588.500766991789,"call_oi":6,"put_oi":0},{"strike":45450.0,"call_gex_1pct":17317.320089304863,"put_gex_1pct":0.0,"net_gex_1pct":17317.320089304863,"gross_gex_1pct":17317.320089304863,"call_oi":11,"put_oi":0},{"strike":45500.0,"call_gex_1pct":1051646.6128238228,"put_gex_1pct":0.0,"net_gex_1pct":1051646.6128238228,"gross_gex_1pct":1051646.6128238228,"call_oi":678,"put_oi":0},{"strike":45550.0,"call_gex_1pct":65723.87262733729,"put_gex_1pct":0.0,"net_gex_1pct":65723.87262733729,"gross_gex_1pct":65723.87262733729,"call_oi":43,"put_oi":0},{"strike":45600.0,"call_gex_1pct":33140.0539200934,"put_gex_1pct":0.0,"net_gex_1pct":33140.0539200934,"gross_gex_1pct":33140.0539200934,"call_oi":22,"put_oi":0},{"strike":45700.0,"call_gex_1pct":43911.96959812875,"put_gex_1pct":0.0,"net_gex_1pct":43911.96959812875,"gross_gex_1pct":43911.96959812875,"call_oi":30,"put_oi":0},{"strike":45800.0,"call_gex_1pct":9961.461535015556,"put_gex_1pct":0.0,"net_gex_1pct":9961.461535015556,"gross_gex_1pct":9961.461535015556,"call_oi":7,"put_oi":0},{"strike":45900.0,"call_gex_1pct":15226.680256653462,"put_gex_1pct":0.0,"net_gex_1pct":15226.680256653462,"gross_gex_1pct":15226.680256653462,"call_oi":11,"put_oi":0},{"strike":46000.0,"call_gex_1pct":1192229.4358806682,"put_gex_1pct":0.0,"net_gex_1pct":1192229.4358806682,"gross_gex_1pct":1192229.4358806682,"call_oi":885,"put_oi":0},{"strike":46100.0,"call_gex_1pct":8536.33303782881,"put_gex_1pct":0.0,"net_gex_1pct":8536.33303782881,"gross_gex_1pct":8536.33303782881,"call_oi":8,"put_oi":0},{"strike":46200.0,"call_gex_1pct":23973.463907452013,"put_gex_1pct":0.0,"net_gex_1pct":23973.463907452013,"gross_gex_1pct":23973.463907452013,"call_oi":31,"put_oi":0},{"strike":46300.0,"call_gex_1pct":12807.860413322349,"put_gex_1pct":0.0,"net_gex_1pct":12807.860413322349,"gross_gex_1pct":12807.860413322349,"call_oi":17,"put_oi":0},{"strike":46400.0,"call_gex_1pct":2189.927809814901,"put_gex_1pct":0.0,"net_gex_1pct":2189.927809814901,"gross_gex_1pct":2189.927809814901,"call_oi":5,"put_oi":0},{"strike":46500.0,"call_gex_1pct":41840.36013334065,"put_gex_1pct":0.0,"net_gex_1pct":41840.36013334065,"gross_gex_1pct":41840.36013334065,"call_oi":98,"put_oi":0},{"strike":46600.0,"call_gex_1pct":8327.06304526151,"put_gex_1pct":0.0,"net_gex_1pct":8327.06304526151,"gross_gex_1pct":8327.06304526151,"call_oi":20,"put_oi":0},{"strike":46700.0,"call_gex_1pct":4468.115907656175,"put_gex_1pct":0.0,"net_gex_1pct":4468.115907656175,"gross_gex_1pct":4468.115907656175,"call_oi":11,"put_oi":0},{"strike":46800.0,"call_gex_1pct":6739.420769738564,"put_gex_1pct":0.0,"net_gex_1pct":6739.420769738564,"gross_gex_1pct":6739.420769738564,"call_oi":17,"put_oi":0},{"strike":46900.0,"call_gex_1pct":1935.3185594651363,"put_gex_1pct":0.0,"net_gex_1pct":1935.3185594651363,"gross_gex_1pct":1935.3185594651363,"call_oi":5,"put_oi":0},{"strike":47000.0,"call_gex_1pct":363687.4755241309,"put_gex_1pct":0.0,"net_gex_1pct":363687.4755241309,"gross_gex_1pct":363687.4755241309,"call_oi":962,"put_oi":0},{"strike":47100.0,"call_gex_1pct":2585.7078751956783,"put_gex_1pct":0.0,"net_gex_1pct":2585.7078751956783,"gross_gex_1pct":2585.7078751956783,"call_oi":7,"put_oi":0},{"strike":47200.0,"call_gex_1pct":2527.321253931856,"put_gex_1pct":0.0,"net_gex_1pct":2527.321253931856,"gross_gex_1pct":2527.321253931856,"call_oi":7,"put_oi":0},{"strike":47300.0,"call_gex_1pct":1765.0700986246418,"put_gex_1pct":0.0,"net_gex_1pct":1765.0700986246418,"gross_gex_1pct":1765.0700986246418,"call_oi":5,"put_oi":0},{"strike":47400.0,"call_gex_1pct":1726.3781750514431,"put_gex_1pct":0.0,"net_gex_1pct":1726.3781750514431,"gross_gex_1pct":1726.3781750514431,"call_oi":5,"put_oi":0},{"strike":47500.0,"call_gex_1pct":1351.2645689266424,"put_gex_1pct":0.0,"net_gex_1pct":1351.2645689266424,"gross_gex_1pct":1351.2645689266424,"call_oi":4,"put_oi":0},{"strike":47600.0,"call_gex_1pct":991.8655675699987,"put_gex_1pct":0.0,"net_gex_1pct":991.8655675699987,"gross_gex_1pct":991.8655675699987,"call_oi":3,"put_oi":0},{"strike":47700.0,"call_gex_1pct":3560.479270389355,"put_gex_1pct":0.0,"net_gex_1pct":3560.479270389355,"gross_gex_1pct":3560.479270389355,"call_oi":11,"put_oi":0},{"strike":47800.0,"call_gex_1pct":25675.243477105156,"put_gex_1pct":0.0,"net_gex_1pct":25675.243477105156,"gross_gex_1pct":25675.243477105156,"call_oi":81,"put_oi":0},{"strike":47900.0,"call_gex_1pct":4036.5735997251377,"put_gex_1pct":0.0,"net_gex_1pct":4036.5735997251377,"gross_gex_1pct":4036.5735997251377,"call_oi":13,"put_oi":0},{"strike":48000.0,"call_gex_1pct":19472.083825928225,"put_gex_1pct":0.0,"net_gex_1pct":19472.083825928225,"gross_gex_1pct":19472.083825928225,"call_oi":64,"put_oi":0},{"strike":48100.0,"call_gex_1pct":596.4104376422815,"put_gex_1pct":0.0,"net_gex_1pct":596.4104376422815,"gross_gex_1pct":596.4104376422815,"call_oi":2,"put_oi":0},{"strike":48200.0,"call_gex_1pct":2046.5055007581457,"put_gex_1pct":0.0,"net_gex_1pct":2046.5055007581457,"gross_gex_1pct":2046.5055007581457,"call_oi":7,"put_oi":0},{"strike":48300.0,"call_gex_1pct":2006.9036379115328,"put_gex_1pct":0.0,"net_gex_1pct":2006.9036379115328,"gross_gex_1pct":2006.9036379115328,"call_oi":7,"put_oi":0},{"strike":48400.0,"call_gex_1pct":1968.5720286890921,"put_gex_1pct":0.0,"net_gex_1pct":1968.5720286890921,"gross_gex_1pct":1968.5720286890921,"call_oi":7,"put_oi":0},{"strike":48500.0,"call_gex_1pct":3035.1436397660564,"put_gex_1pct":0.0,"net_gex_1pct":3035.1436397660564,"gross_gex_1pct":3035.1436397660564,"call_oi":11,"put_oi":0},{"strike":48600.0,"call_gex_1pct":4332.571697349553,"put_gex_1pct":0.0,"net_gex_1pct":4332.571697349553,"gross_gex_1pct":4332.571697349553,"call_oi":16,"put_oi":0},{"strike":48700.0,"call_gex_1pct":32960.219439465625,"put_gex_1pct":0.0,"net_gex_1pct":32960.219439465625,"gross_gex_1pct":32960.219439465625,"call_oi":124,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 37,100 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 前日同月份 Chain 不完整（primary_expiry_chain_empty） |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 39,412 | 41,625 | -2,213 | 92,350 | 99,178 | -6,828 | +4,615 | TAIFEX Proxy |
| 投信 | 8,814 | 120 | +8,694 | 0 | 0 | +0 | +8,694 | TAIFEX Proxy |
| 自營商 | 68,238 | 79,318 | -11,080 | 62,155 | 62,710 | -555 | -10,525 | TAIFEX Proxy |
| 三大法人合計 | 116,464 | 121,063 | -4,599 | 154,505 | 161,888 | -7,383 | +2,784 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.07 | 14.82 | -5.75 | 14.40 | 14.75 | -0.35 | -5.40 | TAIFEX Proxy |
| 投信 | 15.76 | 0.01 | +15.75 | 0.00 | 0.00 | +0 | +15.75 | TAIFEX Proxy |
| 自營商 | 19.44 | 25.85 | -6.41 | 13.90 | 13.27 | +0.63 | -7.04 | TAIFEX Proxy |
| 三大法人合計 | 44.27 | 40.67 | +3.59 | 28.31 | 28.02 | +0.28 | +3.31 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,521 | TAIFEX Proxy |
| 買權空方 OI | 18,614 | TAIFEX Proxy |
| 買權多空淨 OI | -4,093 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | unavailable |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,642 | TAIFEX Proxy |
| 賣權空方 OI | 11,745 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,103 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | unavailable |
- 資料日期：買權 2026-11-23／賣權 2026-11-23 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +5,084 | 2026-11-23→2026-11-24 | TAIFEX Proxy snapshots (2026-11-23) |
| 買權前十大 | unavailable | — | 歷史快照／比較資料不可用 |
| 賣權前十大 | unavailable | — | 歷史快照／比較資料不可用 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-24；本次報告產製時間：2026-11-25 07:48:22；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 未取得欄位 (3)：options.chain_oi_change, options.wall_change, options.top10_change

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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-24；估值 1247 檔；1 檔採最近有效收盤價（價格日期 20261123 至 20261124）；Blave 同 T0 交叉驗證 162.0710%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：亞洲主要指數資料日期落後 T0 2026-11-24，已將舊行情排除並標示 unavailable；原始資料日期：日經225 2026-11-20、韓國KOSPI 2026-11-23、香港恆生 2026-11-23、上海綜合 2026-11-23、深圳成分 2026-11-23
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；1 檔採最近有效收盤價（價格日期 20261123 至 20261124）。Blave 同 T0 交叉驗證 162.0710%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-24 非今日 2026-11-25，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：選擇權 OI 前日變化 unavailable：reason=primary_expiry_chain_empty; 主力=202611W4; 本日/前日有效合約=540/0; 本日/前日合約識別數=540/0; 僅本日/僅前日有效合約=540/0; 本日/前日 OI 缺值或無效=0/0; 無效/重複識別=0/0
- TAIFEX 註記：前日快照主力月份無法確認（快照值：缺失）；選擇權比較仍僅按當日主力月份及共同合約判定
- TAIFEX 註記：選擇權 Call Wall／Put Wall／Max Pain 前日變化 unavailable：reason=previous_chain_incomplete; detail=primary_expiry_chain_empty
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -503.9 | -103,182 | -692 | -3,892 | -2,213 | -6,828 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +97.6 | +98,014 | +4,449 | +754 | +8,694 | +0 | 趨勢偏多 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
| 自營商 | -810.3 | -233 | -1,214 | +2,026 | -11,080 | -555 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
