# DATA_REPORT_20261117

- 報告日期：`2026-11-18`
- T0 交易日期：`2026-11-17`
- 首次資料產出時間：`2026-11-18 08:43:32`
- 本次更新開始時間：`2026-11-18 08:43:32`
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
| 加權指數 | 40,092.11 | 點 | twse-proxy |
| 開盤 | 40,546.64 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 41,533.84 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 39,786.45 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 40,092.11 | 點 | twse-proxy |
| 漲跌點數 | -947.97 | 點 | twse-proxy |
| 漲跌幅 | -2.31 | % | twse-proxy |
| 成交金額 | 10,128.7 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 234 | twse-proxy |
| 下跌家數 | 789 | twse-proxy |
| 平盤家數 | 61 | twse-proxy |
| 漲停家數 | 6 | twse-proxy |
| 跌停家數 | 30 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 162 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 651 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 54 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 5 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 43 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -380.9 | 億元 | twse-proxy /institutional |
| 投信 | -38.2 | 億元 | twse-proxy /institutional |
| 自營商 | -157.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -576.1 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `Blave 上市市場融資維持率估算（當日暫估；資料日期：2026-11-17；自建計算備援）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 6,691.6 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -230.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 242,036 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -14,557 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 153.72 | % | Blave 上市市場融資維持率估算（當日暫估；資料日期：2026-11-17；自建計算備援） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 33,415,477 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,360,770.599 | 2,162,045.778 | 20,522,816.377 | 張 |
| 借券賣出增減 | -55,008.922 | -30,580.178 | -85,589.1 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261117`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-18T08:43:59+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261117`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-18T08:44:01+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,128.7 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,770.4 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 11,899.1 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,340.53 | -76.06 | -1.03 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,328.38 | -181.38 | -0.74 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,001.79 | -195.37 | -0.72 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,759.42 | -848.75 | -1.64 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,642.88 | 32.23 | +0.34 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 25.46 | 2.55 | +11.13 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,263.14 | -398.88 | -0.67 | 2026-11-18 | 2026-11-18T00:44:01+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,087.43 | -13.07 | -0.26 | 2026-11-18 | 2026-11-18T00:44:01+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 23,753.84 | 116.24 | +0.49 | 2026-11-16 | 2026-11-18T00:44:01+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,602.57 | -31.78 | -0.87 | 2026-11-16 | 2026-11-18T00:44:01+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,690.78 | -278.01 | -2.53 | 2026-11-16 | 2026-11-18T00:44:01+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,408.00 | -31.00 | -0.42 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,433.50 | 149.25 | +0.55 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,942.00 | -728.00 | -1.41 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,719.80 | -31.60 | -1.15 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | -0.03 | 17-NOV-26 | 2026-11-18T00:44:23+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.10 | -0.02 | 2026-11-17 | 2026-11-18T00:44:23+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.50 | -0.01 | 17-NOV-26 | 2026-11-18T00:44:43+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.46 | -0.01 | 2026-11-17 | 2026-11-18T00:44:43+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.89 | -0.07 | -0.22 | 2026-11-18 | 2026-11-18T00:44:01+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.60 | 0.05 | +0.05 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.49 | -0.03 | -0.02 | 2026-11-18 | 2026-11-18T00:44:01+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,330.78 | -4.89 | -0.37 | 2026-11-18 | 2026-11-18T00:44:01+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 359.69 | -13.76 | -3.68 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 14.14 | -0.20 | -1.39 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 31.83 | -0.97 | -2.96 | 2026-11-17 | 2026-11-18T00:44:01+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 85.60 | -0.12 | -0.14 | 2026-11-17 | 2026-11-18T00:44:02+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,823.60 | -29.40 | -0.76 | 2026-11-17 | 2026-11-18T00:44:02+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 64,651.12 | -204.72 | -0.32 | 2026-11-18 | 2026-11-18T00:44:02+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：喊話董事會 黃仁勳打破沉默：輝達是我畢生心血
  - 來源：Yahoo 台股；發布時間：2026-11-17T16:38:10Z；台北時間：2026-11-18 00:38
  - 摘要：輝達（NVIDIA）前執行長黃仁勳卸任後首度公開發聲，坦承在個人生活中犯下嚴重錯誤，對造成董事會困擾深感懊悔，並承諾配合獨立調查。他強調，「輝達是我畢生的心血」，離任後持續收到員工、投資人、商業夥伴及客戶呼籲回歸的聲音，若董事會認定符合股東
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%8C%E8%BC%9D%E9%81%94%E6%98%AF%E6%88%91%E7%95%A2%E7%94%9F%E5%BF%83%E8%A1%80%E3%80%8D%E9%BB%83%E4%BB%81%E5%8B%B3%E6%89%93%E7%A0%B4%E6%B2%89%E9%BB%98-%E8%8B%A5%E8%91%A3%E4%BA%8B%E6%9C%83%E5%90%8C%E6%84%8F%E9%A1%98%E5%9B%9E%E9%8D%8B%E6%93%94%E4%BB%BBceo-164236299.html
- 事件2：投顧總座示警還要測底 明年台股極端情境恐下探32K
  - 來源：Yahoo 台股；發布時間：2026-11-17T22:00:02Z；台北時間：2026-11-18 06:00
  - 摘要：台股近期走勢大起大落，短短一個多月重挫約12,000點，市場原先期待年底挑戰5萬點，恐怕要多點耐心。群益投顧總經理范振鴻直言，台股要上攻到5萬點，「明年比較有機會」。根據群益投顧預估，2027年台股指數區間為35,000至50,000點。至
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E5%A4%A7%E8%80%83%E9%A9%973-%E5%8F%B0%E8%82%A11%E5%80%8B%E6%9C%88%E7%8B%82%E6%AE%BA12-000%E9%BB%9E-%E7%BE%A4%E7%9B%8A%E6%8A%95%E9%A1%A7%E7%B8%BD%E5%BA%A7%E7%A4%BA%E8%AD%A6%E9%82%84%E8%A6%81%E6%B8%AC%E5%BA%95-5%E8%90%AC%E9%BB%9E%E7%AD%89%E6%98%8E%E5%B9%B4-220002141.html
- 事件3：美股走低、道瓊尾盤一度摔千點 台積電ADR挫3.6%
  - 來源：Yahoo 台股；發布時間：2026-11-17T21:48:08Z；台北時間：2026-11-18 05:48
  - 摘要：美股週二重挫，道瓊跌848.75點、標普跌破200日線；VIX升11.13%至25.46 美國收緊輝達等AI晶片出口管制，5國出口須先獲許可，市場關注APEC川習會 輝達Q3營收1158.4億美元、EPS2.68美元優於預期，盤後漲約3%；
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E7%9B%A4%E5%BE%8C-%E9%81%93%E7%93%8A%E5%B0%BE%E7%9B%A4-%E5%BA%A6%E7%8B%82%E7%80%89%E9%80%BE1000%E9%BB%9E-%E6%A8%99%E6%99%AE%E5%89%B57%E6%9C%88%E5%BA%95%E4%BE%86%E6%9C%80%E4%BD%8E%E6%94%B6%E7%9B%A4-%E8%BC%9D%E9%81%94%E8%B2%A1%E5%A0%B1%E5%85%AC%E5%B8%83-214808690.html
- 事件4：台玻淨利暴增28750% 卻遭外資連三砍淪賣超王
  - 來源：Yahoo 台股；發布時間：2026-11-17T12:30:00Z；台北時間：2026-11-17 20:30
  - 摘要：[FTNN新聞網]記者邱梓欣／綜合報導台股今（17）日續延低迷氣勢，一度失守4萬關卡，終場下跌947.97點，勉強挽回以40,092.11點作收，跌幅2.31％，成交量9617.95...
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3%E9%96%83%E8%BE%AD%E8%BC%9D%E9%81%94%E8%A1%9D%E6%93%8A-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E9%81%AD%E5%A4%96%E8%B3%87%E6%92%A4%E5%87%BA668%E5%84%84%E5%A4%A7%E5%A4%B1%E8%A1%80-%E9%80%99%E6%AA%94%E7%8E%BB%E7%92%83%E5%A4%A7%E5%BB%A0-9%E6%9C%88%E6%B7%A8%E5%88%A9%E6%9A%B4%E5%A2%9E2-8%E8%90%AC-123000271.html
- 事件5：新台幣昨觸33元關卡 午後大逆轉收在當日最高價
  - 來源：Yahoo 台股；發布時間：2026-11-17T22:37:04Z；台北時間：2026-11-18 06:37
  - 摘要：外資持續賣超台股，新台幣匯率卻出現反轉，外資昨（17）日賣超台股380.9億元，不過，新台幣兌美元匯率並未跟著走貶，反而在午後出現外資匯入，終場以32.85元、當日最高價作收，升值3.6分，成交金額達38億美元。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%AE%E8%A1%8C%E5%8A%9B%E5%AE%8833%E9%97%9C%E5%8D%A1-%E5%8F%B0%E5%B9%A3%E9%80%86%E5%8B%A2%E8%B5%B0%E9%AB%98-17%E6%97%A5%E6%94%B632-85%E5%85%83%E5%85%A8%E6%97%A5%E6%9C%80%E9%AB%98%E5%83%B9-223704367.html
- 事件6：三家純網銀累積虧損收斂 LINE Bank前9月虧轉盈
  - 來源：Yahoo 台股；發布時間：2026-11-17T13:11:54Z；台北時間：2026-11-17 21:11
  - 摘要：（中央社記者高華謙台北2026年11月17日電）金管會統計今年前9月純網銀營運績效，3家純網銀中僅LINEBank維持稅前盈餘，將來銀行與樂天銀行仍處虧損，但LINE Bank與樂天銀行累積虧損均同步收斂。金管會表示，3家純網銀業務持續發展
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E7%AE%A1%E6%9C%83-3%E5%AE%B6%E7%B4%94%E7%B6%B2%E9%8A%80%E6%A5%AD%E5%8B%99%E8%A6%8F%E6%A8%A1%E6%8C%81%E7%BA%8C%E6%88%90%E9%95%B7-%E7%B4%AF%E7%A9%8D%E8%99%A7%E6%90%8D%E6%94%B6%E6%96%82-131154307.html
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
- 事件10：Lisa Cook lawyer signals Fed governor won't attend Trump committee's hearing
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 16:03:38 GMT；台北時間：2026-11-18 00:03
  - 摘要：Cook's attorney sounded more hostile than ever in his first known letter to be sent in the matter since the GOP's drubbing in the Nov. 3 midterm elect
  - 原文連結：https://www.cnbc.com/2026/11/17/lisa-cook-trump-fed-committee-hearing.html
- 事件11：St. Louis Fed's Musalem says four more rate hikes may be needed in coming months
  - 來源：CNBC；發布時間：Tue, 17 Nov 2026 13:40:54 GMT；台北時間：2026-11-17 21:40
  - 摘要：The forecast represents one of the most hawkish views among policymakers.
  - 原文連結：https://www.cnbc.com/2026/11/17/alberto-musalem-fed-interest-rates.html
- 事件12：Want to earn 5% on shorter-term Treasurys again? Watch for this shift.
  - 來源：MarketWatch；發布時間：Tue, 17 Nov 2026 22:08:00 GMT；台北時間：2026-11-18 06:08
  - 摘要：Don&#x2019;t rule out a half-point interest-rate hike in December, BofA Global&#x2019;s rates team said.
  - 原文連結：https://www.marketwatch.com/story/want-to-earn-5-on-shorter-term-treasurys-again-watch-for-this-shift-d6ff42f2?mod=mw_rss_topstories


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-17

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
| 開盤價 | 40,050 | 點 | TAIFEX Proxy |
| 最高價 | 40,451 | 點 | TAIFEX Proxy |
| 最低價 | 39,010 | 點 | TAIFEX Proxy |
| 收盤價 | 39,792 | 點 | TAIFEX Proxy |
| 漲跌點數 | -219 | 點 | TAIFEX Proxy |
| 漲跌幅 | -0.55 | % | TAIFEX Proxy |
| 成交量 | 48,144 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,451 / 39,010 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 17,052 | TAIFEX Proxy |
| 外資空方 OI | 114,948 | TAIFEX Proxy |
| 外資多空淨 OI | -97,896 | TAIFEX Proxy |
| 投信多方 OI | 94,566 | TAIFEX Proxy |
| 投信空方 OI | 3,340 | TAIFEX Proxy |
| 投信多空淨 OI | +91,226 | TAIFEX Proxy |
| 自營商多方 OI | 5,052 | TAIFEX Proxy |
| 自營商空方 OI | 5,488 | TAIFEX Proxy |
| 自營商多空淨 OI | -436 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,670 | TAIFEX Proxy |
| 三大法人合計空方 OI | 123,776 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,106 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,109 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -1,180 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,595 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 11,821 | TAIFEX Proxy |
| 前十大交易人空方 OI | 13,502 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,681 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-13→2026-11-17) | -21,237 | TAIFEX Proxy snapshots (2026-11-16) |
- 資料日期：2026-11-17 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 153,931 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 155,075 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -1,144 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 31,220 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 31,285 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -65 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,079 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -1,180 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -1,180 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,820 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -333 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,487 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -4,144 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -398 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -341.2 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -31.8 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,073 | TAIFEX Proxy |
| 加權指數價格 | 40,092.11 | twse-proxy |
| 台指期與加權指數價差 | -19.11 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | -0.05 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | -19.11 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -281 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,073 | 39,792 | +281 | TAIFEX Proxy |
| 成交量 | 138,833 | 48,144 | +90,689 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-3,884（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 153,931 | 155,075 | -1,144 | 31,220 | 31,285 | -65 | -1,079 | 17,052 | 114,948 | -97,896 | -1,109 | TAIFEX Proxy |
| 投信 | 33,611 | 34,791 | -1,180 | 0 | 0 | +0 | -1,180 | 94,566 | 3,340 | +91,226 | -1,180 | TAIFEX Proxy |
| 自營商 | 15,358 | 17,178 | -1,820 | 2,221 | 2,554 | -333 | -1,487 | 5,052 | 5,488 | -436 | -1,595 | TAIFEX Proxy |
| 三大法人合計 | 202,900 | 207,044 | -4,144 | 33,441 | 33,839 | -398 | -3,746 | 116,670 | 123,776 | -7,106 | -3,884 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 11,821 | TAIFEX Proxy |
| 前十大交易人空方 OI | 13,502 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | -1,681 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-13→2026-11-17) | -21,237 | TAIFEX Proxy snapshots (2026-11-16) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 25.75% | TAIFEX Proxy |
| 夜盤漲跌點數 | -219 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -65 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-17 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-18 08:43:32 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 258,518 | TAIFEX Proxy |
| Call 總未平倉量 OI | 142,228 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-16→2026-11-17) | +29,237 | TAIFEX Proxy snapshot bundle (2026-11-16→2026-11-17) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 206,995 | TAIFEX Proxy |
| Put 總未平倉量 OI | 78,316 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-16→2026-11-17) | +18,610 | TAIFEX Proxy snapshot bundle (2026-11-16→2026-11-17) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.25 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.82 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.55 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-16→2026-11-17) | -2.06 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-16→2026-11-17) | 0.29 | 百分點（pp） | TAIFEX Proxy |
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
| 外資 Call夜買 | 38,353 | TAIFEX Proxy |
| 外資 Call夜賣 | 38,714 | TAIFEX Proxy |
| 外資 Call夜淨 | -361 | TAIFEX Proxy |
| 外資 Put夜買 | 42,433 | TAIFEX Proxy |
| 外資 Put夜賣 | 43,290 | TAIFEX Proxy |
| 外資 Put夜淨 | -857 | TAIFEX Proxy |
| 外資 日盤淨總量 | +2,000 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +2,543 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,039 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 69,887 | TAIFEX Proxy |
| 自營商 Call日賣 | 73,892 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,005 | TAIFEX Proxy |
| 自營商 Put日買 | 64,742 | TAIFEX Proxy |
| 自營商 Put日賣 | 64,997 | TAIFEX Proxy |
| 自營商 Put日淨 | -255 | TAIFEX Proxy |
| 自營商 Call夜買 | 16,423 | TAIFEX Proxy |
| 自營商 Call夜賣 | 21,018 | TAIFEX Proxy |
| 自營商 Call夜淨 | -4,595 | TAIFEX Proxy |
| 自營商 Put夜買 | 21,410 | TAIFEX Proxy |
| 自營商 Put夜賣 | 23,146 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,736 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -3,750 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +590 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | +1,481 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 8,984 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,500 | 6,804 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 6,330 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 8,984 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 8,984 | 6.32% | TAIFEX Proxy |
| C2 | 43,500 | 6,804 | 4.78% | TAIFEX Proxy |
| C3 | 44,000 | 6,330 | 4.45% | TAIFEX Proxy |
| C4 | 45,000 | 4,173 | 2.93% | TAIFEX Proxy |
| C5 | 48,000 | 3,871 | 2.72% | TAIFEX Proxy |
| C6 | 43,000 | 3,538 | 2.49% | TAIFEX Proxy |
| C7 | 47,500 | 3,524 | 2.48% | TAIFEX Proxy |
| C8 | 46,500 | 3,464 | 2.44% | TAIFEX Proxy |
| C9 | 47,000 | 3,313 | 2.33% | TAIFEX Proxy |
| C10 | 44,500 | 2,816 | 1.98% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 11,788 | TAIFEX Proxy |
| Put OI 第2大履約價 | 38,000 | 2,997 | TAIFEX Proxy |
| Put OI 第3大履約價 | 40,000 | 2,889 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 11,788 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 11,788 | 15.05% | TAIFEX Proxy |
| P2 | 38,000 | 2,997 | 3.83% | TAIFEX Proxy |
| P3 | 40,000 | 2,889 | 3.69% | TAIFEX Proxy |
| P4 | 36,000 | 2,750 | 3.51% | TAIFEX Proxy |
| P5 | 37,000 | 2,241 | 2.86% | TAIFEX Proxy |
| P6 | 39,000 | 2,213 | 2.83% | TAIFEX Proxy |
| P7 | 42,000 | 1,959 | 2.5% | TAIFEX Proxy |
| P8 | 36,500 | 1,789 | 2.28% | TAIFEX Proxy |
| P9 | 35,000 | 1,568 | 2.0% | TAIFEX Proxy |
| P10 | 44,000 | 1,536 | 1.96% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 43,500 (+5,478) | TAIFEX Proxy snapshot bundle (2026-11-16→2026-11-17) |
| Call OI 減少最多的履約價（共同合約） | 47,500 (-4,350) | TAIFEX Proxy snapshot bundle (2026-11-16→2026-11-17) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 33,700 (+3,323) | TAIFEX Proxy snapshot bundle (2026-11-16→2026-11-17) |
| Put OI 減少最多的履約價（共同合約） | 40,600 (-406) | TAIFEX Proxy snapshot bundle (2026-11-16→2026-11-17) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | +0 | TAIFEX Proxy snapshots (2026-11-16) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 40,000.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-17 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 40,423.40 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-18 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 142,228 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 142,207 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 78,316 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 78,316 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-17 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：36,082.90～44,101.32
- 搜尋步長／計算次數：10.00／436
- 起點／終點 Net GEX：-3,801,951,827.36／19,592,740.00
- 搜尋區間最低／最高 Net GEX：-3,838,820,297.50／19,592,740.00
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-17","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":354,"delta_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":330,"delta_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":0,"delta_rows":214},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-17","source":"taifex_web","fallback_used":false,"index_duration_ms":2946,"index_error":null,"openapi_fetch_duration_ms":null,"attempts":[{"attempt":1,"duration_ms":3814,"source":"taifex_web","fallback":false,"http_status":200,"raw_rows":3535,"primary_error":null,"parser":{"input_rows":3535,"array_rows":3535,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3530,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3530,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":390,"recognized_type_rows":390,"valid_strike_rows":390,"valid_delta_rows":390,"parsed_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":366,"recognized_type_rows":366,"valid_strike_rows":366,"valid_delta_rows":366,"parsed_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":214,"recognized_type_rows":214,"valid_strike_rows":214,"valid_delta_rows":214,"parsed_rows":214},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"accepted_txo_rows":3530}],"parser":{"input_rows":3535,"array_rows":3535,"object_rows":0,"short_rows":4,"non_txo_rows":1,"txo_rows":3530,"invalid_contract_month":0,"invalid_expiry":0,"unknown_option_type_rows":0,"invalid_strike_rows":0,"invalid_delta_rows":0,"parsed_rows":3530,"per_expiry":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":390,"recognized_type_rows":390,"valid_strike_rows":390,"valid_delta_rows":390,"parsed_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":366,"recognized_type_rows":366,"valid_strike_rows":366,"valid_delta_rows":366,"parsed_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":214,"recognized_type_rows":214,"valid_strike_rows":214,"valid_delta_rows":214,"parsed_rows":214},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]},"final_rows":3530,"per_expiry_rows":[{"contract_month":"202611","expiry":"2026-11-18","raw_txo_rows":616,"recognized_type_rows":616,"valid_strike_rows":616,"valid_delta_rows":616,"parsed_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","raw_txo_rows":404,"recognized_type_rows":404,"valid_strike_rows":404,"valid_delta_rows":404,"parsed_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","raw_txo_rows":390,"recognized_type_rows":390,"valid_strike_rows":390,"valid_delta_rows":390,"parsed_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","raw_txo_rows":366,"recognized_type_rows":366,"valid_strike_rows":366,"valid_delta_rows":366,"parsed_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","raw_txo_rows":214,"recognized_type_rows":214,"valid_strike_rows":214,"valid_delta_rows":214,"parsed_rows":214},{"contract_month":"202612","expiry":"2026-12-16","raw_txo_rows":562,"recognized_type_rows":562,"valid_strike_rows":562,"valid_delta_rows":562,"parsed_rows":562},{"contract_month":"202701","expiry":"2027-01-20","raw_txo_rows":410,"recognized_type_rows":410,"valid_strike_rows":410,"valid_delta_rows":410,"parsed_rows":410},{"contract_month":"202703","expiry":"2027-03-17","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284},{"contract_month":"202706","expiry":"2027-06-16","raw_txo_rows":284,"recognized_type_rows":284,"valid_strike_rows":284,"valid_delta_rows":284,"parsed_rows":284}]}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：34,078.29～46,105.93
- 搜尋步長／計算次數：10.00／1204
- 起點／終點 Net GEX：-2,582,355,922.42／12,216,934,679.08
- 搜尋區間最低／最高 Net GEX：-3,838,812,811.14／15,914,954,341.83
- 正負號交叉次數：1
- 擴大區間診斷 Flip：40,423.39

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | -607,459,951.95 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 11,036,189,603.26 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 306 | 資料日期：2026-11-17 |
| 正 Net GEX 最大履約價 | 39,400 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 40,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：39,400（309,376,600.61 NT$）、39,300（269,347,372.20 NT$）、39,200（253,633,515.88 NT$）、39,500（159,343,095.99 NT$）、42,650（72,970,100.45 NT$）
- 負 Net GEX Top 5：40,000（-448,001,366.84 NT$）、38,000（-250,846,882.03 NT$）、38,800（-128,237,359.18 NT$）、38,500（-99,930,662.94 NT$）、37,000（-75,739,937.12 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-17","underlying":40092.11,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":-607459951.9515861,"gross_gex_1pct":11036189603.26167,"gamma_diagnostics":{"chain_rows":616,"delta_rows":616,"matched_strike_keys":616,"positive_oi_settlement_eligible":514,"invalid_oi":102,"invalid_settlement":0,"below_intrinsic":17,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":497},"formal_flip_diagnostics":{"search_lower_underlying":36082.899000000005,"search_upper_underlying":44101.321,"step":10,"evaluations":436,"start_net_gex_1pct":-3801951827.360597,"end_net_gex_1pct":19592740.004359562,"min_net_gex_1pct":-3838820297.4995594,"max_net_gex_1pct":19592740.004359562,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":40418.2935,"upper_underlying":40428.2935,"estimated_underlying":40423.38976462544,"lower_net_gex_1pct":-10473117.813340124,"upper_net_gex_1pct":10077459.095605303},"wide_range_flip_diagnostics":{"search_lower_underlying":34078.2935,"search_upper_underlying":46105.926499999994,"reference_underlying":40092.11,"step":10,"evaluations":1204,"start_net_gex_1pct":-2582355922.4198847,"end_net_gex_1pct":12216934679.076427,"min_net_gex_1pct":-3838812811.13995,"max_net_gex_1pct":15914954341.83318,"zero_crossings":1,"found":true,"selected_crossing_distance":331.2797646254403},"expiry_selection_diagnostics":{"requested_date":"2026-11-17","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":616},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":354,"delta_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":330,"delta_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":0,"delta_rows":214},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611","expiry":"2026-11-18","delta_contract_month":"202611","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-6091827.534824732,"net_gex_1pct":-6091827.534824732,"gross_gex_1pct":6091827.534824732,"call_oi":0,"put_oi":11788},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-135296.67855228522,"net_gex_1pct":-135296.67855228522,"gross_gex_1pct":135296.67855228522,"call_oi":0,"put_oi":254},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-31857.484597576025,"net_gex_1pct":-31857.484597576025,"gross_gex_1pct":31857.484597576025,"call_oi":0,"put_oi":58},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-120693.3490132877,"net_gex_1pct":-120693.3490132877,"gross_gex_1pct":120693.3490132877,"call_oi":0,"put_oi":213},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-33334.60892422495,"net_gex_1pct":-33334.60892422495,"gross_gex_1pct":33334.60892422495,"call_oi":0,"put_oi":57},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-24154.634414472963,"net_gex_1pct":-24154.634414472963,"gross_gex_1pct":24154.634414472963,"call_oi":0,"put_oi":40},{"strike":34300.0,"call_gex_1pct":0.0,"put_gex_1pct":-88584.75563634351,"net_gex_1pct":-88584.75563634351,"gross_gex_1pct":88584.75563634351,"call_oi":0,"put_oi":142},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-40621.77869304117,"net_gex_1pct":-40621.77869304117,"gross_gex_1pct":40621.77869304117,"call_oi":0,"put_oi":63},{"strike":34500.0,"call_gex_1pct":0.0,"put_gex_1pct":-97351.87200459404,"net_gex_1pct":-97351.87200459404,"gross_gex_1pct":97351.87200459404,"call_oi":0,"put_oi":146},{"strike":34600.0,"call_gex_1pct":0.0,"put_gex_1pct":-35185.861578411255,"net_gex_1pct":-35185.861578411255,"gross_gex_1pct":35185.861578411255,"call_oi":0,"put_oi":51},{"strike":34700.0,"call_gex_1pct":0.0,"put_gex_1pct":-68048.49975977975,"net_gex_1pct":-68048.49975977975,"gross_gex_1pct":68048.49975977975,"call_oi":0,"put_oi":71},{"strike":34800.0,"call_gex_1pct":0.0,"put_gex_1pct":-76427.31233257281,"net_gex_1pct":-76427.31233257281,"gross_gex_1pct":76427.31233257281,"call_oi":0,"put_oi":77},{"strike":34900.0,"call_gex_1pct":0.0,"put_gex_1pct":-104909.33712412084,"net_gex_1pct":-104909.33712412084,"gross_gex_1pct":104909.33712412084,"call_oi":0,"put_oi":102},{"strike":35000.0,"call_gex_1pct":0.0,"put_gex_1pct":-1672186.283217891,"net_gex_1pct":-1672186.283217891,"gross_gex_1pct":1672186.283217891,"call_oi":0,"put_oi":1568},{"strike":35100.0,"call_gex_1pct":0.0,"put_gex_1pct":-99582.93233818426,"net_gex_1pct":-99582.93233818426,"gross_gex_1pct":99582.93233818426,"call_oi":0,"put_oi":90},{"strike":35200.0,"call_gex_1pct":0.0,"put_gex_1pct":-121770.62697355043,"net_gex_1pct":-121770.62697355043,"gross_gex_1pct":121770.62697355043,"call_oi":0,"put_oi":106},{"strike":35300.0,"call_gex_1pct":0.0,"put_gex_1pct":-420122.63384096994,"net_gex_1pct":-420122.63384096994,"gross_gex_1pct":420122.63384096994,"call_oi":0,"put_oi":352},{"strike":35400.0,"call_gex_1pct":0.0,"put_gex_1pct":-153874.6380338666,"net_gex_1pct":-153874.6380338666,"gross_gex_1pct":153874.6380338666,"call_oi":0,"put_oi":124},{"strike":35500.0,"call_gex_1pct":0.0,"put_gex_1pct":-693362.4968041782,"net_gex_1pct":-693362.4968041782,"gross_gex_1pct":693362.4968041782,"call_oi":0,"put_oi":537},{"strike":35600.0,"call_gex_1pct":0.0,"put_gex_1pct":-244649.69027930612,"net_gex_1pct":-244649.69027930612,"gross_gex_1pct":244649.69027930612,"call_oi":0,"put_oi":127},{"strike":35700.0,"call_gex_1pct":0.0,"put_gex_1pct":-357211.7330726899,"net_gex_1pct":-357211.7330726899,"gross_gex_1pct":357211.7330726899,"call_oi":0,"put_oi":178},{"strike":35800.0,"call_gex_1pct":0.0,"put_gex_1pct":-289463.0220653432,"net_gex_1pct":-289463.0220653432,"gross_gex_1pct":289463.0220653432,"call_oi":0,"put_oi":122},{"strike":35900.0,"call_gex_1pct":0.0,"put_gex_1pct":-309451.8265532138,"net_gex_1pct":-309451.8265532138,"gross_gex_1pct":309451.8265532138,"call_oi":0,"put_oi":125},{"strike":36000.0,"call_gex_1pct":0.0,"put_gex_1pct":-7109995.714244958,"net_gex_1pct":-7109995.714244958,"gross_gex_1pct":7109995.714244958,"call_oi":0,"put_oi":2750},{"strike":36100.0,"call_gex_1pct":0.0,"put_gex_1pct":-789378.8042133943,"net_gex_1pct":-789378.8042133943,"gross_gex_1pct":789378.8042133943,"call_oi":0,"put_oi":263},{"strike":36200.0,"call_gex_1pct":0.0,"put_gex_1pct":-1230082.0412501467,"net_gex_1pct":-1230082.0412501467,"gross_gex_1pct":1230082.0412501467,"call_oi":0,"put_oi":260},{"strike":36300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1579826.609486157,"net_gex_1pct":-1579826.609486157,"gross_gex_1pct":1579826.609486157,"call_oi":0,"put_oi":291},{"strike":36400.0,"call_gex_1pct":0.0,"put_gex_1pct":-3917381.615551224,"net_gex_1pct":-3917381.615551224,"gross_gex_1pct":3917381.615551224,"call_oi":0,"put_oi":384},{"strike":36500.0,"call_gex_1pct":0.0,"put_gex_1pct":-26530107.966243498,"net_gex_1pct":-26530107.966243498,"gross_gex_1pct":26530107.966243498,"call_oi":0,"put_oi":1789},{"strike":36600.0,"call_gex_1pct":0.0,"put_gex_1pct":-5982206.685453601,"net_gex_1pct":-5982206.685453601,"gross_gex_1pct":5982206.685453601,"call_oi":0,"put_oi":323},{"strike":36700.0,"call_gex_1pct":0.0,"put_gex_1pct":-4953224.318505512,"net_gex_1pct":-4953224.318505512,"gross_gex_1pct":4953224.318505512,"call_oi":0,"put_oi":222},{"strike":36800.0,"call_gex_1pct":0.0,"put_gex_1pct":-13016276.800444337,"net_gex_1pct":-13016276.800444337,"gross_gex_1pct":13016276.800444337,"call_oi":0,"put_oi":505},{"strike":36900.0,"call_gex_1pct":0.0,"put_gex_1pct":-10101663.61517314,"net_gex_1pct":-10101663.61517314,"gross_gex_1pct":10101663.61517314,"call_oi":0,"put_oi":325},{"strike":37000.0,"call_gex_1pct":0.0,"put_gex_1pct":-75739937.11804184,"net_gex_1pct":-75739937.11804184,"gross_gex_1pct":75739937.11804184,"call_oi":0,"put_oi":2241},{"strike":37100.0,"call_gex_1pct":0.0,"put_gex_1pct":-10632292.56304553,"net_gex_1pct":-10632292.56304553,"gross_gex_1pct":10632292.56304553,"call_oi":0,"put_oi":280},{"strike":37200.0,"call_gex_1pct":0.0,"put_gex_1pct":-9506214.301307287,"net_gex_1pct":-9506214.301307287,"gross_gex_1pct":9506214.301307287,"call_oi":0,"put_oi":221},{"strike":37300.0,"call_gex_1pct":0.0,"put_gex_1pct":-14982079.098233307,"net_gex_1pct":-14982079.098233307,"gross_gex_1pct":14982079.098233307,"call_oi":0,"put_oi":325},{"strike":37400.0,"call_gex_1pct":0.0,"put_gex_1pct":-19688253.154675025,"net_gex_1pct":-19688253.154675025,"gross_gex_1pct":19688253.154675025,"call_oi":0,"put_oi":381},{"strike":37500.0,"call_gex_1pct":26633.017306898135,"put_gex_1pct":-53795428.431928866,"net_gex_1pct":-53768795.414621964,"gross_gex_1pct":53822061.44923577,"call_oi":1,"put_oi":985},{"strike":37600.0,"call_gex_1pct":0.0,"put_gex_1pct":-15635736.965634875,"net_gex_1pct":-15635736.965634875,"gross_gex_1pct":15635736.965634875,"call_oi":0,"put_oi":255},{"strike":37700.0,"call_gex_1pct":312064.02735605225,"put_gex_1pct":-18695140.93899688,"net_gex_1pct":-18383076.91164083,"gross_gex_1pct":19007204.966352932,"call_oi":6,"put_oi":283},{"strike":37800.0,"call_gex_1pct":0.0,"put_gex_1pct":-36995290.209317066,"net_gex_1pct":-36995290.209317066,"gross_gex_1pct":36995290.209317066,"call_oi":0,"put_oi":516},{"strike":37900.0,"call_gex_1pct":0.0,"put_gex_1pct":-22040479.59819596,"net_gex_1pct":-22040479.59819596,"gross_gex_1pct":22040479.59819596,"call_oi":0,"put_oi":284},{"strike":38000.0,"call_gex_1pct":959817.8709056857,"put_gex_1pct":-251806699.89671382,"net_gex_1pct":-250846882.02580813,"gross_gex_1pct":252766517.76761952,"call_oi":13,"put_oi":2997},{"strike":38100.0,"call_gex_1pct":82275.21743786556,"put_gex_1pct":-36578499.609458745,"net_gex_1pct":-36496224.39202088,"gross_gex_1pct":36660774.82689661,"call_oi":1,"put_oi":406},{"strike":38200.0,"call_gex_1pct":181108.65950726933,"put_gex_1pct":-50525861.34354053,"net_gex_1pct":-50344752.68403326,"gross_gex_1pct":50706970.003047794,"call_oi":2,"put_oi":523},{"strike":38300.0,"call_gex_1pct":100408.31062177688,"put_gex_1pct":-56760894.36390402,"net_gex_1pct":-56660486.053282246,"gross_gex_1pct":56861302.6745258,"call_oi":1,"put_oi":549},{"strike":38400.0,"call_gex_1pct":0.0,"put_gex_1pct":-35877583.477265194,"net_gex_1pct":-35877583.477265194,"gross_gex_1pct":35877583.477265194,"call_oi":0,"put_oi":326},{"strike":38500.0,"call_gex_1pct":1633817.2993577865,"put_gex_1pct":-101564480.24403802,"net_gex_1pct":-99930662.94468023,"gross_gex_1pct":103198297.5433958,"call_oi":14,"put_oi":869},{"strike":38550.0,"call_gex_1pct":0.0,"put_gex_1pct":-12707861.807235545,"net_gex_1pct":-12707861.807235545,"gross_gex_1pct":12707861.807235545,"call_oi":0,"put_oi":106},{"strike":38600.0,"call_gex_1pct":125302.75941720764,"put_gex_1pct":-48461918.84549235,"net_gex_1pct":-48336616.08607514,"gross_gex_1pct":48587221.604909554,"call_oi":1,"put_oi":393},{"strike":38650.0,"call_gex_1pct":389061.41117080295,"put_gex_1pct":-11453249.718584655,"net_gex_1pct":-11064188.307413852,"gross_gex_1pct":11842311.129755458,"call_oi":3,"put_oi":90},{"strike":38700.0,"call_gex_1pct":1066181.6908326535,"put_gex_1pct":-38388285.37855452,"net_gex_1pct":-37322103.68772187,"gross_gex_1pct":39454467.069387175,"call_oi":8,"put_oi":294},{"strike":38750.0,"call_gex_1pct":0.0,"put_gex_1pct":-22251718.124269076,"net_gex_1pct":-22251718.124269076,"gross_gex_1pct":22251718.124269076,"call_oi":0,"put_oi":165},{"strike":38800.0,"call_gex_1pct":1847863.3759462119,"put_gex_1pct":-130085222.55415235,"net_gex_1pct":-128237359.17820615,"gross_gex_1pct":131933085.93009856,"call_oi":13,"put_oi":946},{"strike":38850.0,"call_gex_1pct":146283.18581823702,"put_gex_1pct":-15604013.50889646,"net_gex_1pct":-15457730.323078224,"gross_gex_1pct":15750296.694714697,"call_oi":1,"put_oi":110},{"strike":38900.0,"call_gex_1pct":7754752.805868324,"put_gex_1pct":-68676836.42780349,"net_gex_1pct":-60922083.62193516,"gross_gex_1pct":76431589.23367181,"call_oi":52,"put_oi":478},{"strike":38950.0,"call_gex_1pct":0.0,"put_gex_1pct":-38063387.17142381,"net_gex_1pct":-38063387.17142381,"gross_gex_1pct":38063387.17142381,"call_oi":0,"put_oi":261},{"strike":39000.0,"call_gex_1pct":320346765.3566797,"put_gex_1pct":-332512818.9888765,"net_gex_1pct":-12166053.632196844,"gross_gex_1pct":652859584.3455563,"call_oi":2037,"put_oi":2213},{"strike":39050.0,"call_gex_1pct":0.0,"put_gex_1pct":-21969329.790990073,"net_gex_1pct":-21969329.790990073,"gross_gex_1pct":21969329.790990073,"call_oi":0,"put_oi":142},{"strike":39100.0,"call_gex_1pct":147698499.60475332,"put_gex_1pct":-76431639.46840282,"net_gex_1pct":71266860.1363505,"gross_gex_1pct":224130139.07315612,"call_oi":902,"put_oi":488},{"strike":39150.0,"call_gex_1pct":503825.3209964372,"put_gex_1pct":-23849044.766285293,"net_gex_1pct":-23345219.445288856,"gross_gex_1pct":24352870.08728173,"call_oi":3,"put_oi":150},{"strike":39200.0,"call_gex_1pct":341990286.1969114,"put_gex_1pct":-88356770.31699099,"net_gex_1pct":253633515.87992042,"gross_gex_1pct":430347056.51390237,"call_oi":2011,"put_oi":545},{"strike":39250.0,"call_gex_1pct":0.0,"put_gex_1pct":-26415899.747026697,"net_gex_1pct":-26415899.747026697,"gross_gex_1pct":26415899.747026697,"call_oi":0,"put_oi":159},{"strike":39300.0,"call_gex_1pct":353721630.09417903,"put_gex_1pct":-84374257.89239107,"net_gex_1pct":269347372.20178795,"gross_gex_1pct":438095887.9865701,"call_oi":2006,"put_oi":502},{"strike":39350.0,"call_gex_1pct":1265167.993095683,"put_gex_1pct":-30335820.826378517,"net_gex_1pct":-29070652.833282836,"gross_gex_1pct":31600988.819474198,"call_oi":7,"put_oi":178},{"strike":39400.0,"call_gex_1pct":366966023.16828585,"put_gex_1pct":-57589422.55527647,"net_gex_1pct":309376600.6130094,"gross_gex_1pct":424555445.7235623,"call_oi":2009,"put_oi":341},{"strike":39450.0,"call_gex_1pct":1476254.043825394,"put_gex_1pct":-24658690.50604714,"net_gex_1pct":-23182436.462221745,"gross_gex_1pct":26134944.549872536,"call_oi":8,"put_oi":141},{"strike":39500.0,"call_gex_1pct":387417249.6419745,"put_gex_1pct":-228074153.64873806,"net_gex_1pct":159343095.99323645,"gross_gex_1pct":615491403.2907126,"call_oi":2018,"put_oi":1285},{"strike":39550.0,"call_gex_1pct":2100989.231482042,"put_gex_1pct":-20892844.753887177,"net_gex_1pct":-18791855.522405133,"gross_gex_1pct":22993833.98536922,"call_oi":11,"put_oi":115},{"strike":39600.0,"call_gex_1pct":5328272.094396832,"put_gex_1pct":-41484206.213037655,"net_gex_1pct":-36155934.118640825,"gross_gex_1pct":46812478.307434484,"call_oi":27,"put_oi":223},{"strike":39650.0,"call_gex_1pct":4830021.374181083,"put_gex_1pct":-13897196.17068852,"net_gex_1pct":-9067174.796507437,"gross_gex_1pct":18727217.5448696,"call_oi":25,"put_oi":76},{"strike":39700.0,"call_gex_1pct":9780979.168181889,"put_gex_1pct":-48122907.05995015,"net_gex_1pct":-38341927.89176826,"gross_gex_1pct":57903886.22813204,"call_oi":49,"put_oi":262},{"strike":39750.0,"call_gex_1pct":7934344.442701271,"put_gex_1pct":-22766698.22311651,"net_gex_1pct":-14832353.780415239,"gross_gex_1pct":30701042.665817782,"call_oi":40,"put_oi":120},{"strike":39800.0,"call_gex_1pct":118457531.01910365,"put_gex_1pct":-145783039.64790598,"net_gex_1pct":-27325508.62880233,"gross_gex_1pct":264240570.66700962,"call_oi":601,"put_oi":788},{"strike":39850.0,"call_gex_1pct":12730383.518911676,"put_gex_1pct":-19216195.892547842,"net_gex_1pct":-6485812.373636166,"gross_gex_1pct":31946579.41145952,"call_oi":64,"put_oi":106},{"strike":39900.0,"call_gex_1pct":17271277.487104256,"put_gex_1pct":-48768373.928582214,"net_gex_1pct":-31497096.441477958,"gross_gex_1pct":66039651.41568647,"call_oi":84,"put_oi":261},{"strike":39950.0,"call_gex_1pct":21909013.208345696,"put_gex_1pct":-28671738.15091906,"net_gex_1pct":-6762724.942573365,"gross_gex_1pct":50580751.35926476,"call_oi":109,"put_oi":151},{"strike":40000.0,"call_gex_1pct":93180369.65047438,"put_gex_1pct":-541181736.4907361,"net_gex_1pct":-448001366.84026176,"gross_gex_1pct":634362106.1412106,"call_oi":463,"put_oi":2889},{"strike":40050.0,"call_gex_1pct":22991735.940011486,"put_gex_1pct":-56117468.676861726,"net_gex_1pct":-33125732.73685024,"gross_gex_1pct":79109204.6168732,"call_oi":115,"put_oi":297},{"strike":40100.0,"call_gex_1pct":50251617.61226923,"put_gex_1pct":-39688866.54206966,"net_gex_1pct":10562751.070199572,"gross_gex_1pct":89940484.1543389,"call_oi":253,"put_oi":216},{"strike":40150.0,"call_gex_1pct":21412943.589673232,"put_gex_1pct":-23732586.78502911,"net_gex_1pct":-2319643.1953558773,"gross_gex_1pct":45145530.37470234,"call_oi":106,"put_oi":129},{"strike":40200.0,"call_gex_1pct":42744605.42142493,"put_gex_1pct":-46234733.593953885,"net_gex_1pct":-3490128.1725289524,"gross_gex_1pct":88979339.01537882,"call_oi":208,"put_oi":251},{"strike":40250.0,"call_gex_1pct":26342181.856033664,"put_gex_1pct":-16598681.20701996,"net_gex_1pct":9743500.649013704,"gross_gex_1pct":42940863.06305362,"call_oi":127,"put_oi":90},{"strike":40300.0,"call_gex_1pct":60083733.28528636,"put_gex_1pct":-36268397.61082625,"net_gex_1pct":23815335.674460113,"gross_gex_1pct":96352130.8961126,"call_oi":294,"put_oi":195},{"strike":40350.0,"call_gex_1pct":34572255.80579901,"put_gex_1pct":-20777271.55791205,"net_gex_1pct":13794984.247886956,"gross_gex_1pct":55349527.36371106,"call_oi":173,"put_oi":114},{"strike":40400.0,"call_gex_1pct":64620687.10888543,"put_gex_1pct":-36202645.65631069,"net_gex_1pct":28418041.452574737,"gross_gex_1pct":100823332.76519611,"call_oi":323,"put_oi":197},{"strike":40450.0,"call_gex_1pct":16222051.432740854,"put_gex_1pct":-17671221.469828345,"net_gex_1pct":-1449170.0370874908,"gross_gex_1pct":33893272.9025692,"call_oi":81,"put_oi":94},{"strike":40500.0,"call_gex_1pct":68209482.5635423,"put_gex_1pct":-141521774.17863083,"net_gex_1pct":-73312291.61508852,"gross_gex_1pct":209731256.74217314,"call_oi":335,"put_oi":763},{"strike":40550.0,"call_gex_1pct":11209493.700976934,"put_gex_1pct":-67947006.98369275,"net_gex_1pct":-56737513.28271581,"gross_gex_1pct":79156500.68466969,"call_oi":57,"put_oi":366},{"strike":40600.0,"call_gex_1pct":30883759.04609725,"put_gex_1pct":-83232216.49197766,"net_gex_1pct":-52348457.44588041,"gross_gex_1pct":114115975.53807491,"call_oi":156,"put_oi":448},{"strike":40650.0,"call_gex_1pct":19127064.674619578,"put_gex_1pct":-15615763.958475707,"net_gex_1pct":3511300.7161438707,"gross_gex_1pct":34742828.63309529,"call_oi":96,"put_oi":87},{"strike":40700.0,"call_gex_1pct":36000428.100074366,"put_gex_1pct":-33528755.057180233,"net_gex_1pct":2471673.0428941324,"gross_gex_1pct":69529183.1572546,"call_oi":187,"put_oi":188},{"strike":40750.0,"call_gex_1pct":16598931.076560067,"put_gex_1pct":-14726634.692924768,"net_gex_1pct":1872296.3836352993,"gross_gex_1pct":31325565.769484833,"call_oi":87,"put_oi":82},{"strike":40800.0,"call_gex_1pct":50749872.823406816,"put_gex_1pct":-56092529.74978831,"net_gex_1pct":-5342656.926381491,"gross_gex_1pct":106842402.57319513,"call_oi":270,"put_oi":323},{"strike":40850.0,"call_gex_1pct":14208285.067507956,"put_gex_1pct":-15376298.529245725,"net_gex_1pct":-1168013.4617377687,"gross_gex_1pct":29584583.59675368,"call_oi":76,"put_oi":88},{"strike":40900.0,"call_gex_1pct":26130363.01392242,"put_gex_1pct":-38329560.676277295,"net_gex_1pct":-12199197.662354875,"gross_gex_1pct":64459923.69019972,"call_oi":141,"put_oi":221},{"strike":40950.0,"call_gex_1pct":21017760.3702747,"put_gex_1pct":-29425362.713228773,"net_gex_1pct":-8407602.342954073,"gross_gex_1pct":50443123.08350347,"call_oi":116,"put_oi":171},{"strike":41000.0,"call_gex_1pct":264060361.39128515,"put_gex_1pct":-218967107.13205278,"net_gex_1pct":45093254.25923237,"gross_gex_1pct":483027468.52333796,"call_oi":1483,"put_oi":1315},{"strike":41050.0,"call_gex_1pct":27079743.88599349,"put_gex_1pct":-13044637.513432257,"net_gex_1pct":14035106.372561235,"gross_gex_1pct":40124381.399425745,"call_oi":155,"put_oi":79},{"strike":41100.0,"call_gex_1pct":46619843.23703147,"put_gex_1pct":-35670744.330719635,"net_gex_1pct":10949098.906311832,"gross_gex_1pct":82290587.56775111,"call_oi":273,"put_oi":218},{"strike":41150.0,"call_gex_1pct":30845329.37971001,"put_gex_1pct":-12979084.833183238,"net_gex_1pct":17866244.546526775,"gross_gex_1pct":43824414.21289325,"call_oi":183,"put_oi":81},{"strike":41200.0,"call_gex_1pct":58364275.96950261,"put_gex_1pct":-26203662.66197906,"net_gex_1pct":32160613.307523552,"gross_gex_1pct":84567938.63148168,"call_oi":356,"put_oi":167},{"strike":41250.0,"call_gex_1pct":16812599.518383447,"put_gex_1pct":-35224498.7275834,"net_gex_1pct":-18411899.209199954,"gross_gex_1pct":52037098.24596685,"call_oi":105,"put_oi":227},{"strike":41300.0,"call_gex_1pct":30695083.054542936,"put_gex_1pct":-60884314.73970075,"net_gex_1pct":-30189231.685157813,"gross_gex_1pct":91579397.7942437,"call_oi":196,"put_oi":401},{"strike":41350.0,"call_gex_1pct":19446592.46114332,"put_gex_1pct":-12327580.830072641,"net_gex_1pct":7119011.631070677,"gross_gex_1pct":31774173.29121596,"call_oi":126,"put_oi":83},{"strike":41400.0,"call_gex_1pct":37085045.89906459,"put_gex_1pct":-43428567.30635322,"net_gex_1pct":-6343521.407288626,"gross_gex_1pct":80513613.20541781,"call_oi":248,"put_oi":299},{"strike":41450.0,"call_gex_1pct":23926246.576678295,"put_gex_1pct":-17322074.191889185,"net_gex_1pct":6604172.384789109,"gross_gex_1pct":41248320.76856748,"call_oi":164,"put_oi":122},{"strike":41500.0,"call_gex_1pct":197927550.40228853,"put_gex_1pct":-174243774.92900497,"net_gex_1pct":23683775.47328356,"gross_gex_1pct":372171325.33129346,"call_oi":1397,"put_oi":1256},{"strike":41550.0,"call_gex_1pct":18890878.89279664,"put_gex_1pct":-11379442.566919573,"net_gex_1pct":7511436.325877067,"gross_gex_1pct":30270321.459716212,"call_oi":137,"put_oi":84},{"strike":41600.0,"call_gex_1pct":40660016.69891005,"put_gex_1pct":-25248923.758474454,"net_gex_1pct":15411092.940435596,"gross_gex_1pct":65908940.457384504,"call_oi":304,"put_oi":191},{"strike":41650.0,"call_gex_1pct":20607356.709149163,"put_gex_1pct":-22555209.59920466,"net_gex_1pct":-1947852.8900554962,"gross_gex_1pct":43162566.30835383,"call_oi":159,"put_oi":175},{"strike":41700.0,"call_gex_1pct":34408010.02035893,"put_gex_1pct":-26798544.718234405,"net_gex_1pct":7609465.302124523,"gross_gex_1pct":61206554.73859333,"call_oi":274,"put_oi":214},{"strike":41750.0,"call_gex_1pct":14561301.966763897,"put_gex_1pct":-7075713.76806463,"net_gex_1pct":7485588.198699267,"gross_gex_1pct":21637015.734828528,"call_oi":120,"put_oi":58},{"strike":41800.0,"call_gex_1pct":47272373.411106825,"put_gex_1pct":-36440433.16317933,"net_gex_1pct":10831940.247927494,"gross_gex_1pct":83712806.57428616,"call_oi":402,"put_oi":307},{"strike":41850.0,"call_gex_1pct":19985314.286995307,"put_gex_1pct":-8081331.977602784,"net_gex_1pct":11903982.309392523,"gross_gex_1pct":28066646.26459809,"call_oi":176,"put_oi":70},{"strike":41900.0,"call_gex_1pct":18412408.1277707,"put_gex_1pct":-23108212.742182735,"net_gex_1pct":-4695804.614412036,"gross_gex_1pct":41520620.86995344,"call_oi":168,"put_oi":206},{"strike":41950.0,"call_gex_1pct":15190167.75715601,"put_gex_1pct":-11314761.05894096,"net_gex_1pct":3875406.6982150506,"gross_gex_1pct":26504928.81609697,"call_oi":144,"put_oi":104},{"strike":42000.0,"call_gex_1pct":258992847.85870096,"put_gex_1pct":-207475285.57122117,"net_gex_1pct":51517562.28747979,"gross_gex_1pct":466468133.4299221,"call_oi":2539,"put_oi":1959},{"strike":42050.0,"call_gex_1pct":11398747.04542449,"put_gex_1pct":-7584694.612016246,"net_gex_1pct":3814052.4334082436,"gross_gex_1pct":18983441.657440737,"call_oi":117,"put_oi":74},{"strike":42100.0,"call_gex_1pct":44040323.84687784,"put_gex_1pct":-24860618.787070677,"net_gex_1pct":19179705.059807166,"gross_gex_1pct":68900942.63394852,"call_oi":472,"put_oi":249},{"strike":42150.0,"call_gex_1pct":17729317.441485,"put_gex_1pct":-6745135.999818424,"net_gex_1pct":10984181.441666575,"gross_gex_1pct":24474453.441303425,"call_oi":199,"put_oi":70},{"strike":42200.0,"call_gex_1pct":58458119.93083905,"put_gex_1pct":-18032620.90955382,"net_gex_1pct":40425499.02128523,"gross_gex_1pct":76490740.84039286,"call_oi":677,"put_oi":192},{"strike":42250.0,"call_gex_1pct":15312324.671910591,"put_gex_1pct":-14196370.563441882,"net_gex_1pct":1115954.1084687095,"gross_gex_1pct":29508695.23535247,"call_oi":185,"put_oi":155},{"strike":42300.0,"call_gex_1pct":41494266.15183014,"put_gex_1pct":-37524530.61449057,"net_gex_1pct":3969735.537339568,"gross_gex_1pct":79018796.7663207,"call_oi":524,"put_oi":426},{"strike":42350.0,"call_gex_1pct":17442939.878082313,"put_gex_1pct":-5070689.696372351,"net_gex_1pct":12372250.181709962,"gross_gex_1pct":22513629.574454665,"call_oi":232,"put_oi":59},{"strike":42400.0,"call_gex_1pct":30960944.54422802,"put_gex_1pct":-17854061.442528404,"net_gex_1pct":13106883.101699617,"gross_gex_1pct":48815005.98675643,"call_oi":429,"put_oi":217},{"strike":42450.0,"call_gex_1pct":19180333.277191743,"put_gex_1pct":-4818756.589752177,"net_gex_1pct":14361576.687439566,"gross_gex_1pct":23999089.86694392,"call_oi":280,"put_oi":60},{"strike":42500.0,"call_gex_1pct":146897017.56357303,"put_gex_1pct":-110351629.0097432,"net_gex_1pct":36545388.553829834,"gross_gex_1pct":257248646.57331622,"call_oi":2201,"put_oi":1407},{"strike":42550.0,"call_gex_1pct":20657812.512205034,"put_gex_1pct":-6417792.961946399,"net_gex_1pct":14240019.550258636,"gross_gex_1pct":27075605.474151433,"call_oi":333,"put_oi":86},{"strike":42600.0,"call_gex_1pct":40139542.98181216,"put_gex_1pct":-11300153.096920075,"net_gex_1pct":28839389.884892084,"gross_gex_1pct":51439696.07873223,"call_oi":673,"put_oi":155},{"strike":42650.0,"call_gex_1pct":76675209.3828451,"put_gex_1pct":-3705108.934691212,"net_gex_1pct":72970100.4481539,"gross_gex_1pct":80380318.31753631,"call_oi":1338,"put_oi":52},{"strike":42700.0,"call_gex_1pct":32720341.02622154,"put_gex_1pct":-11425097.082648896,"net_gex_1pct":21295243.943572644,"gross_gex_1pct":44145438.10887043,"call_oi":598,"put_oi":164},{"strike":42750.0,"call_gex_1pct":19359974.635662064,"put_gex_1pct":-3883978.545014964,"net_gex_1pct":15475996.0906471,"gross_gex_1pct":23243953.180677027,"call_oi":369,"put_oi":57},{"strike":42800.0,"call_gex_1pct":38530038.28922571,"put_gex_1pct":-17805943.257114615,"net_gex_1pct":20724095.032111097,"gross_gex_1pct":56335981.54634033,"call_oi":812,"put_oi":277},{"strike":42850.0,"call_gex_1pct":9361024.492982194,"put_gex_1pct":-8490350.067081675,"net_gex_1pct":870674.4259005189,"gross_gex_1pct":17851374.56006387,"call_oi":215,"put_oi":135},{"strike":42900.0,"call_gex_1pct":27242278.74248852,"put_gex_1pct":-23513537.519764867,"net_gex_1pct":3728741.2227236517,"gross_gex_1pct":50755816.26225339,"call_oi":641,"put_oi":382},{"strike":42950.0,"call_gex_1pct":7913223.157496418,"put_gex_1pct":-4098052.0107569112,"net_gex_1pct":3815171.1467395066,"gross_gex_1pct":12011275.168253329,"call_oi":206,"put_oi":68},{"strike":43000.0,"call_gex_1pct":132721800.16206175,"put_gex_1pct":-76558487.80063719,"net_gex_1pct":56163312.361424565,"gross_gex_1pct":209280287.96269894,"call_oi":3538,"put_oi":1363},{"strike":43050.0,"call_gex_1pct":6528222.42112952,"put_gex_1pct":-5225427.023540104,"net_gex_1pct":1302795.3975894162,"gross_gex_1pct":11753649.444669623,"call_oi":188,"put_oi":95},{"strike":43100.0,"call_gex_1pct":24759660.51855738,"put_gex_1pct":-42458735.030219726,"net_gex_1pct":-17699074.511662345,"gross_gex_1pct":67218395.5487771,"call_oi":822,"put_oi":788},{"strike":43150.0,"call_gex_1pct":10131181.948821617,"put_gex_1pct":-3695891.274744823,"net_gex_1pct":6435290.674076794,"gross_gex_1pct":13827073.22356644,"call_oi":386,"put_oi":70},{"strike":43200.0,"call_gex_1pct":30177754.80283752,"put_gex_1pct":-10583762.912501805,"net_gex_1pct":19593991.890335716,"gross_gex_1pct":40761517.715339325,"call_oi":1245,"put_oi":219},{"strike":43250.0,"call_gex_1pct":6232362.703567834,"put_gex_1pct":-3173242.6219581836,"net_gex_1pct":3059120.08160965,"gross_gex_1pct":9405605.325526018,"call_oi":366,"put_oi":67},{"strike":43300.0,"call_gex_1pct":22031576.94063689,"put_gex_1pct":-12953746.770372355,"net_gex_1pct":9077830.170264533,"gross_gex_1pct":34985323.71100924,"call_oi":1358,"put_oi":279},{"strike":43350.0,"call_gex_1pct":5053871.641516087,"put_gex_1pct":-3369086.285961671,"net_gex_1pct":1684785.3555544158,"gross_gex_1pct":8422957.927477758,"call_oi":352,"put_oi":74},{"strike":43400.0,"call_gex_1pct":18280606.361679044,"put_gex_1pct":-7234483.847652329,"net_gex_1pct":11046122.514026714,"gross_gex_1pct":25515090.20933137,"call_oi":1473,"put_oi":162},{"strike":43450.0,"call_gex_1pct":3652838.93383896,"put_gex_1pct":-3198504.7213279163,"net_gex_1pct":454334.21251104353,"gross_gex_1pct":6851343.655166876,"call_oi":328,"put_oi":73},{"strike":43500.0,"call_gex_1pct":50450307.606649496,"put_gex_1pct":-25972207.377054416,"net_gex_1pct":24478100.22959508,"gross_gex_1pct":76422514.98370391,"call_oi":6804,"put_oi":604},{"strike":43550.0,"call_gex_1pct":1221169.7497103757,"put_gex_1pct":-1688467.6199417028,"net_gex_1pct":-467297.87023132714,"gross_gex_1pct":2909637.3696520785,"call_oi":186,"put_oi":40},{"strike":43600.0,"call_gex_1pct":14103694.799923325,"put_gex_1pct":-7626431.945729535,"net_gex_1pct":6477262.85419379,"gross_gex_1pct":21730126.745652862,"call_oi":2197,"put_oi":184},{"strike":43650.0,"call_gex_1pct":1418219.9460761568,"put_gex_1pct":-2361073.49101905,"net_gex_1pct":-942853.5449428933,"gross_gex_1pct":3779293.437095207,"call_oi":239,"put_oi":58},{"strike":43700.0,"call_gex_1pct":6211850.3244508235,"put_gex_1pct":-11037554.052630989,"net_gex_1pct":-4825703.728180165,"gross_gex_1pct":17249404.37708181,"call_oi":1070,"put_oi":276},{"strike":43750.0,"call_gex_1pct":1174284.7169457283,"put_gex_1pct":-2514939.9382711938,"net_gex_1pct":-1340655.2213254655,"gross_gex_1pct":3689224.655216922,"call_oi":220,"put_oi":64},{"strike":43800.0,"call_gex_1pct":11160416.303851238,"put_gex_1pct":-10427839.648375358,"net_gex_1pct":732576.6554758791,"gross_gex_1pct":21588255.952226594,"call_oi":2136,"put_oi":270},{"strike":43850.0,"call_gex_1pct":1741760.6609389603,"put_gex_1pct":-6872087.244946069,"net_gex_1pct":-5130326.584007109,"gross_gex_1pct":8613847.90588503,"call_oi":365,"put_oi":181},{"strike":43900.0,"call_gex_1pct":3622001.5420620977,"put_gex_1pct":-8101091.133730717,"net_gex_1pct":-4479089.591668619,"gross_gex_1pct":11723092.675792815,"call_oi":775,"put_oi":217},{"strike":43950.0,"call_gex_1pct":1942259.624943837,"put_gex_1pct":-3781695.771982512,"net_gex_1pct":-1839436.147038675,"gross_gex_1pct":5723955.396926349,"call_oi":502,"put_oi":103},{"strike":44000.0,"call_gex_1pct":19071108.208921403,"put_gex_1pct":-55474810.47620855,"net_gex_1pct":-36403702.26728715,"gross_gex_1pct":74545918.68512996,"call_oi":6330,"put_oi":1536},{"strike":44050.0,"call_gex_1pct":1130683.5604386476,"put_gex_1pct":-3020412.9108407963,"net_gex_1pct":-1889729.3504021487,"gross_gex_1pct":4151096.471279444,"call_oi":383,"put_oi":85},{"strike":44100.0,"call_gex_1pct":4375000.884812666,"put_gex_1pct":-6783867.7893708395,"net_gex_1pct":-2408866.9045581734,"gross_gex_1pct":11158868.674183507,"call_oi":1512,"put_oi":194},{"strike":44150.0,"call_gex_1pct":974108.1904506604,"put_gex_1pct":-1066962.3064207851,"net_gex_1pct":-92854.11597012472,"gross_gex_1pct":2041070.4968714456,"call_oi":401,"put_oi":31},{"strike":44200.0,"call_gex_1pct":3098841.7095328374,"put_gex_1pct":-3523822.513044892,"net_gex_1pct":-424980.8035120545,"gross_gex_1pct":6622664.222577729,"call_oi":1301,"put_oi":104},{"strike":44250.0,"call_gex_1pct":1097958.0852214627,"put_gex_1pct":-1701468.3655698607,"net_gex_1pct":-603510.280348398,"gross_gex_1pct":2799426.4507913236,"call_oi":470,"put_oi":51},{"strike":44300.0,"call_gex_1pct":2562120.333037869,"put_gex_1pct":-4468312.618251962,"net_gex_1pct":-1906192.2852140926,"gross_gex_1pct":7030432.951289831,"call_oi":1118,"put_oi":136},{"strike":44350.0,"call_gex_1pct":642364.3607980157,"put_gex_1pct":-841405.0641944365,"net_gex_1pct":-199040.7033964208,"gross_gex_1pct":1483769.4249924524,"call_oi":350,"put_oi":26},{"strike":44400.0,"call_gex_1pct":1127475.8807647214,"put_gex_1pct":-5387907.4874317935,"net_gex_1pct":-4260431.606667072,"gross_gex_1pct":6515383.368196515,"call_oi":626,"put_oi":169},{"strike":44450.0,"call_gex_1pct":321752.1957943928,"put_gex_1pct":-785322.4056950057,"net_gex_1pct":-463570.2099006129,"gross_gex_1pct":1107074.6014893984,"call_oi":182,"put_oi":25},{"strike":44500.0,"call_gex_1pct":4887597.636301476,"put_gex_1pct":-7305767.947539849,"net_gex_1pct":-2418170.3112383736,"gross_gex_1pct":12193365.583841324,"call_oi":2816,"put_oi":236},{"strike":44550.0,"call_gex_1pct":446549.9793914505,"put_gex_1pct":-152559.6163089892,"net_gex_1pct":293990.3630824613,"gross_gex_1pct":599109.5957004398,"call_oi":262,"put_oi":5},{"strike":44600.0,"call_gex_1pct":1120351.6456201405,"put_gex_1pct":-6466839.9227993945,"net_gex_1pct":-5346488.277179254,"gross_gex_1pct":7587191.568419535,"call_oi":896,"put_oi":215},{"strike":44650.0,"call_gex_1pct":291084.28844855085,"put_gex_1pct":-296554.5909894593,"net_gex_1pct":-5470.302540908451,"gross_gex_1pct":587638.8794380102,"call_oi":237,"put_oi":10},{"strike":44700.0,"call_gex_1pct":1229580.0928351607,"put_gex_1pct":-4035527.3564655357,"net_gex_1pct":-2805947.2636303753,"gross_gex_1pct":5265107.449300696,"call_oi":1019,"put_oi":138},{"strike":44750.0,"call_gex_1pct":266786.3684890778,"put_gex_1pct":-547968.4948679066,"net_gex_1pct":-281182.1263788288,"gross_gex_1pct":814754.8633569843,"call_oi":225,"put_oi":19},{"strike":44800.0,"call_gex_1pct":624638.5901727171,"put_gex_1pct":-3100788.851763689,"net_gex_1pct":-2476150.2615909716,"gross_gex_1pct":3725427.4419364063,"call_oi":536,"put_oi":109},{"strike":44850.0,"call_gex_1pct":238282.9202332205,"put_gex_1pct":-28064.097207434766,"net_gex_1pct":210218.82302578574,"gross_gex_1pct":266347.01744065527,"call_oi":208,"put_oi":1},{"strike":44900.0,"call_gex_1pct":414499.3837004123,"put_gex_1pct":-6783955.574424169,"net_gex_1pct":-6369456.190723756,"gross_gex_1pct":7198454.958124582,"call_oi":368,"put_oi":245},{"strike":44950.0,"call_gex_1pct":247005.54003902632,"put_gex_1pct":0.0,"net_gex_1pct":247005.54003902632,"gross_gex_1pct":247005.54003902632,"call_oi":223,"put_oi":0},{"strike":45000.0,"call_gex_1pct":4546253.313830102,"put_gex_1pct":-21600199.80582905,"net_gex_1pct":-17053946.49199895,"gross_gex_1pct":26146453.11965915,"call_oi":4173,"put_oi":801},{"strike":45050.0,"call_gex_1pct":210058.77118478477,"put_gex_1pct":0.0,"net_gex_1pct":210058.77118478477,"gross_gex_1pct":210058.77118478477,"call_oi":196,"put_oi":0},{"strike":45100.0,"call_gex_1pct":701229.9667521646,"put_gex_1pct":-5228953.118348234,"net_gex_1pct":-4527723.151596069,"gross_gex_1pct":5930183.085100399,"call_oi":665,"put_oi":199},{"strike":45150.0,"call_gex_1pct":248006.9724141339,"put_gex_1pct":0.0,"net_gex_1pct":248006.9724141339,"gross_gex_1pct":248006.9724141339,"call_oi":239,"put_oi":0},{"strike":45200.0,"call_gex_1pct":646500.0037442892,"put_gex_1pct":-2843417.3503954425,"net_gex_1pct":-2196917.346651153,"gross_gex_1pct":3489917.3541397317,"call_oi":633,"put_oi":111},{"strike":45250.0,"call_gex_1pct":257379.46497234842,"put_gex_1pct":-50594.743052302714,"net_gex_1pct":206784.7219200457,"gross_gex_1pct":307974.20802465116,"call_oi":256,"put_oi":2},{"strike":45300.0,"call_gex_1pct":598862.7978772697,"put_gex_1pct":-3023224.7425310235,"net_gex_1pct":-2424361.9446537537,"gross_gex_1pct":3622087.5404082933,"call_oi":605,"put_oi":121},{"strike":45350.0,"call_gex_1pct":213462.56375227295,"put_gex_1pct":0.0,"net_gex_1pct":213462.56375227295,"gross_gex_1pct":213462.56375227295,"call_oi":219,"put_oi":0},{"strike":45400.0,"call_gex_1pct":786200.8226010362,"put_gex_1pct":-2413745.831394279,"net_gex_1pct":-1627545.0087932427,"gross_gex_1pct":3199946.653995315,"call_oi":819,"put_oi":99},{"strike":45450.0,"call_gex_1pct":104956.57690876268,"put_gex_1pct":-24088.85474145116,"net_gex_1pct":80867.72216731153,"gross_gex_1pct":129045.43165021384,"call_oi":111,"put_oi":1},{"strike":45500.0,"call_gex_1pct":1393539.4150242293,"put_gex_1pct":-6664725.686468829,"net_gex_1pct":-5271186.2714446,"gross_gex_1pct":8058265.101493059,"call_oi":1496,"put_oi":280},{"strike":45550.0,"call_gex_1pct":138588.859362624,"put_gex_1pct":-47044.599833706765,"net_gex_1pct":91544.25952891723,"gross_gex_1pct":185633.45919633078,"call_oi":151,"put_oi":2},{"strike":45600.0,"call_gex_1pct":635816.7927941972,"put_gex_1pct":-4951782.273967145,"net_gex_1pct":-4315965.481172948,"gross_gex_1pct":5587599.066761342,"call_oi":703,"put_oi":213},{"strike":45700.0,"call_gex_1pct":518393.5931889653,"put_gex_1pct":-2748579.42984496,"net_gex_1pct":-2230185.836655995,"gross_gex_1pct":3266973.0230339253,"call_oi":590,"put_oi":121},{"strike":45800.0,"call_gex_1pct":563658.3066644795,"put_gex_1pct":-3530515.8305569245,"net_gex_1pct":-2966857.523892445,"gross_gex_1pct":4094174.137221404,"call_oi":660,"put_oi":159},{"strike":45900.0,"call_gex_1pct":559785.4056552651,"put_gex_1pct":-2670764.1959672137,"net_gex_1pct":-2110978.7903119484,"gross_gex_1pct":3230549.601622479,"call_oi":674,"put_oi":123},{"strike":46000.0,"call_gex_1pct":7260036.174264826,"put_gex_1pct":-5119205.704129032,"net_gex_1pct":2140830.470135794,"gross_gex_1pct":12379241.878393859,"call_oi":8984,"put_oi":241},{"strike":46100.0,"call_gex_1pct":1177629.2640725884,"put_gex_1pct":-831497.6817746842,"net_gex_1pct":346131.5822979042,"gross_gex_1pct":2009126.9458472726,"call_oi":1497,"put_oi":40},{"strike":46200.0,"call_gex_1pct":362384.09741896833,"put_gex_1pct":-1953633.779499527,"net_gex_1pct":-1591249.6820805587,"gross_gex_1pct":2316017.8769184956,"call_oi":473,"put_oi":96},{"strike":46300.0,"call_gex_1pct":600180.8058706201,"put_gex_1pct":-3427849.8081950657,"net_gex_1pct":-2827669.0023244456,"gross_gex_1pct":4028030.614065686,"call_oi":804,"put_oi":172},{"strike":46400.0,"call_gex_1pct":431508.5383322809,"put_gex_1pct":-1737603.6085622588,"net_gex_1pct":-1306095.0702299778,"gross_gex_1pct":2169112.1468945397,"call_oi":593,"put_oi":89},{"strike":46500.0,"call_gex_1pct":2458135.562792471,"put_gex_1pct":-2334153.765107615,"net_gex_1pct":123981.79768485622,"gross_gex_1pct":4792289.327900086,"call_oi":3464,"put_oi":122},{"strike":46600.0,"call_gex_1pct":526154.9704243052,"put_gex_1pct":-843972.7913393052,"net_gex_1pct":-317817.82091500005,"gross_gex_1pct":1370127.7617636104,"call_oi":760,"put_oi":45},{"strike":46700.0,"call_gex_1pct":232436.3838546782,"put_gex_1pct":-1195388.1681220676,"net_gex_1pct":-962951.7842673894,"gross_gex_1pct":1427824.5519767457,"call_oi":344,"put_oi":65},{"strike":46800.0,"call_gex_1pct":365484.74522199563,"put_gex_1pct":-1226630.3396395613,"net_gex_1pct":-861145.5944175656,"gross_gex_1pct":1592115.084861557,"call_oi":554,"put_oi":68},{"strike":46900.0,"call_gex_1pct":381468.15139601246,"put_gex_1pct":-1610576.0356434186,"net_gex_1pct":-1229107.8842474062,"gross_gex_1pct":1992044.187039431,"call_oi":592,"put_oi":91},{"strike":47000.0,"call_gex_1pct":2085900.5998055744,"put_gex_1pct":-3213430.853489728,"net_gex_1pct":-1127530.2536841538,"gross_gex_1pct":5299331.453295303,"call_oi":3313,"put_oi":185},{"strike":47100.0,"call_gex_1pct":260932.1409634482,"put_gex_1pct":-460402.1600769433,"net_gex_1pct":-199470.01911349507,"gross_gex_1pct":721334.3010403914,"call_oi":424,"put_oi":27},{"strike":47200.0,"call_gex_1pct":218427.58555647437,"put_gex_1pct":-4370249.036111929,"net_gex_1pct":-4151821.450555455,"gross_gex_1pct":4588676.621668404,"call_oi":363,"put_oi":261},{"strike":47300.0,"call_gex_1pct":602678.0395728678,"put_gex_1pct":-641408.9313181224,"net_gex_1pct":-38730.89174525463,"gross_gex_1pct":1244086.9708909902,"call_oi":1024,"put_oi":39},{"strike":47400.0,"call_gex_1pct":99622.5069103725,"put_gex_1pct":-177736.83600262567,"net_gex_1pct":-78114.32909225317,"gross_gex_1pct":277359.34291299817,"call_oi":173,"put_oi":11},{"strike":47500.0,"call_gex_1pct":1986144.1819267643,"put_gex_1pct":-1429053.2564573402,"net_gex_1pct":557090.9254694241,"gross_gex_1pct":3415197.4383841045,"call_oi":3524,"put_oi":90},{"strike":47600.0,"call_gex_1pct":79457.47123402379,"put_gex_1pct":-608689.3223847096,"net_gex_1pct":-529231.8511506858,"gross_gex_1pct":688146.7936187334,"call_oi":144,"put_oi":39},{"strike":47700.0,"call_gex_1pct":108076.16760290466,"put_gex_1pct":-260859.43400291167,"net_gex_1pct":-152783.266400007,"gross_gex_1pct":368935.60160581634,"call_oi":200,"put_oi":17},{"strike":47800.0,"call_gex_1pct":232390.87144809344,"put_gex_1pct":-271616.1004064751,"net_gex_1pct":-39225.22895838163,"gross_gex_1pct":504006.9718545685,"call_oi":439,"put_oi":18},{"strike":47900.0,"call_gex_1pct":237054.92455462262,"put_gex_1pct":-222636.32060954088,"net_gex_1pct":14418.603945081733,"gross_gex_1pct":459691.2451641635,"call_oi":457,"put_oi":15},{"strike":48000.0,"call_gex_1pct":1968134.0336784697,"put_gex_1pct":-1241193.3625350185,"net_gex_1pct":726940.6711434512,"gross_gex_1pct":3209327.396213488,"call_oi":3871,"put_oi":85},{"strike":48100.0,"call_gex_1pct":61569.64169889532,"put_gex_1pct":-215535.72777896357,"net_gex_1pct":-153966.08608006826,"gross_gex_1pct":277105.3694778589,"call_oi":208,"put_oi":15},{"strike":48200.0,"call_gex_1pct":60367.28209191964,"put_gex_1pct":-395988.9513205609,"net_gex_1pct":-335621.66922864126,"gross_gex_1pct":456356.2334124805,"call_oi":208,"put_oi":28},{"strike":48300.0,"call_gex_1pct":57780.65174150336,"put_gex_1pct":-153144.76747307944,"net_gex_1pct":-95364.11573157608,"gross_gex_1pct":210925.4192145828,"call_oi":203,"put_oi":11},{"strike":48400.0,"call_gex_1pct":50259.408843352125,"put_gex_1pct":-178206.13012612902,"net_gex_1pct":-127946.7212827769,"gross_gex_1pct":228465.53896948113,"call_oi":180,"put_oi":13},{"strike":48500.0,"call_gex_1pct":717814.6954322706,"put_gex_1pct":-1012497.0214059895,"net_gex_1pct":-294682.3259737189,"gross_gex_1pct":1730311.7168382602,"call_oi":2620,"put_oi":75},{"strike":48600.0,"call_gex_1pct":30654.006109071008,"put_gex_1pct":-186163.7925814401,"net_gex_1pct":-155509.7864723691,"gross_gex_1pct":216817.7986905111,"call_oi":114,"put_oi":14},{"strike":48700.0,"call_gex_1pct":23757.40024728519,"put_gex_1pct":-196504.62546519432,"net_gex_1pct":-172747.22521790912,"gross_gex_1pct":220262.02571247952,"call_oi":90,"put_oi":15},{"strike":48800.0,"call_gex_1pct":24623.757481458764,"put_gex_1pct":-271077.21384042536,"net_gex_1pct":-246453.4563589666,"gross_gex_1pct":295700.97132188414,"call_oi":95,"put_oi":21},{"strike":48900.0,"call_gex_1pct":11200.971875031179,"put_gex_1pct":-216267.36132550717,"net_gex_1pct":-205066.38945047598,"gross_gex_1pct":227468.33320053836,"call_oi":44,"put_oi":17},{"strike":49000.0,"call_gex_1pct":296089.3683841692,"put_gex_1pct":-539204.2823643712,"net_gex_1pct":-243114.91398020205,"gross_gex_1pct":835293.6507485404,"call_oi":1184,"put_oi":43},{"strike":49100.0,"call_gex_1pct":10811.488440279032,"put_gex_1pct":-185435.04608901014,"net_gex_1pct":-174623.5576487311,"gross_gex_1pct":196246.53452928917,"call_oi":44,"put_oi":15},{"strike":49200.0,"call_gex_1pct":20767.5136085504,"put_gex_1pct":-170653.64790595765,"net_gex_1pct":-149886.13429740726,"gross_gex_1pct":191421.16151450804,"call_oi":86,"put_oi":14},{"strike":49300.0,"call_gex_1pct":19227.102438403337,"put_gex_1pct":-204358.74940594228,"net_gex_1pct":-185131.64696753892,"gross_gex_1pct":223585.85184434563,"call_oi":81,"put_oi":17},{"strike":49400.0,"call_gex_1pct":18670.20808392664,"put_gex_1pct":-154139.08227560652,"net_gex_1pct":-135468.87419167988,"gross_gex_1pct":172809.29035953316,"call_oi":80,"put_oi":13},{"strike":49500.0,"call_gex_1pct":82159.586443234,"put_gex_1pct":-163753.07444547064,"net_gex_1pct":-81593.48800223664,"gross_gex_1pct":245912.66088870465,"call_oi":358,"put_oi":14},{"strike":49600.0,"call_gex_1pct":26183.82714047627,"put_gex_1pct":-92322.79788375905,"net_gex_1pct":-66138.97074328279,"gross_gex_1pct":118506.62502423531,"call_oi":116,"put_oi":8},{"strike":49700.0,"call_gex_1pct":16209.888129731038,"put_gex_1pct":-159429.5240552745,"net_gex_1pct":-143219.63592554347,"gross_gex_1pct":175639.41218500552,"call_oi":73,"put_oi":14},{"strike":49800.0,"call_gex_1pct":18571.137051729722,"put_gex_1pct":-910354.1628896887,"net_gex_1pct":-891783.025837959,"gross_gex_1pct":928925.2999414185,"call_oi":85,"put_oi":81},{"strike":49900.0,"call_gex_1pct":94174.82484774884,"put_gex_1pct":-765456.9229984756,"net_gex_1pct":-671282.0981507268,"gross_gex_1pct":859631.7478462245,"call_oi":438,"put_oi":69},{"strike":50000.0,"call_gex_1pct":565689.2554210492,"put_gex_1pct":-514726.17832230555,"net_gex_1pct":50963.07709874364,"gross_gex_1pct":1080415.4337433549,"call_oi":2673,"put_oi":47},{"strike":50100.0,"call_gex_1pct":29584.288795724042,"put_gex_1pct":-248697.95776992326,"net_gex_1pct":-219113.66897419922,"gross_gex_1pct":278282.2465656473,"call_oi":142,"put_oi":23},{"strike":50200.0,"call_gex_1pct":45334.92714877323,"put_gex_1pct":-234904.39919180603,"net_gex_1pct":-189569.47204303282,"gross_gex_1pct":280239.32634057925,"call_oi":221,"put_oi":22},{"strike":50300.0,"call_gex_1pct":10908.746226526766,"put_gex_1pct":-84360.57454146403,"net_gex_1pct":-73451.82831493726,"gross_gex_1pct":95269.3207679908,"call_oi":54,"put_oi":8},{"strike":50400.0,"call_gex_1pct":14127.034346269782,"put_gex_1pct":0.0,"net_gex_1pct":14127.034346269782,"gross_gex_1pct":14127.034346269782,"call_oi":71,"put_oi":0},{"strike":50500.0,"call_gex_1pct":61938.554337047346,"put_gex_1pct":-10289.12253871648,"net_gex_1pct":51649.431798330865,"gross_gex_1pct":72227.67687576382,"call_oi":316,"put_oi":1},{"strike":50600.0,"call_gex_1pct":11200.868909248218,"put_gex_1pct":0.0,"net_gex_1pct":11200.868909248218,"gross_gex_1pct":11200.868909248218,"call_oi":58,"put_oi":0},{"strike":50700.0,"call_gex_1pct":2664.2108699093174,"put_gex_1pct":0.0,"net_gex_1pct":2664.2108699093174,"gross_gex_1pct":2664.2108699093174,"call_oi":14,"put_oi":0},{"strike":50800.0,"call_gex_1pct":8627.422357926142,"put_gex_1pct":0.0,"net_gex_1pct":8627.422357926142,"gross_gex_1pct":8627.422357926142,"call_oi":46,"put_oi":0},{"strike":50900.0,"call_gex_1pct":82822.53159692402,"put_gex_1pct":0.0,"net_gex_1pct":82822.53159692402,"gross_gex_1pct":82822.53159692402,"call_oi":448,"put_oi":0},{"strike":51000.0,"call_gex_1pct":110811.4696958229,"put_gex_1pct":-29090.189089951422,"net_gex_1pct":81721.28060587148,"gross_gex_1pct":139901.6587857743,"call_oi":608,"put_oi":3},{"strike":51100.0,"call_gex_1pct":8446.015254316022,"put_gex_1pct":-9585.739905711887,"net_gex_1pct":-1139.7246513958653,"gross_gex_1pct":18031.75516002791,"call_oi":47,"put_oi":1},{"strike":51200.0,"call_gex_1pct":9037.704321542125,"put_gex_1pct":0.0,"net_gex_1pct":9037.704321542125,"gross_gex_1pct":9037.704321542125,"call_oi":51,"put_oi":0},{"strike":51300.0,"call_gex_1pct":3845.072708465082,"put_gex_1pct":0.0,"net_gex_1pct":3845.072708465082,"gross_gex_1pct":3845.072708465082,"call_oi":22,"put_oi":0},{"strike":51400.0,"call_gex_1pct":5516.767391288366,"put_gex_1pct":0.0,"net_gex_1pct":5516.767391288366,"gross_gex_1pct":5516.767391288366,"call_oi":32,"put_oi":0},{"strike":51500.0,"call_gex_1pct":24491.07518038012,"put_gex_1pct":0.0,"net_gex_1pct":24491.07518038012,"gross_gex_1pct":24491.07518038012,"call_oi":144,"put_oi":0},{"strike":51600.0,"call_gex_1pct":16948.615294745825,"put_gex_1pct":-9064.300661892445,"net_gex_1pct":7884.31463285338,"gross_gex_1pct":26012.91595663827,"call_oi":101,"put_oi":1},{"strike":51700.0,"call_gex_1pct":9273.083969643469,"put_gex_1pct":0.0,"net_gex_1pct":9273.083969643469,"gross_gex_1pct":9273.083969643469,"call_oi":56,"put_oi":0},{"strike":51800.0,"call_gex_1pct":13400.7218567694,"put_gex_1pct":0.0,"net_gex_1pct":13400.7218567694,"gross_gex_1pct":13400.7218567694,"call_oi":82,"put_oi":0},{"strike":51900.0,"call_gex_1pct":6774.7881508174905,"put_gex_1pct":0.0,"net_gex_1pct":6774.7881508174905,"gross_gex_1pct":6774.7881508174905,"call_oi":42,"put_oi":0},{"strike":52000.0,"call_gex_1pct":103341.84361488905,"put_gex_1pct":0.0,"net_gex_1pct":103341.84361488905,"gross_gex_1pct":103341.84361488905,"call_oi":649,"put_oi":0},{"strike":52100.0,"call_gex_1pct":5816.616147551676,"put_gex_1pct":0.0,"net_gex_1pct":5816.616147551676,"gross_gex_1pct":5816.616147551676,"call_oi":37,"put_oi":0},{"strike":52200.0,"call_gex_1pct":9002.954663887269,"put_gex_1pct":0.0,"net_gex_1pct":9002.954663887269,"gross_gex_1pct":9002.954663887269,"call_oi":58,"put_oi":0},{"strike":52300.0,"call_gex_1pct":6591.196763052427,"put_gex_1pct":0.0,"net_gex_1pct":6591.196763052427,"gross_gex_1pct":6591.196763052427,"call_oi":43,"put_oi":0},{"strike":52400.0,"call_gex_1pct":3784.6359445247153,"put_gex_1pct":0.0,"net_gex_1pct":3784.6359445247153,"gross_gex_1pct":3784.6359445247153,"call_oi":25,"put_oi":0},{"strike":52500.0,"call_gex_1pct":16747.080935071797,"put_gex_1pct":0.0,"net_gex_1pct":16747.080935071797,"gross_gex_1pct":16747.080935071797,"call_oi":112,"put_oi":0},{"strike":52600.0,"call_gex_1pct":6942.307902575631,"put_gex_1pct":0.0,"net_gex_1pct":6942.307902575631,"gross_gex_1pct":6942.307902575631,"call_oi":47,"put_oi":0},{"strike":52700.0,"call_gex_1pct":5107.473494351611,"put_gex_1pct":0.0,"net_gex_1pct":5107.473494351611,"gross_gex_1pct":5107.473494351611,"call_oi":35,"put_oi":0},{"strike":52800.0,"call_gex_1pct":3172.0440656303517,"put_gex_1pct":0.0,"net_gex_1pct":3172.0440656303517,"gross_gex_1pct":3172.0440656303517,"call_oi":22,"put_oi":0},{"strike":52900.0,"call_gex_1pct":4416.745042106528,"put_gex_1pct":0.0,"net_gex_1pct":4416.745042106528,"gross_gex_1pct":4416.745042106528,"call_oi":31,"put_oi":0},{"strike":53000.0,"call_gex_1pct":201488.0554244627,"put_gex_1pct":0.0,"net_gex_1pct":201488.0554244627,"gross_gex_1pct":201488.0554244627,"call_oi":1431,"put_oi":0},{"strike":53100.0,"call_gex_1pct":5427.34637524237,"put_gex_1pct":0.0,"net_gex_1pct":5427.34637524237,"gross_gex_1pct":5427.34637524237,"call_oi":39,"put_oi":0},{"strike":53200.0,"call_gex_1pct":3438.901512392936,"put_gex_1pct":0.0,"net_gex_1pct":3438.901512392936,"gross_gex_1pct":3438.901512392936,"call_oi":25,"put_oi":0},{"strike":53300.0,"call_gex_1pct":2311.683172842138,"put_gex_1pct":0.0,"net_gex_1pct":2311.683172842138,"gross_gex_1pct":2311.683172842138,"call_oi":17,"put_oi":0},{"strike":53400.0,"call_gex_1pct":9276.205218067216,"put_gex_1pct":0.0,"net_gex_1pct":9276.205218067216,"gross_gex_1pct":9276.205218067216,"call_oi":69,"put_oi":0},{"strike":53500.0,"call_gex_1pct":17546.01993827827,"put_gex_1pct":0.0,"net_gex_1pct":17546.01993827827,"gross_gex_1pct":17546.01993827827,"call_oi":132,"put_oi":0},{"strike":53600.0,"call_gex_1pct":2760.249543284631,"put_gex_1pct":0.0,"net_gex_1pct":2760.249543284631,"gross_gex_1pct":2760.249543284631,"call_oi":21,"put_oi":0},{"strike":53700.0,"call_gex_1pct":7539.138645062306,"put_gex_1pct":0.0,"net_gex_1pct":7539.138645062306,"gross_gex_1pct":7539.138645062306,"call_oi":58,"put_oi":0},{"strike":53800.0,"call_gex_1pct":3599.615980296722,"put_gex_1pct":0.0,"net_gex_1pct":3599.615980296722,"gross_gex_1pct":3599.615980296722,"call_oi":28,"put_oi":0},{"strike":53900.0,"call_gex_1pct":2034.518562139541,"put_gex_1pct":0.0,"net_gex_1pct":2034.518562139541,"gross_gex_1pct":2034.518562139541,"call_oi":16,"put_oi":0},{"strike":54000.0,"call_gex_1pct":28301.293254537195,"put_gex_1pct":0.0,"net_gex_1pct":28301.293254537195,"gross_gex_1pct":28301.293254537195,"call_oi":225,"put_oi":0},{"strike":54100.0,"call_gex_1pct":1244.3537054238627,"put_gex_1pct":0.0,"net_gex_1pct":1244.3537054238627,"gross_gex_1pct":1244.3537054238627,"call_oi":10,"put_oi":0},{"strike":54200.0,"call_gex_1pct":1846.684177040218,"put_gex_1pct":0.0,"net_gex_1pct":1846.684177040218,"gross_gex_1pct":1846.684177040218,"call_oi":15,"put_oi":0},{"strike":54300.0,"call_gex_1pct":2436.272093885376,"put_gex_1pct":0.0,"net_gex_1pct":2436.272093885376,"gross_gex_1pct":2436.272093885376,"call_oi":20,"put_oi":0},{"strike":54400.0,"call_gex_1pct":2290.235786101755,"put_gex_1pct":0.0,"net_gex_1pct":2290.235786101755,"gross_gex_1pct":2290.235786101755,"call_oi":19,"put_oi":0},{"strike":54500.0,"call_gex_1pct":6799.361148824216,"put_gex_1pct":0.0,"net_gex_1pct":6799.361148824216,"gross_gex_1pct":6799.361148824216,"call_oi":57,"put_oi":0},{"strike":54600.0,"call_gex_1pct":2125.043226527533,"put_gex_1pct":0.0,"net_gex_1pct":2125.043226527533,"gross_gex_1pct":2125.043226527533,"call_oi":18,"put_oi":0},{"strike":54700.0,"call_gex_1pct":2687.5711186475987,"put_gex_1pct":0.0,"net_gex_1pct":2687.5711186475987,"gross_gex_1pct":2687.5711186475987,"call_oi":23,"put_oi":0},{"strike":54800.0,"call_gex_1pct":925.3229903569172,"put_gex_1pct":0.0,"net_gex_1pct":925.3229903569172,"gross_gex_1pct":925.3229903569172,"call_oi":8,"put_oi":0},{"strike":54900.0,"call_gex_1pct":2862.519840775596,"put_gex_1pct":0.0,"net_gex_1pct":2862.519840775596,"gross_gex_1pct":2862.519840775596,"call_oi":25,"put_oi":0},{"strike":55000.0,"call_gex_1pct":57811.898706815104,"put_gex_1pct":0.0,"net_gex_1pct":57811.898706815104,"gross_gex_1pct":57811.898706815104,"call_oi":510,"put_oi":0},{"strike":55100.0,"call_gex_1pct":1571.2548274743351,"put_gex_1pct":0.0,"net_gex_1pct":1571.2548274743351,"gross_gex_1pct":1571.2548274743351,"call_oi":14,"put_oi":0},{"strike":55200.0,"call_gex_1pct":444.51112811377334,"put_gex_1pct":0.0,"net_gex_1pct":444.51112811377334,"gross_gex_1pct":444.51112811377334,"call_oi":4,"put_oi":0},{"strike":55300.0,"call_gex_1pct":1320.5049568396134,"put_gex_1pct":0.0,"net_gex_1pct":1320.5049568396134,"gross_gex_1pct":1320.5049568396134,"call_oi":12,"put_oi":0},{"strike":55400.0,"call_gex_1pct":980.774348292749,"put_gex_1pct":0.0,"net_gex_1pct":980.774348292749,"gross_gex_1pct":980.774348292749,"call_oi":9,"put_oi":0},{"strike":55500.0,"call_gex_1pct":1403.0365194098752,"put_gex_1pct":0.0,"net_gex_1pct":1403.0365194098752,"gross_gex_1pct":1403.0365194098752,"call_oi":13,"put_oi":0},{"strike":55600.0,"call_gex_1pct":1817.2069935731547,"put_gex_1pct":0.0,"net_gex_1pct":1817.2069935731547,"gross_gex_1pct":1817.2069935731547,"call_oi":17,"put_oi":0},{"strike":55700.0,"call_gex_1pct":529.4022141937508,"put_gex_1pct":0.0,"net_gex_1pct":529.4022141937508,"gross_gex_1pct":529.4022141937508,"call_oi":5,"put_oi":0},{"strike":55800.0,"call_gex_1pct":839.0658102506729,"put_gex_1pct":0.0,"net_gex_1pct":839.0658102506729,"gross_gex_1pct":839.0658102506729,"call_oi":8,"put_oi":0},{"strike":55900.0,"call_gex_1pct":6441.954377924471,"put_gex_1pct":0.0,"net_gex_1pct":6441.954377924471,"gross_gex_1pct":6441.954377924471,"call_oi":62,"put_oi":0},{"strike":56000.0,"call_gex_1pct":8646.779895278136,"put_gex_1pct":0.0,"net_gex_1pct":8646.779895278136,"gross_gex_1pct":8646.779895278136,"call_oi":84,"put_oi":0},{"strike":56100.0,"call_gex_1pct":4487.514112800376,"put_gex_1pct":0.0,"net_gex_1pct":4487.514112800376,"gross_gex_1pct":4487.514112800376,"call_oi":44,"put_oi":0},{"strike":56200.0,"call_gex_1pct":202.11087449383086,"put_gex_1pct":0.0,"net_gex_1pct":202.11087449383086,"gross_gex_1pct":202.11087449383086,"call_oi":2,"put_oi":0},{"strike":56400.0,"call_gex_1pct":198.4663196686019,"put_gex_1pct":0.0,"net_gex_1pct":198.4663196686019,"gross_gex_1pct":198.4663196686019,"call_oi":2,"put_oi":0},{"strike":56500.0,"call_gex_1pct":1573.4998310365315,"put_gex_1pct":0.0,"net_gex_1pct":1573.4998310365315,"gross_gex_1pct":1573.4998310365315,"call_oi":16,"put_oi":0},{"strike":56600.0,"call_gex_1pct":97.46837162053038,"put_gex_1pct":0.0,"net_gex_1pct":97.46837162053038,"gross_gex_1pct":97.46837162053038,"call_oi":1,"put_oi":0},{"strike":56700.0,"call_gex_1pct":96.60674787250261,"put_gex_1pct":0.0,"net_gex_1pct":96.60674787250261,"gross_gex_1pct":96.60674787250261,"call_oi":1,"put_oi":0},{"strike":56900.0,"call_gex_1pct":4841.100607439076,"put_gex_1pct":0.0,"net_gex_1pct":4841.100607439076,"gross_gex_1pct":4841.100607439076,"call_oi":51,"put_oi":0},{"strike":57000.0,"call_gex_1pct":37075.94506197298,"put_gex_1pct":0.0,"net_gex_1pct":37075.94506197298,"gross_gex_1pct":37075.94506197298,"call_oi":394,"put_oi":0},{"strike":57100.0,"call_gex_1pct":31532.63474851793,"put_gex_1pct":0.0,"net_gex_1pct":31532.63474851793,"gross_gex_1pct":31532.63474851793,"call_oi":338,"put_oi":0},{"strike":57200.0,"call_gex_1pct":47449.71912720239,"put_gex_1pct":0.0,"net_gex_1pct":47449.71912720239,"gross_gex_1pct":47449.71912720239,"call_oi":513,"put_oi":0},{"strike":57300.0,"call_gex_1pct":151870.77246731374,"put_gex_1pct":0.0,"net_gex_1pct":151870.77246731374,"gross_gex_1pct":151870.77246731374,"call_oi":1656,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 41,600 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-16→2026-11-17) | -1,500 | TAIFEX Proxy snapshots (2026-11-16) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 135,406 | 133,406 | +2,000 | 81,643 | 81,147 | +496 | +1,504 | TAIFEX Proxy |
| 投信 | 8,005 | 18,220 | -10,215 | 0 | 0 | +0 | -10,215 | TAIFEX Proxy |
| 自營商 | 134,884 | 138,634 | -3,750 | 39,569 | 42,428 | -2,859 | -891 | TAIFEX Proxy |
| 三大法人合計 | 278,295 | 290,260 | -11,965 | 121,212 | 123,575 | -2,363 | -9,602 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 24.03 | 21.58 | +2.45 | 11.33 | 10.97 | +0.35 | +2.10 | TAIFEX Proxy |
| 投信 | 0.17 | 11.21 | -11.04 | 0.00 | 0.00 | +0 | -11.04 | TAIFEX Proxy |
| 自營商 | 29.03 | 21.62 | +7.41 | 7.19 | 7.48 | -0.29 | +7.70 | TAIFEX Proxy |
| 三大法人合計 | 53.23 | 54.40 | -1.18 | 18.52 | 18.45 | +0.06 | -1.24 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 56,585 | TAIFEX Proxy |
| 買權空方 OI | 89,839 | TAIFEX Proxy |
| 買權多空淨 OI | -33,254 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-13→2026-11-17) | -26,342 | TAIFEX Proxy snapshots (2026-11-16) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 40,929 | TAIFEX Proxy |
| 賣權空方 OI | 36,173 | TAIFEX Proxy |
| 賣權多空淨 OI | +4,756 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-13→2026-11-17) | +2,345 | TAIFEX Proxy snapshots (2026-11-16) |
- 資料日期：買權 2026-11-17／賣權 2026-11-17 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -21,237 | 2026-11-13→2026-11-17 | TAIFEX Proxy snapshots (2026-11-16) |
| 買權前十大 | -26,342 | 2026-11-13→2026-11-17 | TAIFEX Proxy snapshots (2026-11-16) |
| 賣權前十大 | +2,345 | 2026-11-13→2026-11-17 | TAIFEX Proxy snapshots (2026-11-16) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-17；本次報告產製時間：2026-11-18 08:43:32；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
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
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)`
- margin_ratio：`Blave 上市市場融資維持率估算（當日暫估；資料日期：2026-11-17；自建計算備援）`
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
- 註記：上市市場維持率為當日暫估；TWSE 自建部分計算僅供診斷（部分估算 153.7444%；價格覆蓋率 0.999195；已估值 1242/1243 檔；缺價 1 檔：['1589']），不得作為正式維持率。TWSE 自建計算未成功（partial calculation only; missing close for 1 listed securities: ['1589']）；改用 Blave 同 T0 數值（2026-11-17）。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-17 非今日 2026-11-18，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -380.9 | -97,896 | -1,144 | -65 | +2,000 | +496 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -38.2 | +91,226 | -1,180 | +0 | -10,215 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -157.0 | -436 | -1,820 | -333 | -3,750 | -2,859 | 趨勢偏空 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
