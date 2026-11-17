# DATA_REPORT_20261116

- 報告日期：`2026-11-17`
- T0 交易日期：`2026-11-16`
- 首次資料產出時間：`2026-11-17 18:57:32`
- 本次更新開始時間：`2026-11-17 18:57:32`
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
| 加權指數 | 41,040.08 | 點 | twse-proxy |
| 開盤 | 43,512.42 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 43,512.42 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 41,040.08 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 41,040.08 | 點 | twse-proxy |
| 漲跌點數 | -2,635.04 | 點 | twse-proxy |
| 漲跌幅 | -6.03 | % | twse-proxy |
| 成交金額 | 9,031.2 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 99 | twse-proxy |
| 下跌家數 | 948 | twse-proxy |
| 平盤家數 | 36 | twse-proxy |
| 漲停家數 | 8 | twse-proxy |
| 跌停家數 | 83 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 97 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 746 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 35 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 24 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 85 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -701.9 | 億元 | TWSE RWD BFI82U |
| 投信 | -183.0 | 億元 | TWSE RWD BFI82U |
| 自營商 | -259.0 | 億元 | TWSE RWD BFI82U |
| 三大法人合計 | -1,143.9 | 億元 | TWSE RWD BFI82U |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `Blave 上市市場融資維持率估算（當日暫估；資料日期：2026-11-16；自建計算備援）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 6,922.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -163.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 256,593 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | 10,712 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 158.59 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-16；估值 1240 檔；5 檔採最近有效收盤價（價格日期 20260402 至 20261116）；Blave 同 T0 交叉驗證 158.5240%；差異 0.068 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 33,344,159 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,415,779.521 | 2,192,625.956 | 20,608,405.477 | 張 |
| 借券賣出增減 | +9,493.336 | -1,885.045 | +7,608.291 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261116`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-17T18:57:57+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261116`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-17T18:57:58+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,031.2 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,705.4 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 10,736.6 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,416.59 | -145.08 | -1.92 | 2026-11-16 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,509.76 | -626.51 | -2.49 | 2026-11-16 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,197.15 | -746.59 | -2.67 | 2026-11-16 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,608.17 | -739.38 | -1.41 | 2026-11-16 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,610.65 | -535.67 | -5.28 | 2026-11-16 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 23.49 | 0.58 | +2.53 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 58,860.43 | -801.59 | -1.34 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,968.48 | -132.02 | -2.59 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,508.17 | -245.67 | -1.03 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,584.58 | -17.99 | -0.50 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,638.52 | -52.26 | -0.49 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,413.50 | -25.50 | -0.34 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,191.50 | -92.75 | -0.34 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,434.00 | -236.00 | -0.46 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,736.10 | -15.30 | -0.56 | 2026-11-17 | 2026-11-17T10:57:58+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | -0.05 | 16-NOV-26 | 2026-11-17T10:58:21+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.12 | -0.03 | 2026-11-16 | 2026-11-17T10:58:21+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.51 | -0.01 | 16-NOV-26 | 2026-11-17T10:58:40+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | -0.01 | 2026-11-16 | 2026-11-17T10:58:40+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.90 | 0.02 | +0.06 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.57 | 0.02 | +0.02 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.14 | -0.64 | -0.40 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,336.15 | 2.90 | +0.22 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 373.45 | -25.28 | -6.34 | 2026-11-16 | 2026-11-17T10:57:59+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.34 | -1.06 | -6.88 | 2026-11-16 | 2026-11-17T10:57:59+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.80 | -2.75 | -7.74 | 2026-11-16 | 2026-11-17T10:57:59+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.96 | 0.24 | +0.28 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,859.00 | 6.00 | +0.16 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,044.76 | -811.08 | -1.25 | 2026-11-17 | 2026-11-17T10:57:59+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：股王摔下萬元 聯發科鴻海收紅撐住4萬關
  - 來源：Yahoo 台股；發布時間：2026-11-17T09:08:36Z；台北時間：2026-11-17 17:08
  - 摘要：台股急拉後再下殺，重挫947點險守4萬關卡！今(17)日加權指數終場下跌947.97點、跌幅2.31%，收40092.11點，上市成交金額9631.10億元。早盤一度重挫1253.63點，隨後買盤拉抬、急拉1747.39點翻紅，但反攻未能延
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E8%B7%8C%E8%BF%91%E5%8D%83%E9%BB%9E%E8%90%AC%E9%87%91%E8%82%A1%E6%B2%92%E4%BA%86%E3%80%814%E8%90%AC%E9%97%9C%E9%82%84%E5%9C%A8%EF%BC%81%E9%AB%98%E5%83%B9%E8%82%A1%E6%B7%AA%E9%87%8D%E7%81%BD%E5%8D%80-%E8%81%AF%E7%99%BC%E7%A7%91%E9%B4%BB%E6%B5%B7%E7%B6%A0%E5%9C%B0%E4%B8%AD%E9%96%8B%E7%B4%85%E8%8A%B1%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090836112.html
- 事件2：韭菜翻車 旺矽、倉和爆違約交割波及6券商
  - 來源：Yahoo 台股；發布時間：2026-11-17T10:29:22Z；台北時間：2026-11-17 18:29
  - 摘要：台股近期震盪劇烈，又有上櫃個股爆出違約交割！櫃買中心今（17）日公告，半導體測試設備廠旺矽（6223）遭通報違約交割，金額高達5,406萬元；另一檔倉和（6538）也遭通報1,096.1萬元，兩檔合計達6,502.1萬元。值得注意的是，旺矽
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%88%E6%9C%89%E9%9F%AD%E8%8F%9C%E7%BF%BB%E8%BB%8A%EF%BC%81%E6%97%BA%E7%9F%BD%E4%BB%8A%E5%B9%B4%E5%86%8D%E7%88%865406%E8%90%AC%E5%85%83%E9%81%95%E7%B4%84%E4%BA%A4%E5%89%B2-%E5%80%89%E5%92%8C%E4%B9%9F%E9%81%AD%E9%80%9A%E5%A0%B1-102922897.html
- 事件3：5檔ETF換股 南亞科一口氣獲3檔納入
  - 來源：Yahoo 台股；發布時間：2026-11-17T09:25:11Z；台北時間：2026-11-17 17:25
  - 摘要：台灣指數公司今（17）日公布，不配息的0050之稱的凱基台灣TOP50 （009816）、中信小資高價30（00894）、中信綠能及電動車（00896）、兆豐台灣晶圓製造（00913）、元大台灣價值高息（00940）5檔案ETF換股，其中，
  - 原文連結：https://tw.stock.yahoo.com/news/5%E6%AA%94etf%E6%8F%9B%E8%82%A1%EF%BC%8100940%E3%80%8C10%E9%80%B210%E5%87%BA%E3%80%8D-%E5%88%AA%E8%8B%B1%E6%A5%AD%E9%81%94%E3%80%81%E8%81%AF%E7%99%BC%E7%A7%91%E5%A2%9E%E5%8D%97%E4%BA%9E%E7%A7%91-092511942.html
- 事件4：美選後藍色浪潮誰沾光？四大產業台鏈出列
  - 來源：Yahoo 台股；發布時間：2026-11-17T10:00:00Z；台北時間：2026-11-17 18:00
  - 摘要：美國期中選舉結果尚未開票完畢，但民主黨已確定拿下參眾兩院多數，並從共和黨手中奪下德州等6州的州長席位。這場選舉並不只是影響美國本土的政治版圖，同時也可能牽動美國能源投資、資料中心建置及台廠接單。美國期中選舉選什麼？川普的施政將受到哪些牽制？
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%8C%E8%97%8D%E8%89%B2%E6%B5%AA%E6%BD%AE%E3%80%8D%E4%BE%86%E8%A5%B2%EF%BC%81%E7%BE%8E%E5%9C%8B%E6%9C%9F%E4%B8%AD%E9%81%B8%E8%88%89%E5%BE%8C%E5%93%AA%E4%BA%9B%E7%94%A2%E6%A5%AD%E6%9C%89%E6%9C%9B%E6%88%90%E8%B4%8F%E5%AE%B6%EF%BC%9F%E5%9B%9B%E5%A4%A7%E7%94%A2%E6%A5%AD%E5%8F%97%E6%83%A0%E5%8F%B0%E9%8F%88%E5%87%BA%E5%88%97%EF%BC%81%EF%BD%9C%E7%9B%A4%E9%BB%9E%E6%A6%82%E5%BF%B5%E8%82%A1-100000395.html
- 事件5：大到不能倒銀行揭榜 6家名單連3年不變
  - 來源：Yahoo 台股；發布時間：2026-11-17T08:23:26Z；台北時間：2026-11-17 16:23
  - 摘要：金管會今（17）日今布今年度系統性重要銀行（D-SIBs，俗稱大到不能倒銀行）名單，維持中信銀行、台北富邦銀行、國泰世華銀行、合庫銀行、兆豐銀行與第一銀行等6家銀行，名單跟2025年及2024年相同。D-SIBs是在金融市場是具有領導性地位
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E5%88%B0%E4%B8%8D%E8%83%BD%E5%80%92%EF%BC%81%E9%87%91%E7%AE%A1%E6%9C%83%E4%BB%8A%E5%85%AC%E5%B8%836%E5%AE%B6%E7%B3%BB%E7%B5%B1%E6%80%A7%E9%8A%80%E8%A1%8C%E5%90%8D%E5%96%AE-082326041.html
- 事件6：PCB綠光罩頂！「這檔」連4跌26.3%挾景碩、南電跌停　富喬、德宏、聯茂、台燿也亮綠燈
  - 來源：Yahoo 台股；發布時間：2026-11-17T08:00:00Z；台北時間：2026-11-17 16:00
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導由於台積電（2330）、聯發科（2454）、日月光投控（3711）等電子權值齊殺，台股大盤今（17）日續跌，加權指數終場來到40092...
  - 原文連結：https://tw.stock.yahoo.com/news/pcb%E7%B6%A0%E5%85%89%E7%BD%A9%E9%A0%82-%E9%80%99%E6%AA%94-%E9%80%A34%E8%B7%8C26-3-%E6%8C%BE%E6%99%AF%E7%A2%A9-080000325.html
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
- 事件10：Analysis: The Fed's chairman sees an AI revolution coming. Now he has to figure out what it means
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 00:42:33 GMT；台北時間：2026-11-17 08:42
  - 摘要：Kevin Warsh sees AI at a turning point. He faces tough questions on jobs and interest rates.
  - 原文連結：https://www.cnbc.com/2026/11/16/kevin-warsh-fed-ai-jobs-productivity-interest-rateshtml.html
- 事件11：Fed Chairman Kevin Warsh stresses importance of AI to economy, but says it could ‘disappoint’
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 18:46:07 GMT；台北時間：2026-11-17 02:46
  - 摘要：unavailable
  - 原文連結：https://www.cnbc.com/2026/11/16/fed-ai-task-force-kevin-warsh.html
- 事件12：Anthropic’s Wall Street whisperer: Meet CFO Krishna Rao
  - 來源：CNBC；發布時間：Mon, 16 Nov 2026 20:44:24 GMT；台北時間：2026-11-17 04:44
  - 摘要：Anthropic's upcoming IPO is putting finance chief Krishna Rao into the limelight.
  - 原文連結：https://www.cnbc.com/2026/11/16/anthropic-cfo-krishna-rao-ipo.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-16

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,590 | 點 | TAIFEX Proxy |
| 最高價 | 41,828 | 點 | TAIFEX Proxy |
| 最低價 | 39,761 | 點 | TAIFEX Proxy |
| 收盤價 | 40,073 | 點 | TAIFEX Proxy |
| 漲跌點數 | -708 | 點 | TAIFEX Proxy |
| 漲跌幅 | -1.74 | % | TAIFEX Proxy |
| 成交量 | 138,833 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 41,828 / 39,761 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,900 | 點 | TAIFEX Proxy |
| 最高價 | 41,627 | 點 | TAIFEX Proxy |
| 最低價 | 40,616 | 點 | TAIFEX Proxy |
| 收盤價 | 40,935 | 點 | TAIFEX Proxy |
| 漲跌點數 | +154 | 點 | TAIFEX Proxy |
| 漲跌幅 | +0.38 | % | TAIFEX Proxy |
| 成交量 | 63,335 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 41,627 / 40,616 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,030 | TAIFEX Proxy |
| 外資空方 OI | 108,817 | TAIFEX Proxy |
| 外資多空淨 OI | -96,787 | TAIFEX Proxy |
| 投信多方 OI | 95,851 | TAIFEX Proxy |
| 投信空方 OI | 3,445 | TAIFEX Proxy |
| 投信多空淨 OI | +92,406 | TAIFEX Proxy |
| 自營商多方 OI | 5,573 | TAIFEX Proxy |
| 自營商空方 OI | 4,414 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,159 | TAIFEX Proxy |
| 三大法人合計多方 OI | 113,454 | TAIFEX Proxy |
| 三大法人合計空方 OI | 116,676 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -3,222 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +4,083 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -7,517 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +3,930 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-11→2026-11-16) | -15,651 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 153,931 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 155,075 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,144 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 41,010 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 38,693 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,317 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,461 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -1,180 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -1,180 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,820 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -706 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,114 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -4,144 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,611 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -341.2 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +131.7 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,073 | TAIFEX Proxy |
| 加權指數價格 | 41,040.08 | twse-proxy |
| 台指期與加權指數價差 | -967.08 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | -2.36 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | -967.08 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +862 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,073 | 40,935 | -862 | TAIFEX Proxy |
| 成交量 | 138,833 | 63,335 | +75,498 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+496（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 153,931 | 155,075 | -1,144 | 41,010 | 38,693 | +2,317 | -3,461 | 12,030 | 108,817 | -96,787 | +4,083 | TAIFEX Proxy |
| 投信 | 33,611 | 34,791 | -1,180 | 0 | 0 | +0 | -1,180 | 95,851 | 3,445 | +92,406 | -7,517 | TAIFEX Proxy |
| 自營商 | 15,358 | 17,178 | -1,820 | 2,238 | 2,944 | -706 | -1,114 | 5,573 | 4,414 | +1,159 | +3,930 | TAIFEX Proxy |
| 三大法人合計 | 202,900 | 207,044 | -4,144 | 43,248 | 41,637 | +1,611 | -5,755 | 113,454 | 116,676 | -3,222 | +496 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 39,917 | TAIFEX Proxy |
| 前十大交易人空方 OI | 35,820 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,097 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-11→2026-11-16) | -15,651 | TAIFEX Proxy snapshots (2026-11-12) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 31.33% | TAIFEX Proxy |
| 夜盤漲跌點數 | +154 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,317 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-16 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-17 18:57:32 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 224,718 | TAIFEX Proxy |
| Call 總未平倉量 OI | 112,991 | TAIFEX Proxy |
| Call OI 增減（共同合約） | unavailable | unavailable |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 182,619 | TAIFEX Proxy |
| Put 總未平倉量 OI | 59,706 | TAIFEX Proxy |
| Put OI 增減（共同合約） | unavailable | unavailable |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.23 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.89 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.53 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-13→2026-11-16) | -17.65 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-13→2026-11-16) | -3.96 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 66,734 | TAIFEX Proxy |
| 外資 Call日賣 | 64,552 | TAIFEX Proxy |
| 外資 Call日淨 | +2,182 | TAIFEX Proxy |
| 外資 Put日買 | 68,854 | TAIFEX Proxy |
| 外資 Put日賣 | 68,672 | TAIFEX Proxy |
| 外資 Put日淨 | +182 | TAIFEX Proxy |
| 外資 Call夜買 | 28,132 | TAIFEX Proxy |
| 外資 Call夜賣 | 27,501 | TAIFEX Proxy |
| 外資 Call夜淨 | +631 | TAIFEX Proxy |
| 外資 Put夜買 | 15,841 | TAIFEX Proxy |
| 外資 Put夜賣 | 16,953 | TAIFEX Proxy |
| 外資 Put夜淨 | -1,112 | TAIFEX Proxy |
| 外資 日盤淨總量 | +2,000 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,551 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,294 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 69,887 | TAIFEX Proxy |
| 自營商 Call日賣 | 73,892 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,005 | TAIFEX Proxy |
| 自營商 Put日買 | 64,742 | TAIFEX Proxy |
| 自營商 Put日賣 | 64,997 | TAIFEX Proxy |
| 自營商 Put日淨 | -255 | TAIFEX Proxy |
| 自營商 Call夜買 | 17,481 | TAIFEX Proxy |
| 自營商 Call夜賣 | 20,567 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,086 | TAIFEX Proxy |
| 自營商 Put夜買 | 19,141 | TAIFEX Proxy |
| 自營商 Put夜賣 | 18,195 | TAIFEX Proxy |
| 自營商 Put夜淨 | +946 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -3,750 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -919 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -1,201 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 9,318 | TAIFEX Proxy |
| Call OI 第2大履約價 | 47,500 | 7,874 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 5,357 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 9,318 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 9,318 | 8.25% | TAIFEX Proxy |
| C2 | 47,500 | 7,874 | 6.97% | TAIFEX Proxy |
| C3 | 44,000 | 5,357 | 4.74% | TAIFEX Proxy |
| C4 | 48,000 | 5,068 | 4.49% | TAIFEX Proxy |
| C5 | 45,000 | 4,329 | 3.83% | TAIFEX Proxy |
| C6 | 46,500 | 3,724 | 3.3% | TAIFEX Proxy |
| C7 | 43,000 | 3,567 | 3.16% | TAIFEX Proxy |
| C8 | 47,000 | 3,385 | 3.0% | TAIFEX Proxy |
| C9 | 48,500 | 3,253 | 2.88% | TAIFEX Proxy |
| C10 | 50,000 | 2,700 | 2.39% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 8,465 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 2,741 | TAIFEX Proxy |
| Put OI 第3大履約價 | 42,000 | 1,970 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 8,465 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 8,465 | 14.18% | TAIFEX Proxy |
| P2 | 40,000 | 2,741 | 4.59% | TAIFEX Proxy |
| P3 | 42,000 | 1,970 | 3.3% | TAIFEX Proxy |
| P4 | 38,000 | 1,697 | 2.84% | TAIFEX Proxy |
| P5 | 41,000 | 1,614 | 2.7% | TAIFEX Proxy |
| P6 | 44,000 | 1,562 | 2.62% | TAIFEX Proxy |
| P7 | 41,500 | 1,528 | 2.56% | TAIFEX Proxy |
| P8 | 39,000 | 1,513 | 2.53% | TAIFEX Proxy |
| P9 | 43,000 | 1,464 | 2.45% | TAIFEX Proxy |
| P10 | 42,500 | 1,297 | 2.17% | TAIFEX Proxy |


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
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 40,000.00 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,380.47 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 112,991 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 0 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 59,706 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 0 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-16 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：36,936.07～45,144.09
- 搜尋步長／計算次數：10.00／446
- 起點／終點 Net GEX：-2,381,516,663.30／16,509,259.28
- 搜尋區間最低／最高 Net GEX：-3,077,859,327.63／16,509,259.28
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-16","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":292,"delta_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":254,"delta_rows":330},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-16","source":"taifex_web","fallback_used":false,"attempts":[{"attempt":1,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3249,"primary_error":null,"parser":{"input_rows":3249,"array_rows":3249,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3244,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3244,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"accepted_txo_rows":3244}],"parser":{"input_rows":3249,"array_rows":3249,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3244,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3244,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"final_rows":3244,"per_expiry_rows":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：34,884.07～47,196.09
- 搜尋步長／計算次數：10.00／1232
- 起點／終點 Net GEX：-1,716,562,460.70／11,422,309,026.60
- 搜尋區間最低／最高 Net GEX：-3,077,860,821.24／12,571,742,843.25
- 正負號交叉次數：1
- 擴大區間診斷 Flip：41,380.47

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | -920,749,536.99 NT$ | 沿用前版（原來源：TAIFEX Gamma model；NT$／標的變動 1%） |
| Gross GEX（標的變動 1%） | 8,438,153,714.55 NT$ | 沿用前版（原來源：TAIFEX Gamma model；NT$／標的變動 1%） |
| 模型品質 | usable | 沿用前版（原來源：Black-Scholes Gamma using TAIFEX settlement-implied volatility） |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 沿用前版（原來源：模型限制；非 TAIFEX 公布的 Dealer 部位） |
| 履約價資料筆數 | 306 | 沿用前版（原來源：資料日期：2026-11-16） |
| 正 Net GEX 最大履約價 | 43,000 | 沿用前版（原來源：依 Net GEX 排序） |
| 負 Net GEX 最低履約價 | 40,000 | 沿用前版（原來源：依 Net GEX 排序） |
- GEX 明細 unavailable；不以 Wall／Flip proxy 代替。

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 43,100 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 135,406 | 133,406 | +2,000 | 45,085 | 43,342 | +1,743 | +257 | TAIFEX Proxy |
| 投信 | 8,005 | 18,220 | -10,215 | 5 | 0 | +5 | -10,220 | TAIFEX Proxy |
| 自營商 | 134,884 | 138,634 | -3,750 | 35,676 | 39,708 | -4,032 | +282 | TAIFEX Proxy |
| 三大法人合計 | 278,295 | 290,260 | -11,965 | 80,766 | 83,050 | -2,284 | -9,681 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 24.03 | 21.58 | +2.45 | 5.96 | 5.34 | +0.62 | +1.83 | TAIFEX Proxy |
| 投信 | 0.17 | 11.21 | -11.04 | 0.00 | 0.00 | +0.00 | -11.04 | TAIFEX Proxy |
| 自營商 | 29.03 | 21.62 | +7.41 | 5.68 | 6.23 | -0.55 | +7.96 | TAIFEX Proxy |
| 三大法人合計 | 53.23 | 54.40 | -1.18 | 11.64 | 11.57 | +0.07 | -1.25 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 46,765 | TAIFEX Proxy |
| 買權空方 OI | 70,976 | TAIFEX Proxy |
| 買權多空淨 OI | -24,211 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-11→2026-11-16) | -19,234 | TAIFEX Proxy snapshots (2026-11-12) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 30,112 | TAIFEX Proxy |
| 賣權空方 OI | 28,929 | TAIFEX Proxy |
| 賣權多空淨 OI | +1,183 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-11→2026-11-16) | +3,690 | TAIFEX Proxy snapshots (2026-11-12) |
- 資料日期：買權 2026-11-16／賣權 2026-11-16 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -15,651 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |
| 買權前十大 | -19,234 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |
| 賣權前十大 | +3,690 | 2026-11-11→2026-11-16 | TAIFEX Proxy snapshots (2026-11-12) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-16；本次報告產製時間：2026-11-17 18:57:32；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 保護：8 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：91 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (3)：options.chain_oi_change, options.pos_change, options.wall_change

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
- margin_ratio：`Blave 上市市場融資維持率估算（當日暫估；資料日期：2026-11-16；自建計算備援）`
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
- 註記：亞洲指數與前份 DATA (DATA_REPORT_20261113.md) 完全相同，疑似 Yahoo 未更新，僅參考不解讀方向
- 註記：上市市場維持率為當日暫估；TWSE 自建部分計算僅供診斷（部分估算 158.5918%；價格覆蓋率 0.999194；已估值 1239/1240 檔；缺價 1 檔：['1589']），不得作為正式維持率。TWSE 自建計算未成功（partial calculation only; missing close for 1 listed securities: ['1589']）；改用 Blave 同 T0 數值（2026-11-16）。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-17，非 T0 2026-11-16)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：GEX Worker 診斷：code=REQUEST_TIMEOUT；stage=http_request；HTTP=None；Worker request timed out；HTTPSConnectionPool(host='taifex.grichtoyang.workers.dev', port=443): Read timed out. (read timeout=40)
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma 原始端點不可用（上游 502）；已由 options-market-structure-compact (proxy) 備援取得（Wall 有值；Flip 有值）
- TAIFEX 註記：逐履約價 GEX／Net GEX／Gross GEX 未取得或資料不完整，標 unavailable（不以 Wall/Flip proxy 代替）
- TAIFEX 註記：跨到期換月（舊202611F2→新202611），日對日 OI/Walls 變化不適用
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -701.9 | -96,787 | -1,144 | +2,317 | +2,000 | +1,743 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -183.0 | +92,406 | -1,180 | +0 | -10,215 | +5 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -259.0 | +1,159 | -1,820 | -706 | -3,750 | -4,032 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
