# DATA_REPORT_20261118

- 報告日期：`2026-11-19`
- T0 交易日期：`2026-11-18`
- 首次資料產出時間：`2026-11-19 13:58:07`
- 本次更新開始時間：`2026-11-19 13:58:07`
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
| 加權指數 | 40,194.91 | 點 | twse-proxy |
| 開盤 | 40,720.09 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 40,938.20 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 39,260.99 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 40,194.91 | 點 | twse-proxy |
| 漲跌點數 | 102.80 | 點 | twse-proxy |
| 漲跌幅 | +0.26 | % | twse-proxy |
| 成交金額 | 10,751.7 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 492 | twse-proxy |
| 下跌家數 | 520 | twse-proxy |
| 平盤家數 | 71 | twse-proxy |
| 漲停家數 | 21 | twse-proxy |
| 跌停家數 | 4 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 352 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 433 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 86 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 16 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 9 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -765.6 | 億元 | twse-proxy /institutional |
| 投信 | +166.1 | 億元 | twse-proxy /institutional |
| 自營商 | -42.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -641.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-18；估值 1242 檔；1 檔採最近有效收盤價（價格日期 20261111 至 20261118）；Blave 同 T0 交叉驗證 156.2150%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 6,652.5 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -39.1 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 223,288 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -18,748 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 156.24 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-18；估值 1242 檔；1 檔採最近有效收盤價（價格日期 20261111 至 20261118）；Blave 同 T0 交叉驗證 156.2150%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 33,809,810 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,415,396.417 | 2,165,706.932 | 20,581,103.349 | 張 |
| 借券賣出增減 | +54,625.818 | +3,661.154 | +58,286.972 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261118`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-19T13:58:20+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261118`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-19T13:58:20+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 10,751.7 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,140.5 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 12,892.3 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,323.63 | -16.90 | -0.23 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,429.88 | 101.50 | +0.42 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 27,116.26 | 114.48 | +0.42 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,198.17 | -561.25 | -1.11 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,652.80 | 9.92 | +0.10 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 24.56 | -0.90 | -3.53 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,288.56 | 264.28 | +0.45 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,066.08 | -1.36 | -0.03 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,809.93 | -484.82 | -2.08 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,568.71 | -19.12 | -0.53 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,594.71 | -64.70 | -0.61 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,385.50 | 45.00 | +0.61 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,472.00 | 285.25 | +1.05 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,482.00 | 209.00 | +0.42 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,729.70 | 7.70 | +0.28 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.80 | 0.00 | 18-NOV-26 | 2026-11-19T05:58:42+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 5.07 | -0.04 | 2026-11-18 | 2026-11-19T05:58:42+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.44 | -0.06 | 18-NOV-26 | 2026-11-19T05:59:00+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.41 | -0.05 | 2026-11-18 | 2026-11-19T05:59:01+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.95 | 0.04 | +0.13 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.88 | 0.02 | +0.02 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.54 | 0.03 | +0.02 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,330.99 | -2.02 | -0.15 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 362.62 | 2.93 | +0.81 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.96 | -0.18 | -1.27 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 32.52 | 0.69 | +2.17 | 2026-11-18 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 82.12 | -1.14 | -1.37 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,738.60 | -3.30 | -0.09 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 63,272.69 | -1,621.25 | -2.50 | 2026-11-19 | 2026-11-19T05:58:21+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：0050零股大爆量 分析師勸別急接刀
  - 來源：Yahoo 台股；發布時間：2026-11-19T05:49:13Z；台北時間：2026-11-19 13:49
  - 摘要：小資族勇敢抄底！元大台灣50（0050）盤中最低跌至89.8元，創逾一周新低，收盤以90.2元作收，下跌4.14％，但零股成交量一天爆3775萬股。分析師表示，近期投資人不必恐慌殺低，但空手者也別急著「接刀」，靜待量縮止跌、站穩支撐後再分批
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%91%94%E7%A0%B43%E8%90%AC9%EF%BC%81%E5%B0%8F%E8%B3%87%E6%97%8F%E6%90%B6%E8%B2%B70050-%E9%9B%B6%E8%82%A1%E4%B8%80%E5%A4%A9%E7%88%863775%E8%90%AC%E8%82%A1-054913626.html
- 事件2：大單利多不敵賣壓 日月光漲一天又重挫
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:40:00Z；台北時間：2026-11-19 12:40
  - 摘要：[FTNN新聞網]記者陳雅婷／綜合報導台股今（19）日賣壓再度擴大，早盤開高後一路走低，盤中最高來到40,315.53點，隨後下探38,259.70點，截至中午12時10分報39,...
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%95%B8%E5%8D%81%E5%84%84%E7%BE%8E%E5%85%83%E5%A4%A7%E5%96%AE%E8%90%BD%E8%A2%8B-%E6%97%A5%E6%9C%88%E5%85%89%E6%8B%BF%E4%B8%8Bai%E5%B0%81%E8%A3%9D%E5%A4%A7%E6%A9%9F%E6%9C%83-%E8%82%A1%E5%83%B9%E4%BB%8A%E5%8D%BB%E9%87%8D%E6%8C%AB%E9%80%BE5-044000904.html
- 事件3：輝達回不去了？外媒預測黃仁勳籌資另開戰場
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:40:00Z；台北時間：2026-11-19 12:40
  - 摘要：財經中心／李明融報導輝達（NVIDIA）前執行長黃仁勳因風波離任後，外界高度關注他是否還有機會重掌兵符。對此，美媒Semafor商業記者戈斯瓦米分析，董事會當初是經過數小時討論才讓黃仁勳在「自行辭職或遭解雇」間二選一，加上輝達身為上市公司，
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%BB%83%E4%BB%81%E5%8B%B3-%E5%9B%9E%E9%8D%8B%E8%BC%9D%E9%81%94-%E6%A9%9F%E7%8E%87%E6%9B%9D-%E5%A4%96%E5%AA%92%E6%8F%AD-%E8%80%81%E9%BB%83%E5%BE%A9%E4%BB%87%E5%8A%87%E6%9C%AC-044000049.html
- 事件4：昨天亮眼今天變臉 5檔輝達概念股躺跌停
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:23:37Z；台北時間：2026-11-19 12:23
  - 摘要：輝達財報雖亮眼並點名台積電、鴻海等6家台廠，但受創辦人風波及股價連黑影響，台股今（19）日無量大跌逾1400點，摜破40K與39K關卡，創意、景碩等概念股苦吞跌停。市場正聚焦Anthropic美股IPO能否拯救AI投資信心。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BC%9D%E9%81%94%E6%A6%82%E5%BF%B5%E8%82%A1%E8%B1%AC%E7%BE%8A%E8%AE%8A%E8%89%B2-%E8%82%A1%E5%90%8E%E5%89%B5%E6%84%8F-%E4%BA%AC%E5%85%83%E9%9B%BB%E5%85%A8%E8%B7%8C%E5%81%9C-041700554.html
- 事件5：12月恐升不只1碼 聯準會放鷹點名AI風險
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:39:00Z；台北時間：2026-11-19 12:39
  - 摘要：聯準會公布10月會議記錄顯示，幾乎全數官員支持持續升息以對抗通膨，部分官員更主張若通膨數據不佳，12月可能需升息超過1碼。受此鷹派立場與通膨升溫影響，美元指數創下近19個月新高，黃金與比特幣等資產全面承壓。此外，報告也點出AI基建熱潮與複雜
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%81%AF%E6%BA%96%E6%9C%83%E6%9C%83%E8%AD%B0%E8%A8%98%E9%8C%84%E6%94%BE%E9%B7%B9-%E5%B9%BE%E4%B9%8E%E6%89%80%E6%9C%89%E4%BA%BA-%E5%96%8A%E5%86%8D%E5%8D%87%E6%81%AF-%E8%AD%A6%E5%91%8Aai%E7%86%B1%E6%BD%AE%E6%88%90%E9%A2%A8%E9%9A%AA-043900198.html
- 事件6：兆豐金衝天價後收斂 官股金控齊撐盤
  - 來源：Yahoo 台股；發布時間：2026-11-19T04:26:20Z；台北時間：2026-11-19 12:26
  - 摘要：台股今（19）日盤中重挫1,935.21點，加權指數最低探至38,259.7點，跌破年線、陷3萬8千點保衛戰。金融股多數走低，惟公股龍頭兆豐金（2886）逆勢大漲逾7%，最高攻上56.5元，寫下歷史新天價。華南金（2880）、合庫金（588
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%87%91%E8%9E%8D%E8%82%A1%E6%9C%80%E9%A3%86%EF%BC%81%E5%85%86%E8%B1%90%E9%87%91%E4%B8%80%E5%BA%A6%E9%80%86%E5%8B%A2%E5%A4%A7%E6%BC%B2%E9%80%BE7-%E6%94%B9%E5%AF%AB%E6%AD%B7%E5%8F%B2%E6%96%B0%E5%A4%A9%E5%83%B9-042501962.html
- 事件7：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 來源：Federal Reserve；發布時間：Wed, 18 Nov 2026 19:00:00 GMT；台北時間：2026-11-19 03:00
  - 摘要：Minutes of the Federal Open Market Committee, October 27-28, 2026
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm
- 事件8：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions, and changes to streamline and adjust their check services
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 18:30:00 GMT；台北時間：2026-11-13 02:30
  - 摘要：Federal Reserve Board announces pricing, effective January 1, 2027, for payment services the Federal Reserve Banks provide to banks and credit unions,
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/other20261112a.htm
- 事件9：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 17:45:00 GMT；台北時間：2026-11-13 01:45
  - 摘要：Federal Reserve announces revised tentative schedule of Federal Open Market Committee meetings in 2027
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/monetary20261112a.htm
- 事件10：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 來源：Federal Reserve；發布時間：Thu, 12 Nov 2026 16:00:00 GMT；台北時間：2026-11-13 00:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of United Community Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261112a.htm
- 事件11：Fed officials expect more rate hikes, worry about AI impact on inflation, minutes show
  - 來源：CNBC；發布時間：Wed, 18 Nov 2026 19:41:59 GMT；台北時間：2026-11-19 03:41
  - 摘要：The Federal Reserve on Wednesday released minutes from its October policy meeting at which it voted to hold its benchmark interest rate in a range bet
  - 原文連結：https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html
- 事件12：Inside India newsletter: Foreign flows helped the market recover. Now it faces the inflation test
  - 來源：CNBC；發布時間：Thu, 19 Nov 2026 00:01:23 GMT；台北時間：2026-11-19 08:01
  - 摘要：India’s inflation, which has been on the rise for 12 straight months, is becoming a risk to growth and to the reversal of foreign inflows.
  - 原文連結：https://www.cnbc.com/2026/11/19/india-inflation-foreign-investor-nifty50.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-18

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 41,073 | 點 | TAIFEX Proxy |
| 最高價 | 41,205 | 點 | TAIFEX Proxy |
| 最低價 | 39,523 | 點 | TAIFEX Proxy |
| 收盤價 | 40,312 | 點 | TAIFEX Proxy |
| 漲跌點數 | +205 | 點 | TAIFEX Proxy |
| 漲跌幅 | +0.51 | % | TAIFEX Proxy |
| 成交量 | 74,871 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 41,205 / 39,523 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 40,330 | 點 | TAIFEX Proxy |
| 最高價 | 40,689 | 點 | TAIFEX Proxy |
| 最低價 | 39,411 | 點 | TAIFEX Proxy |
| 收盤價 | 39,987 | 點 | TAIFEX Proxy |
| 漲跌點數 | -345 | 點 | TAIFEX Proxy |
| 漲跌幅 | -0.86 | % | TAIFEX Proxy |
| 成交量 | 56,051 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,689 / 39,411 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 9,922 | TAIFEX Proxy |
| 外資空方 OI | 109,360 | TAIFEX Proxy |
| 外資多空淨 OI | -99,438 | TAIFEX Proxy |
| 投信多方 OI | 96,839 | TAIFEX Proxy |
| 投信空方 OI | 3,266 | TAIFEX Proxy |
| 投信多空淨 OI | +93,573 | TAIFEX Proxy |
| 自營商多方 OI | 3,306 | TAIFEX Proxy |
| 自營商空方 OI | 4,763 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,457 | TAIFEX Proxy |
| 三大法人合計多方 OI | 110,067 | TAIFEX Proxy |
| 三大法人合計空方 OI | 117,389 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,322 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,542 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +2,347 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,021 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,057 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,315 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,742 | TAIFEX Proxy |
| 多空淨 OI 變化 | unavailable | 換月基準重建 |
- 資料日期：2026-11-18 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 93,106 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 95,726 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -2,620 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 33,877 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 33,985 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -108 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -2,512 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +2,347 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +2,347 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -2,486 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +262 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -2,748 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -2,759 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +154 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -221.7 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +12.2 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 40,312 | TAIFEX Proxy |
| 加權指數價格 | 40,194.91 | twse-proxy |
| 台指期與加權指數價差 | +117.09 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +0.29 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +117.09 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -325 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 40,312 | 39,987 | +325 | TAIFEX Proxy |
| 成交量 | 74,871 | 56,051 | +18,820 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-216（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 93,106 | 95,726 | -2,620 | 33,877 | 33,985 | -108 | -2,512 | 9,922 | 109,360 | -99,438 | -1,542 | TAIFEX Proxy |
| 投信 | 2,599 | 252 | +2,347 | 0 | 0 | +0 | +2,347 | 96,839 | 3,266 | +93,573 | +2,347 | TAIFEX Proxy |
| 自營商 | 12,215 | 14,701 | -2,486 | 1,121 | 859 | +262 | -2,748 | 3,306 | 4,763 | -1,457 | -1,021 | TAIFEX Proxy |
| 三大法人合計 | 107,920 | 110,679 | -2,759 | 34,998 | 34,844 | +154 | -2,913 | 110,067 | 117,389 | -7,322 | -216 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 100,057 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,315 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,742 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | unavailable | 換月基準重建 |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 42.81% | TAIFEX Proxy |
| 夜盤漲跌點數 | -345 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -108 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-18 | TAIFEX Proxy |
| 到期月份／到期日 | 202611 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-19 13:58:07 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 409,461 | TAIFEX Proxy |
| Call 總未平倉量 OI | 167,265 | TAIFEX Proxy |
| Call OI 增減（共同合約） | +25,037 | 沿用前版（原來源：TAIFEX Proxy snapshot bundle (2026-11-17→2026-11-18)） |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 402,395 | TAIFEX Proxy |
| Put 總未平倉量 OI | 113,894 | TAIFEX Proxy |
| Put OI 增減（共同合約） | +35,578 | 沿用前版（原來源：TAIFEX Proxy snapshot bundle (2026-11-17→2026-11-18)） |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.02 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.47 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.68 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-17→2026-11-18) | 13.02 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-17→2026-11-18) | -14.28 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 143,558 | TAIFEX Proxy |
| 外資 Call日賣 | 139,131 | TAIFEX Proxy |
| 外資 Call日淨 | +4,427 | TAIFEX Proxy |
| 外資 Put日買 | 148,683 | TAIFEX Proxy |
| 外資 Put日賣 | 150,740 | TAIFEX Proxy |
| 外資 Put日淨 | -2,057 | TAIFEX Proxy |
| 外資 Call夜買 | 20,465 | TAIFEX Proxy |
| 外資 Call夜賣 | 21,034 | TAIFEX Proxy |
| 外資 Call夜淨 | -569 | TAIFEX Proxy |
| 外資 Put夜買 | 20,222 | TAIFEX Proxy |
| 外資 Put夜賣 | 21,075 | TAIFEX Proxy |
| 外資 Put夜淨 | -853 | TAIFEX Proxy |
| 外資 日盤淨總量 | +6,484 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +4,996 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -1,204 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 103,086 | TAIFEX Proxy |
| 自營商 Call日賣 | 114,939 | TAIFEX Proxy |
| 自營商 Call日淨 | -11,853 | TAIFEX Proxy |
| 自營商 Put日買 | 94,078 | TAIFEX Proxy |
| 自營商 Put日賣 | 111,089 | TAIFEX Proxy |
| 自營商 Put日淨 | -17,011 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,065 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,102 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,037 | TAIFEX Proxy |
| 自營商 Put夜買 | 12,324 | TAIFEX Proxy |
| 自營商 Put夜賣 | 12,906 | TAIFEX Proxy |
| 自營商 Put夜淨 | -582 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +5,158 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -10,816 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -16,429 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 46,000 | 7,825 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,500 | 7,630 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 6,064 | TAIFEX Proxy |
| Call OI 最大履約價 | 46,000 | 7,825 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 46,000 | 7,825 | 4.68% | TAIFEX Proxy |
| C2 | 43,500 | 7,630 | 4.56% | TAIFEX Proxy |
| C3 | 44,000 | 6,064 | 3.63% | TAIFEX Proxy |
| C4 | 41,000 | 4,767 | 2.85% | TAIFEX Proxy |
| C5 | 45,000 | 3,808 | 2.28% | TAIFEX Proxy |
| C6 | 43,000 | 3,709 | 2.22% | TAIFEX Proxy |
| C7 | 42,000 | 3,502 | 2.09% | TAIFEX Proxy |
| C8 | 48,000 | 3,396 | 2.03% | TAIFEX Proxy |
| C9 | 46,500 | 3,343 | 2.0% | TAIFEX Proxy |
| C10 | 47,000 | 3,093 | 1.85% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 33,700 | 11,549 | TAIFEX Proxy |
| Put OI 第2大履約價 | 40,000 | 4,691 | TAIFEX Proxy |
| Put OI 第3大履約價 | 36,000 | 4,490 | TAIFEX Proxy |
| Put OI 最大履約價 | 33,700 | 11,549 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 33,700 | 11,549 | 10.14% | TAIFEX Proxy |
| P2 | 40,000 | 4,691 | 4.12% | TAIFEX Proxy |
| P3 | 36,000 | 4,490 | 3.94% | TAIFEX Proxy |
| P4 | 38,000 | 4,109 | 3.61% | TAIFEX Proxy |
| P5 | 37,000 | 4,094 | 3.59% | TAIFEX Proxy |
| P6 | 39,000 | 4,030 | 3.54% | TAIFEX Proxy |
| P7 | 36,200 | 3,830 | 3.36% | TAIFEX Proxy |
| P8 | 39,500 | 3,525 | 3.09% | TAIFEX Proxy |
| P9 | 38,500 | 2,697 | 2.37% | TAIFEX Proxy |
| P10 | 36,500 | 2,604 | 2.29% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 41,000 (+3,284) | 沿用前版（原來源：TAIFEX Proxy snapshot bundle (2026-11-17→2026-11-18)） |
| Call OI 減少最多的履約價（共同合約） | 46,000 (-1,159) | 沿用前版（原來源：TAIFEX Proxy snapshot bundle (2026-11-17→2026-11-18)） |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 36,200 (+3,570) | 沿用前版（原來源：TAIFEX Proxy snapshot bundle (2026-11-17→2026-11-18)） |
| Put OI 減少最多的履約價（共同合約） | 42,500 (-320) | 沿用前版（原來源：TAIFEX Proxy snapshot bundle (2026-11-17→2026-11-18)） |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 46,000 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 33,700 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-17→2026-11-18) | +0 | TAIFEX Proxy snapshots (2026-11-17) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 39,500.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611F3 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-20 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611 | TAIFEX Proxy |
| 資料日期 | 2026-11-18 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 36,223.97 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611F3 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-20 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 45,066 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 45,056 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 13,105 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 13,105 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-18 | TAIFEX Proxy (options-gamma-levels) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：36,175.42～44,214.40
- 搜尋步長／計算次數：10.00／6
- 起點／終點 Net GEX：-32,021,696.29／976,268.34
- 搜尋區間最低／最高 Net GEX：-32,021,696.29／976,268.34
- 正負號交叉次數：1
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-18","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":0},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":214,"delta_rows":218},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":0,"delta_rows":246},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：34,165.67～46,224.15
- 搜尋步長／計算次數：10.00／1207
- 起點／終點 Net GEX：-288,195,673.28／2,053,614,650.75
- 搜尋區間最低／最高 Net GEX：-359,419,741.27／3,232,351,157.02
- 正負號交叉次數：1
- 擴大區間診斷 Flip：36,223.97

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 3,200,834,625.92 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 5,449,339,641.17 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 201 | 資料日期：2026-11-18 |
| 正 Net GEX 最大履約價 | 39,500 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 38,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：39,500（279,273,745.15 NT$）、38,900（247,025,901.80 NT$）、39,100（237,394,518.47 NT$）、38,700（230,555,453.29 NT$）、38,600（214,935,974.77 NT$）
- 負 Net GEX Top 5：38,000（-55,033,587.59 NT$）、35,700（-27,511,477.75 NT$）、40,000（-20,774,454.16 NT$）、37,000（-19,001,864.47 NT$）、37,700（-16,309,674.54 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-18","underlying":40194.91,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":3200834625.9162054,"gross_gex_1pct":5449339641.174176,"gamma_diagnostics":{"chain_rows":404,"delta_rows":404,"matched_strike_keys":404,"positive_oi_settlement_eligible":345,"invalid_oi":59,"invalid_settlement":0,"below_intrinsic":6,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":339},"formal_flip_diagnostics":{"search_lower_underlying":36175.419,"search_upper_underlying":44214.401000000005,"step":10,"evaluations":6,"start_net_gex_1pct":-32021696.28540028,"end_net_gex_1pct":976268.3356710034,"min_net_gex_1pct":-32021696.28540028,"max_net_gex_1pct":976268.3356710034,"zero_crossings":1,"found":true},"wide_range_flip":{"lower_underlying":36215.673500000004,"upper_underlying":36225.673500000004,"estimated_underlying":36223.97068514771,"lower_net_gex_1pct":-5598077.834312801,"upper_net_gex_1pct":1148882.411429801},"wide_range_flip_diagnostics":{"search_lower_underlying":34165.673500000004,"search_upper_underlying":46224.1465,"reference_underlying":40194.91,"step":10,"evaluations":1207,"start_net_gex_1pct":-288195673.2818655,"end_net_gex_1pct":2053614650.747673,"min_net_gex_1pct":-359419741.2651078,"max_net_gex_1pct":3232351157.0208097,"zero_crossings":1,"found":true,"selected_crossing_distance":3970.939314852294},"expiry_selection_diagnostics":{"requested_date":"2026-11-18","chain_expiries":[{"contract_month":"202611","expiry":"2026-11-18"},{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611","expiry":"2026-11-18","chain_rows":616,"delta_rows":0},{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":404,"delta_rows":404},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":390,"delta_rows":390},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":366,"delta_rows":366},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":214,"delta_rows":218},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":562,"delta_rows":562},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":410,"delta_rows":410},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":0,"delta_rows":246},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":284,"delta_rows":284},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":284,"delta_rows":284}],"selected":{"contract_month":"202611F3","expiry":"2026-11-20","delta_contract_month":"202611F3","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":35700.0,"call_gex_1pct":0.0,"put_gex_1pct":-27511477.754373226,"net_gex_1pct":-27511477.754373226,"gross_gex_1pct":27511477.754373226,"call_oi":0,"put_oi":1736},{"strike":35800.0,"call_gex_1pct":0.0,"put_gex_1pct":-1318218.8073996266,"net_gex_1pct":-1318218.8073996266,"gross_gex_1pct":1318218.8073996266,"call_oi":0,"put_oi":73},{"strike":35900.0,"call_gex_1pct":0.0,"put_gex_1pct":-1110774.021602753,"net_gex_1pct":-1110774.021602753,"gross_gex_1pct":1110774.021602753,"call_oi":0,"put_oi":55},{"strike":36000.0,"call_gex_1pct":0.0,"put_gex_1pct":-7785149.4190820465,"net_gex_1pct":-7785149.4190820465,"gross_gex_1pct":7785149.4190820465,"call_oi":0,"put_oi":368},{"strike":36100.0,"call_gex_1pct":0.0,"put_gex_1pct":-3983382.9278851314,"net_gex_1pct":-3983382.9278851314,"gross_gex_1pct":3983382.9278851314,"call_oi":0,"put_oi":175},{"strike":36200.0,"call_gex_1pct":0.0,"put_gex_1pct":-854643.5895073529,"net_gex_1pct":-854643.5895073529,"gross_gex_1pct":854643.5895073529,"call_oi":0,"put_oi":35},{"strike":36300.0,"call_gex_1pct":0.0,"put_gex_1pct":-2183896.2665691325,"net_gex_1pct":-2183896.2665691325,"gross_gex_1pct":2183896.2665691325,"call_oi":0,"put_oi":83},{"strike":36400.0,"call_gex_1pct":0.0,"put_gex_1pct":-762987.3577242498,"net_gex_1pct":-762987.3577242498,"gross_gex_1pct":762987.3577242498,"call_oi":0,"put_oi":27},{"strike":36500.0,"call_gex_1pct":0.0,"put_gex_1pct":-2906607.7574214656,"net_gex_1pct":-2906607.7574214656,"gross_gex_1pct":2906607.7574214656,"call_oi":0,"put_oi":95},{"strike":36600.0,"call_gex_1pct":0.0,"put_gex_1pct":-1931422.549659001,"net_gex_1pct":-1931422.549659001,"gross_gex_1pct":1931422.549659001,"call_oi":0,"put_oi":60},{"strike":36700.0,"call_gex_1pct":0.0,"put_gex_1pct":-1967505.5147680603,"net_gex_1pct":-1967505.5147680603,"gross_gex_1pct":1967505.5147680603,"call_oi":0,"put_oi":57},{"strike":36800.0,"call_gex_1pct":0.0,"put_gex_1pct":-2662544.6000931696,"net_gex_1pct":-2662544.6000931696,"gross_gex_1pct":2662544.6000931696,"call_oi":0,"put_oi":73},{"strike":36900.0,"call_gex_1pct":0.0,"put_gex_1pct":-2479197.1698330217,"net_gex_1pct":-2479197.1698330217,"gross_gex_1pct":2479197.1698330217,"call_oi":0,"put_oi":62},{"strike":37000.0,"call_gex_1pct":0.0,"put_gex_1pct":-19001864.467881836,"net_gex_1pct":-19001864.467881836,"gross_gex_1pct":19001864.467881836,"call_oi":0,"put_oi":441},{"strike":37100.0,"call_gex_1pct":0.0,"put_gex_1pct":-1275072.8736037845,"net_gex_1pct":-1275072.8736037845,"gross_gex_1pct":1275072.8736037845,"call_oi":0,"put_oi":28},{"strike":37200.0,"call_gex_1pct":0.0,"put_gex_1pct":-5148231.841316149,"net_gex_1pct":-5148231.841316149,"gross_gex_1pct":5148231.841316149,"call_oi":0,"put_oi":104},{"strike":37300.0,"call_gex_1pct":0.0,"put_gex_1pct":-3065681.082893433,"net_gex_1pct":-3065681.082893433,"gross_gex_1pct":3065681.082893433,"call_oi":0,"put_oi":58},{"strike":37400.0,"call_gex_1pct":0.0,"put_gex_1pct":-2891295.400789299,"net_gex_1pct":-2891295.400789299,"gross_gex_1pct":2891295.400789299,"call_oi":0,"put_oi":51},{"strike":37500.0,"call_gex_1pct":0.0,"put_gex_1pct":-8831458.593543008,"net_gex_1pct":-8831458.593543008,"gross_gex_1pct":8831458.593543008,"call_oi":0,"put_oi":145},{"strike":37600.0,"call_gex_1pct":0.0,"put_gex_1pct":-9240809.708696574,"net_gex_1pct":-9240809.708696574,"gross_gex_1pct":9240809.708696574,"call_oi":0,"put_oi":143},{"strike":37700.0,"call_gex_1pct":0.0,"put_gex_1pct":-16309674.53857207,"net_gex_1pct":-16309674.53857207,"gross_gex_1pct":16309674.53857207,"call_oi":0,"put_oi":238},{"strike":37800.0,"call_gex_1pct":0.0,"put_gex_1pct":-9750109.172081148,"net_gex_1pct":-9750109.172081148,"gross_gex_1pct":9750109.172081148,"call_oi":0,"put_oi":134},{"strike":37900.0,"call_gex_1pct":0.0,"put_gex_1pct":-6134990.651290165,"net_gex_1pct":-6134990.651290165,"gross_gex_1pct":6134990.651290165,"call_oi":0,"put_oi":79},{"strike":38000.0,"call_gex_1pct":0.0,"put_gex_1pct":-55033587.59176333,"net_gex_1pct":-55033587.59176333,"gross_gex_1pct":55033587.59176333,"call_oi":0,"put_oi":663},{"strike":38100.0,"call_gex_1pct":0.0,"put_gex_1pct":-6787200.899236564,"net_gex_1pct":-6787200.899236564,"gross_gex_1pct":6787200.899236564,"call_oi":0,"put_oi":77},{"strike":38200.0,"call_gex_1pct":0.0,"put_gex_1pct":-9114183.227964299,"net_gex_1pct":-9114183.227964299,"gross_gex_1pct":9114183.227964299,"call_oi":0,"put_oi":98},{"strike":38300.0,"call_gex_1pct":5680614.147022337,"put_gex_1pct":-11101250.229702115,"net_gex_1pct":-5420636.082679778,"gross_gex_1pct":16781864.37672445,"call_oi":63,"put_oi":113},{"strike":38400.0,"call_gex_1pct":8841291.511251532,"put_gex_1pct":-9832953.37344001,"net_gex_1pct":-991661.8621884789,"gross_gex_1pct":18674244.884691544,"call_oi":87,"put_oi":95},{"strike":38500.0,"call_gex_1pct":227080776.52217233,"put_gex_1pct":-48445180.335077934,"net_gex_1pct":178635596.1870944,"gross_gex_1pct":275525956.8572503,"call_oi":2066,"put_oi":447},{"strike":38550.0,"call_gex_1pct":11053130.019067029,"put_gex_1pct":-10097392.060822718,"net_gex_1pct":955737.9582443107,"gross_gex_1pct":21150522.079889745,"call_oi":97,"put_oi":91},{"strike":38600.0,"call_gex_1pct":235347874.491171,"put_gex_1pct":-20411899.718817223,"net_gex_1pct":214935974.77235377,"gross_gex_1pct":255759774.20998824,"call_oi":2000,"put_oi":179},{"strike":38650.0,"call_gex_1pct":11674578.638885932,"put_gex_1pct":-10786235.130897345,"net_gex_1pct":888343.507988587,"gross_gex_1pct":22460813.769783277,"call_oi":96,"put_oi":92},{"strike":38700.0,"call_gex_1pct":251553071.66971174,"put_gex_1pct":-20997618.377521213,"net_gex_1pct":230555453.29219052,"gross_gex_1pct":272550690.0472329,"call_oi":2000,"put_oi":174},{"strike":38750.0,"call_gex_1pct":13268837.10571425,"put_gex_1pct":-6423961.179977157,"net_gex_1pct":6844875.925737093,"gross_gex_1pct":19692798.285691407,"call_oi":103,"put_oi":53},{"strike":38800.0,"call_gex_1pct":266455604.4508606,"put_gex_1pct":-60799535.91391623,"net_gex_1pct":205656068.53694436,"gross_gex_1pct":327255140.36477685,"call_oi":2000,"put_oi":493},{"strike":38850.0,"call_gex_1pct":5368630.947450441,"put_gex_1pct":-7662715.8297470715,"net_gex_1pct":-2294084.88229663,"gross_gex_1pct":13031346.777197514,"call_oi":40,"put_oi":61},{"strike":38900.0,"call_gex_1pct":275934271.02679956,"put_gex_1pct":-28908369.224619776,"net_gex_1pct":247025901.80217978,"gross_gex_1pct":304842640.2514193,"call_oi":2005,"put_oi":225},{"strike":38950.0,"call_gex_1pct":15376129.528625898,"put_gex_1pct":-7214562.4817904495,"net_gex_1pct":8161567.046835449,"gross_gex_1pct":22590692.010416348,"call_oi":109,"put_oi":55},{"strike":39000.0,"call_gex_1pct":286786926.9247767,"put_gex_1pct":-83958047.79921652,"net_gex_1pct":202828879.12556016,"gross_gex_1pct":370744974.7239932,"call_oi":2003,"put_oi":630},{"strike":39050.0,"call_gex_1pct":31373305.443109274,"put_gex_1pct":-11042800.193842208,"net_gex_1pct":20330505.249267064,"gross_gex_1pct":42416105.636951484,"call_oi":214,"put_oi":82},{"strike":39100.0,"call_gex_1pct":297012772.6438754,"put_gex_1pct":-59618254.17072503,"net_gex_1pct":237394518.47315037,"gross_gex_1pct":356631026.81460047,"call_oi":2000,"put_oi":437},{"strike":39150.0,"call_gex_1pct":13060544.45420295,"put_gex_1pct":-3351063.3265821105,"net_gex_1pct":9709481.127620839,"gross_gex_1pct":16411607.780785061,"call_oi":85,"put_oi":24},{"strike":39200.0,"call_gex_1pct":84309734.57702392,"put_gex_1pct":-7861819.914745578,"net_gex_1pct":76447914.66227834,"gross_gex_1pct":92171554.49176951,"call_oi":536,"put_oi":55},{"strike":39250.0,"call_gex_1pct":0.0,"put_gex_1pct":-3835314.7180213155,"net_gex_1pct":-3835314.7180213155,"gross_gex_1pct":3835314.7180213155,"call_oi":0,"put_oi":27},{"strike":39300.0,"call_gex_1pct":23390801.86839408,"put_gex_1pct":-9567772.457388643,"net_gex_1pct":13823029.411005437,"gross_gex_1pct":32958574.325782724,"call_oi":149,"put_oi":67},{"strike":39350.0,"call_gex_1pct":649982.367838289,"put_gex_1pct":-1904080.1492154473,"net_gex_1pct":-1254097.7813771581,"gross_gex_1pct":2554062.5170537364,"call_oi":4,"put_oi":13},{"strike":39400.0,"call_gex_1pct":38394185.906116776,"put_gex_1pct":-6455162.447430149,"net_gex_1pct":31939023.458686627,"gross_gex_1pct":44849348.353546925,"call_oi":231,"put_oi":43},{"strike":39450.0,"call_gex_1pct":1635499.7204791468,"put_gex_1pct":-3804622.775492154,"net_gex_1pct":-2169123.0550130075,"gross_gex_1pct":5440122.495971301,"call_oi":10,"put_oi":26},{"strike":39500.0,"call_gex_1pct":322392953.36666983,"put_gex_1pct":-43119208.213320754,"net_gex_1pct":279273745.1533491,"gross_gex_1pct":365512161.57999057,"call_oi":2004,"put_oi":290},{"strike":39550.0,"call_gex_1pct":1664899.2002766589,"put_gex_1pct":-4171121.517077531,"net_gex_1pct":-2506222.3168008723,"gross_gex_1pct":5836020.71735419,"call_oi":10,"put_oi":28},{"strike":39600.0,"call_gex_1pct":862398.5404504276,"put_gex_1pct":-5587090.086620748,"net_gex_1pct":-4724691.54617032,"gross_gex_1pct":6449488.627071176,"call_oi":5,"put_oi":37},{"strike":39650.0,"call_gex_1pct":3556721.0858878535,"put_gex_1pct":-1345226.5907518105,"net_gex_1pct":2211494.495136043,"gross_gex_1pct":4901947.676639664,"call_oi":21,"put_oi":9},{"strike":39700.0,"call_gex_1pct":107902810.53543594,"put_gex_1pct":-5943233.390679122,"net_gex_1pct":101959577.14475682,"gross_gex_1pct":113846043.92611507,"call_oi":636,"put_oi":39},{"strike":39750.0,"call_gex_1pct":4994576.638996001,"put_gex_1pct":-2331172.7489003506,"net_gex_1pct":2663403.8900956507,"gross_gex_1pct":7325749.3878963515,"call_oi":29,"put_oi":15},{"strike":39800.0,"call_gex_1pct":8098820.695148833,"put_gex_1pct":-8350540.733605787,"net_gex_1pct":-251720.03845695406,"gross_gex_1pct":16449361.42875462,"call_oi":46,"put_oi":53},{"strike":39850.0,"call_gex_1pct":2503003.0093763834,"put_gex_1pct":-2236508.8745634807,"net_gex_1pct":266494.13481290266,"gross_gex_1pct":4739511.883939864,"call_oi":14,"put_oi":14},{"strike":39900.0,"call_gex_1pct":4701821.24894573,"put_gex_1pct":-10332715.575797305,"net_gex_1pct":-5630894.326851575,"gross_gex_1pct":15034536.824743034,"call_oi":27,"put_oi":65},{"strike":39950.0,"call_gex_1pct":7248151.992266426,"put_gex_1pct":-10123770.377527354,"net_gex_1pct":-2875618.3852609284,"gross_gex_1pct":17371922.36979378,"call_oi":41,"put_oi":64},{"strike":40000.0,"call_gex_1pct":26184753.412306733,"put_gex_1pct":-46959207.57369671,"net_gex_1pct":-20774454.161389977,"gross_gex_1pct":73143960.98600344,"call_oi":151,"put_oi":302},{"strike":40050.0,"call_gex_1pct":4997181.668602008,"put_gex_1pct":-3964610.637801916,"net_gex_1pct":1032571.0308000925,"gross_gex_1pct":8961792.306403924,"call_oi":28,"put_oi":25},{"strike":40100.0,"call_gex_1pct":114447813.05198067,"put_gex_1pct":-12782206.875185492,"net_gex_1pct":101665606.17679518,"gross_gex_1pct":127230019.92716616,"call_oi":636,"put_oi":81},{"strike":40150.0,"call_gex_1pct":4058514.6629158505,"put_gex_1pct":-7426103.184483459,"net_gex_1pct":-3367588.5215676087,"gross_gex_1pct":11484617.84739931,"call_oi":23,"put_oi":47},{"strike":40200.0,"call_gex_1pct":10077422.90518335,"put_gex_1pct":-14445584.674546394,"net_gex_1pct":-4368161.769363044,"gross_gex_1pct":24523007.579729743,"call_oi":59,"put_oi":93},{"strike":40250.0,"call_gex_1pct":4894378.591050504,"put_gex_1pct":-2596757.2775793686,"net_gex_1pct":2297621.313471135,"gross_gex_1pct":7491135.868629873,"call_oi":29,"put_oi":17},{"strike":40300.0,"call_gex_1pct":121637495.75177823,"put_gex_1pct":-13594497.872054566,"net_gex_1pct":108042997.87972367,"gross_gex_1pct":135231993.6238328,"call_oi":734,"put_oi":91},{"strike":40350.0,"call_gex_1pct":2621041.739249486,"put_gex_1pct":-3400757.8272922286,"net_gex_1pct":-779716.0880427426,"gross_gex_1pct":6021799.566541715,"call_oi":16,"put_oi":23},{"strike":40400.0,"call_gex_1pct":5633197.922791539,"put_gex_1pct":-3638418.1554482086,"net_gex_1pct":1994779.7673433302,"gross_gex_1pct":9271616.078239746,"call_oi":35,"put_oi":25},{"strike":40450.0,"call_gex_1pct":6240180.752360697,"put_gex_1pct":-2832470.4009602997,"net_gex_1pct":3407710.3514003973,"gross_gex_1pct":9072651.153320996,"call_oi":38,"put_oi":19},{"strike":40500.0,"call_gex_1pct":37450563.8642266,"put_gex_1pct":-9778051.733404553,"net_gex_1pct":27672512.130822048,"gross_gex_1pct":47228615.59763116,"call_oi":222,"put_oi":64},{"strike":40550.0,"call_gex_1pct":5537283.63828667,"put_gex_1pct":-2889223.6975549194,"net_gex_1pct":2648059.9407317503,"gross_gex_1pct":8426507.335841589,"call_oi":33,"put_oi":19},{"strike":40600.0,"call_gex_1pct":9452595.908092713,"put_gex_1pct":-4437017.009546132,"net_gex_1pct":5015578.898546581,"gross_gex_1pct":13889612.917638846,"call_oi":57,"put_oi":30},{"strike":40650.0,"call_gex_1pct":41568492.03621792,"put_gex_1pct":-4876975.965947618,"net_gex_1pct":36691516.0702703,"gross_gex_1pct":46445468.00216554,"call_oi":252,"put_oi":32},{"strike":40700.0,"call_gex_1pct":9593609.638409773,"put_gex_1pct":-7059265.214768431,"net_gex_1pct":2534344.4236413417,"gross_gex_1pct":16652874.853178203,"call_oi":57,"put_oi":46},{"strike":40750.0,"call_gex_1pct":5155374.064880184,"put_gex_1pct":-3471703.0676489957,"net_gex_1pct":1683670.9972311882,"gross_gex_1pct":8627077.13252918,"call_oi":31,"put_oi":23},{"strike":40800.0,"call_gex_1pct":19226662.92197426,"put_gex_1pct":-6088636.954687488,"net_gex_1pct":13138025.967286773,"gross_gex_1pct":25315299.876661748,"call_oi":117,"put_oi":41},{"strike":40850.0,"call_gex_1pct":11111060.632983666,"put_gex_1pct":-3546815.3521184637,"net_gex_1pct":7564245.280865202,"gross_gex_1pct":14657875.98510213,"call_oi":68,"put_oi":24},{"strike":40900.0,"call_gex_1pct":38713028.97615941,"put_gex_1pct":-3054042.73045034,"net_gex_1pct":35658986.24570907,"gross_gex_1pct":41767071.70660975,"call_oi":243,"put_oi":21},{"strike":40950.0,"call_gex_1pct":6660518.359768812,"put_gex_1pct":-4196733.483993263,"net_gex_1pct":2463784.8757755486,"gross_gex_1pct":10857251.843762074,"call_oi":42,"put_oi":29},{"strike":41000.0,"call_gex_1pct":127666359.37332527,"put_gex_1pct":-8442984.767375141,"net_gex_1pct":119223374.60595013,"gross_gex_1pct":136109344.1407004,"call_oi":807,"put_oi":58},{"strike":41050.0,"call_gex_1pct":4054277.8410361684,"put_gex_1pct":-4534937.344130373,"net_gex_1pct":-480659.50309420424,"gross_gex_1pct":8589215.185166541,"call_oi":26,"put_oi":32},{"strike":41100.0,"call_gex_1pct":57400571.320441306,"put_gex_1pct":-3906159.8641879936,"net_gex_1pct":53494411.45625331,"gross_gex_1pct":61306731.1846293,"call_oi":376,"put_oi":28},{"strike":41150.0,"call_gex_1pct":7031544.228879599,"put_gex_1pct":-7571670.192053902,"net_gex_1pct":-540125.9631743031,"gross_gex_1pct":14603214.4209335,"call_oi":46,"put_oi":54},{"strike":41200.0,"call_gex_1pct":11336478.42499912,"put_gex_1pct":-3551956.6526822993,"net_gex_1pct":7784521.772316821,"gross_gex_1pct":14888435.077681419,"call_oi":76,"put_oi":26},{"strike":41250.0,"call_gex_1pct":4709454.802273805,"put_gex_1pct":-1358500.883274917,"net_gex_1pct":3350953.918998888,"gross_gex_1pct":6067955.685548723,"call_oi":32,"put_oi":10},{"strike":41300.0,"call_gex_1pct":18450004.200730983,"put_gex_1pct":-2781419.5041084075,"net_gex_1pct":15668584.696622577,"gross_gex_1pct":21231423.70483939,"call_oi":128,"put_oi":21},{"strike":41350.0,"call_gex_1pct":4483349.000311891,"put_gex_1pct":-1462296.725010945,"net_gex_1pct":3021052.2753009456,"gross_gex_1pct":5945645.725322835,"call_oi":31,"put_oi":11},{"strike":41400.0,"call_gex_1pct":10699098.291472232,"put_gex_1pct":-4148770.6000747546,"net_gex_1pct":6550327.691397477,"gross_gex_1pct":14847868.891546987,"call_oi":76,"put_oi":32},{"strike":41450.0,"call_gex_1pct":7104212.757721593,"put_gex_1pct":-1531944.4014616415,"net_gex_1pct":5572268.356259951,"gross_gex_1pct":8636157.159183234,"call_oi":51,"put_oi":12},{"strike":41500.0,"call_gex_1pct":25301919.65720047,"put_gex_1pct":-4350187.084026406,"net_gex_1pct":20951732.573174067,"gross_gex_1pct":29652106.741226874,"call_oi":185,"put_oi":34},{"strike":41550.0,"call_gex_1pct":8155737.907194992,"put_gex_1pct":-2122487.7156476215,"net_gex_1pct":6033250.19154737,"gross_gex_1pct":10278225.622842614,"call_oi":61,"put_oi":17},{"strike":41600.0,"call_gex_1pct":12784444.885498479,"put_gex_1pct":-2335339.4995514336,"net_gex_1pct":10449105.385947045,"gross_gex_1pct":15119784.385049913,"call_oi":97,"put_oi":19},{"strike":41650.0,"call_gex_1pct":7108897.852613709,"put_gex_1pct":-1814994.7747644451,"net_gex_1pct":5293903.077849263,"gross_gex_1pct":8923892.627378155,"call_oi":55,"put_oi":15},{"strike":41700.0,"call_gex_1pct":12267585.532344138,"put_gex_1pct":-2501320.352830046,"net_gex_1pct":9766265.179514091,"gross_gex_1pct":14768905.885174185,"call_oi":97,"put_oi":21},{"strike":41750.0,"call_gex_1pct":6204640.447713812,"put_gex_1pct":-1055180.5004980955,"net_gex_1pct":5149459.947215716,"gross_gex_1pct":7259820.948211907,"call_oi":50,"put_oi":9},{"strike":41800.0,"call_gex_1pct":18158753.91527411,"put_gex_1pct":-1961666.5285953626,"net_gex_1pct":16197087.386678748,"gross_gex_1pct":20120420.44386947,"call_oi":149,"put_oi":17},{"strike":41850.0,"call_gex_1pct":7173036.428608822,"put_gex_1pct":-3406716.6529298536,"net_gex_1pct":3766319.775678968,"gross_gex_1pct":10579753.081538675,"call_oi":60,"put_oi":30},{"strike":41900.0,"call_gex_1pct":10162858.192467561,"put_gex_1pct":-222038.9295489206,"net_gex_1pct":9940819.26291864,"gross_gex_1pct":10384897.122016482,"call_oi":87,"put_oi":2},{"strike":41950.0,"call_gex_1pct":8244634.341347918,"put_gex_1pct":-549605.8570514447,"net_gex_1pct":7695028.484296473,"gross_gex_1pct":8794240.198399363,"call_oi":72,"put_oi":5},{"strike":42000.0,"call_gex_1pct":85920036.57291809,"put_gex_1pct":-3870158.6191088147,"net_gex_1pct":82049877.95380928,"gross_gex_1pct":89790195.1920269,"call_oi":766,"put_oi":36},{"strike":42050.0,"call_gex_1pct":7122859.608679989,"put_gex_1pct":-1163305.7657911975,"net_gex_1pct":5959553.842888792,"gross_gex_1pct":8286165.374471187,"call_oi":65,"put_oi":11},{"strike":42100.0,"call_gex_1pct":8572902.896716677,"put_gex_1pct":-1872127.8576491077,"net_gex_1pct":6700775.039067569,"gross_gex_1pct":10445030.754365785,"call_oi":80,"put_oi":18},{"strike":42150.0,"call_gex_1pct":6698543.605289916,"put_gex_1pct":-1323359.0484906652,"net_gex_1pct":5375184.556799251,"gross_gex_1pct":8021902.6537805805,"call_oi":64,"put_oi":13},{"strike":42200.0,"call_gex_1pct":8594983.685791416,"put_gex_1pct":-900889.7477096737,"net_gex_1pct":7694093.938081742,"gross_gex_1pct":9495873.433501089,"call_oi":84,"put_oi":9},{"strike":42250.0,"call_gex_1pct":8494990.144266091,"put_gex_1pct":-1377520.5484371218,"net_gex_1pct":7117469.595828969,"gross_gex_1pct":9872510.692703214,"call_oi":85,"put_oi":14},{"strike":42300.0,"call_gex_1pct":8877865.711699896,"put_gex_1pct":-1933592.7091293426,"net_gex_1pct":6944273.002570553,"gross_gex_1pct":10811458.420829238,"call_oi":91,"put_oi":20},{"strike":42350.0,"call_gex_1pct":9426007.070086941,"put_gex_1pct":-2272810.237006048,"net_gex_1pct":7153196.833080893,"gross_gex_1pct":11698817.307092989,"call_oi":99,"put_oi":24},{"strike":42400.0,"call_gex_1pct":4638732.0362692,"put_gex_1pct":-1855913.581848634,"net_gex_1pct":2782818.454420566,"gross_gex_1pct":6494645.6181178335,"call_oi":50,"put_oi":20},{"strike":42450.0,"call_gex_1pct":4986174.933951402,"put_gex_1pct":-1367355.5232638326,"net_gex_1pct":3618819.4106875695,"gross_gex_1pct":6353530.457215235,"call_oi":55,"put_oi":15},{"strike":42500.0,"call_gex_1pct":22358818.836447153,"put_gex_1pct":-2058469.5476511414,"net_gex_1pct":20300349.28879601,"gross_gex_1pct":24417288.384098295,"call_oi":253,"put_oi":23},{"strike":42550.0,"call_gex_1pct":6447697.31127366,"put_gex_1pct":-2019770.6985417444,"net_gex_1pct":4427926.612731915,"gross_gex_1pct":8467468.009815404,"call_oi":75,"put_oi":23},{"strike":42600.0,"call_gex_1pct":88272785.22115114,"put_gex_1pct":-17393286.666501217,"net_gex_1pct":70879498.55464992,"gross_gex_1pct":105666071.88765237,"call_oi":1055,"put_oi":202},{"strike":42650.0,"call_gex_1pct":3762387.0847885944,"put_gex_1pct":-1604653.830886081,"net_gex_1pct":2157733.2539025135,"gross_gex_1pct":5367040.915674675,"call_oi":46,"put_oi":19},{"strike":42700.0,"call_gex_1pct":7166643.761587588,"put_gex_1pct":-3561368.6505829673,"net_gex_1pct":3605275.111004621,"gross_gex_1pct":10728012.412170555,"call_oi":90,"put_oi":43},{"strike":42750.0,"call_gex_1pct":3573073.140190137,"put_gex_1pct":-2438013.278173234,"net_gex_1pct":1135059.8620169032,"gross_gex_1pct":6011086.418363371,"call_oi":46,"put_oi":30},{"strike":42800.0,"call_gex_1pct":157284237.35947537,"put_gex_1pct":-24230620.35697925,"net_gex_1pct":133053617.00249612,"gross_gex_1pct":181514857.71645463,"call_oi":2119,"put_oi":305},{"strike":42850.0,"call_gex_1pct":5284954.665540047,"put_gex_1pct":-3352386.441455122,"net_gex_1pct":1932568.224084925,"gross_gex_1pct":8637341.10699517,"call_oi":73,"put_oi":43},{"strike":42900.0,"call_gex_1pct":9287770.063810678,"put_gex_1pct":-2372442.3519955985,"net_gex_1pct":6915327.71181508,"gross_gex_1pct":11660212.415806277,"call_oi":131,"put_oi":31},{"strike":42950.0,"call_gex_1pct":6185453.786261265,"put_gex_1pct":-4283321.848215581,"net_gex_1pct":1902131.9380456842,"gross_gex_1pct":10468775.634476846,"call_oi":90,"put_oi":57},{"strike":43000.0,"call_gex_1pct":145588654.62722617,"put_gex_1pct":-16315562.717492342,"net_gex_1pct":129273091.90973383,"gross_gex_1pct":161904217.34471852,"call_oi":2188,"put_oi":222},{"strike":43050.0,"call_gex_1pct":7284028.391218524,"put_gex_1pct":-4547779.440994688,"net_gex_1pct":2736248.950223836,"gross_gex_1pct":11831807.832213212,"call_oi":112,"put_oi":63},{"strike":43100.0,"call_gex_1pct":14081221.57259082,"put_gex_1pct":-4255345.969974777,"net_gex_1pct":9825875.602616044,"gross_gex_1pct":18336567.5425656,"call_oi":224,"put_oi":60},{"strike":43150.0,"call_gex_1pct":10779956.796961425,"put_gex_1pct":-4225979.125188394,"net_gex_1pct":6553977.67177303,"gross_gex_1pct":15005935.922149818,"call_oi":176,"put_oi":61},{"strike":43200.0,"call_gex_1pct":92214186.65130508,"put_gex_1pct":-11438149.475255521,"net_gex_1pct":80776037.17604956,"gross_gex_1pct":103652336.1265606,"call_oi":1567,"put_oi":168},{"strike":43250.0,"call_gex_1pct":12899152.319536727,"put_gex_1pct":-6773501.994050685,"net_gex_1pct":6125650.325486042,"gross_gex_1pct":19672654.313587412,"call_oi":227,"put_oi":102},{"strike":43300.0,"call_gex_1pct":13206618.315194692,"put_gex_1pct":-7441877.747796796,"net_gex_1pct":5764740.567397896,"gross_gex_1pct":20648496.06299149,"call_oi":240,"put_oi":114},{"strike":43350.0,"call_gex_1pct":2139577.36531964,"put_gex_1pct":-962802.3392984738,"net_gex_1pct":1176775.0260211662,"gross_gex_1pct":3102379.7046181136,"call_oi":40,"put_oi":15},{"strike":43400.0,"call_gex_1pct":2623994.9004104766,"put_gex_1pct":-1187410.407478247,"net_gex_1pct":1436584.4929322295,"gross_gex_1pct":3811405.307888724,"call_oi":51,"put_oi":19},{"strike":43450.0,"call_gex_1pct":4022772.8194983243,"put_gex_1pct":-1167811.500396296,"net_gex_1pct":2854961.3191020284,"gross_gex_1pct":5190584.31989462,"call_oi":81,"put_oi":19},{"strike":43500.0,"call_gex_1pct":14128443.62536986,"put_gex_1pct":-1148793.6160055157,"net_gex_1pct":12979650.009364344,"gross_gex_1pct":15277237.241375376,"call_oi":297,"put_oi":19},{"strike":43550.0,"call_gex_1pct":2795668.8948143735,"put_gex_1pct":-646184.891525874,"net_gex_1pct":2149484.0032884995,"gross_gex_1pct":3441853.7863402474,"call_oi":62,"put_oi":11},{"strike":43600.0,"call_gex_1pct":19154681.429497663,"put_gex_1pct":-1138563.520726602,"net_gex_1pct":18016117.90877106,"gross_gex_1pct":20293244.950224265,"call_oi":455,"put_oi":20},{"strike":43650.0,"call_gex_1pct":1613239.3238990402,"put_gex_1pct":-1008220.0736440036,"net_gex_1pct":605019.2502550366,"gross_gex_1pct":2621459.397543044,"call_oi":40,"put_oi":18},{"strike":43700.0,"call_gex_1pct":2442005.02516605,"put_gex_1pct":-1819045.8304304278,"net_gex_1pct":622959.1947356223,"gross_gex_1pct":4261050.855596478,"call_oi":62,"put_oi":33},{"strike":43750.0,"call_gex_1pct":3364493.840310492,"put_gex_1pct":-1193680.9207990936,"net_gex_1pct":2170812.9195113983,"gross_gex_1pct":4558174.761109586,"call_oi":87,"put_oi":22},{"strike":43800.0,"call_gex_1pct":9256025.887403116,"put_gex_1pct":-1549124.1820173042,"net_gex_1pct":7706901.705385812,"gross_gex_1pct":10805150.06942042,"call_oi":245,"put_oi":29},{"strike":43850.0,"call_gex_1pct":4244766.440030961,"put_gex_1pct":-1209827.3584795082,"net_gex_1pct":3034939.081551453,"gross_gex_1pct":5454593.7985104695,"call_oi":115,"put_oi":23},{"strike":43900.0,"call_gex_1pct":2851872.532599482,"put_gex_1pct":-1295166.252787668,"net_gex_1pct":1556706.2798118142,"gross_gex_1pct":4147038.78538715,"call_oi":83,"put_oi":25},{"strike":43950.0,"call_gex_1pct":2135096.4740188913,"put_gex_1pct":-1551283.0502863475,"net_gex_1pct":583813.4237325438,"gross_gex_1pct":3686379.524305239,"call_oi":67,"put_oi":31},{"strike":44000.0,"call_gex_1pct":15795735.770139618,"put_gex_1pct":-1577381.8519621235,"net_gex_1pct":14218353.918177495,"gross_gex_1pct":17373117.622101743,"call_oi":536,"put_oi":32},{"strike":44050.0,"call_gex_1pct":795073.0117898353,"put_gex_1pct":-1214123.4472009845,"net_gex_1pct":-419050.43541114917,"gross_gex_1pct":2009196.4589908198,"call_oi":28,"put_oi":25},{"strike":44100.0,"call_gex_1pct":1270782.2964094006,"put_gex_1pct":-1483532.8140691032,"net_gex_1pct":-212750.51765970257,"gross_gex_1pct":2754315.1104785036,"call_oi":47,"put_oi":31},{"strike":44150.0,"call_gex_1pct":667406.8343353722,"put_gex_1pct":-1697952.2902838266,"net_gex_1pct":-1030545.4559484544,"gross_gex_1pct":2365359.124619199,"call_oi":26,"put_oi":36},{"strike":44200.0,"call_gex_1pct":1669908.762183249,"put_gex_1pct":-1270463.8604455295,"net_gex_1pct":399444.90173771954,"gross_gex_1pct":2940372.622628778,"call_oi":74,"put_oi":28},{"strike":44250.0,"call_gex_1pct":343129.9349117999,"put_gex_1pct":-1073390.191661565,"net_gex_1pct":-730260.2567497652,"gross_gex_1pct":1416520.126573365,"call_oi":16,"put_oi":24},{"strike":44300.0,"call_gex_1pct":1076706.2484159097,"put_gex_1pct":-661380.1625567473,"net_gex_1pct":415326.0858591624,"gross_gex_1pct":1738086.4109726571,"call_oi":52,"put_oi":15},{"strike":44350.0,"call_gex_1pct":1282515.7653738272,"put_gex_1pct":-739081.2920123145,"net_gex_1pct":543434.4733615126,"gross_gex_1pct":2021597.0573861417,"call_oi":63,"put_oi":17},{"strike":44400.0,"call_gex_1pct":452820.8520540874,"put_gex_1pct":-257244.59586389657,"net_gex_1pct":195576.25619019082,"gross_gex_1pct":710065.447917984,"call_oi":24,"put_oi":6},{"strike":44450.0,"call_gex_1pct":417589.9710668062,"put_gex_1pct":-465164.20342418406,"net_gex_1pct":-47574.232357377885,"gross_gex_1pct":882754.1744909902,"call_oi":23,"put_oi":11},{"strike":44500.0,"call_gex_1pct":1976299.0237546782,"put_gex_1pct":-417155.18011950544,"net_gex_1pct":1559143.8436351728,"gross_gex_1pct":2393454.203874184,"call_oi":119,"put_oi":10},{"strike":44550.0,"call_gex_1pct":205533.8075392261,"put_gex_1pct":-452729.1280597028,"net_gex_1pct":-247195.3205204767,"gross_gex_1pct":658262.935598929,"call_oi":13,"put_oi":11},{"strike":44600.0,"call_gex_1pct":953907.045764827,"put_gex_1pct":-406122.0801983569,"net_gex_1pct":547784.9655664702,"gross_gex_1pct":1360029.125963184,"call_oi":66,"put_oi":10},{"strike":44650.0,"call_gex_1pct":255409.90519500707,"put_gex_1pct":-272021.34316525975,"net_gex_1pct":-16611.43797025268,"gross_gex_1pct":527431.2483602668,"call_oi":19,"put_oi":7},{"strike":44700.0,"call_gex_1pct":3216655.4291183557,"put_gex_1pct":-421838.03648175276,"net_gex_1pct":2794817.3926366027,"gross_gex_1pct":3638493.4656001087,"call_oi":257,"put_oi":11},{"strike":44750.0,"call_gex_1pct":257010.99056847894,"put_gex_1pct":-378496.06524922163,"net_gex_1pct":-121485.07468074269,"gross_gex_1pct":635507.0558177006,"call_oi":22,"put_oi":10},{"strike":44800.0,"call_gex_1pct":541852.8333494108,"put_gex_1pct":-186809.38448102667,"net_gex_1pct":355043.4488683841,"gross_gex_1pct":728662.2178304375,"call_oi":50,"put_oi":5},{"strike":44850.0,"call_gex_1pct":200529.94453658117,"put_gex_1pct":0.0,"net_gex_1pct":200529.94453658117,"gross_gex_1pct":200529.94453658117,"call_oi":19,"put_oi":0},{"strike":44900.0,"call_gex_1pct":322077.5548891915,"put_gex_1pct":0.0,"net_gex_1pct":322077.5548891915,"gross_gex_1pct":322077.5548891915,"call_oi":31,"put_oi":0},{"strike":44950.0,"call_gex_1pct":220505.60605964228,"put_gex_1pct":-251750.95388848995,"net_gex_1pct":-31245.347828847676,"gross_gex_1pct":472256.55994813226,"call_oi":30,"put_oi":7},{"strike":45000.0,"call_gex_1pct":35170789.83737897,"put_gex_1pct":0.0,"net_gex_1pct":35170789.83737897,"gross_gex_1pct":35170789.83737897,"call_oi":5419,"put_oi":0},{"strike":45050.0,"call_gex_1pct":74790.74305206322,"put_gex_1pct":0.0,"net_gex_1pct":74790.74305206322,"gross_gex_1pct":74790.74305206322,"call_oi":13,"put_oi":0},{"strike":45100.0,"call_gex_1pct":147265.78025106335,"put_gex_1pct":0.0,"net_gex_1pct":147265.78025106335,"gross_gex_1pct":147265.78025106335,"call_oi":26,"put_oi":0},{"strike":45150.0,"call_gex_1pct":27075.296956845254,"put_gex_1pct":-34241.88669552342,"net_gex_1pct":-7166.589738678165,"gross_gex_1pct":61317.18365236867,"call_oi":5,"put_oi":1},{"strike":45200.0,"call_gex_1pct":506618.0629932046,"put_gex_1pct":-33834.33007807399,"net_gex_1pct":472783.7329151306,"gross_gex_1pct":540452.3930712786,"call_oi":95,"put_oi":1},{"strike":45250.0,"call_gex_1pct":35641.65001170466,"put_gex_1pct":0.0,"net_gex_1pct":35641.65001170466,"gross_gex_1pct":35641.65001170466,"call_oi":7,"put_oi":0},{"strike":45300.0,"call_gex_1pct":160504.8349520076,"put_gex_1pct":-297404.67272557004,"net_gex_1pct":-136899.83777356244,"gross_gex_1pct":457909.50767757767,"call_oi":32,"put_oi":9},{"strike":45350.0,"call_gex_1pct":14825.301104012293,"put_gex_1pct":0.0,"net_gex_1pct":14825.301104012293,"gross_gex_1pct":14825.301104012293,"call_oi":3,"put_oi":0},{"strike":45400.0,"call_gex_1pct":82782.74274049727,"put_gex_1pct":-64576.46727969915,"net_gex_1pct":18206.27546079812,"gross_gex_1pct":147359.21002019642,"call_oi":17,"put_oi":2},{"strike":45450.0,"call_gex_1pct":9287.100188807157,"put_gex_1pct":0.0,"net_gex_1pct":9287.100188807157,"gross_gex_1pct":9287.100188807157,"call_oi":2,"put_oi":0},{"strike":45500.0,"call_gex_1pct":398192.3405254996,"put_gex_1pct":0.0,"net_gex_1pct":398192.3405254996,"gross_gex_1pct":398192.3405254996,"call_oi":87,"put_oi":0},{"strike":45550.0,"call_gex_1pct":13535.661542957674,"put_gex_1pct":0.0,"net_gex_1pct":13535.661542957674,"gross_gex_1pct":13535.661542957674,"call_oi":3,"put_oi":0},{"strike":45600.0,"call_gex_1pct":120106.503902656,"put_gex_1pct":0.0,"net_gex_1pct":120106.503902656,"gross_gex_1pct":120106.503902656,"call_oi":27,"put_oi":0},{"strike":45700.0,"call_gex_1pct":83540.3084665247,"put_gex_1pct":0.0,"net_gex_1pct":83540.3084665247,"gross_gex_1pct":83540.3084665247,"call_oi":20,"put_oi":0},{"strike":45800.0,"call_gex_1pct":130043.07654519193,"put_gex_1pct":0.0,"net_gex_1pct":130043.07654519193,"gross_gex_1pct":130043.07654519193,"call_oi":32,"put_oi":0},{"strike":45900.0,"call_gex_1pct":55380.397156334984,"put_gex_1pct":0.0,"net_gex_1pct":55380.397156334984,"gross_gex_1pct":55380.397156334984,"call_oi":14,"put_oi":0},{"strike":46000.0,"call_gex_1pct":1028041.9996740669,"put_gex_1pct":-28336.203136462882,"net_gex_1pct":999705.7965376041,"gross_gex_1pct":1056378.2028105299,"call_oi":277,"put_oi":1},{"strike":46100.0,"call_gex_1pct":32543.278643679674,"put_gex_1pct":0.0,"net_gex_1pct":32543.278643679674,"gross_gex_1pct":32543.278643679674,"call_oi":9,"put_oi":0},{"strike":46200.0,"call_gex_1pct":17622.80346147531,"put_gex_1pct":0.0,"net_gex_1pct":17622.80346147531,"gross_gex_1pct":17622.80346147531,"call_oi":5,"put_oi":0},{"strike":46300.0,"call_gex_1pct":9908.042734981407,"put_gex_1pct":0.0,"net_gex_1pct":9908.042734981407,"gross_gex_1pct":9908.042734981407,"call_oi":3,"put_oi":0},{"strike":46400.0,"call_gex_1pct":32218.920548947775,"put_gex_1pct":0.0,"net_gex_1pct":32218.920548947775,"gross_gex_1pct":32218.920548947775,"call_oi":10,"put_oi":0},{"strike":46500.0,"call_gex_1pct":2462053.254275621,"put_gex_1pct":0.0,"net_gex_1pct":2462053.254275621,"gross_gex_1pct":2462053.254275621,"call_oi":783,"put_oi":0},{"strike":46600.0,"call_gex_1pct":12279.906662709986,"put_gex_1pct":-25181.98815699799,"net_gex_1pct":-12902.081494288006,"gross_gex_1pct":37461.89481970797,"call_oi":4,"put_oi":1},{"strike":46700.0,"call_gex_1pct":50974.470383178494,"put_gex_1pct":-24717.81212444668,"net_gex_1pct":26256.658258731815,"gross_gex_1pct":75692.28250762518,"call_oi":17,"put_oi":1},{"strike":46800.0,"call_gex_1pct":117191.66548510492,"put_gex_1pct":0.0,"net_gex_1pct":117191.66548510492,"gross_gex_1pct":117191.66548510492,"call_oi":40,"put_oi":0},{"strike":46900.0,"call_gex_1pct":31500.80599419332,"put_gex_1pct":0.0,"net_gex_1pct":31500.80599419332,"gross_gex_1pct":31500.80599419332,"call_oi":11,"put_oi":0},{"strike":47000.0,"call_gex_1pct":226809.30926256062,"put_gex_1pct":0.0,"net_gex_1pct":226809.30926256062,"gross_gex_1pct":226809.30926256062,"call_oi":81,"put_oi":0},{"strike":47100.0,"call_gex_1pct":15031.756249244703,"put_gex_1pct":0.0,"net_gex_1pct":15031.756249244703,"gross_gex_1pct":15031.756249244703,"call_oi":6,"put_oi":0},{"strike":47200.0,"call_gex_1pct":41973.06395581831,"put_gex_1pct":0.0,"net_gex_1pct":41973.06395581831,"gross_gex_1pct":41973.06395581831,"call_oi":19,"put_oi":0},{"strike":47300.0,"call_gex_1pct":18338.874664272214,"put_gex_1pct":0.0,"net_gex_1pct":18338.874664272214,"gross_gex_1pct":18338.874664272214,"call_oi":9,"put_oi":0},{"strike":47400.0,"call_gex_1pct":67272.3621151645,"put_gex_1pct":0.0,"net_gex_1pct":67272.3621151645,"gross_gex_1pct":67272.3621151645,"call_oi":36,"put_oi":0},{"strike":47500.0,"call_gex_1pct":18573.258013166094,"put_gex_1pct":0.0,"net_gex_1pct":18573.258013166094,"gross_gex_1pct":18573.258013166094,"call_oi":13,"put_oi":0},{"strike":47600.0,"call_gex_1pct":6995.318876727961,"put_gex_1pct":0.0,"net_gex_1pct":6995.318876727961,"gross_gex_1pct":6995.318876727961,"call_oi":5,"put_oi":0},{"strike":47700.0,"call_gex_1pct":22131.305116548116,"put_gex_1pct":0.0,"net_gex_1pct":22131.305116548116,"gross_gex_1pct":22131.305116548116,"call_oi":18,"put_oi":0},{"strike":47800.0,"call_gex_1pct":12046.27567238954,"put_gex_1pct":0.0,"net_gex_1pct":12046.27567238954,"gross_gex_1pct":12046.27567238954,"call_oi":10,"put_oi":0},{"strike":47900.0,"call_gex_1pct":16593.59955345857,"put_gex_1pct":0.0,"net_gex_1pct":16593.59955345857,"gross_gex_1pct":16593.59955345857,"call_oi":16,"put_oi":0},{"strike":48000.0,"call_gex_1pct":12125.687806717566,"put_gex_1pct":-39716.19528851938,"net_gex_1pct":-27590.50748180182,"gross_gex_1pct":51841.883095236946,"call_oi":14,"put_oi":2},{"strike":48200.0,"call_gex_1pct":8783.135385904008,"put_gex_1pct":0.0,"net_gex_1pct":8783.135385904008,"gross_gex_1pct":8783.135385904008,"call_oi":13,"put_oi":0},{"strike":48300.0,"call_gex_1pct":6626.649952859167,"put_gex_1pct":-37957.24597756657,"net_gex_1pct":-31330.596024707404,"gross_gex_1pct":44583.89593042574,"call_oi":10,"put_oi":2},{"strike":48400.0,"call_gex_1pct":1446.1230284319174,"put_gex_1pct":0.0,"net_gex_1pct":1446.1230284319174,"gross_gex_1pct":1446.1230284319174,"call_oi":3,"put_oi":0},{"strike":48500.0,"call_gex_1pct":2364.832366010814,"put_gex_1pct":0.0,"net_gex_1pct":2364.832366010814,"gross_gex_1pct":2364.832366010814,"call_oi":5,"put_oi":0},{"strike":48600.0,"call_gex_1pct":464.1765372433738,"put_gex_1pct":0.0,"net_gex_1pct":464.1765372433738,"gross_gex_1pct":464.1765372433738,"call_oi":1,"put_oi":0},{"strike":48700.0,"call_gex_1pct":146266.53630191574,"put_gex_1pct":0.0,"net_gex_1pct":146266.53630191574,"gross_gex_1pct":146266.53630191574,"call_oi":321,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,500 | TAIFEX Proxy |
| 對應到期月份 | 202611 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-17→2026-11-18) | -1,100 | TAIFEX Proxy snapshots (2026-11-17) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 294,298 | 287,814 | +6,484 | 41,540 | 41,256 | +284 | +6,200 | TAIFEX Proxy |
| 投信 | 374 | 17,556 | -17,182 | 0 | 0 | +0 | -17,182 | TAIFEX Proxy |
| 自營商 | 214,175 | 209,017 | +5,158 | 27,971 | 28,426 | -455 | +5,613 | TAIFEX Proxy |
| 三大法人合計 | 508,847 | 514,387 | -5,540 | 69,511 | 69,682 | -171 | -5,369 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 31.21 | 25.05 | +6.16 | 5.97 | 5.92 | +0.04 | +6.12 | TAIFEX Proxy |
| 投信 | 0.13 | 13.02 | -12.89 | 0.00 | 0.00 | +0 | -12.89 | TAIFEX Proxy |
| 自營商 | 27.68 | 22.09 | +5.59 | 5.07 | 5.03 | +0.05 | +5.54 | TAIFEX Proxy |
| 三大法人合計 | 59.01 | 60.16 | -1.14 | 11.04 | 10.95 | +0.09 | -1.23 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,882 | TAIFEX Proxy |
| 買權空方 OI | 14,309 | TAIFEX Proxy |
| 買權多空淨 OI | -2,427 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | unavailable | 換月基準重建 |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,359 | TAIFEX Proxy |
| 賣權空方 OI | 10,230 | TAIFEX Proxy |
| 賣權多空淨 OI | +129 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | unavailable | 換月基準重建 |
- 資料日期：買權 2026-11-18／賣權 2026-11-18 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | unavailable | — | 換月基準重建 |
| 買權前十大 | unavailable | — | 換月基準重建 |
| 賣權前十大 | unavailable | — | 換月基準重建 |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-18；本次報告產製時間：2026-11-19 13:58:07；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 換月註記：期貨前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減；買權前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減；賣權前十大：前一交易日快照只有舊契約月份，無新主力月份可比基準；換月建立新基準，不跨月相減
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 保護：12 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：91 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
- 未取得欄位 (3)：options.chain_oi_change, futures.top10_change, options.top10_change

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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-18；估值 1242 檔；1 檔採最近有效收盤價（價格日期 20261111 至 20261118）；Blave 同 T0 交叉驗證 156.2150%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；1 檔採最近有效收盤價（價格日期 20261111 至 20261118）。Blave 同 T0 交叉驗證 156.2150%；差異 0.024 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-19，非 T0 2026-11-18)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-18 非今日 2026-11-19，視為無新節次，不採用
- TAIFEX 註記：Gamma Flip Proxy 查詢診斷：2026-11-18: response=unavailable, response_date=None, status=None, wall=None, flip=None, error=REQUEST_TIMEOUT；2026-11-17: response=unavailable, response_date=None, status=None, wall=None, flip=None, error=TXO_CHAIN_PRIMARY_TIMEOUT；2026-11-16: response=unavailable, response_date=None, status=None, wall=None, flip=None, error=TXO_CHAIN_PRIMARY_TIMEOUT
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611F3（到期日 2026-11-20）與 Options Key Levels 主到期月份 202611 不同；GEX 數值應以實際使用到期月份為準
- TAIFEX 註記：選擇權 OI 前日變化 unavailable：reason=no_common_valid_contracts; 主力=202611; 本日/前日有效合約=616/616; 本日/前日合約識別數=616/616; 僅本日/僅前日有效合約=616/616; 本日/前日 OI 缺值或無效=0/0; 無效/重複識別=0/0
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -765.6 | -99,438 | -2,620 | -108 | +6,484 | +284 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 投信 | +166.1 | +93,573 | +2,347 | +0 | -17,182 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -42.0 | -1,457 | -2,486 | +262 | +5,158 | -455 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
