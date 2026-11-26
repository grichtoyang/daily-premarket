# DATA_REPORT_20261125

- 報告日期：`2026-11-26`
- T0 交易日期：`2026-11-25`
- 首次資料產出時間：`2026-11-26 16:39:27`
- 本次更新開始時間：`2026-11-26 16:39:27`
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
| 加權指數 | 38,195.43 | 點 | twse-proxy |
| 開盤 | 39,983.91 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 39,983.91 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 36,681.90 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 38,195.43 | 點 | twse-proxy |
| 漲跌點數 | -1,926.92 | 點 | twse-proxy |
| 漲跌幅 | -4.80 | % | twse-proxy |
| 成交金額 | 12,297.6 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 39 | twse-proxy |
| 下跌家數 | 1,033 | twse-proxy |
| 平盤家數 | 14 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 46 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 66 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 774 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 26 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 3 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 54 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -1,236.5 | 億元 | TWSE RWD BFI82U |
| 投信 | +550.3 | 億元 | TWSE RWD BFI82U |
| 自營商 | -128.3 | 億元 | TWSE RWD BFI82U |
| 三大法人合計 | -814.5 | 億元 | TWSE RWD BFI82U |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-25；估值 1246 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 151.6130%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 5,620.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -203.4 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 189,053 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -19,609 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 151.61 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-25；估值 1246 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 151.6130%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 34,775,784 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,462,374.525 | 2,123,058.961 | 20,585,433.486 | 張 |
| 借券賣出增減 | -16,660.699 | -7,353.299 | -24,013.998 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261125`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-26T16:39:41+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261125`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-26T16:39:42+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 12,297.6 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,531.1 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 13,828.7 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,182.78 | -18.31 | -0.25 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 23,585.80 | -147.74 | -0.62 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,046.90 | -167.27 | -0.64 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,182.95 | 164.25 | +0.33 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 8,774.86 | -57.64 | -0.65 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 27.03 | -1.26 | -4.45 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 57,499.16 | 487.54 | +0.86 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 4,711.21 | 13.70 | +0.29 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 22,226.88 | 260.87 | +1.19 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,476.88 | 0.41 | +0.01 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 10,084.04 | -2.32 | -0.02 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,220.50 | 24.75 | +0.34 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,182.50 | 82.25 | +0.32 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,330.00 | 102.00 | +0.20 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,712.30 | 6.20 | +0.23 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.61 | -0.02 | 25-NOV-26 | 2026-11-26T08:40:00+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.85 | -0.06 | 2026-11-25 | 2026-11-26T08:40:00+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.28 | -0.05 | 25-NOV-26 | 2026-11-26T08:40:00+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.24 | -0.06 | 2026-11-25 | 2026-11-26T08:40:00+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.97 | 0.04 | +0.14 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 103.75 | 0.08 | +0.08 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.13 | -0.13 | -0.08 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.46 | 0.81 | +0.06 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 342.34 | -6.86 | -1.96 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.19 | -0.21 | -1.57 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 29.49 | 0.16 | +0.55 | 2026-11-25 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 83.91 | 0.23 | +0.27 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,593.30 | 57.50 | +1.63 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 60,647.72 | 269.52 | +0.45 | 2026-11-26 | 2026-11-26T08:39:42+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：越跌越要買 三檔ETF本周吸金破千億
  - 來源：Yahoo 台股；發布時間：2026-11-26T07:09:04Z；台北時間：2026-11-26 15:09
  - 摘要：股市亂流不斷人心惶惶之際，散戶越跌越要買？統計指出，本周最受資金寵愛的是元大台灣50(0050)、主動統一台股增長(00981A)、主動中信台灣收益(00406A)，這三檔的新增發行張數推算，合計本周吸金超過千億元。統一投信表示，「AI需求
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B6%8A%E8%B7%8C%E8%B6%8A%E8%B2%B7%EF%BC%81%E6%8A%84%E5%BA%95%E6%97%8F%E6%90%B6%E8%B2%B70050%E3%80%8100981a%E3%80%8100406a-%E4%B8%80%E5%91%A8%E5%90%B8%E9%87%91%E7%A0%B4%E5%8D%83%E5%84%84%E5%85%83-071115168.html
- 事件2：外資提款縮手空單卻創高 分析師示警賣壓仍在
  - 來源：Yahoo 台股；發布時間：2026-11-26T07:03:51Z；台北時間：2026-11-26 15:03
  - 摘要：台股再度迎來絕地反攻，終場收漲近千點，收在39151點。三大法人今（26）日合計賣超132.65億元。其中，外資獨自賣超491.81億元，連續9個交易日賣超4708.43億元，呈現土洋對作。此外，外資淨空單水位再度提升至106,275口，再
  - 原文連結：https://tw.stock.yahoo.com/news/%E3%80%90follow%E6%B3%95%E4%BA%BA%E3%80%91%E5%A4%96%E8%B3%87%E6%8F%90%E6%AC%BE%E5%8F%B0%E7%A9%8D%E9%9B%BB392%E5%84%84%E5%85%83%EF%BC%81%E5%90%8C%E6%AD%A5%E7%BF%BB%E8%87%89%E9%87%8D%E7%A0%8D%E5%8F%B0%E7%8E%BB8%E8%90%AC%E5%BC%B5-%E4%B8%AD%E8%8F%AF%E9%9B%BB%E4%B9%9F%E9%9B%A3%E9%80%83%E8%90%AC%E5%BC%B5%E8%B3%A3%E8%B6%85-083548257.html
- 事件3：看急跌是情緒震盪 郭哲榮點名跌深股迎補漲
  - 來源：Yahoo 台股；發布時間：2026-11-26T07:45:00Z；台北時間：2026-11-26 15:45
  - 摘要：台股今（26）日大漲956點收39151點，重返3萬9000點。郭哲榮喊「天黑請閉眼、天亮請數錢」，看好欣興、健鼎等飆股，並持續看好台股5萬點、台積電3000元。（記者唐家興）
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%98%A8%E6%99%9A%E5%9A%87%E5%93%AD%E4%BB%8A%E6%95%B8%E9%8C%A2-%E5%8F%B0%E8%82%A1%E5%A5%87%E8%B9%9F%E5%A4%A7%E6%BC%B2956%E9%BB%9E-%E5%93%B2%E5%93%B2%E9%87%8D%E6%8A%BC0050%E7%A7%92%E7%BF%BB%E6%AD%A3-%E9%BB%9E%E5%90%8D8%E6%AA%94%E9%A3%86%E8%82%A1-074500480.html
- 事件4：看屋一圈能看出多少？房仲揭6類人幫你找隱憂
  - 來源：Yahoo 台股；發布時間：2026-11-26T07:38:35Z；台北時間：2026-11-26 15:38
  - 摘要：買房除了評估價格、地段、格局及屋況，周邊生活環境也是影響居住品質的重要因素。房仲何莉指出，部分居住問題不一定能從不動產說明書或短時間看屋過程中發現，尤其是購買中古屋、透天厝或屋齡較高的社區住宅時，建議購屋族除了向房仲及代書諮詢，也可向社區住
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%B2%B7%E6%88%BF%E5%88%A5%E5%8F%AA%E8%81%BD%E6%88%BF%E4%BB%B2%E8%AA%AA%EF%BC%816%E9%A1%9E%E3%80%8C%E7%A5%9E%E9%9A%8A%E5%8F%8B%E3%80%8D%E5%8A%A9%E6%8F%90%E5%89%8D%E7%99%BC%E7%8F%BE%E5%B1%85%E4%BD%8F%E9%9A%B1%E6%86%82-073835079.html
- 事件5：買錯聯發科認賠出場 技術分析達人分享兩大停損紀律
  - 來源：Yahoo 台股；發布時間：2026-11-25T22:58:57Z；台北時間：2026-11-26 06:58
  - 摘要：以基本面出發，卻總是賺不到錢，到改以技術分析操作，5年資產翻倍，林穎如今累積逾2千萬元資產，但她並非每次操作都成功，今年6月底她就曾買進聯發科，最後認賠停損出場。林穎強調，選錯股票不可怕，真正可怕的是捨不得認賠，讓小虧變成大賠。
  - 原文連結：https://tw.stock.yahoo.com/news/k%E7%B7%9A%E7%85%89%E9%87%91%E8%A1%933-%E8%B2%B7%E9%8C%AF%E8%81%AF%E7%99%BC%E7%A7%91%E6%9E%9C%E6%96%B7%E8%AA%8D%E8%B3%A0-%E5%8D%83%E8%90%AC%E9%81%94%E4%BA%BA%E7%94%A82%E5%A4%A7%E5%81%9C%E6%90%8D%E7%B4%80%E5%BE%8B%E4%B8%8D%E8%AE%93%E5%B0%8F%E8%99%A7%E8%AE%8A%E5%A4%A7%E8%B3%A0-225857991.html
- 事件6：基本面好為何外資狂賣超？投信副總剖析三大關鍵
  - 來源：Yahoo 台股；發布時間：2026-11-26T06:00:01Z；台北時間：2026-11-26 14:00
  - 摘要：台股週三(11/25)面臨沉重賣壓，終場大跌1926.92點，收在38195.43點，從籌碼面來看，三大法人合計賣超829.55億元，土洋法人操作呈現兩極。 今年以來大舉在台股提款的外資仍不手軟，賣超金額高達1236.54億元，創史上第7大
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%88%91%E4%BB%8A%E5%B9%B4%E8%B3%BA%E9%82%A3%E9%BA%BC%E5%A4%9A-%E5%85%88%E4%B8%8D%E7%8E%A9%E4%BA%86-%E5%A4%96%E8%B3%87%E5%9C%88%E6%8F%90%E6%AC%BE3%E6%83%85%E5%A2%83%E6%8F%AD%E5%AF%86-%E5%8F%88%E8%B3%A3%E8%B6%851236%E5%84%84-%E7%A9%BA%E5%96%AE10%E8%90%AC%E5%8F%A3-060001740.html
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
- 事件10：Asia-Pacific markets close higher as investors look past fresh U.S. tariffs
  - 來源：CNBC；發布時間：Thu, 26 Nov 2026 08:00:27 GMT；台北時間：2026-11-26 16:00
  - 摘要：Investors appeared to have shrugged off a fresh set of tariffs unveiled by the White House on Wednesday, targeting more than a dozen major trading par
  - 原文連結：https://www.cnbc.com/2026/11/26/stock-markets-today-.html
- 事件11：U.S. tariff-hike threats pile pressure on partners to sign trade deals
  - 來源：CNBC；發布時間：Thu, 26 Nov 2026 08:09:39 GMT；台北時間：2026-11-26 16:09
  - 摘要：The U.S. planned a fresh tariff salvo on 14 trading partners, while offering some countries lower rates if they secure trade deals with Washington.
  - 原文連結：https://www.cnbc.com/2026/11/26/us-tariffs-hike-trade-agreement.html
- 事件12：U.S. proposes new tariffs on 14 trading partners, including China and the EU
  - 來源：CNBC；發布時間：Wed, 25 Nov 2026 16:02:52 GMT；台北時間：2026-11-26 00:02
  - 摘要：The new levies seek to counter foreign trade practices deemed unfair, discriminatory or burdensome to U.S. commerce.
  - 原文連結：https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-25

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 38,990 | 點 | TAIFEX Proxy |
| 最高價 | 39,688 | 點 | TAIFEX Proxy |
| 最低價 | 38,473 | 點 | TAIFEX Proxy |
| 收盤價 | 39,455 | 點 | TAIFEX Proxy |
| 漲跌點數 | +1,332 | 點 | TAIFEX Proxy |
| 漲跌幅 | +3.49 | % | TAIFEX Proxy |
| 成交量 | 79,377 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 39,688 / 38,473 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 37,868 | 點 | TAIFEX Proxy |
| 最高價 | 38,397 | 點 | TAIFEX Proxy |
| 最低價 | 35,933 | 點 | TAIFEX Proxy |
| 收盤價 | 38,397 | 點 | TAIFEX Proxy |
| 漲跌點數 | +274 | 點 | TAIFEX Proxy |
| 漲跌幅 | +0.72 | % | TAIFEX Proxy |
| 成交量 | 79,451 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 38,397 / 35,933 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 11,439 | TAIFEX Proxy |
| 外資空方 OI | 117,148 | TAIFEX Proxy |
| 外資多空淨 OI | -105,709 | TAIFEX Proxy |
| 投信多方 OI | 104,614 | TAIFEX Proxy |
| 投信空方 OI | 3,696 | TAIFEX Proxy |
| 投信多空淨 OI | +100,918 | TAIFEX Proxy |
| 自營商多方 OI | 3,247 | TAIFEX Proxy |
| 自營商空方 OI | 3,898 | TAIFEX Proxy |
| 自營商多空淨 OI | -651 | TAIFEX Proxy |
| 三大法人合計多方 OI | 119,300 | TAIFEX Proxy |
| 三大法人合計空方 OI | 124,742 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,442 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -2,527 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +2,904 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -418 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 107,269 | TAIFEX Proxy |
| 前十大交易人空方 OI | 96,581 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,688 | TAIFEX Proxy |
| 多空淨 OI 變化 | +885 | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |
- 資料日期：2026-11-25 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 103,678 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 104,261 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -583 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 52,786 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 51,664 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,122 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,705 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +4,002 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +4,002 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,550 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +212 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,762 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,869 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,334 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | +137.8 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +95.4 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 39,455 | TAIFEX Proxy |
| 加權指數價格 | 38,195.43 | twse-proxy |
| 台指期與加權指數價差 | +1,259.57 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +3.30 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +1,259.57 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -1,058 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,455 | 38,397 | +1,058 | TAIFEX Proxy |
| 成交量 | 79,377 | 79,451 | -74 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-41（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 103,678 | 104,261 | -583 | 52,786 | 51,664 | +1,122 | -1,705 | 11,439 | 117,148 | -105,709 | -2,527 | TAIFEX Proxy |
| 投信 | 4,492 | 490 | +4,002 | 0 | 0 | +0 | +4,002 | 104,614 | 3,696 | +100,918 | +2,904 | TAIFEX Proxy |
| 自營商 | 4,271 | 5,821 | -1,550 | 1,120 | 908 | +212 | -1,762 | 3,247 | 3,898 | -651 | -418 | TAIFEX Proxy |
| 三大法人合計 | 112,441 | 110,572 | +1,869 | 53,906 | 52,572 | +1,334 | +535 | 119,300 | 124,742 | -5,442 | -41 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 107,269 | TAIFEX Proxy |
| 前十大交易人空方 OI | 96,581 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +10,688 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 | +885 | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 50.02% | TAIFEX Proxy |
| 夜盤漲跌點數 | +274 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,122 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-25 | TAIFEX Proxy |
| 到期月份／到期日 | 202611W4 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-26 16:39:27 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 449,066 | TAIFEX Proxy |
| Call 總未平倉量 OI | 144,977 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-24→2026-11-25) | +40,504 | TAIFEX Proxy snapshot bundle (2026-11-24→2026-11-25) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 397,862 | TAIFEX Proxy |
| Put 總未平倉量 OI | 94,561 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-24→2026-11-25) | +47,156 | TAIFEX Proxy snapshot bundle (2026-11-24→2026-11-25) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.13 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.53 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.65 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-24→2026-11-25) | 18.83 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-24→2026-11-25) | -6.12 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 42,858 | TAIFEX Proxy |
| 外資 Call日賣 | 41,698 | TAIFEX Proxy |
| 外資 Call日淨 | +1,160 | TAIFEX Proxy |
| 外資 Put日買 | 36,549 | TAIFEX Proxy |
| 外資 Put日賣 | 36,027 | TAIFEX Proxy |
| 外資 Put日淨 | +522 | TAIFEX Proxy |
| 外資 Call夜買 | 22,428 | TAIFEX Proxy |
| 外資 Call夜賣 | 20,966 | TAIFEX Proxy |
| 外資 Call夜淨 | +1,462 | TAIFEX Proxy |
| 外資 Put夜買 | 9,590 | TAIFEX Proxy |
| 外資 Put夜賣 | 10,072 | TAIFEX Proxy |
| 外資 Put夜淨 | -482 | TAIFEX Proxy |
| 外資 日盤淨總量 | +638 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -302 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,004 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 37,346 | TAIFEX Proxy |
| 自營商 Call日賣 | 35,880 | TAIFEX Proxy |
| 自營商 Call日淨 | +1,466 | TAIFEX Proxy |
| 自營商 Put日買 | 37,624 | TAIFEX Proxy |
| 自營商 Put日賣 | 43,115 | TAIFEX Proxy |
| 自營商 Put日淨 | -5,491 | TAIFEX Proxy |
| 自營商 Call夜買 | 10,013 | TAIFEX Proxy |
| 自營商 Call夜賣 | 15,440 | TAIFEX Proxy |
| 自營商 Call夜淨 | -5,427 | TAIFEX Proxy |
| 自營商 Put夜買 | 12,972 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,497 | TAIFEX Proxy |
| 自營商 Put夜淨 | -525 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +6,957 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +6,893 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -4,966 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 41,000 | 13,378 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 8,779 | TAIFEX Proxy |
| Call OI 第3大履約價 | 44,000 | 5,770 | TAIFEX Proxy |
| Call OI 最大履約價 | 41,000 | 13,378 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 41,000 | 13,378 | 9.23% | TAIFEX Proxy |
| C2 | 43,000 | 8,779 | 6.06% | TAIFEX Proxy |
| C3 | 44,000 | 5,770 | 3.98% | TAIFEX Proxy |
| C4 | 40,000 | 4,883 | 3.37% | TAIFEX Proxy |
| C5 | 42,000 | 3,995 | 2.76% | TAIFEX Proxy |
| C6 | 39,000 | 3,777 | 2.61% | TAIFEX Proxy |
| C7 | 38,500 | 3,693 | 2.55% | TAIFEX Proxy |
| C8 | 35,700 | 3,068 | 2.12% | TAIFEX Proxy |
| C9 | 41,500 | 2,938 | 2.03% | TAIFEX Proxy |
| C10 | 35,800 | 2,641 | 1.82% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 36,200 | 7,924 | TAIFEX Proxy |
| Put OI 第2大履約價 | 36,000 | 6,312 | TAIFEX Proxy |
| Put OI 第3大履約價 | 36,500 | 4,924 | TAIFEX Proxy |
| Put OI 最大履約價 | 36,200 | 7,924 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611W4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 36,200 | 7,924 | 8.38% | TAIFEX Proxy |
| P2 | 36,000 | 6,312 | 6.68% | TAIFEX Proxy |
| P3 | 36,500 | 4,924 | 5.21% | TAIFEX Proxy |
| P4 | 36,300 | 3,914 | 4.14% | TAIFEX Proxy |
| P5 | 36,100 | 3,264 | 3.45% | TAIFEX Proxy |
| P6 | 38,000 | 3,229 | 3.41% | TAIFEX Proxy |
| P7 | 32,400 | 3,017 | 3.19% | TAIFEX Proxy |
| P8 | 37,000 | 2,801 | 2.96% | TAIFEX Proxy |
| P9 | 34,500 | 2,362 | 2.5% | TAIFEX Proxy |
| P10 | 37,500 | 2,337 | 2.47% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 38,500 (+3,070) | TAIFEX Proxy snapshot bundle (2026-11-24→2026-11-25) |
| Call OI 減少最多的履約價（共同合約） | 44,000 (-807) | TAIFEX Proxy snapshot bundle (2026-11-24→2026-11-25) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 36,200 (+7,624) | TAIFEX Proxy snapshot bundle (2026-11-24→2026-11-25) |
| Put OI 減少最多的履約價（共同合約） | 39,000 (-977) | TAIFEX Proxy snapshot bundle (2026-11-24→2026-11-25) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 41,000 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-24→2026-11-25) | +0 | TAIFEX Proxy snapshots (2026-11-24) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 36,200 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-24→2026-11-25) | +3,800 | TAIFEX Proxy snapshots (2026-11-24) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 37,800.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202611F4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-27 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611W4 | TAIFEX Proxy |
| 資料日期 | 2026-11-25 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 37,924.75 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202611F4 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-11-27 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611W4 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 37,336 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 37,326 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 7,980 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 7,980 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-25 | TAIFEX Proxy (options-gamma-levels + options-market-structure-compact (proxy)) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：34,375.89～42,014.97
- 搜尋步長／計算次數：10.00／765
- 起點／終點 Net GEX：1,118,190,065.88／2,102,680,298.15
- 搜尋區間最低／最高 Net GEX：1,118,190,065.88／2,103,845,020.09
- 正負號交叉次數：0
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-25","chain_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":540,"delta_rows":0},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":364,"delta_rows":364},{"contract_month":"202612W2","expiry":"2026-12-09","chain_rows":212,"delta_rows":212},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-25","source":"taifex_csv","fallback_used":false,"csv_duration_ms":1851,"attempts":[{"source":"taifex_csv","duration_ms":1851,"http_status":200,"bytes":487377,"parser":{"requested_date":"2026-11-25","source_date":"2026-11-25","published_at":"2026/11/25 04:32:33 PM","input_lines":9846,"txo_rows":3464,"parsed_rows":3464,"invalid_rows":0,"call_rows":1732,"put_rows":1732},"accepted_txo_rows":3464}],"parser":{"requested_date":"2026-11-25","source_date":"2026-11-25","published_at":"2026/11/25 04:32:33 PM","input_lines":9846,"txo_rows":3464,"parsed_rows":3464,"invalid_rows":0,"call_rows":1732,"put_rows":1732},"final_rows":3464}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：32,466.12～43,924.74
- 搜尋步長／計算次數：10.00／1147
- 起點／終點 Net GEX：28,838,257.36／1,846,234,791.49
- 搜尋區間最低／最高 Net GEX：28,838,257.36／2,106,331,561.77
- 正負號交叉次數：0
- 擴大區間診斷 Flip：unavailable

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 2,076,073,509.68 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 2,864,728,656.52 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 257 | 資料日期：2026-11-25 |
| 正 Net GEX 最大履約價 | 37,800 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 32,400 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：37,800（444,152,839.79 NT$）、37,600（442,478,270.53 NT$）、37,500（321,753,569.35 NT$）、35,200（96,657,247.64 NT$）、35,400（91,504,339.16 NT$）
- 負 Net GEX Top 5：32,400（-30,755,726.33 NT$）、36,000（-18,529,542.69 NT$）、37,000（-17,112,818.38 NT$）、34,500（-15,329,019.62 NT$）、34,000（-11,287,999.46 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-25","underlying":38195.43,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":2076073509.6807532,"gross_gex_1pct":2864728656.5195417,"gamma_diagnostics":{"chain_rows":516,"delta_rows":516,"matched_strike_keys":516,"positive_oi_settlement_eligible":400,"invalid_oi":116,"invalid_settlement":0,"below_intrinsic":5,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":395},"formal_flip_diagnostics":{"search_lower_underlying":34375.887,"search_upper_underlying":42014.973000000005,"step":10,"evaluations":765,"start_net_gex_1pct":1118190065.875099,"end_net_gex_1pct":2102680298.1490672,"min_net_gex_1pct":1118190065.875099,"max_net_gex_1pct":2103845020.0870583,"zero_crossings":0,"found":false},"wide_range_flip":null,"wide_range_flip_diagnostics":{"search_lower_underlying":32466.1155,"search_upper_underlying":43924.74449999999,"reference_underlying":38195.43,"step":10,"evaluations":1147,"start_net_gex_1pct":28838257.357210644,"end_net_gex_1pct":1846234791.4949498,"min_net_gex_1pct":28838257.357210644,"max_net_gex_1pct":2106331561.7652977,"zero_crossings":0,"found":false,"selected_crossing_distance":null},"expiry_selection_diagnostics":{"requested_date":"2026-11-25","chain_expiries":[{"contract_month":"202611W4","expiry":"2026-11-25"},{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611W4","expiry":"2026-11-25","chain_rows":540,"delta_rows":0},{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":516},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":364,"delta_rows":364},{"contract_month":"202612W2","expiry":"2026-12-09","chain_rows":212,"delta_rows":212},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202611F4","expiry":"2026-11-27","delta_contract_month":"202611F4","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":32400.0,"call_gex_1pct":0.0,"put_gex_1pct":-30755726.327815246,"net_gex_1pct":-30755726.327815246,"gross_gex_1pct":30755726.327815246,"call_oi":0,"put_oi":1694},{"strike":32500.0,"call_gex_1pct":0.0,"put_gex_1pct":-6994616.575937611,"net_gex_1pct":-6994616.575937611,"gross_gex_1pct":6994616.575937611,"call_oi":0,"put_oi":364},{"strike":32600.0,"call_gex_1pct":0.0,"put_gex_1pct":-3540824.1476303297,"net_gex_1pct":-3540824.1476303297,"gross_gex_1pct":3540824.1476303297,"call_oi":0,"put_oi":176},{"strike":32700.0,"call_gex_1pct":0.0,"put_gex_1pct":-2200802.4483456416,"net_gex_1pct":-2200802.4483456416,"gross_gex_1pct":2200802.4483456416,"call_oi":0,"put_oi":105},{"strike":32800.0,"call_gex_1pct":0.0,"put_gex_1pct":-2976959.4195654285,"net_gex_1pct":-2976959.4195654285,"gross_gex_1pct":2976959.4195654285,"call_oi":0,"put_oi":136},{"strike":32900.0,"call_gex_1pct":0.0,"put_gex_1pct":-2324141.2636728324,"net_gex_1pct":-2324141.2636728324,"gross_gex_1pct":2324141.2636728324,"call_oi":0,"put_oi":103},{"strike":33000.0,"call_gex_1pct":0.0,"put_gex_1pct":-4686241.088004824,"net_gex_1pct":-4686241.088004824,"gross_gex_1pct":4686241.088004824,"call_oi":0,"put_oi":198},{"strike":33100.0,"call_gex_1pct":0.0,"put_gex_1pct":-2593376.523974403,"net_gex_1pct":-2593376.523974403,"gross_gex_1pct":2593376.523974403,"call_oi":0,"put_oi":106},{"strike":33200.0,"call_gex_1pct":0.0,"put_gex_1pct":-2867326.866103522,"net_gex_1pct":-2867326.866103522,"gross_gex_1pct":2867326.866103522,"call_oi":0,"put_oi":112},{"strike":33300.0,"call_gex_1pct":0.0,"put_gex_1pct":-4996284.557700184,"net_gex_1pct":-4996284.557700184,"gross_gex_1pct":4996284.557700184,"call_oi":0,"put_oi":188},{"strike":33400.0,"call_gex_1pct":0.0,"put_gex_1pct":-357077.72514208267,"net_gex_1pct":-357077.72514208267,"gross_gex_1pct":357077.72514208267,"call_oi":0,"put_oi":13},{"strike":33500.0,"call_gex_1pct":0.0,"put_gex_1pct":-541630.6727359481,"net_gex_1pct":-541630.6727359481,"gross_gex_1pct":541630.6727359481,"call_oi":0,"put_oi":19},{"strike":33600.0,"call_gex_1pct":0.0,"put_gex_1pct":-2564068.070844249,"net_gex_1pct":-2564068.070844249,"gross_gex_1pct":2564068.070844249,"call_oi":0,"put_oi":87},{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-554214.3184430844,"net_gex_1pct":-554214.3184430844,"gross_gex_1pct":554214.3184430844,"call_oi":0,"put_oi":18},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-320280.1090864965,"net_gex_1pct":-320280.1090864965,"gross_gex_1pct":320280.1090864965,"call_oi":0,"put_oi":10},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-332082.51985395007,"net_gex_1pct":-332082.51985395007,"gross_gex_1pct":332082.51985395007,"call_oi":0,"put_oi":10},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-11287999.462164877,"net_gex_1pct":-11287999.462164877,"gross_gex_1pct":11287999.462164877,"call_oi":0,"put_oi":324},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-539128.4418388226,"net_gex_1pct":-539128.4418388226,"gross_gex_1pct":539128.4418388226,"call_oi":0,"put_oi":15},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-1007717.8478259369,"net_gex_1pct":-1007717.8478259369,"gross_gex_1pct":1007717.8478259369,"call_oi":0,"put_oi":27},{"strike":34300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1277572.268547494,"net_gex_1pct":-1277572.268547494,"gross_gex_1pct":1277572.268547494,"call_oi":0,"put_oi":33},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-2126713.520504254,"net_gex_1pct":-2126713.520504254,"gross_gex_1pct":2126713.520504254,"call_oi":0,"put_oi":53},{"strike":34500.0,"call_gex_1pct":0.0,"put_gex_1pct":-15329019.618918207,"net_gex_1pct":-15329019.618918207,"gross_gex_1pct":15329019.618918207,"call_oi":0,"put_oi":367},{"strike":34600.0,"call_gex_1pct":0.0,"put_gex_1pct":-7315695.773521439,"net_gex_1pct":-7315695.773521439,"gross_gex_1pct":7315695.773521439,"call_oi":0,"put_oi":168},{"strike":34700.0,"call_gex_1pct":0.0,"put_gex_1pct":-3759153.2927649813,"net_gex_1pct":-3759153.2927649813,"gross_gex_1pct":3759153.2927649813,"call_oi":0,"put_oi":83},{"strike":34800.0,"call_gex_1pct":4819254.308015846,"put_gex_1pct":-3242445.0619501327,"net_gex_1pct":1576809.246065713,"gross_gex_1pct":8061699.369965978,"call_oi":415,"put_oi":69},{"strike":34900.0,"call_gex_1pct":4698455.939366796,"put_gex_1pct":-2629195.635163467,"net_gex_1pct":2069260.3042033291,"gross_gex_1pct":7327651.5745302625,"call_oi":211,"put_oi":54},{"strike":35000.0,"call_gex_1pct":82241807.04444396,"put_gex_1pct":-15393293.527282141,"net_gex_1pct":66848513.517161824,"gross_gex_1pct":97635100.57172611,"call_oi":2801,"put_oi":305},{"strike":35050.0,"call_gex_1pct":34298.76005285713,"put_gex_1pct":-617023.3497870147,"net_gex_1pct":-582724.5897341575,"gross_gex_1pct":651322.1098398718,"call_oi":1,"put_oi":12},{"strike":35100.0,"call_gex_1pct":4739336.289576542,"put_gex_1pct":-2355584.9067756347,"net_gex_1pct":2383751.382800907,"gross_gex_1pct":7094921.196352176,"call_oi":135,"put_oi":45},{"strike":35150.0,"call_gex_1pct":0.0,"put_gex_1pct":-1066038.320361187,"net_gex_1pct":-1066038.320361187,"gross_gex_1pct":1066038.320361187,"call_oi":0,"put_oi":20},{"strike":35200.0,"call_gex_1pct":100564917.31902528,"put_gex_1pct":-3907669.67842945,"net_gex_1pct":96657247.64059582,"gross_gex_1pct":104472586.99745473,"call_oi":2505,"put_oi":72},{"strike":35250.0,"call_gex_1pct":0.0,"put_gex_1pct":-331563.1829854407,"net_gex_1pct":-331563.1829854407,"gross_gex_1pct":331563.1829854407,"call_oi":0,"put_oi":6},{"strike":35300.0,"call_gex_1pct":5372855.185118007,"put_gex_1pct":-2361677.8212180543,"net_gex_1pct":3011177.3638999523,"gross_gex_1pct":7734533.006336061,"call_oi":120,"put_oi":42},{"strike":35350.0,"call_gex_1pct":48003.22487119875,"put_gex_1pct":-229064.43978193146,"net_gex_1pct":-181061.2149107327,"gross_gex_1pct":277067.6646531302,"call_oi":1,"put_oi":4},{"strike":35400.0,"call_gex_1pct":98615764.81589882,"put_gex_1pct":-7111425.660279874,"net_gex_1pct":91504339.15561895,"gross_gex_1pct":105727190.47617869,"call_oi":1937,"put_oi":122},{"strike":35450.0,"call_gex_1pct":0.0,"put_gex_1pct":-296425.5192075574,"net_gex_1pct":-296425.5192075574,"gross_gex_1pct":296425.5192075574,"call_oi":0,"put_oi":5},{"strike":35500.0,"call_gex_1pct":4443061.619139111,"put_gex_1pct":-6152411.99774129,"net_gex_1pct":-1709350.3786021797,"gross_gex_1pct":10595473.616880402,"call_oi":81,"put_oi":102},{"strike":35550.0,"call_gex_1pct":0.0,"put_gex_1pct":-982778.2207331567,"net_gex_1pct":-982778.2207331567,"gross_gex_1pct":982778.2207331567,"call_oi":0,"put_oi":16},{"strike":35600.0,"call_gex_1pct":66996956.50321316,"put_gex_1pct":-4373062.409439878,"net_gex_1pct":62623894.09377328,"gross_gex_1pct":71370018.91265304,"call_oi":1140,"put_oi":70},{"strike":35650.0,"call_gex_1pct":0.0,"put_gex_1pct":-190590.67302846644,"net_gex_1pct":-190590.67302846644,"gross_gex_1pct":190590.67302846644,"call_oi":0,"put_oi":3},{"strike":35700.0,"call_gex_1pct":2159261.1035158997,"put_gex_1pct":-2325536.861727728,"net_gex_1pct":-166275.7582118283,"gross_gex_1pct":4484797.965243628,"call_oi":34,"put_oi":36},{"strike":35750.0,"call_gex_1pct":197132.95926057996,"put_gex_1pct":-1117729.0294360074,"net_gex_1pct":-920596.0701754275,"gross_gex_1pct":1314861.9886965873,"call_oi":3,"put_oi":17},{"strike":35800.0,"call_gex_1pct":3837558.189557687,"put_gex_1pct":-3142990.587032919,"net_gex_1pct":694567.6025247681,"gross_gex_1pct":6980548.776590606,"call_oi":57,"put_oi":47},{"strike":35850.0,"call_gex_1pct":208500.23425308755,"put_gex_1pct":-1633642.5267272955,"net_gex_1pct":-1425142.292474208,"gross_gex_1pct":1842142.760980383,"call_oi":3,"put_oi":24},{"strike":35900.0,"call_gex_1pct":1217289.7459056745,"put_gex_1pct":-1243993.191886061,"net_gex_1pct":-26703.445980386576,"gross_gex_1pct":2461282.937791736,"call_oi":17,"put_oi":18},{"strike":35950.0,"call_gex_1pct":73653.95402217541,"put_gex_1pct":-1965222.048479557,"net_gex_1pct":-1891568.0944573816,"gross_gex_1pct":2038876.0025017324,"call_oi":1,"put_oi":28},{"strike":36000.0,"call_gex_1pct":4463749.789845778,"put_gex_1pct":-22993292.481187396,"net_gex_1pct":-18529542.691341616,"gross_gex_1pct":27457042.271033175,"call_oi":59,"put_oi":322},{"strike":36050.0,"call_gex_1pct":232868.4041364161,"put_gex_1pct":-2384181.593736807,"net_gex_1pct":-2151313.189600391,"gross_gex_1pct":2617049.997873223,"call_oi":3,"put_oi":33},{"strike":36100.0,"call_gex_1pct":1670756.2371889497,"put_gex_1pct":-4235508.028012198,"net_gex_1pct":-2564751.7908232487,"gross_gex_1pct":5906264.265201148,"call_oi":21,"put_oi":58},{"strike":36150.0,"call_gex_1pct":81474.62547856188,"put_gex_1pct":-1261998.4767344166,"net_gex_1pct":-1180523.8512558546,"gross_gex_1pct":1343473.1022129785,"call_oi":1,"put_oi":17},{"strike":36200.0,"call_gex_1pct":1167224.9315936365,"put_gex_1pct":-3178783.4991537216,"net_gex_1pct":-2011558.567560085,"gross_gex_1pct":4346008.430747358,"call_oi":14,"put_oi":42},{"strike":36250.0,"call_gex_1pct":85260.9273175997,"put_gex_1pct":-614893.9959017263,"net_gex_1pct":-529633.0685841267,"gross_gex_1pct":700154.923219326,"call_oi":1,"put_oi":8},{"strike":36300.0,"call_gex_1pct":958568.810053248,"put_gex_1pct":-702496.1516912276,"net_gex_1pct":256072.6583620204,"gross_gex_1pct":1661064.9617444756,"call_oi":11,"put_oi":9},{"strike":36350.0,"call_gex_1pct":89411.16922009009,"put_gex_1pct":-556268.6407038143,"net_gex_1pct":-466857.47148372425,"gross_gex_1pct":645679.8099239045,"call_oi":1,"put_oi":7},{"strike":36400.0,"call_gex_1pct":730841.1683887563,"put_gex_1pct":-885464.8836830162,"net_gex_1pct":-154623.71529425983,"gross_gex_1pct":1616306.0520717725,"call_oi":8,"put_oi":11},{"strike":36450.0,"call_gex_1pct":185588.35365271106,"put_gex_1pct":-1386925.1611049683,"net_gex_1pct":-1201336.8074522573,"gross_gex_1pct":1572513.5147576793,"call_oi":2,"put_oi":17},{"strike":36500.0,"call_gex_1pct":1609780.747743581,"put_gex_1pct":-11319276.702172663,"net_gex_1pct":-9709495.954429083,"gross_gex_1pct":12929057.449916244,"call_oi":17,"put_oi":137},{"strike":36550.0,"call_gex_1pct":96605.15606277269,"put_gex_1pct":-1256746.7280857884,"net_gex_1pct":-1160141.5720230157,"gross_gex_1pct":1353351.8841485612,"call_oi":1,"put_oi":15},{"strike":36600.0,"call_gex_1pct":1182408.0826489953,"put_gex_1pct":-1528153.848865574,"net_gex_1pct":-345745.76621657866,"gross_gex_1pct":2710561.9315145696,"call_oi":12,"put_oi":18},{"strike":36650.0,"call_gex_1pct":997493.4945828719,"put_gex_1pct":-1814412.127789194,"net_gex_1pct":-816918.6332063221,"gross_gex_1pct":2811905.6223720657,"call_oi":10,"put_oi":21},{"strike":36700.0,"call_gex_1pct":1220047.3578073836,"put_gex_1pct":-1749711.093225648,"net_gex_1pct":-529663.7354182643,"gross_gex_1pct":2969758.4510330316,"call_oi":12,"put_oi":20},{"strike":36750.0,"call_gex_1pct":207236.6847663841,"put_gex_1pct":-1233554.445881494,"net_gex_1pct":-1026317.76111511,"gross_gex_1pct":1440791.1306478782,"call_oi":2,"put_oi":14},{"strike":36800.0,"call_gex_1pct":1055954.7157352162,"put_gex_1pct":-2315664.9100855174,"net_gex_1pct":-1259710.1943503013,"gross_gex_1pct":3371619.6258207336,"call_oi":10,"put_oi":26},{"strike":36850.0,"call_gex_1pct":0.0,"put_gex_1pct":-990226.4638919745,"net_gex_1pct":-990226.4638919745,"gross_gex_1pct":990226.4638919745,"call_oi":0,"put_oi":11},{"strike":36900.0,"call_gex_1pct":1077133.5174689293,"put_gex_1pct":-4094176.4786724295,"net_gex_1pct":-3017042.9612035,"gross_gex_1pct":5171309.996141359,"call_oi":10,"put_oi":45},{"strike":36950.0,"call_gex_1pct":0.0,"put_gex_1pct":-926911.4907660299,"net_gex_1pct":-926911.4907660299,"gross_gex_1pct":926911.4907660299,"call_oi":0,"put_oi":10},{"strike":37000.0,"call_gex_1pct":6591986.190588256,"put_gex_1pct":-23704804.574090205,"net_gex_1pct":-17112818.383501947,"gross_gex_1pct":30296790.764678463,"call_oi":59,"put_oi":252},{"strike":37050.0,"call_gex_1pct":568997.5227328896,"put_gex_1pct":-375607.92252296483,"net_gex_1pct":193389.6002099248,"gross_gex_1pct":944605.4452558544,"call_oi":5,"put_oi":4},{"strike":37100.0,"call_gex_1pct":1287784.1961027258,"put_gex_1pct":-1518252.6307259295,"net_gex_1pct":-230468.4346232037,"gross_gex_1pct":2806036.8268286553,"call_oi":11,"put_oi":16},{"strike":37150.0,"call_gex_1pct":2337997.944812844,"put_gex_1pct":-582686.7075821307,"net_gex_1pct":1755311.2372307135,"gross_gex_1pct":2920684.6523949746,"call_oi":20,"put_oi":6},{"strike":37200.0,"call_gex_1pct":2828622.548504113,"put_gex_1pct":-1177794.1759065648,"net_gex_1pct":1650828.3725975484,"gross_gex_1pct":4006416.7244106783,"call_oi":24,"put_oi":12},{"strike":37250.0,"call_gex_1pct":593995.7528635876,"put_gex_1pct":-1573420.714688275,"net_gex_1pct":-979424.9618246874,"gross_gex_1pct":2167416.467551863,"call_oi":5,"put_oi":16},{"strike":37300.0,"call_gex_1pct":604911.4332117346,"put_gex_1pct":-1689435.2302766633,"net_gex_1pct":-1084523.7970649288,"gross_gex_1pct":2294346.663488398,"call_oi":5,"put_oi":17},{"strike":37350.0,"call_gex_1pct":2316412.305249328,"put_gex_1pct":-2340893.585838065,"net_gex_1pct":-24481.280588737223,"gross_gex_1pct":4657305.891087392,"call_oi":19,"put_oi":23},{"strike":37400.0,"call_gex_1pct":7861765.7257026145,"put_gex_1pct":-1307801.3447374369,"net_gex_1pct":6553964.380965178,"gross_gex_1pct":9169567.070440052,"call_oi":64,"put_oi":13},{"strike":37450.0,"call_gex_1pct":13636781.800467407,"put_gex_1pct":-1736003.0278867353,"net_gex_1pct":11900778.772580672,"gross_gex_1pct":15372784.828354143,"call_oi":109,"put_oi":17},{"strike":37500.0,"call_gex_1pct":329593778.5624206,"put_gex_1pct":-7840209.215586607,"net_gex_1pct":321753569.346834,"gross_gex_1pct":337433987.7780072,"call_oi":2615,"put_oi":77},{"strike":37550.0,"call_gex_1pct":20568765.78589899,"put_gex_1pct":-207663.78893850307,"net_gex_1pct":20361101.996960487,"gross_gex_1pct":20776429.574837495,"call_oi":162,"put_oi":2},{"strike":37600.0,"call_gex_1pct":447885517.71370256,"put_gex_1pct":-5407247.187010874,"net_gex_1pct":442478270.5266917,"gross_gex_1pct":453292764.90071344,"call_oi":3502,"put_oi":52},{"strike":37650.0,"call_gex_1pct":13139756.107678335,"put_gex_1pct":-1385326.6129212552,"net_gex_1pct":11754429.49475708,"gross_gex_1pct":14525082.72059959,"call_oi":102,"put_oi":13},{"strike":37700.0,"call_gex_1pct":15139056.104754683,"put_gex_1pct":-628558.8897240005,"net_gex_1pct":14510497.215030681,"gross_gex_1pct":15767614.994478684,"call_oi":118,"put_oi":6},{"strike":37750.0,"call_gex_1pct":27521775.428306237,"put_gex_1pct":-638201.0337315741,"net_gex_1pct":26883574.394574665,"gross_gex_1pct":28159976.46203781,"call_oi":213,"put_oi":6},{"strike":37800.0,"call_gex_1pct":449090104.3267396,"put_gex_1pct":-4937264.534850846,"net_gex_1pct":444152839.7918888,"gross_gex_1pct":454027368.86159045,"call_oi":3412,"put_oi":47},{"strike":37850.0,"call_gex_1pct":21509430.720716268,"put_gex_1pct":-1690787.2292062715,"net_gex_1pct":19818643.491509996,"gross_gex_1pct":23200217.94992254,"call_oi":166,"put_oi":16},{"strike":37900.0,"call_gex_1pct":64069403.68331979,"put_gex_1pct":-9735030.39834772,"net_gex_1pct":54334373.28497207,"gross_gex_1pct":73804434.08166751,"call_oi":491,"put_oi":92},{"strike":37950.0,"call_gex_1pct":1689037.5401293386,"put_gex_1pct":-644641.1023456813,"net_gex_1pct":1044396.4377836573,"gross_gex_1pct":2333678.64247502,"call_oi":13,"put_oi":6},{"strike":38000.0,"call_gex_1pct":19756370.34148538,"put_gex_1pct":-12625452.730850387,"net_gex_1pct":7130917.610634994,"gross_gex_1pct":32381823.07233577,"call_oi":151,"put_oi":119},{"strike":38050.0,"call_gex_1pct":1976360.0293063277,"put_gex_1pct":-533637.648620643,"net_gex_1pct":1442722.3806856847,"gross_gex_1pct":2509997.6779269706,"call_oi":15,"put_oi":5},{"strike":38100.0,"call_gex_1pct":3240289.953711281,"put_gex_1pct":-875184.6215604363,"net_gex_1pct":2365105.332150845,"gross_gex_1pct":4115474.5752717173,"call_oi":24,"put_oi":8},{"strike":38150.0,"call_gex_1pct":1727210.5560069662,"put_gex_1pct":-642050.1631807246,"net_gex_1pct":1085160.3928262414,"gross_gex_1pct":2369260.719187691,"call_oi":13,"put_oi":6},{"strike":38200.0,"call_gex_1pct":5202056.187780479,"put_gex_1pct":-861173.4041281061,"net_gex_1pct":4340882.783652373,"gross_gex_1pct":6063229.591908585,"call_oi":40,"put_oi":8},{"strike":38250.0,"call_gex_1pct":9990808.065406749,"put_gex_1pct":0.0,"net_gex_1pct":9990808.065406749,"gross_gex_1pct":9990808.065406749,"call_oi":75,"put_oi":0},{"strike":38300.0,"call_gex_1pct":4907078.6699873535,"put_gex_1pct":-2158573.022164038,"net_gex_1pct":2748505.6478233156,"gross_gex_1pct":7065651.692151392,"call_oi":37,"put_oi":20},{"strike":38350.0,"call_gex_1pct":3169038.1255506515,"put_gex_1pct":-109597.47220695336,"net_gex_1pct":3059440.653343698,"gross_gex_1pct":3278635.597757605,"call_oi":24,"put_oi":1},{"strike":38400.0,"call_gex_1pct":2644293.4483346073,"put_gex_1pct":-750497.5993782117,"net_gex_1pct":1893795.8489563956,"gross_gex_1pct":3394791.0477128187,"call_oi":20,"put_oi":7},{"strike":38450.0,"call_gex_1pct":1997104.4666308481,"put_gex_1pct":-1402046.8529959363,"net_gex_1pct":595057.6136349118,"gross_gex_1pct":3399151.3196267844,"call_oi":15,"put_oi":13},{"strike":38500.0,"call_gex_1pct":7820665.306787953,"put_gex_1pct":-2982311.160078,"net_gex_1pct":4838354.1467099525,"gross_gex_1pct":10802976.466865953,"call_oi":59,"put_oi":28},{"strike":38550.0,"call_gex_1pct":2243510.644732027,"put_gex_1pct":-109136.98032064515,"net_gex_1pct":2134373.664411382,"gross_gex_1pct":2352647.625052672,"call_oi":17,"put_oi":1},{"strike":38600.0,"call_gex_1pct":4598721.801632979,"put_gex_1pct":-1174616.872747611,"net_gex_1pct":3424104.9288853677,"gross_gex_1pct":5773338.67438059,"call_oi":35,"put_oi":11},{"strike":38650.0,"call_gex_1pct":1438966.1708339856,"put_gex_1pct":-106431.95154725733,"net_gex_1pct":1332534.2192867282,"gross_gex_1pct":1545398.122381243,"call_oi":11,"put_oi":1},{"strike":38700.0,"call_gex_1pct":11786191.895587023,"put_gex_1pct":-1379065.1033083745,"net_gex_1pct":10407126.79227865,"gross_gex_1pct":13165256.998895397,"call_oi":92,"put_oi":13},{"strike":38750.0,"call_gex_1pct":3094883.4678022396,"put_gex_1pct":-845862.7222313099,"net_gex_1pct":2249020.7455709297,"gross_gex_1pct":3940746.1900335494,"call_oi":24,"put_oi":8},{"strike":38800.0,"call_gex_1pct":4108269.198290482,"put_gex_1pct":-948457.6907532229,"net_gex_1pct":3159811.5075372593,"gross_gex_1pct":5056726.889043706,"call_oi":32,"put_oi":9},{"strike":38850.0,"call_gex_1pct":1533722.3627728322,"put_gex_1pct":-1041085.09651058,"net_gex_1pct":492637.2662622521,"gross_gex_1pct":2574807.4592834124,"call_oi":12,"put_oi":10},{"strike":38900.0,"call_gex_1pct":3290395.920465795,"put_gex_1pct":-1245202.8744267414,"net_gex_1pct":2045193.0460390535,"gross_gex_1pct":4535598.7948925365,"call_oi":26,"put_oi":12},{"strike":38950.0,"call_gex_1pct":3884729.9102939744,"put_gex_1pct":-310272.29621372453,"net_gex_1pct":3574457.61408025,"gross_gex_1pct":4195002.206507699,"call_oi":31,"put_oi":3},{"strike":39000.0,"call_gex_1pct":26650261.02910805,"put_gex_1pct":-8349433.696266443,"net_gex_1pct":18300827.33284161,"gross_gex_1pct":34999694.72537449,"call_oi":217,"put_oi":81},{"strike":39050.0,"call_gex_1pct":3458284.478048972,"put_gex_1pct":-1027321.7656153702,"net_gex_1pct":2430962.7124336017,"gross_gex_1pct":4485606.243664342,"call_oi":28,"put_oi":10},{"strike":39100.0,"call_gex_1pct":5992431.563064785,"put_gex_1pct":-710570.3882407208,"net_gex_1pct":5281861.174824064,"gross_gex_1pct":6703001.951305506,"call_oi":49,"put_oi":7},{"strike":39150.0,"call_gex_1pct":25626539.338213183,"put_gex_1pct":-596878.7341820678,"net_gex_1pct":25029660.604031116,"gross_gex_1pct":26223418.07239525,"call_oi":211,"put_oi":6},{"strike":39200.0,"call_gex_1pct":13989821.107535029,"put_gex_1pct":-604874.4974247062,"net_gex_1pct":13384946.610110322,"gross_gex_1pct":14594695.604959736,"call_oi":116,"put_oi":6},{"strike":39250.0,"call_gex_1pct":3715541.5996976574,"put_gex_1pct":-199247.37640273548,"net_gex_1pct":3516294.223294922,"gross_gex_1pct":3914788.9761003926,"call_oi":31,"put_oi":2},{"strike":39300.0,"call_gex_1pct":6029884.709913969,"put_gex_1pct":-1588301.3151630352,"net_gex_1pct":4441583.394750934,"gross_gex_1pct":7618186.025077004,"call_oi":50,"put_oi":16},{"strike":39350.0,"call_gex_1pct":2825833.117481151,"put_gex_1pct":-4963219.939832507,"net_gex_1pct":-2137386.8223513556,"gross_gex_1pct":7789053.057313658,"call_oi":24,"put_oi":51},{"strike":39400.0,"call_gex_1pct":2990437.250394301,"put_gex_1pct":-3909773.9700420415,"net_gex_1pct":-919336.7196477405,"gross_gex_1pct":6900211.220436342,"call_oi":26,"put_oi":40},{"strike":39450.0,"call_gex_1pct":3563595.4359086924,"put_gex_1pct":-3115933.9342432185,"net_gex_1pct":447661.5016654739,"gross_gex_1pct":6679529.370151911,"call_oi":31,"put_oi":32},{"strike":39500.0,"call_gex_1pct":10764822.171282127,"put_gex_1pct":-5004073.882472566,"net_gex_1pct":5760748.288809561,"gross_gex_1pct":15768896.053754695,"call_oi":94,"put_oi":52},{"strike":39550.0,"call_gex_1pct":4052206.6250927914,"put_gex_1pct":-475557.5895067253,"net_gex_1pct":3576649.035586066,"gross_gex_1pct":4527764.214599516,"call_oi":36,"put_oi":5},{"strike":39600.0,"call_gex_1pct":4555392.826115631,"put_gex_1pct":-663075.8248083057,"net_gex_1pct":3892317.001307325,"gross_gex_1pct":5218468.650923937,"call_oi":41,"put_oi":7},{"strike":39650.0,"call_gex_1pct":2958199.1097017974,"put_gex_1pct":-93620.50588550112,"net_gex_1pct":2864578.6038162964,"gross_gex_1pct":3051819.6155872983,"call_oi":27,"put_oi":1},{"strike":39700.0,"call_gex_1pct":3351264.7787464987,"put_gex_1pct":-1758130.2439791257,"net_gex_1pct":1593134.534767373,"gross_gex_1pct":5109395.022725625,"call_oi":31,"put_oi":19},{"strike":39750.0,"call_gex_1pct":4049287.936427324,"put_gex_1pct":-182924.225377419,"net_gex_1pct":3866363.711049905,"gross_gex_1pct":4232212.161804743,"call_oi":38,"put_oi":2},{"strike":39800.0,"call_gex_1pct":6120647.316063701,"put_gex_1pct":-1274652.469741377,"net_gex_1pct":4845994.846322324,"gross_gex_1pct":7395299.785805078,"call_oi":58,"put_oi":14},{"strike":39850.0,"call_gex_1pct":1757608.1304862988,"put_gex_1pct":-899845.7557417772,"net_gex_1pct":857762.3747445216,"gross_gex_1pct":2657453.886228076,"call_oi":17,"put_oi":10},{"strike":39900.0,"call_gex_1pct":3767682.190844203,"put_gex_1pct":-978297.3422497237,"net_gex_1pct":2789384.8485944793,"gross_gex_1pct":4745979.5330939265,"call_oi":37,"put_oi":11},{"strike":39950.0,"call_gex_1pct":3408700.54496138,"put_gex_1pct":-615302.1000902324,"net_gex_1pct":2793398.444871147,"gross_gex_1pct":4024002.6450516125,"call_oi":34,"put_oi":7},{"strike":40000.0,"call_gex_1pct":95166065.38349238,"put_gex_1pct":-3822551.926899626,"net_gex_1pct":91343513.45659275,"gross_gex_1pct":98988617.310392,"call_oi":962,"put_oi":44},{"strike":40050.0,"call_gex_1pct":2518411.0798970764,"put_gex_1pct":-858628.4460945795,"net_gex_1pct":1659782.6338024968,"gross_gex_1pct":3377039.525991656,"call_oi":26,"put_oi":10},{"strike":40100.0,"call_gex_1pct":4008746.8698294987,"put_gex_1pct":-1272890.7548807005,"net_gex_1pct":2735856.114948798,"gross_gex_1pct":5281637.624710199,"call_oi":42,"put_oi":15},{"strike":40150.0,"call_gex_1pct":2998259.634514728,"put_gex_1pct":-838648.9225694909,"net_gex_1pct":2159610.711945237,"gross_gex_1pct":3836908.557084219,"call_oi":32,"put_oi":10},{"strike":40200.0,"call_gex_1pct":7527138.47261826,"put_gex_1pct":-1077420.0639839047,"net_gex_1pct":6449718.408634355,"gross_gex_1pct":8604558.536602166,"call_oi":82,"put_oi":13},{"strike":40250.0,"call_gex_1pct":2157306.354498077,"put_gex_1pct":-1064689.596600139,"net_gex_1pct":1092616.7578979381,"gross_gex_1pct":3221995.951098216,"call_oi":24,"put_oi":13},{"strike":40300.0,"call_gex_1pct":5728717.213372974,"put_gex_1pct":-724415.6506779161,"net_gex_1pct":5004301.562695058,"gross_gex_1pct":6453132.864050889,"call_oi":65,"put_oi":9},{"strike":40350.0,"call_gex_1pct":2332380.571587641,"put_gex_1pct":-397719.7948512024,"net_gex_1pct":1934660.7767364383,"gross_gex_1pct":2730100.3664388433,"call_oi":27,"put_oi":5},{"strike":40400.0,"call_gex_1pct":3214895.259171598,"put_gex_1pct":-2200854.932308279,"net_gex_1pct":1014040.3268633191,"gross_gex_1pct":5415750.191479877,"call_oi":38,"put_oi":28},{"strike":40450.0,"call_gex_1pct":1740587.4867242116,"put_gex_1pct":-388318.6680942066,"net_gex_1pct":1352268.818630005,"gross_gex_1pct":2128906.1548184184,"call_oi":21,"put_oi":5},{"strike":40500.0,"call_gex_1pct":24910543.922370687,"put_gex_1pct":-916499.988972562,"net_gex_1pct":23994043.933398124,"gross_gex_1pct":25827043.91134325,"call_oi":307,"put_oi":12},{"strike":40550.0,"call_gex_1pct":2143872.9580473257,"put_gex_1pct":0.0,"net_gex_1pct":2143872.9580473257,"gross_gex_1pct":2143872.9580473257,"call_oi":27,"put_oi":0},{"strike":40600.0,"call_gex_1pct":3417239.8910650625,"put_gex_1pct":-74552.38369446677,"net_gex_1pct":3342687.507370596,"gross_gex_1pct":3491792.274759529,"call_oi":44,"put_oi":1},{"strike":40650.0,"call_gex_1pct":2117740.0185091468,"put_gex_1pct":-73348.52856775072,"net_gex_1pct":2044391.489941396,"gross_gex_1pct":2191088.5470768977,"call_oi":28,"put_oi":1},{"strike":40700.0,"call_gex_1pct":2814478.687245743,"put_gex_1pct":-217379.3022301012,"net_gex_1pct":2597099.385015642,"gross_gex_1pct":3031857.989475844,"call_oi":38,"put_oi":3},{"strike":40750.0,"call_gex_1pct":1522654.465083174,"put_gex_1pct":0.0,"net_gex_1pct":1522654.465083174,"gross_gex_1pct":1522654.465083174,"call_oi":21,"put_oi":0},{"strike":40800.0,"call_gex_1pct":4032978.6267965687,"put_gex_1pct":-422661.92996653053,"net_gex_1pct":3610316.696830038,"gross_gex_1pct":4455640.5567630995,"call_oi":57,"put_oi":6},{"strike":40850.0,"call_gex_1pct":2073000.0990654868,"put_gex_1pct":0.0,"net_gex_1pct":2073000.0990654868,"gross_gex_1pct":2073000.0990654868,"call_oi":30,"put_oi":0},{"strike":40900.0,"call_gex_1pct":2426104.065397988,"put_gex_1pct":-273991.06723956094,"net_gex_1pct":2152112.998158427,"gross_gex_1pct":2700095.132637549,"call_oi":36,"put_oi":4},{"strike":40950.0,"call_gex_1pct":1512231.6602070231,"put_gex_1pct":0.0,"net_gex_1pct":1512231.6602070231,"gross_gex_1pct":1512231.6602070231,"call_oi":23,"put_oi":0},{"strike":41000.0,"call_gex_1pct":51468584.86293677,"put_gex_1pct":-333081.58096621145,"net_gex_1pct":51135503.28197056,"gross_gex_1pct":51801666.443902984,"call_oi":814,"put_oi":5},{"strike":41050.0,"call_gex_1pct":1783726.8168235272,"put_gex_1pct":0.0,"net_gex_1pct":1783726.8168235272,"gross_gex_1pct":1783726.8168235272,"call_oi":29,"put_oi":0},{"strike":41100.0,"call_gex_1pct":6660916.277093109,"put_gex_1pct":0.0,"net_gex_1pct":6660916.277093109,"gross_gex_1pct":6660916.277093109,"call_oi":111,"put_oi":0},{"strike":41150.0,"call_gex_1pct":2991065.585794487,"put_gex_1pct":-127921.53294580874,"net_gex_1pct":2863144.052848678,"gross_gex_1pct":3118987.118740296,"call_oi":51,"put_oi":2},{"strike":41200.0,"call_gex_1pct":7623496.823682904,"put_gex_1pct":0.0,"net_gex_1pct":7623496.823682904,"gross_gex_1pct":7623496.823682904,"call_oi":133,"put_oi":0},{"strike":41250.0,"call_gex_1pct":1344485.9862526313,"put_gex_1pct":-124401.8008158106,"net_gex_1pct":1220084.1854368206,"gross_gex_1pct":1468887.787068442,"call_oi":24,"put_oi":2},{"strike":41300.0,"call_gex_1pct":2217494.400629923,"put_gex_1pct":-490454.4073259631,"net_gex_1pct":1727039.9933039602,"gross_gex_1pct":2707948.8079558862,"call_oi":41,"put_oi":8},{"strike":41350.0,"call_gex_1pct":688510.4706178636,"put_gex_1pct":-60488.315335791056,"net_gex_1pct":628022.1552820725,"gross_gex_1pct":748998.7859536547,"call_oi":13,"put_oi":1},{"strike":41400.0,"call_gex_1pct":1285820.804891485,"put_gex_1pct":-357797.76433371194,"net_gex_1pct":928023.0405577731,"gross_gex_1pct":1643618.569225197,"call_oi":25,"put_oi":6},{"strike":41450.0,"call_gex_1pct":2145658.061664907,"put_gex_1pct":-117600.51741536752,"net_gex_1pct":2028057.5442495393,"gross_gex_1pct":2263258.5790802743,"call_oi":43,"put_oi":2},{"strike":41500.0,"call_gex_1pct":14979205.209727203,"put_gex_1pct":-57999.97214639267,"net_gex_1pct":14921205.237580812,"gross_gex_1pct":15037205.181873595,"call_oi":312,"put_oi":1},{"strike":41550.0,"call_gex_1pct":936103.3596247004,"put_gex_1pct":-57202.60395823804,"net_gex_1pct":878900.7556664624,"gross_gex_1pct":993305.9635829384,"call_oi":20,"put_oi":1},{"strike":41600.0,"call_gex_1pct":4470692.563384512,"put_gex_1pct":-225702.95793964562,"net_gex_1pct":4244989.605444867,"gross_gex_1pct":4696395.521324158,"call_oi":98,"put_oi":4},{"strike":41650.0,"call_gex_1pct":486825.96115073963,"put_gex_1pct":-55640.028289913374,"net_gex_1pct":431185.93286082626,"gross_gex_1pct":542465.989440653,"call_oi":11,"put_oi":1},{"strike":41700.0,"call_gex_1pct":1274272.449003862,"put_gex_1pct":-768537.2780252019,"net_gex_1pct":505735.1709786601,"gross_gex_1pct":2042809.7270290637,"call_oi":30,"put_oi":14},{"strike":41750.0,"call_gex_1pct":332274.5136567428,"put_gex_1pct":-54169.62136603044,"net_gex_1pct":278104.8922907124,"gross_gex_1pct":386444.13502277323,"call_oi":8,"put_oi":1},{"strike":41800.0,"call_gex_1pct":2544836.099758136,"put_gex_1pct":-266975.70908312174,"net_gex_1pct":2277860.3906750144,"gross_gex_1pct":2811811.808841258,"call_oi":63,"put_oi":5},{"strike":41850.0,"call_gex_1pct":351309.7081938176,"put_gex_1pct":0.0,"net_gex_1pct":351309.7081938176,"gross_gex_1pct":351309.7081938176,"call_oi":9,"put_oi":0},{"strike":41900.0,"call_gex_1pct":1895516.6623046761,"put_gex_1pct":0.0,"net_gex_1pct":1895516.6623046761,"gross_gex_1pct":1895516.6623046761,"call_oi":50,"put_oi":0},{"strike":41950.0,"call_gex_1pct":2082977.9944978172,"put_gex_1pct":0.0,"net_gex_1pct":2082977.9944978172,"gross_gex_1pct":2082977.9944978172,"call_oi":57,"put_oi":0},{"strike":42000.0,"call_gex_1pct":31575579.863852896,"put_gex_1pct":0.0,"net_gex_1pct":31575579.863852896,"gross_gex_1pct":31575579.863852896,"call_oi":905,"put_oi":0},{"strike":42050.0,"call_gex_1pct":1264741.9835861193,"put_gex_1pct":0.0,"net_gex_1pct":1264741.9835861193,"gross_gex_1pct":1264741.9835861193,"call_oi":37,"put_oi":0},{"strike":42100.0,"call_gex_1pct":1081888.8688980697,"put_gex_1pct":0.0,"net_gex_1pct":1081888.8688980697,"gross_gex_1pct":1081888.8688980697,"call_oi":33,"put_oi":0},{"strike":42150.0,"call_gex_1pct":1566292.658802817,"put_gex_1pct":0.0,"net_gex_1pct":1566292.658802817,"gross_gex_1pct":1566292.658802817,"call_oi":49,"put_oi":0},{"strike":42200.0,"call_gex_1pct":1884241.120616933,"put_gex_1pct":-48143.85710212233,"net_gex_1pct":1836097.2635148107,"gross_gex_1pct":1932384.9777190555,"call_oi":62,"put_oi":1},{"strike":42250.0,"call_gex_1pct":1035660.7198784138,"put_gex_1pct":0.0,"net_gex_1pct":1035660.7198784138,"gross_gex_1pct":1035660.7198784138,"call_oi":35,"put_oi":0},{"strike":42300.0,"call_gex_1pct":633653.8584350748,"put_gex_1pct":0.0,"net_gex_1pct":633653.8584350748,"gross_gex_1pct":633653.8584350748,"call_oi":22,"put_oi":0},{"strike":42350.0,"call_gex_1pct":27171.759939074385,"put_gex_1pct":0.0,"net_gex_1pct":27171.759939074385,"gross_gex_1pct":27171.759939074385,"call_oi":1,"put_oi":0},{"strike":42400.0,"call_gex_1pct":594408.8186001588,"put_gex_1pct":-45741.38861863303,"net_gex_1pct":548667.4299815258,"gross_gex_1pct":640150.2072187918,"call_oi":23,"put_oi":1},{"strike":42450.0,"call_gex_1pct":323378.603292275,"put_gex_1pct":0.0,"net_gex_1pct":323378.603292275,"gross_gex_1pct":323378.603292275,"call_oi":13,"put_oi":0},{"strike":42500.0,"call_gex_1pct":5874688.343102475,"put_gex_1pct":-88994.0122353741,"net_gex_1pct":5785694.3308671005,"gross_gex_1pct":5963682.355337849,"call_oi":250,"put_oi":2},{"strike":42550.0,"call_gex_1pct":22075.234965179763,"put_gex_1pct":0.0,"net_gex_1pct":22075.234965179763,"gross_gex_1pct":22075.234965179763,"call_oi":1,"put_oi":0},{"strike":42600.0,"call_gex_1pct":463401.2586011013,"put_gex_1pct":0.0,"net_gex_1pct":463401.2586011013,"gross_gex_1pct":463401.2586011013,"call_oi":22,"put_oi":0},{"strike":42650.0,"call_gex_1pct":501730.5211144625,"put_gex_1pct":0.0,"net_gex_1pct":501730.5211144625,"gross_gex_1pct":501730.5211144625,"call_oi":26,"put_oi":0},{"strike":42700.0,"call_gex_1pct":532119.8296712292,"put_gex_1pct":0.0,"net_gex_1pct":532119.8296712292,"gross_gex_1pct":532119.8296712292,"call_oi":28,"put_oi":0},{"strike":42750.0,"call_gex_1pct":445339.9624308662,"put_gex_1pct":-41814.15089476088,"net_gex_1pct":403525.81153610535,"gross_gex_1pct":487154.11332562706,"call_oi":26,"put_oi":1},{"strike":42800.0,"call_gex_1pct":768527.8512867809,"put_gex_1pct":-41351.638837190665,"net_gex_1pct":727176.2124495902,"gross_gex_1pct":809879.4901239716,"call_oi":51,"put_oi":1},{"strike":42850.0,"call_gex_1pct":170220.81634673956,"put_gex_1pct":0.0,"net_gex_1pct":170220.81634673956,"gross_gex_1pct":170220.81634673956,"call_oi":12,"put_oi":0},{"strike":42900.0,"call_gex_1pct":318862.8463308877,"put_gex_1pct":0.0,"net_gex_1pct":318862.8463308877,"gross_gex_1pct":318862.8463308877,"call_oi":24,"put_oi":0},{"strike":42950.0,"call_gex_1pct":222492.7501181081,"put_gex_1pct":-40020.11036360875,"net_gex_1pct":182472.63975449934,"gross_gex_1pct":262512.8604817168,"call_oi":17,"put_oi":1},{"strike":43000.0,"call_gex_1pct":68023378.88395505,"put_gex_1pct":-158376.12699639986,"net_gex_1pct":67865002.75695865,"gross_gex_1pct":68181755.01095144,"call_oi":5874,"put_oi":4},{"strike":43050.0,"call_gex_1pct":398823.74503421376,"put_gex_1pct":-155655.60223568763,"net_gex_1pct":243168.14279852613,"gross_gex_1pct":554479.3472699014,"call_oi":37,"put_oi":4},{"strike":43100.0,"call_gex_1pct":58195.85835859911,"put_gex_1pct":-77007.07100495441,"net_gex_1pct":-18811.212646355307,"gross_gex_1pct":135202.92936355353,"call_oi":6,"put_oi":2},{"strike":43150.0,"call_gex_1pct":218758.4664313933,"put_gex_1pct":0.0,"net_gex_1pct":218758.4664313933,"gross_gex_1pct":218758.4664313933,"call_oi":24,"put_oi":0},{"strike":43200.0,"call_gex_1pct":180984.5677295341,"put_gex_1pct":-37706.73612664166,"net_gex_1pct":143277.83160289243,"gross_gex_1pct":218691.30385617574,"call_oi":21,"put_oi":1},{"strike":43250.0,"call_gex_1pct":7004.707781301474,"put_gex_1pct":-37319.855430322204,"net_gex_1pct":-30315.14764902073,"gross_gex_1pct":44324.56321162368,"call_oi":1,"put_oi":1},{"strike":43300.0,"call_gex_1pct":370515.961243026,"put_gex_1pct":-147761.48012133164,"net_gex_1pct":222754.48112169438,"gross_gex_1pct":518277.44136435766,"call_oi":63,"put_oi":4},{"strike":43350.0,"call_gex_1pct":34775.618182826816,"put_gex_1pct":-73136.15304279861,"net_gex_1pct":-38360.5348599718,"gross_gex_1pct":107911.77122562543,"call_oi":6,"put_oi":2},{"strike":43400.0,"call_gex_1pct":209025.04060589283,"put_gex_1pct":0.0,"net_gex_1pct":209025.04060589283,"gross_gex_1pct":209025.04060589283,"call_oi":41,"put_oi":0},{"strike":43450.0,"call_gex_1pct":38138.541775305996,"put_gex_1pct":0.0,"net_gex_1pct":38138.541775305996,"gross_gex_1pct":38138.541775305996,"call_oi":8,"put_oi":0},{"strike":43500.0,"call_gex_1pct":1751835.8601243377,"put_gex_1pct":0.0,"net_gex_1pct":1751835.8601243377,"gross_gex_1pct":1751835.8601243377,"call_oi":395,"put_oi":0},{"strike":43550.0,"call_gex_1pct":8475.638913009967,"put_gex_1pct":0.0,"net_gex_1pct":8475.638913009967,"gross_gex_1pct":8475.638913009967,"call_oi":2,"put_oi":0},{"strike":43600.0,"call_gex_1pct":40427.39274540451,"put_gex_1pct":0.0,"net_gex_1pct":40427.39274540451,"gross_gex_1pct":40427.39274540451,"call_oi":10,"put_oi":0},{"strike":43650.0,"call_gex_1pct":73141.54126530797,"put_gex_1pct":0.0,"net_gex_1pct":73141.54126530797,"gross_gex_1pct":73141.54126530797,"call_oi":19,"put_oi":0},{"strike":43700.0,"call_gex_1pct":18982.490926447823,"put_gex_1pct":0.0,"net_gex_1pct":18982.490926447823,"gross_gex_1pct":18982.490926447823,"call_oi":5,"put_oi":0},{"strike":43750.0,"call_gex_1pct":14431.95558944908,"put_gex_1pct":0.0,"net_gex_1pct":14431.95558944908,"gross_gex_1pct":14431.95558944908,"call_oi":4,"put_oi":0},{"strike":43800.0,"call_gex_1pct":58153.68578711418,"put_gex_1pct":0.0,"net_gex_1pct":58153.68578711418,"gross_gex_1pct":58153.68578711418,"call_oi":17,"put_oi":0},{"strike":43850.0,"call_gex_1pct":6469.350900081161,"put_gex_1pct":0.0,"net_gex_1pct":6469.350900081161,"gross_gex_1pct":6469.350900081161,"call_oi":2,"put_oi":0},{"strike":43900.0,"call_gex_1pct":12197.219865051746,"put_gex_1pct":0.0,"net_gex_1pct":12197.219865051746,"gross_gex_1pct":12197.219865051746,"call_oi":4,"put_oi":0},{"strike":43950.0,"call_gex_1pct":11457.47072986212,"put_gex_1pct":0.0,"net_gex_1pct":11457.47072986212,"gross_gex_1pct":11457.47072986212,"call_oi":4,"put_oi":0},{"strike":44000.0,"call_gex_1pct":2371355.647518653,"put_gex_1pct":0.0,"net_gex_1pct":2371355.647518653,"gross_gex_1pct":2371355.647518653,"call_oi":885,"put_oi":0},{"strike":44050.0,"call_gex_1pct":144998.84590188478,"put_gex_1pct":-32012.74965793272,"net_gex_1pct":112986.09624395205,"gross_gex_1pct":177011.5955598175,"call_oi":62,"put_oi":1},{"strike":44100.0,"call_gex_1pct":39239.76305916949,"put_gex_1pct":0.0,"net_gex_1pct":39239.76305916949,"gross_gex_1pct":39239.76305916949,"call_oi":17,"put_oi":0},{"strike":44150.0,"call_gex_1pct":61501.70508618266,"put_gex_1pct":0.0,"net_gex_1pct":61501.70508618266,"gross_gex_1pct":61501.70508618266,"call_oi":29,"put_oi":0},{"strike":44200.0,"call_gex_1pct":29309.36294685784,"put_gex_1pct":0.0,"net_gex_1pct":29309.36294685784,"gross_gex_1pct":29309.36294685784,"call_oi":14,"put_oi":0},{"strike":44250.0,"call_gex_1pct":17158.531919195684,"put_gex_1pct":0.0,"net_gex_1pct":17158.531919195684,"gross_gex_1pct":17158.531919195684,"call_oi":9,"put_oi":0},{"strike":44350.0,"call_gex_1pct":1694.8627413833422,"put_gex_1pct":0.0,"net_gex_1pct":1694.8627413833422,"gross_gex_1pct":1694.8627413833422,"call_oi":1,"put_oi":0},{"strike":44400.0,"call_gex_1pct":27057.57968242473,"put_gex_1pct":0.0,"net_gex_1pct":27057.57968242473,"gross_gex_1pct":27057.57968242473,"call_oi":18,"put_oi":0},{"strike":44450.0,"call_gex_1pct":10391.7113788201,"put_gex_1pct":0.0,"net_gex_1pct":10391.7113788201,"gross_gex_1pct":10391.7113788201,"call_oi":7,"put_oi":0},{"strike":44500.0,"call_gex_1pct":20527.467029408977,"put_gex_1pct":0.0,"net_gex_1pct":20527.467029408977,"gross_gex_1pct":20527.467029408977,"call_oi":14,"put_oi":0},{"strike":44550.0,"call_gex_1pct":6369.367481213756,"put_gex_1pct":0.0,"net_gex_1pct":6369.367481213756,"gross_gex_1pct":6369.367481213756,"call_oi":5,"put_oi":0},{"strike":44600.0,"call_gex_1pct":46560.06662645945,"put_gex_1pct":0.0,"net_gex_1pct":46560.06662645945,"gross_gex_1pct":46560.06662645945,"call_oi":37,"put_oi":0},{"strike":44650.0,"call_gex_1pct":4972.802666294823,"put_gex_1pct":0.0,"net_gex_1pct":4972.802666294823,"gross_gex_1pct":4972.802666294823,"call_oi":4,"put_oi":0},{"strike":44700.0,"call_gex_1pct":1047.9208880371884,"put_gex_1pct":0.0,"net_gex_1pct":1047.9208880371884,"gross_gex_1pct":1047.9208880371884,"call_oi":1,"put_oi":0},{"strike":44750.0,"call_gex_1pct":2070.848936143219,"put_gex_1pct":0.0,"net_gex_1pct":2070.848936143219,"gross_gex_1pct":2070.848936143219,"call_oi":2,"put_oi":0},{"strike":44800.0,"call_gex_1pct":49112.45471020888,"put_gex_1pct":0.0,"net_gex_1pct":49112.45471020888,"gross_gex_1pct":49112.45471020888,"call_oi":48,"put_oi":0},{"strike":44850.0,"call_gex_1pct":1643.5176052385232,"put_gex_1pct":0.0,"net_gex_1pct":1643.5176052385232,"gross_gex_1pct":1643.5176052385232,"call_oi":2,"put_oi":0},{"strike":44900.0,"call_gex_1pct":5684.95281159846,"put_gex_1pct":0.0,"net_gex_1pct":5684.95281159846,"gross_gex_1pct":5684.95281159846,"call_oi":7,"put_oi":0},{"strike":44950.0,"call_gex_1pct":802.7008971440514,"put_gex_1pct":0.0,"net_gex_1pct":802.7008971440514,"gross_gex_1pct":802.7008971440514,"call_oi":1,"put_oi":0},{"strike":45000.0,"call_gex_1pct":324875.1387478738,"put_gex_1pct":0.0,"net_gex_1pct":324875.1387478738,"gross_gex_1pct":324875.1387478738,"call_oi":551,"put_oi":0},{"strike":45100.0,"call_gex_1pct":6337.657232839584,"put_gex_1pct":0.0,"net_gex_1pct":6337.657232839584,"gross_gex_1pct":6337.657232839584,"call_oi":11,"put_oi":0},{"strike":45200.0,"call_gex_1pct":9574.368008807087,"put_gex_1pct":0.0,"net_gex_1pct":9574.368008807087,"gross_gex_1pct":9574.368008807087,"call_oi":17,"put_oi":0},{"strike":45300.0,"call_gex_1pct":983.2168065984399,"put_gex_1pct":0.0,"net_gex_1pct":983.2168065984399,"gross_gex_1pct":983.2168065984399,"call_oi":3,"put_oi":0},{"strike":45400.0,"call_gex_1pct":2243.5506394013887,"put_gex_1pct":0.0,"net_gex_1pct":2243.5506394013887,"gross_gex_1pct":2243.5506394013887,"call_oi":7,"put_oi":0},{"strike":45500.0,"call_gex_1pct":1567.6923702461893,"put_gex_1pct":0.0,"net_gex_1pct":1567.6923702461893,"gross_gex_1pct":1567.6923702461893,"call_oi":5,"put_oi":0},{"strike":45600.0,"call_gex_1pct":1534.0981639616175,"put_gex_1pct":0.0,"net_gex_1pct":1534.0981639616175,"gross_gex_1pct":1534.0981639616175,"call_oi":5,"put_oi":0},{"strike":45700.0,"call_gex_1pct":1201.353992356736,"put_gex_1pct":0.0,"net_gex_1pct":1201.353992356736,"gross_gex_1pct":1201.353992356736,"call_oi":4,"put_oi":0},{"strike":45800.0,"call_gex_1pct":3529.00328667718,"put_gex_1pct":0.0,"net_gex_1pct":3529.00328667718,"gross_gex_1pct":3529.00328667718,"call_oi":12,"put_oi":0},{"strike":45900.0,"call_gex_1pct":2592.3977278646594,"put_gex_1pct":0.0,"net_gex_1pct":2592.3977278646594,"gross_gex_1pct":2592.3977278646594,"call_oi":9,"put_oi":0},{"strike":46000.0,"call_gex_1pct":78172.205529603,"put_gex_1pct":0.0,"net_gex_1pct":78172.205529603,"gross_gex_1pct":78172.205529603,"call_oi":277,"put_oi":0},{"strike":46100.0,"call_gex_1pct":2765.718898785461,"put_gex_1pct":0.0,"net_gex_1pct":2765.718898785461,"gross_gex_1pct":2765.718898785461,"call_oi":10,"put_oi":0},{"strike":46200.0,"call_gex_1pct":1355.6025311862509,"put_gex_1pct":0.0,"net_gex_1pct":1355.6025311862509,"gross_gex_1pct":1355.6025311862509,"call_oi":5,"put_oi":0},{"strike":46300.0,"call_gex_1pct":797.5425706222068,"put_gex_1pct":0.0,"net_gex_1pct":797.5425706222068,"gross_gex_1pct":797.5425706222068,"call_oi":3,"put_oi":0},{"strike":46400.0,"call_gex_1pct":260.7449690248102,"put_gex_1pct":0.0,"net_gex_1pct":260.7449690248102,"gross_gex_1pct":260.7449690248102,"call_oi":1,"put_oi":0},{"strike":46500.0,"call_gex_1pct":3325.469136484972,"put_gex_1pct":0.0,"net_gex_1pct":3325.469136484972,"gross_gex_1pct":3325.469136484972,"call_oi":13,"put_oi":0},{"strike":46600.0,"call_gex_1pct":502.04292910041454,"put_gex_1pct":0.0,"net_gex_1pct":502.04292910041454,"gross_gex_1pct":502.04292910041454,"call_oi":2,"put_oi":0},{"strike":46700.0,"call_gex_1pct":3203.0269931543903,"put_gex_1pct":0.0,"net_gex_1pct":3203.0269931543903,"gross_gex_1pct":3203.0269931543903,"call_oi":13,"put_oi":0},{"strike":46800.0,"call_gex_1pct":483.78929605059704,"put_gex_1pct":0.0,"net_gex_1pct":483.78929605059704,"gross_gex_1pct":483.78929605059704,"call_oi":2,"put_oi":0},{"strike":46900.0,"call_gex_1pct":712.6179664367957,"put_gex_1pct":0.0,"net_gex_1pct":712.6179664367957,"gross_gex_1pct":712.6179664367957,"call_oi":3,"put_oi":0},{"strike":47000.0,"call_gex_1pct":5832.87554546325,"put_gex_1pct":0.0,"net_gex_1pct":5832.87554546325,"gross_gex_1pct":5832.87554546325,"call_oi":25,"put_oi":0},{"strike":47100.0,"call_gex_1pct":2292.163532072928,"put_gex_1pct":0.0,"net_gex_1pct":2292.163532072928,"gross_gex_1pct":2292.163532072928,"call_oi":10,"put_oi":0},{"strike":47200.0,"call_gex_1pct":3603.8112350938877,"put_gex_1pct":0.0,"net_gex_1pct":3603.8112350938877,"gross_gex_1pct":3603.8112350938877,"call_oi":16,"put_oi":0},{"strike":47300.0,"call_gex_1pct":221.37571695910344,"put_gex_1pct":0.0,"net_gex_1pct":221.37571695910344,"gross_gex_1pct":221.37571695910344,"call_oi":1,"put_oi":0},{"strike":47400.0,"call_gex_1pct":1305.7457509167923,"put_gex_1pct":0.0,"net_gex_1pct":1305.7457509167923,"gross_gex_1pct":1305.7457509167923,"call_oi":6,"put_oi":0},{"strike":47500.0,"call_gex_1pct":22895.81208977951,"put_gex_1pct":0.0,"net_gex_1pct":22895.81208977951,"gross_gex_1pct":22895.81208977951,"call_oi":107,"put_oi":0},{"strike":47600.0,"call_gex_1pct":210.43734089528218,"put_gex_1pct":0.0,"net_gex_1pct":210.43734089528218,"gross_gex_1pct":210.43734089528218,"call_oi":1,"put_oi":0},{"strike":47700.0,"call_gex_1pct":1241.962228333543,"put_gex_1pct":0.0,"net_gex_1pct":1241.962228333543,"gross_gex_1pct":1241.962228333543,"call_oi":6,"put_oi":0},{"strike":47800.0,"call_gex_1pct":1629.1590627091923,"put_gex_1pct":0.0,"net_gex_1pct":1629.1590627091923,"gross_gex_1pct":1629.1590627091923,"call_oi":8,"put_oi":0},{"strike":47900.0,"call_gex_1pct":1001.9364766941814,"put_gex_1pct":0.0,"net_gex_1pct":1001.9364766941814,"gross_gex_1pct":1001.9364766941814,"call_oi":5,"put_oi":0},{"strike":48000.0,"call_gex_1pct":8283.136378538828,"put_gex_1pct":0.0,"net_gex_1pct":8283.136378538828,"gross_gex_1pct":8283.136378538828,"call_oi":42,"put_oi":0},{"strike":48100.0,"call_gex_1pct":40767.792792586944,"put_gex_1pct":0.0,"net_gex_1pct":40767.792792586944,"gross_gex_1pct":40767.792792586944,"call_oi":210,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 37,600 | TAIFEX Proxy |
| 對應到期月份 | 202611W4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-24→2026-11-25) | +500 | TAIFEX Proxy snapshots (2026-11-24) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 78,885 | 78,247 | +638 | 32,500 | 30,556 | +1,944 | -1,306 | TAIFEX Proxy |
| 投信 | 0 | 2,010 | -2,010 | 0 | 0 | +0 | -2,010 | TAIFEX Proxy |
| 自營商 | 80,461 | 73,504 | +6,957 | 23,510 | 28,412 | -4,902 | +11,859 | TAIFEX Proxy |
| 三大法人合計 | 159,346 | 153,761 | +5,585 | 56,010 | 58,968 | -2,958 | +8,543 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 13.44 | 12.99 | +0.45 | 5.61 | 5.38 | +0.22 | +0.23 | TAIFEX Proxy |
| 投信 | 0.00 | 0.47 | -0.47 | 0.00 | 0.00 | +0 | -0.47 | TAIFEX Proxy |
| 自營商 | 15.65 | 15.41 | +0.25 | 6.59 | 7.73 | -1.14 | +1.39 | TAIFEX Proxy |
| 三大法人合計 | 29.10 | 28.87 | +0.23 | 12.20 | 13.12 | -0.92 | +1.15 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 16,054 | TAIFEX Proxy |
| 買權空方 OI | 19,423 | TAIFEX Proxy |
| 買權多空淨 OI | -3,369 | TAIFEX Proxy |
| 買權多空淨 OI 變化 | +414 | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 12,563 | TAIFEX Proxy |
| 賣權空方 OI | 14,639 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,076 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 | -143 | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |
- 資料日期：買權 2026-11-25／賣權 2026-11-25 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | +885 | — | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |
| 買權前十大 | +414 | — | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |
| 賣權前十大 | -143 | — | 沿用前版（原來源：TAIFEX Proxy snapshots (2026-11-24)） |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-25；本次報告產製時間：2026-11-26 16:39:27；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 保護：11 格沿用前版有值（本次抓取缺失不覆寫）
- 註記：同 T0 覆蓋：198 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-25；估值 1246 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 151.6130%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；0 檔採最近有效收盤價。Blave 同 T0 交叉驗證 151.6130%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：無日期端點為最新盤勢快照 (判定資料日期 2026-11-26，非 T0 2026-11-25)，適用：日盤價／法人交易／夜盤／選擇權法人；T0 相符時不另標註
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202611F4（到期日 2026-11-27）與 Options Key Levels 主到期月份 202611W4 不同；GEX 數值應以實際使用到期月份為準
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -1,236.5 | -105,709 | -583 | +1,122 | +638 | +1,944 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +550.3 | +100,918 | +4,002 | +0 | -2,010 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -128.3 | -651 | -1,550 | +212 | +6,957 | -4,902 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
