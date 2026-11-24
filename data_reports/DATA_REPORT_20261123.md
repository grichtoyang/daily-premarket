# DATA_REPORT_20261123

- 報告日期：`2026-11-25`
- T0 交易日期：`2026-11-23`
- 首次資料產出時間：`2026-11-25 00:14:39`
- 本次更新開始時間：`2026-11-25 00:14:39`
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
| 加權指數 | 36,811.89 | 點 | twse-proxy |
| 開盤 | 35,899.48 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 37,108.20 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 35,442.41 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 36,811.89 | 點 | twse-proxy |
| 漲跌點數 | 778.60 | 點 | twse-proxy |
| 漲跌幅 | +2.16 | % | twse-proxy |
| 成交金額 | 11,137.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 652 | twse-proxy |
| 下跌家數 | 362 | twse-proxy |
| 平盤家數 | 72 | twse-proxy |
| 漲停家數 | 43 | twse-proxy |
| 跌停家數 | 9 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 560 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 254 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 59 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 25 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 7 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -289.5 | 億元 | TWSE RWD BFI82U |
| 投信 | -41.5 | 億元 | TWSE RWD BFI82U |
| 自營商 | -190.0 | 億元 | TWSE RWD BFI82U |
| 三大法人合計 | -521.0 | 億元 | TWSE RWD BFI82U |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-23；估值 1243 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 148.4610%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 5,616.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -64.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 194,890 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -30,725 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 148.46 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-23；估值 1243 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 148.4610%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 34,590,832 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,440,868.343 | 2,142,041.563 | 20,582,909.906 | 張 |
| 借券賣出增減 | -51,166.5 | -9,003.564 | -60,170.064 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261123`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-25T00:15:17+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261123`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-25T00:15:19+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 11,137.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,621.7 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 12,759.2 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,147.84 | -89.33 | -1.23 | 2026-11-24 | 2026-11-24T16:15:19+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,478.30 | -611.26 | -2.54 | 2026-11-24 | 2026-11-24T16:15:19+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 25,956.57 | -789.53 | -2.95 | 2026-11-24 | 2026-11-24T16:15:19+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 49,593.94 | -1.37 | -0.00 | 2026-11-24 | 2026-11-24T16:15:19+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 8,666.63 | -921.42 | -9.61 | 2026-11-24 | 2026-11-24T16:15:19+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 28.63 | 2.01 | +7.55 | 2026-11-24 | 2026-11-24T16:15:19+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | unavailable | unavailable | unavailable | 2026-11-20 | 2026-11-24T16:15:19+00:00 | Asia/Tokyo | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 韓國KOSPI | ^KS11 | 4,708.54 | -161.42 | -3.31 | 2026-11-23 | 2026-11-24T16:15:19+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,383.74 | -27.06 | -0.12 | 2026-11-23 | 2026-11-24T16:15:19+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,538.95 | 5.16 | +0.15 | 2026-11-23 | 2026-11-24T16:15:19+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,454.37 | 197.98 | +1.93 | 2026-11-23 | 2026-11-24T16:15:19+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,159.75 | -94.75 | -1.31 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,027.25 | -780.75 | -2.91 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 49,594.00 | -83.00 | -0.17 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,666.70 | -7.40 | -0.28 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.63 | 0.00 | 23-NOV-26 | 2026-11-24T16:15:46+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.89 | -0.03 | 2026-11-24 | 2026-11-24T16:15:46+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.33 | -0.01 | 23-NOV-26 | 2026-11-24T16:15:46+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.27 | -0.02 | 2026-11-24 | 2026-11-24T16:15:46+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.98 | 0.02 | +0.06 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.85 | -0.47 | -0.45 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.06 | 0.12 | +0.08 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,344.54 | 0.23 | +0.02 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 341.26 | -22.35 | -6.15 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.19 | -1.20 | -8.33 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 28.80 | -3.08 | -9.66 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 80.06 | -0.11 | -0.14 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,567.60 | -83.80 | -2.30 | 2026-11-24 | 2026-11-24T16:15:26+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 59,468.08 | -1,742.91 | -2.85 | 2026-11-24 | 2026-11-24T16:15:20+00:00 | UTC | Yahoo Finance Chart API |

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
- 事件6：氣象署深夜大雨特報！基隆、新北超冷雨炸到明早
  - 來源：Yahoo 台股；發布時間：2026-11-24T14:50:04Z；台北時間：2026-11-24 22:50
  - 摘要：受到東北季風影響，中央氣象署24日發布基隆市、新北市大雨特報，24日晚間至25日清晨，基隆北海岸將有局部大雨發生，提醒民眾外出注意天氣變化。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B0%A3%E8%B1%A1%E7%BD%B2%E6%B7%B1%E5%A4%9C%E5%A4%A7%E9%9B%A8%E7%89%B9%E5%A0%B1-%E5%9F%BA%E9%9A%86-%E6%96%B0%E5%8C%97%E8%B6%85%E5%86%B7%E9%9B%A8%E7%82%B8%E5%88%B0%E6%98%8E%E6%97%A9-145004666.html
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
  - 來源：CNBC；發布時間：Tue, 24 Nov 2026 16:06:07 GMT；台北時間：2026-11-25 00:06
  - 摘要：The Conference Board survey released Tuesday showed improvement across the board, with the headline confidence index jumping to 103.3.
  - 原文連結：https://www.cnbc.com/2026/11/24/consumer-confidence-november-election-midterm.html
- 事件12：Fed's John Williams indicates higher interest rates likely 'over time' to address inflation
  - 來源：CNBC；發布時間：Tue, 24 Nov 2026 13:33:26 GMT；台北時間：2026-11-24 21:33
  - 摘要：The influential central banker expressed confidence that inflation will get closer to the Fed's 2% target in 2027.
  - 原文連結：https://www.cnbc.com/2026/11/23/john-williams-fed-inflation-rate-hikes.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-23

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
| 開盤價 | 36,671 | 點 | TAIFEX Proxy |
| 最高價 | 40,324 | 點 | TAIFEX Proxy |
| 最低價 | 36,280 | 點 | TAIFEX Proxy |
| 收盤價 | 39,829 | 點 | TAIFEX Proxy |
| 漲跌點數 | +3,170 | 點 | TAIFEX Proxy |
| 漲跌幅 | +8.65 | % | TAIFEX Proxy |
| 成交量 | 92,939 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,324 / 36,280 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 14,599 | TAIFEX Proxy |
| 外資空方 OI | 118,031 | TAIFEX Proxy |
| 外資多空淨 OI | -103,432 | TAIFEX Proxy |
| 投信多方 OI | 97,312 | TAIFEX Proxy |
| 投信空方 OI | 3,747 | TAIFEX Proxy |
| 投信多空淨 OI | +93,565 | TAIFEX Proxy |
| 自營商多方 OI | 4,472 | TAIFEX Proxy |
| 自營商空方 OI | 3,154 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,318 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,383 | TAIFEX Proxy |
| 三大法人合計空方 OI | 124,932 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -8,549 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -5,569 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +5,966 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,036 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 105,231 | TAIFEX Proxy |
| 前十大交易人空方 OI | 100,512 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,719 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-20→2026-11-23) | +374 | TAIFEX Proxy snapshots (2026-11-20) |
- 資料日期：2026-11-23 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 68,962 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 69,654 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -692 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 59,748 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 56,533 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +3,215 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,907 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +4,449 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +4,449 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,214 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -1,501 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +287 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,543 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,714 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | +201.8 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +135.0 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,324 | TAIFEX Proxy |
| 加權指數價格 | 36,811.89 | twse-proxy |
| 台指期與加權指數價差 | +3,512.11 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +9.54 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +3,512.11 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -495 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,324 | 39,829 | +495 | TAIFEX Proxy |
| 成交量 | 18,862 | 92,939 | -74,077 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,433（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 68,962 | 69,654 | -692 | 59,748 | 56,533 | +3,215 | -3,907 | 14,599 | 118,031 | -103,432 | -5,569 | TAIFEX Proxy |
| 投信 | 4,449 | 0 | +4,449 | 0 | 0 | +0 | +4,449 | 97,312 | 3,747 | +93,565 | +5,966 | TAIFEX Proxy |
| 自營商 | 4,552 | 5,766 | -1,214 | 3,012 | 4,513 | -1,501 | +287 | 4,472 | 3,154 | +1,318 | +1,036 | TAIFEX Proxy |
| 三大法人合計 | 77,963 | 75,420 | +2,543 | 62,760 | 61,046 | +1,714 | +829 | 116,383 | 124,932 | -8,549 | +1,433 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 105,231 | TAIFEX Proxy |
| 前十大交易人空方 OI | 100,512 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,719 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-20→2026-11-23) | +374 | TAIFEX Proxy snapshots (2026-11-20) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 83.13% | TAIFEX Proxy |
| 夜盤漲跌點數 | +3,170 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +3,215 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-23 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W4 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-25 00:14:39 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 145,433 | TAIFEX Proxy |
| Call 總未平倉量 OI | 82,454 | TAIFEX Proxy |
| Call OI 增減（共同合約） | unavailable | unavailable |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 74,482 | TAIFEX Proxy |
| Put 總未平倉量 OI | 18,390 | TAIFEX Proxy |
| Put OI 增減（共同合約） | unavailable | unavailable |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.95 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 4.48 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.22 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-20→2026-11-23) | -24.75 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-20→2026-11-23) | 0.85 | 百分點（pp） | TAIFEX Proxy |
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
| 外資 Call夜買 | 17,293 | TAIFEX Proxy |
| 外資 Call夜賣 | 15,366 | TAIFEX Proxy |
| 外資 Call夜淨 | +1,927 | TAIFEX Proxy |
| 外資 Put夜買 | 10,335 | TAIFEX Proxy |
| 外資 Put夜賣 | 11,817 | TAIFEX Proxy |
| 外資 Put夜淨 | -1,482 | TAIFEX Proxy |
| 外資 日盤淨總量 | -2,213 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -3,164 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +2,458 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 38,760 | TAIFEX Proxy |
| 自營商 Call日賣 | 51,825 | TAIFEX Proxy |
| 自營商 Call日淨 | -13,065 | TAIFEX Proxy |
| 自營商 Put日買 | 27,493 | TAIFEX Proxy |
| 自營商 Put日賣 | 29,478 | TAIFEX Proxy |
| 自營商 Put日淨 | -1,985 | TAIFEX Proxy |
| 自營商 Call夜買 | 29,556 | TAIFEX Proxy |
| 自營商 Call夜賣 | 29,400 | TAIFEX Proxy |
| 自營商 Call夜淨 | +156 | TAIFEX Proxy |
| 自營商 Put夜買 | 15,537 | TAIFEX Proxy |
| 自營商 Put夜賣 | 19,790 | TAIFEX Proxy |
| 自營商 Put夜淨 | -4,253 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,080 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -13,221 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +2,268 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 41,000 | 10,101 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 5,476 | TAIFEX Proxy |
| Call OI 第3大履約價 | 40,000 | 3,496 | TAIFEX Proxy |
| Call OI 最大履約價 | 41,000 | 10,101 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 41,000 | 10,101 | 12.25% | TAIFEX Proxy |
| C2 | 43,000 | 5,476 | 6.64% | TAIFEX Proxy |
| C3 | 40,000 | 3,496 | 4.24% | TAIFEX Proxy |
| C4 | 35,700 | 3,076 | 3.73% | TAIFEX Proxy |
| C5 | 42,000 | 2,992 | 3.63% | TAIFEX Proxy |
| C6 | 42,500 | 2,776 | 3.37% | TAIFEX Proxy |
| C7 | 35,800 | 2,669 | 3.24% | TAIFEX Proxy |
| C8 | 35,300 | 2,530 | 3.07% | TAIFEX Proxy |
| C9 | 39,100 | 2,172 | 2.63% | TAIFEX Proxy |
| C10 | 35,000 | 2,170 | 2.63% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 32,400 | 2,832 | TAIFEX Proxy |
| Put OI 第2大履約價 | 34,500 | 2,011 | TAIFEX Proxy |
| Put OI 第3大履約價 | 34,000 | 1,026 | TAIFEX Proxy |
| Put OI 最大履約價 | 32,400 | 2,832 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 32,400 | 2,832 | 15.4% | TAIFEX Proxy |
| P2 | 34,500 | 2,011 | 10.94% | TAIFEX Proxy |
| P3 | 34,000 | 1,026 | 5.58% | TAIFEX Proxy |
| P4 | 35,000 | 824 | 4.48% | TAIFEX Proxy |
| P5 | 33,000 | 822 | 4.47% | TAIFEX Proxy |
| P6 | 36,000 | 755 | 4.11% | TAIFEX Proxy |
| P7 | 39,500 | 544 | 2.96% | TAIFEX Proxy |
| P8 | 37,800 | 528 | 2.87% | TAIFEX Proxy |
| P9 | 32,600 | 383 | 2.08% | TAIFEX Proxy |
| P10 | 35,500 | 377 | 2.05% | TAIFEX Proxy |


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
| Gamma Wall 價位 | 35,700.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611W4 | TAIFEX Proxy |
| 資料日期 | 2026-11-23 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 33,285.92 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611W4 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 82,454 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 82,250 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 18,390 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 18,390 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-23 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：33,130.70～40,493.08
- 搜尋步長／計算次數：10.00／17
- 起點／終點 Net GEX：-132,055,955.05／4,290,320.77
- 搜尋區間最低／最高 Net GEX：-132,055,955.05／4,290,320.77
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-23","chain_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":540,"delta_rows":540},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":292,"delta_rows":292},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：31,290.11～42,333.67
- 搜尋步長／計算次數：10.00／1105
- 起點／終點 Net GEX：-595,230,144.75／6,311,137,725.63
- 搜尋區間最低／最高 Net GEX：-633,796,785.67／7,150,470,235.37
- 正負號交叉次數：1
- 擴大區間診斷 Flip：33,285.92

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 3,320,406,977.65 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 5,593,126,865.62 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 270 | 資料日期：2026-11-23 |
| 正 Net GEX 最大履約價 | 35,700 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 34,500 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：35,700（360,051,178.13 NT$）、35,800（314,156,442.73 NT$）、35,300（250,489,592.07 NT$）、37,200（234,198,043.95 NT$）、38,000（209,991,735.94 NT$）
- 負 Net GEX Top 5：34,500（-132,873,618.48 NT$）、32,400（-61,246,992.17 NT$）、34,000（-54,558,805.57 NT$）、33,000（-25,779,148.64 NT$）、37,800（-25,130,243.70 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-23","underlying":36811.89,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":3320406977.6549244,"gross_gex_1pct":5593126865.617987,"gamma_diagnostics":{"chain_rows":540,"delta_rows":540,"matched_strike_keys":540,"positive_oi_settlement_eligible":451,"invalid_oi":89,"invalid_settlement":0,"below_intrinsic":12,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":439},"formal_flip_diagnostics":{"search_lower_underlying":33130.701,"search_upper_underlying":40493.079000000005,"step":10,"evaluations":17,"start_net_gex_1pct":-132055955.0512737,"end_net_gex_1pct":4290320.774611087,"min_net_gex_1pct":-132055955.0512737,"max_net_gex_1pct":4290320.774611087,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":33280.106499999994,"upper_underlying":33290.106499999994,"estimated_underlying":33285.92383208902,"lower_net_gex_1pct":-5222200.731013372,"upper_net_gex_1pct":3754767.836526702},"wide_range_flip_diagnostics":{"search_lower_underlying":31290.106499999998,"search_upper_underlying":42333.6735,"reference_underlying":36811.89,"step":10,"evaluations":1105,"start_net_gex_1pct":-595230144.7509053,"end_net_gex_1pct":6311137725.634843,"min_net_gex_1pct":-633796785.6665167,"max_net_gex_1pct":7150470235.369522,"zero_crossings":1,"found":true,"selected_crossing_distance":3525.9661679109777},"expiry_selection_diagnostics":{"requested_date":"2026-11-23","chain_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":540,"delta_rows":540},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":292,"delta_rows":292},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":32400.0,"call_gex_1pct":0.0,"put_gex_1pct":-61246992.165950656,"net_gex_1pct":-61246992.165950656,"gross_gex_1pct":61246992.165950656,"call_oi":0,"put_oi":2832},{"strike":32500.0,"call_gex_1pct":0.0,"put_gex_1pct":-7029201.20043103,"net_gex_1pct":-7029201.20043103,"gross_gex_1pct":7029201.20043103,"call_oi":0,"put_oi":302},{"strike":32600.0,"call_gex_1pct":0.0,"put_gex_1pct":-9404927.568596687,"net_gex_1pct":-9404927.568596687,"gross_gex_1pct":9404927.568596687,"call_oi":0,"put_oi":383},{"strike":32700.0,"call_gex_1pct":0.0,"put_gex_1pct":-2353926.0848533846,"net_gex_1pct":-2353926.0848533846,"gross_gex_1pct":2353926.0848533846,"call_oi":0,"put_oi":92},{"strike":32800.0,"call_gex_1pct":0.0,"put_gex_1pct":-2692301.9591499614,"net_gex_1pct":-2692301.9591499614,"gross_gex_1pct":2692301.9591499614,"call_oi":0,"put_oi":96},{"strike":32900.0,"call_gex_1pct":0.0,"put_gex_1pct":-975679.7757888157,"net_gex_1pct":-975679.7757888157,"gross_gex_1pct":975679.7757888157,"call_oi":0,"put_oi":33},{"strike":33000.0,"call_gex_1pct":0.0,"put_gex_1pct":-25779148.64382194,"net_gex_1pct":-25779148.64382194,"gross_gex_1pct":25779148.64382194,"call_oi":0,"put_oi":822},{"strike":33100.0,"call_gex_1pct":0.0,"put_gex_1pct":-5368969.796675622,"net_gex_1pct":-5368969.796675622,"gross_gex_1pct":5368969.796675622,"call_oi":0,"put_oi":165},{"strike":33200.0,"call_gex_1pct":0.0,"put_gex_1pct":-12263176.926958265,"net_gex_1pct":-12263176.926958265,"gross_gex_1pct":12263176.926958265,"call_oi":0,"put_oi":356},{"strike":33300.0,"call_gex_1pct":0.0,"put_gex_1pct":-3427819.6832446707,"net_gex_1pct":-3427819.6832446707,"gross_gex_1pct":3427819.6832446707,"call_oi":0,"put_oi":93},{"strike":33400.0,"call_gex_1pct":0.0,"put_gex_1pct":-8101386.836031172,"net_gex_1pct":-8101386.836031172,"gross_gex_1pct":8101386.836031172,"call_oi":0,"put_oi":207},{"strike":33500.0,"call_gex_1pct":0.0,"put_gex_1pct":-12939047.180032747,"net_gex_1pct":-12939047.180032747,"gross_gex_1pct":12939047.180032747,"call_oi":0,"put_oi":313},{"strike":33600.0,"call_gex_1pct":0.0,"put_gex_1pct":-4493088.509634395,"net_gex_1pct":-4493088.509634395,"gross_gex_1pct":4493088.509634395,"call_oi":0,"put_oi":103},{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-3781417.0941734416,"net_gex_1pct":-3781417.0941734416,"gross_gex_1pct":3781417.0941734416,"call_oi":0,"put_oi":83},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-5215909.563718662,"net_gex_1pct":-5215909.563718662,"gross_gex_1pct":5215909.563718662,"call_oi":0,"put_oi":108},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-5129418.143748007,"net_gex_1pct":-5129418.143748007,"gross_gex_1pct":5129418.143748007,"call_oi":0,"put_oi":101},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-54558805.56833569,"net_gex_1pct":-54558805.56833569,"gross_gex_1pct":54558805.56833569,"call_oi":0,"put_oi":1026},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-6662723.839262259,"net_gex_1pct":-6662723.839262259,"gross_gex_1pct":6662723.839262259,"call_oi":0,"put_oi":120},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-8038466.8987349905,"net_gex_1pct":-8038466.8987349905,"gross_gex_1pct":8038466.8987349905,"call_oi":0,"put_oi":138},{"strike":34300.0,"call_gex_1pct":0.0,"put_gex_1pct":-4740087.0819012,"net_gex_1pct":-4740087.0819012,"gross_gex_1pct":4740087.0819012,"call_oi":0,"put_oi":78},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-11023575.282852152,"net_gex_1pct":-11023575.282852152,"gross_gex_1pct":11023575.282852152,"call_oi":0,"put_oi":174},{"strike":34500.0,"call_gex_1pct":0.0,"put_gex_1pct":-132873618.48177934,"net_gex_1pct":-132873618.48177934,"gross_gex_1pct":132873618.48177934,"call_oi":0,"put_oi":2011},{"strike":34600.0,"call_gex_1pct":2348005.2905431613,"put_gex_1pct":-21751599.37374248,"net_gex_1pct":-19403594.08319932,"gross_gex_1pct":24099604.66428564,"call_oi":81,"put_oi":318},{"strike":34700.0,"call_gex_1pct":1355530.653443217,"put_gex_1pct":-14256613.54271993,"net_gex_1pct":-12901082.889276713,"gross_gex_1pct":15612144.196163148,"call_oi":26,"put_oi":200},{"strike":34800.0,"call_gex_1pct":4243076.237846401,"put_gex_1pct":-14949571.035492893,"net_gex_1pct":-10706494.797646493,"gross_gex_1pct":19192647.273339294,"call_oi":65,"put_oi":203},{"strike":34900.0,"call_gex_1pct":149033163.49475196,"put_gex_1pct":-11694773.052112425,"net_gex_1pct":137338390.44263953,"gross_gex_1pct":160727936.5468644,"call_oi":1985,"put_oi":154},{"strike":35000.0,"call_gex_1pct":182746987.54989067,"put_gex_1pct":-64798252.71085094,"net_gex_1pct":117948734.83903973,"gross_gex_1pct":247545240.2607416,"call_oi":2170,"put_oi":824},{"strike":35050.0,"call_gex_1pct":176200.32286707807,"put_gex_1pct":-1188550.72286708,"net_gex_1pct":-1012350.400000002,"gross_gex_1pct":1364751.045734158,"call_oi":2,"put_oi":15},{"strike":35100.0,"call_gex_1pct":8388444.963809056,"put_gex_1pct":-9590633.090319617,"net_gex_1pct":-1202188.1265105605,"gross_gex_1pct":17979078.054128673,"call_oi":92,"put_oi":119},{"strike":35150.0,"call_gex_1pct":941291.9541147259,"put_gex_1pct":-1967349.1008513088,"net_gex_1pct":-1026057.1467365829,"gross_gex_1pct":2908641.054966035,"call_oi":10,"put_oi":24},{"strike":35200.0,"call_gex_1pct":199890939.23105174,"put_gex_1pct":-9997905.237699443,"net_gex_1pct":189893033.9933523,"gross_gex_1pct":209888844.4687512,"call_oi":2058,"put_oi":120},{"strike":35250.0,"call_gex_1pct":1002944.7650237051,"put_gex_1pct":-2802730.088995703,"net_gex_1pct":-1799785.323971998,"gross_gex_1pct":3805674.854019408,"call_oi":10,"put_oi":33},{"strike":35300.0,"call_gex_1pct":260383746.71839952,"put_gex_1pct":-9894154.65324877,"net_gex_1pct":250489592.06515077,"gross_gex_1pct":270277901.3716483,"call_oi":2530,"put_oi":114},{"strike":35350.0,"call_gex_1pct":0.0,"put_gex_1pct":-2943850.5015939367,"net_gex_1pct":-2943850.5015939367,"gross_gex_1pct":2943850.5015939367,"call_oi":0,"put_oi":34},{"strike":35400.0,"call_gex_1pct":8470792.192492055,"put_gex_1pct":-12141516.958387105,"net_gex_1pct":-3670724.76589505,"gross_gex_1pct":20612309.15087916,"call_oi":79,"put_oi":139},{"strike":35450.0,"call_gex_1pct":0.0,"put_gex_1pct":-1607861.04280093,"net_gex_1pct":-1607861.04280093,"gross_gex_1pct":1607861.04280093,"call_oi":0,"put_oi":18},{"strike":35500.0,"call_gex_1pct":16345572.801791597,"put_gex_1pct":-33823909.25006846,"net_gex_1pct":-17478336.448276866,"gross_gex_1pct":50169482.051860064,"call_oi":144,"put_oi":377},{"strike":35550.0,"call_gex_1pct":345913.83459299995,"put_gex_1pct":-3289812.053811472,"net_gex_1pct":-2943898.219218472,"gross_gex_1pct":3635725.888404472,"call_oi":3,"put_oi":36},{"strike":35600.0,"call_gex_1pct":11811922.159584193,"put_gex_1pct":-16283244.470271679,"net_gex_1pct":-4471322.310687486,"gross_gex_1pct":28095166.62985587,"call_oi":101,"put_oi":174},{"strike":35650.0,"call_gex_1pct":1421704.0707970948,"put_gex_1pct":-2518761.360311051,"net_gex_1pct":-1097057.289513956,"gross_gex_1pct":3940465.431108146,"call_oi":12,"put_oi":27},{"strike":35700.0,"call_gex_1pct":372696120.89123714,"put_gex_1pct":-12644942.765195174,"net_gex_1pct":360051178.12604195,"gross_gex_1pct":385341063.65643233,"call_oi":3076,"put_oi":134},{"strike":35750.0,"call_gex_1pct":1103133.5861684491,"put_gex_1pct":-1710448.141345565,"net_gex_1pct":-607314.5551771158,"gross_gex_1pct":2813581.727514014,"call_oi":9,"put_oi":18},{"strike":35800.0,"call_gex_1pct":330708520.81324923,"put_gex_1pct":-16552078.085869987,"net_gex_1pct":314156442.72737926,"gross_gex_1pct":347260598.8991192,"call_oi":2669,"put_oi":173},{"strike":35850.0,"call_gex_1pct":3165662.0623061936,"put_gex_1pct":-2999628.748223443,"net_gex_1pct":166033.31408275058,"gross_gex_1pct":6165290.810529636,"call_oi":25,"put_oi":31},{"strike":35900.0,"call_gex_1pct":23662034.589940805,"put_gex_1pct":-11396890.257045629,"net_gex_1pct":12265144.332895176,"gross_gex_1pct":35058924.846986435,"call_oi":185,"put_oi":117},{"strike":35950.0,"call_gex_1pct":2352514.3493194375,"put_gex_1pct":-3562911.358779287,"net_gex_1pct":-1210397.0094598494,"gross_gex_1pct":5915425.7080987245,"call_oi":18,"put_oi":36},{"strike":36000.0,"call_gex_1pct":206216379.31336164,"put_gex_1pct":-74513552.1605679,"net_gex_1pct":131702827.15279375,"gross_gex_1pct":280729931.4739295,"call_oi":1563,"put_oi":755},{"strike":36050.0,"call_gex_1pct":4208508.278966472,"put_gex_1pct":-3476645.6386625106,"net_gex_1pct":731862.640303961,"gross_gex_1pct":7685153.917628982,"call_oi":32,"put_oi":35},{"strike":36100.0,"call_gex_1pct":24181034.60257736,"put_gex_1pct":-11909135.677928677,"net_gex_1pct":12271898.924648682,"gross_gex_1pct":36090170.28050604,"call_oi":180,"put_oi":118},{"strike":36150.0,"call_gex_1pct":4625449.220911665,"put_gex_1pct":-2303102.8343940265,"net_gex_1pct":2322346.3865176383,"gross_gex_1pct":6928552.055305691,"call_oi":35,"put_oi":23},{"strike":36200.0,"call_gex_1pct":29822973.530010924,"put_gex_1pct":-13429300.45962773,"net_gex_1pct":16393673.070383193,"gross_gex_1pct":43252273.98963866,"call_oi":221,"put_oi":132},{"strike":36250.0,"call_gex_1pct":4548452.713670704,"put_gex_1pct":-6099609.63415872,"net_gex_1pct":-1551156.9204880167,"gross_gex_1pct":10648062.347829424,"call_oi":33,"put_oi":59},{"strike":36300.0,"call_gex_1pct":16524824.780777402,"put_gex_1pct":-8163653.434168947,"net_gex_1pct":8361171.346608455,"gross_gex_1pct":24688478.21494635,"call_oi":122,"put_oi":80},{"strike":36350.0,"call_gex_1pct":4287857.989950856,"put_gex_1pct":-1140592.5314293383,"net_gex_1pct":3147265.458521518,"gross_gex_1pct":5428450.521380194,"call_oi":31,"put_oi":11},{"strike":36400.0,"call_gex_1pct":23674873.060706064,"put_gex_1pct":-9553207.859177792,"net_gex_1pct":14121665.201528272,"gross_gex_1pct":33228080.919883855,"call_oi":172,"put_oi":92},{"strike":36450.0,"call_gex_1pct":1905332.25386872,"put_gex_1pct":-2152196.8639817066,"net_gex_1pct":-246864.61011298653,"gross_gex_1pct":4057529.1178504266,"call_oi":14,"put_oi":21},{"strike":36500.0,"call_gex_1pct":54099676.56970995,"put_gex_1pct":-29885258.30568302,"net_gex_1pct":24214418.26402693,"gross_gex_1pct":83984934.87539297,"call_oi":402,"put_oi":294},{"strike":36550.0,"call_gex_1pct":3726514.3660550867,"put_gex_1pct":-2722412.6741947983,"net_gex_1pct":1004101.6918602884,"gross_gex_1pct":6448927.040249885,"call_oi":28,"put_oi":27},{"strike":36600.0,"call_gex_1pct":19408257.61945791,"put_gex_1pct":-8232955.843704139,"net_gex_1pct":11175301.775753774,"gross_gex_1pct":27641213.46316205,"call_oi":142,"put_oi":80},{"strike":36650.0,"call_gex_1pct":4046611.4659700366,"put_gex_1pct":-2679375.4911414455,"net_gex_1pct":1367235.974828591,"gross_gex_1pct":6725986.957111482,"call_oi":29,"put_oi":26},{"strike":36700.0,"call_gex_1pct":20407440.224427767,"put_gex_1pct":-3769378.716800923,"net_gex_1pct":16638061.507626845,"gross_gex_1pct":24176818.94122869,"call_oi":147,"put_oi":36},{"strike":36750.0,"call_gex_1pct":6296413.281327161,"put_gex_1pct":-2726042.7028478556,"net_gex_1pct":3570370.5784793054,"gross_gex_1pct":9022455.984175017,"call_oi":45,"put_oi":26},{"strike":36800.0,"call_gex_1pct":21855197.555176225,"put_gex_1pct":-13438793.745245267,"net_gex_1pct":8416403.809930958,"gross_gex_1pct":35293991.30042149,"call_oi":157,"put_oi":128},{"strike":36850.0,"call_gex_1pct":5471752.340290425,"put_gex_1pct":-950841.5168635364,"net_gex_1pct":4520910.823426889,"gross_gex_1pct":6422593.857153961,"call_oi":39,"put_oi":9},{"strike":36900.0,"call_gex_1pct":22994851.495967947,"put_gex_1pct":-10634334.463380987,"net_gex_1pct":12360517.03258696,"gross_gex_1pct":33629185.95934893,"call_oi":169,"put_oi":102},{"strike":36950.0,"call_gex_1pct":2221985.3004118893,"put_gex_1pct":-623383.218443886,"net_gex_1pct":1598602.0819680034,"gross_gex_1pct":2845368.5188557752,"call_oi":16,"put_oi":6},{"strike":37000.0,"call_gex_1pct":115606924.66637574,"put_gex_1pct":-14702623.59457556,"net_gex_1pct":100904301.07180019,"gross_gex_1pct":130309548.2609513,"call_oi":826,"put_oi":142},{"strike":37050.0,"call_gex_1pct":4751533.621441415,"put_gex_1pct":-103185.15156193693,"net_gex_1pct":4648348.469879477,"gross_gex_1pct":4854718.773003352,"call_oi":35,"put_oi":1},{"strike":37100.0,"call_gex_1pct":32624789.713970892,"put_gex_1pct":-6067181.396469008,"net_gex_1pct":26557608.317501884,"gross_gex_1pct":38691971.1104399,"call_oi":240,"put_oi":59},{"strike":37150.0,"call_gex_1pct":5271222.350779666,"put_gex_1pct":0.0,"net_gex_1pct":5271222.350779666,"gross_gex_1pct":5271222.350779666,"call_oi":38,"put_oi":0},{"strike":37200.0,"call_gex_1pct":253891377.43972242,"put_gex_1pct":-19693333.494255956,"net_gex_1pct":234198043.94546646,"gross_gex_1pct":273584710.9339784,"call_oi":1863,"put_oi":191},{"strike":37250.0,"call_gex_1pct":6522555.786429087,"put_gex_1pct":0.0,"net_gex_1pct":6522555.786429087,"gross_gex_1pct":6522555.786429087,"call_oi":49,"put_oi":0},{"strike":37300.0,"call_gex_1pct":25564308.636865143,"put_gex_1pct":-6086965.079304545,"net_gex_1pct":19477343.557560597,"gross_gex_1pct":31651273.71616969,"call_oi":193,"put_oi":60},{"strike":37350.0,"call_gex_1pct":7117222.422519147,"put_gex_1pct":-1020515.373236259,"net_gex_1pct":6096707.049282888,"gross_gex_1pct":8137737.795755407,"call_oi":54,"put_oi":10},{"strike":37400.0,"call_gex_1pct":27766993.176867794,"put_gex_1pct":-13379249.580992334,"net_gex_1pct":14387743.59587546,"gross_gex_1pct":41146242.757860124,"call_oi":213,"put_oi":134},{"strike":37450.0,"call_gex_1pct":5707029.346080743,"put_gex_1pct":-1094618.4272455878,"net_gex_1pct":4612410.918835155,"gross_gex_1pct":6801647.773326331,"call_oi":44,"put_oi":11},{"strike":37500.0,"call_gex_1pct":55163134.238891326,"put_gex_1pct":-5003980.940563145,"net_gex_1pct":50159153.29832818,"gross_gex_1pct":60167115.17945447,"call_oi":420,"put_oi":50},{"strike":37550.0,"call_gex_1pct":5047127.1504790345,"put_gex_1pct":0.0,"net_gex_1pct":5047127.1504790345,"gross_gex_1pct":5047127.1504790345,"call_oi":39,"put_oi":0},{"strike":37600.0,"call_gex_1pct":20137364.321628664,"put_gex_1pct":-3447541.8747048075,"net_gex_1pct":16689822.446923856,"gross_gex_1pct":23584906.19633347,"call_oi":157,"put_oi":35},{"strike":37650.0,"call_gex_1pct":6475373.855682675,"put_gex_1pct":-98160.21855720005,"net_gex_1pct":6377213.637125474,"gross_gex_1pct":6573534.074239875,"call_oi":51,"put_oi":1},{"strike":37700.0,"call_gex_1pct":33052639.253979046,"put_gex_1pct":-1467235.3783499915,"net_gex_1pct":31585403.875629053,"gross_gex_1pct":34519874.63232904,"call_oi":263,"put_oi":15},{"strike":37750.0,"call_gex_1pct":8958454.702560885,"put_gex_1pct":-779733.6571168709,"net_gex_1pct":8178721.045444014,"gross_gex_1pct":9738188.359677756,"call_oi":71,"put_oi":8},{"strike":37800.0,"call_gex_1pct":26145031.384307314,"put_gex_1pct":-51275275.085955754,"net_gex_1pct":-25130243.70164844,"gross_gex_1pct":77420306.47026306,"call_oi":209,"put_oi":528},{"strike":37850.0,"call_gex_1pct":6891977.154589479,"put_gex_1pct":-665750.7678257836,"net_gex_1pct":6226226.386763696,"gross_gex_1pct":7557727.922415262,"call_oi":56,"put_oi":7},{"strike":37900.0,"call_gex_1pct":27204808.786120504,"put_gex_1pct":-2443083.7564649577,"net_gex_1pct":24761725.029655546,"gross_gex_1pct":29647892.542585462,"call_oi":227,"put_oi":26},{"strike":37950.0,"call_gex_1pct":10538851.307535764,"put_gex_1pct":0.0,"net_gex_1pct":10538851.307535764,"gross_gex_1pct":10538851.307535764,"call_oi":89,"put_oi":0},{"strike":38000.0,"call_gex_1pct":219426521.73402706,"put_gex_1pct":-9434785.796320781,"net_gex_1pct":209991735.9377063,"gross_gex_1pct":228861307.53034782,"call_oi":1885,"put_oi":102},{"strike":38050.0,"call_gex_1pct":9180567.981223924,"put_gex_1pct":-1096807.6091941202,"net_gex_1pct":8083760.372029804,"gross_gex_1pct":10277375.590418044,"call_oi":80,"put_oi":12},{"strike":38100.0,"call_gex_1pct":15864750.795925548,"put_gex_1pct":-1638766.421651974,"net_gex_1pct":14225984.374273574,"gross_gex_1pct":17503517.21757752,"call_oi":139,"put_oi":18},{"strike":38150.0,"call_gex_1pct":6358440.965866501,"put_gex_1pct":0.0,"net_gex_1pct":6358440.965866501,"gross_gex_1pct":6358440.965866501,"call_oi":57,"put_oi":0},{"strike":38200.0,"call_gex_1pct":27924682.979749043,"put_gex_1pct":-1523055.4620945847,"net_gex_1pct":26401627.517654456,"gross_gex_1pct":29447738.44184363,"call_oi":251,"put_oi":17},{"strike":38250.0,"call_gex_1pct":9378656.467580365,"put_gex_1pct":-178407.9724726093,"net_gex_1pct":9200248.495107755,"gross_gex_1pct":9557064.440052975,"call_oi":86,"put_oi":2},{"strike":38300.0,"call_gex_1pct":18386354.976577796,"put_gex_1pct":-2291554.000489475,"net_gex_1pct":16094800.97608832,"gross_gex_1pct":20677908.97706727,"call_oi":171,"put_oi":26},{"strike":38350.0,"call_gex_1pct":6417726.967441653,"put_gex_1pct":0.0,"net_gex_1pct":6417726.967441653,"gross_gex_1pct":6417726.967441653,"call_oi":61,"put_oi":0},{"strike":38400.0,"call_gex_1pct":23414995.303766556,"put_gex_1pct":-8088616.753800417,"net_gex_1pct":15326378.549966138,"gross_gex_1pct":31503612.057566974,"call_oi":227,"put_oi":94},{"strike":38450.0,"call_gex_1pct":7552426.428911878,"put_gex_1pct":0.0,"net_gex_1pct":7552426.428911878,"gross_gex_1pct":7552426.428911878,"call_oi":75,"put_oi":0},{"strike":38500.0,"call_gex_1pct":75145144.1811243,"put_gex_1pct":-5293109.094320342,"net_gex_1pct":69852035.08680396,"gross_gex_1pct":80438253.27544464,"call_oi":754,"put_oi":63},{"strike":38550.0,"call_gex_1pct":7687407.2202689955,"put_gex_1pct":0.0,"net_gex_1pct":7687407.2202689955,"gross_gex_1pct":7687407.2202689955,"call_oi":79,"put_oi":0},{"strike":38600.0,"call_gex_1pct":26044773.951495826,"put_gex_1pct":-2461035.455304033,"net_gex_1pct":23583738.496191792,"gross_gex_1pct":28505809.40679986,"call_oi":273,"put_oi":30},{"strike":38650.0,"call_gex_1pct":13436811.885572903,"put_gex_1pct":-324235.20956489234,"net_gex_1pct":13112576.67600801,"gross_gex_1pct":13761047.095137795,"call_oi":144,"put_oi":4},{"strike":38700.0,"call_gex_1pct":114654392.3948177,"put_gex_1pct":-6845586.042410632,"net_gex_1pct":107808806.35240707,"gross_gex_1pct":121499978.43722832,"call_oi":1258,"put_oi":86},{"strike":38750.0,"call_gex_1pct":7209705.64617277,"put_gex_1pct":0.0,"net_gex_1pct":7209705.64617277,"gross_gex_1pct":7209705.64617277,"call_oi":81,"put_oi":0},{"strike":38800.0,"call_gex_1pct":37357048.236382306,"put_gex_1pct":-1954600.236398498,"net_gex_1pct":35402447.99998381,"gross_gex_1pct":39311648.4727808,"call_oi":430,"put_oi":25},{"strike":38850.0,"call_gex_1pct":8476940.542417204,"put_gex_1pct":0.0,"net_gex_1pct":8476940.542417204,"gross_gex_1pct":8476940.542417204,"call_oi":100,"put_oi":0},{"strike":38900.0,"call_gex_1pct":178542991.0353184,"put_gex_1pct":-5540036.939497553,"net_gex_1pct":173002954.09582084,"gross_gex_1pct":184083027.97481596,"call_oi":2162,"put_oi":73},{"strike":38950.0,"call_gex_1pct":5705651.839503902,"put_gex_1pct":-524848.6122077415,"net_gex_1pct":5180803.2272961605,"gross_gex_1pct":6230500.4517116435,"call_oi":71,"put_oi":7},{"strike":39000.0,"call_gex_1pct":117196836.2950393,"put_gex_1pct":-5110824.416063727,"net_gex_1pct":112086011.87897557,"gross_gex_1pct":122307660.71110302,"call_oi":1502,"put_oi":69},{"strike":39050.0,"call_gex_1pct":7813837.424291303,"put_gex_1pct":-438987.800066982,"net_gex_1pct":7374849.624224321,"gross_gex_1pct":8252825.224358286,"call_oi":103,"put_oi":6},{"strike":39100.0,"call_gex_1pct":160395354.18713257,"put_gex_1pct":-8991496.70008686,"net_gex_1pct":151403857.4870457,"gross_gex_1pct":169386850.88721943,"call_oi":2172,"put_oi":125},{"strike":39150.0,"call_gex_1pct":4450462.59311725,"put_gex_1pct":-355258.2809394874,"net_gex_1pct":4095204.312177763,"gross_gex_1pct":4805720.874056738,"call_oi":62,"put_oi":5},{"strike":39200.0,"call_gex_1pct":18268564.863229133,"put_gex_1pct":-2236166.808638353,"net_gex_1pct":16032398.05459078,"gross_gex_1pct":20504731.671867486,"call_oi":262,"put_oi":32},{"strike":39250.0,"call_gex_1pct":3919194.6053731157,"put_gex_1pct":-414131.42593456997,"net_gex_1pct":3505063.179438546,"gross_gex_1pct":4333326.031307686,"call_oi":58,"put_oi":6},{"strike":39300.0,"call_gex_1pct":17098054.58173252,"put_gex_1pct":-613466.5020139287,"net_gex_1pct":16484588.07971859,"gross_gex_1pct":17711521.08374645,"call_oi":263,"put_oi":9},{"strike":39350.0,"call_gex_1pct":6598846.640002774,"put_gex_1pct":-335342.09063840966,"net_gex_1pct":6263504.549364365,"gross_gex_1pct":6934188.730641183,"call_oi":104,"put_oi":5},{"strike":39400.0,"call_gex_1pct":14866223.48821177,"put_gex_1pct":-990107.4229709466,"net_gex_1pct":13876116.065240823,"gross_gex_1pct":15856330.911182716,"call_oi":240,"put_oi":15},{"strike":39450.0,"call_gex_1pct":12732364.46476087,"put_gex_1pct":-649777.0001686075,"net_gex_1pct":12082587.464592263,"gross_gex_1pct":13382141.464929476,"call_oi":212,"put_oi":10},{"strike":39500.0,"call_gex_1pct":37104031.48666893,"put_gex_1pct":-34910284.1973381,"net_gex_1pct":2193747.2893308327,"gross_gex_1pct":72014315.68400702,"call_oi":649,"put_oi":544},{"strike":39550.0,"call_gex_1pct":7153052.864159749,"put_gex_1pct":-379148.85020794766,"net_gex_1pct":6773904.013951801,"gross_gex_1pct":7532201.714367697,"call_oi":130,"put_oi":6},{"strike":39600.0,"call_gex_1pct":13261622.911399277,"put_gex_1pct":-1372808.632241939,"net_gex_1pct":11888814.279157339,"gross_gex_1pct":14634431.543641215,"call_oi":249,"put_oi":22},{"strike":39650.0,"call_gex_1pct":2868230.1505960524,"put_gex_1pct":-553169.0477960617,"net_gex_1pct":2315061.1027999907,"gross_gex_1pct":3421399.198392114,"call_oi":55,"put_oi":9},{"strike":39700.0,"call_gex_1pct":28246666.466532793,"put_gex_1pct":-546149.4104722107,"net_gex_1pct":27700517.056060582,"gross_gex_1pct":28792815.877005003,"call_oi":573,"put_oi":9},{"strike":39750.0,"call_gex_1pct":5018167.771932615,"put_gex_1pct":-358728.6112544553,"net_gex_1pct":4659439.160678159,"gross_gex_1pct":5376896.3831870705,"call_oi":105,"put_oi":6},{"strike":39800.0,"call_gex_1pct":33762299.87007893,"put_gex_1pct":-707013.9464993823,"net_gex_1pct":33055285.923579548,"gross_gex_1pct":34469313.81657831,"call_oi":729,"put_oi":12},{"strike":39850.0,"call_gex_1pct":3935648.801180606,"put_gex_1pct":-290357.21195034275,"net_gex_1pct":3645291.589230263,"gross_gex_1pct":4226006.013130949,"call_oi":90,"put_oi":5},{"strike":39900.0,"call_gex_1pct":16185238.864512015,"put_gex_1pct":-229317.2375682688,"net_gex_1pct":15955921.626943747,"gross_gex_1pct":16414556.102080284,"call_oi":379,"put_oi":4},{"strike":39950.0,"call_gex_1pct":12818158.618930269,"put_gex_1pct":-565194.7231114978,"net_gex_1pct":12252963.895818772,"gross_gex_1pct":13383353.342041766,"call_oi":313,"put_oi":10},{"strike":40000.0,"call_gex_1pct":139261797.64176542,"put_gex_1pct":-2786559.006952971,"net_gex_1pct":136475238.63481244,"gross_gex_1pct":142048356.6487184,"call_oi":3496,"put_oi":50},{"strike":40050.0,"call_gex_1pct":8186168.921200248,"put_gex_1pct":-549636.0041831526,"net_gex_1pct":7636532.917017096,"gross_gex_1pct":8735804.9253834,"call_oi":214,"put_oi":10},{"strike":40100.0,"call_gex_1pct":19409235.205407742,"put_gex_1pct":-325516.3794347102,"net_gex_1pct":19083718.825973034,"gross_gex_1pct":19734751.58484245,"call_oi":540,"put_oi":6},{"strike":40150.0,"call_gex_1pct":3927653.969668814,"put_gex_1pct":-321103.23530625954,"net_gex_1pct":3606550.7343625543,"gross_gex_1pct":4248757.204975073,"call_oi":112,"put_oi":6},{"strike":40200.0,"call_gex_1pct":12617218.352193536,"put_gex_1pct":-1003208.4625203848,"net_gex_1pct":11614009.889673151,"gross_gex_1pct":13620426.814713921,"call_oi":389,"put_oi":19},{"strike":40250.0,"call_gex_1pct":2229108.0856775944,"put_gex_1pct":-364728.1878812643,"net_gex_1pct":1864379.89779633,"gross_gex_1pct":2593836.273558859,"call_oi":71,"put_oi":7},{"strike":40300.0,"call_gex_1pct":6348561.1684014425,"put_gex_1pct":-154249.82419898498,"net_gex_1pct":6194311.344202458,"gross_gex_1pct":6502810.992600427,"call_oi":209,"put_oi":3},{"strike":40350.0,"call_gex_1pct":3018645.250968841,"put_gex_1pct":-152238.70411231444,"net_gex_1pct":2866406.5468565263,"gross_gex_1pct":3170883.9550811555,"call_oi":102,"put_oi":3},{"strike":40400.0,"call_gex_1pct":5394487.201895462,"put_gex_1pct":-300553.76472475944,"net_gex_1pct":5093933.437170703,"gross_gex_1pct":5695040.966620222,"call_oi":204,"put_oi":6},{"strike":40450.0,"call_gex_1pct":2513768.760508368,"put_gex_1pct":-98908.40495461778,"net_gex_1pct":2414860.35555375,"gross_gex_1pct":2612677.1654629856,"call_oi":101,"put_oi":2},{"strike":40500.0,"call_gex_1pct":16307016.937701955,"put_gex_1pct":-1219751.025225816,"net_gex_1pct":15087265.91247614,"gross_gex_1pct":17526767.96292777,"call_oi":683,"put_oi":25},{"strike":40550.0,"call_gex_1pct":4438571.23439904,"put_gex_1pct":0.0,"net_gex_1pct":4438571.23439904,"gross_gex_1pct":4438571.23439904,"call_oi":205,"put_oi":0},{"strike":40600.0,"call_gex_1pct":4453183.578275077,"put_gex_1pct":-523365.61848460365,"net_gex_1pct":3929817.9597904733,"gross_gex_1pct":4976549.19675968,"call_oi":216,"put_oi":11},{"strike":40650.0,"call_gex_1pct":904192.6526307022,"put_gex_1pct":0.0,"net_gex_1pct":904192.6526307022,"gross_gex_1pct":904192.6526307022,"call_oi":47,"put_oi":0},{"strike":40700.0,"call_gex_1pct":6639573.133224175,"put_gex_1pct":-371385.965820135,"net_gex_1pct":6268187.167404041,"gross_gex_1pct":7010959.09904431,"call_oi":358,"put_oi":8},{"strike":40750.0,"call_gex_1pct":937391.3351681565,"put_gex_1pct":-687979.7622836982,"net_gex_1pct":249411.57288445835,"gross_gex_1pct":1625371.0974518547,"call_oi":64,"put_oi":15},{"strike":40800.0,"call_gex_1pct":7164829.627710341,"put_gex_1pct":-2216556.824553472,"net_gex_1pct":4948272.803156869,"gross_gex_1pct":9381386.452263813,"call_oi":518,"put_oi":49},{"strike":40850.0,"call_gex_1pct":1312635.0106737574,"put_gex_1pct":-1117477.0126006529,"net_gex_1pct":195157.99807310454,"gross_gex_1pct":2430112.0232744105,"call_oi":104,"put_oi":25},{"strike":40900.0,"call_gex_1pct":2988213.2037830674,"put_gex_1pct":-1457750.997129854,"net_gex_1pct":1530462.2066532134,"gross_gex_1pct":4445964.200912922,"call_oi":247,"put_oi":33},{"strike":40950.0,"call_gex_1pct":633851.2518472901,"put_gex_1pct":-43661.044146174405,"net_gex_1pct":590190.2077011156,"gross_gex_1pct":677512.2959934645,"call_oi":69,"put_oi":1},{"strike":41000.0,"call_gex_1pct":84582784.91658038,"put_gex_1pct":-517908.3053675924,"net_gex_1pct":84064876.61121279,"gross_gex_1pct":85100693.22194797,"call_oi":10101,"put_oi":12},{"strike":41050.0,"call_gex_1pct":3129525.0051984717,"put_gex_1pct":-42667.86237652389,"net_gex_1pct":3086857.142821948,"gross_gex_1pct":3172192.8675749954,"call_oi":471,"put_oi":1},{"strike":41100.0,"call_gex_1pct":2426051.8775230544,"put_gex_1pct":-168748.86152969924,"net_gex_1pct":2257303.0159933553,"gross_gex_1pct":2594800.7390527534,"call_oi":401,"put_oi":4},{"strike":41150.0,"call_gex_1pct":943364.6937608337,"put_gex_1pct":-292017.3115024175,"net_gex_1pct":651347.3822584162,"gross_gex_1pct":1235382.0052632513,"call_oi":168,"put_oi":7},{"strike":41200.0,"call_gex_1pct":2103056.092610975,"put_gex_1pct":-247537.08049534902,"net_gex_1pct":1855519.0121156257,"gross_gex_1pct":2350593.173106324,"call_oi":406,"put_oi":6},{"strike":41250.0,"call_gex_1pct":910526.4513344147,"put_gex_1pct":0.0,"net_gex_1pct":910526.4513344147,"gross_gex_1pct":910526.4513344147,"call_oi":192,"put_oi":0},{"strike":41300.0,"call_gex_1pct":765459.3605899086,"put_gex_1pct":-40363.46830369025,"net_gex_1pct":725095.8922862184,"gross_gex_1pct":805822.8288935988,"call_oi":178,"put_oi":1},{"strike":41350.0,"call_gex_1pct":396740.66573192313,"put_gex_1pct":0.0,"net_gex_1pct":396740.66573192313,"gross_gex_1pct":396740.66573192313,"call_oi":115,"put_oi":0},{"strike":41400.0,"call_gex_1pct":420207.6597340316,"put_gex_1pct":-79013.63896752326,"net_gex_1pct":341194.0207665083,"gross_gex_1pct":499221.2987015549,"call_oi":132,"put_oi":2},{"strike":41450.0,"call_gex_1pct":268346.27715249616,"put_gex_1pct":-195456.79948767458,"net_gex_1pct":72889.47766482158,"gross_gex_1pct":463803.07664017077,"call_oi":92,"put_oi":5},{"strike":41500.0,"call_gex_1pct":2538594.8924261997,"put_gex_1pct":-116052.43689326491,"net_gex_1pct":2422542.455532935,"gross_gex_1pct":2654647.3293194645,"call_oi":885,"put_oi":3},{"strike":41550.0,"call_gex_1pct":132608.19499787854,"put_gex_1pct":-76569.88002141615,"net_gex_1pct":56038.314976462396,"gross_gex_1pct":209178.0750192947,"call_oi":47,"put_oi":2},{"strike":41600.0,"call_gex_1pct":352514.45395174937,"put_gex_1pct":-37893.515235455,"net_gex_1pct":314620.93871629436,"gross_gex_1pct":390407.9691872044,"call_oi":127,"put_oi":1},{"strike":41650.0,"call_gex_1pct":210301.00645023247,"put_gex_1pct":-75019.30393443642,"net_gex_1pct":135281.70251579606,"gross_gex_1pct":285320.3103846689,"call_oi":77,"put_oi":2},{"strike":41700.0,"call_gex_1pct":252656.8347603866,"put_gex_1pct":-148532.5557729806,"net_gex_1pct":104124.27898740603,"gross_gex_1pct":401189.3905333672,"call_oi":94,"put_oi":4},{"strike":41750.0,"call_gex_1pct":51296.96444016235,"put_gex_1pct":-110291.31782917307,"net_gex_1pct":-58994.35338901072,"gross_gex_1pct":161588.2822693354,"call_oi":21,"put_oi":3},{"strike":41800.0,"call_gex_1pct":185157.01106149444,"put_gex_1pct":-36401.3567750984,"net_gex_1pct":148755.65428639605,"gross_gex_1pct":221558.36783659284,"call_oi":77,"put_oi":1},{"strike":41850.0,"call_gex_1pct":82863.93428697843,"put_gex_1pct":-36045.70228187965,"net_gex_1pct":46818.232005098784,"gross_gex_1pct":118909.63656885808,"call_oi":35,"put_oi":1},{"strike":41900.0,"call_gex_1pct":137552.09146353765,"put_gex_1pct":-142786.50678331254,"net_gex_1pct":-5234.415319774882,"gross_gex_1pct":280338.5982468502,"call_oi":59,"put_oi":4},{"strike":41950.0,"call_gex_1pct":68884.63882334848,"put_gex_1pct":-35353.954011429705,"net_gex_1pct":33530.68481191877,"gross_gex_1pct":104238.59283477819,"call_oi":30,"put_oi":1},{"strike":42000.0,"call_gex_1pct":6176068.064944621,"put_gex_1pct":-315157.6293541775,"net_gex_1pct":5860910.435590444,"gross_gex_1pct":6491225.694298798,"call_oi":2992,"put_oi":9},{"strike":42050.0,"call_gex_1pct":93541.5994750553,"put_gex_1pct":-69374.2876165995,"net_gex_1pct":24167.31185845581,"gross_gex_1pct":162915.88709165482,"call_oi":46,"put_oi":2},{"strike":42100.0,"call_gex_1pct":378677.88002328546,"put_gex_1pct":-103088.05194116643,"net_gex_1pct":275589.828082119,"gross_gex_1pct":481765.9319644519,"call_oi":189,"put_oi":3},{"strike":42150.0,"call_gex_1pct":81640.43671121237,"put_gex_1pct":-170219.90972971817,"net_gex_1pct":-88579.4730185058,"gross_gex_1pct":251860.34644093056,"call_oi":46,"put_oi":5},{"strike":42200.0,"call_gex_1pct":309587.8289586807,"put_gex_1pct":-134923.5597210747,"net_gex_1pct":174664.26923760597,"gross_gex_1pct":444511.3886797554,"call_oi":177,"put_oi":4},{"strike":42250.0,"call_gex_1pct":108611.47867629869,"put_gex_1pct":-133693.0604468732,"net_gex_1pct":-25081.5817705745,"gross_gex_1pct":242304.53912317188,"call_oi":63,"put_oi":4},{"strike":42300.0,"call_gex_1pct":190343.51563659133,"put_gex_1pct":-33120.96941707587,"net_gex_1pct":157222.54621951547,"gross_gex_1pct":223464.4850536672,"call_oi":112,"put_oi":1},{"strike":42350.0,"call_gex_1pct":85553.9635928735,"put_gex_1pct":0.0,"net_gex_1pct":85553.9635928735,"gross_gex_1pct":85553.9635928735,"call_oi":58,"put_oi":0},{"strike":42400.0,"call_gex_1pct":164348.93732028056,"put_gex_1pct":-32531.83569073225,"net_gex_1pct":131817.1016295483,"gross_gex_1pct":196880.77301101282,"call_oi":113,"put_oi":1},{"strike":42450.0,"call_gex_1pct":41592.99550661972,"put_gex_1pct":0.0,"net_gex_1pct":41592.99550661972,"gross_gex_1pct":41592.99550661972,"call_oi":29,"put_oi":0},{"strike":42500.0,"call_gex_1pct":3926737.1134578628,"put_gex_1pct":-159812.35986083883,"net_gex_1pct":3766924.753597024,"gross_gex_1pct":4086549.4733187016,"call_oi":2776,"put_oi":5},{"strike":42550.0,"call_gex_1pct":96273.56569622416,"put_gex_1pct":-285164.134993165,"net_gex_1pct":-188890.5692969408,"gross_gex_1pct":381437.70068938914,"call_oi":69,"put_oi":9},{"strike":42600.0,"call_gex_1pct":166549.53219842794,"put_gex_1pct":-94235.77782753298,"net_gex_1pct":72313.75437089497,"gross_gex_1pct":260785.3100259609,"call_oi":121,"put_oi":3},{"strike":42650.0,"call_gex_1pct":18552.59471463638,"put_gex_1pct":-124573.71338915791,"net_gex_1pct":-106021.11867452154,"gross_gex_1pct":143126.3081037943,"call_oi":16,"put_oi":4},{"strike":42700.0,"call_gex_1pct":56060.69578112664,"put_gex_1pct":-123517.21897456748,"net_gex_1pct":-67456.52319344084,"gross_gex_1pct":179577.91475569413,"call_oi":49,"put_oi":4},{"strike":42750.0,"call_gex_1pct":20321.91743068542,"put_gex_1pct":-30619.452069919866,"net_gex_1pct":-10297.534639234447,"gross_gex_1pct":50941.36950060529,"call_oi":18,"put_oi":1},{"strike":42800.0,"call_gex_1pct":94709.17469466623,"put_gex_1pct":-151818.8521782869,"net_gex_1pct":-57109.677483620675,"gross_gex_1pct":246528.02687295314,"call_oi":85,"put_oi":5},{"strike":42850.0,"call_gex_1pct":23095.3047477408,"put_gex_1pct":-90336.48900388741,"net_gex_1pct":-67241.18425614662,"gross_gex_1pct":113431.79375162821,"call_oi":21,"put_oi":3},{"strike":42900.0,"call_gex_1pct":44150.27590019797,"put_gex_1pct":-59729.07172664645,"net_gex_1pct":-15578.795826448477,"gross_gex_1pct":103879.34762684442,"call_oi":50,"put_oi":2},{"strike":42950.0,"call_gex_1pct":65376.40427000833,"put_gex_1pct":-29620.797944548718,"net_gex_1pct":35755.60632545961,"gross_gex_1pct":94997.20221455705,"call_oi":75,"put_oi":1},{"strike":43000.0,"call_gex_1pct":4712678.215671627,"put_gex_1pct":-146904.3044462227,"net_gex_1pct":4565773.911225405,"gross_gex_1pct":4859582.520117849,"call_oi":5476,"put_oi":5},{"strike":43050.0,"call_gex_1pct":11896.642729637188,"put_gex_1pct":-174867.83377744432,"net_gex_1pct":-162971.19104780714,"gross_gex_1pct":186764.4765070815,"call_oi":14,"put_oi":6},{"strike":43100.0,"call_gex_1pct":36825.415168013686,"put_gex_1pct":-28912.04895640314,"net_gex_1pct":7913.366211610544,"gross_gex_1pct":65737.46412441683,"call_oi":59,"put_oi":1},{"strike":43150.0,"call_gex_1pct":7396.389795063361,"put_gex_1pct":-57366.02018854701,"net_gex_1pct":-49969.63039348365,"gross_gex_1pct":64762.40998361037,"call_oi":12,"put_oi":2},{"strike":43200.0,"call_gex_1pct":132095.1340087385,"put_gex_1pct":-56914.88789399025,"net_gex_1pct":75180.24611474825,"gross_gex_1pct":189010.02190272877,"call_oi":217,"put_oi":2},{"strike":43250.0,"call_gex_1pct":28259.10548568661,"put_gex_1pct":-56470.54869399042,"net_gex_1pct":-28211.443208303812,"gross_gex_1pct":84729.65417967703,"call_oi":47,"put_oi":2},{"strike":43300.0,"call_gex_1pct":40981.45189663227,"put_gex_1pct":0.0,"net_gex_1pct":40981.45189663227,"gross_gex_1pct":40981.45189663227,"call_oi":69,"put_oi":0},{"strike":43350.0,"call_gex_1pct":39312.829362672295,"put_gex_1pct":0.0,"net_gex_1pct":39312.829362672295,"gross_gex_1pct":39312.829362672295,"call_oi":67,"put_oi":0},{"strike":43400.0,"call_gex_1pct":17273.797192787766,"put_gex_1pct":-27588.415419081306,"net_gex_1pct":-10314.61822629354,"gross_gex_1pct":44862.21261186907,"call_oi":50,"put_oi":1},{"strike":43450.0,"call_gex_1pct":17407.39397670629,"put_gex_1pct":0.0,"net_gex_1pct":17407.39397670629,"gross_gex_1pct":17407.39397670629,"call_oi":51,"put_oi":0},{"strike":43500.0,"call_gex_1pct":58344.18894000307,"put_gex_1pct":-271728.57174648915,"net_gex_1pct":-213384.38280648607,"gross_gex_1pct":330072.7606864922,"call_oi":173,"put_oi":10},{"strike":43550.0,"call_gex_1pct":15996.397376003348,"put_gex_1pct":0.0,"net_gex_1pct":15996.397376003348,"gross_gex_1pct":15996.397376003348,"call_oi":48,"put_oi":0},{"strike":43600.0,"call_gex_1pct":12185.771225599006,"put_gex_1pct":-53538.46353538596,"net_gex_1pct":-41352.69230978696,"gross_gex_1pct":65724.23476098497,"call_oi":37,"put_oi":2},{"strike":43650.0,"call_gex_1pct":12369.31209940819,"put_gex_1pct":0.0,"net_gex_1pct":12369.31209940819,"gross_gex_1pct":12369.31209940819,"call_oi":38,"put_oi":0},{"strike":43700.0,"call_gex_1pct":23165.667508331702,"put_gex_1pct":-79131.13994590657,"net_gex_1pct":-55965.47243757487,"gross_gex_1pct":102296.80745423827,"call_oi":72,"put_oi":3},{"strike":43750.0,"call_gex_1pct":17174.954457496056,"put_gex_1pct":0.0,"net_gex_1pct":17174.954457496056,"gross_gex_1pct":17174.954457496056,"call_oi":54,"put_oi":0},{"strike":43800.0,"call_gex_1pct":16036.149623476364,"put_gex_1pct":-51991.671295308464,"net_gex_1pct":-35955.5216718321,"gross_gex_1pct":68027.82091878483,"call_oi":51,"put_oi":2},{"strike":43850.0,"call_gex_1pct":14611.46953181249,"put_gex_1pct":-129046.03273941072,"net_gex_1pct":-114434.56320759823,"gross_gex_1pct":143657.5022712232,"call_oi":47,"put_oi":5},{"strike":43900.0,"call_gex_1pct":14140.26250252148,"put_gex_1pct":-76875.47173208668,"net_gex_1pct":-62735.2092295652,"gross_gex_1pct":91015.73423460816,"call_oi":46,"put_oi":3},{"strike":43950.0,"call_gex_1pct":9119.298967157487,"put_gex_1pct":0.0,"net_gex_1pct":9119.298967157487,"gross_gex_1pct":9119.298967157487,"call_oi":30,"put_oi":0},{"strike":44000.0,"call_gex_1pct":207427.47894732203,"put_gex_1pct":-808466.9750231561,"net_gex_1pct":-601039.4960758341,"gross_gex_1pct":1015894.4539704781,"call_oi":690,"put_oi":32},{"strike":44050.0,"call_gex_1pct":4757.185796274355,"put_gex_1pct":-50175.957594878695,"net_gex_1pct":-45418.77179860434,"gross_gex_1pct":54933.14339115305,"call_oi":16,"put_oi":2},{"strike":44100.0,"call_gex_1pct":12351.730035940258,"put_gex_1pct":0.0,"net_gex_1pct":12351.730035940258,"gross_gex_1pct":12351.730035940258,"call_oi":42,"put_oi":0},{"strike":44150.0,"call_gex_1pct":2909.1212407289745,"put_gex_1pct":0.0,"net_gex_1pct":2909.1212407289745,"gross_gex_1pct":2909.1212407289745,"call_oi":10,"put_oi":0},{"strike":44200.0,"call_gex_1pct":15253.007586173686,"put_gex_1pct":0.0,"net_gex_1pct":15253.007586173686,"gross_gex_1pct":15253.007586173686,"call_oi":53,"put_oi":0},{"strike":44250.0,"call_gex_1pct":1708.3728872564457,"put_gex_1pct":-169613.56330829085,"net_gex_1pct":-167905.1904210344,"gross_gex_1pct":171321.93619554729,"call_oi":6,"put_oi":7},{"strike":44300.0,"call_gex_1pct":10705.337668819584,"put_gex_1pct":-120326.88325261544,"net_gex_1pct":-109621.54558379586,"gross_gex_1pct":131032.22092143503,"call_oi":38,"put_oi":5},{"strike":44350.0,"call_gex_1pct":5017.735157795443,"put_gex_1pct":0.0,"net_gex_1pct":5017.735157795443,"gross_gex_1pct":5017.735157795443,"call_oi":18,"put_oi":0},{"strike":44400.0,"call_gex_1pct":14068.782801742265,"put_gex_1pct":-23741.58233787337,"net_gex_1pct":-9672.799536131104,"gross_gex_1pct":37810.365139615635,"call_oi":51,"put_oi":1},{"strike":44450.0,"call_gex_1pct":4914.079801472657,"put_gex_1pct":-70748.51673807319,"net_gex_1pct":-65834.43693660053,"gross_gex_1pct":75662.59653954585,"call_oi":18,"put_oi":3},{"strike":44500.0,"call_gex_1pct":30802.765645937805,"put_gex_1pct":0.0,"net_gex_1pct":30802.765645937805,"gross_gex_1pct":30802.765645937805,"call_oi":114,"put_oi":0},{"strike":44550.0,"call_gex_1pct":1604.6586687820336,"put_gex_1pct":0.0,"net_gex_1pct":1604.6586687820336,"gross_gex_1pct":1604.6586687820336,"call_oi":6,"put_oi":0},{"strike":44600.0,"call_gex_1pct":2912.068901411441,"put_gex_1pct":-69356.26613823087,"net_gex_1pct":-66444.19723681943,"gross_gex_1pct":72268.33503964232,"call_oi":11,"put_oi":3},{"strike":44650.0,"call_gex_1pct":524.1397444349635,"put_gex_1pct":0.0,"net_gex_1pct":524.1397444349635,"gross_gex_1pct":524.1397444349635,"call_oi":2,"put_oi":0},{"strike":44700.0,"call_gex_1pct":2594.5104980347437,"put_gex_1pct":0.0,"net_gex_1pct":2594.5104980347437,"gross_gex_1pct":2594.5104980347437,"call_oi":10,"put_oi":0},{"strike":44750.0,"call_gex_1pct":1284.380159451089,"put_gex_1pct":0.0,"net_gex_1pct":1284.380159451089,"gross_gex_1pct":1284.380159451089,"call_oi":5,"put_oi":0},{"strike":44800.0,"call_gex_1pct":4323.84479524072,"put_gex_1pct":0.0,"net_gex_1pct":4323.84479524072,"gross_gex_1pct":4323.84479524072,"call_oi":17,"put_oi":0},{"strike":44850.0,"call_gex_1pct":1762.9738762947504,"put_gex_1pct":0.0,"net_gex_1pct":1762.9738762947504,"gross_gex_1pct":1762.9738762947504,"call_oi":7,"put_oi":0},{"strike":44900.0,"call_gex_1pct":1745.8271649227174,"put_gex_1pct":0.0,"net_gex_1pct":1745.8271649227174,"gross_gex_1pct":1745.8271649227174,"call_oi":7,"put_oi":0},{"strike":44950.0,"call_gex_1pct":1975.9543901559641,"put_gex_1pct":0.0,"net_gex_1pct":1975.9543901559641,"gross_gex_1pct":1975.9543901559641,"call_oi":8,"put_oi":0},{"strike":45000.0,"call_gex_1pct":224319.99644944884,"put_gex_1pct":0.0,"net_gex_1pct":224319.99644944884,"gross_gex_1pct":224319.99644944884,"call_oi":917,"put_oi":0},{"strike":45050.0,"call_gex_1pct":3876.662750709363,"put_gex_1pct":-21827.487370221064,"net_gex_1pct":-17950.824619511703,"gross_gex_1pct":25704.150120930426,"call_oi":16,"put_oi":1},{"strike":45100.0,"call_gex_1pct":3839.942572868169,"put_gex_1pct":0.0,"net_gex_1pct":3839.942572868169,"gross_gex_1pct":3839.942572868169,"call_oi":16,"put_oi":0},{"strike":45150.0,"call_gex_1pct":3566.068708256723,"put_gex_1pct":0.0,"net_gex_1pct":3566.068708256723,"gross_gex_1pct":3566.068708256723,"call_oi":15,"put_oi":0},{"strike":45200.0,"call_gex_1pct":4945.81777150755,"put_gex_1pct":0.0,"net_gex_1pct":4945.81777150755,"gross_gex_1pct":4945.81777150755,"call_oi":21,"put_oi":0},{"strike":45250.0,"call_gex_1pct":1399.9637283846314,"put_gex_1pct":-106488.72776468201,"net_gex_1pct":-105088.76403629739,"gross_gex_1pct":107888.69149306664,"call_oi":6,"put_oi":5},{"strike":45300.0,"call_gex_1pct":2080.562638747744,"put_gex_1pct":0.0,"net_gex_1pct":2080.562638747744,"gross_gex_1pct":2080.562638747744,"call_oi":9,"put_oi":0},{"strike":45350.0,"call_gex_1pct":916.2136498633373,"put_gex_1pct":0.0,"net_gex_1pct":916.2136498633373,"gross_gex_1pct":916.2136498633373,"call_oi":4,"put_oi":0},{"strike":45400.0,"call_gex_1pct":1134.8296547578248,"put_gex_1pct":0.0,"net_gex_1pct":1134.8296547578248,"gross_gex_1pct":1134.8296547578248,"call_oi":5,"put_oi":0},{"strike":45450.0,"call_gex_1pct":2474.0153509517813,"put_gex_1pct":0.0,"net_gex_1pct":2474.0153509517813,"gross_gex_1pct":2474.0153509517813,"call_oi":11,"put_oi":0},{"strike":45500.0,"call_gex_1pct":147773.68461031216,"put_gex_1pct":0.0,"net_gex_1pct":147773.68461031216,"gross_gex_1pct":147773.68461031216,"call_oi":663,"put_oi":0},{"strike":45550.0,"call_gex_1pct":8393.934731966787,"put_gex_1pct":0.0,"net_gex_1pct":8393.934731966787,"gross_gex_1pct":8393.934731966787,"call_oi":38,"put_oi":0},{"strike":45600.0,"call_gex_1pct":4597.523630247654,"put_gex_1pct":0.0,"net_gex_1pct":4597.523630247654,"gross_gex_1pct":4597.523630247654,"call_oi":21,"put_oi":0},{"strike":45700.0,"call_gex_1pct":6452.722555845024,"put_gex_1pct":0.0,"net_gex_1pct":6452.722555845024,"gross_gex_1pct":6452.722555845024,"call_oi":30,"put_oi":0},{"strike":45800.0,"call_gex_1pct":1056.8238393350218,"put_gex_1pct":0.0,"net_gex_1pct":1056.8238393350218,"gross_gex_1pct":1056.8238393350218,"call_oi":5,"put_oi":0},{"strike":45900.0,"call_gex_1pct":2077.4719142731633,"put_gex_1pct":0.0,"net_gex_1pct":2077.4719142731633,"gross_gex_1pct":2077.4719142731633,"call_oi":10,"put_oi":0},{"strike":46000.0,"call_gex_1pct":171964.7759019989,"put_gex_1pct":0.0,"net_gex_1pct":171964.7759019989,"gross_gex_1pct":171964.7759019989,"call_oi":842,"put_oi":0},{"strike":46100.0,"call_gex_1pct":1405.741334484177,"put_gex_1pct":0.0,"net_gex_1pct":1405.741334484177,"gross_gex_1pct":1405.741334484177,"call_oi":7,"put_oi":0},{"strike":46200.0,"call_gex_1pct":5925.082828627815,"put_gex_1pct":0.0,"net_gex_1pct":5925.082828627815,"gross_gex_1pct":5925.082828627815,"call_oi":30,"put_oi":0},{"strike":46300.0,"call_gex_1pct":3108.4432448688326,"put_gex_1pct":0.0,"net_gex_1pct":3108.4432448688326,"gross_gex_1pct":3108.4432448688326,"call_oi":16,"put_oi":0},{"strike":46400.0,"call_gex_1pct":573.4244641196346,"put_gex_1pct":0.0,"net_gex_1pct":573.4244641196346,"gross_gex_1pct":573.4244641196346,"call_oi":3,"put_oi":0},{"strike":46500.0,"call_gex_1pct":18432.894332733573,"put_gex_1pct":0.0,"net_gex_1pct":18432.894332733573,"gross_gex_1pct":18432.894332733573,"call_oi":98,"put_oi":0},{"strike":46600.0,"call_gex_1pct":3517.324007424362,"put_gex_1pct":0.0,"net_gex_1pct":3517.324007424362,"gross_gex_1pct":3517.324007424362,"call_oi":19,"put_oi":0},{"strike":46700.0,"call_gex_1pct":1822.3311404718247,"put_gex_1pct":0.0,"net_gex_1pct":1822.3311404718247,"gross_gex_1pct":1822.3311404718247,"call_oi":10,"put_oi":0},{"strike":46800.0,"call_gex_1pct":2870.723959580088,"put_gex_1pct":0.0,"net_gex_1pct":2870.723959580088,"gross_gex_1pct":2870.723959580088,"call_oi":16,"put_oi":0},{"strike":46900.0,"call_gex_1pct":706.7237849036319,"put_gex_1pct":0.0,"net_gex_1pct":706.7237849036319,"gross_gex_1pct":706.7237849036319,"call_oi":4,"put_oi":0},{"strike":47000.0,"call_gex_1pct":320009.1107023517,"put_gex_1pct":0.0,"net_gex_1pct":320009.1107023517,"gross_gex_1pct":320009.1107023517,"call_oi":1839,"put_oi":0},{"strike":47100.0,"call_gex_1pct":1028.4755184590645,"put_gex_1pct":0.0,"net_gex_1pct":1028.4755184590645,"gross_gex_1pct":1028.4755184590645,"call_oi":6,"put_oi":0},{"strike":47200.0,"call_gex_1pct":1013.2715668719762,"put_gex_1pct":0.0,"net_gex_1pct":1013.2715668719762,"gross_gex_1pct":1013.2715668719762,"call_oi":6,"put_oi":0},{"strike":47300.0,"call_gex_1pct":499.22486535989003,"put_gex_1pct":0.0,"net_gex_1pct":499.22486535989003,"gross_gex_1pct":499.22486535989003,"call_oi":3,"put_oi":0},{"strike":47400.0,"call_gex_1pct":655.9978684529394,"put_gex_1pct":0.0,"net_gex_1pct":655.9978684529394,"gross_gex_1pct":655.9978684529394,"call_oi":4,"put_oi":0},{"strike":47500.0,"call_gex_1pct":484.9500760690421,"put_gex_1pct":0.0,"net_gex_1pct":484.9500760690421,"gross_gex_1pct":484.9500760690421,"call_oi":3,"put_oi":0},{"strike":47600.0,"call_gex_1pct":318.71589833150784,"put_gex_1pct":0.0,"net_gex_1pct":318.71589833150784,"gross_gex_1pct":318.71589833150784,"call_oi":2,"put_oi":0},{"strike":47700.0,"call_gex_1pct":1571.2131085073186,"put_gex_1pct":0.0,"net_gex_1pct":1571.2131085073186,"gross_gex_1pct":1571.2131085073186,"call_oi":10,"put_oi":0},{"strike":47800.0,"call_gex_1pct":12395.06116809645,"put_gex_1pct":0.0,"net_gex_1pct":12395.06116809645,"gross_gex_1pct":12395.06116809645,"call_oi":80,"put_oi":0},{"strike":47900.0,"call_gex_1pct":1833.684507516537,"put_gex_1pct":0.0,"net_gex_1pct":1833.684507516537,"gross_gex_1pct":1833.684507516537,"call_oi":12,"put_oi":0},{"strike":48000.0,"call_gex_1pct":9646.460772736693,"put_gex_1pct":0.0,"net_gex_1pct":9646.460772736693,"gross_gex_1pct":9646.460772736693,"call_oi":64,"put_oi":0},{"strike":48100.0,"call_gex_1pct":297.3867242624387,"put_gex_1pct":0.0,"net_gex_1pct":297.3867242624387,"gross_gex_1pct":297.3867242624387,"call_oi":2,"put_oi":0},{"strike":48200.0,"call_gex_1pct":1026.954055528298,"put_gex_1pct":0.0,"net_gex_1pct":1026.954055528298,"gross_gex_1pct":1026.954055528298,"call_oi":7,"put_oi":0},{"strike":48300.0,"call_gex_1pct":868.6052121687129,"put_gex_1pct":0.0,"net_gex_1pct":868.6052121687129,"gross_gex_1pct":868.6052121687129,"call_oi":6,"put_oi":0},{"strike":48400.0,"call_gex_1pct":1000.099570984767,"put_gex_1pct":0.0,"net_gex_1pct":1000.099570984767,"gross_gex_1pct":1000.099570984767,"call_oi":7,"put_oi":0},{"strike":48500.0,"call_gex_1pct":1551.196250562234,"put_gex_1pct":0.0,"net_gex_1pct":1551.196250562234,"gross_gex_1pct":1551.196250562234,"call_oi":11,"put_oi":0},{"strike":48600.0,"call_gex_1pct":2227.2901419202644,"put_gex_1pct":0.0,"net_gex_1pct":2227.2901419202644,"gross_gex_1pct":2227.2901419202644,"call_oi":16,"put_oi":0},{"strike":48700.0,"call_gex_1pct":12781.313214202757,"put_gex_1pct":-29975.99811082325,"net_gex_1pct":-17194.684896620493,"gross_gex_1pct":42757.31132502601,"call_oi":93,"put_oi":2}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 35,300 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 前日同月份 Chain 不完整（primary_expiry_chain_empty） |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 39,412 | 41,625 | -2,213 | 29,110 | 25,701 | +3,409 | -5,622 | TAIFEX Proxy |
| 投信 | 8,814 | 120 | +8,694 | 0 | 0 | +0 | +8,694 | TAIFEX Proxy |
| 自營商 | 68,238 | 79,318 | -11,080 | 49,346 | 44,937 | +4,409 | -15,489 | TAIFEX Proxy |
| 三大法人合計 | 116,464 | 121,063 | -4,599 | 78,456 | 70,638 | +7,818 | -12,417 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 9.07 | 14.82 | -5.75 | 6.53 | 5.06 | +1.47 | -7.22 | TAIFEX Proxy |
| 投信 | 15.76 | 0.01 | +15.75 | 0.00 | 0.00 | +0 | +15.75 | TAIFEX Proxy |
| 自營商 | 19.44 | 25.85 | -6.41 | 13.42 | 10.48 | +2.95 | -9.36 | TAIFEX Proxy |
| 三大法人合計 | 44.27 | 40.67 | +3.59 | 19.95 | 15.53 | +4.42 | -0.83 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,521 | TAIFEX Proxy |
| 買權空方 OI | 18,614 | TAIFEX Proxy |
| 買權多空淨 OI | -4,093 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-20→2026-11-23) | +93 | TAIFEX Proxy snapshots (2026-11-20) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,642 | TAIFEX Proxy |
| 賣權空方 OI | 11,745 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,103 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-20→2026-11-23) | -511 | TAIFEX Proxy snapshots (2026-11-20) |
- 資料日期：買權 2026-11-23／賣權 2026-11-23 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +374 | 2026-11-20→2026-11-23 | TAIFEX Proxy snapshots (2026-11-20) |
| 買權前十大 | +93 | 2026-11-20→2026-11-23 | TAIFEX Proxy snapshots (2026-11-20) |
| 賣權前十大 | -511 | 2026-11-20→2026-11-23 | TAIFEX Proxy snapshots (2026-11-20) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-23；本次報告產製時間：2026-11-25 00:14:39；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 覆蓋：101 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (2)：options.chain_oi_change, options.wall_change

## 五、資料來源、時間與完整性

- 台股現貨、TAIFEX 期貨／選擇權以 T0 為基準；海外指數、匯率、ADR、原油、黃金與 Bitcoin 採各來源最新可得報價。各表格均列示實際資料日期；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- otc_breadth：`TPEx 歷史市場現況 highlight_result.php`
- otc_turnover：`TPEx 歷史市場現況 highlight_result.php`
- otc：`漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`
- institutional：`TWSE RWD BFI82U`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)`
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-23；估值 1243 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 148.4610%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：亞洲主要指數資料日期落後 T0 2026-11-23，已將舊行情排除並標示 unavailable；原始資料日期：日經225 2026-11-20
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；0 檔採最近有效收盤價。Blave 同 T0 交叉驗證 148.4610%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-24，非 T0 2026-11-23)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：選擇權 OI 前日變化 unavailable：reason=primary_expiry_chain_empty; 主力=202611W4; 本日/前日有效合約=540/0; 本日/前日合約識別數=540/0; 僅本日/僅前日有效合約=540/0; 本日/前日 OI 缺值或無效=0/0; 無效/重複識別=0/0
- TAIFEX 註記：前日快照主力月份無法確認（快照值：缺失）；選擇權比較仍僅按當日主力月份及共同合約判定
- TAIFEX 註記：選擇權 Call Wall／Put Wall／Max Pain 前日變化 unavailable：reason=previous_chain_incomplete; detail=primary_expiry_chain_empty
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -289.5 | -103,432 | -692 | +3,215 | -2,213 | +3,409 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -41.5 | +93,565 | +4,449 | +0 | +8,694 | +0 | 避險／對沖 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
| 自營商 | -190.0 | +1,318 | -1,214 | -1,501 | -11,080 | +4,409 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
