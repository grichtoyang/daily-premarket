# DATA_REPORT_20261119

- 報告日期：`2026-11-20`
- T0 交易日期：`2026-11-19`
- 首次資料產出時間：`2026-11-20 15:52:36`
- 本次更新開始時間：`2026-11-20 15:52:36`
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
- TWSE TWT93U（上市）：資料日期：`20261119`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-20T15:52:57+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261119`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-20T15:52:58+08:00`；狀態：`available_after_schedule`

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
| S&P 500 | ^GSPC | 7,175.83 | -147.80 | -2.02 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,879.20 | -550.68 | -2.25 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,517.05 | -599.21 | -2.21 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 49,097.06 | -1,101.11 | -2.19 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,419.72 | -233.08 | -2.41 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 28.44 | 3.88 | +15.80 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 56,436.65 | -3,007.56 | -5.06 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,869.96 | -267.93 | -5.21 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,354.53 | -487.09 | -2.13 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,533.79 | -43.82 | -1.22 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,256.39 | -326.81 | -3.09 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,160.00 | -37.25 | -0.52 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,306.75 | -293.50 | -1.10 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 49,119.00 | -61.00 | -0.12 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,654.50 | -8.80 | -0.33 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | -0.04 | 19-NOV-26 | 2026-11-20T07:53:21+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.05 | -0.01 | 2026-11-19 | 2026-11-20T07:53:21+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.43 | -0.01 | 19-NOV-26 | 2026-11-20T07:53:40+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.40 | -0.01 | 2026-11-19 | 2026-11-20T07:53:40+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.95 | 0.02 | +0.06 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.72 | -0.18 | -0.17 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.20 | -0.18 | -0.11 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,333.59 | 3.19 | +0.24 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 352.09 | -10.53 | -2.90 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.40 | -0.56 | -4.01 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 30.49 | -2.03 | -6.24 | 2026-11-19 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 82.56 | -0.65 | -0.78 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,554.20 | -131.30 | -3.56 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 61,848.67 | -53.15 | -0.09 | 2026-11-20 | 2026-11-20T07:52:58+00:00 | UTC | Yahoo Finance Chart API |

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
- 事件12：SoftBank suffers worst day in over two years as AI sell-off hits Asian tech stocks
  - 來源：CNBC；發布時間：Fri, 20 Nov 2026 07:23:06 GMT；台北時間：2026-11-20 15:23
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
| 多空淨 OI 變化 (2026-11-18→2026-11-19) | -1,671 | TAIFEX Proxy snapshots (2026-11-18) |
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
| 前十大交易人多空淨 OI 變化 (2026-11-18→2026-11-19) | -1,671 | TAIFEX Proxy snapshots (2026-11-18) |

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
| 本次報告產製時間 | 2026-11-20 15:52:36 | 本機 |
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
| Gamma Wall 價位 | 38,700.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F3 | TAIFEX Proxy |
| 資料日期 | 2026-11-19 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 42,464.63 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F3 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 15,920 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 15,920 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 3,819 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 3,694 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-19 | TAIFEX Proxy (options-gamma-levels + options-market-structure-compact (proxy)) |
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
{"requested_date":"2026-11-19","source":"taifex_web","fallback_used":false,"index_duration_ms":1326,"index_error":null,"openapi_fetch_duration_ms":11,"attempts":[{"attempt":1,"duration_ms":543,"source":"taifex_web","fallback":false,"http_status":502,"raw_rows":0,"primary_error":"TAIFEX primary HTTP 200 / rows 0","parser":{"input_rows":0,"array_rows":0,"object_rows":0,"short_rows":0,"non_txo_rows":0,"txo_rows":0,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":0,"per_expiry":[]},"accepted_txo_rows":0},{"attempt":2,"duration_ms":4095,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3237,"primary_error":null,"parser":{"input_rows":3237,"array_rows":3237,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3232,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3232,"per_expiry":[{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]},"accepted_txo_rows":3232}],"parser":{"input_rows":3237,"array_rows":3237,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3232,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3232,"per_expiry":[{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]},"final_rows":3232,"per_expiry_rows":[{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]}
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
| Net GEX（標的變動 1%） | 532,446,991.50 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 1,227,961,919.81 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 195 | 資料日期：2026-11-19 |
| 正 Net GEX 最大履約價 | 38,700 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 39,500 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：38,700（209,630,782.74 NT$）、38,900（209,562,636.80 NT$）、39,100（206,387,554.62 NT$）、40,000（36,626,094.79 NT$）、42,000（12,427,622.53 NT$）
- 負 Net GEX Top 5：39,500（-67,231,907.62 NT$）、37,800（-63,762,287.28 NT$）、36,000（-34,697,784.19 NT$）、36,500（-19,980,674.09 NT$）、38,400（-9,149,164.09 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-19","underlying":38426.89,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":532446991.49909127,"gross_gex_1pct":1227961919.805821,"gamma_diagnostics":{"chain_rows":390,"delta_rows":452,"matched_strike_keys":390,"positive_oi_settlement_eligible":300,"invalid_oi":90,"invalid_settlement":0,"below_intrinsic":30,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":270},"formal_flip_diagnostics":{"search_lower_underlying":34584.201,"search_upper_underlying":42269.579000000005,"step":10,"evaluations":770,"start_net_gex_1pct":25681386.30962444,"end_net_gex_1pct":923465502.5879338,"min_net_gex_1pct":25681386.30962444,"max_net_gex_1pct":923465502.5879338,"zero_crossings":0,"found":false},"wide_range_flip":{"lower_underlying":34092.856499999994,"upper_underlying":34102.856499999994,"estimated_underlying":34097.58012357852,"lower_net_gex_1pct":-196394.2995805163,"upper_net_gex_1pct":219376.12817615573},"wide_range_flip_diagnostics":{"search_lower_underlying":32662.856499999998,"search_upper_underlying":44190.9235,"reference_underlying":38426.89,"step":10,"evaluations":1154,"start_net_gex_1pct":-24108730.85708739,"end_net_gex_1pct":1105094326.9691648,"min_net_gex_1pct":-24142169.269735206,"max_net_gex_1pct":1105094326.9691648,"zero_crossings":1,"found":true,"selected_crossing_distance":4329.309876421481},"expiry_selection_diagnostics":{"requested_date":"2026-11-19","chain_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":0},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":218,"delta_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":0,"delta_rows":204},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":572},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":432},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":246,"delta_rows":276},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":294},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":294}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":36000.0,"call_gex_1pct":0.0,"put_gex_1pct":-34697784.19132811,"net_gex_1pct":-34697784.19132811,"gross_gex_1pct":34697784.19132811,"call_oi":0,"put_oi":526},{"strike":36100.0,"call_gex_1pct":0.0,"put_gex_1pct":-2851553.523691007,"net_gex_1pct":-2851553.523691007,"gross_gex_1pct":2851553.523691007,"call_oi":0,"put_oi":42},{"strike":36200.0,"call_gex_1pct":0.0,"put_gex_1pct":-2170504.5524285124,"net_gex_1pct":-2170504.5524285124,"gross_gex_1pct":2170504.5524285124,"call_oi":0,"put_oi":31},{"strike":36300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1236618.5222683602,"net_gex_1pct":-1236618.5222683602,"gross_gex_1pct":1236618.5222683602,"call_oi":0,"put_oi":17},{"strike":36400.0,"call_gex_1pct":0.0,"put_gex_1pct":-3489424.9672819586,"net_gex_1pct":-3489424.9672819586,"gross_gex_1pct":3489424.9672819586,"call_oi":0,"put_oi":47},{"strike":36500.0,"call_gex_1pct":0.0,"put_gex_1pct":-19980674.09332511,"net_gex_1pct":-19980674.09332511,"gross_gex_1pct":19980674.09332511,"call_oi":0,"put_oi":261},{"strike":36600.0,"call_gex_1pct":0.0,"put_gex_1pct":-940172.082569505,"net_gex_1pct":-940172.082569505,"gross_gex_1pct":940172.082569505,"call_oi":0,"put_oi":12},{"strike":36700.0,"call_gex_1pct":0.0,"put_gex_1pct":-483096.01700334204,"net_gex_1pct":-483096.01700334204,"gross_gex_1pct":483096.01700334204,"call_oi":0,"put_oi":6},{"strike":36800.0,"call_gex_1pct":0.0,"put_gex_1pct":-247539.7463904172,"net_gex_1pct":-247539.7463904172,"gross_gex_1pct":247539.7463904172,"call_oi":0,"put_oi":3},{"strike":36900.0,"call_gex_1pct":0.0,"put_gex_1pct":-3054611.948702475,"net_gex_1pct":-3054611.948702475,"gross_gex_1pct":3054611.948702475,"call_oi":0,"put_oi":36},{"strike":37000.0,"call_gex_1pct":0.0,"put_gex_1pct":-7303211.538885635,"net_gex_1pct":-7303211.538885635,"gross_gex_1pct":7303211.538885635,"call_oi":0,"put_oi":84},{"strike":37100.0,"call_gex_1pct":0.0,"put_gex_1pct":-798697.8363953806,"net_gex_1pct":-798697.8363953806,"gross_gex_1pct":798697.8363953806,"call_oi":0,"put_oi":9},{"strike":37200.0,"call_gex_1pct":0.0,"put_gex_1pct":-552046.8303865566,"net_gex_1pct":-552046.8303865566,"gross_gex_1pct":552046.8303865566,"call_oi":0,"put_oi":6},{"strike":37300.0,"call_gex_1pct":0.0,"put_gex_1pct":-3099461.1206334215,"net_gex_1pct":-3099461.1206334215,"gross_gex_1pct":3099461.1206334215,"call_oi":0,"put_oi":33},{"strike":37400.0,"call_gex_1pct":0.0,"put_gex_1pct":-1251554.5623299764,"net_gex_1pct":-1251554.5623299764,"gross_gex_1pct":1251554.5623299764,"call_oi":0,"put_oi":13},{"strike":37500.0,"call_gex_1pct":0.0,"put_gex_1pct":-2501900.5734511553,"net_gex_1pct":-2501900.5734511553,"gross_gex_1pct":2501900.5734511553,"call_oi":0,"put_oi":26},{"strike":37600.0,"call_gex_1pct":0.0,"put_gex_1pct":-1798230.7642941657,"net_gex_1pct":-1798230.7642941657,"gross_gex_1pct":1798230.7642941657,"call_oi":0,"put_oi":18},{"strike":37700.0,"call_gex_1pct":0.0,"put_gex_1pct":-905919.2379107726,"net_gex_1pct":-905919.2379107726,"gross_gex_1pct":905919.2379107726,"call_oi":0,"put_oi":9},{"strike":37800.0,"call_gex_1pct":0.0,"put_gex_1pct":-63762287.28148112,"net_gex_1pct":-63762287.28148112,"gross_gex_1pct":63762287.28148112,"call_oi":0,"put_oi":615},{"strike":37900.0,"call_gex_1pct":0.0,"put_gex_1pct":-1751835.906461365,"net_gex_1pct":-1751835.906461365,"gross_gex_1pct":1751835.906461365,"call_oi":0,"put_oi":17},{"strike":38000.0,"call_gex_1pct":0.0,"put_gex_1pct":-7609504.967440497,"net_gex_1pct":-7609504.967440497,"gross_gex_1pct":7609504.967440497,"call_oi":0,"put_oi":72},{"strike":38100.0,"call_gex_1pct":0.0,"put_gex_1pct":-855573.9882347105,"net_gex_1pct":-855573.9882347105,"gross_gex_1pct":855573.9882347105,"call_oi":0,"put_oi":8},{"strike":38200.0,"call_gex_1pct":103596.11358155323,"put_gex_1pct":-3967498.401415931,"net_gex_1pct":-3863902.287834378,"gross_gex_1pct":4071094.514997484,"call_oi":1,"put_oi":37},{"strike":38300.0,"call_gex_1pct":105748.48681499824,"put_gex_1pct":-545079.185046894,"net_gex_1pct":-439330.6982318958,"gross_gex_1pct":650827.6718618922,"call_oi":1,"put_oi":5},{"strike":38400.0,"call_gex_1pct":318074.6835541907,"put_gex_1pct":-9467238.772490425,"net_gex_1pct":-9149164.088936234,"gross_gex_1pct":9785313.456044616,"call_oi":3,"put_oi":85},{"strike":38500.0,"call_gex_1pct":6590676.477992386,"put_gex_1pct":-5360137.543507355,"net_gex_1pct":1230538.9344850304,"gross_gex_1pct":11950814.021499742,"call_oi":62,"put_oi":48},{"strike":38600.0,"call_gex_1pct":1417586.9701836333,"put_gex_1pct":-2739111.6617136444,"net_gex_1pct":-1321524.6915300111,"gross_gex_1pct":4156698.6318972777,"call_oi":13,"put_oi":24},{"strike":38700.0,"call_gex_1pct":217754901.651812,"put_gex_1pct":-8124118.9073080765,"net_gex_1pct":209630782.74450392,"gross_gex_1pct":225879020.55912006,"call_oi":2001,"put_oi":71},{"strike":38800.0,"call_gex_1pct":4820674.943952711,"put_gex_1pct":-2840361.4154237355,"net_gex_1pct":1980313.5285289758,"gross_gex_1pct":7661036.359376447,"call_oi":45,"put_oi":25},{"strike":38900.0,"call_gex_1pct":216965864.7464811,"put_gex_1pct":-7403227.9481450785,"net_gex_1pct":209562636.798336,"gross_gex_1pct":224369092.69462618,"call_oi":2002,"put_oi":65},{"strike":38950.0,"call_gex_1pct":976557.4277560478,"put_gex_1pct":-462783.8030031922,"net_gex_1pct":513773.6247528556,"gross_gex_1pct":1439341.23075924,"call_oi":9,"put_oi":4},{"strike":39000.0,"call_gex_1pct":8582185.053709047,"put_gex_1pct":-14985010.251831684,"net_gex_1pct":-6402825.198122637,"gross_gex_1pct":23567195.305540733,"call_oi":79,"put_oi":130},{"strike":39050.0,"call_gex_1pct":1740167.098151752,"put_gex_1pct":-341244.290395175,"net_gex_1pct":1398922.8077565772,"gross_gex_1pct":2081411.388546927,"call_oi":16,"put_oi":3},{"strike":39100.0,"call_gex_1pct":219873865.5915802,"put_gex_1pct":-13486310.96937321,"net_gex_1pct":206387554.62220702,"gross_gex_1pct":233360176.5609534,"call_oi":2001,"put_oi":119},{"strike":39150.0,"call_gex_1pct":871969.857543794,"put_gex_1pct":0.0,"net_gex_1pct":871969.857543794,"gross_gex_1pct":871969.857543794,"call_oi":8,"put_oi":0},{"strike":39200.0,"call_gex_1pct":864975.6921974078,"put_gex_1pct":-3065889.9897895236,"net_gex_1pct":-2200914.2975921156,"gross_gex_1pct":3930865.6819869317,"call_oi":8,"put_oi":27},{"strike":39250.0,"call_gex_1pct":757561.8163329604,"put_gex_1pct":-228372.31179983602,"net_gex_1pct":529189.5045331244,"gross_gex_1pct":985934.1281327964,"call_oi":7,"put_oi":2},{"strike":39300.0,"call_gex_1pct":1725299.938238905,"put_gex_1pct":-676031.5207676045,"net_gex_1pct":1049268.4174713006,"gross_gex_1pct":2401331.4590065097,"call_oi":16,"put_oi":6},{"strike":39350.0,"call_gex_1pct":962636.9502634271,"put_gex_1pct":0.0,"net_gex_1pct":962636.9502634271,"gross_gex_1pct":962636.9502634271,"call_oi":9,"put_oi":0},{"strike":39400.0,"call_gex_1pct":3607273.3244108153,"put_gex_1pct":-1564715.9288595316,"net_gex_1pct":2042557.3955512836,"gross_gex_1pct":5171989.253270347,"call_oi":34,"put_oi":14},{"strike":39450.0,"call_gex_1pct":213243.31137661193,"put_gex_1pct":-330882.0687890051,"net_gex_1pct":-117638.75741239317,"gross_gex_1pct":544125.380165617,"call_oi":2,"put_oi":3},{"strike":39500.0,"call_gex_1pct":3278068.527410459,"put_gex_1pct":-70509976.14300856,"net_gex_1pct":-67231907.6155981,"gross_gex_1pct":73788044.67041902,"call_oi":31,"put_oi":642},{"strike":39550.0,"call_gex_1pct":419487.5522369852,"put_gex_1pct":-328050.7503650877,"net_gex_1pct":91436.80187189748,"gross_gex_1pct":747538.302602073,"call_oi":4,"put_oi":3},{"strike":39600.0,"call_gex_1pct":2097729.836182785,"put_gex_1pct":-2394847.243293225,"net_gex_1pct":-297117.4071104396,"gross_gex_1pct":4492577.07947601,"call_oi":20,"put_oi":22},{"strike":39650.0,"call_gex_1pct":832014.8937557536,"put_gex_1pct":-975109.0845222285,"net_gex_1pct":-143094.1907664748,"gross_gex_1pct":1807123.9782779822,"call_oi":8,"put_oi":9},{"strike":39700.0,"call_gex_1pct":1138997.5661986428,"put_gex_1pct":-3153453.613840606,"net_gex_1pct":-2014456.0476419632,"gross_gex_1pct":4292451.180039249,"call_oi":11,"put_oi":29},{"strike":39750.0,"call_gex_1pct":821217.9081930876,"put_gex_1pct":-643549.1316933353,"net_gex_1pct":177668.7764997523,"gross_gex_1pct":1464767.039886423,"call_oi":8,"put_oi":6},{"strike":39800.0,"call_gex_1pct":2543951.0233655656,"put_gex_1pct":-1481225.9274695364,"net_gex_1pct":1062725.0958960291,"gross_gex_1pct":4025176.9508351022,"call_oi":25,"put_oi":14},{"strike":39850.0,"call_gex_1pct":704368.7504407476,"put_gex_1pct":-526048.645880119,"net_gex_1pct":178320.10456062865,"gross_gex_1pct":1230417.3963208664,"call_oi":7,"put_oi":5},{"strike":39900.0,"call_gex_1pct":3103536.630903527,"put_gex_1pct":-726364.23215848,"net_gex_1pct":2377172.398745047,"gross_gex_1pct":3829900.8630620074,"call_oi":31,"put_oi":7},{"strike":39950.0,"call_gex_1pct":1387787.29597592,"put_gex_1pct":-1031268.3329368152,"net_gex_1pct":356518.9630391048,"gross_gex_1pct":2419055.6289127353,"call_oi":14,"put_oi":10},{"strike":40000.0,"call_gex_1pct":39473385.75506541,"put_gex_1pct":-2847290.9606224666,"net_gex_1pct":36626094.794442944,"gross_gex_1pct":42320676.71568788,"call_oi":404,"put_oi":28},{"strike":40050.0,"call_gex_1pct":1256557.5407869031,"put_gex_1pct":-1009889.8499633003,"net_gex_1pct":246667.69082360284,"gross_gex_1pct":2266447.3907502033,"call_oi":13,"put_oi":10},{"strike":40100.0,"call_gex_1pct":3656001.4248900777,"put_gex_1pct":-696837.0639720676,"net_gex_1pct":2959164.36091801,"gross_gex_1pct":4352838.488862146,"call_oi":38,"put_oi":7},{"strike":40150.0,"call_gex_1pct":1230084.5597730568,"put_gex_1pct":-588722.8259216269,"net_gex_1pct":641361.7338514299,"gross_gex_1pct":1818807.3856946835,"call_oi":13,"put_oi":6},{"strike":40200.0,"call_gex_1pct":4517506.429307998,"put_gex_1pct":-1849030.3936798787,"net_gex_1pct":2668476.0356281195,"gross_gex_1pct":6366536.822987877,"call_oi":48,"put_oi":19},{"strike":40250.0,"call_gex_1pct":838262.7529940663,"put_gex_1pct":-671105.8220832124,"net_gex_1pct":167156.9309108539,"gross_gex_1pct":1509368.5750772788,"call_oi":9,"put_oi":7},{"strike":40300.0,"call_gex_1pct":2670577.506876232,"put_gex_1pct":-379853.2392554591,"net_gex_1pct":2290724.267620773,"gross_gex_1pct":3050430.746131691,"call_oi":29,"put_oi":4},{"strike":40350.0,"call_gex_1pct":1000069.6697313129,"put_gex_1pct":-280462.11603532056,"net_gex_1pct":719607.5536959923,"gross_gex_1pct":1280531.7857666335,"call_oi":11,"put_oi":3},{"strike":40400.0,"call_gex_1pct":1884422.0750829438,"put_gex_1pct":-552075.1693072831,"net_gex_1pct":1332346.9057756606,"gross_gex_1pct":2436497.244390227,"call_oi":21,"put_oi":6},{"strike":40450.0,"call_gex_1pct":884986.468698454,"put_gex_1pct":-181072.45965417285,"net_gex_1pct":703914.0090442811,"gross_gex_1pct":1066058.9283526267,"call_oi":10,"put_oi":2},{"strike":40500.0,"call_gex_1pct":10680319.203337917,"put_gex_1pct":-2760729.0837438195,"net_gex_1pct":7919590.119594097,"gross_gex_1pct":13441048.287081737,"call_oi":122,"put_oi":31},{"strike":40550.0,"call_gex_1pct":86268.39943125538,"put_gex_1pct":0.0,"net_gex_1pct":86268.39943125538,"gross_gex_1pct":86268.39943125538,"call_oi":1,"put_oi":0},{"strike":40600.0,"call_gex_1pct":4151220.6854231125,"put_gex_1pct":-774635.8858486268,"net_gex_1pct":3376584.7995744855,"gross_gex_1pct":4925856.571271739,"call_oi":49,"put_oi":9},{"strike":40650.0,"call_gex_1pct":501926.7656679129,"put_gex_1pct":-338238.04395407374,"net_gex_1pct":163688.72171383916,"gross_gex_1pct":840164.8096219867,"call_oi":6,"put_oi":4},{"strike":40700.0,"call_gex_1pct":1150063.0987078655,"put_gex_1pct":-664249.3561470142,"net_gex_1pct":485813.7425608513,"gross_gex_1pct":1814312.4548548795,"call_oi":14,"put_oi":8},{"strike":40750.0,"call_gex_1pct":808117.252847788,"put_gex_1pct":-1222223.3775311147,"net_gex_1pct":-414106.1246833267,"gross_gex_1pct":2030340.630378903,"call_oi":10,"put_oi":15},{"strike":40800.0,"call_gex_1pct":4133483.216428369,"put_gex_1pct":-4075213.359222337,"net_gex_1pct":58269.85720603168,"gross_gex_1pct":8208696.575650706,"call_oi":52,"put_oi":51},{"strike":40850.0,"call_gex_1pct":1407765.3705124569,"put_gex_1pct":-1957495.8148622448,"net_gex_1pct":-549730.4443497879,"gross_gex_1pct":3365261.1853747014,"call_oi":18,"put_oi":25},{"strike":40900.0,"call_gex_1pct":1766974.8797340097,"put_gex_1pct":-2529675.9034813694,"net_gex_1pct":-762701.0237473596,"gross_gex_1pct":4296650.783215379,"call_oi":23,"put_oi":33},{"strike":40950.0,"call_gex_1pct":226264.79099299907,"put_gex_1pct":-74970.56613094594,"net_gex_1pct":151294.22486205312,"gross_gex_1pct":301235.357123945,"call_oi":3,"put_oi":1},{"strike":41000.0,"call_gex_1pct":10144821.109673437,"put_gex_1pct":-1464666.7600856146,"net_gex_1pct":8680154.349587822,"gross_gex_1pct":11609487.869759051,"call_oi":137,"put_oi":20},{"strike":41050.0,"call_gex_1pct":217994.04519168078,"put_gex_1pct":-71436.20502089894,"net_gex_1pct":146557.84017078183,"gross_gex_1pct":289430.25021257973,"call_oi":3,"put_oi":1},{"strike":41100.0,"call_gex_1pct":856333.9685682995,"put_gex_1pct":-280256.4217448738,"net_gex_1pct":576077.5468234257,"gross_gex_1pct":1136590.3903131734,"call_oi":12,"put_oi":4},{"strike":41150.0,"call_gex_1pct":769022.619491156,"put_gex_1pct":-477642.27289178176,"net_gex_1pct":291380.3465993742,"gross_gex_1pct":1246664.8923829377,"call_oi":11,"put_oi":7},{"strike":41200.0,"call_gex_1pct":1781834.586164144,"put_gex_1pct":-331613.1680686227,"net_gex_1pct":1450221.4180955214,"gross_gex_1pct":2113447.754232767,"call_oi":26,"put_oi":5},{"strike":41250.0,"call_gex_1pct":671485.8236725924,"put_gex_1pct":0.0,"net_gex_1pct":671485.8236725924,"gross_gex_1pct":671485.8236725924,"call_oi":10,"put_oi":0},{"strike":41300.0,"call_gex_1pct":854856.4891882987,"put_gex_1pct":-126201.34161670793,"net_gex_1pct":728655.1475715907,"gross_gex_1pct":981057.8308050067,"call_oi":13,"put_oi":2},{"strike":41350.0,"call_gex_1pct":193074.99395246882,"put_gex_1pct":0.0,"net_gex_1pct":193074.99395246882,"gross_gex_1pct":193074.99395246882,"call_oi":3,"put_oi":0},{"strike":41400.0,"call_gex_1pct":566515.5991273436,"put_gex_1pct":-117579.41236206681,"net_gex_1pct":448936.1867652768,"gross_gex_1pct":684095.0114894104,"call_oi":9,"put_oi":2},{"strike":41450.0,"call_gex_1pct":369424.13912335865,"put_gex_1pct":-288482.06161403016,"net_gex_1pct":80942.07750932849,"gross_gex_1pct":657906.2007373888,"call_oi":6,"put_oi":5},{"strike":41500.0,"call_gex_1pct":4462450.967935772,"put_gex_1pct":-387421.7378915869,"net_gex_1pct":4075029.2300441847,"gross_gex_1pct":4849872.705827358,"call_oi":74,"put_oi":7},{"strike":41550.0,"call_gex_1pct":58927.504833033134,"put_gex_1pct":-108659.0494142629,"net_gex_1pct":-49731.54458122977,"gross_gex_1pct":167586.55424729604,"call_oi":1,"put_oi":2},{"strike":41600.0,"call_gex_1pct":1781641.9798973529,"put_gex_1pct":-51818.329806463466,"net_gex_1pct":1729823.6500908893,"gross_gex_1pct":1833460.3097038164,"call_oi":31,"put_oi":1},{"strike":41650.0,"call_gex_1pct":112286.97804609776,"put_gex_1pct":-101754.30559445158,"net_gex_1pct":10532.672451646184,"gross_gex_1pct":214041.28364054934,"call_oi":2,"put_oi":2},{"strike":41700.0,"call_gex_1pct":762606.1331707871,"put_gex_1pct":-192635.2507556009,"net_gex_1pct":569970.8824151863,"gross_gex_1pct":955241.383926388,"call_oi":14,"put_oi":4},{"strike":41750.0,"call_gex_1pct":319775.99080999155,"put_gex_1pct":-141876.91447968356,"net_gex_1pct":177899.076330308,"gross_gex_1pct":461652.9052896751,"call_oi":6,"put_oi":3},{"strike":41800.0,"call_gex_1pct":881270.3760522401,"put_gex_1pct":-44302.38169205898,"net_gex_1pct":836967.9943601812,"gross_gex_1pct":925572.7577442991,"call_oi":17,"put_oi":1},{"strike":41850.0,"call_gex_1pct":606877.3906364527,"put_gex_1pct":-43511.208105935046,"net_gex_1pct":563366.1825305177,"gross_gex_1pct":650388.5987423877,"call_oi":12,"put_oi":1},{"strike":41900.0,"call_gex_1pct":891577.4526016037,"put_gex_1pct":-160620.80510573648,"net_gex_1pct":730956.6474958672,"gross_gex_1pct":1052198.2577073402,"call_oi":18,"put_oi":4},{"strike":41950.0,"call_gex_1pct":481625.57059160905,"put_gex_1pct":-39441.746288507355,"net_gex_1pct":442183.8243031017,"gross_gex_1pct":521067.3168801164,"call_oi":10,"put_oi":1},{"strike":42000.0,"call_gex_1pct":12747759.07130346,"put_gex_1pct":-320136.53811004653,"net_gex_1pct":12427622.533193415,"gross_gex_1pct":13067895.609413506,"call_oi":269,"put_oi":9},{"strike":42050.0,"call_gex_1pct":2517341.2730393894,"put_gex_1pct":-69879.96684714784,"net_gex_1pct":2447461.3061922416,"gross_gex_1pct":2587221.239886537,"call_oi":55,"put_oi":2},{"strike":42100.0,"call_gex_1pct":1322375.64995525,"put_gex_1pct":-102985.61487488463,"net_gex_1pct":1219390.0350803654,"gross_gex_1pct":1425361.2648301348,"call_oi":30,"put_oi":3},{"strike":42150.0,"call_gex_1pct":520588.27942833933,"put_gex_1pct":-148776.24072466177,"net_gex_1pct":371812.0387036776,"gross_gex_1pct":669364.5201530011,"call_oi":12,"put_oi":5},{"strike":42200.0,"call_gex_1pct":2147589.764371832,"put_gex_1pct":-116932.50047095404,"net_gex_1pct":2030657.263900878,"gross_gex_1pct":2264522.264842786,"call_oi":51,"put_oi":4},{"strike":42250.0,"call_gex_1pct":1516480.7495791838,"put_gex_1pct":-143633.52460087487,"net_gex_1pct":1372847.224978309,"gross_gex_1pct":1660114.2741800586,"call_oi":37,"put_oi":5},{"strike":42300.0,"call_gex_1pct":1366574.3552368765,"put_gex_1pct":-22955.318027070516,"net_gex_1pct":1343619.037209806,"gross_gex_1pct":1389529.673263947,"call_oi":34,"put_oi":1},{"strike":42350.0,"call_gex_1pct":1627126.1185970742,"put_gex_1pct":0.0,"net_gex_1pct":1627126.1185970742,"gross_gex_1pct":1627126.1185970742,"call_oi":42,"put_oi":0},{"strike":42400.0,"call_gex_1pct":2031295.7891404305,"put_gex_1pct":-22163.582705575176,"net_gex_1pct":2009132.2064348552,"gross_gex_1pct":2053459.3718460058,"call_oi":54,"put_oi":1},{"strike":42450.0,"call_gex_1pct":222287.38444930775,"put_gex_1pct":0.0,"net_gex_1pct":222287.38444930775,"gross_gex_1pct":222287.38444930775,"call_oi":6,"put_oi":0},{"strike":42500.0,"call_gex_1pct":2015193.2297400136,"put_gex_1pct":-67570.25966568939,"net_gex_1pct":1947622.9700743242,"gross_gex_1pct":2082763.489405703,"call_oi":57,"put_oi":5},{"strike":42550.0,"call_gex_1pct":619575.3213121671,"put_gex_1pct":-119489.28081788302,"net_gex_1pct":500086.04049428407,"gross_gex_1pct":739064.6021300501,"call_oi":18,"put_oi":9},{"strike":42600.0,"call_gex_1pct":793439.3904026522,"put_gex_1pct":-39138.334843400145,"net_gex_1pct":754301.055559252,"gross_gex_1pct":832577.7252460524,"call_oi":24,"put_oi":3},{"strike":42650.0,"call_gex_1pct":388205.4221169142,"put_gex_1pct":0.0,"net_gex_1pct":388205.4221169142,"gross_gex_1pct":388205.4221169142,"call_oi":12,"put_oi":0},{"strike":42700.0,"call_gex_1pct":939302.8881263798,"put_gex_1pct":0.0,"net_gex_1pct":939302.8881263798,"gross_gex_1pct":939302.8881263798,"call_oi":30,"put_oi":0},{"strike":42750.0,"call_gex_1pct":121055.41674630209,"put_gex_1pct":0.0,"net_gex_1pct":121055.41674630209,"gross_gex_1pct":121055.41674630209,"call_oi":4,"put_oi":0},{"strike":42800.0,"call_gex_1pct":955465.9734186754,"put_gex_1pct":0.0,"net_gex_1pct":955465.9734186754,"gross_gex_1pct":955465.9734186754,"call_oi":33,"put_oi":0},{"strike":42850.0,"call_gex_1pct":255664.87158437067,"put_gex_1pct":0.0,"net_gex_1pct":255664.87158437067,"gross_gex_1pct":255664.87158437067,"call_oi":9,"put_oi":0},{"strike":42900.0,"call_gex_1pct":219817.89814321804,"put_gex_1pct":0.0,"net_gex_1pct":219817.89814321804,"gross_gex_1pct":219817.89814321804,"call_oi":8,"put_oi":0},{"strike":42950.0,"call_gex_1pct":265442.10046543734,"put_gex_1pct":0.0,"net_gex_1pct":265442.10046543734,"gross_gex_1pct":265442.10046543734,"call_oi":10,"put_oi":0},{"strike":43000.0,"call_gex_1pct":6100757.034476466,"put_gex_1pct":0.0,"net_gex_1pct":6100757.034476466,"gross_gex_1pct":6100757.034476466,"call_oi":241,"put_oi":0},{"strike":43050.0,"call_gex_1pct":396980.86145634967,"put_gex_1pct":0.0,"net_gex_1pct":396980.86145634967,"gross_gex_1pct":396980.86145634967,"call_oi":16,"put_oi":0},{"strike":43100.0,"call_gex_1pct":384285.7906566621,"put_gex_1pct":0.0,"net_gex_1pct":384285.7906566621,"gross_gex_1pct":384285.7906566621,"call_oi":16,"put_oi":0},{"strike":43150.0,"call_gex_1pct":371602.16921172175,"put_gex_1pct":0.0,"net_gex_1pct":371602.16921172175,"gross_gex_1pct":371602.16921172175,"call_oi":16,"put_oi":0},{"strike":43200.0,"call_gex_1pct":663154.4114495722,"put_gex_1pct":0.0,"net_gex_1pct":663154.4114495722,"gross_gex_1pct":663154.4114495722,"call_oi":30,"put_oi":0},{"strike":43250.0,"call_gex_1pct":562570.9654102462,"put_gex_1pct":0.0,"net_gex_1pct":562570.9654102462,"gross_gex_1pct":562570.9654102462,"call_oi":26,"put_oi":0},{"strike":43300.0,"call_gex_1pct":735355.5230157992,"put_gex_1pct":0.0,"net_gex_1pct":735355.5230157992,"gross_gex_1pct":735355.5230157992,"call_oi":35,"put_oi":0},{"strike":43350.0,"call_gex_1pct":565994.4396272955,"put_gex_1pct":0.0,"net_gex_1pct":565994.4396272955,"gross_gex_1pct":565994.4396272955,"call_oi":28,"put_oi":0},{"strike":43400.0,"call_gex_1pct":450621.0922910835,"put_gex_1pct":0.0,"net_gex_1pct":450621.0922910835,"gross_gex_1pct":450621.0922910835,"call_oi":23,"put_oi":0},{"strike":43450.0,"call_gex_1pct":469758.4129393428,"put_gex_1pct":0.0,"net_gex_1pct":469758.4129393428,"gross_gex_1pct":469758.4129393428,"call_oi":25,"put_oi":0},{"strike":43500.0,"call_gex_1pct":1453628.481579645,"put_gex_1pct":0.0,"net_gex_1pct":1453628.481579645,"gross_gex_1pct":1453628.481579645,"call_oi":80,"put_oi":0},{"strike":43550.0,"call_gex_1pct":684527.7551451018,"put_gex_1pct":0.0,"net_gex_1pct":684527.7551451018,"gross_gex_1pct":684527.7551451018,"call_oi":39,"put_oi":0},{"strike":43600.0,"call_gex_1pct":669409.1469420916,"put_gex_1pct":0.0,"net_gex_1pct":669409.1469420916,"gross_gex_1pct":669409.1469420916,"call_oi":40,"put_oi":0},{"strike":43650.0,"call_gex_1pct":571096.5897025936,"put_gex_1pct":0.0,"net_gex_1pct":571096.5897025936,"gross_gex_1pct":571096.5897025936,"call_oi":35,"put_oi":0},{"strike":43700.0,"call_gex_1pct":675047.2208652901,"put_gex_1pct":0.0,"net_gex_1pct":675047.2208652901,"gross_gex_1pct":675047.2208652901,"call_oi":43,"put_oi":0},{"strike":43750.0,"call_gex_1pct":723778.476732417,"put_gex_1pct":0.0,"net_gex_1pct":723778.476732417,"gross_gex_1pct":723778.476732417,"call_oi":48,"put_oi":0},{"strike":43800.0,"call_gex_1pct":636056.4042481156,"put_gex_1pct":0.0,"net_gex_1pct":636056.4042481156,"gross_gex_1pct":636056.4042481156,"call_oi":44,"put_oi":0},{"strike":43850.0,"call_gex_1pct":562122.6863522887,"put_gex_1pct":0.0,"net_gex_1pct":562122.6863522887,"gross_gex_1pct":562122.6863522887,"call_oi":40,"put_oi":0},{"strike":43900.0,"call_gex_1pct":375987.60714262695,"put_gex_1pct":0.0,"net_gex_1pct":375987.60714262695,"gross_gex_1pct":375987.60714262695,"call_oi":28,"put_oi":0},{"strike":43950.0,"call_gex_1pct":260623.2636522379,"put_gex_1pct":0.0,"net_gex_1pct":260623.2636522379,"gross_gex_1pct":260623.2636522379,"call_oi":20,"put_oi":0},{"strike":44000.0,"call_gex_1pct":5084354.454261684,"put_gex_1pct":0.0,"net_gex_1pct":5084354.454261684,"gross_gex_1pct":5084354.454261684,"call_oi":410,"put_oi":0},{"strike":44050.0,"call_gex_1pct":11761.950696963839,"put_gex_1pct":0.0,"net_gex_1pct":11761.950696963839,"gross_gex_1pct":11761.950696963839,"call_oi":1,"put_oi":0},{"strike":44100.0,"call_gex_1pct":250096.36265590927,"put_gex_1pct":0.0,"net_gex_1pct":250096.36265590927,"gross_gex_1pct":250096.36265590927,"call_oi":22,"put_oi":0},{"strike":44150.0,"call_gex_1pct":96449.32261607288,"put_gex_1pct":0.0,"net_gex_1pct":96449.32261607288,"gross_gex_1pct":96449.32261607288,"call_oi":9,"put_oi":0},{"strike":44200.0,"call_gex_1pct":371877.5555537865,"put_gex_1pct":0.0,"net_gex_1pct":371877.5555537865,"gross_gex_1pct":371877.5555537865,"call_oi":37,"put_oi":0},{"strike":44250.0,"call_gex_1pct":57913.882878040764,"put_gex_1pct":0.0,"net_gex_1pct":57913.882878040764,"gross_gex_1pct":57913.882878040764,"call_oi":6,"put_oi":0},{"strike":44300.0,"call_gex_1pct":338131.03698186664,"put_gex_1pct":0.0,"net_gex_1pct":338131.03698186664,"gross_gex_1pct":338131.03698186664,"call_oi":37,"put_oi":0},{"strike":44350.0,"call_gex_1pct":121489.32617352749,"put_gex_1pct":0.0,"net_gex_1pct":121489.32617352749,"gross_gex_1pct":121489.32617352749,"call_oi":14,"put_oi":0},{"strike":44400.0,"call_gex_1pct":229944.51747609582,"put_gex_1pct":0.0,"net_gex_1pct":229944.51747609582,"gross_gex_1pct":229944.51747609582,"call_oi":28,"put_oi":0},{"strike":44450.0,"call_gex_1pct":116113.2756767558,"put_gex_1pct":0.0,"net_gex_1pct":116113.2756767558,"gross_gex_1pct":116113.2756767558,"call_oi":15,"put_oi":0},{"strike":44500.0,"call_gex_1pct":813396.8983562497,"put_gex_1pct":0.0,"net_gex_1pct":813396.8983562497,"gross_gex_1pct":813396.8983562497,"call_oi":111,"put_oi":0},{"strike":44550.0,"call_gex_1pct":13820.945692098001,"put_gex_1pct":0.0,"net_gex_1pct":13820.945692098001,"gross_gex_1pct":13820.945692098001,"call_oi":2,"put_oi":0},{"strike":44600.0,"call_gex_1pct":64873.83473834332,"put_gex_1pct":0.0,"net_gex_1pct":64873.83473834332,"gross_gex_1pct":64873.83473834332,"call_oi":10,"put_oi":0},{"strike":44650.0,"call_gex_1pct":6129.485161611472,"put_gex_1pct":0.0,"net_gex_1pct":6129.485161611472,"gross_gex_1pct":6129.485161611472,"call_oi":1,"put_oi":0},{"strike":44700.0,"call_gex_1pct":63447.14389611932,"put_gex_1pct":0.0,"net_gex_1pct":63447.14389611932,"gross_gex_1pct":63447.14389611932,"call_oi":11,"put_oi":0},{"strike":44750.0,"call_gex_1pct":27008.219238363607,"put_gex_1pct":0.0,"net_gex_1pct":27008.219238363607,"gross_gex_1pct":27008.219238363607,"call_oi":5,"put_oi":0},{"strike":44800.0,"call_gex_1pct":51083.312261806925,"put_gex_1pct":0.0,"net_gex_1pct":51083.312261806925,"gross_gex_1pct":51083.312261806925,"call_oi":10,"put_oi":0},{"strike":44850.0,"call_gex_1pct":33122.23314788654,"put_gex_1pct":0.0,"net_gex_1pct":33122.23314788654,"gross_gex_1pct":33122.23314788654,"call_oi":7,"put_oi":0},{"strike":44900.0,"call_gex_1pct":39878.00308369427,"put_gex_1pct":0.0,"net_gex_1pct":39878.00308369427,"gross_gex_1pct":39878.00308369427,"call_oi":9,"put_oi":0},{"strike":44950.0,"call_gex_1pct":30665.288502260675,"put_gex_1pct":0.0,"net_gex_1pct":30665.288502260675,"gross_gex_1pct":30665.288502260675,"call_oi":7,"put_oi":0},{"strike":45000.0,"call_gex_1pct":1964557.3544921633,"put_gex_1pct":0.0,"net_gex_1pct":1964557.3544921633,"gross_gex_1pct":1964557.3544921633,"call_oi":877,"put_oi":0},{"strike":45050.0,"call_gex_1pct":33402.39217222696,"put_gex_1pct":0.0,"net_gex_1pct":33402.39217222696,"gross_gex_1pct":33402.39217222696,"call_oi":16,"put_oi":0},{"strike":45100.0,"call_gex_1pct":41275.73574883879,"put_gex_1pct":0.0,"net_gex_1pct":41275.73574883879,"gross_gex_1pct":41275.73574883879,"call_oi":20,"put_oi":0},{"strike":45150.0,"call_gex_1pct":30605.73395006786,"put_gex_1pct":0.0,"net_gex_1pct":30605.73395006786,"gross_gex_1pct":30605.73395006786,"call_oi":15,"put_oi":0},{"strike":45200.0,"call_gex_1pct":42365.89998221463,"put_gex_1pct":0.0,"net_gex_1pct":42365.89998221463,"gross_gex_1pct":42365.89998221463,"call_oi":21,"put_oi":0},{"strike":45250.0,"call_gex_1pct":11969.39820553108,"put_gex_1pct":0.0,"net_gex_1pct":11969.39820553108,"gross_gex_1pct":11969.39820553108,"call_oi":6,"put_oi":0},{"strike":45300.0,"call_gex_1pct":17755.187474187434,"put_gex_1pct":0.0,"net_gex_1pct":17755.187474187434,"gross_gex_1pct":17755.187474187434,"call_oi":9,"put_oi":0},{"strike":45350.0,"call_gex_1pct":13657.767016745338,"put_gex_1pct":0.0,"net_gex_1pct":13657.767016745338,"gross_gex_1pct":13657.767016745338,"call_oi":7,"put_oi":0},{"strike":45400.0,"call_gex_1pct":19298.22000816105,"put_gex_1pct":0.0,"net_gex_1pct":19298.22000816105,"gross_gex_1pct":19298.22000816105,"call_oi":10,"put_oi":0},{"strike":45450.0,"call_gex_1pct":20998.182019328848,"put_gex_1pct":0.0,"net_gex_1pct":20998.182019328848,"gross_gex_1pct":20998.182019328848,"call_oi":11,"put_oi":0},{"strike":45500.0,"call_gex_1pct":1176592.8174917821,"put_gex_1pct":0.0,"net_gex_1pct":1176592.8174917821,"gross_gex_1pct":1176592.8174917821,"call_oi":665,"put_oi":0},{"strike":45550.0,"call_gex_1pct":66514.9186962312,"put_gex_1pct":0.0,"net_gex_1pct":66514.9186962312,"gross_gex_1pct":66514.9186962312,"call_oi":38,"put_oi":0},{"strike":45600.0,"call_gex_1pct":41563.52699739417,"put_gex_1pct":0.0,"net_gex_1pct":41563.52699739417,"gross_gex_1pct":41563.52699739417,"call_oi":24,"put_oi":0},{"strike":45700.0,"call_gex_1pct":50869.34566491034,"put_gex_1pct":0.0,"net_gex_1pct":50869.34566491034,"gross_gex_1pct":50869.34566491034,"call_oi":30,"put_oi":0},{"strike":45800.0,"call_gex_1pct":8303.707679929235,"put_gex_1pct":0.0,"net_gex_1pct":8303.707679929235,"gross_gex_1pct":8303.707679929235,"call_oi":5,"put_oi":0},{"strike":45900.0,"call_gex_1pct":16270.429656973958,"put_gex_1pct":0.0,"net_gex_1pct":16270.429656973958,"gross_gex_1pct":16270.429656973958,"call_oi":10,"put_oi":0},{"strike":46000.0,"call_gex_1pct":2294474.153624503,"put_gex_1pct":0.0,"net_gex_1pct":2294474.153624503,"gross_gex_1pct":2294474.153624503,"call_oi":1439,"put_oi":0},{"strike":46100.0,"call_gex_1pct":10941.24751393151,"put_gex_1pct":0.0,"net_gex_1pct":10941.24751393151,"gross_gex_1pct":10941.24751393151,"call_oi":7,"put_oi":0},{"strike":46200.0,"call_gex_1pct":41324.61842915005,"put_gex_1pct":0.0,"net_gex_1pct":41324.61842915005,"gross_gex_1pct":41324.61842915005,"call_oi":29,"put_oi":0},{"strike":46300.0,"call_gex_1pct":20963.458814263515,"put_gex_1pct":0.0,"net_gex_1pct":20963.458814263515,"gross_gex_1pct":20963.458814263515,"call_oi":15,"put_oi":0},{"strike":46400.0,"call_gex_1pct":4113.087939164662,"put_gex_1pct":0.0,"net_gex_1pct":4113.087939164662,"gross_gex_1pct":4113.087939164662,"call_oi":3,"put_oi":0},{"strike":46500.0,"call_gex_1pct":102246.10677886933,"put_gex_1pct":0.0,"net_gex_1pct":102246.10677886933,"gross_gex_1pct":102246.10677886933,"call_oi":76,"put_oi":0},{"strike":46600.0,"call_gex_1pct":25088.915214504512,"put_gex_1pct":0.0,"net_gex_1pct":25088.915214504512,"gross_gex_1pct":25088.915214504512,"call_oi":19,"put_oi":0},{"strike":46700.0,"call_gex_1pct":16852.82592699232,"put_gex_1pct":0.0,"net_gex_1pct":16852.82592699232,"gross_gex_1pct":16852.82592699232,"call_oi":13,"put_oi":0},{"strike":46800.0,"call_gex_1pct":22914.292101741732,"put_gex_1pct":0.0,"net_gex_1pct":22914.292101741732,"gross_gex_1pct":22914.292101741732,"call_oi":18,"put_oi":0},{"strike":46900.0,"call_gex_1pct":5001.490962523189,"put_gex_1pct":0.0,"net_gex_1pct":5001.490962523189,"gross_gex_1pct":5001.490962523189,"call_oi":4,"put_oi":0},{"strike":47000.0,"call_gex_1pct":2507186.7687578835,"put_gex_1pct":0.0,"net_gex_1pct":2507186.7687578835,"gross_gex_1pct":2507186.7687578835,"call_oi":2041,"put_oi":0},{"strike":47100.0,"call_gex_1pct":6669.905461529586,"put_gex_1pct":0.0,"net_gex_1pct":6669.905461529586,"gross_gex_1pct":6669.905461529586,"call_oi":6,"put_oi":0},{"strike":47200.0,"call_gex_1pct":5462.755808597076,"put_gex_1pct":0.0,"net_gex_1pct":5462.755808597076,"gross_gex_1pct":5462.755808597076,"call_oi":5,"put_oi":0},{"strike":47300.0,"call_gex_1pct":2932.6479045139395,"put_gex_1pct":0.0,"net_gex_1pct":2932.6479045139395,"gross_gex_1pct":2932.6479045139395,"call_oi":3,"put_oi":0},{"strike":47400.0,"call_gex_1pct":2883.320586852602,"put_gex_1pct":0.0,"net_gex_1pct":2883.320586852602,"gross_gex_1pct":2883.320586852602,"call_oi":3,"put_oi":0},{"strike":47500.0,"call_gex_1pct":2541.2564619410355,"put_gex_1pct":0.0,"net_gex_1pct":2541.2564619410355,"gross_gex_1pct":2541.2564619410355,"call_oi":3,"put_oi":0},{"strike":47600.0,"call_gex_1pct":833.1255527493748,"put_gex_1pct":0.0,"net_gex_1pct":833.1255527493748,"gross_gex_1pct":833.1255527493748,"call_oi":1,"put_oi":0},{"strike":47700.0,"call_gex_1pct":7376.00487322125,"put_gex_1pct":0.0,"net_gex_1pct":7376.00487322125,"gross_gex_1pct":7376.00487322125,"call_oi":9,"put_oi":0},{"strike":47800.0,"call_gex_1pct":54479.2703002482,"put_gex_1pct":0.0,"net_gex_1pct":54479.2703002482,"gross_gex_1pct":54479.2703002482,"call_oi":77,"put_oi":0},{"strike":47900.0,"call_gex_1pct":6962.193434231162,"put_gex_1pct":0.0,"net_gex_1pct":6962.193434231162,"gross_gex_1pct":6962.193434231162,"call_oi":10,"put_oi":0},{"strike":48000.0,"call_gex_1pct":41798.57655458679,"put_gex_1pct":0.0,"net_gex_1pct":41798.57655458679,"gross_gex_1pct":41798.57655458679,"call_oi":61,"put_oi":0},{"strike":48100.0,"call_gex_1pct":3442.847845876217,"put_gex_1pct":0.0,"net_gex_1pct":3442.847845876217,"gross_gex_1pct":3442.847845876217,"call_oi":6,"put_oi":0},{"strike":48200.0,"call_gex_1pct":2824.5316407721934,"put_gex_1pct":0.0,"net_gex_1pct":2824.5316407721934,"gross_gex_1pct":2824.5316407721934,"call_oi":5,"put_oi":0},{"strike":48300.0,"call_gex_1pct":2781.197706776518,"put_gex_1pct":0.0,"net_gex_1pct":2781.197706776518,"gross_gex_1pct":2781.197706776518,"call_oi":5,"put_oi":0},{"strike":48400.0,"call_gex_1pct":2738.995418373103,"put_gex_1pct":0.0,"net_gex_1pct":2738.995418373103,"gross_gex_1pct":2738.995418373103,"call_oi":5,"put_oi":0},{"strike":48500.0,"call_gex_1pct":3495.3109459685484,"put_gex_1pct":0.0,"net_gex_1pct":3495.3109459685484,"gross_gex_1pct":3495.3109459685484,"call_oi":8,"put_oi":0},{"strike":48600.0,"call_gex_1pct":1721.5631743572699,"put_gex_1pct":0.0,"net_gex_1pct":1721.5631743572699,"gross_gex_1pct":1721.5631743572699,"call_oi":4,"put_oi":0},{"strike":48700.0,"call_gex_1pct":32226.550747183315,"put_gex_1pct":0.0,"net_gex_1pct":32226.550747183315,"gross_gex_1pct":32226.550747183315,"call_oi":76,"put_oi":0}]}
```

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
| 買權多空淨 OI 變化 (2026-11-18→2026-11-19) | -508 | TAIFEX Proxy snapshots (2026-11-18) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,459 | TAIFEX Proxy |
| 賣權空方 OI | 10,621 | TAIFEX Proxy |
| 賣權多空淨 OI | -162 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-18→2026-11-19) | -291 | TAIFEX Proxy snapshots (2026-11-18) |
- 資料日期：買權 2026-11-19／賣權 2026-11-19 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -1,671 | 2026-11-18→2026-11-19 | TAIFEX Proxy snapshots (2026-11-18) |
| 買權前十大 | -508 | 2026-11-18→2026-11-19 | TAIFEX Proxy snapshots (2026-11-18) |
| 賣權前十大 | -291 | 2026-11-18→2026-11-19 | TAIFEX Proxy snapshots (2026-11-18) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-19；本次報告產製時間：2026-11-20 15:52:36；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 覆蓋：86 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (0)：無

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
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611W4（到期日 2026-11-25）與 Options Key Levels 主到期月份 202611F3 不同；GEX 數值應以實際使用到期月份為準
- TAIFEX 註記：主力到期月份已由 202611 換至 202611F3；僅比較前後快照中相同主力月份的共同合約，不跨月份相減
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -243.1 | -99,219 | +1,310 | +2,657 | +9,756 | -601 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +43.9 | +91,791 | -4,192 | +0 | -23,450 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -233.0 | -1,455 | +1,723 | -366 | -9,929 | -1,537 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
