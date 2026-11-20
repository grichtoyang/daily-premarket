# DATA_REPORT_20261119

- 報告日期：`2026-11-20`
- T0 交易日期：`2026-11-19`
- 首次資料產出時間：`2026-11-20 15:21:28`
- 本次更新開始時間：`2026-11-20 15:21:28`
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
| 加權指數 | 38,426.89 | 點 | twse-proxy |
| 開盤 | 40,145.73 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 40,315.53 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 38,259.70 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 38,426.89 | 點 | twse-proxy |
| 漲跌點數 | -1,768.02 | 點 | twse-proxy |
| 漲跌幅 | -4.40 | % | twse-proxy |
| 成交金額 | 9,429.9 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 67 | twse-proxy |
| 下跌家數 | 993 | twse-proxy |
| 平盤家數 | 25 | twse-proxy |
| 漲停家數 | 1 | twse-proxy |
| 跌停家數 | 128 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 51 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 807 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 18 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 2 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 156 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -243.1 | 億元 | TWSE RWD BFI82U |
| 投信 | +43.9 | 億元 | TWSE RWD BFI82U |
| 自營商 | -233.0 | 億元 | TWSE RWD BFI82U |
| 三大法人合計 | -432.3 | 億元 | TWSE RWD BFI82U |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-19；估值 1243 檔；2 檔採最近有效收盤價（價格日期 20261111 至 20261119）；Blave 同 T0 交叉驗證 147.9030%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 6,317.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -334.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 238,338 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | 15,050 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 147.93 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-19；估值 1243 檔；2 檔採最近有效收盤價（價格日期 20261111 至 20261119）；Blave 同 T0 交叉驗證 147.9030%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 33,906,767 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,481,033.42 | 2,162,786.315 | 20,643,819.735 | 張 |
| 借券賣出增減 | +65,637.003 | -2,879.617 | +62,757.386 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261119`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-20T15:21:44+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261119`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-20T15:21:44+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,429.9 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,330.1 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 10,760.0 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,175.83 | -147.80 | -2.02 | 2026-11-19 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,879.20 | -550.68 | -2.25 | 2026-11-19 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,517.05 | -599.21 | -2.21 | 2026-11-19 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 49,097.06 | -1,101.11 | -2.19 | 2026-11-19 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,419.72 | -233.08 | -2.41 | 2026-11-19 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 28.44 | 3.88 | +15.80 | 2026-11-19 | 2026-11-20T07:21:44+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 56,436.65 | -3,007.56 | -5.06 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,869.96 | -267.93 | -5.21 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,342.69 | -498.93 | -2.18 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,533.79 | -43.82 | -1.22 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,256.39 | -326.81 | -3.09 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,160.50 | -36.75 | -0.51 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,332.25 | -268.00 | -1.01 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 49,075.00 | -105.00 | -0.21 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,653.00 | -10.30 | -0.39 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | -0.04 | 19-NOV-26 | 2026-11-20T07:22:02+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.05 | -0.01 | 2026-11-19 | 2026-11-20T07:22:02+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.43 | -0.01 | 19-NOV-26 | 2026-11-20T07:22:21+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.40 | -0.01 | 2026-11-19 | 2026-11-20T07:22:21+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.95 | 0.02 | +0.07 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.74 | -0.16 | -0.15 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.16 | -0.22 | -0.14 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,334.60 | 4.20 | +0.32 | 2026-11-20 | 2026-11-20T07:21:44+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 352.09 | -10.53 | -2.90 | 2026-11-19 | 2026-11-20T07:21:45+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.40 | -0.56 | -4.01 | 2026-11-19 | 2026-11-20T07:21:45+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 30.49 | -2.03 | -6.24 | 2026-11-19 | 2026-11-20T07:21:45+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 83.11 | -0.10 | -0.12 | 2026-11-20 | 2026-11-20T07:21:45+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,553.10 | -132.40 | -3.59 | 2026-11-20 | 2026-11-20T07:21:45+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 61,824.03 | -77.79 | -0.13 | 2026-11-20 | 2026-11-20T07:21:45+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：散戶搶 台積零股交易額增1.6倍、0050翻倍
  - 來源：Yahoo 台股；發布時間：2026-11-20T06:47:47Z；台北時間：2026-11-20 14:47
  - 摘要：台股今天（20日）遭遇沉重賣壓，晶圓代工廠台積電股價開低走低，盤中一度跌破2000元關卡，滑落至1970元，創下七個多月來新低，終場收在2000元，下跌100元，散戶依然勇於搶進，盤中零股交易金額達到新台幣241.15億元，高居台股之冠。此
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E9%80%BE%E4%B8%83%E5%80%8B%E6%9C%88%E6%96%B0%E4%BD%8E%E5%83%B9-%E6%95%A3%E6%88%B6%E6%90%B6%E9%80%B2-%E7%9B%A4%E4%B8%AD%E9%9B%B6%E8%82%A1%E4%BA%A4%E6%98%93%E8%A1%9D241%E5%84%84%E5%B1%85%E5%8F%B0%E8%82%A1%E4%B9%8B%E5%86%A0-071023320.html
- 事件2：超過300檔收跌停 投顧董看築底跡象、下周拚報復性反彈
  - 來源：Yahoo 台股；發布時間：2026-11-20T06:37:50Z；台北時間：2026-11-20 14:37
  - 摘要：台股今（20）日盤中一度狂瀉2,688.21點、跌破3萬6千點，終場重挫2,393.6點、收在36,033.29點，創近7個月新低，亦寫下史上第三大收盤跌點。不少投資人追問「國安基金在哪裡？」富邦投顧董事長陳奕光接受《Yahoo股市》採訪時
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%8C%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E5%9C%A8%E5%93%AA%E8%A3%A1%EF%BC%9F%E3%80%8D%E5%8F%B0%E8%82%A1%E6%94%B6%E7%9B%A4%E6%9A%B4%E8%B7%8C2393%E9%BB%9E-%E9%99%B3%E5%A5%95%E5%85%89%EF%BC%9A%E6%AD%A4%E6%99%82%E9%87%8D%E6%8A%BC%E6%9C%AA%E5%BF%85%E7%90%86%E6%83%B3-063750331.html
- 事件3：主動式ETF套牢還要繼續定期定額？專家獻策
  - 來源：Yahoo 台股；發布時間：2026-11-19T22:29:00Z；台北時間：2026-11-20 06:29
  - 摘要：愈跌愈買，是不少投資人奉行的ETF投資策略，但這套方法也適用於主動式ETF嗎？財經名師朱岳中認為，主動式ETF與被動式ETF、傳統共同基金的操作特性不同，尤其每日揭露持股的機制，讓經理人的投資策略攤在陽光下，並不適合長期持有。而眼下輝達風波
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%82%A1%E7%81%BD%E5%A4%A7%E8%80%83%E9%A9%972-%E4%B8%BB%E5%8B%95%E5%BC%8Fetf%E5%A5%97%E7%89%A2%E9%82%84%E8%A6%81%E7%B9%BC%E7%BA%8C%E5%AE%9A%E6%9C%9F%E5%AE%9A%E9%A1%8D-%E6%9C%B1%E5%B2%B3%E4%B8%AD%E6%90%96%E9%A0%AD%E6%8F%AD%E5%8A%A0%E7%A2%BC%E7%AD%96%E7%95%A5-222900446.html
- 事件4：集中市場周摔7641點 上櫃指數高點回檔近四成
  - 來源：Yahoo 台股；發布時間：2026-11-20T06:37:12Z；台北時間：2026-11-20 14:37
  - 摘要：（中央社記者曾仁凱台北2026年11月20日電）AI利空頻傳，投資人信心潰堤，台股今天盤中重挫2688.21點，下探35738.68點；尾盤護盤基金進場拉抬，終場指數下跌2393.6點或6.23%，收在36033.29點，創下近7個月新低，
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%9B%A4%E5%BE%8C%E7%84%A6%E9%BB%9E-%E5%8F%B0%E8%82%A1%E5%86%8D%E5%B4%A92393%E9%BB%9E%E5%89%B5%E8%BF%917%E6%9C%88%E6%96%B0%E4%BD%8E-%E6%9C%AC%E9%80%B1%E9%87%8D%E6%8C%AB7641%E9%BB%9E-063712992.html
- 事件5：國安基金護尾盤？台積電最後一單強拉15元
  - 來源：Yahoo 台股；發布時間：2026-11-20T05:38:07Z；台北時間：2026-11-20 13:38
  - 摘要：受美國晶片管制升級消息衝擊，權值王台積電（2330）今（20）日最後一盤湧現破萬張買單，股價急拉15元，終場收在2,000元整，跌幅收斂，單日下跌100元、跌幅4.76％，分析師表示，有可能是國安基金拉的。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%AE%89%E5%9F%BA%E9%87%91%E5%8F%AA%E8%AD%B7%E5%B0%BE%E7%9B%A4%EF%BC%9F%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%9C%80%E5%BE%8C%E4%B8%80%E5%96%AE%E7%A0%B4%E8%90%AC%E5%BC%B5%E8%B2%B7%E5%96%AE-%E5%BC%B7%E6%8B%8915%E5%85%83%E9%9A%AA%E5%AE%882000%E5%85%83-054659397.html
- 事件6：台股融資斷頭潮 追繳金額逼近30億520戶強制平倉
  - 來源：Yahoo 台股；發布時間：2026-11-20T05:56:57Z；台北時間：2026-11-20 13:56
  - 摘要：台股19日出現恐慌性賣盤，大盤暴跌1768點、跌幅逾6%，全市場融資擔保維持率降至156.18%，創統計以來新低。當日2947戶收到追繳保證金通知，涉及29.64億元，另有520戶遭強制平倉，金額達9.18億元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%9E%8D%E8%B3%87%E6%96%B7%E9%A0%AD%E6%BD%AE%E4%BE%86%E8%A5%B2-%E8%BF%BD%E7%B9%B3%E9%87%91%E9%A1%8D%E8%BF%9130%E5%84%84-%E6%96%B7%E9%A0%AD%E9%87%91%E9%A1%8D9-18%E5%84%84-055657073.html
- 事件7：Federal Reserve Board issues enforcement action with former employee of First Security Bancorp
  - 來源：Federal Reserve；發布時間：Thu, 19 Nov 2026 16:00:00 GMT；台北時間：2026-11-20 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of First Security Bancorp
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261119a.htm
- 事件8：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 來源：Federal Reserve；發布時間：Wed, 18 Nov 2026 19:00:00 GMT；台北時間：2026-11-19 03:00
  - 摘要：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm
- 事件9：Japan core inflation soars to highest this year as energy subsidy expiry pushes up consumer prices
  - 來源：CNBC；發布時間：Fri, 20 Nov 2026 01:49:03 GMT；台北時間：2026-11-20 09:49
  - 摘要：The core inflation figure — which strips out prices of food — was lower than the 2.3% expected by Reuters-polled economists.
  - 原文連結：https://www.cnbc.com/2026/11/20/japan-inflation-cpi-october.html
- 事件10：Trump bought Nvidia, Palantir, SpaceX in September as federal deals, White House ties grew
  - 來源：CNBC；發布時間：Thu, 19 Nov 2026 19:43:08 GMT；台北時間：2026-11-20 03:43
  - 摘要：President Trump disclosed purchases of Nvidia stock, SpaceX debt and Tesla shares in September, alongside millions of dollars in other investments.
  - 原文連結：https://www.cnbc.com/2026/11/19/trump-nvidia-spacex-palantir-stock-trades-september.html
- 事件11：Inside India newsletter: Foreign flows helped the market recover. Now it faces the inflation test
  - 來源：CNBC；發布時間：Thu, 19 Nov 2026 00:01:23 GMT；台北時間：2026-11-19 08:01
  - 摘要：India’s inflation, which has been on the rise for 12 straight months, is becoming a risk to growth and to the reversal of foreign inflows.
  - 原文連結：https://www.cnbc.com/2026/11/19/india-inflation-foreign-investor-nifty50.html
- 事件12：SoftBank plunges over 16% as AI sell-off hits Asian tech stocks following Anthropic debut
  - 來源：CNBC；發布時間：Fri, 20 Nov 2026 03:30:34 GMT；台北時間：2026-11-20 11:30
  - 摘要：The declines in Asia come after the tech-heavy Nasdaq Composite fell more than 2% overnight following Anthropic's highly anticipated Wall Street debut
  - 原文連結：https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-19

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 37,550 | 點 | TAIFEX Proxy |
| 最高價 | 37,673 | 點 | TAIFEX Proxy |
| 最低價 | 35,563 | 點 | TAIFEX Proxy |
| 收盤價 | 35,875 | 點 | TAIFEX Proxy |
| 漲跌點數 | -2,732 | 點 | TAIFEX Proxy |
| 漲跌幅 | -7.08 | % | TAIFEX Proxy |
| 成交量 | 109,453 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 37,673 / 35,563 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 39,200 | 點 | TAIFEX Proxy |
| 最高價 | 39,765 | 點 | TAIFEX Proxy |
| 最低價 | 37,931 | 點 | TAIFEX Proxy |
| 收盤價 | 38,107 | 點 | TAIFEX Proxy |
| 漲跌點數 | -500 | 點 | TAIFEX Proxy |
| 漲跌幅 | -1.30 | % | TAIFEX Proxy |
| 成交量 | 74,153 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 39,765 / 37,931 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,664 | TAIFEX Proxy |
| 外資空方 OI | 111,883 | TAIFEX Proxy |
| 外資多空淨 OI | -99,219 | TAIFEX Proxy |
| 投信多方 OI | 95,246 | TAIFEX Proxy |
| 投信空方 OI | 3,455 | TAIFEX Proxy |
| 投信多空淨 OI | +91,791 | TAIFEX Proxy |
| 自營商多方 OI | 3,102 | TAIFEX Proxy |
| 自營商空方 OI | 4,557 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,455 | TAIFEX Proxy |
| 三大法人合計多方 OI | 111,012 | TAIFEX Proxy |
| 三大法人合計空方 OI | 119,895 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -8,883 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +219 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -1,782 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +2 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,642 | TAIFEX Proxy |
| 前十大交易人空方 OI | 95,571 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,071 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 換月基準重建 |
- 資料日期：2026-11-19 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 118,873 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 117,563 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,310 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 48,306 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 45,649 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,657 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,347 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -4,192 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -4,192 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,723 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -366 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +2,089 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,159 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +2,291 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -73.5 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +179.3 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 35,875 | TAIFEX Proxy |
| 加權指數價格 | 38,426.89 | twse-proxy |
| 台指期與加權指數價差 | -2,551.89 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | -6.64 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | -2,551.89 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +2,232 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 35,875 | 38,107 | -2,232 | TAIFEX Proxy |
| 成交量 | 109,453 | 74,153 | +35,300 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,561（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 118,873 | 117,563 | +1,310 | 48,306 | 45,649 | +2,657 | -1,347 | 12,664 | 111,883 | -99,219 | +219 | TAIFEX Proxy |
| 投信 | 60 | 4,252 | -4,192 | 0 | 0 | +0 | -4,192 | 95,246 | 3,455 | +91,791 | -1,782 | TAIFEX Proxy |
| 自營商 | 11,645 | 9,922 | +1,723 | 1,746 | 2,112 | -366 | +2,089 | 3,102 | 4,557 | -1,455 | +2 | TAIFEX Proxy |
| 三大法人合計 | 130,578 | 131,737 | -1,159 | 50,052 | 47,761 | +2,291 | -3,450 | 111,012 | 119,895 | -8,883 | -1,561 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,642 | TAIFEX Proxy |
| 前十大交易人空方 OI | 95,571 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,071 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 換月基準重建 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 40.39% | TAIFEX Proxy |
| 夜盤漲跌點數 | -500 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,657 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-19 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F3 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-20 15:21:28 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 216,126 | TAIFEX Proxy |
| Call 總未平倉量 OI | 83,887 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-18→2026-11-19) | +38,821 | TAIFEX Proxy snapshot bundle (2026-11-18→2026-11-19) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 162,246 | TAIFEX Proxy |
| Put 總未平倉量 OI | 31,249 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-18→2026-11-19) | +18,144 | TAIFEX Proxy snapshot bundle (2026-11-18→2026-11-19) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.33 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.68 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.37 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-18→2026-11-19) | -18.59 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-18→2026-11-19) | 1.20 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 130,405 | TAIFEX Proxy |
| 外資 Call日賣 | 119,895 | TAIFEX Proxy |
| 外資 Call日淨 | +10,510 | TAIFEX Proxy |
| 外資 Put日買 | 112,478 | TAIFEX Proxy |
| 外資 Put日賣 | 111,724 | TAIFEX Proxy |
| 外資 Put日淨 | +754 | TAIFEX Proxy |
| 外資 Call夜買 | 41,965 | TAIFEX Proxy |
| 外資 Call夜賣 | 42,801 | TAIFEX Proxy |
| 外資 Call夜淨 | -836 | TAIFEX Proxy |
| 外資 Put夜買 | 45,532 | TAIFEX Proxy |
| 外資 Put夜賣 | 45,767 | TAIFEX Proxy |
| 外資 Put夜淨 | -235 | TAIFEX Proxy |
| 外資 日盤淨總量 | +9,756 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +11,346 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +989 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 88,783 | TAIFEX Proxy |
| 自營商 Call日賣 | 111,101 | TAIFEX Proxy |
| 自營商 Call日淨 | -22,318 | TAIFEX Proxy |
| 自營商 Put日買 | 73,633 | TAIFEX Proxy |
| 自營商 Put日賣 | 86,022 | TAIFEX Proxy |
| 自營商 Put日淨 | -12,389 | TAIFEX Proxy |
| 自營商 Call夜買 | 18,408 | TAIFEX Proxy |
| 自營商 Call夜賣 | 22,271 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,863 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,293 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,619 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,326 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -9,929 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -18,455 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -10,063 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 45,000 | 6,670 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 4,387 | TAIFEX Proxy |
| Call OI 第3大履約價 | 42,000 | 4,135 | TAIFEX Proxy |
| Call OI 最大履約價 | 45,000 | 6,670 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 45,000 | 6,670 | 7.95% | TAIFEX Proxy |
| C2 | 43,000 | 4,387 | 5.23% | TAIFEX Proxy |
| C3 | 42,000 | 4,135 | 4.93% | TAIFEX Proxy |
| C4 | 41,000 | 3,326 | 3.96% | TAIFEX Proxy |
| C5 | 39,500 | 2,796 | 3.33% | TAIFEX Proxy |
| C6 | 39,000 | 2,558 | 3.05% | TAIFEX Proxy |
| C7 | 40,000 | 2,472 | 2.95% | TAIFEX Proxy |
| C8 | 42,800 | 2,350 | 2.8% | TAIFEX Proxy |
| C9 | 38,500 | 2,324 | 2.77% | TAIFEX Proxy |
| C10 | 39,100 | 2,137 | 2.55% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 35,700 | 3,728 | TAIFEX Proxy |
| Put OI 第2大履約價 | 37,000 | 2,283 | TAIFEX Proxy |
| Put OI 第3大履約價 | 38,000 | 1,455 | TAIFEX Proxy |
| Put OI 最大履約價 | 35,700 | 3,728 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 35,700 | 3,728 | 11.93% | TAIFEX Proxy |
| P2 | 37,000 | 2,283 | 7.31% | TAIFEX Proxy |
| P3 | 38,000 | 1,455 | 4.66% | TAIFEX Proxy |
| P4 | 39,500 | 1,057 | 3.38% | TAIFEX Proxy |
| P5 | 40,000 | 1,043 | 3.34% | TAIFEX Proxy |
| P6 | 36,000 | 985 | 3.15% | TAIFEX Proxy |
| P7 | 39,000 | 968 | 3.1% | TAIFEX Proxy |
| P8 | 38,500 | 959 | 3.07% | TAIFEX Proxy |
| P9 | 37,500 | 824 | 2.64% | TAIFEX Proxy |
| P10 | 36,500 | 728 | 2.33% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 42,000 (+3,369) | TAIFEX Proxy snapshot bundle (2026-11-18→2026-11-19) |
| Call OI 減少最多的履約價（共同合約） | 44,600 (-13) | TAIFEX Proxy snapshot bundle (2026-11-18→2026-11-19) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 35,700 (+1,992) | TAIFEX Proxy snapshot bundle (2026-11-18→2026-11-19) |
| Put OI 減少最多的履約價（共同合約） | 38,800 (-19) | TAIFEX Proxy snapshot bundle (2026-11-18→2026-11-19) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-18→2026-11-19) | +0 | TAIFEX Proxy snapshots (2026-11-18) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 35,700 | TAIFEX Proxy |
| 對應到期月份 | 202611F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-18→2026-11-19) | +0 | TAIFEX Proxy snapshots (2026-11-18) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 38,700.00 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F3 | TAIFEX Proxy |
| 資料日期 | 2026-11-19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,464.63 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F3 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 15,920 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 0 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 3,819 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 0 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-19 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：34,584.20～42,269.58
- 搜尋步長／計算次數：10.00／770
- 起點／終點 Net GEX：25,681,386.31／923,465,502.59
- 搜尋區間最低／最高 Net GEX：25,681,386.31／923,465,502.59
- 正負號交叉次數：0
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-19","chain_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":0},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":218,"delta_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":0,"delta_rows":204},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":572},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":432},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":246,"delta_rows":276},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":294},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":294}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-19","source":"taifex_web","fallback_used":false,"index_duration_ms":3193,"index_error":null,"openapi_fetch_duration_ms":11,"attempts":[{"attempt":1,"duration_ms":791,"source":"taifex_web","fallback":false,"http_status":502,"raw_rows":0,"primary_error":"TAIFEX primary HTTP 200 / rows 0","parser":{"input_rows":0,"array_rows":0,"object_rows":0,"short_rows":0,"non_txo_rows":0,"txo_rows":0,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":0,"per_expiry":[]},"accepted_txo_rows":0},{"attempt":2,"duration_ms":5775,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3237,"primary_error":null,"parser":{"input_rows":3237,"array_rows":3237,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3232,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3232,"per_expiry":[{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]},"accepted_txo_rows":3232}],"parser":{"input_rows":3237,"array_rows":3237,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3232,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3232,"per_expiry":[{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]},"final_rows":3232,"per_expiry_rows":[{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：32,662.86～44,190.92
- 搜尋步長／計算次數：10.00／1154
- 起點／終點 Net GEX：-24,108,730.86／1,105,094,326.97
- 搜尋區間最低／最高 Net GEX：-24,142,169.27／1,105,094,326.97
- 正負號交叉次數：1
- 擴大區間診斷 Flip：34,097.58

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 2,412,597,917.00 NT$ | 沿用前版（原來源：TAIFEX Gamma model；NT$／標的變動 1%） |
| Gross GEX（標的變動 1%） | 9,714,546,932.77 NT$ | 沿用前版（原來源：TAIFEX Gamma model；NT$／標的變動 1%） |
| 模型品質 | usable | 沿用前版（原來源：Black-Scholes Gamma using TAIFEX settlement-implied volatility） |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 沿用前版（原來源：模型限制；非 TAIFEX 公布的 Dealer 部位） |
| 履約價資料筆數 | 201 | 沿用前版（原來源：資料日期：2026-11-19） |
| 正 Net GEX 最大履約價 | 38,700 | 沿用前版（原來源：依 Net GEX 排序） |
| 負 Net GEX 最低履約價 | 37,000 | 沿用前版（原來源：依 Net GEX 排序） |
- GEX 明細 unavailable；不以 Wall／Flip proxy 代替。

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 38,900 | TAIFEX Proxy |
| 對應到期月份 | 202611F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-18→2026-11-19) | +100 | TAIFEX Proxy snapshots (2026-11-18) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 242,129 | 232,373 | +9,756 | 87,732 | 88,333 | -601 | +10,357 | TAIFEX Proxy |
| 投信 | 280 | 23,730 | -23,450 | 0 | 0 | +0 | -23,450 | TAIFEX Proxy |
| 自營商 | 174,805 | 184,734 | -9,929 | 39,027 | 40,564 | -1,537 | -8,392 | TAIFEX Proxy |
| 三大法人合計 | 417,214 | 440,837 | -23,623 | 126,759 | 128,897 | -2,138 | -21,485 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 29.72 | 20.17 | +9.54 | 8.81 | 8.89 | -0.09 | +9.63 | TAIFEX Proxy |
| 投信 | 0.02 | 15.04 | -15.02 | 0.00 | 0.00 | +0 | -15.02 | TAIFEX Proxy |
| 自營商 | 26.94 | 25.21 | +1.73 | 5.92 | 5.81 | +0.11 | +1.62 | TAIFEX Proxy |
| 三大法人合計 | 56.68 | 60.42 | -3.74 | 14.73 | 14.70 | +0.02 | -3.76 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,296 | TAIFEX Proxy |
| 買權空方 OI | 15,231 | TAIFEX Proxy |
| 買權多空淨 OI | -2,935 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | 換月基準重建 |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,459 | TAIFEX Proxy |
| 賣權空方 OI | 10,621 | TAIFEX Proxy |
| 賣權多空淨 OI | -162 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | 換月基準重建 |
- 資料日期：買權 2026-11-19／賣權 2026-11-19 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | unavailable | — | 換月基準重建 |
| 買權前十大 | unavailable | — | 換月基準重建 |
| 賣權前十大 | unavailable | — | 換月基準重建 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-19；本次報告產製時間：2026-11-20 15:21:28；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 換月註記：期貨前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減；買權前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減；賣權前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 保護：8 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：203 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (2)：futures.top10_change, options.top10_change

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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-19；估值 1243 檔；2 檔採最近有效收盤價（價格日期 20261111 至 20261119）；Blave 同 T0 交叉驗證 147.9030%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；2 檔採最近有效收盤價（價格日期 20261111 至 20261119）。Blave 同 T0 交叉驗證 147.9030%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-20，非 T0 2026-11-19)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：GEX Worker 診斷：code=TXO_DELTA_FETCH_FAILED；stage=delta_fetch；HTTP=502；TAIFEX Daily Delta not found；TAIFEX historical Delta file could not be parsed (last HTTP 502)
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma 原始端點不可用（上游 502）；已由 options-market-structure-compact (proxy) 備援取得（Wall 有值；Flip 有值）
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611W4（到期日 2026-11-25）與 Options Key Levels 主到期月份 202611F3 不同；GEX 數值應以實際使用到期月份為準
- TAIFEX 註記：逐履約價 GEX／Net GEX／Gross GEX 未取得或資料不完整，標 unavailable（不以 Wall/Flip proxy 代替）
- TAIFEX 註記：主力到期月份已由 202611 換至 202611F3；僅比較前後快照中相同主力月份的共同合約，不跨月份相減
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -243.1 | -99,219 | +1,310 | +2,657 | +9,756 | -601 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +43.9 | +91,791 | -4,192 | +0 | -23,450 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -233.0 | -1,455 | +1,723 | -366 | -9,929 | -1,537 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
