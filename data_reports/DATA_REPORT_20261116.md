# DATA_REPORT_20261116

- 報告日期：`2026-11-17`
- T0 交易日期：`2026-11-16`
- 首次資料產出時間：`2026-11-17 21:32:57`
- 本次更新開始時間：`2026-11-17 21:32:57`
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

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-16；估值 1240 檔；5 檔採最近有效收盤價（價格日期 20260402 至 20261116）；Blave 同 T0 交叉驗證 158.5240%；差異 0.068 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

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
- TWSE TWT93U（上市）：資料日期：`20261116`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-17T21:34:25+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261116`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-17T21:34:32+08:00`；狀態：`available_after_schedule`

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
| S&P 500 | ^GSPC | 7,416.59 | -145.08 | -1.92 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,509.76 | -626.51 | -2.49 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,197.15 | -746.59 | -2.67 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,608.17 | -739.38 | -1.41 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,610.65 | -535.67 | -5.28 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 22.90 | -0.01 | -0.04 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 58,860.43 | -801.59 | -1.34 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,968.48 | -132.02 | -2.59 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,508.17 | -245.67 | -1.03 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,584.58 | -17.99 | -0.50 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,638.52 | -52.26 | -0.49 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,432.00 | -7.00 | -0.09 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,366.50 | 82.25 | +0.30 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,314.00 | -356.00 | -0.69 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,739.20 | -12.20 | -0.44 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | -0.05 | 16-NOV-26 | 2026-11-17T13:34:54+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.12 | -0.03 | 2026-11-16 | 2026-11-17T13:34:54+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.51 | -0.01 | 16-NOV-26 | 2026-11-17T13:35:11+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.47 | 0.01 | 2026-11-17 | 2026-11-17T13:35:11+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.94 | 0.06 | +0.18 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.64 | 0.09 | +0.09 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.44 | -0.34 | -0.21 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,337.31 | 4.06 | +0.30 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 373.45 | -25.28 | -6.34 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.34 | -1.06 | -6.88 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.80 | -2.75 | -7.74 | 2026-11-16 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 86.70 | 0.98 | +1.14 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,856.50 | 3.50 | +0.09 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,889.28 | 33.44 | +0.05 | 2026-11-17 | 2026-11-17T13:34:33+00:00 | UTC | Yahoo Finance Chart API |

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
- 事件6：低軌衛星整片綠！「這檔」連挫5根牽金像電、奇鋐、台燿、騰輝跌停　大眾控、精測跌破9%
  - 來源：Yahoo 台股；發布時間：2026-11-17T13:15:00Z；台北時間：2026-11-17 21:15
  - 摘要：[FTNN新聞網]記者陳献朋／綜合報導隨記憶體、PCB等AI相關族群及台積電（2330）等多檔權值收低，台股大盤今（17）繼續大跌，加權指數來到40092.11點，下跌947....
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BD%8E%E8%BB%8C%E8%A1%9B%E6%98%9F%E6%95%B4%E7%89%87%E7%B6%A0-%E9%80%99%E6%AA%94-%E9%80%A3%E6%8C%AB5%E6%A0%B9%E7%89%BD%E9%87%91%E5%83%8F%E9%9B%BB-%E5%A5%87%E9%8B%90-%E5%8F%B0%E7%87%BF-131500348.html
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
- 事件11：Investor Steve Eisman says the AI neocloud stocks are in 'big trouble' from Nvidia fallout
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 13:33:20 GMT；台北時間：2026-11-17 21:33
  - 摘要：Steve Eisman is appearing on "Squawk Box" on Tuesday.
  - 原文連結：https://www.cnbc.com/2026/11/17/big-short-investor-steve-eisman-to-discuss-nvidia-anthropic-and-ai-bull-on-cnbc.html
- 事件12：Anthropic IPO: For hundreds of billions of dollars flowing into AI startups, a big debut is a must
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 13:15:44 GMT；台北時間：2026-11-17 21:15
  - 摘要：Venture investors are sitting on big gains from the AI buildout. Anthropic's IPO could set the stage for many smaller AI startups seeking exits.
  - 原文連結：https://www.cnbc.com/2026/11/17/anthropic-ipo-ai-venture-capital.html


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
| 本次報告產製時間 | 2026-11-17 21:32:57 | 本機 |
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
| Gamma Wall 價位 | 40,000.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-16 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 41,380.47 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 112,991 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 112,961 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 59,706 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 59,706 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-16 | TAIFEX Proxy (options-gamma-levels) |
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
{"requested_date":"2026-11-16","source":"taifex_web","fallback_used":false,"index_duration_ms":2204,"index_error":null,"openapi_fetch_duration_ms":null,"attempts":[{"attempt":1,"duration_ms":4989,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3249,"primary_error":null,"parser":{"input_rows":3249,"array_rows":3249,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3244,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3244,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"accepted_txo_rows":3244}],"parser":{"input_rows":3249,"array_rows":3249,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3244,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3244,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"final_rows":3244,"per_expiry_rows":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":354,"recognized_type_rows":354,"valid_strike_rows":354,"valid_delta_rows":354,"parsed_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":330,"recognized_type_rows":330,"valid_strike_rows":330,"valid_delta_rows":330,"parsed_rows":330},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]}
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
| Net GEX（標的變動 1%） | -920,749,536.99 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 8,438,153,714.55 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 306 | 資料日期：2026-11-16 |
| 正 Net GEX 最大履約價 | 43,000 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 40,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：43,000（232,261,523.11 NT$）、43,200（205,611,889.06 NT$）、43,400（174,190,205.29 NT$）、44,000（172,728,673.55 NT$）、43,600（164,362,979.27 NT$）
- 負 Net GEX Top 5：40,000（-315,536,544.85 NT$）、41,500（-183,709,928.80 NT$）、41,000（-156,315,180.69 NT$）、39,000（-133,925,364.81 NT$）、42,000（-129,382,142.14 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-16","underlying":41040.08,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":-920749536.9897897,"gross_gex_1pct":8438153714.552064,"gamma_diagnostics":{"chain_rows":616,"delta_rows":616,"matched_strike_keys":616,"positive_oi_settlement_eligible":494,"invalid_oi":122,"invalid_settlement":0,"below_intrinsic":11,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":483},"formal_flip_diagnostics":{"search_lower_underlying":36936.072,"search_upper_underlying":45144.088,"step":10,"evaluations":446,"start_net_gex_1pct":-2381516663.2993035,"end_net_gex_1pct":16509259.281836879,"min_net_gex_1pct":-3077859327.6332536,"max_net_gex_1pct":16509259.281836879,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":41374.068,"upper_underlying":41384.068,"estimated_underlying":41380.46806231109,"lower_net_gex_1pct":-18836030.915580224,"upper_net_gex_1pct":10594980.846500685},"wide_range_flip_diagnostics":{"search_lower_underlying":34884.068,"search_upper_underlying":47196.092,"reference_underlying":41040.08,"step":10,"evaluations":1232,"start_net_gex_1pct":-1716562460.6986191,"end_net_gex_1pct":11422309026.59668,"min_net_gex_1pct":-3077860821.2418823,"max_net_gex_1pct":12571742843.253386,"zero_crossings":1,"found":true,"selected_crossing_distance":340.388062311089},"expiry_selection_diagnostics":{"requested_date":"2026-11-16","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":292,"delta_rows":354},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":254,"delta_rows":330},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-15311538.05262736,"net_gex_1pct":-15311538.05262736,"gross_gex_1pct":15311538.05262736,"call_oi":0,"put_oi":8465},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-772550.0815613812,"net_gex_1pct":-772550.0815613812,"gross_gex_1pct":772550.0815613812,"call_oi":0,"put_oi":238},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-175324.2360902881,"net_gex_1pct":-175324.2360902881,"gross_gex_1pct":175324.2360902881,"call_oi":0,"put_oi":51},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-385355.42655200296,"net_gex_1pct":-385355.42655200296,"gross_gex_1pct":385355.42655200296,"call_oi":0,"put_oi":106},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-172778.12094123918,"net_gex_1pct":-172778.12094123918,"gross_gex_1pct":172778.12094123918,"call_oi":0,"put_oi":45},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-136527.50204084575,"net_gex_1pct":-136527.50204084575,"gross_gex_1pct":136527.50204084575,"call_oi":0,"put_oi":25},{"strike":34300.0,"call_gex_1pct":0.0,"put_gex_1pct":-165018.66886630218,"net_gex_1pct":-165018.66886630218,"gross_gex_1pct":165018.66886630218,"call_oi":0,"put_oi":29},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-231201.1718517607,"net_gex_1pct":-231201.1718517607,"gross_gex_1pct":231201.1718517607,"call_oi":0,"put_oi":39},{"strike":34500.0,"call_gex_1pct":0.0,"put_gex_1pct":-194841.27091627952,"net_gex_1pct":-194841.27091627952,"gross_gex_1pct":194841.27091627952,"call_oi":0,"put_oi":32},{"strike":34600.0,"call_gex_1pct":0.0,"put_gex_1pct":-155576.2101678394,"net_gex_1pct":-155576.2101678394,"gross_gex_1pct":155576.2101678394,"call_oi":0,"put_oi":19},{"strike":34700.0,"call_gex_1pct":0.0,"put_gex_1pct":-254048.08966740826,"net_gex_1pct":-254048.08966740826,"gross_gex_1pct":254048.08966740826,"call_oi":0,"put_oi":28},{"strike":34800.0,"call_gex_1pct":0.0,"put_gex_1pct":-474390.3862603333,"net_gex_1pct":-474390.3862603333,"gross_gex_1pct":474390.3862603333,"call_oi":0,"put_oi":47},{"strike":34900.0,"call_gex_1pct":0.0,"put_gex_1pct":-754183.6558799678,"net_gex_1pct":-754183.6558799678,"gross_gex_1pct":754183.6558799678,"call_oi":0,"put_oi":68},{"strike":35000.0,"call_gex_1pct":0.0,"put_gex_1pct":-8330825.751540575,"net_gex_1pct":-8330825.751540575,"gross_gex_1pct":8330825.751540575,"call_oi":0,"put_oi":722},{"strike":35100.0,"call_gex_1pct":0.0,"put_gex_1pct":-478360.7536153634,"net_gex_1pct":-478360.7536153634,"gross_gex_1pct":478360.7536153634,"call_oi":0,"put_oi":37},{"strike":35200.0,"call_gex_1pct":0.0,"put_gex_1pct":-820528.9108487605,"net_gex_1pct":-820528.9108487605,"gross_gex_1pct":820528.9108487605,"call_oi":0,"put_oi":58},{"strike":35300.0,"call_gex_1pct":0.0,"put_gex_1pct":-4981973.7666510055,"net_gex_1pct":-4981973.7666510055,"gross_gex_1pct":4981973.7666510055,"call_oi":0,"put_oi":337},{"strike":35400.0,"call_gex_1pct":0.0,"put_gex_1pct":-699277.6064273476,"net_gex_1pct":-699277.6064273476,"gross_gex_1pct":699277.6064273476,"call_oi":0,"put_oi":44},{"strike":35500.0,"call_gex_1pct":0.0,"put_gex_1pct":-1683380.5167518584,"net_gex_1pct":-1683380.5167518584,"gross_gex_1pct":1683380.5167518584,"call_oi":0,"put_oi":99},{"strike":35600.0,"call_gex_1pct":0.0,"put_gex_1pct":-720855.498043923,"net_gex_1pct":-720855.498043923,"gross_gex_1pct":720855.498043923,"call_oi":0,"put_oi":40},{"strike":35700.0,"call_gex_1pct":0.0,"put_gex_1pct":-1609021.2053147838,"net_gex_1pct":-1609021.2053147838,"gross_gex_1pct":1609021.2053147838,"call_oi":0,"put_oi":84},{"strike":35800.0,"call_gex_1pct":0.0,"put_gex_1pct":-710629.345412949,"net_gex_1pct":-710629.345412949,"gross_gex_1pct":710629.345412949,"call_oi":0,"put_oi":35},{"strike":35900.0,"call_gex_1pct":0.0,"put_gex_1pct":-987678.6562987175,"net_gex_1pct":-987678.6562987175,"gross_gex_1pct":987678.6562987175,"call_oi":0,"put_oi":46},{"strike":36000.0,"call_gex_1pct":0.0,"put_gex_1pct":-22550462.65281522,"net_gex_1pct":-22550462.65281522,"gross_gex_1pct":22550462.65281522,"call_oi":0,"put_oi":1015},{"strike":36100.0,"call_gex_1pct":0.0,"put_gex_1pct":-2117605.6203247244,"net_gex_1pct":-2117605.6203247244,"gross_gex_1pct":2117605.6203247244,"call_oi":0,"put_oi":89},{"strike":36200.0,"call_gex_1pct":0.0,"put_gex_1pct":-1741336.3270297067,"net_gex_1pct":-1741336.3270297067,"gross_gex_1pct":1741336.3270297067,"call_oi":0,"put_oi":70},{"strike":36300.0,"call_gex_1pct":0.0,"put_gex_1pct":-2354619.3005012055,"net_gex_1pct":-2354619.3005012055,"gross_gex_1pct":2354619.3005012055,"call_oi":0,"put_oi":90},{"strike":36400.0,"call_gex_1pct":0.0,"put_gex_1pct":-4317548.865100107,"net_gex_1pct":-4317548.865100107,"gross_gex_1pct":4317548.865100107,"call_oi":0,"put_oi":158},{"strike":36500.0,"call_gex_1pct":0.0,"put_gex_1pct":-28291858.95692331,"net_gex_1pct":-28291858.95692331,"gross_gex_1pct":28291858.95692331,"call_oi":0,"put_oi":997},{"strike":36600.0,"call_gex_1pct":0.0,"put_gex_1pct":-2730995.3323535775,"net_gex_1pct":-2730995.3323535775,"gross_gex_1pct":2730995.3323535775,"call_oi":0,"put_oi":89},{"strike":36700.0,"call_gex_1pct":0.0,"put_gex_1pct":-3740696.0298086405,"net_gex_1pct":-3740696.0298086405,"gross_gex_1pct":3740696.0298086405,"call_oi":0,"put_oi":115},{"strike":36800.0,"call_gex_1pct":0.0,"put_gex_1pct":-17443687.671609223,"net_gex_1pct":-17443687.671609223,"gross_gex_1pct":17443687.671609223,"call_oi":0,"put_oi":511},{"strike":36900.0,"call_gex_1pct":0.0,"put_gex_1pct":-4668591.137200646,"net_gex_1pct":-4668591.137200646,"gross_gex_1pct":4668591.137200646,"call_oi":0,"put_oi":130},{"strike":37000.0,"call_gex_1pct":0.0,"put_gex_1pct":-37947635.25675871,"net_gex_1pct":-37947635.25675871,"gross_gex_1pct":37947635.25675871,"call_oi":0,"put_oi":1015},{"strike":37100.0,"call_gex_1pct":0.0,"put_gex_1pct":-4640468.573560254,"net_gex_1pct":-4640468.573560254,"gross_gex_1pct":4640468.573560254,"call_oi":0,"put_oi":116},{"strike":37200.0,"call_gex_1pct":0.0,"put_gex_1pct":-6144306.520176284,"net_gex_1pct":-6144306.520176284,"gross_gex_1pct":6144306.520176284,"call_oi":0,"put_oi":146},{"strike":37300.0,"call_gex_1pct":0.0,"put_gex_1pct":-7764181.55638427,"net_gex_1pct":-7764181.55638427,"gross_gex_1pct":7764181.55638427,"call_oi":0,"put_oi":176},{"strike":37400.0,"call_gex_1pct":0.0,"put_gex_1pct":-13974812.096651355,"net_gex_1pct":-13974812.096651355,"gross_gex_1pct":13974812.096651355,"call_oi":0,"put_oi":303},{"strike":37500.0,"call_gex_1pct":0.0,"put_gex_1pct":-28009538.065531407,"net_gex_1pct":-28009538.065531407,"gross_gex_1pct":28009538.065531407,"call_oi":0,"put_oi":582},{"strike":37600.0,"call_gex_1pct":0.0,"put_gex_1pct":-8966942.341294765,"net_gex_1pct":-8966942.341294765,"gross_gex_1pct":8966942.341294765,"call_oi":0,"put_oi":176},{"strike":37700.0,"call_gex_1pct":0.0,"put_gex_1pct":-6576853.094787231,"net_gex_1pct":-6576853.094787231,"gross_gex_1pct":6576853.094787231,"call_oi":0,"put_oi":124},{"strike":37800.0,"call_gex_1pct":0.0,"put_gex_1pct":-7346841.044278482,"net_gex_1pct":-7346841.044278482,"gross_gex_1pct":7346841.044278482,"call_oi":0,"put_oi":133},{"strike":37900.0,"call_gex_1pct":0.0,"put_gex_1pct":-7011842.134162431,"net_gex_1pct":-7011842.134162431,"gross_gex_1pct":7011842.134162431,"call_oi":0,"put_oi":121},{"strike":38000.0,"call_gex_1pct":0.0,"put_gex_1pct":-103046918.9780219,"net_gex_1pct":-103046918.9780219,"gross_gex_1pct":103046918.9780219,"call_oi":0,"put_oi":1697},{"strike":38100.0,"call_gex_1pct":0.0,"put_gex_1pct":-20661171.213425785,"net_gex_1pct":-20661171.213425785,"gross_gex_1pct":20661171.213425785,"call_oi":0,"put_oi":326},{"strike":38200.0,"call_gex_1pct":0.0,"put_gex_1pct":-8092909.167057011,"net_gex_1pct":-8092909.167057011,"gross_gex_1pct":8092909.167057011,"call_oi":0,"put_oi":122},{"strike":38300.0,"call_gex_1pct":28700.947555057817,"put_gex_1pct":-11479334.624772582,"net_gex_1pct":-11450633.677217524,"gross_gex_1pct":11508035.57232764,"call_oi":1,"put_oi":166},{"strike":38400.0,"call_gex_1pct":0.0,"put_gex_1pct":-6855079.9544020705,"net_gex_1pct":-6855079.9544020705,"gross_gex_1pct":6855079.9544020705,"call_oi":0,"put_oi":95},{"strike":38500.0,"call_gex_1pct":792616.4603949385,"put_gex_1pct":-41974851.65109477,"net_gex_1pct":-41182235.19069983,"gross_gex_1pct":42767468.11148971,"call_oi":14,"put_oi":558},{"strike":38550.0,"call_gex_1pct":0.0,"put_gex_1pct":-2610770.896074616,"net_gex_1pct":-2610770.896074616,"gross_gex_1pct":2610770.896074616,"call_oi":0,"put_oi":34},{"strike":38600.0,"call_gex_1pct":63881.66751511214,"put_gex_1pct":-11900741.32281138,"net_gex_1pct":-11836859.655296268,"gross_gex_1pct":11964622.990326492,"call_oi":1,"put_oi":152},{"strike":38650.0,"call_gex_1pct":0.0,"put_gex_1pct":-3914083.879399916,"net_gex_1pct":-3914083.879399916,"gross_gex_1pct":3914083.879399916,"call_oi":0,"put_oi":49},{"strike":38700.0,"call_gex_1pct":566042.2767823262,"put_gex_1pct":-9547678.559916653,"net_gex_1pct":-8981636.283134326,"gross_gex_1pct":10113720.83669898,"call_oi":8,"put_oi":117},{"strike":38750.0,"call_gex_1pct":0.0,"put_gex_1pct":-7791176.519904578,"net_gex_1pct":-7791176.519904578,"gross_gex_1pct":7791176.519904578,"call_oi":0,"put_oi":94},{"strike":38800.0,"call_gex_1pct":567266.7046602374,"put_gex_1pct":-37068824.977508634,"net_gex_1pct":-36501558.2728484,"gross_gex_1pct":37636091.68216887,"call_oi":7,"put_oi":438},{"strike":38850.0,"call_gex_1pct":0.0,"put_gex_1pct":-2847176.867414015,"net_gex_1pct":-2847176.867414015,"gross_gex_1pct":2847176.867414015,"call_oi":0,"put_oi":33},{"strike":38900.0,"call_gex_1pct":868927.2574592764,"put_gex_1pct":-69131499.33189945,"net_gex_1pct":-68262572.07444017,"gross_gex_1pct":70000426.58935873,"call_oi":10,"put_oi":787},{"strike":38950.0,"call_gex_1pct":0.0,"put_gex_1pct":-5927158.624624402,"net_gex_1pct":-5927158.624624402,"gross_gex_1pct":5927158.624624402,"call_oi":0,"put_oi":66},{"strike":39000.0,"call_gex_1pct":4457827.546856007,"put_gex_1pct":-138383192.36007157,"net_gex_1pct":-133925364.81321557,"gross_gex_1pct":142841019.9069276,"call_oi":48,"put_oi":1513},{"strike":39050.0,"call_gex_1pct":0.0,"put_gex_1pct":-7353972.8750641355,"net_gex_1pct":-7353972.8750641355,"gross_gex_1pct":7353972.8750641355,"call_oi":0,"put_oi":79},{"strike":39100.0,"call_gex_1pct":398000.538110313,"put_gex_1pct":-15758629.150114903,"net_gex_1pct":-15360628.61200459,"gross_gex_1pct":16156629.688225217,"call_oi":4,"put_oi":167},{"strike":39150.0,"call_gex_1pct":0.0,"put_gex_1pct":-6271145.174771315,"net_gex_1pct":-6271145.174771315,"gross_gex_1pct":6271145.174771315,"call_oi":0,"put_oi":65},{"strike":39200.0,"call_gex_1pct":846020.4719403805,"put_gex_1pct":-21814676.3460311,"net_gex_1pct":-20968655.87409072,"gross_gex_1pct":22660696.81797148,"call_oi":8,"put_oi":222},{"strike":39250.0,"call_gex_1pct":0.0,"put_gex_1pct":-11509244.585349293,"net_gex_1pct":-11509244.585349293,"gross_gex_1pct":11509244.585349293,"call_oi":0,"put_oi":115},{"strike":39300.0,"call_gex_1pct":111780.41177555385,"put_gex_1pct":-39723972.774444014,"net_gex_1pct":-39612192.36266846,"gross_gex_1pct":39835753.186219566,"call_oi":1,"put_oi":391},{"strike":39350.0,"call_gex_1pct":0.0,"put_gex_1pct":-13449837.21027351,"net_gex_1pct":-13449837.21027351,"gross_gex_1pct":13449837.21027351,"call_oi":0,"put_oi":130},{"strike":39400.0,"call_gex_1pct":470772.4974217869,"put_gex_1pct":-20665509.80926616,"net_gex_1pct":-20194737.311844375,"gross_gex_1pct":21136282.306687947,"call_oi":4,"put_oi":196},{"strike":39450.0,"call_gex_1pct":361900.0931937354,"put_gex_1pct":-6735338.360544186,"net_gex_1pct":-6373438.267350451,"gross_gex_1pct":7097238.453737921,"call_oi":3,"put_oi":63},{"strike":39500.0,"call_gex_1pct":2333776.102159461,"put_gex_1pct":-57309996.2936741,"net_gex_1pct":-54976220.19151463,"gross_gex_1pct":59643772.39583356,"call_oi":19,"put_oi":526},{"strike":39550.0,"call_gex_1pct":0.0,"put_gex_1pct":-3936094.1197400736,"net_gex_1pct":-3936094.1197400736,"gross_gex_1pct":3936094.1197400736,"call_oi":0,"put_oi":36},{"strike":39600.0,"call_gex_1pct":1414072.6835635577,"put_gex_1pct":-14204819.818285268,"net_gex_1pct":-12790747.13472171,"gross_gex_1pct":15618892.501848826,"call_oi":11,"put_oi":127},{"strike":39650.0,"call_gex_1pct":0.0,"put_gex_1pct":-6418265.590663377,"net_gex_1pct":-6418265.590663377,"gross_gex_1pct":6418265.590663377,"call_oi":0,"put_oi":57},{"strike":39700.0,"call_gex_1pct":3090796.562624686,"put_gex_1pct":-22334119.7657072,"net_gex_1pct":-19243323.203082513,"gross_gex_1pct":25424916.328331884,"call_oi":23,"put_oi":194},{"strike":39750.0,"call_gex_1pct":137354.3320752438,"put_gex_1pct":-11576752.169141656,"net_gex_1pct":-11439397.837066412,"gross_gex_1pct":11714106.5012169,"call_oi":1,"put_oi":99},{"strike":39800.0,"call_gex_1pct":80012191.85002576,"put_gex_1pct":-87124311.05580185,"net_gex_1pct":-7112119.205776095,"gross_gex_1pct":167136502.9058276,"call_oi":570,"put_oi":738},{"strike":39850.0,"call_gex_1pct":0.0,"put_gex_1pct":-8799911.407713955,"net_gex_1pct":-8799911.407713955,"gross_gex_1pct":8799911.407713955,"call_oi":0,"put_oi":73},{"strike":39900.0,"call_gex_1pct":3446989.703223664,"put_gex_1pct":-24302126.066156834,"net_gex_1pct":-20855136.36293317,"gross_gex_1pct":27749115.7693805,"call_oi":24,"put_oi":201},{"strike":39950.0,"call_gex_1pct":0.0,"put_gex_1pct":-10191898.848983465,"net_gex_1pct":-10191898.848983465,"gross_gex_1pct":10191898.848983465,"call_oi":0,"put_oi":83},{"strike":40000.0,"call_gex_1pct":26641030.132098924,"put_gex_1pct":-342177574.9852709,"net_gex_1pct":-315536544.853172,"gross_gex_1pct":368818605.11736983,"call_oi":176,"put_oi":2741},{"strike":40050.0,"call_gex_1pct":0.0,"put_gex_1pct":-10611252.01915154,"net_gex_1pct":-10611252.01915154,"gross_gex_1pct":10611252.01915154,"call_oi":0,"put_oi":84},{"strike":40100.0,"call_gex_1pct":2933187.3065350805,"put_gex_1pct":-23890855.70785074,"net_gex_1pct":-20957668.40131566,"gross_gex_1pct":26824043.01438582,"call_oi":19,"put_oi":186},{"strike":40150.0,"call_gex_1pct":155806.59060190062,"put_gex_1pct":-9319978.901193842,"net_gex_1pct":-9164172.310591942,"gross_gex_1pct":9475785.491795743,"call_oi":1,"put_oi":71},{"strike":40200.0,"call_gex_1pct":6203372.250243648,"put_gex_1pct":-38216653.72127541,"net_gex_1pct":-32013281.471031763,"gross_gex_1pct":44420025.97151906,"call_oi":39,"put_oi":292},{"strike":40250.0,"call_gex_1pct":160462.543315833,"put_gex_1pct":-8201730.509861265,"net_gex_1pct":-8041267.966545432,"gross_gex_1pct":8362193.053177099,"call_oi":1,"put_oi":61},{"strike":40300.0,"call_gex_1pct":22608298.564267423,"put_gex_1pct":-22933309.7189269,"net_gex_1pct":-325011.15465947613,"gross_gex_1pct":45541608.28319432,"call_oi":138,"put_oi":172},{"strike":40350.0,"call_gex_1pct":2808803.2782806195,"put_gex_1pct":-20642142.177705344,"net_gex_1pct":-17833338.899424724,"gross_gex_1pct":23450945.455985963,"call_oi":17,"put_oi":153},{"strike":40400.0,"call_gex_1pct":4831509.998473438,"put_gex_1pct":-17792605.181834295,"net_gex_1pct":-12961095.183360856,"gross_gex_1pct":22624115.180307735,"call_oi":29,"put_oi":131},{"strike":40450.0,"call_gex_1pct":3191499.736244381,"put_gex_1pct":-6217055.070590496,"net_gex_1pct":-3025555.334346115,"gross_gex_1pct":9408554.806834877,"call_oi":19,"put_oi":45},{"strike":40500.0,"call_gex_1pct":8061824.656382227,"put_gex_1pct":-105703194.94447708,"net_gex_1pct":-97641370.28809485,"gross_gex_1pct":113765019.60085931,"call_oi":47,"put_oi":760},{"strike":40550.0,"call_gex_1pct":1707005.9535998006,"put_gex_1pct":-50594139.408531696,"net_gex_1pct":-48887133.45493189,"gross_gex_1pct":52301145.3621315,"call_oi":10,"put_oi":369},{"strike":40600.0,"call_gex_1pct":4444869.45754432,"put_gex_1pct":-119101297.50733152,"net_gex_1pct":-114656428.0497872,"gross_gex_1pct":123546166.96487585,"call_oi":26,"put_oi":854},{"strike":40650.0,"call_gex_1pct":2618633.9719675262,"put_gex_1pct":-7762229.313025749,"net_gex_1pct":-5143595.341058223,"gross_gex_1pct":10380863.284993276,"call_oi":15,"put_oi":55},{"strike":40700.0,"call_gex_1pct":4047329.1243920876,"put_gex_1pct":-22162689.945849992,"net_gex_1pct":-18115360.821457904,"gross_gex_1pct":26210019.07024208,"call_oi":23,"put_oi":156},{"strike":40750.0,"call_gex_1pct":1762016.7048795263,"put_gex_1pct":-10582970.93121289,"net_gex_1pct":-8820954.226333365,"gross_gex_1pct":12344987.636092417,"call_oi":10,"put_oi":74},{"strike":40800.0,"call_gex_1pct":11188999.855645228,"put_gex_1pct":-49956224.40821392,"net_gex_1pct":-38767224.55256869,"gross_gex_1pct":61145224.26385915,"call_oi":63,"put_oi":347},{"strike":40850.0,"call_gex_1pct":1074117.7873152741,"put_gex_1pct":-10289895.743028931,"net_gex_1pct":-9215777.955713658,"gross_gex_1pct":11364013.530344205,"call_oi":6,"put_oi":71},{"strike":40900.0,"call_gex_1pct":5450438.112636073,"put_gex_1pct":-24813160.262063343,"net_gex_1pct":-19362722.149427272,"gross_gex_1pct":30263598.374699414,"call_oi":30,"put_oi":171},{"strike":40950.0,"call_gex_1pct":1648359.9695459048,"put_gex_1pct":-21356741.048193857,"net_gex_1pct":-19708381.078647953,"gross_gex_1pct":23005101.01773976,"call_oi":9,"put_oi":147},{"strike":41000.0,"call_gex_1pct":78459914.94711407,"put_gex_1pct":-234775095.6402367,"net_gex_1pct":-156315180.69312263,"gross_gex_1pct":313235010.5873508,"call_oi":422,"put_oi":1614},{"strike":41050.0,"call_gex_1pct":5795721.7018180555,"put_gex_1pct":-8053970.181225241,"net_gex_1pct":-2258248.4794071857,"gross_gex_1pct":13849691.883043297,"call_oi":32,"put_oi":55},{"strike":41100.0,"call_gex_1pct":6249964.949498054,"put_gex_1pct":-24044722.24652669,"net_gex_1pct":-17794757.297028635,"gross_gex_1pct":30294687.196024742,"call_oi":34,"put_oi":164},{"strike":41150.0,"call_gex_1pct":2779737.469821199,"put_gex_1pct":-7717631.270378225,"net_gex_1pct":-4937893.800557026,"gross_gex_1pct":10497368.740199424,"call_oi":15,"put_oi":52},{"strike":41200.0,"call_gex_1pct":13909040.616458965,"put_gex_1pct":-25866801.079371277,"net_gex_1pct":-11957760.462912312,"gross_gex_1pct":39775841.69583024,"call_oi":76,"put_oi":176},{"strike":41250.0,"call_gex_1pct":4731841.764553888,"put_gex_1pct":-10006064.891134068,"net_gex_1pct":-5274223.126580181,"gross_gex_1pct":14737906.655687956,"call_oi":26,"put_oi":68},{"strike":41300.0,"call_gex_1pct":12390154.689519309,"put_gex_1pct":-63297987.7549664,"net_gex_1pct":-50907833.06544709,"gross_gex_1pct":75688142.44448571,"call_oi":68,"put_oi":432},{"strike":41350.0,"call_gex_1pct":7843926.438188155,"put_gex_1pct":-13569928.852568222,"net_gex_1pct":-5726002.414380067,"gross_gex_1pct":21413855.29075638,"call_oi":43,"put_oi":92},{"strike":41400.0,"call_gex_1pct":7747876.216742978,"put_gex_1pct":-39360702.46240861,"net_gex_1pct":-31612826.245665632,"gross_gex_1pct":47108578.67915159,"call_oi":43,"put_oi":268},{"strike":41450.0,"call_gex_1pct":6536904.716322725,"put_gex_1pct":-14185372.845011296,"net_gex_1pct":-7648468.128688571,"gross_gex_1pct":20722277.56133402,"call_oi":36,"put_oi":97},{"strike":41500.0,"call_gex_1pct":38791610.349051155,"put_gex_1pct":-222501539.14984235,"net_gex_1pct":-183709928.8007912,"gross_gex_1pct":261293149.4988935,"call_oi":212,"put_oi":1528},{"strike":41550.0,"call_gex_1pct":5219449.435899959,"put_gex_1pct":-9424535.294043038,"net_gex_1pct":-4205085.858143079,"gross_gex_1pct":14643984.729942996,"call_oi":29,"put_oi":65},{"strike":41600.0,"call_gex_1pct":12770944.738749795,"put_gex_1pct":-31810503.529243402,"net_gex_1pct":-19039558.790493608,"gross_gex_1pct":44581448.2679932,"call_oi":71,"put_oi":218},{"strike":41650.0,"call_gex_1pct":7658125.538712991,"put_gex_1pct":-26295459.63255484,"net_gex_1pct":-18637334.09384185,"gross_gex_1pct":33953585.17126783,"call_oi":43,"put_oi":181},{"strike":41700.0,"call_gex_1pct":18826037.510234118,"put_gex_1pct":-33203391.769811366,"net_gex_1pct":-14377354.259577248,"gross_gex_1pct":52029429.28004548,"call_oi":108,"put_oi":232},{"strike":41750.0,"call_gex_1pct":6491864.862777138,"put_gex_1pct":-8264210.038836399,"net_gex_1pct":-1772345.176059261,"gross_gex_1pct":14756074.901613537,"call_oi":37,"put_oi":58},{"strike":41800.0,"call_gex_1pct":32814377.280305386,"put_gex_1pct":-46384392.18978178,"net_gex_1pct":-13570014.909476392,"gross_gex_1pct":79198769.47008717,"call_oi":188,"put_oi":327},{"strike":41850.0,"call_gex_1pct":9304410.821580471,"put_gex_1pct":-10590126.736667572,"net_gex_1pct":-1285715.9150871001,"gross_gex_1pct":19894537.558248043,"call_oi":54,"put_oi":75},{"strike":41900.0,"call_gex_1pct":17173151.20409471,"put_gex_1pct":-30608313.204729073,"net_gex_1pct":-13435162.000634361,"gross_gex_1pct":47781464.40882379,"call_oi":100,"put_oi":220},{"strike":41950.0,"call_gex_1pct":9433146.790006759,"put_gex_1pct":-16340299.457608929,"net_gex_1pct":-6907152.66760217,"gross_gex_1pct":25773446.247615688,"call_oi":56,"put_oi":118},{"strike":42000.0,"call_gex_1pct":139444755.04076356,"put_gex_1pct":-268826897.1809245,"net_gex_1pct":-129382142.14016092,"gross_gex_1pct":408271652.22168803,"call_oi":839,"put_oi":1970},{"strike":42050.0,"call_gex_1pct":9251621.839620218,"put_gex_1pct":-10727862.090131983,"net_gex_1pct":-1476240.2505117655,"gross_gex_1pct":19979483.9297522,"call_oi":57,"put_oi":79},{"strike":42100.0,"call_gex_1pct":25059982.529077116,"put_gex_1pct":-34723380.15172375,"net_gex_1pct":-9663397.622646634,"gross_gex_1pct":59783362.68080087,"call_oi":155,"put_oi":257},{"strike":42150.0,"call_gex_1pct":13561403.628289076,"put_gex_1pct":-7988415.530516113,"net_gex_1pct":5572988.097772962,"gross_gex_1pct":21549819.158805188,"call_oi":85,"put_oi":60},{"strike":42200.0,"call_gex_1pct":51929454.41050563,"put_gex_1pct":-27942022.599895872,"net_gex_1pct":23987431.810609758,"gross_gex_1pct":79871477.0104015,"call_oi":331,"put_oi":211},{"strike":42250.0,"call_gex_1pct":18181654.260447133,"put_gex_1pct":-20487242.53183562,"net_gex_1pct":-2305588.271388486,"gross_gex_1pct":38668896.79228275,"call_oi":117,"put_oi":157},{"strike":42300.0,"call_gex_1pct":26366245.04455319,"put_gex_1pct":-55295422.42545144,"net_gex_1pct":-28929177.380898252,"gross_gex_1pct":81661667.47000463,"call_oi":174,"put_oi":430},{"strike":42350.0,"call_gex_1pct":10574621.042767141,"put_gex_1pct":-8053291.1556411,"net_gex_1pct":2521329.8871260406,"gross_gex_1pct":18627912.198408242,"call_oi":71,"put_oi":63},{"strike":42400.0,"call_gex_1pct":30647324.60363692,"put_gex_1pct":-33755597.79412298,"net_gex_1pct":-3108273.1904860586,"gross_gex_1pct":64402922.3977599,"call_oi":210,"put_oi":268},{"strike":42450.0,"call_gex_1pct":17487417.2629564,"put_gex_1pct":-7942846.799157412,"net_gex_1pct":9544570.463798989,"gross_gex_1pct":25430264.06211381,"call_oi":122,"put_oi":64},{"strike":42500.0,"call_gex_1pct":144718397.60578948,"put_gex_1pct":-158606641.69213718,"net_gex_1pct":-13888244.0863477,"gross_gex_1pct":303325039.29792666,"call_oi":1035,"put_oi":1297},{"strike":42550.0,"call_gex_1pct":13967798.234359542,"put_gex_1pct":-10723812.377488129,"net_gex_1pct":3243985.856871413,"gross_gex_1pct":24691610.61184767,"call_oi":102,"put_oi":89},{"strike":42600.0,"call_gex_1pct":54103671.49416351,"put_gex_1pct":-20894626.07973317,"net_gex_1pct":33209045.414430343,"gross_gex_1pct":74998297.57389668,"call_oi":405,"put_oi":176},{"strike":42650.0,"call_gex_1pct":18124830.63538478,"put_gex_1pct":-6784057.043772813,"net_gex_1pct":11340773.591611966,"gross_gex_1pct":24908887.679157592,"call_oi":139,"put_oi":58},{"strike":42700.0,"call_gex_1pct":24936641.479464293,"put_gex_1pct":-20165423.927428983,"net_gex_1pct":4771217.552035309,"gross_gex_1pct":45102065.406893276,"call_oi":196,"put_oi":175},{"strike":42750.0,"call_gex_1pct":13513537.670649093,"put_gex_1pct":-6427285.175209972,"net_gex_1pct":7086252.495439121,"gross_gex_1pct":19940822.845859066,"call_oi":109,"put_oi":57},{"strike":42800.0,"call_gex_1pct":31873622.04549653,"put_gex_1pct":-31218044.978238918,"net_gex_1pct":655577.067257613,"gross_gex_1pct":63091667.02373545,"call_oi":264,"put_oi":281},{"strike":42850.0,"call_gex_1pct":9504944.40085968,"put_gex_1pct":-14337165.600895701,"net_gex_1pct":-4832221.200036021,"gross_gex_1pct":23842110.00175538,"call_oi":81,"put_oi":131},{"strike":42900.0,"call_gex_1pct":25587027.885171853,"put_gex_1pct":-53589192.20687209,"net_gex_1pct":-28002164.321700238,"gross_gex_1pct":79176220.09204394,"call_oi":224,"put_oi":500},{"strike":42950.0,"call_gex_1pct":9552198.992924333,"put_gex_1pct":-7918922.1407640735,"net_gex_1pct":1633276.8521602591,"gross_gex_1pct":17471121.133688405,"call_oi":86,"put_oi":75},{"strike":43000.0,"call_gex_1pct":384514072.62020373,"put_gex_1pct":-152252549.5097961,"net_gex_1pct":232261523.11040762,"gross_gex_1pct":536766622.1299999,"call_oi":3567,"put_oi":1464},{"strike":43050.0,"call_gex_1pct":13068583.785648335,"put_gex_1pct":-10701048.65973502,"net_gex_1pct":2367535.1259133145,"gross_gex_1pct":23769632.445383355,"call_oi":125,"put_oi":105},{"strike":43100.0,"call_gex_1pct":41155752.17280573,"put_gex_1pct":-84623417.76811223,"net_gex_1pct":-43467665.5953065,"gross_gex_1pct":125779169.94091795,"call_oi":406,"put_oi":847},{"strike":43150.0,"call_gex_1pct":19561874.17856303,"put_gex_1pct":-9191532.283292985,"net_gex_1pct":10370341.895270044,"gross_gex_1pct":28753406.461856015,"call_oi":199,"put_oi":93},{"strike":43200.0,"call_gex_1pct":229452773.25827655,"put_gex_1pct":-23840884.201697126,"net_gex_1pct":205611889.0565794,"gross_gex_1pct":253293657.4599737,"call_oi":2419,"put_oi":246},{"strike":43250.0,"call_gex_1pct":12338719.988697961,"put_gex_1pct":-6487924.953724785,"net_gex_1pct":5850795.034973176,"gross_gex_1pct":18826644.942422748,"call_oi":134,"put_oi":68},{"strike":43300.0,"call_gex_1pct":49597120.40375617,"put_gex_1pct":-26582315.24303913,"net_gex_1pct":23014805.16071704,"gross_gex_1pct":76179435.6467953,"call_oi":553,"put_oi":284},{"strike":43350.0,"call_gex_1pct":13186554.218315814,"put_gex_1pct":-7001690.187568952,"net_gex_1pct":6184864.030746861,"gross_gex_1pct":20188244.405884765,"call_oi":153,"put_oi":76},{"strike":43400.0,"call_gex_1pct":190194012.44407603,"put_gex_1pct":-16003807.152630351,"net_gex_1pct":174190205.29144567,"gross_gex_1pct":206197819.5967064,"call_oi":2293,"put_oi":177},{"strike":43450.0,"call_gex_1pct":14338038.944634173,"put_gex_1pct":-6583789.857851914,"net_gex_1pct":7754249.086782259,"gross_gex_1pct":20921828.802486088,"call_oi":178,"put_oi":74},{"strike":43500.0,"call_gex_1pct":103416902.9807053,"put_gex_1pct":-57565519.20282543,"net_gex_1pct":45851383.77787988,"gross_gex_1pct":160982422.18353075,"call_oi":1326,"put_oi":659},{"strike":43550.0,"call_gex_1pct":7496507.85421528,"put_gex_1pct":-3694802.7984379223,"net_gex_1pct":3801705.055777358,"gross_gex_1pct":11191310.652653202,"call_oi":100,"put_oi":43},{"strike":43600.0,"call_gex_1pct":180313654.18812305,"put_gex_1pct":-15950674.9209694,"net_gex_1pct":164362979.26715365,"gross_gex_1pct":196264329.10909244,"call_oi":2529,"put_oi":189},{"strike":43650.0,"call_gex_1pct":11237359.703256013,"put_gex_1pct":-4974884.441908325,"net_gex_1pct":6262475.261347688,"gross_gex_1pct":16212244.145164337,"call_oi":162,"put_oi":60},{"strike":43700.0,"call_gex_1pct":40566633.1961758,"put_gex_1pct":-22992173.95414664,"net_gex_1pct":17574459.24202916,"gross_gex_1pct":63558807.15032244,"call_oi":601,"put_oi":282},{"strike":43750.0,"call_gex_1pct":13270561.002842316,"put_gex_1pct":-5208415.746983916,"net_gex_1pct":8062145.255858401,"gross_gex_1pct":18478976.74982623,"call_oi":204,"put_oi":65},{"strike":43800.0,"call_gex_1pct":129226046.39354812,"put_gex_1pct":-22607211.293502573,"net_gex_1pct":106618835.10004555,"gross_gex_1pct":151833257.6870507,"call_oi":2100,"put_oi":287},{"strike":43850.0,"call_gex_1pct":16336812.876052538,"put_gex_1pct":-13941792.502284084,"net_gex_1pct":2395020.3737684544,"gross_gex_1pct":30278605.378336623,"call_oi":274,"put_oi":180},{"strike":43900.0,"call_gex_1pct":31260404.53604275,"put_gex_1pct":-17282545.70462107,"net_gex_1pct":13977858.83142168,"gross_gex_1pct":48542950.24066382,"call_oi":545,"put_oi":227},{"strike":43950.0,"call_gex_1pct":17400931.53251207,"put_gex_1pct":-7862877.88180146,"net_gex_1pct":9538053.650710609,"gross_gex_1pct":25263809.41431353,"call_oi":317,"put_oi":105},{"strike":44000.0,"call_gex_1pct":287804626.32091945,"put_gex_1pct":-115075952.7737652,"net_gex_1pct":172728673.54715425,"gross_gex_1pct":402880579.09468466,"call_oi":5357,"put_oi":1562},{"strike":44050.0,"call_gex_1pct":14592153.746014073,"put_gex_1pct":-6234641.371004961,"net_gex_1pct":8357512.375009112,"gross_gex_1pct":20826795.117019035,"call_oi":282,"put_oi":86},{"strike":44100.0,"call_gex_1pct":67606672.81647983,"put_gex_1pct":-14270789.025093982,"net_gex_1pct":53335883.79138585,"gross_gex_1pct":81877461.84157382,"call_oi":1358,"put_oi":200},{"strike":44150.0,"call_gex_1pct":9459881.637086013,"put_gex_1pct":-2247842.409613456,"net_gex_1pct":7212039.227472557,"gross_gex_1pct":11707724.04669947,"call_oi":194,"put_oi":32},{"strike":44200.0,"call_gex_1pct":30158808.49869692,"put_gex_1pct":-7385051.21245382,"net_gex_1pct":22773757.2862431,"gross_gex_1pct":37543859.711150736,"call_oi":672,"put_oi":107},{"strike":44250.0,"call_gex_1pct":11771069.366299413,"put_gex_1pct":-3534097.0297945687,"net_gex_1pct":8236972.336504845,"gross_gex_1pct":15305166.396093981,"call_oi":278,"put_oi":52},{"strike":44300.0,"call_gex_1pct":25189857.249119297,"put_gex_1pct":-9371212.602579411,"net_gex_1pct":15818644.646539886,"gross_gex_1pct":34561069.85169871,"call_oi":620,"put_oi":140},{"strike":44350.0,"call_gex_1pct":11533676.622522986,"put_gex_1pct":-1708818.1298300463,"net_gex_1pct":9824858.49269294,"gross_gex_1pct":13242494.752353031,"call_oi":294,"put_oi":26},{"strike":44400.0,"call_gex_1pct":25804068.104700398,"put_gex_1pct":-11201074.65026387,"net_gex_1pct":14602993.454436528,"gross_gex_1pct":37005142.75496427,"call_oi":671,"put_oi":173},{"strike":44450.0,"call_gex_1pct":12820744.367871938,"put_gex_1pct":-1594875.595754919,"net_gex_1pct":11225868.772117019,"gross_gex_1pct":14415619.963626858,"call_oi":340,"put_oi":25},{"strike":44500.0,"call_gex_1pct":69974848.13128142,"put_gex_1pct":-15403031.47691983,"net_gex_1pct":54571816.65436159,"gross_gex_1pct":85377879.60820125,"call_oi":1938,"put_oi":245},{"strike":44550.0,"call_gex_1pct":12559689.887361314,"put_gex_1pct":-309842.92836698546,"net_gex_1pct":12249846.958994329,"gross_gex_1pct":12869532.8157283,"call_oi":382,"put_oi":5},{"strike":44600.0,"call_gex_1pct":29341078.036199085,"put_gex_1pct":-13440084.688003974,"net_gex_1pct":15900993.348195111,"gross_gex_1pct":42781162.72420306,"call_oi":940,"put_oi":220},{"strike":44650.0,"call_gex_1pct":13291208.511191264,"put_gex_1pct":-602367.4979744094,"net_gex_1pct":12688841.013216855,"gross_gex_1pct":13893576.009165673,"call_oi":434,"put_oi":10},{"strike":44700.0,"call_gex_1pct":25276020.71977797,"put_gex_1pct":-8197766.5152489105,"net_gex_1pct":17078254.204529062,"gross_gex_1pct":33473787.23502688,"call_oi":841,"put_oi":138},{"strike":44750.0,"call_gex_1pct":8980806.545636706,"put_gex_1pct":-1113258.5171048841,"net_gex_1pct":7867548.028531821,"gross_gex_1pct":10094065.06274159,"call_oi":308,"put_oi":19},{"strike":44800.0,"call_gex_1pct":18408244.94396784,"put_gex_1pct":-6300344.626202137,"net_gex_1pct":12107900.317765705,"gross_gex_1pct":24708589.570169978,"call_oi":643,"put_oi":109},{"strike":44850.0,"call_gex_1pct":5110534.256511676,"put_gex_1pct":-56715.01271402193,"net_gex_1pct":5053819.243797654,"gross_gex_1pct":5167249.269225698,"call_oi":184,"put_oi":1},{"strike":44900.0,"call_gex_1pct":9484988.68706544,"put_gex_1pct":-13709875.416501272,"net_gex_1pct":-4224886.729435833,"gross_gex_1pct":23194864.103566714,"call_oi":390,"put_oi":245},{"strike":44950.0,"call_gex_1pct":5744134.794562034,"put_gex_1pct":0.0,"net_gex_1pct":5744134.794562034,"gross_gex_1pct":5744134.794562034,"call_oi":249,"put_oi":0},{"strike":45000.0,"call_gex_1pct":98099683.73275973,"put_gex_1pct":-44581601.0225031,"net_gex_1pct":53518082.71025663,"gross_gex_1pct":142681284.75526282,"call_oi":4329,"put_oi":818},{"strike":45050.0,"call_gex_1pct":3373605.1408450603,"put_gex_1pct":0.0,"net_gex_1pct":3373605.1408450603,"gross_gex_1pct":3373605.1408450603,"call_oi":172,"put_oi":0},{"strike":45100.0,"call_gex_1pct":10935317.336069744,"put_gex_1pct":-10622321.37212657,"net_gex_1pct":312995.9639431741,"gross_gex_1pct":21557638.708196312,"call_oi":582,"put_oi":200},{"strike":45150.0,"call_gex_1pct":4228089.538584382,"put_gex_1pct":0.0,"net_gex_1pct":4228089.538584382,"gross_gex_1pct":4228089.538584382,"call_oi":229,"put_oi":0},{"strike":45200.0,"call_gex_1pct":11295988.262321776,"put_gex_1pct":-5800107.8073641835,"net_gex_1pct":5495880.454957592,"gross_gex_1pct":17096096.06968596,"call_oi":658,"put_oi":112},{"strike":45250.0,"call_gex_1pct":4176884.691643611,"put_gex_1pct":-102293.908140649,"net_gex_1pct":4074590.783502962,"gross_gex_1pct":4279178.59978426,"call_oi":249,"put_oi":2},{"strike":45300.0,"call_gex_1pct":11130728.613470642,"put_gex_1pct":-6719389.876778334,"net_gex_1pct":4411338.7366923075,"gross_gex_1pct":17850118.49024898,"call_oi":679,"put_oi":133},{"strike":45350.0,"call_gex_1pct":3389645.28354577,"put_gex_1pct":0.0,"net_gex_1pct":3389645.28354577,"gross_gex_1pct":3389645.28354577,"call_oi":217,"put_oi":0},{"strike":45400.0,"call_gex_1pct":12280191.991743786,"put_gex_1pct":-4843642.267013084,"net_gex_1pct":7436549.724730702,"gross_gex_1pct":17123834.25875687,"call_oi":810,"put_oi":99},{"strike":45450.0,"call_gex_1pct":1579789.1898537097,"put_gex_1pct":-48339.93718392253,"net_gex_1pct":1531449.252669787,"gross_gex_1pct":1628129.1270376323,"call_oi":113,"put_oi":1},{"strike":45500.0,"call_gex_1pct":20184765.87608329,"put_gex_1pct":-13470306.262892276,"net_gex_1pct":6714459.613191012,"gross_gex_1pct":33655072.13897556,"call_oi":1515,"put_oi":282},{"strike":45550.0,"call_gex_1pct":2097345.9757404733,"put_gex_1pct":-94413.18829938844,"net_gex_1pct":2002932.7874410849,"gross_gex_1pct":2191759.164039862,"call_oi":160,"put_oi":2},{"strike":45600.0,"call_gex_1pct":9020670.352439655,"put_gex_1pct":-9938196.916314721,"net_gex_1pct":-917526.5638750661,"gross_gex_1pct":18958867.268754378,"call_oi":797,"put_oi":213},{"strike":45700.0,"call_gex_1pct":8285210.074698236,"put_gex_1pct":-5517129.686497542,"net_gex_1pct":2768080.3882006938,"gross_gex_1pct":13802339.761195779,"call_oi":764,"put_oi":121},{"strike":45800.0,"call_gex_1pct":8025915.660628707,"put_gex_1pct":-7087898.352142882,"net_gex_1pct":938017.3084858255,"gross_gex_1pct":15113814.012771588,"call_oi":809,"put_oi":159},{"strike":45900.0,"call_gex_1pct":4949599.889222604,"put_gex_1pct":-5406549.815105514,"net_gex_1pct":-456949.92588290945,"gross_gex_1pct":10356149.704328118,"call_oi":669,"put_oi":124},{"strike":46000.0,"call_gex_1pct":58500129.636066705,"put_gex_1pct":-10495200.637599219,"net_gex_1pct":48004928.99846749,"gross_gex_1pct":68995330.27366592,"call_oi":9318,"put_oi":246},{"strike":46100.0,"call_gex_1pct":8217444.992270604,"put_gex_1pct":-1670495.7080296383,"net_gex_1pct":6546949.284240966,"gross_gex_1pct":9887940.700300243,"call_oi":1554,"put_oi":40},{"strike":46200.0,"call_gex_1pct":2399436.2926286766,"put_gex_1pct":-3966920.227415304,"net_gex_1pct":-1567483.9347866275,"gross_gex_1pct":6366356.52004398,"call_oi":540,"put_oi":97},{"strike":46300.0,"call_gex_1pct":3233291.9854843337,"put_gex_1pct":-6890765.664690853,"net_gex_1pct":-3657473.6792065194,"gross_gex_1pct":10124057.650175188,"call_oi":859,"put_oi":172},{"strike":46400.0,"call_gex_1pct":2041024.8063502905,"put_gex_1pct":-3572673.0450776787,"net_gex_1pct":-1531648.2387273882,"gross_gex_1pct":5613697.8514279695,"call_oi":624,"put_oi":91},{"strike":46500.0,"call_gex_1pct":11101006.81970435,"put_gex_1pct":-4810887.045811496,"net_gex_1pct":6290119.773892854,"gross_gex_1pct":15911893.865515847,"call_oi":3724,"put_oi":125},{"strike":46600.0,"call_gex_1pct":2199569.4478326878,"put_gex_1pct":-1698386.2764415825,"net_gex_1pct":501183.1713911053,"gross_gex_1pct":3897955.7242742702,"call_oi":759,"put_oi":45},{"strike":46700.0,"call_gex_1pct":997861.2882528172,"put_gex_1pct":-2406506.4541125013,"net_gex_1pct":-1408645.165859684,"gross_gex_1pct":3404367.7423653184,"call_oi":354,"put_oi":65},{"strike":46800.0,"call_gex_1pct":1300580.5479236091,"put_gex_1pct":-2506738.1269354755,"net_gex_1pct":-1206157.5790118664,"gross_gex_1pct":3807318.6748590847,"call_oi":552,"put_oi":69},{"strike":46900.0,"call_gex_1pct":1244714.8436532945,"put_gex_1pct":-3245037.6699786084,"net_gex_1pct":-2000322.826325314,"gross_gex_1pct":4489752.513631903,"call_oi":595,"put_oi":91},{"strike":47000.0,"call_gex_1pct":6195145.2387685,"put_gex_1pct":-8017898.6171533745,"net_gex_1pct":-1822753.3783848742,"gross_gex_1pct":14213043.855921876,"call_oi":3385,"put_oi":229},{"strike":47100.0,"call_gex_1pct":685531.044333941,"put_gex_1pct":-928453.1324020774,"net_gex_1pct":-242922.08806813648,"gross_gex_1pct":1613984.1767360184,"call_oi":437,"put_oi":27},{"strike":47200.0,"call_gex_1pct":567194.4648119196,"put_gex_1pct":-8850940.176455414,"net_gex_1pct":-8283745.711643495,"gross_gex_1pct":9418134.641267333,"call_oi":371,"put_oi":262},{"strike":47300.0,"call_gex_1pct":1523389.4190461915,"put_gex_1pct":-1294678.2631251926,"net_gex_1pct":228711.1559209989,"gross_gex_1pct":2818067.682171384,"call_oi":1022,"put_oi":39},{"strike":47400.0,"call_gex_1pct":252985.0462519741,"put_gex_1pct":-358932.6444912404,"net_gex_1pct":-105947.59823926628,"gross_gex_1pct":611917.6907432145,"call_oi":174,"put_oi":11},{"strike":47500.0,"call_gex_1pct":11171319.50792449,"put_gex_1pct":-2919411.852204018,"net_gex_1pct":8251907.655720472,"gross_gex_1pct":14090731.360128507,"call_oi":7874,"put_oi":91},{"strike":47600.0,"call_gex_1pct":198052.81219821406,"put_gex_1pct":-1230438.4177509192,"net_gex_1pct":-1032385.6055527052,"gross_gex_1pct":1428491.2299491332,"call_oi":143,"put_oi":39},{"strike":47700.0,"call_gex_1pct":231889.53082666508,"put_gex_1pct":-527582.216749709,"net_gex_1pct":-295692.6859230439,"gross_gex_1pct":759471.7475763741,"call_oi":201,"put_oi":17},{"strike":47800.0,"call_gex_1pct":498108.9774480477,"put_gex_1pct":-549618.7049395131,"net_gex_1pct":-51509.7274914654,"gross_gex_1pct":1047727.6823875608,"call_oi":442,"put_oi":18},{"strike":47900.0,"call_gex_1pct":505463.97056657233,"put_gex_1pct":-450741.07507836825,"net_gex_1pct":54722.895488204085,"gross_gex_1pct":956205.0456449406,"call_oi":459,"put_oi":15},{"strike":48000.0,"call_gex_1pct":5455610.734224476,"put_gex_1pct":-2514190.4831059948,"net_gex_1pct":2941420.251118481,"gross_gex_1pct":7969801.217330471,"call_oi":5068,"put_oi":85},{"strike":48100.0,"call_gex_1pct":220004.5977047543,"put_gex_1pct":-436825.39504356915,"net_gex_1pct":-216820.79733881485,"gross_gex_1pct":656829.9927483235,"call_oi":209,"put_oi":15},{"strike":48200.0,"call_gex_1pct":209028.48206818072,"put_gex_1pct":-802977.9136850738,"net_gex_1pct":-593949.4316168932,"gross_gex_1pct":1012006.3957532545,"call_oi":203,"put_oi":28},{"strike":48300.0,"call_gex_1pct":204536.42412927502,"put_gex_1pct":-310710.8851779479,"net_gex_1pct":-106174.46104867285,"gross_gex_1pct":515247.3093072229,"call_oi":203,"put_oi":11},{"strike":48400.0,"call_gex_1pct":173576.0723090065,"put_gex_1pct":-361753.20271625597,"net_gex_1pct":-188177.13040724947,"gross_gex_1pct":535329.2750252625,"call_oi":176,"put_oi":13},{"strike":48500.0,"call_gex_1pct":3141213.7729127207,"put_gex_1pct":-2056460.7872938944,"net_gex_1pct":1084752.9856188262,"gross_gex_1pct":5197674.560206615,"call_oi":3253,"put_oi":75},{"strike":48600.0,"call_gex_1pct":88286.96560604704,"put_gex_1pct":-378320.7490465919,"net_gex_1pct":-290033.78344054485,"gross_gex_1pct":466607.714652639,"call_oi":115,"put_oi":14},{"strike":48700.0,"call_gex_1pct":67683.60941008454,"put_gex_1pct":-399555.5478026983,"net_gex_1pct":-331871.9383926137,"gross_gex_1pct":467239.1572127828,"call_oi":90,"put_oi":15},{"strike":48800.0,"call_gex_1pct":70005.32391884281,"put_gex_1pct":-551490.3079994821,"net_gex_1pct":-481484.9840806393,"gross_gex_1pct":621495.631918325,"call_oi":95,"put_oi":21},{"strike":48900.0,"call_gex_1pct":31779.54196129037,"put_gex_1pct":-440227.5753778748,"net_gex_1pct":-408448.0334165844,"gross_gex_1pct":472007.1173391651,"call_oi":44,"put_oi":17},{"strike":49000.0,"call_gex_1pct":838401.6406206039,"put_gex_1pct":-1098200.8284302119,"net_gex_1pct":-259799.18780960795,"gross_gex_1pct":1936602.4690508158,"call_oi":1184,"put_oi":43},{"strike":49100.0,"call_gex_1pct":30554.386836766495,"put_gex_1pct":-377887.9910506547,"net_gex_1pct":-347333.6042138882,"gross_gex_1pct":408442.3778874212,"call_oi":44,"put_oi":15},{"strike":49200.0,"call_gex_1pct":59942.689740244256,"put_gex_1pct":-347960.7421511076,"net_gex_1pct":-288018.05241086334,"gross_gex_1pct":407903.4318913518,"call_oi":88,"put_oi":14},{"strike":49300.0,"call_gex_1pct":54135.31571050187,"put_gex_1pct":-416919.0729911551,"net_gex_1pct":-362783.7572806532,"gross_gex_1pct":471054.38870165695,"call_oi":81,"put_oi":17},{"strike":49400.0,"call_gex_1pct":52472.83709253514,"put_gex_1pct":-314641.14407960983,"net_gex_1pct":-262168.30698707467,"gross_gex_1pct":367113.981172145,"call_oi":80,"put_oi":13},{"strike":49500.0,"call_gex_1pct":231149.0807821804,"put_gex_1pct":-334454.2316165437,"net_gex_1pct":-103305.15083436333,"gross_gex_1pct":565603.3123987241,"call_oi":359,"put_oi":14},{"strike":49600.0,"call_gex_1pct":73334.89545971731,"put_gex_1pct":-188669.13919402362,"net_gex_1pct":-115334.2437343063,"gross_gex_1pct":262004.03465374094,"call_oi":116,"put_oi":8},{"strike":49700.0,"call_gex_1pct":45324.179020365984,"put_gex_1pct":-325990.8788069076,"net_gex_1pct":-280666.69978654163,"gross_gex_1pct":371315.0578272736,"call_oi":73,"put_oi":14},{"strike":49800.0,"call_gex_1pct":51841.49924277009,"put_gex_1pct":-1862481.2433000032,"net_gex_1pct":-1810639.7440572332,"gross_gex_1pct":1914322.7425427733,"call_oi":85,"put_oi":81},{"strike":49900.0,"call_gex_1pct":262469.7207712595,"put_gex_1pct":-1566920.9077996442,"net_gex_1pct":-1304451.1870283848,"gross_gex_1pct":1829390.6285709036,"call_oi":438,"put_oi":69},{"strike":50000.0,"call_gex_1pct":1590040.2844608577,"put_gex_1pct":-1054258.9005333572,"net_gex_1pct":535781.3839275006,"gross_gex_1pct":2644299.184994215,"call_oi":2700,"put_oi":47},{"strike":50100.0,"call_gex_1pct":80461.6907365348,"put_gex_1pct":-509668.4879090692,"net_gex_1pct":-429206.7971725344,"gross_gex_1pct":590130.178645604,"call_oi":139,"put_oi":23},{"strike":50200.0,"call_gex_1pct":125772.39894487934,"put_gex_1pct":-481671.6056303005,"net_gex_1pct":-355899.2066854211,"gross_gex_1pct":607444.0045751798,"call_oi":221,"put_oi":22},{"strike":50300.0,"call_gex_1pct":30219.852461988754,"put_gex_1pct":-173078.64688000304,"net_gex_1pct":-142858.7944180143,"gross_gex_1pct":203298.4993419918,"call_oi":54,"put_oi":8},{"strike":50400.0,"call_gex_1pct":39079.352288500646,"put_gex_1pct":0.0,"net_gex_1pct":39079.352288500646,"gross_gex_1pct":39079.352288500646,"call_oi":71,"put_oi":0},{"strike":50500.0,"call_gex_1pct":126659.89803465408,"put_gex_1pct":-21133.403576006185,"net_gex_1pct":105526.4944586479,"gross_gex_1pct":147793.30161066027,"call_oi":316,"put_oi":1},{"strike":50600.0,"call_gex_1pct":22870.935041310684,"put_gex_1pct":0.0,"net_gex_1pct":22870.935041310684,"gross_gex_1pct":22870.935041310684,"call_oi":58,"put_oi":0},{"strike":50700.0,"call_gex_1pct":5432.104617706426,"put_gex_1pct":0.0,"net_gex_1pct":5432.104617706426,"gross_gex_1pct":5432.104617706426,"call_oi":14,"put_oi":0},{"strike":50800.0,"call_gex_1pct":17565.5077560207,"put_gex_1pct":0.0,"net_gex_1pct":17565.5077560207,"gross_gex_1pct":17565.5077560207,"call_oi":46,"put_oi":0},{"strike":50900.0,"call_gex_1pct":168391.70247700214,"put_gex_1pct":0.0,"net_gex_1pct":168391.70247700214,"gross_gex_1pct":168391.70247700214,"call_oi":448,"put_oi":0},{"strike":51000.0,"call_gex_1pct":225729.20500319143,"put_gex_1pct":-59916.685673908425,"net_gex_1pct":165812.519329283,"gross_gex_1pct":285645.8906770999,"call_oi":610,"put_oi":3},{"strike":51100.0,"call_gex_1pct":17125.56649445262,"put_gex_1pct":-19754.556785575358,"net_gex_1pct":-2628.9902911227364,"gross_gex_1pct":36880.12328002798,"call_oi":47,"put_oi":1},{"strike":51200.0,"call_gex_1pct":18301.171514191174,"put_gex_1pct":0.0,"net_gex_1pct":18301.171514191174,"gross_gex_1pct":18301.171514191174,"call_oi":51,"put_oi":0},{"strike":51300.0,"call_gex_1pct":7776.139586220026,"put_gex_1pct":0.0,"net_gex_1pct":7776.139586220026,"gross_gex_1pct":7776.139586220026,"call_oi":22,"put_oi":0},{"strike":51400.0,"call_gex_1pct":11142.782006899017,"put_gex_1pct":0.0,"net_gex_1pct":11142.782006899017,"gross_gex_1pct":11142.782006899017,"call_oi":32,"put_oi":0},{"strike":51500.0,"call_gex_1pct":49405.66227751774,"put_gex_1pct":0.0,"net_gex_1pct":49405.66227751774,"gross_gex_1pct":49405.66227751774,"call_oi":144,"put_oi":0},{"strike":51600.0,"call_gex_1pct":20181.306650247734,"put_gex_1pct":-18731.31816208781,"net_gex_1pct":1449.9884881599246,"gross_gex_1pct":38912.62481233555,"call_oi":101,"put_oi":1},{"strike":51700.0,"call_gex_1pct":11026.821639173937,"put_gex_1pct":0.0,"net_gex_1pct":11026.821639173937,"gross_gex_1pct":11026.821639173937,"call_oi":56,"put_oi":0},{"strike":51800.0,"call_gex_1pct":15913.870750910244,"put_gex_1pct":0.0,"net_gex_1pct":15913.870750910244,"gross_gex_1pct":15913.870750910244,"call_oi":82,"put_oi":0},{"strike":51900.0,"call_gex_1pct":8034.797445025838,"put_gex_1pct":0.0,"net_gex_1pct":8034.797445025838,"gross_gex_1pct":8034.797445025838,"call_oi":42,"put_oi":0},{"strike":52000.0,"call_gex_1pct":122781.55537987134,"put_gex_1pct":0.0,"net_gex_1pct":122781.55537987134,"gross_gex_1pct":122781.55537987134,"call_oi":651,"put_oi":0},{"strike":52100.0,"call_gex_1pct":6880.849261055699,"put_gex_1pct":0.0,"net_gex_1pct":6880.849261055699,"gross_gex_1pct":6880.849261055699,"call_oi":37,"put_oi":0},{"strike":52200.0,"call_gex_1pct":10636.948259844068,"put_gex_1pct":0.0,"net_gex_1pct":10636.948259844068,"gross_gex_1pct":10636.948259844068,"call_oi":58,"put_oi":0},{"strike":52300.0,"call_gex_1pct":7777.960003146289,"put_gex_1pct":0.0,"net_gex_1pct":7777.960003146289,"gross_gex_1pct":7777.960003146289,"call_oi":43,"put_oi":0},{"strike":52400.0,"call_gex_1pct":4460.708619146676,"put_gex_1pct":0.0,"net_gex_1pct":4460.708619146676,"gross_gex_1pct":4460.708619146676,"call_oi":25,"put_oi":0},{"strike":52500.0,"call_gex_1pct":19715.410791042807,"put_gex_1pct":0.0,"net_gex_1pct":19715.410791042807,"gross_gex_1pct":19715.410791042807,"call_oi":112,"put_oi":0},{"strike":52600.0,"call_gex_1pct":8163.304242578964,"put_gex_1pct":0.0,"net_gex_1pct":8163.304242578964,"gross_gex_1pct":8163.304242578964,"call_oi":47,"put_oi":0},{"strike":52700.0,"call_gex_1pct":5998.903274799317,"put_gex_1pct":0.0,"net_gex_1pct":5998.903274799317,"gross_gex_1pct":5998.903274799317,"call_oi":35,"put_oi":0},{"strike":52800.0,"call_gex_1pct":3721.4878226026694,"put_gex_1pct":0.0,"net_gex_1pct":3721.4878226026694,"gross_gex_1pct":3721.4878226026694,"call_oi":22,"put_oi":0},{"strike":52900.0,"call_gex_1pct":5176.058835836515,"put_gex_1pct":0.0,"net_gex_1pct":5176.058835836515,"gross_gex_1pct":5176.058835836515,"call_oi":31,"put_oi":0},{"strike":53000.0,"call_gex_1pct":235870.32547605596,"put_gex_1pct":0.0,"net_gex_1pct":235870.32547605596,"gross_gex_1pct":235870.32547605596,"call_oi":1431,"put_oi":0},{"strike":53100.0,"call_gex_1pct":6346.6730755124345,"put_gex_1pct":0.0,"net_gex_1pct":6346.6730755124345,"gross_gex_1pct":6346.6730755124345,"call_oi":39,"put_oi":0},{"strike":53200.0,"call_gex_1pct":4017.1698904848454,"put_gex_1pct":0.0,"net_gex_1pct":4017.1698904848454,"gross_gex_1pct":4017.1698904848454,"call_oi":25,"put_oi":0},{"strike":53300.0,"call_gex_1pct":2697.601275744416,"put_gex_1pct":0.0,"net_gex_1pct":2697.601275744416,"gross_gex_1pct":2697.601275744416,"call_oi":17,"put_oi":0},{"strike":53400.0,"call_gex_1pct":10813.735145512546,"put_gex_1pct":0.0,"net_gex_1pct":10813.735145512546,"gross_gex_1pct":10813.735145512546,"call_oi":69,"put_oi":0},{"strike":53500.0,"call_gex_1pct":20433.6862355587,"put_gex_1pct":0.0,"net_gex_1pct":20433.6862355587,"gross_gex_1pct":20433.6862355587,"call_oi":132,"put_oi":0},{"strike":53600.0,"call_gex_1pct":3211.3363996947833,"put_gex_1pct":0.0,"net_gex_1pct":3211.3363996947833,"gross_gex_1pct":3211.3363996947833,"call_oi":21,"put_oi":0},{"strike":53700.0,"call_gex_1pct":8762.641012204858,"put_gex_1pct":0.0,"net_gex_1pct":8762.641012204858,"gross_gex_1pct":8762.641012204858,"call_oi":58,"put_oi":0},{"strike":53800.0,"call_gex_1pct":4179.762742223536,"put_gex_1pct":0.0,"net_gex_1pct":4179.762742223536,"gross_gex_1pct":4179.762742223536,"call_oi":28,"put_oi":0},{"strike":53900.0,"call_gex_1pct":2360.181914736628,"put_gex_1pct":0.0,"net_gex_1pct":2360.181914736628,"gross_gex_1pct":2360.181914736628,"call_oi":16,"put_oi":0},{"strike":54000.0,"call_gex_1pct":32946.587757563226,"put_gex_1pct":0.0,"net_gex_1pct":32946.587757563226,"gross_gex_1pct":32946.587757563226,"call_oi":226,"put_oi":0},{"strike":54100.0,"call_gex_1pct":1440.8621202338302,"put_gex_1pct":0.0,"net_gex_1pct":1440.8621202338302,"gross_gex_1pct":1440.8621202338302,"call_oi":10,"put_oi":0},{"strike":54200.0,"call_gex_1pct":2136.37426611283,"put_gex_1pct":0.0,"net_gex_1pct":2136.37426611283,"gross_gex_1pct":2136.37426611283,"call_oi":15,"put_oi":0},{"strike":54300.0,"call_gex_1pct":2815.932873683932,"put_gex_1pct":0.0,"net_gex_1pct":2815.932873683932,"gross_gex_1pct":2815.932873683932,"call_oi":20,"put_oi":0},{"strike":54400.0,"call_gex_1pct":2644.8073589108762,"put_gex_1pct":0.0,"net_gex_1pct":2644.8073589108762,"gross_gex_1pct":2644.8073589108762,"call_oi":19,"put_oi":0},{"strike":54500.0,"call_gex_1pct":7845.212711750368,"put_gex_1pct":0.0,"net_gex_1pct":7845.212711750368,"gross_gex_1pct":7845.212711750368,"call_oi":57,"put_oi":0},{"strike":54600.0,"call_gex_1pct":2449.8103089242686,"put_gex_1pct":0.0,"net_gex_1pct":2449.8103089242686,"gross_gex_1pct":2449.8103089242686,"call_oi":18,"put_oi":0},{"strike":54700.0,"call_gex_1pct":3095.6932986645916,"put_gex_1pct":0.0,"net_gex_1pct":3095.6932986645916,"gross_gex_1pct":3095.6932986645916,"call_oi":23,"put_oi":0},{"strike":54800.0,"call_gex_1pct":1064.9511209397378,"put_gex_1pct":0.0,"net_gex_1pct":1064.9511209397378,"gross_gex_1pct":1064.9511209397378,"call_oi":8,"put_oi":0},{"strike":54900.0,"call_gex_1pct":3291.7600544741013,"put_gex_1pct":0.0,"net_gex_1pct":3291.7600544741013,"gross_gex_1pct":3291.7600544741013,"call_oi":25,"put_oi":0},{"strike":55000.0,"call_gex_1pct":66427.07360009303,"put_gex_1pct":0.0,"net_gex_1pct":66427.07360009303,"gross_gex_1pct":66427.07360009303,"call_oi":510,"put_oi":0},{"strike":55100.0,"call_gex_1pct":1803.9625325451161,"put_gex_1pct":0.0,"net_gex_1pct":1803.9625325451161,"gross_gex_1pct":1803.9625325451161,"call_oi":14,"put_oi":0},{"strike":55200.0,"call_gex_1pct":509.94249951455436,"put_gex_1pct":0.0,"net_gex_1pct":509.94249951455436,"gross_gex_1pct":509.94249951455436,"call_oi":4,"put_oi":0},{"strike":55300.0,"call_gex_1pct":1513.7037095227167,"put_gex_1pct":0.0,"net_gex_1pct":1513.7037095227167,"gross_gex_1pct":1513.7037095227167,"call_oi":12,"put_oi":0},{"strike":55400.0,"call_gex_1pct":1123.4059018422638,"put_gex_1pct":0.0,"net_gex_1pct":1123.4059018422638,"gross_gex_1pct":1123.4059018422638,"call_oi":9,"put_oi":0},{"strike":55500.0,"call_gex_1pct":1605.8602400664165,"put_gex_1pct":0.0,"net_gex_1pct":1605.8602400664165,"gross_gex_1pct":1605.8602400664165,"call_oi":13,"put_oi":0},{"strike":55600.0,"call_gex_1pct":2078.349847905443,"put_gex_1pct":0.0,"net_gex_1pct":2078.349847905443,"gross_gex_1pct":2078.349847905443,"call_oi":17,"put_oi":0},{"strike":55700.0,"call_gex_1pct":605.0339211737532,"put_gex_1pct":0.0,"net_gex_1pct":605.0339211737532,"gross_gex_1pct":605.0339211737532,"call_oi":5,"put_oi":0},{"strike":55800.0,"call_gex_1pct":958.2390401787644,"put_gex_1pct":0.0,"net_gex_1pct":958.2390401787644,"gross_gex_1pct":958.2390401787644,"call_oi":8,"put_oi":0},{"strike":55900.0,"call_gex_1pct":7351.626143120307,"put_gex_1pct":0.0,"net_gex_1pct":7351.626143120307,"gross_gex_1pct":7351.626143120307,"call_oi":62,"put_oi":0},{"strike":56000.0,"call_gex_1pct":9860.798747265195,"put_gex_1pct":0.0,"net_gex_1pct":9860.798747265195,"gross_gex_1pct":9860.798747265195,"call_oi":84,"put_oi":0},{"strike":56100.0,"call_gex_1pct":5113.983867109035,"put_gex_1pct":0.0,"net_gex_1pct":5113.983867109035,"gross_gex_1pct":5113.983867109035,"call_oi":44,"put_oi":0},{"strike":56200.0,"call_gex_1pct":230.16690641848322,"put_gex_1pct":0.0,"net_gex_1pct":230.16690641848322,"gross_gex_1pct":230.16690641848322,"call_oi":2,"put_oi":0},{"strike":56400.0,"call_gex_1pct":225.70988864787046,"put_gex_1pct":0.0,"net_gex_1pct":225.70988864787046,"gross_gex_1pct":225.70988864787046,"call_oi":2,"put_oi":0},{"strike":56500.0,"call_gex_1pct":1788.3035076375577,"put_gex_1pct":0.0,"net_gex_1pct":1788.3035076375577,"gross_gex_1pct":1788.3035076375577,"call_oi":16,"put_oi":0},{"strike":56600.0,"call_gex_1pct":110.70125726877048,"put_gex_1pct":0.0,"net_gex_1pct":110.70125726877048,"gross_gex_1pct":110.70125726877048,"call_oi":1,"put_oi":0},{"strike":56700.0,"call_gex_1pct":109.65138259743505,"put_gex_1pct":0.0,"net_gex_1pct":109.65138259743505,"gross_gex_1pct":109.65138259743505,"call_oi":1,"put_oi":0},{"strike":56900.0,"call_gex_1pct":5487.778720780686,"put_gex_1pct":0.0,"net_gex_1pct":5487.778720780686,"gross_gex_1pct":5487.778720780686,"call_oi":51,"put_oi":0},{"strike":57000.0,"call_gex_1pct":42002.255852941154,"put_gex_1pct":0.0,"net_gex_1pct":42002.255852941154,"gross_gex_1pct":42002.255852941154,"call_oi":394,"put_oi":0},{"strike":57100.0,"call_gex_1pct":35700.294071247416,"put_gex_1pct":0.0,"net_gex_1pct":35700.294071247416,"gross_gex_1pct":35700.294071247416,"call_oi":338,"put_oi":0},{"strike":57200.0,"call_gex_1pct":53688.282660444296,"put_gex_1pct":0.0,"net_gex_1pct":53688.282660444296,"gross_gex_1pct":53688.282660444296,"call_oi":513,"put_oi":0},{"strike":57300.0,"call_gex_1pct":171734.49225362946,"put_gex_1pct":0.0,"net_gex_1pct":171734.49225362946,"gross_gex_1pct":171734.49225362946,"call_oi":1656,"put_oi":0}]}
```

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
- 資料日期：2026-11-16；本次報告產製時間：2026-11-17 21:32:57；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 覆蓋：79 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-16；估值 1240 檔；5 檔採最近有效收盤價（價格日期 20260402 至 20261116）；Blave 同 T0 交叉驗證 158.5240%；差異 0.068 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；5 檔採最近有效收盤價（價格日期 20260402 至 20261116）。Blave 同 T0 交叉驗證 158.5240%；差異 0.068 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-17，非 T0 2026-11-16)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：跨到期換月（舊202611F2→新202611），日對日 OI/Walls 變化不適用
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -701.9 | -96,787 | -1,144 | +2,317 | +2,000 | +1,743 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -183.0 | +92,406 | -1,180 | +0 | -10,215 | +5 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -259.0 | +1,159 | -1,820 | -706 | -3,750 | -4,032 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
