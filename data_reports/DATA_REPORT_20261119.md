# DATA_REPORT_20261119

- 報告日期：`2026-11-20`
- T0 交易日期：`2026-11-19`
- 首次資料產出時間：`2026-11-20 12:35:47`
- 本次更新開始時間：`2026-11-20 12:35:47`
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

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -243.1 | 億元 | twse-proxy /institutional |
| 投信 | +43.9 | 億元 | twse-proxy /institutional |
| 自營商 | -233.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -432.3 | 億元 | twse-proxy /institutional |

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
- TWSE TWT93U（上市）：資料日期：`20261119`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-20T12:35:59+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261119`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-20T12:36:06+08:00`；狀態：`available_after_schedule`

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
| S&P 500 | ^GSPC | 7,175.83 | -147.80 | -2.02 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,879.20 | -550.68 | -2.25 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,517.05 | -599.21 | -2.21 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 49,097.10 | -1,101.07 | -2.19 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,419.72 | -233.08 | -2.41 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 28.44 | 3.88 | +15.80 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 56,694.08 | -2,750.13 | -4.63 | 2026-11-20 | 2026-11-20T04:36:06+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,891.44 | -246.45 | -4.80 | 2026-11-20 | 2026-11-20T04:36:06+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,451.91 | -389.71 | -1.71 | 2026-11-20 | 2026-11-20T04:36:06+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,521.40 | -56.22 | -1.57 | 2026-11-20 | 2026-11-20T04:36:06+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,365.76 | -217.44 | -2.05 | 2026-11-20 | 2026-11-20T04:36:06+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,169.50 | -27.75 | -0.39 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,407.25 | -193.00 | -0.73 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 49,099.00 | -81.00 | -0.16 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,654.60 | -8.70 | -0.33 | 2026-11-19 | 2026-11-20T04:36:06+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.76 | -0.04 | 19-NOV-26 | 2026-11-20T04:36:27+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.05 | -0.01 | 2026-11-19 | 2026-11-20T04:36:27+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.43 | -0.01 | 19-NOV-26 | 2026-11-20T04:36:46+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.40 | -0.01 | 2026-11-19 | 2026-11-20T04:36:46+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.96 | 0.03 | +0.09 | 2026-11-20 | 2026-11-20T04:36:07+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.80 | -0.10 | -0.10 | 2026-11-19 | 2026-11-20T04:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.16 | -0.22 | -0.14 | 2026-11-20 | 2026-11-20T04:36:06+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,337.91 | 7.51 | +0.56 | 2026-11-20 | 2026-11-20T04:36:07+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 352.09 | -10.53 | -2.90 | 2026-11-19 | 2026-11-20T04:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.40 | -0.56 | -4.01 | 2026-11-19 | 2026-11-20T04:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 30.49 | -2.03 | -6.24 | 2026-11-19 | 2026-11-20T04:36:07+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 82.90 | -0.31 | -0.37 | 2026-11-19 | 2026-11-20T04:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,534.90 | -150.60 | -4.09 | 2026-11-19 | 2026-11-20T04:36:07+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 61,346.81 | -1,640.46 | -2.60 | 2026-11-20 | 2026-11-20T04:36:07+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：「腰斬再腰斬」國巨跌破300元 股東數卻創高
  - 來源：Yahoo 台股；發布時間：2026-11-20T03:18:11Z；台北時間：2026-11-20 11:18
  - 摘要：被動元件龍頭廠國巨（2327）今天股價正式摔破300元，最低來到296元，跌幅達到9%，相較今年創下的天價1220元已經「腰斬再腰斬」。凱旭投顧分析師王士維指出，如今操作上還是要以晶片與IC設計等技術護城河較高的方向走，若這些上游未漲，恐怕
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%9C%8B%E5%B7%A867%E8%90%AC%E8%82%A1%E6%9D%B1%E5%BF%83%E7%97%9B%E8%82%A1%E5%83%B9%E3%80%8C%E8%85%B0%E6%96%AC%E5%86%8D%E8%85%B0%E6%96%AC%E3%80%8D%E8%B7%8C%E7%A0%B4300%E5%85%83-%E5%88%86%E6%9E%90%E5%B8%AB%E7%9C%8B%E6%B3%95%E6%9B%9D-031811460.html
- 事件2：杜金龍早盤逆勢買3個股 揭台積進場價「選後你會贏」
  - 來源：Yahoo 台股；發布時間：2026-11-20T02:23:00Z；台北時間：2026-11-20 10:23
  - 摘要：台股空襲警報響起！繼昨（19）日暴跌1,768點失守年線後，今（20）日早盤即便有金管會限空令2.0上路，台股仍是賣壓沉重，開盤重挫且摜破11/6的前波低點37,837點。投資市場哀鴻遍野，股市老先覺杜金龍認為，破底破線後，將迎來反彈，他透
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E7%A9%BA%E8%A5%B2%E8%AD%A6%E5%A0%B1-%E4%B8%8D%E8%A6%81-%E7%9B%B4%E8%AC%9B%E9%9B%BB%E8%A9%B1-%E8%B6%95%E5%BF%AB%E8%B2%B7%E8%82%A1%E7%A5%A8-%E6%9D%9C%E9%87%91%E9%BE%8D%E5%8F%B0%E8%82%A1%E5%B4%A9%E7%9B%A4%E6%97%A5%E5%87%BA%E6%89%8B3%E6%AA%94%E5%90%8D%E5%96%AE%E6%9B%9D%E5%85%89-022300618.html
- 事件3：22千金盤中慘跌停 僅一檔逆勢漲近5%
  - 來源：Yahoo 台股；發布時間：2026-11-20T03:07:00Z；台北時間：2026-11-20 11:07
  - 摘要：台股今（20）日遭空軍大舉轟炸，盤中加權指數一度重挫逾2400點，失守36000點大關。權王台積電跌破2000元，股王信驊等22檔千金股慘吞跌停，盤面一片慘綠，僅創新服務逆勢走揚。投資人應審慎評估風險。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%A4%B1%E5%AE%882000%E5%85%83%E5%A4%A7%E9%97%9C-22%E6%AA%94%E5%8D%83%E9%87%91%E8%82%A1%E9%96%8B%E8%B7%8C%E5%81%9C%E6%B4%BE%E5%B0%8D-%E5%AE%83-%E7%AB%9F%E9%80%86%E5%8B%A2%E6%BC%B2%E8%BF%915-030700267.html
- 事件4：股市低迷 民眾景氣樂觀情緒、消費意願雙雙降溫
  - 來源：Yahoo 台股；發布時間：2026-11-20T01:48:41Z；台北時間：2026-11-20 09:48
  - 摘要：[NOWNEWS今日新聞]台股跌不停，今（20）日早盤再崩逾千點，失守37000點，根據國泰金控公布最新11月國民經濟信心調查結果也顯示，民眾景氣樂觀情緒降溫，消費意願亦下降，美伊戰爭持續且AI擔憂再...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%B4%A9%E8%B7%8C-%E6%B0%91%E7%9C%BE%E8%82%A1%E5%B8%82%E6%A8%82%E8%A7%80%E6%8C%87%E6%95%B8%E8%88%87%E9%A2%A8%E9%9A%AA%E5%81%8F%E5%A5%BD%E9%9B%99%E9%99%8D-014841145.html
- 事件5：恐慌情緒蔓延 韓股挫4%、日股一度瀉2800點
  - 來源：Yahoo 台股；發布時間：2026-11-20T02:48:24Z；台北時間：2026-11-20 10:48
  - 摘要：受美國晶片出口管制新規上路及美股科技股重挫影響，亞股20日恐慌蔓延，日、韓股市同步暴跌。日經指數盤中狂瀉逾2600點，軟銀與半導體股災情慘重；韓股則跌破5000點大關，記憶體雙雄領跌。新規涵蓋先進邏輯晶片，傳出台積電已暫停部分中國處理器出貨
  - 原文連結：https://tw.stock.yahoo.com/news/%E4%BA%9E%E8%82%A1%E9%9B%AA%E5%B4%A9-%E9%9F%93%E8%82%A1%E6%91%9C%E7%A0%B45000%E9%BB%9E%E5%A4%A7%E9%97%9C-%E6%97%A5%E8%82%A1%E8%B7%8C%E9%80%BE2800%E9%BB%9E-023600096.html
- 事件6：央行守不住 新台幣開盤不久就貶破33元大關
  - 來源：Yahoo 台股；發布時間：2026-11-20T01:17:52Z；台北時間：2026-11-20 09:17
  - 摘要：[NOWNEWS今日新聞]美元指數居高盤整，加上台股再崩跌逾千點，新台幣兌美元今（20）日上午一開盤不久就貶破33元整數關卡，一度來到33.038元，貶值9.6分。就國際匯市來看，美元指數一度來到10...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%AE%E8%A1%8C%E5%AE%88%E4%B9%9F%E6%B2%92%E7%94%A8-%E5%8F%B0%E8%82%A1%E5%8F%88%E5%B4%A9-%E6%96%B0%E5%8F%B0%E5%B9%A3%E5%86%8D%E8%B2%B6%E7%A0%B433%E5%85%83-011752232.html
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
- 事件12：Commerce approved sales of more than 879,000 AI chips to Chinese companies, Rep. Mast says
  - 來源：CNBC；發布時間：Fri, 20 Nov 2026 00:53:55 GMT；台北時間：2026-11-20 08:53
  - 摘要：Members of Congress have pushed in the wake of the Jensen Huang scandal for legislation to tighten export controls on chip sales to China.
  - 原文連結：https://www.cnbc.com/2026/11/19/nvidia-amd-china-chip-sales-congress.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-19

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,500 | 點 | TAIFEX Proxy |
| 最高價 | 40,670 | 點 | TAIFEX Proxy |
| 最低價 | 38,386 | 點 | TAIFEX Proxy |
| 收盤價 | 38,649 | 點 | TAIFEX Proxy |
| 漲跌點數 | -1,683 | 點 | TAIFEX Proxy |
| 漲跌幅 | -4.17 | % | TAIFEX Proxy |
| 成交量 | 114,619 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 40,670 / 38,386 | 點 | TAIFEX Proxy |

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
| 多空淨 OI 變化 | unavailable | 沿用前版（原來源：換月基準重建） |
- 資料日期：2026-11-19 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 108,065 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 106,627 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,438 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 48,306 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 45,649 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,657 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,219 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -1,782 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -1,782 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -16 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -366 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +350 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -360 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +2,291 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -30.3 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +179.3 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 38,649 | TAIFEX Proxy |
| 加權指數價格 | 38,426.89 | twse-proxy |
| 台指期與加權指數價差 | +222.11 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +0.58 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +222.11 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -542 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 38,649 | 38,107 | +542 | TAIFEX Proxy |
| 成交量 | 114,619 | 74,153 | +40,466 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,561（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 108,065 | 106,627 | +1,438 | 48,306 | 45,649 | +2,657 | -1,219 | 12,664 | 111,883 | -99,219 | +219 | TAIFEX Proxy |
| 投信 | 8 | 1,790 | -1,782 | 0 | 0 | +0 | -1,782 | 95,246 | 3,455 | +91,791 | -1,782 | TAIFEX Proxy |
| 自營商 | 8,895 | 8,911 | -16 | 1,746 | 2,112 | -366 | +350 | 3,102 | 4,557 | -1,455 | +2 | TAIFEX Proxy |
| 三大法人合計 | 116,968 | 117,328 | -360 | 50,052 | 47,761 | +2,291 | -2,651 | 111,012 | 119,895 | -8,883 | -1,561 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,642 | TAIFEX Proxy |
| 前十大交易人空方 OI | 95,571 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +5,071 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 沿用前版（原來源：換月基準重建） |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 39.28% | TAIFEX Proxy |
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
| 本次報告產製時間 | 2026-11-20 12:35:47 | 本機 |
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
| 外資 Call日買 | 60,034 | TAIFEX Proxy |
| 外資 Call日賣 | 60,896 | TAIFEX Proxy |
| 外資 Call日淨 | -862 | TAIFEX Proxy |
| 外資 Put日買 | 53,592 | TAIFEX Proxy |
| 外資 Put日賣 | 55,016 | TAIFEX Proxy |
| 外資 Put日淨 | -1,424 | TAIFEX Proxy |
| 外資 Call夜買 | 41,965 | TAIFEX Proxy |
| 外資 Call夜賣 | 42,801 | TAIFEX Proxy |
| 外資 Call夜淨 | -836 | TAIFEX Proxy |
| 外資 Put夜買 | 45,532 | TAIFEX Proxy |
| 外資 Put夜賣 | 45,767 | TAIFEX Proxy |
| 外資 Put夜淨 | -235 | TAIFEX Proxy |
| 外資 日盤淨總量 | +562 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -26 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -1,189 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 53,248 | TAIFEX Proxy |
| 自營商 Call日賣 | 59,009 | TAIFEX Proxy |
| 自營商 Call日淨 | -5,761 | TAIFEX Proxy |
| 自營商 Put日買 | 46,234 | TAIFEX Proxy |
| 自營商 Put日賣 | 43,344 | TAIFEX Proxy |
| 自營商 Put日淨 | +2,890 | TAIFEX Proxy |
| 自營商 Call夜買 | 18,408 | TAIFEX Proxy |
| 自營商 Call夜賣 | 22,271 | TAIFEX Proxy |
| 自營商 Call夜淨 | -3,863 | TAIFEX Proxy |
| 自營商 Put夜買 | 18,293 | TAIFEX Proxy |
| 自營商 Put夜賣 | 20,619 | TAIFEX Proxy |
| 自營商 Put夜淨 | -2,326 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -8,651 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -1,898 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +5,216 | TAIFEX Proxy |

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
| GEX 實際使用到期月份 | 202611F3 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-20 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F3 | TAIFEX Proxy |
| 資料日期 | 2026-11-19 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 37,575.78 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611F3 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-20 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F3 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 83,887 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 83,887 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 31,249 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 25,737 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-19 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：34,584.20～42,269.58
- 搜尋步長／計算次數：10.00／301
- 起點／終點 Net GEX：-1,013,220,570.01／19,919,411.63
- 搜尋區間最低／最高 Net GEX：-1,727,188,247.50／19,919,411.63
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-19","chain_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":452},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":218,"delta_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":0,"delta_rows":204},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":572},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":432},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":246,"delta_rows":276},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":294},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":294}],"selected":{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-19","source":"taifex_web","fallback_used":false,"index_duration_ms":1453,"index_error":null,"openapi_fetch_duration_ms":17,"attempts":[{"attempt":1,"duration_ms":1358,"source":"taifex_web","fallback":false,"http_status":502,"raw_rows":0,"primary_error":"TAIFEX primary HTTP 200 / rows 0","parser":{"input_rows":0,"array_rows":0,"object_rows":0,"short_rows":0,"non_txo_rows":0,"txo_rows":0,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":0,"per_expiry":[]},"accepted_txo_rows":0},{"attempt":2,"duration_ms":2545,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3689,"primary_error":null,"parser":{"input_rows":3689,"array_rows":3689,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3684,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3684,"per_expiry":[{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]},"accepted_txo_rows":3684}],"parser":{"input_rows":3689,"array_rows":3689,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3684,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3684,"per_expiry":[{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]},"final_rows":3684,"per_expiry_rows":[{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":452,"recognized_type_rows":452,"valid_strike_rows":452,"valid_delta_rows":452,"parsed_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":428,"recognized_type_rows":428,"valid_strike_rows":428,"valid_delta_rows":428,"parsed_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":280,"recognized_type_rows":280,"valid_strike_rows":280,"valid_delta_rows":280,"parsed_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","raw_txo_rows":204,"recognized_type_rows":204,"valid_strike_rows":204,"valid_delta_rows":204,"parsed_rows":204},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":572,"recognized_type_rows":572,"valid_strike_rows":572,"valid_delta_rows":572,"parsed_rows":572},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":432,"recognized_type_rows":432,"valid_strike_rows":432,"valid_delta_rows":432,"parsed_rows":432},{"contract_month":"202702","expiry":"2027-02-17","raw_txo_rows":276,"recognized_type_rows":276,"valid_strike_rows":276,"valid_delta_rows":276,"parsed_rows":276},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":294,"recognized_type_rows":294,"valid_strike_rows":294,"valid_delta_rows":294,"parsed_rows":294}]}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：32,662.86～44,190.92
- 搜尋步長／計算次數：10.00／1154
- 起點／終點 Net GEX：-155,678,591.21／6,104,732,932.63
- 搜尋區間最低／最高 Net GEX：-1,727,183,149.83／10,423,030,284.82
- 正負號交叉次數：1
- 擴大區間診斷 Flip：37,575.77

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 2,412,597,917.00 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 9,714,546,932.77 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 201 | 資料日期：2026-11-19 |
| 正 Net GEX 最大履約價 | 38,700 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 37,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：38,700（372,316,275.61 NT$）、38,600（358,741,069.55 NT$）、38,900（354,000,286.79 NT$）、38,800（326,105,532.35 NT$）、39,100（320,019,670.82 NT$）
- 負 Net GEX Top 5：37,000（-272,127,442.32 NT$）、38,000（-261,162,228.62 NT$）、35,700（-179,926,343.65 NT$）、37,500（-127,903,289.00 NT$）、37,600（-99,030,140.53 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-19","underlying":38426.89,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":2412597916.998448,"gross_gex_1pct":9714546932.766554,"gamma_diagnostics":{"chain_rows":404,"delta_rows":452,"matched_strike_keys":404,"positive_oi_settlement_eligible":364,"invalid_oi":40,"invalid_settlement":0,"below_intrinsic":108,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":256},"formal_flip_diagnostics":{"search_lower_underlying":34584.201,"search_upper_underlying":42269.579000000005,"step":10,"evaluations":301,"start_net_gex_1pct":-1013220570.0069048,"end_net_gex_1pct":19919411.62556194,"min_net_gex_1pct":-1727188247.497862,"max_net_gex_1pct":19919411.62556194,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":37572.856499999994,"upper_underlying":37582.856499999994,"estimated_underlying":37575.77375810321,"lower_net_gex_1pct":-6891729.52795422,"upper_net_gex_1pct":16732266.992475692},"wide_range_flip_diagnostics":{"search_lower_underlying":32662.856499999998,"search_upper_underlying":44190.9235,"reference_underlying":38426.89,"step":10,"evaluations":1154,"start_net_gex_1pct":-155678591.2108729,"end_net_gex_1pct":6104732932.631371,"min_net_gex_1pct":-1727183149.8307655,"max_net_gex_1pct":10423030284.815968,"zero_crossings":1,"found":true,"selected_crossing_distance":851.116241896787},"expiry_selection_diagnostics":{"requested_date":"2026-11-19","chain_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":452},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":218,"delta_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":0,"delta_rows":204},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":572},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":432},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":246,"delta_rows":276},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":294},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":294}],"selected":{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":35700.0,"call_gex_1pct":0.0,"put_gex_1pct":-179926343.65088996,"net_gex_1pct":-179926343.65088996,"gross_gex_1pct":179926343.65088996,"call_oi":0,"put_oi":3728},{"strike":35800.0,"call_gex_1pct":0.0,"put_gex_1pct":-21987776.144025106,"net_gex_1pct":-21987776.144025106,"gross_gex_1pct":21987776.144025106,"call_oi":0,"put_oi":424},{"strike":35900.0,"call_gex_1pct":0.0,"put_gex_1pct":-16027300.647547636,"net_gex_1pct":-16027300.647547636,"gross_gex_1pct":16027300.647547636,"call_oi":0,"put_oi":292},{"strike":36000.0,"call_gex_1pct":135170.51381757134,"put_gex_1pct":-58722922.03586349,"net_gex_1pct":-58587751.52204592,"gross_gex_1pct":58858092.54968106,"call_oi":2,"put_oi":985},{"strike":36100.0,"call_gex_1pct":70952.42770411145,"put_gex_1pct":-13120891.863066994,"net_gex_1pct":-13049939.435362883,"gross_gex_1pct":13191844.290771104,"call_oi":1,"put_oi":203},{"strike":36200.0,"call_gex_1pct":74971.02479421768,"put_gex_1pct":-20364157.87572744,"net_gex_1pct":-20289186.850933224,"gross_gex_1pct":20439128.90052166,"call_oi":1,"put_oi":292},{"strike":36300.0,"call_gex_1pct":157820.71123643042,"put_gex_1pct":-16168029.653001538,"net_gex_1pct":-16010208.941765107,"gross_gex_1pct":16325850.364237968,"call_oi":2,"put_oi":216},{"strike":36400.0,"call_gex_1pct":250136.81049527464,"put_gex_1pct":-29674721.14935521,"net_gex_1pct":-29424584.338859934,"gross_gex_1pct":29924857.959850486,"call_oi":3,"put_oi":370},{"strike":36500.0,"call_gex_1pct":88042.6403581729,"put_gex_1pct":-62282877.22265768,"net_gex_1pct":-62194834.58229951,"gross_gex_1pct":62370919.86301585,"call_oi":1,"put_oi":728},{"strike":36600.0,"call_gex_1pct":278801.0011712281,"put_gex_1pct":-24288627.599415824,"net_gex_1pct":-24009826.598244596,"gross_gex_1pct":24567428.60058705,"call_oi":3,"put_oi":264},{"strike":36700.0,"call_gex_1pct":294261.3301164102,"put_gex_1pct":-37534539.0233415,"net_gex_1pct":-37240277.693225086,"gross_gex_1pct":37828800.35345791,"call_oi":3,"put_oi":382},{"strike":36800.0,"call_gex_1pct":207083.83694209272,"put_gex_1pct":-44362571.33998685,"net_gex_1pct":-44155487.50304476,"gross_gex_1pct":44569655.176928945,"call_oi":2,"put_oi":422},{"strike":36900.0,"call_gex_1pct":437368.0164216113,"put_gex_1pct":-35034354.56054806,"net_gex_1pct":-34596986.54412645,"gross_gex_1pct":35471722.57696967,"call_oi":4,"put_oi":312},{"strike":37000.0,"call_gex_1pct":1155375.6241956663,"put_gex_1pct":-273282817.9458766,"net_gex_1pct":-272127442.3216809,"gross_gex_1pct":274438193.5700723,"call_oi":10,"put_oi":2283},{"strike":37100.0,"call_gex_1pct":969549.6584888623,"put_gex_1pct":-21116381.12650296,"net_gex_1pct":-20146831.4680141,"gross_gex_1pct":22085930.784991823,"call_oi":8,"put_oi":166},{"strike":37200.0,"call_gex_1pct":1025359.9711721524,"put_gex_1pct":-50917409.586000785,"net_gex_1pct":-49892049.61482863,"gross_gex_1pct":51942769.55717294,"call_oi":8,"put_oi":375},{"strike":37300.0,"call_gex_1pct":537348.6634798747,"put_gex_1pct":-40096220.56683759,"net_gex_1pct":-39558871.903357714,"gross_gex_1pct":40633569.23031746,"call_oi":4,"put_oi":280},{"strike":37400.0,"call_gex_1pct":1281095.3706776705,"put_gex_1pct":-44537505.33342253,"net_gex_1pct":-43256409.962744854,"gross_gex_1pct":45818600.7041002,"call_oi":9,"put_oi":293},{"strike":37500.0,"call_gex_1pct":3134631.6801212807,"put_gex_1pct":-131037920.67561907,"net_gex_1pct":-127903288.99549778,"gross_gex_1pct":134172552.35574035,"call_oi":21,"put_oi":824},{"strike":37600.0,"call_gex_1pct":2627322.0693802824,"put_gex_1pct":-101657462.59623954,"net_gex_1pct":-99030140.52685925,"gross_gex_1pct":104284784.66561982,"call_oi":17,"put_oi":608},{"strike":37700.0,"call_gex_1pct":2629313.0317425723,"put_gex_1pct":-83882348.8636898,"net_gex_1pct":-81253035.83194722,"gross_gex_1pct":86511661.89543237,"call_oi":16,"put_oi":473},{"strike":37800.0,"call_gex_1pct":13918536.32645154,"put_gex_1pct":-70034011.56727025,"net_gex_1pct":-56115475.24081871,"gross_gex_1pct":83952547.89372179,"call_oi":83,"put_oi":380},{"strike":37900.0,"call_gex_1pct":12337548.407608321,"put_gex_1pct":-61854798.27195259,"net_gex_1pct":-49517249.86434427,"gross_gex_1pct":74192346.67956091,"call_oi":69,"put_oi":321},{"strike":38000.0,"call_gex_1pct":28153808.33085046,"put_gex_1pct":-289316036.9535517,"net_gex_1pct":-261162228.62270126,"gross_gex_1pct":317469845.2844022,"call_oi":152,"put_oi":1455},{"strike":38100.0,"call_gex_1pct":11423412.12739727,"put_gex_1pct":-81210631.13875768,"net_gex_1pct":-69787219.0113604,"gross_gex_1pct":92634043.26615494,"call_oi":60,"put_oi":400},{"strike":38200.0,"call_gex_1pct":18712434.845892575,"put_gex_1pct":-77084188.35666506,"net_gex_1pct":-58371753.51077248,"gross_gex_1pct":95796623.20255764,"call_oi":98,"put_oi":366},{"strike":38300.0,"call_gex_1pct":24719393.585683815,"put_gex_1pct":-85555180.73075387,"net_gex_1pct":-60835787.14507005,"gross_gex_1pct":110274574.31643769,"call_oi":127,"put_oi":400},{"strike":38400.0,"call_gex_1pct":36766534.79944124,"put_gex_1pct":-91975631.32246982,"net_gex_1pct":-55209096.523028575,"gross_gex_1pct":128742166.12191105,"call_oi":179,"put_oi":414},{"strike":38500.0,"call_gex_1pct":470357241.08804595,"put_gex_1pct":-213608763.47349298,"net_gex_1pct":256748477.61455297,"gross_gex_1pct":683966004.5615389,"call_oi":2324,"put_oi":959},{"strike":38550.0,"call_gex_1pct":23919169.777318966,"put_gex_1pct":-46157608.43571248,"net_gex_1pct":-22238438.658393513,"gross_gex_1pct":70076778.21303144,"call_oi":116,"put_oi":205},{"strike":38600.0,"call_gex_1pct":430193781.5740324,"put_gex_1pct":-71452712.02759416,"net_gex_1pct":358741069.5464383,"gross_gex_1pct":501646493.6016266,"call_oi":2080,"put_oi":323},{"strike":38650.0,"call_gex_1pct":69027049.82915464,"put_gex_1pct":-45142875.02480545,"net_gex_1pct":23884174.80434919,"gross_gex_1pct":114169924.8539601,"call_oi":331,"put_oi":200},{"strike":38700.0,"call_gex_1pct":433100740.2113754,"put_gex_1pct":-60784464.605752915,"net_gex_1pct":372316275.60562253,"gross_gex_1pct":493885204.8171283,"call_oi":2111,"put_oi":269},{"strike":38750.0,"call_gex_1pct":29626384.92356494,"put_gex_1pct":-37814147.143968284,"net_gex_1pct":-8187762.220403343,"gross_gex_1pct":67440532.06753322,"call_oi":143,"put_oi":164},{"strike":38800.0,"call_gex_1pct":431391058.7906918,"put_gex_1pct":-105285526.4393014,"net_gex_1pct":326105532.35139036,"gross_gex_1pct":536676585.2299932,"call_oi":2113,"put_oi":474},{"strike":38850.0,"call_gex_1pct":29207730.613958254,"put_gex_1pct":-34746622.796033785,"net_gex_1pct":-5538892.18207553,"gross_gex_1pct":63954353.40999204,"call_oi":141,"put_oi":152},{"strike":38900.0,"call_gex_1pct":421820484.733505,"put_gex_1pct":-67820197.93978171,"net_gex_1pct":354000286.7937233,"gross_gex_1pct":489640682.67328674,"call_oi":2106,"put_oi":308},{"strike":38950.0,"call_gex_1pct":24521275.65474842,"put_gex_1pct":-27699142.07817065,"net_gex_1pct":-3177866.4234222285,"gross_gex_1pct":52220417.73291907,"call_oi":122,"put_oi":127},{"strike":39000.0,"call_gex_1pct":506402453.0796209,"put_gex_1pct":-214681990.1522623,"net_gex_1pct":291720462.9273586,"gross_gex_1pct":721084443.2318832,"call_oi":2558,"put_oi":968},{"strike":39050.0,"call_gex_1pct":60923395.7474985,"put_gex_1pct":-32601337.57022662,"net_gex_1pct":28322058.177271876,"gross_gex_1pct":93524733.31772512,"call_oi":311,"put_oi":150},{"strike":39100.0,"call_gex_1pct":414699184.7628193,"put_gex_1pct":-94679513.94468775,"net_gex_1pct":320019670.81813157,"gross_gex_1pct":509378698.707507,"call_oi":2137,"put_oi":441},{"strike":39150.0,"call_gex_1pct":63771963.81963209,"put_gex_1pct":-16410017.671799172,"net_gex_1pct":47361946.147832915,"gross_gex_1pct":80181981.49143127,"call_oi":334,"put_oi":80},{"strike":39200.0,"call_gex_1pct":237528371.38095638,"put_gex_1pct":-71475148.06115851,"net_gex_1pct":166053223.31979787,"gross_gex_1pct":309003519.4421149,"call_oi":1265,"put_oi":348},{"strike":39250.0,"call_gex_1pct":28208057.861339647,"put_gex_1pct":-18650914.676136106,"net_gex_1pct":9557143.185203541,"gross_gex_1pct":46858972.53747575,"call_oi":152,"put_oi":93},{"strike":39300.0,"call_gex_1pct":50062430.396362096,"put_gex_1pct":-45267565.68083278,"net_gex_1pct":4794864.715529315,"gross_gex_1pct":95329996.07719487,"call_oi":277,"put_oi":236},{"strike":39350.0,"call_gex_1pct":27699573.045365974,"put_gex_1pct":-11219572.787063876,"net_gex_1pct":16480000.258302098,"gross_gex_1pct":38919145.83242985,"call_oi":157,"put_oi":59},{"strike":39400.0,"call_gex_1pct":81970498.88160975,"put_gex_1pct":-40467602.78638083,"net_gex_1pct":41502896.095228925,"gross_gex_1pct":122438101.66799058,"call_oi":474,"put_oi":217},{"strike":39450.0,"call_gex_1pct":19192057.963685274,"put_gex_1pct":-11935708.10591146,"net_gex_1pct":7256349.857773814,"gross_gex_1pct":31127766.069596734,"call_oi":114,"put_oi":67},{"strike":39500.0,"call_gex_1pct":458735492.3814168,"put_gex_1pct":-180730059.65471265,"net_gex_1pct":278005432.7267041,"gross_gex_1pct":639465552.0361295,"call_oi":2796,"put_oi":1057},{"strike":39550.0,"call_gex_1pct":16628387.620235996,"put_gex_1pct":-13526787.528006822,"net_gex_1pct":3101600.0922291745,"gross_gex_1pct":30155175.148242816,"call_oi":104,"put_oi":83},{"strike":39600.0,"call_gex_1pct":54383978.88415292,"put_gex_1pct":-23462647.235345706,"net_gex_1pct":30921331.648807213,"gross_gex_1pct":77846626.11949863,"call_oi":351,"put_oi":152},{"strike":39650.0,"call_gex_1pct":20707539.195878558,"put_gex_1pct":-15506358.905271519,"net_gex_1pct":5201180.290607039,"gross_gex_1pct":36213898.10115008,"call_oi":138,"put_oi":105},{"strike":39700.0,"call_gex_1pct":157245882.43644014,"put_gex_1pct":-19013024.00610607,"net_gex_1pct":138232858.43033406,"gross_gex_1pct":176258906.44254622,"call_oi":1086,"put_oi":137},{"strike":39750.0,"call_gex_1pct":22904008.769188005,"put_gex_1pct":-9020891.459703831,"net_gex_1pct":13883117.309484174,"gross_gex_1pct":31924900.228891835,"call_oi":164,"put_oi":70},{"strike":39800.0,"call_gex_1pct":69514888.09235713,"put_gex_1pct":-12447688.212414121,"net_gex_1pct":57067199.879943006,"gross_gex_1pct":81962576.30477124,"call_oi":517,"put_oi":106},{"strike":39850.0,"call_gex_1pct":16000151.705015596,"put_gex_1pct":-5287637.063762823,"net_gex_1pct":10712514.641252773,"gross_gex_1pct":21287788.76877842,"call_oi":124,"put_oi":47},{"strike":39900.0,"call_gex_1pct":42096674.52443412,"put_gex_1pct":-36787588.99308074,"net_gex_1pct":5309085.531353377,"gross_gex_1pct":78884263.51751485,"call_oi":341,"put_oi":432},{"strike":39950.0,"call_gex_1pct":12308540.30152894,"put_gex_1pct":-4236735.623543338,"net_gex_1pct":8071804.677985602,"gross_gex_1pct":16545275.925072279,"call_oi":104,"put_oi":52},{"strike":40000.0,"call_gex_1pct":280113101.1165351,"put_gex_1pct":0.0,"net_gex_1pct":280113101.1165351,"gross_gex_1pct":280113101.1165351,"call_oi":2472,"put_oi":0},{"strike":40050.0,"call_gex_1pct":20098705.693250507,"put_gex_1pct":0.0,"net_gex_1pct":20098705.693250507,"gross_gex_1pct":20098705.693250507,"call_oi":186,"put_oi":0},{"strike":40100.0,"call_gex_1pct":97360414.1782368,"put_gex_1pct":0.0,"net_gex_1pct":97360414.1782368,"gross_gex_1pct":97360414.1782368,"call_oi":945,"put_oi":0},{"strike":40150.0,"call_gex_1pct":17016747.20958238,"put_gex_1pct":0.0,"net_gex_1pct":17016747.20958238,"gross_gex_1pct":17016747.20958238,"call_oi":175,"put_oi":0},{"strike":40200.0,"call_gex_1pct":76614634.49354026,"put_gex_1pct":0.0,"net_gex_1pct":76614634.49354026,"gross_gex_1pct":76614634.49354026,"call_oi":825,"put_oi":0},{"strike":40250.0,"call_gex_1pct":15294057.253754089,"put_gex_1pct":0.0,"net_gex_1pct":15294057.253754089,"gross_gex_1pct":15294057.253754089,"call_oi":174,"put_oi":0},{"strike":40300.0,"call_gex_1pct":88127699.98043093,"put_gex_1pct":0.0,"net_gex_1pct":88127699.98043093,"gross_gex_1pct":88127699.98043093,"call_oi":1057,"put_oi":0},{"strike":40350.0,"call_gex_1pct":10519603.601725094,"put_gex_1pct":0.0,"net_gex_1pct":10519603.601725094,"gross_gex_1pct":10519603.601725094,"call_oi":132,"put_oi":0},{"strike":40400.0,"call_gex_1pct":27914272.950690884,"put_gex_1pct":0.0,"net_gex_1pct":27914272.950690884,"gross_gex_1pct":27914272.950690884,"call_oi":371,"put_oi":0},{"strike":40450.0,"call_gex_1pct":9949567.070902433,"put_gex_1pct":0.0,"net_gex_1pct":9949567.070902433,"gross_gex_1pct":9949567.070902433,"call_oi":142,"put_oi":0},{"strike":40500.0,"call_gex_1pct":98205628.9076445,"put_gex_1pct":0.0,"net_gex_1pct":98205628.9076445,"gross_gex_1pct":98205628.9076445,"call_oi":1476,"put_oi":0},{"strike":40550.0,"call_gex_1pct":18729853.266399853,"put_gex_1pct":0.0,"net_gex_1pct":18729853.266399853,"gross_gex_1pct":18729853.266399853,"call_oi":297,"put_oi":0},{"strike":40600.0,"call_gex_1pct":23004029.13982819,"put_gex_1pct":0.0,"net_gex_1pct":23004029.13982819,"gross_gex_1pct":23004029.13982819,"call_oi":394,"put_oi":0},{"strike":40650.0,"call_gex_1pct":17496809.45934725,"put_gex_1pct":0.0,"net_gex_1pct":17496809.45934725,"gross_gex_1pct":17496809.45934725,"call_oi":316,"put_oi":0},{"strike":40700.0,"call_gex_1pct":20231092.483703308,"put_gex_1pct":0.0,"net_gex_1pct":20231092.483703308,"gross_gex_1pct":20231092.483703308,"call_oi":397,"put_oi":0},{"strike":40750.0,"call_gex_1pct":9998706.563232632,"put_gex_1pct":0.0,"net_gex_1pct":9998706.563232632,"gross_gex_1pct":9998706.563232632,"call_oi":202,"put_oi":0},{"strike":40800.0,"call_gex_1pct":27645907.963556115,"put_gex_1pct":0.0,"net_gex_1pct":27645907.963556115,"gross_gex_1pct":27645907.963556115,"call_oi":614,"put_oi":0},{"strike":40850.0,"call_gex_1pct":8038412.692873834,"put_gex_1pct":0.0,"net_gex_1pct":8038412.692873834,"gross_gex_1pct":8038412.692873834,"call_oi":191,"put_oi":0},{"strike":40900.0,"call_gex_1pct":14905627.679237299,"put_gex_1pct":0.0,"net_gex_1pct":14905627.679237299,"gross_gex_1pct":14905627.679237299,"call_oi":387,"put_oi":0},{"strike":40950.0,"call_gex_1pct":5656753.583550529,"put_gex_1pct":0.0,"net_gex_1pct":5656753.583550529,"gross_gex_1pct":5656753.583550529,"call_oi":151,"put_oi":0},{"strike":41000.0,"call_gex_1pct":114905276.86813204,"put_gex_1pct":0.0,"net_gex_1pct":114905276.86813204,"gross_gex_1pct":114905276.86813204,"call_oi":3326,"put_oi":0},{"strike":41050.0,"call_gex_1pct":6457108.506737776,"put_gex_1pct":0.0,"net_gex_1pct":6457108.506737776,"gross_gex_1pct":6457108.506737776,"call_oi":200,"put_oi":0},{"strike":41100.0,"call_gex_1pct":13365213.099870339,"put_gex_1pct":0.0,"net_gex_1pct":13365213.099870339,"gross_gex_1pct":13365213.099870339,"call_oi":445,"put_oi":0},{"strike":41150.0,"call_gex_1pct":4497399.8336008005,"put_gex_1pct":0.0,"net_gex_1pct":4497399.8336008005,"gross_gex_1pct":4497399.8336008005,"call_oi":161,"put_oi":0},{"strike":41200.0,"call_gex_1pct":11628492.248155996,"put_gex_1pct":0.0,"net_gex_1pct":11628492.248155996,"gross_gex_1pct":11628492.248155996,"call_oi":471,"put_oi":0},{"strike":41250.0,"call_gex_1pct":4946809.894329816,"put_gex_1pct":0.0,"net_gex_1pct":4946809.894329816,"gross_gex_1pct":4946809.894329816,"call_oi":218,"put_oi":0},{"strike":41300.0,"call_gex_1pct":13800704.53077354,"put_gex_1pct":0.0,"net_gex_1pct":13800704.53077354,"gross_gex_1pct":13800704.53077354,"call_oi":650,"put_oi":0},{"strike":41350.0,"call_gex_1pct":3906042.188036163,"put_gex_1pct":0.0,"net_gex_1pct":3906042.188036163,"gross_gex_1pct":3906042.188036163,"call_oi":192,"put_oi":0},{"strike":41400.0,"call_gex_1pct":9130178.461089429,"put_gex_1pct":0.0,"net_gex_1pct":9130178.461089429,"gross_gex_1pct":9130178.461089429,"call_oi":508,"put_oi":0},{"strike":41450.0,"call_gex_1pct":2351735.7670932966,"put_gex_1pct":0.0,"net_gex_1pct":2351735.7670932966,"gross_gex_1pct":2351735.7670932966,"call_oi":144,"put_oi":0},{"strike":41500.0,"call_gex_1pct":19480602.31187496,"put_gex_1pct":0.0,"net_gex_1pct":19480602.31187496,"gross_gex_1pct":19480602.31187496,"call_oi":1272,"put_oi":0},{"strike":41550.0,"call_gex_1pct":3198989.7652159557,"put_gex_1pct":0.0,"net_gex_1pct":3198989.7652159557,"gross_gex_1pct":3198989.7652159557,"call_oi":217,"put_oi":0},{"strike":41600.0,"call_gex_1pct":5638405.698750017,"put_gex_1pct":0.0,"net_gex_1pct":5638405.698750017,"gross_gex_1pct":5638405.698750017,"call_oi":454,"put_oi":0},{"strike":41650.0,"call_gex_1pct":1964268.9262463087,"put_gex_1pct":0.0,"net_gex_1pct":1964268.9262463087,"gross_gex_1pct":1964268.9262463087,"call_oi":172,"put_oi":0},{"strike":41700.0,"call_gex_1pct":3152586.61506677,"put_gex_1pct":0.0,"net_gex_1pct":3152586.61506677,"gross_gex_1pct":3152586.61506677,"call_oi":310,"put_oi":0},{"strike":41750.0,"call_gex_1pct":1154081.6943244354,"put_gex_1pct":0.0,"net_gex_1pct":1154081.6943244354,"gross_gex_1pct":1154081.6943244354,"call_oi":126,"put_oi":0},{"strike":41800.0,"call_gex_1pct":4931328.8566928785,"put_gex_1pct":0.0,"net_gex_1pct":4931328.8566928785,"gross_gex_1pct":4931328.8566928785,"call_oi":586,"put_oi":0},{"strike":41850.0,"call_gex_1pct":1130309.2631977436,"put_gex_1pct":0.0,"net_gex_1pct":1130309.2631977436,"gross_gex_1pct":1130309.2631977436,"call_oi":153,"put_oi":0},{"strike":41900.0,"call_gex_1pct":2212028.5186298774,"put_gex_1pct":0.0,"net_gex_1pct":2212028.5186298774,"gross_gex_1pct":2212028.5186298774,"call_oi":368,"put_oi":0},{"strike":41950.0,"call_gex_1pct":830014.2498618142,"put_gex_1pct":0.0,"net_gex_1pct":830014.2498618142,"gross_gex_1pct":830014.2498618142,"call_oi":159,"put_oi":0},{"strike":42000.0,"call_gex_1pct":19697897.45245796,"put_gex_1pct":0.0,"net_gex_1pct":19697897.45245796,"gross_gex_1pct":19697897.45245796,"call_oi":4135,"put_oi":0},{"strike":42050.0,"call_gex_1pct":3243574.929958527,"put_gex_1pct":0.0,"net_gex_1pct":3243574.929958527,"gross_gex_1pct":3243574.929958527,"call_oi":823,"put_oi":0},{"strike":42100.0,"call_gex_1pct":1492447.987325891,"put_gex_1pct":0.0,"net_gex_1pct":1492447.987325891,"gross_gex_1pct":1492447.987325891,"call_oi":387,"put_oi":0},{"strike":42150.0,"call_gex_1pct":546362.6377952452,"put_gex_1pct":0.0,"net_gex_1pct":546362.6377952452,"gross_gex_1pct":546362.6377952452,"call_oi":182,"put_oi":0},{"strike":42200.0,"call_gex_1pct":1629163.477482402,"put_gex_1pct":0.0,"net_gex_1pct":1629163.477482402,"gross_gex_1pct":1629163.477482402,"call_oi":647,"put_oi":0},{"strike":42250.0,"call_gex_1pct":1156252.7828434175,"put_gex_1pct":0.0,"net_gex_1pct":1156252.7828434175,"gross_gex_1pct":1156252.7828434175,"call_oi":469,"put_oi":0},{"strike":42300.0,"call_gex_1pct":994762.7492143107,"put_gex_1pct":0.0,"net_gex_1pct":994762.7492143107,"gross_gex_1pct":994762.7492143107,"call_oi":412,"put_oi":0},{"strike":42350.0,"call_gex_1pct":330390.0550364922,"put_gex_1pct":0.0,"net_gex_1pct":330390.0550364922,"gross_gex_1pct":330390.0550364922,"call_oi":171,"put_oi":0},{"strike":42400.0,"call_gex_1pct":452429.62090655306,"put_gex_1pct":0.0,"net_gex_1pct":452429.62090655306,"gross_gex_1pct":452429.62090655306,"call_oi":239,"put_oi":0},{"strike":42450.0,"call_gex_1pct":235610.02047658362,"put_gex_1pct":0.0,"net_gex_1pct":235610.02047658362,"gross_gex_1pct":235610.02047658362,"call_oi":127,"put_oi":0},{"strike":42500.0,"call_gex_1pct":3793613.395729443,"put_gex_1pct":0.0,"net_gex_1pct":3793613.395729443,"gross_gex_1pct":3793613.395729443,"call_oi":2086,"put_oi":0},{"strike":42550.0,"call_gex_1pct":340588.5004887384,"put_gex_1pct":0.0,"net_gex_1pct":340588.5004887384,"gross_gex_1pct":340588.5004887384,"call_oi":191,"put_oi":0},{"strike":42600.0,"call_gex_1pct":2719514.3907328183,"put_gex_1pct":0.0,"net_gex_1pct":2719514.3907328183,"gross_gex_1pct":2719514.3907328183,"call_oi":1555,"put_oi":0},{"strike":42650.0,"call_gex_1pct":221319.16509136604,"put_gex_1pct":0.0,"net_gex_1pct":221319.16509136604,"gross_gex_1pct":221319.16509136604,"call_oi":129,"put_oi":0},{"strike":42700.0,"call_gex_1pct":1218814.9854875915,"put_gex_1pct":0.0,"net_gex_1pct":1218814.9854875915,"gross_gex_1pct":1218814.9854875915,"call_oi":724,"put_oi":0},{"strike":42750.0,"call_gex_1pct":383315.45172271185,"put_gex_1pct":0.0,"net_gex_1pct":383315.45172271185,"gross_gex_1pct":383315.45172271185,"call_oi":232,"put_oi":0},{"strike":42800.0,"call_gex_1pct":3811555.758523343,"put_gex_1pct":0.0,"net_gex_1pct":3811555.758523343,"gross_gex_1pct":3811555.758523343,"call_oi":2350,"put_oi":0},{"strike":42850.0,"call_gex_1pct":308956.2475502561,"put_gex_1pct":0.0,"net_gex_1pct":308956.2475502561,"gross_gex_1pct":308956.2475502561,"call_oi":194,"put_oi":0},{"strike":42900.0,"call_gex_1pct":351909.713504991,"put_gex_1pct":0.0,"net_gex_1pct":351909.713504991,"gross_gex_1pct":351909.713504991,"call_oi":225,"put_oi":0},{"strike":42950.0,"call_gex_1pct":308808.2407063817,"put_gex_1pct":0.0,"net_gex_1pct":308808.2407063817,"gross_gex_1pct":308808.2407063817,"call_oi":201,"put_oi":0},{"strike":43000.0,"call_gex_1pct":6622060.893391893,"put_gex_1pct":0.0,"net_gex_1pct":6622060.893391893,"gross_gex_1pct":6622060.893391893,"call_oi":4387,"put_oi":0},{"strike":43050.0,"call_gex_1pct":295187.54830862035,"put_gex_1pct":0.0,"net_gex_1pct":295187.54830862035,"gross_gex_1pct":295187.54830862035,"call_oi":199,"put_oi":0},{"strike":43100.0,"call_gex_1pct":567151.1773931741,"put_gex_1pct":0.0,"net_gex_1pct":567151.1773931741,"gross_gex_1pct":567151.1773931741,"call_oi":389,"put_oi":0},{"strike":43150.0,"call_gex_1pct":248223.20005599418,"put_gex_1pct":0.0,"net_gex_1pct":248223.20005599418,"gross_gex_1pct":248223.20005599418,"call_oi":232,"put_oi":0},{"strike":43200.0,"call_gex_1pct":1777668.3789151672,"put_gex_1pct":0.0,"net_gex_1pct":1777668.3789151672,"gross_gex_1pct":1777668.3789151672,"call_oi":1690,"put_oi":0},{"strike":43250.0,"call_gex_1pct":263751.0911719898,"put_gex_1pct":0.0,"net_gex_1pct":263751.0911719898,"gross_gex_1pct":263751.0911719898,"call_oi":255,"put_oi":0},{"strike":43300.0,"call_gex_1pct":439447.1055580269,"put_gex_1pct":0.0,"net_gex_1pct":439447.1055580269,"gross_gex_1pct":439447.1055580269,"call_oi":432,"put_oi":0},{"strike":43350.0,"call_gex_1pct":112069.33541683508,"put_gex_1pct":0.0,"net_gex_1pct":112069.33541683508,"gross_gex_1pct":112069.33541683508,"call_oi":112,"put_oi":0},{"strike":43400.0,"call_gex_1pct":138806.3655577012,"put_gex_1pct":0.0,"net_gex_1pct":138806.3655577012,"gross_gex_1pct":138806.3655577012,"call_oi":141,"put_oi":0},{"strike":43450.0,"call_gex_1pct":90088.38353563024,"put_gex_1pct":0.0,"net_gex_1pct":90088.38353563024,"gross_gex_1pct":90088.38353563024,"call_oi":93,"put_oi":0},{"strike":43500.0,"call_gex_1pct":588219.2101720669,"put_gex_1pct":0.0,"net_gex_1pct":588219.2101720669,"gross_gex_1pct":588219.2101720669,"call_oi":617,"put_oi":0},{"strike":43550.0,"call_gex_1pct":82580.23336273592,"put_gex_1pct":0.0,"net_gex_1pct":82580.23336273592,"gross_gex_1pct":82580.23336273592,"call_oi":88,"put_oi":0},{"strike":43600.0,"call_gex_1pct":480403.31384743284,"put_gex_1pct":0.0,"net_gex_1pct":480403.31384743284,"gross_gex_1pct":480403.31384743284,"call_oi":520,"put_oi":0},{"strike":43650.0,"call_gex_1pct":52760.432538940164,"put_gex_1pct":0.0,"net_gex_1pct":52760.432538940164,"gross_gex_1pct":52760.432538940164,"call_oi":58,"put_oi":0},{"strike":43700.0,"call_gex_1pct":120041.12060162073,"put_gex_1pct":0.0,"net_gex_1pct":120041.12060162073,"gross_gex_1pct":120041.12060162073,"call_oi":134,"put_oi":0},{"strike":43750.0,"call_gex_1pct":79410.61580164649,"put_gex_1pct":0.0,"net_gex_1pct":79410.61580164649,"gross_gex_1pct":79410.61580164649,"call_oi":90,"put_oi":0},{"strike":43800.0,"call_gex_1pct":299868.3681419839,"put_gex_1pct":0.0,"net_gex_1pct":299868.3681419839,"gross_gex_1pct":299868.3681419839,"call_oi":345,"put_oi":0},{"strike":43850.0,"call_gex_1pct":97623.73521359023,"put_gex_1pct":0.0,"net_gex_1pct":97623.73521359023,"gross_gex_1pct":97623.73521359023,"call_oi":114,"put_oi":0},{"strike":43900.0,"call_gex_1pct":134168.0292796892,"put_gex_1pct":0.0,"net_gex_1pct":134168.0292796892,"gross_gex_1pct":134168.0292796892,"call_oi":159,"put_oi":0},{"strike":43950.0,"call_gex_1pct":88149.59854422833,"put_gex_1pct":0.0,"net_gex_1pct":88149.59854422833,"gross_gex_1pct":88149.59854422833,"call_oi":106,"put_oi":0},{"strike":44000.0,"call_gex_1pct":719667.1124121358,"put_gex_1pct":0.0,"net_gex_1pct":719667.1124121358,"gross_gex_1pct":719667.1124121358,"call_oi":878,"put_oi":0},{"strike":44050.0,"call_gex_1pct":15352.264660507333,"put_gex_1pct":0.0,"net_gex_1pct":15352.264660507333,"gross_gex_1pct":15352.264660507333,"call_oi":19,"put_oi":0},{"strike":44100.0,"call_gex_1pct":68510.47895987991,"put_gex_1pct":0.0,"net_gex_1pct":68510.47895987991,"gross_gex_1pct":68510.47895987991,"call_oi":86,"put_oi":0},{"strike":44150.0,"call_gex_1pct":30635.13843006142,"put_gex_1pct":0.0,"net_gex_1pct":30635.13843006142,"gross_gex_1pct":30635.13843006142,"call_oi":39,"put_oi":0},{"strike":44200.0,"call_gex_1pct":166550.66917489888,"put_gex_1pct":0.0,"net_gex_1pct":166550.66917489888,"gross_gex_1pct":166550.66917489888,"call_oi":215,"put_oi":0},{"strike":44250.0,"call_gex_1pct":22157.136496001964,"put_gex_1pct":0.0,"net_gex_1pct":22157.136496001964,"gross_gex_1pct":22157.136496001964,"call_oi":29,"put_oi":0},{"strike":44300.0,"call_gex_1pct":62554.06447327831,"put_gex_1pct":0.0,"net_gex_1pct":62554.06447327831,"gross_gex_1pct":62554.06447327831,"call_oi":83,"put_oi":0},{"strike":44350.0,"call_gex_1pct":69147.32328608815,"put_gex_1pct":0.0,"net_gex_1pct":69147.32328608815,"gross_gex_1pct":69147.32328608815,"call_oi":93,"put_oi":0},{"strike":44400.0,"call_gex_1pct":34479.22946924495,"put_gex_1pct":0.0,"net_gex_1pct":34479.22946924495,"gross_gex_1pct":34479.22946924495,"call_oi":47,"put_oi":0},{"strike":44450.0,"call_gex_1pct":23888.689136063364,"put_gex_1pct":0.0,"net_gex_1pct":23888.689136063364,"gross_gex_1pct":23888.689136063364,"call_oi":33,"put_oi":0},{"strike":44500.0,"call_gex_1pct":171458.44224405105,"put_gex_1pct":0.0,"net_gex_1pct":171458.44224405105,"gross_gex_1pct":171458.44224405105,"call_oi":240,"put_oi":0},{"strike":44550.0,"call_gex_1pct":30320.410750625953,"put_gex_1pct":0.0,"net_gex_1pct":30320.410750625953,"gross_gex_1pct":30320.410750625953,"call_oi":43,"put_oi":0},{"strike":44600.0,"call_gex_1pct":36890.149870571244,"put_gex_1pct":0.0,"net_gex_1pct":36890.149870571244,"gross_gex_1pct":36890.149870571244,"call_oi":53,"put_oi":0},{"strike":44650.0,"call_gex_1pct":10994.376420560195,"put_gex_1pct":0.0,"net_gex_1pct":10994.376420560195,"gross_gex_1pct":10994.376420560195,"call_oi":16,"put_oi":0},{"strike":44700.0,"call_gex_1pct":180466.12795466857,"put_gex_1pct":0.0,"net_gex_1pct":180466.12795466857,"gross_gex_1pct":180466.12795466857,"call_oi":266,"put_oi":0},{"strike":44750.0,"call_gex_1pct":24787.10780894063,"put_gex_1pct":0.0,"net_gex_1pct":24787.10780894063,"gross_gex_1pct":24787.10780894063,"call_oi":37,"put_oi":0},{"strike":44800.0,"call_gex_1pct":40356.168322823694,"put_gex_1pct":0.0,"net_gex_1pct":40356.168322823694,"gross_gex_1pct":40356.168322823694,"call_oi":61,"put_oi":0},{"strike":44850.0,"call_gex_1pct":8494.240907375646,"put_gex_1pct":0.0,"net_gex_1pct":8494.240907375646,"gross_gex_1pct":8494.240907375646,"call_oi":13,"put_oi":0},{"strike":44900.0,"call_gex_1pct":19361.904877684057,"put_gex_1pct":0.0,"net_gex_1pct":19361.904877684057,"gross_gex_1pct":19361.904877684057,"call_oi":30,"put_oi":0},{"strike":44950.0,"call_gex_1pct":20401.69269482526,"put_gex_1pct":0.0,"net_gex_1pct":20401.69269482526,"gross_gex_1pct":20401.69269482526,"call_oi":32,"put_oi":0},{"strike":45000.0,"call_gex_1pct":4201211.783334529,"put_gex_1pct":0.0,"net_gex_1pct":4201211.783334529,"gross_gex_1pct":4201211.783334529,"call_oi":6670,"put_oi":0},{"strike":45050.0,"call_gex_1pct":10579.682845069163,"put_gex_1pct":0.0,"net_gex_1pct":10579.682845069163,"gross_gex_1pct":10579.682845069163,"call_oi":17,"put_oi":0},{"strike":45100.0,"call_gex_1pct":17833.58030720979,"put_gex_1pct":0.0,"net_gex_1pct":17833.58030720979,"gross_gex_1pct":17833.58030720979,"call_oi":29,"put_oi":0},{"strike":45150.0,"call_gex_1pct":5469.417498963872,"put_gex_1pct":0.0,"net_gex_1pct":5469.417498963872,"gross_gex_1pct":5469.417498963872,"call_oi":9,"put_oi":0},{"strike":45200.0,"call_gex_1pct":71473.35121365332,"put_gex_1pct":0.0,"net_gex_1pct":71473.35121365332,"gross_gex_1pct":71473.35121365332,"call_oi":119,"put_oi":0},{"strike":45250.0,"call_gex_1pct":9498.516533476271,"put_gex_1pct":0.0,"net_gex_1pct":9498.516533476271,"gross_gex_1pct":9498.516533476271,"call_oi":16,"put_oi":0},{"strike":45300.0,"call_gex_1pct":15724.648304640898,"put_gex_1pct":0.0,"net_gex_1pct":15724.648304640898,"gross_gex_1pct":15724.648304640898,"call_oi":45,"put_oi":0},{"strike":45350.0,"call_gex_1pct":6217.276431329037,"put_gex_1pct":0.0,"net_gex_1pct":6217.276431329037,"gross_gex_1pct":6217.276431329037,"call_oi":18,"put_oi":0},{"strike":45400.0,"call_gex_1pct":11267.813178583785,"put_gex_1pct":0.0,"net_gex_1pct":11267.813178583785,"gross_gex_1pct":11267.813178583785,"call_oi":33,"put_oi":0},{"strike":45450.0,"call_gex_1pct":4050.822326091847,"put_gex_1pct":0.0,"net_gex_1pct":4050.822326091847,"gross_gex_1pct":4050.822326091847,"call_oi":12,"put_oi":0},{"strike":45500.0,"call_gex_1pct":35378.6899469691,"put_gex_1pct":0.0,"net_gex_1pct":35378.6899469691,"gross_gex_1pct":35378.6899469691,"call_oi":106,"put_oi":0},{"strike":45550.0,"call_gex_1pct":3960.301142898078,"put_gex_1pct":0.0,"net_gex_1pct":3960.301142898078,"gross_gex_1pct":3960.301142898078,"call_oi":12,"put_oi":0},{"strike":45600.0,"call_gex_1pct":12075.257523873028,"put_gex_1pct":0.0,"net_gex_1pct":12075.257523873028,"gross_gex_1pct":12075.257523873028,"call_oi":37,"put_oi":0},{"strike":45700.0,"call_gex_1pct":7342.193002152046,"put_gex_1pct":0.0,"net_gex_1pct":7342.193002152046,"gross_gex_1pct":7342.193002152046,"call_oi":23,"put_oi":0},{"strike":45800.0,"call_gex_1pct":8433.45514340004,"put_gex_1pct":0.0,"net_gex_1pct":8433.45514340004,"gross_gex_1pct":8433.45514340004,"call_oi":27,"put_oi":0},{"strike":45900.0,"call_gex_1pct":5502.9406634243605,"put_gex_1pct":0.0,"net_gex_1pct":5502.9406634243605,"gross_gex_1pct":5502.9406634243605,"call_oi":18,"put_oi":0},{"strike":46000.0,"call_gex_1pct":80217.80195365482,"put_gex_1pct":0.0,"net_gex_1pct":80217.80195365482,"gross_gex_1pct":80217.80195365482,"call_oi":268,"put_oi":0},{"strike":46100.0,"call_gex_1pct":2638.284937505627,"put_gex_1pct":0.0,"net_gex_1pct":2638.284937505627,"gross_gex_1pct":2638.284937505627,"call_oi":9,"put_oi":0},{"strike":46200.0,"call_gex_1pct":1148.7052957906574,"put_gex_1pct":0.0,"net_gex_1pct":1148.7052957906574,"gross_gex_1pct":1148.7052957906574,"call_oi":4,"put_oi":0},{"strike":46300.0,"call_gex_1pct":844.2329716949841,"put_gex_1pct":0.0,"net_gex_1pct":844.2329716949841,"gross_gex_1pct":844.2329716949841,"call_oi":3,"put_oi":0},{"strike":46400.0,"call_gex_1pct":3034.212727345775,"put_gex_1pct":0.0,"net_gex_1pct":3034.212727345775,"gross_gex_1pct":3034.212727345775,"call_oi":11,"put_oi":0},{"strike":46500.0,"call_gex_1pct":211760.15699970053,"put_gex_1pct":0.0,"net_gex_1pct":211760.15699970053,"gross_gex_1pct":211760.15699970053,"call_oi":783,"put_oi":0},{"strike":46600.0,"call_gex_1pct":1060.9272363160162,"put_gex_1pct":0.0,"net_gex_1pct":1060.9272363160162,"gross_gex_1pct":1060.9272363160162,"call_oi":4,"put_oi":0},{"strike":46700.0,"call_gex_1pct":4423.121145383287,"put_gex_1pct":0.0,"net_gex_1pct":4423.121145383287,"gross_gex_1pct":4423.121145383287,"call_oi":17,"put_oi":0},{"strike":46800.0,"call_gex_1pct":10211.809652737791,"put_gex_1pct":0.0,"net_gex_1pct":10211.809652737791,"gross_gex_1pct":10211.809652737791,"call_oi":40,"put_oi":0},{"strike":46900.0,"call_gex_1pct":2756.1580758767996,"put_gex_1pct":0.0,"net_gex_1pct":2756.1580758767996,"gross_gex_1pct":2756.1580758767996,"call_oi":11,"put_oi":0},{"strike":47000.0,"call_gex_1pct":19923.635387939077,"put_gex_1pct":0.0,"net_gex_1pct":19923.635387939077,"gross_gex_1pct":19923.635387939077,"call_oi":81,"put_oi":0},{"strike":47100.0,"call_gex_1pct":1449.131995178881,"put_gex_1pct":0.0,"net_gex_1pct":1449.131995178881,"gross_gex_1pct":1449.131995178881,"call_oi":6,"put_oi":0},{"strike":47200.0,"call_gex_1pct":4506.943291369051,"put_gex_1pct":0.0,"net_gex_1pct":4506.943291369051,"gross_gex_1pct":4506.943291369051,"call_oi":19,"put_oi":0},{"strike":47300.0,"call_gex_1pct":2097.196953529093,"put_gex_1pct":0.0,"net_gex_1pct":2097.196953529093,"gross_gex_1pct":2097.196953529093,"call_oi":9,"put_oi":0},{"strike":47400.0,"call_gex_1pct":8242.551482687724,"put_gex_1pct":0.0,"net_gex_1pct":8242.551482687724,"gross_gex_1pct":8242.551482687724,"call_oi":36,"put_oi":0},{"strike":47500.0,"call_gex_1pct":2925.210463856995,"put_gex_1pct":0.0,"net_gex_1pct":2925.210463856995,"gross_gex_1pct":2925.210463856995,"call_oi":13,"put_oi":0},{"strike":47600.0,"call_gex_1pct":1105.9321248925723,"put_gex_1pct":0.0,"net_gex_1pct":1105.9321248925723,"gross_gex_1pct":1105.9321248925723,"call_oi":5,"put_oi":0},{"strike":47700.0,"call_gex_1pct":3914.3874826108877,"put_gex_1pct":0.0,"net_gex_1pct":3914.3874826108877,"gross_gex_1pct":3914.3874826108877,"call_oi":18,"put_oi":0},{"strike":47800.0,"call_gex_1pct":2138.5055394120795,"put_gex_1pct":0.0,"net_gex_1pct":2138.5055394120795,"gross_gex_1pct":2138.5055394120795,"call_oi":10,"put_oi":0},{"strike":47900.0,"call_gex_1pct":3365.3777499334187,"put_gex_1pct":0.0,"net_gex_1pct":3365.3777499334187,"gross_gex_1pct":3365.3777499334187,"call_oi":16,"put_oi":0},{"strike":48000.0,"call_gex_1pct":2896.8628090833686,"put_gex_1pct":0.0,"net_gex_1pct":2896.8628090833686,"gross_gex_1pct":2896.8628090833686,"call_oi":14,"put_oi":0},{"strike":48200.0,"call_gex_1pct":2604.691437613703,"put_gex_1pct":0.0,"net_gex_1pct":2604.691437613703,"gross_gex_1pct":2604.691437613703,"call_oi":13,"put_oi":0},{"strike":48300.0,"call_gex_1pct":1972.1348445299323,"put_gex_1pct":0.0,"net_gex_1pct":1972.1348445299323,"gross_gex_1pct":1972.1348445299323,"call_oi":10,"put_oi":0},{"strike":48400.0,"call_gex_1pct":582.4484882469382,"put_gex_1pct":0.0,"net_gex_1pct":582.4484882469382,"gross_gex_1pct":582.4484882469382,"call_oi":3,"put_oi":0},{"strike":48500.0,"call_gex_1pct":955.8294054274485,"put_gex_1pct":0.0,"net_gex_1pct":955.8294054274485,"gross_gex_1pct":955.8294054274485,"call_oi":5,"put_oi":0},{"strike":48600.0,"call_gex_1pct":188.25974513610157,"put_gex_1pct":0.0,"net_gex_1pct":188.25974513610157,"gross_gex_1pct":188.25974513610157,"call_oi":1,"put_oi":0},{"strike":48700.0,"call_gex_1pct":60078.77744184875,"put_gex_1pct":0.0,"net_gex_1pct":60078.77744184875,"gross_gex_1pct":60078.77744184875,"call_oi":324,"put_oi":0}]}
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
| 外資 | 115,050 | 114,488 | +562 | 87,732 | 88,333 | -601 | +1,163 | TAIFEX Proxy |
| 投信 | 3 | 0 | +3 | 0 | 0 | +0 | +3 | TAIFEX Proxy |
| 自營商 | 96,592 | 105,243 | -8,651 | 39,027 | 40,564 | -1,537 | -7,114 | TAIFEX Proxy |
| 三大法人合計 | 211,645 | 219,731 | -8,086 | 126,759 | 128,897 | -2,138 | -5,948 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 16.61 | 16.27 | +0.35 | 8.81 | 8.89 | -0.09 | +0.44 | TAIFEX Proxy |
| 投信 | 0.00 | 0.00 | +0.00 | 0.00 | 0.00 | +0 | +0.00 | TAIFEX Proxy |
| 自營商 | 16.33 | 18.20 | -1.87 | 5.92 | 5.81 | +0.11 | -1.98 | TAIFEX Proxy |
| 三大法人合計 | 32.95 | 34.47 | -1.52 | 14.73 | 14.70 | +0.02 | -1.54 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,296 | TAIFEX Proxy |
| 買權空方 OI | 15,231 | TAIFEX Proxy |
| 買權多空淨 OI | -2,935 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | 沿用前版（原來源：換月基準重建） |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,459 | TAIFEX Proxy |
| 賣權空方 OI | 10,621 | TAIFEX Proxy |
| 賣權多空淨 OI | -162 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | 沿用前版（原來源：換月基準重建） |
- 資料日期：買權 2026-11-19／賣權 2026-11-19 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | unavailable | — | 歷史快照／比較資料不可用 |
| 買權前十大 | unavailable | — | 歷史快照／比較資料不可用 |
| 賣權前十大 | unavailable | — | 歷史快照／比較資料不可用 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-19；本次報告產製時間：2026-11-20 12:35:47；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 保護：4 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：97 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (3)：options.pos_change, futures.top10_change, options.top10_change

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
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-19 非今日 2026-11-20，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：主力到期月份已由 202611 換至 202611F3；僅比較前後快照中相同主力月份的共同合約，不跨月份相減
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -243.1 | -99,219 | +1,438 | +2,657 | +562 | -601 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +43.9 | +91,791 | -1,782 | +0 | +3 | +0 | 趨勢偏多 | 趨勢偏多 | twse-proxy／TAIFEX Proxy |
| 自營商 | -233.0 | -1,455 | -16 | -366 | -8,651 | -1,537 | 趨勢偏空 | 對沖避險 | twse-proxy／TAIFEX Proxy |
