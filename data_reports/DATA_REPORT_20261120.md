# DATA_REPORT_20261120

- 報告日期：`2026-11-21`
- T0 交易日期：`2026-11-20`
- 首次資料產出時間：`2026-11-21 07:54:06`
- 本次更新開始時間：`2026-11-21 07:54:06`
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
| 加權指數 | 36,033.29 | 點 | twse-proxy |
| 開盤 | 37,646.13 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 37,646.13 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 35,738.68 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 36,033.29 | 點 | twse-proxy |
| 漲跌點數 | -2,393.60 | 點 | twse-proxy |
| 漲跌幅 | -6.23 | % | twse-proxy |
| 成交金額 | 9,353.1 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 16 | twse-proxy |
| 下跌家數 | 1,058 | twse-proxy |
| 平盤家數 | 11 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 179 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 49 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 815 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 19 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 6 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 186 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -95.1 | 億元 | twse-proxy /institutional |
| 投信 | -73.5 | 億元 | twse-proxy /institutional |
| 自營商 | -340.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -509.4 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-20；估值 1242 檔；3 檔採最近有效收盤價（價格日期 20261111 至 20261120）；Blave 同 T0 交叉驗證 140.4010%；差異 0.027 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 5,680.8 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -637.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 225,615 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -12,723 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 140.43 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-20；估值 1242 檔；3 檔採最近有效收盤價（價格日期 20261111 至 20261120）；Blave 同 T0 交叉驗證 140.4010%；差異 0.027 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 34,229,330 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,492,034.843 | 2,151,045.127 | 20,643,079.97 | 張 |
| 借券賣出增減 | +11,001.423 | -11,741.188 | -739.765 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261120`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-21T07:54:22+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261120`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-21T07:54:22+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,353.1 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 861.7 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 10,214.8 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 6,910.39 | -265.44 | -3.70 | 2026-11-20 | 2026-11-20T23:54:22+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 22,617.73 | -1,261.47 | -5.28 | 2026-11-20 | 2026-11-20T23:54:22+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 25,028.98 | -1,488.07 | -5.61 | 2026-11-20 | 2026-11-20T23:54:22+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 48,147.33 | -949.73 | -1.93 | 2026-11-20 | 2026-11-20T23:54:22+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 8,408.59 | -1,011.13 | -10.73 | 2026-11-20 | 2026-11-20T23:54:22+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 35.89 | 7.45 | +26.20 | 2026-11-20 | 2026-11-20T23:54:22+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 59,444.21 | 419.93 | +0.71 | 2026-11-19 | 2026-11-20T23:54:23+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,137.89 | 70.45 | +1.39 | 2026-11-19 | 2026-11-20T23:54:23+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,841.62 | -453.13 | -1.95 | 2026-11-19 | 2026-11-20T23:54:23+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,577.62 | -10.22 | -0.28 | 2026-11-19 | 2026-11-20T23:54:23+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,583.20 | -76.21 | -0.71 | 2026-11-19 | 2026-11-20T23:54:23+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 6,966.75 | -230.50 | -3.20 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 25,291.00 | -1,309.25 | -4.92 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 48,391.00 | -789.00 | -1.60 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,599.90 | -63.40 | -2.38 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.63 | -0.13 | 20-NOV-26 | 2026-11-20T23:54:45+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.91 | -0.14 | 2026-11-20 | 2026-11-20T23:54:45+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.34 | -0.09 | 20-NOV-26 | 2026-11-20T23:54:45+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.30 | -0.10 | 2026-11-20 | 2026-11-20T23:54:45+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.96 | 0.03 | +0.09 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.84 | -0.06 | -0.06 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.51 | -0.87 | -0.55 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,346.13 | 15.73 | +1.18 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 318.71 | -33.38 | -9.48 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 12.04 | -1.36 | -10.15 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 26.27 | -4.22 | -13.84 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 83.62 | 0.41 | +0.49 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,539.00 | -146.50 | -3.98 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 58,755.09 | -3,146.73 | -5.08 | 2026-11-20 | 2026-11-20T23:54:23+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：單周狂瀉7641點寫新紀錄！台股再崩2393點史上第三大
  - 來源：Yahoo 台股；發布時間：2026-11-20T08:40:04Z；台北時間：2026-11-20 16:40
  - 摘要：台股今(20)日又是歷史級別的崩跌，盤中一度失守3萬6千點，終場下跌2,393.60點，收36,033.29點，寫下史上第三大收盤跌點，跌幅6.23%也是史上第四大，成交金額8,773.50億元，而櫃買指數更是重挫7.72%。

拉長到整周
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%96%AE%E5%91%A8%E7%8B%82%E7%80%897641%E9%BB%9E%E5%AF%AB%E6%96%B0%E7%B4%80%E9%8C%84%EF%BC%81%E5%8F%B0%E8%82%A1%E5%86%8D%E5%B4%A92393%E9%BB%9E%E3%80%8C%E5%8F%B2%E4%B8%8A%E7%AC%AC%E4%B8%89%E5%A4%A7%E3%80%8D%E8%81%AF%E7%99%BC%E7%A7%91%E3%80%81%E5%8F%B0%E9%81%94%E9%9B%BB%E9%BD%8A%E8%B7%8C%E5%81%9C%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-084004851.html
- 事件2：獨／閣揆卓榮泰緊急召跨部會議 研議提出第三波護盤措施
  - 來源：Yahoo 台股；發布時間：2026-11-20T14:35:23Z；台北時間：2026-11-20 22:35
  - 摘要：知情人士透露，行政院長卓榮泰今日近傍晚時，已經召集金管會、財政部等重要部會首長緊急開會，針對台股連續五個交易日大跌超過7千點，以及今日大跌2393.6點再研商是否有更多護盤台股的方式，尤其金管會昨日才宣布第二波的限空令，結果今日台股跌幅更甚
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8D%A8-%E9%96%A3%E6%8F%86%E5%8D%93%E6%A6%AE%E6%B3%B0%E7%B7%8A%E6%80%A5%E5%8F%AC%E8%B7%A8%E9%83%A8%E6%9C%83%E8%AD%B0-%E7%A0%94%E8%AD%B0%E6%8F%90%E5%87%BA%E7%AC%AC%E4%B8%89%E6%B3%A2%E8%AD%B7%E7%9B%A4%E6%8E%AA%E6%96%BD-143523325.html
- 事件3：台股慘跌逾7千點、周線收黑！卓榮泰急召跨部會議「明日續戰」　商討第三波限空令救市
  - 來源：Yahoo 台股；發布時間：2026-11-20T13:40:00Z；台北時間：2026-11-20 21:40
  - 摘要：[FTNN新聞網]記者邱梓欣／綜合報導即使金管會出手祭出「限空令」仍難敵賣壓，台股今（20）日以37,646.13開低後下殺，終場慘摔2393.60點，以36,033.29點作收，...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%85%98%E8%B7%8C%E9%80%BE7%E5%8D%83%E9%BB%9E-%E5%91%A8%E7%B7%9A%E6%94%B6%E9%BB%91-%E5%8D%93%E6%A6%AE%E6%B3%B0%E6%80%A5%E5%8F%AC%E8%B7%A8%E9%83%A8%E6%9C%83%E8%AD%B0-%E6%98%8E%E6%97%A5%E7%BA%8C%E6%88%B0-%E5%95%86%E8%A8%8E%E7%AC%AC%E4%B8%89%E6%B3%A2%E9%99%90%E7%A9%BA%E4%BB%A4%E6%95%91%E5%B8%82-134000929.html
- 事件4：台股第2波限空令失靈「慘變凌遲」 教授透露散戶3大救生圈！
  - 來源：Yahoo 台股；發布時間：2026-11-20T13:12:47Z；台北時間：2026-11-20 21:12
  - 摘要：台股將迎來恐慌潮，20日盤中再度狂瀉2688點，最低下探35738點，終場暴跌2393點，累計本週跌幅高達18％，恐寫下1990年以來最大單週跌幅紀錄。金管會升級限空措施仍未能止住賣壓，引發市場對政策效能的質疑。
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E7%AC%AC2%E6%B3%A2%E9%99%90%E7%A9%BA%E4%BB%A4%E5%A4%B1%E9%9D%88-%E6%85%98%E8%AE%8A%E5%87%8C%E9%81%B2-%E6%95%99%E6%8E%88%E9%80%8F%E9%9C%B2%E6%95%A3%E6%88%B63%E5%A4%A7%E6%95%91%E7%94%9F%E5%9C%88-131247433.html
- 事件5：美收緊中國晶片管制！台積電接單限制同步升級、輝達利空橫飛　「這檔金融」賺贏去年全年仍遭外資狠砍逾2萬張淪賣超王
  - 來源：Yahoo 台股；發布時間：2026-11-20T12:30:00Z；台北時間：2026-11-20 20:30
  - 摘要：[FTNN新聞網]記者邱梓欣／綜合報導即使金管會出手祭出「限空令」仍難敵賣壓，台股今（20）日以37,646.13開低後下殺，終場慘摔2393.60點，以36,033.29點作收，...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E6%94%B6%E7%B7%8A%E4%B8%AD%E5%9C%8B%E6%99%B6%E7%89%87%E7%AE%A1%E5%88%B6-%E5%8F%B0%E7%A9%8D%E9%9B%BB%E6%8E%A5%E5%96%AE%E9%99%90%E5%88%B6%E5%90%8C%E6%AD%A5%E5%8D%87%E7%B4%9A-%E8%BC%9D%E9%81%94%E5%88%A9%E7%A9%BA%E6%A9%AB%E9%A3%9B-%E9%80%99%E6%AA%94%E9%87%91%E8%9E%8D-%E8%B3%BA%E8%B4%8F%E5%8E%BB%E5%B9%B4%E5%85%A8%E5%B9%B4%E4%BB%8D%E9%81%AD%E5%A4%96%E8%B3%87%E7%8B%A0%E7%A0%8D%E9%80%BE2%E8%90%AC%E5%BC%B5%E6%B7%AA%E8%B3%A3%E8%B6%85%E7%8E%8B-123000645.html
- 事件6：晶圓代工跌深成買點？「這2檔」今日獲外資合計掃入逾9.8萬張　趁低加碼聯電8萬張、斥資65億元
  - 來源：Yahoo 台股；發布時間：2026-11-20T12:00:00Z；台北時間：2026-11-20 20:00
  - 摘要：[FTNN新聞網]記者王凱暄／綜合報導台股加權指數今（20）日開低走低續跌，盤中一度下殺至3萬5千點、台積電（2330）則一度跌破2000元，指數終場暴跌2393.60點，...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%99%B6%E5%9C%93%E4%BB%A3%E5%B7%A5%E8%B7%8C%E6%B7%B1%E6%88%90%E8%B2%B7%E9%BB%9E-%E9%80%992%E6%AA%94-%E4%BB%8A%E6%97%A5%E7%8D%B2%E5%A4%96%E8%B3%87%E5%90%88%E8%A8%88%E6%8E%83%E5%85%A5%E9%80%BE9-8%E8%90%AC%E5%BC%B5-%E8%B6%81%E4%BD%8E%E5%8A%A0%E7%A2%BC%E8%81%AF%E9%9B%BB8%E8%90%AC%E5%BC%B5-120000970.html
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
- 事件11：Warsh wants Fed officials to talk less. Instead, they’re talking more
  - 來源：CNBC；發布時間：Fri, 20 Nov 2026 21:10:48 GMT；台北時間：2026-11-21 05:10
  - 摘要：Fed officials have been rushing to the microphones lately while the Fed chairman stays on the sidelines.
  - 原文連結：https://www.cnbc.com/2026/11/20/warsh-fed-forward-guidance-rate-hikes.html
- 事件12：A massive bearish trade just happened in the chip stocks
  - 來源：CNBC；發布時間：Fri, 20 Nov 2026 19:33:31 GMT；台北時間：2026-11-21 03:33
  - 摘要：Options traders place big bets that semiconductor stocks have further to fall
  - 原文連結：https://www.cnbc.com/2026/11/20/a-massive-bearish-trade-just-happened-in-the-chip-stocks.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-20

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
| 開盤價 | 35,943 | 點 | TAIFEX Proxy |
| 最高價 | 36,396 | 點 | TAIFEX Proxy |
| 最低價 | 33,719 | 點 | TAIFEX Proxy |
| 收盤價 | 33,919 | 點 | TAIFEX Proxy |
| 漲跌點數 | -1,881 | 點 | TAIFEX Proxy |
| 漲跌幅 | -5.25 | % | TAIFEX Proxy |
| 成交量 | 82,477 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 36,396 / 33,719 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 16,303 | TAIFEX Proxy |
| 外資空方 OI | 114,166 | TAIFEX Proxy |
| 外資多空淨 OI | -97,863 | TAIFEX Proxy |
| 投信多方 OI | 91,618 | TAIFEX Proxy |
| 投信空方 OI | 4,019 | TAIFEX Proxy |
| 投信多空淨 OI | +87,599 | TAIFEX Proxy |
| 自營商多方 OI | 4,128 | TAIFEX Proxy |
| 自營商空方 OI | 3,846 | TAIFEX Proxy |
| 自營商多空淨 OI | +282 | TAIFEX Proxy |
| 三大法人合計多方 OI | 112,049 | TAIFEX Proxy |
| 三大法人合計空方 OI | 122,031 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -9,982 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +1,356 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -4,192 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | +1,737 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 101,260 | TAIFEX Proxy |
| 前十大交易人空方 OI | 96,915 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,345 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-19→2026-11-20) | -726 | TAIFEX Proxy snapshots (2026-11-19) |
- 資料日期：2026-11-20 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 118,873 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 117,563 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +1,310 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 55,920 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 54,490 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,430 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -120 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -4,192 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -4,192 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | +1,723 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -317 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | +2,040 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,159 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,113 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -73.5 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +76.8 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 35,875 | TAIFEX Proxy |
| 加權指數價格 | 36,033.29 | twse-proxy |
| 台指期與加權指數價差 | -158.29 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | -0.44 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | -158.29 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -1,956 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 35,875 | 33,919 | +1,956 | TAIFEX Proxy |
| 成交量 | 109,453 | 82,477 | +26,976 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-1,099（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 118,873 | 117,563 | +1,310 | 55,920 | 54,490 | +1,430 | -120 | 16,303 | 114,166 | -97,863 | +1,356 | TAIFEX Proxy |
| 投信 | 60 | 4,252 | -4,192 | 0 | 0 | +0 | -4,192 | 91,618 | 4,019 | +87,599 | -4,192 | TAIFEX Proxy |
| 自營商 | 11,645 | 9,922 | +1,723 | 1,273 | 1,590 | -317 | +2,040 | 4,128 | 3,846 | +282 | +1,737 | TAIFEX Proxy |
| 三大法人合計 | 130,578 | 131,737 | -1,159 | 57,193 | 56,080 | +1,113 | -2,272 | 112,049 | 122,031 | -9,982 | -1,099 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 101,260 | TAIFEX Proxy |
| 前十大交易人空方 OI | 96,915 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,345 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-19→2026-11-20) | -726 | TAIFEX Proxy snapshots (2026-11-19) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 42.97% | TAIFEX Proxy |
| 夜盤漲跌點數 | -1,881 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,430 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-20 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F3 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-21 07:54:06 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 376,851 | TAIFEX Proxy |
| Call 總未平倉量 OI | 138,730 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-19→2026-11-20) | +52,458 | TAIFEX Proxy snapshot bundle (2026-11-19→2026-11-20) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 330,120 | TAIFEX Proxy |
| Put 總未平倉量 OI | 65,847 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-19→2026-11-20) | +7,349 | TAIFEX Proxy snapshot bundle (2026-11-19→2026-11-20) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.14 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 2.11 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.47 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-19→2026-11-20) | 5.58 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-19→2026-11-20) | -10.95 | 百分點（pp） | TAIFEX Proxy |
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
| 外資 Call夜買 | 13,791 | TAIFEX Proxy |
| 外資 Call夜賣 | 15,394 | TAIFEX Proxy |
| 外資 Call夜淨 | -1,603 | TAIFEX Proxy |
| 外資 Put夜買 | 5,449 | TAIFEX Proxy |
| 外資 Put夜賣 | 5,663 | TAIFEX Proxy |
| 外資 Put夜淨 | -214 | TAIFEX Proxy |
| 外資 日盤淨總量 | +9,756 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +12,113 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +968 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 88,783 | TAIFEX Proxy |
| 自營商 Call日賣 | 111,101 | TAIFEX Proxy |
| 自營商 Call日淨 | -22,318 | TAIFEX Proxy |
| 自營商 Put日買 | 73,633 | TAIFEX Proxy |
| 自營商 Put日賣 | 86,022 | TAIFEX Proxy |
| 自營商 Put日淨 | -12,389 | TAIFEX Proxy |
| 自營商 Call夜買 | 16,688 | TAIFEX Proxy |
| 自營商 Call夜賣 | 15,516 | TAIFEX Proxy |
| 自營商 Call夜淨 | +1,172 | TAIFEX Proxy |
| 自營商 Put夜買 | 7,397 | TAIFEX Proxy |
| 自營商 Put夜賣 | 9,202 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,805 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -9,929 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -23,490 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -10,584 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 45,000 | 6,609 | TAIFEX Proxy |
| Call OI 第2大履約價 | 41,000 | 5,919 | TAIFEX Proxy |
| Call OI 第3大履約價 | 42,000 | 5,199 | TAIFEX Proxy |
| Call OI 最大履約價 | 45,000 | 6,609 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 45,000 | 6,609 | 4.76% | TAIFEX Proxy |
| C2 | 41,000 | 5,919 | 4.27% | TAIFEX Proxy |
| C3 | 42,000 | 5,199 | 3.75% | TAIFEX Proxy |
| C4 | 40,000 | 4,518 | 3.26% | TAIFEX Proxy |
| C5 | 39,500 | 3,747 | 2.7% | TAIFEX Proxy |
| C6 | 43,000 | 3,629 | 2.62% | TAIFEX Proxy |
| C7 | 39,000 | 3,549 | 2.56% | TAIFEX Proxy |
| C8 | 37,000 | 3,273 | 2.36% | TAIFEX Proxy |
| C9 | 38,500 | 3,041 | 2.19% | TAIFEX Proxy |
| C10 | 36,000 | 3,006 | 2.17% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 35,000 | 11,591 | TAIFEX Proxy |
| Put OI 第2大履約價 | 35,700 | 4,558 | TAIFEX Proxy |
| Put OI 第3大履約價 | 35,800 | 2,990 | TAIFEX Proxy |
| Put OI 最大履約價 | 35,000 | 11,591 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F3)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 35,000 | 11,591 | 17.6% | TAIFEX Proxy |
| P2 | 35,700 | 4,558 | 6.92% | TAIFEX Proxy |
| P3 | 35,800 | 2,990 | 4.54% | TAIFEX Proxy |
| P4 | 34,900 | 2,691 | 4.09% | TAIFEX Proxy |
| P5 | 34,500 | 1,780 | 2.7% | TAIFEX Proxy |
| P6 | 36,000 | 1,762 | 2.68% | TAIFEX Proxy |
| P7 | 37,000 | 1,653 | 2.51% | TAIFEX Proxy |
| P8 | 35,500 | 1,463 | 2.22% | TAIFEX Proxy |
| P9 | 35,600 | 1,435 | 2.18% | TAIFEX Proxy |
| P10 | 34,700 | 1,427 | 2.17% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 37,000 (+3,263) | TAIFEX Proxy snapshot bundle (2026-11-19→2026-11-20) |
| Call OI 減少最多的履約價（共同合約） | 43,000 (-758) | TAIFEX Proxy snapshot bundle (2026-11-19→2026-11-20) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 35,800 (+2,566) | TAIFEX Proxy snapshot bundle (2026-11-19→2026-11-20) |
| Put OI 減少最多的履約價（共同合約） | 37,000 (-630) | TAIFEX Proxy snapshot bundle (2026-11-19→2026-11-20) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 45,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-19→2026-11-20) | +0 | TAIFEX Proxy snapshots (2026-11-19) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 35,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-19→2026-11-20) | -700 | TAIFEX Proxy snapshots (2026-11-19) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 35,700.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F3 | TAIFEX Proxy |
| 資料日期 | 2026-11-20 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 37,575.78 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611W4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-25 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F3 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 43,557 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 43,557 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 5,731 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 5,731 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-20 | TAIFEX Proxy (options-gamma-levels + options-market-structure-compact (proxy)) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：32,429.96～39,636.62
- 搜尋步長／計算次數：10.00／722
- 起點／終點 Net GEX：523,231,045.02／2,069,668,404.60
- 搜尋區間最低／最高 Net GEX：523,231,045.02／2,069,668,404.60
- 正負號交叉次數：0
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-20","chain_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":452,"delta_rows":0},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":452,"delta_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":428,"delta_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":280,"delta_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":204,"delta_rows":204},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":572,"delta_rows":572},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":432,"delta_rows":432},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":276,"delta_rows":276},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":294,"delta_rows":294},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":294,"delta_rows":294}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-20","source":"taifex_csv","fallback_used":false,"csv_duration_ms":971,"attempts":[{"source":"taifex_csv","duration_ms":971,"http_status":200,"bytes":447777,"parser":{"requested_date":"2026-11-20","source_date":"2026-11-20","published_at":"2026/11/20 04:37:26 PM","input_lines":9046,"txo_rows":3232,"parsed_rows":3232,"invalid_rows":0,"call_rows":1616,"put_rows":1616},"accepted_txo_rows":3232}],"parser":{"requested_date":"2026-11-20","source_date":"2026-11-20","published_at":"2026/11/20 04:37:26 PM","input_lines":9046,"txo_rows":3232,"parsed_rows":3232,"invalid_rows":0,"call_rows":1616,"put_rows":1616},"final_rows":3232}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：30,628.30～41,438.28
- 搜尋步長／計算次數：10.00／1082
- 起點／終點 Net GEX：72,433,074.90／2,154,146,635.57
- 搜尋區間最低／最高 Net GEX：72,433,074.90／2,154,146,635.57
- 正負號交叉次數：0
- 擴大區間診斷 Flip：unavailable

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 1,966,070,303.40 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 2,741,823,652.46 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 226 | 資料日期：2026-11-20 |
| 正 Net GEX 最大履約價 | 35,700 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 34,500 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：35,700（323,534,920.15 NT$）、35,800（260,531,454.00 NT$）、35,300（259,763,099.19 NT$）、35,200（204,323,726.13 NT$）、34,900（187,994,745.93 NT$）
- 負 Net GEX Top 5：34,500（-42,191,312.46 NT$）、37,800（-39,732,951.47 NT$）、39,500（-26,431,300.91 NT$）、36,000（-13,272,377.96 NT$）、36,500（-10,625,793.21 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-20","underlying":36033.29,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":1966070303.4043014,"gross_gex_1pct":2741823652.4607143,"gamma_diagnostics":{"chain_rows":452,"delta_rows":452,"matched_strike_keys":452,"positive_oi_settlement_eligible":379,"invalid_oi":73,"invalid_settlement":0,"below_intrinsic":0,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":379},"formal_flip_diagnostics":{"search_lower_underlying":32429.961000000003,"search_upper_underlying":39636.619000000006,"step":10,"evaluations":722,"start_net_gex_1pct":523231045.02205163,"end_net_gex_1pct":2069668404.595156,"min_net_gex_1pct":523231045.02205163,"max_net_gex_1pct":2069668404.595156,"zero_crossings":0,"found":false},"wide_range_flip":null,"wide_range_flip_diagnostics":{"search_lower_underlying":30628.2965,"search_upper_underlying":41438.2835,"reference_underlying":36033.29,"step":10,"evaluations":1082,"start_net_gex_1pct":72433074.90057588,"end_net_gex_1pct":2154146635.5695553,"min_net_gex_1pct":72433074.90057588,"max_net_gex_1pct":2154146635.5695553,"zero_crossings":0,"found":false,"selected_crossing_distance":null},"expiry_selection_diagnostics":{"requested_date":"2026-11-20","chain_expiries":[{"contract_month":"202611F3","expiry":"2026-11-20"},{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F3","expiry":"2026-11-20","chain_rows":452,"delta_rows":0},{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":452,"delta_rows":452},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":428,"delta_rows":428},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":280,"delta_rows":280},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":204,"delta_rows":204},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":572,"delta_rows":572},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":432,"delta_rows":432},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":276,"delta_rows":276},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":294,"delta_rows":294},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":294,"delta_rows":294}],"selected":{"contract_month":"202611W4","expiry":"2026-11-25","delta_contract_month":"202611W4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":34500.0,"call_gex_1pct":2509968.1715989797,"put_gex_1pct":-44701280.63552682,"net_gex_1pct":-42191312.46392784,"gross_gex_1pct":47211248.8071258,"call_oi":28,"put_oi":609},{"strike":34600.0,"call_gex_1pct":733571.7609748729,"put_gex_1pct":-5544129.908011822,"net_gex_1pct":-4810558.147036949,"gross_gex_1pct":6277701.668986695,"call_oi":8,"put_oi":74},{"strike":34700.0,"call_gex_1pct":660516.5814643095,"put_gex_1pct":-8498894.593244828,"net_gex_1pct":-7838378.011780519,"gross_gex_1pct":9159411.174709138,"call_oi":7,"put_oi":112},{"strike":34800.0,"call_gex_1pct":2521920.7173734503,"put_gex_1pct":-3341453.211183688,"net_gex_1pct":-819532.4938102379,"gross_gex_1pct":5863373.928557139,"call_oi":26,"put_oi":43},{"strike":34900.0,"call_gex_1pct":192539045.24276665,"put_gex_1pct":-4544299.313065696,"net_gex_1pct":187994745.92970094,"gross_gex_1pct":197083344.55583236,"call_oi":1951,"put_oi":58},{"strike":35000.0,"call_gex_1pct":202761352.9053714,"put_gex_1pct":-18942667.131424762,"net_gex_1pct":183818685.77394664,"gross_gex_1pct":221704020.03679615,"call_oi":2002,"put_oi":238},{"strike":35100.0,"call_gex_1pct":5906496.637140749,"put_gex_1pct":-1449362.690878357,"net_gex_1pct":4457133.946262392,"gross_gex_1pct":7355859.328019106,"call_oi":58,"put_oi":18},{"strike":35200.0,"call_gex_1pct":206685693.95920902,"put_gex_1pct":-2361967.8263410474,"net_gex_1pct":204323726.132868,"gross_gex_1pct":209047661.78555006,"call_oi":2000,"put_oi":29},{"strike":35300.0,"call_gex_1pct":262069623.25469682,"put_gex_1pct":-2306524.0645859353,"net_gex_1pct":259763099.1901109,"gross_gex_1pct":264376147.31928274,"call_oi":2500,"put_oi":28},{"strike":35400.0,"call_gex_1pct":2763913.032736088,"put_gex_1pct":-1885094.3293298176,"net_gex_1pct":878818.7034062706,"gross_gex_1pct":4649007.362065906,"call_oi":26,"put_oi":23},{"strike":35500.0,"call_gex_1pct":8638896.664037596,"put_gex_1pct":-5598336.57033673,"net_gex_1pct":3040560.093700866,"gross_gex_1pct":14237233.234374326,"call_oi":81,"put_oi":67},{"strike":35600.0,"call_gex_1pct":12757459.527759688,"put_gex_1pct":-3519564.809718626,"net_gex_1pct":9237894.718041062,"gross_gex_1pct":16277024.337478314,"call_oi":118,"put_oi":42},{"strike":35700.0,"call_gex_1pct":328110638.6479197,"put_gex_1pct":-4575718.500987638,"net_gex_1pct":323534920.14693207,"gross_gex_1pct":332686357.14890736,"call_oi":3026,"put_oi":54},{"strike":35800.0,"call_gex_1pct":274892050.939689,"put_gex_1pct":-14360596.936848616,"net_gex_1pct":260531454.00284037,"gross_gex_1pct":289252647.8765376,"call_oi":2528,"put_oi":169},{"strike":35900.0,"call_gex_1pct":8200284.416902206,"put_gex_1pct":-2619797.03823493,"net_gex_1pct":5580487.378667276,"gross_gex_1pct":10820081.455137135,"call_oi":76,"put_oi":31},{"strike":36000.0,"call_gex_1pct":20992750.43427382,"put_gex_1pct":-34265128.39164889,"net_gex_1pct":-13272377.957375068,"gross_gex_1pct":55257878.82592271,"call_oi":193,"put_oi":401},{"strike":36100.0,"call_gex_1pct":1068170.0951086865,"put_gex_1pct":-6742916.56063431,"net_gex_1pct":-5674746.465525623,"gross_gex_1pct":7811086.655742997,"call_oi":10,"put_oi":80},{"strike":36200.0,"call_gex_1pct":3963176.0327296634,"put_gex_1pct":-4817656.153060451,"net_gex_1pct":-854480.1203307877,"gross_gex_1pct":8780832.185790114,"call_oi":37,"put_oi":57},{"strike":36300.0,"call_gex_1pct":7372990.007844541,"put_gex_1pct":-2858275.364325851,"net_gex_1pct":4514714.64351869,"gross_gex_1pct":10231265.372170392,"call_oi":69,"put_oi":34},{"strike":36400.0,"call_gex_1pct":2015008.0953367858,"put_gex_1pct":-4214884.930840918,"net_gex_1pct":-2199876.8355041323,"gross_gex_1pct":6229893.026177703,"call_oi":19,"put_oi":50},{"strike":36500.0,"call_gex_1pct":5760290.269151488,"put_gex_1pct":-16386083.483384602,"net_gex_1pct":-10625793.214233113,"gross_gex_1pct":22146373.75253609,"call_oi":55,"put_oi":197},{"strike":36600.0,"call_gex_1pct":1696895.4788672137,"put_gex_1pct":-2501984.7795688524,"net_gex_1pct":-805089.3007016387,"gross_gex_1pct":4198880.258436066,"call_oi":16,"put_oi":30},{"strike":36700.0,"call_gex_1pct":3182744.8291319124,"put_gex_1pct":-1959914.527449825,"net_gex_1pct":1222830.3016820874,"gross_gex_1pct":5142659.356581737,"call_oi":31,"put_oi":24},{"strike":36800.0,"call_gex_1pct":3395051.5415224773,"put_gex_1pct":-1555473.6868294445,"net_gex_1pct":1839577.8546930328,"gross_gex_1pct":4950525.228351922,"call_oi":33,"put_oi":19},{"strike":36900.0,"call_gex_1pct":2102983.084718589,"put_gex_1pct":-4444302.604074985,"net_gex_1pct":-2341319.5193563956,"gross_gex_1pct":6547285.6887935735,"call_oi":21,"put_oi":55},{"strike":37000.0,"call_gex_1pct":24239387.23485907,"put_gex_1pct":-9013616.728986075,"net_gex_1pct":15225770.505872997,"gross_gex_1pct":33253003.96384515,"call_oi":244,"put_oi":113},{"strike":37100.0,"call_gex_1pct":7092346.5038915705,"put_gex_1pct":-3779861.591236096,"net_gex_1pct":3312484.9126554746,"gross_gex_1pct":10872208.095127666,"call_oi":72,"put_oi":48},{"strike":37200.0,"call_gex_1pct":4070437.464280967,"put_gex_1pct":-12827807.675015407,"net_gex_1pct":-8757370.21073444,"gross_gex_1pct":16898245.139296375,"call_oi":43,"put_oi":165},{"strike":37300.0,"call_gex_1pct":5988430.515637041,"put_gex_1pct":-4039276.63921569,"net_gex_1pct":1949153.876421351,"gross_gex_1pct":10027707.154852731,"call_oi":64,"put_oi":53},{"strike":37350.0,"call_gex_1pct":1573860.564875163,"put_gex_1pct":-754668.6425406561,"net_gex_1pct":819191.9223345068,"gross_gex_1pct":2328529.207415819,"call_oi":17,"put_oi":10},{"strike":37400.0,"call_gex_1pct":4579867.130879367,"put_gex_1pct":-1505026.0182746274,"net_gex_1pct":3074841.112604739,"gross_gex_1pct":6084893.149153994,"call_oi":50,"put_oi":20},{"strike":37450.0,"call_gex_1pct":543286.614876216,"put_gex_1pct":-375153.02747680026,"net_gex_1pct":168133.5873994158,"gross_gex_1pct":918439.6423530163,"call_oi":6,"put_oi":5},{"strike":37500.0,"call_gex_1pct":12579834.98701166,"put_gex_1pct":-3394633.2393121533,"net_gex_1pct":9185201.747699507,"gross_gex_1pct":15974468.226323813,"call_oi":140,"put_oi":46},{"strike":37550.0,"call_gex_1pct":2129820.8308382006,"put_gex_1pct":0.0,"net_gex_1pct":2129820.8308382006,"gross_gex_1pct":2129820.8308382006,"call_oi":24,"put_oi":0},{"strike":37600.0,"call_gex_1pct":3078789.679635156,"put_gex_1pct":-1530132.904099617,"net_gex_1pct":1548656.775535539,"gross_gex_1pct":4608922.583734773,"call_oi":35,"put_oi":21},{"strike":37650.0,"call_gex_1pct":863603.1460378473,"put_gex_1pct":-72162.41780648382,"net_gex_1pct":791440.7282313635,"gross_gex_1pct":935765.5638443311,"call_oi":10,"put_oi":1},{"strike":37700.0,"call_gex_1pct":3760352.2025717944,"put_gex_1pct":-923211.6257965032,"net_gex_1pct":2837140.576775291,"gross_gex_1pct":4683563.828368298,"call_oi":44,"put_oi":13},{"strike":37750.0,"call_gex_1pct":1347417.2332169965,"put_gex_1pct":-566315.1034703676,"net_gex_1pct":781102.1297466289,"gross_gex_1pct":1913732.3366873641,"call_oi":16,"put_oi":8},{"strike":37800.0,"call_gex_1pct":3739273.236175194,"put_gex_1pct":-43472224.71100078,"net_gex_1pct":-39732951.47482558,"gross_gex_1pct":47211497.94717597,"call_oi":45,"put_oi":620},{"strike":37850.0,"call_gex_1pct":1901160.4876602048,"put_gex_1pct":-486164.56465678423,"net_gex_1pct":1414995.9230034205,"gross_gex_1pct":2387325.052316989,"call_oi":23,"put_oi":7},{"strike":37900.0,"call_gex_1pct":6725696.9975957,"put_gex_1pct":-1788688.8266290776,"net_gex_1pct":4937008.170966623,"gross_gex_1pct":8514385.824224778,"call_oi":83,"put_oi":26},{"strike":37950.0,"call_gex_1pct":2628529.768839108,"put_gex_1pct":0.0,"net_gex_1pct":2628529.768839108,"gross_gex_1pct":2628529.768839108,"call_oi":33,"put_oi":0},{"strike":38000.0,"call_gex_1pct":53262528.89012996,"put_gex_1pct":-5805472.562984272,"net_gex_1pct":47457056.32714569,"gross_gex_1pct":59068001.453114234,"call_oi":676,"put_oi":86},{"strike":38050.0,"call_gex_1pct":1706739.37949572,"put_gex_1pct":-735578.8363522941,"net_gex_1pct":971160.5431434258,"gross_gex_1pct":2442318.2158480138,"call_oi":22,"put_oi":11},{"strike":38100.0,"call_gex_1pct":5064032.596989535,"put_gex_1pct":-1126122.941001379,"net_gex_1pct":3937909.655988156,"gross_gex_1pct":6190155.537990914,"call_oi":66,"put_oi":17},{"strike":38150.0,"call_gex_1pct":2107949.245441262,"put_gex_1pct":0.0,"net_gex_1pct":2107949.245441262,"gross_gex_1pct":2107949.245441262,"call_oi":28,"put_oi":0},{"strike":38200.0,"call_gex_1pct":3269910.4279698804,"put_gex_1pct":-1300072.88449128,"net_gex_1pct":1969837.5434786004,"gross_gex_1pct":4569983.31246116,"call_oi":44,"put_oi":20},{"strike":38250.0,"call_gex_1pct":1827369.6013858537,"put_gex_1pct":-64053.96413914602,"net_gex_1pct":1763315.6372467077,"gross_gex_1pct":1891423.5655249998,"call_oi":25,"put_oi":1},{"strike":38300.0,"call_gex_1pct":3747062.8666742523,"put_gex_1pct":-1786001.0100998539,"net_gex_1pct":1961061.8565743985,"gross_gex_1pct":5533063.876774106,"call_oi":52,"put_oi":28},{"strike":38350.0,"call_gex_1pct":1205627.4215223948,"put_gex_1pct":0.0,"net_gex_1pct":1205627.4215223948,"gross_gex_1pct":1205627.4215223948,"call_oi":17,"put_oi":0},{"strike":38400.0,"call_gex_1pct":9148131.686562723,"put_gex_1pct":-6290145.644317281,"net_gex_1pct":2857986.042245441,"gross_gex_1pct":15438277.330880005,"call_oi":131,"put_oi":101},{"strike":38450.0,"call_gex_1pct":3232644.93749909,"put_gex_1pct":0.0,"net_gex_1pct":3232644.93749909,"gross_gex_1pct":3232644.93749909,"call_oi":47,"put_oi":0},{"strike":38500.0,"call_gex_1pct":16247111.835151983,"put_gex_1pct":-2919786.3499739836,"net_gex_1pct":13327325.485178,"gross_gex_1pct":19166898.185125966,"call_oi":240,"put_oi":48},{"strike":38550.0,"call_gex_1pct":1929702.8871207936,"put_gex_1pct":0.0,"net_gex_1pct":1929702.8871207936,"gross_gex_1pct":1929702.8871207936,"call_oi":29,"put_oi":0},{"strike":38600.0,"call_gex_1pct":2616096.5269965148,"put_gex_1pct":-1970020.8305752482,"net_gex_1pct":646075.6964212665,"gross_gex_1pct":4586117.357571763,"call_oi":40,"put_oi":33},{"strike":38650.0,"call_gex_1pct":1093804.9974301204,"put_gex_1pct":-236542.91838223627,"net_gex_1pct":857262.0790478841,"gross_gex_1pct":1330347.9158123566,"call_oi":17,"put_oi":4},{"strike":38700.0,"call_gex_1pct":129315714.51893464,"put_gex_1pct":-5016464.726471242,"net_gex_1pct":124299249.79246339,"gross_gex_1pct":134332179.24540588,"call_oi":2045,"put_oi":86},{"strike":38750.0,"call_gex_1pct":1242995.871146847,"put_gex_1pct":0.0,"net_gex_1pct":1242995.871146847,"gross_gex_1pct":1242995.871146847,"call_oi":20,"put_oi":0},{"strike":38800.0,"call_gex_1pct":8000458.187113535,"put_gex_1pct":-1368270.88120933,"net_gex_1pct":6632187.305904205,"gross_gex_1pct":9368729.068322865,"call_oi":131,"put_oi":24},{"strike":38850.0,"call_gex_1pct":1260799.9210282376,"put_gex_1pct":0.0,"net_gex_1pct":1260799.9210282376,"gross_gex_1pct":1260799.9210282376,"call_oi":21,"put_oi":0},{"strike":38900.0,"call_gex_1pct":118826843.31388535,"put_gex_1pct":-4012941.958399696,"net_gex_1pct":114813901.35548565,"gross_gex_1pct":122839785.27228504,"call_oi":2014,"put_oi":72},{"strike":38950.0,"call_gex_1pct":1216139.3753578414,"put_gex_1pct":-386482.45839073363,"net_gex_1pct":829656.9169671077,"gross_gex_1pct":1602621.833748575,"call_oi":21,"put_oi":7},{"strike":39000.0,"call_gex_1pct":25782574.074441686,"put_gex_1pct":-3500067.4294364103,"net_gex_1pct":22282506.645005275,"gross_gex_1pct":29282641.503878098,"call_oi":453,"put_oi":64},{"strike":39050.0,"call_gex_1pct":1451433.5865056387,"put_gex_1pct":-324991.5595176703,"net_gex_1pct":1126442.0269879685,"gross_gex_1pct":1776425.1460233089,"call_oi":26,"put_oi":6},{"strike":39100.0,"call_gex_1pct":109795784.76062393,"put_gex_1pct":-6684208.6244518915,"net_gex_1pct":103111576.13617204,"gross_gex_1pct":116479993.38507582,"call_oi":2005,"put_oi":125},{"strike":39150.0,"call_gex_1pct":968431.9666133571,"put_gex_1pct":-264798.7008433544,"net_gex_1pct":703633.2657700027,"gross_gex_1pct":1233230.6674567114,"call_oi":18,"put_oi":5},{"strike":39200.0,"call_gex_1pct":1636852.607358281,"put_gex_1pct":-1673430.7913422745,"net_gex_1pct":-36578.183983993484,"gross_gex_1pct":3310283.398700556,"call_oi":31,"put_oi":32},{"strike":39250.0,"call_gex_1pct":1245714.141333461,"put_gex_1pct":-309874.9984453657,"net_gex_1pct":935839.1428880953,"gross_gex_1pct":1555589.1397788269,"call_oi":24,"put_oi":6},{"strike":39300.0,"call_gex_1pct":2740218.191025894,"put_gex_1pct":-460343.25744228717,"net_gex_1pct":2279874.933583607,"gross_gex_1pct":3200561.4484681813,"call_oi":54,"put_oi":9},{"strike":39350.0,"call_gex_1pct":3186830.6752316584,"put_gex_1pct":-253255.11610737213,"net_gex_1pct":2933575.5591242863,"gross_gex_1pct":3440085.7913390305,"call_oi":64,"put_oi":5},{"strike":39400.0,"call_gex_1pct":3646963.3557541864,"put_gex_1pct":-750525.1563040059,"net_gex_1pct":2896438.1994501804,"gross_gex_1pct":4397488.512058192,"call_oi":75,"put_oi":15},{"strike":39450.0,"call_gex_1pct":6600009.896831645,"put_gex_1pct":-495432.138124648,"net_gex_1pct":6104577.758706996,"gross_gex_1pct":7095442.034956293,"call_oi":138,"put_oi":10},{"strike":39500.0,"call_gex_1pct":4798708.245436758,"put_gex_1pct":-31230009.15315367,"net_gex_1pct":-26431300.90771691,"gross_gex_1pct":36028717.39859043,"call_oi":102,"put_oi":638},{"strike":39550.0,"call_gex_1pct":596921.121068314,"put_gex_1pct":-290221.18124800856,"net_gex_1pct":306699.9398203054,"gross_gex_1pct":887142.3023163225,"call_oi":13,"put_oi":6},{"strike":39600.0,"call_gex_1pct":1391182.778731154,"put_gex_1pct":-1053619.258543493,"net_gex_1pct":337563.52018766105,"gross_gex_1pct":2444802.037274647,"call_oi":31,"put_oi":22},{"strike":39650.0,"call_gex_1pct":794562.4327690637,"put_gex_1pct":-426691.7541862181,"net_gex_1pct":367870.67858284566,"gross_gex_1pct":1221254.1869552818,"call_oi":18,"put_oi":9},{"strike":39700.0,"call_gex_1pct":1426741.4617179343,"put_gex_1pct":-421730.0510605775,"net_gex_1pct":1005011.4106573568,"gross_gex_1pct":1848471.5127785117,"call_oi":33,"put_oi":9},{"strike":39750.0,"call_gex_1pct":679451.7323040011,"put_gex_1pct":-277919.5260684167,"net_gex_1pct":401532.2062355844,"gross_gex_1pct":957371.2583724179,"call_oi":16,"put_oi":6},{"strike":39800.0,"call_gex_1pct":2831631.751235177,"put_gex_1pct":-595307.3337586467,"net_gex_1pct":2236324.41747653,"gross_gex_1pct":3426939.0849938234,"call_oi":68,"put_oi":13},{"strike":39850.0,"call_gex_1pct":652054.2701880417,"put_gex_1pct":-226646.76527361685,"net_gex_1pct":425407.50491442485,"gross_gex_1pct":878701.0354616586,"call_oi":16,"put_oi":5},{"strike":39900.0,"call_gex_1pct":1786924.2877810907,"put_gex_1pct":-179282.59571167495,"net_gex_1pct":1607641.6920694157,"gross_gex_1pct":1966206.8834927657,"call_oi":45,"put_oi":4},{"strike":39950.0,"call_gex_1pct":1313889.5560518352,"put_gex_1pct":-443596.0908647934,"net_gex_1pct":870293.4651870418,"gross_gex_1pct":1757485.6469166286,"call_oi":34,"put_oi":10},{"strike":40000.0,"call_gex_1pct":57987327.61218882,"put_gex_1pct":-1140579.3666453117,"net_gex_1pct":56846748.24554351,"gross_gex_1pct":59127906.97883414,"call_oi":1552,"put_oi":26},{"strike":40050.0,"call_gex_1pct":1215355.4867081065,"put_gex_1pct":-433877.06234233506,"net_gex_1pct":781478.4243657715,"gross_gex_1pct":1649232.5490504415,"call_oi":33,"put_oi":10},{"strike":40100.0,"call_gex_1pct":4538577.971217927,"put_gex_1pct":-300543.01689008315,"net_gex_1pct":4238034.954327843,"gross_gex_1pct":4839120.98810801,"call_oi":125,"put_oi":7},{"strike":40150.0,"call_gex_1pct":783401.6323553306,"put_gex_1pct":-254821.57411033826,"net_gex_1pct":528580.0582449924,"gross_gex_1pct":1038223.2064656689,"call_oi":22,"put_oi":6},{"strike":40200.0,"call_gex_1pct":6501798.6002375465,"put_gex_1pct":-798342.4557896345,"net_gex_1pct":5703456.1444479115,"gross_gex_1pct":7300141.056027181,"call_oi":189,"put_oi":19},{"strike":40250.0,"call_gex_1pct":1014517.6612893767,"put_gex_1pct":-290984.2013086025,"net_gex_1pct":723533.4599807742,"gross_gex_1pct":1305501.8625979791,"call_oi":30,"put_oi":7},{"strike":40300.0,"call_gex_1pct":1363051.4908357477,"put_gex_1pct":-123388.5202221635,"net_gex_1pct":1239662.9706135842,"gross_gex_1pct":1486440.0110579112,"call_oi":41,"put_oi":3},{"strike":40350.0,"call_gex_1pct":623079.6596433115,"put_gex_1pct":-122096.26695683444,"net_gex_1pct":500983.39268647705,"gross_gex_1pct":745175.926600146,"call_oi":19,"put_oi":3},{"strike":40400.0,"call_gex_1pct":1193051.1164756229,"put_gex_1pct":-241659.9319752512,"net_gex_1pct":951391.1845003717,"gross_gex_1pct":1434711.0484508742,"call_oi":37,"put_oi":6},{"strike":40450.0,"call_gex_1pct":412179.5593666374,"put_gex_1pct":-79725.90585169038,"net_gex_1pct":332453.653514947,"gross_gex_1pct":491905.46521832776,"call_oi":13,"put_oi":2},{"strike":40500.0,"call_gex_1pct":6026790.306113465,"put_gex_1pct":-986435.1321362666,"net_gex_1pct":5040355.173977198,"gross_gex_1pct":7013225.438249731,"call_oi":194,"put_oi":25},{"strike":40550.0,"call_gex_1pct":391015.6673316912,"put_gex_1pct":0.0,"net_gex_1pct":391015.6673316912,"gross_gex_1pct":391015.6673316912,"call_oi":13,"put_oi":0},{"strike":40600.0,"call_gex_1pct":2039964.3308968304,"put_gex_1pct":-425041.17282917694,"net_gex_1pct":1614923.1580676534,"gross_gex_1pct":2465005.5037260074,"call_oi":69,"put_oi":11},{"strike":40650.0,"call_gex_1pct":434052.5407426572,"put_gex_1pct":-76510.268059316,"net_gex_1pct":357542.2726833412,"gross_gex_1pct":510562.80880197324,"call_oi":15,"put_oi":2},{"strike":40700.0,"call_gex_1pct":1450464.2336099672,"put_gex_1pct":-303020.1550134386,"net_gex_1pct":1147444.0785965286,"gross_gex_1pct":1753484.3886234057,"call_oi":51,"put_oi":8},{"strike":40750.0,"call_gex_1pct":744223.4272119604,"put_gex_1pct":-562605.8724360348,"net_gex_1pct":181617.5547759256,"gross_gex_1pct":1306829.2996479953,"call_oi":27,"put_oi":15},{"strike":40800.0,"call_gex_1pct":2386008.617902499,"put_gex_1pct":-1891862.7835276634,"net_gex_1pct":494145.8343748357,"gross_gex_1pct":4277871.401430163,"call_oi":89,"put_oi":51},{"strike":40850.0,"call_gex_1pct":442824.9720560695,"put_gex_1pct":-918411.3758614417,"net_gex_1pct":-475586.4038053722,"gross_gex_1pct":1361236.3479175111,"call_oi":17,"put_oi":25},{"strike":40900.0,"call_gex_1pct":1068066.4101326326,"put_gex_1pct":-1200679.2659523902,"net_gex_1pct":-132612.85581975756,"gross_gex_1pct":2268745.6760850227,"call_oi":42,"put_oi":33},{"strike":40950.0,"call_gex_1pct":74441.90375772839,"put_gex_1pct":-36038.46461497243,"net_gex_1pct":38403.43914275596,"gross_gex_1pct":110480.36837270082,"call_oi":3,"put_oi":1},{"strike":41000.0,"call_gex_1pct":16492823.710749835,"put_gex_1pct":-498864.71205007687,"net_gex_1pct":15993958.998699758,"gross_gex_1pct":16991688.42279991,"call_oi":686,"put_oi":14},{"strike":41050.0,"call_gex_1pct":166214.11359310683,"put_gex_1pct":-35298.05483647682,"net_gex_1pct":130916.05875663001,"gross_gex_1pct":201512.16842958366,"call_oi":7,"put_oi":1},{"strike":41100.0,"call_gex_1pct":442638.69613230275,"put_gex_1pct":-139875.83453399132,"net_gex_1pct":302762.86159831146,"gross_gex_1pct":582514.530666294,"call_oi":19,"put_oi":4},{"strike":41150.0,"call_gex_1pct":272315.984247035,"put_gex_1pct":-242520.22837623642,"net_gex_1pct":29795.755870798574,"gross_gex_1pct":514836.2126232714,"call_oi":12,"put_oi":7},{"strike":41200.0,"call_gex_1pct":1268564.9122885186,"put_gex_1pct":-205969.60135438596,"net_gex_1pct":1062595.3109341327,"gross_gex_1pct":1474534.5136429046,"call_oi":57,"put_oi":6},{"strike":41250.0,"call_gex_1pct":872950.0248237355,"put_gex_1pct":0.0,"net_gex_1pct":872950.0248237355,"gross_gex_1pct":872950.0248237355,"call_oi":40,"put_oi":0},{"strike":41300.0,"call_gex_1pct":442139.0607743409,"put_gex_1pct":-67248.3135462956,"net_gex_1pct":374890.74722804525,"gross_gex_1pct":509387.3743206365,"call_oi":21,"put_oi":2},{"strike":41350.0,"call_gex_1pct":100880.94205053942,"put_gex_1pct":0.0,"net_gex_1pct":100880.94205053942,"gross_gex_1pct":100880.94205053942,"call_oi":5,"put_oi":0},{"strike":41400.0,"call_gex_1pct":506079.2071248806,"put_gex_1pct":-66048.45804029738,"net_gex_1pct":440030.7490845832,"gross_gex_1pct":572127.665165178,"call_oi":26,"put_oi":2},{"strike":41450.0,"call_gex_1pct":857386.6999913588,"put_gex_1pct":-163157.88173076182,"net_gex_1pct":694228.818260597,"gross_gex_1pct":1020544.5817221206,"call_oi":46,"put_oi":5},{"strike":41500.0,"call_gex_1pct":5691008.691731168,"put_gex_1pct":-97029.18206891681,"net_gex_1pct":5593979.509662251,"gross_gex_1pct":5788037.873800085,"call_oi":318,"put_oi":3},{"strike":41550.0,"call_gex_1pct":275990.43146129954,"put_gex_1pct":-64118.86786781009,"net_gex_1pct":211871.56359348944,"gross_gex_1pct":340109.2993291096,"call_oi":16,"put_oi":2},{"strike":41600.0,"call_gex_1pct":1006709.2188053334,"put_gex_1pct":-31780.575961349557,"net_gex_1pct":974928.6428439838,"gross_gex_1pct":1038489.7947666829,"call_oi":62,"put_oi":1},{"strike":41650.0,"call_gex_1pct":79635.64572983587,"put_gex_1pct":-63012.74102825515,"net_gex_1pct":16622.904701580723,"gross_gex_1pct":142648.38675809102,"call_oi":5,"put_oi":2},{"strike":41700.0,"call_gex_1pct":515513.1977985671,"put_gex_1pct":-124946.82016449369,"net_gex_1pct":390566.37763407343,"gross_gex_1pct":640460.0179630609,"call_oi":33,"put_oi":4},{"strike":41750.0,"call_gex_1pct":277958.6995900894,"put_gex_1pct":-92914.41165639265,"net_gex_1pct":185044.28793369673,"gross_gex_1pct":370873.111246482,"call_oi":18,"put_oi":3},{"strike":41800.0,"call_gex_1pct":787584.1824934965,"put_gex_1pct":-30710.561478848744,"net_gex_1pct":756873.6210146477,"gross_gex_1pct":818294.7439723453,"call_oi":52,"put_oi":1},{"strike":41850.0,"call_gex_1pct":356489.27908646606,"put_gex_1pct":-30334.070396175077,"net_gex_1pct":326155.208690291,"gross_gex_1pct":386823.34948264115,"call_oi":24,"put_oi":1},{"strike":41900.0,"call_gex_1pct":495470.97743515635,"put_gex_1pct":-120322.70130107265,"net_gex_1pct":375148.2761340837,"gross_gex_1pct":615793.678736229,"call_oi":37,"put_oi":4},{"strike":41950.0,"call_gex_1pct":116634.02272983971,"put_gex_1pct":-29831.342442909954,"net_gex_1pct":86802.68028692975,"gross_gex_1pct":146465.36517274968,"call_oi":9,"put_oi":1},{"strike":42000.0,"call_gex_1pct":7521495.411716648,"put_gex_1pct":-266273.7964929581,"net_gex_1pct":7255221.61522369,"gross_gex_1pct":7787769.208209607,"call_oi":615,"put_oi":9},{"strike":42050.0,"call_gex_1pct":221021.52535058808,"put_gex_1pct":-58688.977330351954,"net_gex_1pct":162332.54802023614,"gross_gex_1pct":279710.50268094003,"call_oi":19,"put_oi":2},{"strike":42100.0,"call_gex_1pct":1577005.2598299847,"put_gex_1pct":-86915.23594072282,"net_gex_1pct":1490090.023889262,"gross_gex_1pct":1663920.4957707075,"call_oi":139,"put_oi":3},{"strike":42150.0,"call_gex_1pct":132727.99313632082,"put_gex_1pct":-143685.68217198172,"net_gex_1pct":-10957.689035660907,"gross_gex_1pct":276413.6753083025,"call_oi":12,"put_oi":5},{"strike":42200.0,"call_gex_1pct":612576.0319440142,"put_gex_1pct":-114024.69477956089,"net_gex_1pct":498551.33716445335,"gross_gex_1pct":726600.7267235751,"call_oi":56,"put_oi":4},{"strike":42250.0,"call_gex_1pct":437081.79214482405,"put_gex_1pct":-113115.10015328167,"net_gex_1pct":323966.69199154235,"gross_gex_1pct":550196.8922981058,"call_oi":41,"put_oi":4},{"strike":42300.0,"call_gex_1pct":758064.8692276144,"put_gex_1pct":-28054.86082088932,"net_gex_1pct":730010.008406725,"gross_gex_1pct":786119.7300485037,"call_oi":73,"put_oi":1},{"strike":42350.0,"call_gex_1pct":469265.6398708991,"put_gex_1pct":0.0,"net_gex_1pct":469265.6398708991,"gross_gex_1pct":469265.6398708991,"call_oi":48,"put_oi":0},{"strike":42400.0,"call_gex_1pct":522245.4285521022,"put_gex_1pct":-27617.178671734335,"net_gex_1pct":494628.24988036783,"gross_gex_1pct":549862.6072238365,"call_oi":54,"put_oi":1},{"strike":42450.0,"call_gex_1pct":199196.30668431584,"put_gex_1pct":0.0,"net_gex_1pct":199196.30668431584,"gross_gex_1pct":199196.30668431584,"call_oi":24,"put_oi":0},{"strike":42500.0,"call_gex_1pct":1913541.5570342701,"put_gex_1pct":-135962.67561830732,"net_gex_1pct":1777578.8814159627,"gross_gex_1pct":2049504.2326525776,"call_oi":245,"put_oi":5},{"strike":42550.0,"call_gex_1pct":240648.2673067848,"put_gex_1pct":-242864.34281010376,"net_gex_1pct":-2216.075503318949,"gross_gex_1pct":483512.61011688854,"call_oi":32,"put_oi":9},{"strike":42600.0,"call_gex_1pct":550572.2714730537,"put_gex_1pct":-80341.11430785386,"net_gex_1pct":470231.15716519987,"gross_gex_1pct":630913.3857809076,"call_oi":74,"put_oi":3},{"strike":42650.0,"call_gex_1pct":105376.89019370622,"put_gex_1pct":-106315.21396055502,"net_gex_1pct":-938.3237668488,"gross_gex_1pct":211692.10415426124,"call_oi":15,"put_oi":4},{"strike":42700.0,"call_gex_1pct":264052.5028541584,"put_gex_1pct":-104911.86611432165,"net_gex_1pct":159140.63673983677,"gross_gex_1pct":368964.36896848003,"call_oi":40,"put_oi":4},{"strike":42750.0,"call_gex_1pct":105632.5264523634,"put_gex_1pct":-26031.92148547442,"net_gex_1pct":79600.60496688898,"gross_gex_1pct":131664.4479378378,"call_oi":17,"put_oi":1},{"strike":42800.0,"call_gex_1pct":343237.0345038019,"put_gex_1pct":-129193.4874711855,"net_gex_1pct":214043.5470326164,"gross_gex_1pct":472430.5219749874,"call_oi":59,"put_oi":5},{"strike":42850.0,"call_gex_1pct":109799.95999248001,"put_gex_1pct":-76944.70739819726,"net_gex_1pct":32855.25259428275,"gross_gex_1pct":186744.66739067726,"call_oi":22,"put_oi":3},{"strike":42900.0,"call_gex_1pct":121564.52118072983,"put_gex_1pct":-50920.95848744734,"net_gex_1pct":70643.5626932825,"gross_gex_1pct":172485.47966817717,"call_oi":29,"put_oi":2},{"strike":42950.0,"call_gex_1pct":253563.31844674217,"put_gex_1pct":-25275.37221461079,"net_gex_1pct":228287.9462321314,"gross_gex_1pct":278838.69066135294,"call_oi":63,"put_oi":1},{"strike":43000.0,"call_gex_1pct":17254905.486671776,"put_gex_1pct":-125464.30296317922,"net_gex_1pct":17129441.183708597,"gross_gex_1pct":17380369.789634954,"call_oi":5302,"put_oi":5},{"strike":43050.0,"call_gex_1pct":61186.897368948805,"put_gex_1pct":-149477.35021274825,"net_gex_1pct":-88290.45284379944,"gross_gex_1pct":210664.24758169707,"call_oi":19,"put_oi":6},{"strike":43100.0,"call_gex_1pct":159346.03386269548,"put_gex_1pct":-24735.414263671162,"net_gex_1pct":134610.6195990243,"gross_gex_1pct":184081.44812636665,"call_oi":50,"put_oi":1},{"strike":43150.0,"call_gex_1pct":44157.012638638385,"put_gex_1pct":-49120.75669701796,"net_gex_1pct":-4963.744058379576,"gross_gex_1pct":93277.76933565634,"call_oi":14,"put_oi":2},{"strike":43200.0,"call_gex_1pct":518219.3564945778,"put_gex_1pct":-48775.470669309645,"net_gex_1pct":469443.8858252681,"gross_gex_1pct":566994.8271638874,"call_oi":166,"put_oi":2},{"strike":43250.0,"call_gex_1pct":92702.98708619655,"put_gex_1pct":-48434.875729485204,"net_gex_1pct":44268.11135671134,"gross_gex_1pct":141137.86281568176,"call_oi":30,"put_oi":2},{"strike":43300.0,"call_gex_1pct":137588.43240424382,"put_gex_1pct":0.0,"net_gex_1pct":137588.43240424382,"gross_gex_1pct":137588.43240424382,"call_oi":46,"put_oi":0},{"strike":43350.0,"call_gex_1pct":85871.38959894673,"put_gex_1pct":0.0,"net_gex_1pct":85871.38959894673,"gross_gex_1pct":85871.38959894673,"call_oi":29,"put_oi":0},{"strike":43400.0,"call_gex_1pct":73290.66355351,"put_gex_1pct":-23720.16327343658,"net_gex_1pct":49570.50028007342,"gross_gex_1pct":97010.82682694659,"call_oi":25,"put_oi":1},{"strike":43450.0,"call_gex_1pct":110301.57579095446,"put_gex_1pct":0.0,"net_gex_1pct":110301.57579095446,"gross_gex_1pct":110301.57579095446,"call_oi":38,"put_oi":0},{"strike":43500.0,"call_gex_1pct":491489.9149138294,"put_gex_1pct":-233995.59707651415,"net_gex_1pct":257494.31783731526,"gross_gex_1pct":725485.5119903436,"call_oi":171,"put_oi":10},{"strike":43550.0,"call_gex_1pct":113849.03834790818,"put_gex_1pct":0.0,"net_gex_1pct":113849.03834790818,"gross_gex_1pct":113849.03834790818,"call_oi":40,"put_oi":0},{"strike":43600.0,"call_gex_1pct":138116.77302844278,"put_gex_1pct":-46174.6006277452,"net_gex_1pct":91942.17240069757,"gross_gex_1pct":184291.373656188,"call_oi":49,"put_oi":2},{"strike":43650.0,"call_gex_1pct":100499.40945267586,"put_gex_1pct":0.0,"net_gex_1pct":100499.40945267586,"gross_gex_1pct":100499.40945267586,"call_oi":36,"put_oi":0},{"strike":43700.0,"call_gex_1pct":218782.82242458995,"put_gex_1pct":-68349.21744652062,"net_gex_1pct":150433.6049780693,"gross_gex_1pct":287132.0398711106,"call_oi":81,"put_oi":3},{"strike":43750.0,"call_gex_1pct":131095.6093102169,"put_gex_1pct":0.0,"net_gex_1pct":131095.6093102169,"gross_gex_1pct":131095.6093102169,"call_oi":49,"put_oi":0},{"strike":43800.0,"call_gex_1pct":113960.14376588786,"put_gex_1pct":-44973.15762094505,"net_gex_1pct":68986.98614494281,"gross_gex_1pct":158933.3013868329,"call_oi":43,"put_oi":2},{"strike":43850.0,"call_gex_1pct":102392.89988232956,"put_gex_1pct":-111705.71640175056,"net_gex_1pct":-9312.816519421001,"gross_gex_1pct":214098.6162840801,"call_oi":39,"put_oi":5},{"strike":43900.0,"call_gex_1pct":73611.32386493623,"put_gex_1pct":-66592.60859289578,"net_gex_1pct":7018.715272040456,"gross_gex_1pct":140203.932457832,"call_oi":29,"put_oi":3},{"strike":43950.0,"call_gex_1pct":53936.177269278734,"put_gex_1pct":0.0,"net_gex_1pct":53936.177269278734,"gross_gex_1pct":53936.177269278734,"call_oi":22,"put_oi":0},{"strike":44000.0,"call_gex_1pct":1530351.5258382566,"put_gex_1pct":-723217.2750140198,"net_gex_1pct":807134.2508242368,"gross_gex_1pct":2253568.8008522764,"call_oi":630,"put_oi":33},{"strike":44050.0,"call_gex_1pct":2343.7666447702495,"put_gex_1pct":-43554.713309851,"net_gex_1pct":-41210.94666508075,"gross_gex_1pct":45898.47995462125,"call_oi":1,"put_oi":2},{"strike":44100.0,"call_gex_1pct":42916.005273757095,"put_gex_1pct":0.0,"net_gex_1pct":42916.005273757095,"gross_gex_1pct":42916.005273757095,"call_oi":19,"put_oi":0},{"strike":44150.0,"call_gex_1pct":19565.82416603647,"put_gex_1pct":0.0,"net_gex_1pct":19565.82416603647,"gross_gex_1pct":19565.82416603647,"call_oi":9,"put_oi":0},{"strike":44200.0,"call_gex_1pct":77309.003468419,"put_gex_1pct":0.0,"net_gex_1pct":77309.003468419,"gross_gex_1pct":77309.003468419,"call_oi":37,"put_oi":0},{"strike":44250.0,"call_gex_1pct":12424.608393913062,"put_gex_1pct":-148685.48492366695,"net_gex_1pct":-136260.8765297539,"gross_gex_1pct":161110.09331758,"call_oi":6,"put_oi":7},{"strike":44300.0,"call_gex_1pct":73526.55947421232,"put_gex_1pct":-105553.34620779859,"net_gex_1pct":-32026.78673358627,"gross_gex_1pct":179079.90568201093,"call_oi":37,"put_oi":5},{"strike":44350.0,"call_gex_1pct":35453.82002526362,"put_gex_1pct":0.0,"net_gex_1pct":35453.82002526362,"gross_gex_1pct":35453.82002526362,"call_oi":18,"put_oi":0},{"strike":44400.0,"call_gex_1pct":56609.06496177594,"put_gex_1pct":-20855.080085276473,"net_gex_1pct":35753.98487649947,"gross_gex_1pct":77464.14504705241,"call_oi":30,"put_oi":1},{"strike":44450.0,"call_gex_1pct":32476.47632346596,"put_gex_1pct":-62188.65594420697,"net_gex_1pct":-29712.17962074101,"gross_gex_1pct":94665.13226767293,"call_oi":18,"put_oi":3},{"strike":44500.0,"call_gex_1pct":203897.17078269343,"put_gex_1pct":0.0,"net_gex_1pct":203897.17078269343,"gross_gex_1pct":203897.17078269343,"call_oi":114,"put_oi":0},{"strike":44550.0,"call_gex_1pct":10239.137933457565,"put_gex_1pct":0.0,"net_gex_1pct":10239.137933457565,"gross_gex_1pct":10239.137933457565,"call_oi":6,"put_oi":0},{"strike":44600.0,"call_gex_1pct":18610.433924116613,"put_gex_1pct":-61085.17923095936,"net_gex_1pct":-42474.74530684274,"gross_gex_1pct":79695.61315507597,"call_oi":11,"put_oi":3},{"strike":44650.0,"call_gex_1pct":1610.359141543281,"put_gex_1pct":0.0,"net_gex_1pct":1610.359141543281,"gross_gex_1pct":1610.359141543281,"call_oi":1,"put_oi":0},{"strike":44700.0,"call_gex_1pct":15966.690951877043,"put_gex_1pct":0.0,"net_gex_1pct":15966.690951877043,"gross_gex_1pct":15966.690951877043,"call_oi":10,"put_oi":0},{"strike":44750.0,"call_gex_1pct":7577.962792906083,"put_gex_1pct":0.0,"net_gex_1pct":7577.962792906083,"gross_gex_1pct":7577.962792906083,"call_oi":5,"put_oi":0},{"strike":44800.0,"call_gex_1pct":25548.350325686086,"put_gex_1pct":0.0,"net_gex_1pct":25548.350325686086,"gross_gex_1pct":25548.350325686086,"call_oi":17,"put_oi":0},{"strike":44850.0,"call_gex_1pct":9954.364096801733,"put_gex_1pct":0.0,"net_gex_1pct":9954.364096801733,"gross_gex_1pct":9954.364096801733,"call_oi":7,"put_oi":0},{"strike":44900.0,"call_gex_1pct":9871.498848897738,"put_gex_1pct":0.0,"net_gex_1pct":9871.498848897738,"gross_gex_1pct":9871.498848897738,"call_oi":7,"put_oi":0},{"strike":44950.0,"call_gex_1pct":10636.452965584218,"put_gex_1pct":0.0,"net_gex_1pct":10636.452965584218,"gross_gex_1pct":10636.452965584218,"call_oi":8,"put_oi":0},{"strike":45000.0,"call_gex_1pct":1163005.8419817167,"put_gex_1pct":0.0,"net_gex_1pct":1163005.8419817167,"gross_gex_1pct":1163005.8419817167,"call_oi":882,"put_oi":0},{"strike":45050.0,"call_gex_1pct":20924.808831883965,"put_gex_1pct":-19331.56500658659,"net_gex_1pct":1593.243825297377,"gross_gex_1pct":40256.37383847055,"call_oi":16,"put_oi":1},{"strike":45100.0,"call_gex_1pct":22100.617388523882,"put_gex_1pct":0.0,"net_gex_1pct":22100.617388523882,"gross_gex_1pct":22100.617388523882,"call_oi":18,"put_oi":0},{"strike":45150.0,"call_gex_1pct":18267.81556768226,"put_gex_1pct":0.0,"net_gex_1pct":18267.81556768226,"gross_gex_1pct":18267.81556768226,"call_oi":15,"put_oi":0},{"strike":45200.0,"call_gex_1pct":23890.38907902606,"put_gex_1pct":0.0,"net_gex_1pct":23890.38907902606,"gross_gex_1pct":23890.38907902606,"call_oi":21,"put_oi":0},{"strike":45250.0,"call_gex_1pct":6770.99767147325,"put_gex_1pct":-94530.18398710244,"net_gex_1pct":-87759.1863156292,"gross_gex_1pct":101301.18165857569,"call_oi":6,"put_oi":5},{"strike":45300.0,"call_gex_1pct":10075.394879857702,"put_gex_1pct":0.0,"net_gex_1pct":10075.394879857702,"gross_gex_1pct":10075.394879857702,"call_oi":9,"put_oi":0},{"strike":45350.0,"call_gex_1pct":4158.010295138598,"put_gex_1pct":0.0,"net_gex_1pct":4158.010295138598,"gross_gex_1pct":4158.010295138598,"call_oi":4,"put_oi":0},{"strike":45400.0,"call_gex_1pct":9281.509303647961,"put_gex_1pct":0.0,"net_gex_1pct":9281.509303647961,"gross_gex_1pct":9281.509303647961,"call_oi":9,"put_oi":0},{"strike":45450.0,"call_gex_1pct":11254.841094624648,"put_gex_1pct":0.0,"net_gex_1pct":11254.841094624648,"gross_gex_1pct":11254.841094624648,"call_oi":11,"put_oi":0},{"strike":45500.0,"call_gex_1pct":626245.6253544089,"put_gex_1pct":0.0,"net_gex_1pct":626245.6253544089,"gross_gex_1pct":626245.6253544089,"call_oi":664,"put_oi":0},{"strike":45550.0,"call_gex_1pct":35559.979604577886,"put_gex_1pct":0.0,"net_gex_1pct":35559.979604577886,"gross_gex_1pct":35559.979604577886,"call_oi":38,"put_oi":0},{"strike":45600.0,"call_gex_1pct":19499.25280673259,"put_gex_1pct":0.0,"net_gex_1pct":19499.25280673259,"gross_gex_1pct":19499.25280673259,"call_oi":21,"put_oi":0},{"strike":45700.0,"call_gex_1pct":25249.045572174775,"put_gex_1pct":0.0,"net_gex_1pct":25249.045572174775,"gross_gex_1pct":25249.045572174775,"call_oi":30,"put_oi":0},{"strike":45800.0,"call_gex_1pct":4144.286788459263,"put_gex_1pct":0.0,"net_gex_1pct":4144.286788459263,"gross_gex_1pct":4144.286788459263,"call_oi":5,"put_oi":0},{"strike":45900.0,"call_gex_1pct":7427.254210126507,"put_gex_1pct":0.0,"net_gex_1pct":7427.254210126507,"gross_gex_1pct":7427.254210126507,"call_oi":10,"put_oi":0},{"strike":46000.0,"call_gex_1pct":1052131.7893145308,"put_gex_1pct":0.0,"net_gex_1pct":1052131.7893145308,"gross_gex_1pct":1052131.7893145308,"call_oi":1438,"put_oi":0},{"strike":46100.0,"call_gex_1pct":4520.281258127844,"put_gex_1pct":0.0,"net_gex_1pct":4520.281258127844,"gross_gex_1pct":4520.281258127844,"call_oi":7,"put_oi":0},{"strike":46200.0,"call_gex_1pct":16183.496268205949,"put_gex_1pct":0.0,"net_gex_1pct":16183.496268205949,"gross_gex_1pct":16183.496268205949,"call_oi":29,"put_oi":0},{"strike":46300.0,"call_gex_1pct":8249.212275346787,"put_gex_1pct":0.0,"net_gex_1pct":8249.212275346787,"gross_gex_1pct":8249.212275346787,"call_oi":15,"put_oi":0},{"strike":46400.0,"call_gex_1pct":1382.6857964523358,"put_gex_1pct":0.0,"net_gex_1pct":1382.6857964523358,"gross_gex_1pct":1382.6857964523358,"call_oi":3,"put_oi":0},{"strike":46500.0,"call_gex_1pct":44068.3707703279,"put_gex_1pct":0.0,"net_gex_1pct":44068.3707703279,"gross_gex_1pct":44068.3707703279,"call_oi":97,"put_oi":0},{"strike":46600.0,"call_gex_1pct":8509.959728867498,"put_gex_1pct":0.0,"net_gex_1pct":8509.959728867498,"gross_gex_1pct":8509.959728867498,"call_oi":19,"put_oi":0},{"strike":46700.0,"call_gex_1pct":3574.326362955401,"put_gex_1pct":0.0,"net_gex_1pct":3574.326362955401,"gross_gex_1pct":3574.326362955401,"call_oi":10,"put_oi":0},{"strike":46800.0,"call_gex_1pct":5639.3216862452,"put_gex_1pct":0.0,"net_gex_1pct":5639.3216862452,"gross_gex_1pct":5639.3216862452,"call_oi":16,"put_oi":0},{"strike":46900.0,"call_gex_1pct":1390.4069151922156,"put_gex_1pct":0.0,"net_gex_1pct":1390.4069151922156,"gross_gex_1pct":1390.4069151922156,"call_oi":4,"put_oi":0},{"strike":47000.0,"call_gex_1pct":516681.55773229524,"put_gex_1pct":-15849.205106734777,"net_gex_1pct":500832.3526255605,"gross_gex_1pct":532530.76283903,"call_oi":2039,"put_oi":1},{"strike":47100.0,"call_gex_1pct":1499.7216103079254,"put_gex_1pct":0.0,"net_gex_1pct":1499.7216103079254,"gross_gex_1pct":1499.7216103079254,"call_oi":6,"put_oi":0},{"strike":47200.0,"call_gex_1pct":1232.9416228301666,"put_gex_1pct":0.0,"net_gex_1pct":1232.9416228301666,"gross_gex_1pct":1232.9416228301666,"call_oi":5,"put_oi":0},{"strike":47300.0,"call_gex_1pct":729.9031646498867,"put_gex_1pct":0.0,"net_gex_1pct":729.9031646498867,"gross_gex_1pct":729.9031646498867,"call_oi":3,"put_oi":0},{"strike":47400.0,"call_gex_1pct":720.2678896264932,"put_gex_1pct":0.0,"net_gex_1pct":720.2678896264932,"gross_gex_1pct":720.2678896264932,"call_oi":3,"put_oi":0},{"strike":47500.0,"call_gex_1pct":473.9013091143359,"put_gex_1pct":0.0,"net_gex_1pct":473.9013091143359,"gross_gex_1pct":473.9013091143359,"call_oi":2,"put_oi":0},{"strike":47600.0,"call_gex_1pct":138.01384827627487,"put_gex_1pct":0.0,"net_gex_1pct":138.01384827627487,"gross_gex_1pct":138.01384827627487,"call_oi":1,"put_oi":0},{"strike":47700.0,"call_gex_1pct":1226.0220555190645,"put_gex_1pct":0.0,"net_gex_1pct":1226.0220555190645,"gross_gex_1pct":1226.0220555190645,"call_oi":9,"put_oi":0},{"strike":47800.0,"call_gex_1pct":10354.607537610385,"put_gex_1pct":0.0,"net_gex_1pct":10354.607537610385,"gross_gex_1pct":10354.607537610385,"call_oi":77,"put_oi":0},{"strike":47900.0,"call_gex_1pct":1327.6486803318496,"put_gex_1pct":0.0,"net_gex_1pct":1327.6486803318496,"gross_gex_1pct":1327.6486803318496,"call_oi":10,"put_oi":0},{"strike":48000.0,"call_gex_1pct":8389.87697372556,"put_gex_1pct":0.0,"net_gex_1pct":8389.87697372556,"gross_gex_1pct":8389.87697372556,"call_oi":64,"put_oi":0},{"strike":48100.0,"call_gex_1pct":129.45516577040925,"put_gex_1pct":0.0,"net_gex_1pct":129.45516577040925,"gross_gex_1pct":129.45516577040925,"call_oi":1,"put_oi":0},{"strike":48200.0,"call_gex_1pct":639.2689495374087,"put_gex_1pct":0.0,"net_gex_1pct":639.2689495374087,"gross_gex_1pct":639.2689495374087,"call_oi":5,"put_oi":0},{"strike":48300.0,"call_gex_1pct":631.4332468418414,"put_gex_1pct":0.0,"net_gex_1pct":631.4332468418414,"gross_gex_1pct":631.4332468418414,"call_oi":5,"put_oi":0},{"strike":48400.0,"call_gex_1pct":623.7636650831946,"put_gex_1pct":0.0,"net_gex_1pct":623.7636650831946,"gross_gex_1pct":623.7636650831946,"call_oi":5,"put_oi":0},{"strike":48500.0,"call_gex_1pct":986.0085404148101,"put_gex_1pct":0.0,"net_gex_1pct":986.0085404148101,"gross_gex_1pct":986.0085404148101,"call_oi":8,"put_oi":0},{"strike":48600.0,"call_gex_1pct":487.122863189401,"put_gex_1pct":0.0,"net_gex_1pct":487.122863189401,"gross_gex_1pct":487.122863189401,"call_oi":4,"put_oi":0},{"strike":48700.0,"call_gex_1pct":9025.558130787791,"put_gex_1pct":-27399.06450010428,"net_gex_1pct":-18373.50636931649,"gross_gex_1pct":36424.622630892074,"call_oi":75,"put_oi":2}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 37,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F3 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-19→2026-11-20) | -1,900 | TAIFEX Proxy snapshots (2026-11-19) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 242,129 | 232,373 | +9,756 | 19,454 | 20,843 | -1,389 | +11,145 | TAIFEX Proxy |
| 投信 | 280 | 23,730 | -23,450 | 0 | 0 | +0 | -23,450 | TAIFEX Proxy |
| 自營商 | 174,805 | 184,734 | -9,929 | 25,890 | 22,913 | +2,977 | -12,906 | TAIFEX Proxy |
| 三大法人合計 | 417,214 | 440,837 | -23,623 | 45,344 | 43,756 | +1,588 | -25,211 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 29.72 | 20.17 | +9.54 | 5.04 | 5.68 | -0.63 | +10.18 | TAIFEX Proxy |
| 投信 | 0.02 | 15.04 | -15.02 | 0.00 | 0.00 | +0 | -15.02 | TAIFEX Proxy |
| 自營商 | 26.94 | 25.21 | +1.73 | 7.95 | 6.97 | +0.98 | +0.75 | TAIFEX Proxy |
| 三大法人合計 | 56.68 | 60.42 | -3.74 | 13.00 | 12.65 | +0.34 | -4.08 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,790 | TAIFEX Proxy |
| 買權空方 OI | 16,976 | TAIFEX Proxy |
| 買權多空淨 OI | -4,186 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-19→2026-11-20) | -1,251 | TAIFEX Proxy snapshots (2026-11-19) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,564 | TAIFEX Proxy |
| 賣權空方 OI | 11,156 | TAIFEX Proxy |
| 賣權多空淨 OI | -592 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-19→2026-11-20) | -430 | TAIFEX Proxy snapshots (2026-11-19) |
- 資料日期：買權 2026-11-20／賣權 2026-11-20 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -726 | 2026-11-19→2026-11-20 | TAIFEX Proxy snapshots (2026-11-19) |
| 買權前十大 | -1,251 | 2026-11-19→2026-11-20 | TAIFEX Proxy snapshots (2026-11-19) |
| 賣權前十大 | -430 | 2026-11-19→2026-11-20 | TAIFEX Proxy snapshots (2026-11-19) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-20；本次報告產製時間：2026-11-21 07:54:06；時區：`Asia/Taipei`
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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-20；估值 1242 檔；3 檔採最近有效收盤價（價格日期 20261111 至 20261120）；Blave 同 T0 交叉驗證 140.4010%；差異 0.027 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；3 檔採最近有效收盤價（價格日期 20261111 至 20261120）。Blave 同 T0 交叉驗證 140.4010%；差異 0.027 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-20 非今日 2026-11-23，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611W4（到期日 2026-11-25）與 Options Key Levels 主到期月份 202611F3 不同；GEX 數值應以實際使用到期月份為準
- TAIFEX 註記：選擇權 OI 前日變化採共同有效合約計算：主力=202611F3; 共同合約=404; 本日有效/識別合約=452/452（覆蓋率 89.4%，OI 缺值/無效 0）；前日有效/識別合約=404/404（覆蓋率 100.0%，OI 缺值/無效 0）；僅本日/僅前日有效合約=48 / 0，未補零
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -95.1 | -97,863 | +1,310 | +1,430 | +9,756 | -1,389 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -73.5 | +87,599 | -4,192 | +0 | -23,450 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -340.8 | +282 | +1,723 | -317 | -9,929 | +2,977 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
