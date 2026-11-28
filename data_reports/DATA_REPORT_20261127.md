# DATA_REPORT_20261127

- 報告日期：`2026-11-28`
- T0 交易日期：`2026-11-27`
- 首次資料產出時間：`2026-11-28 09:45:23`
- 本次更新開始時間：`2026-11-28 09:45:23`
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
| 加權指數 | 39,308.08 | 點 | twse-proxy |
| 開盤 | 39,168.57 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 39,495.41 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 38,890.53 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 39,308.08 | 點 | twse-proxy |
| 漲跌點數 | 156.27 | 點 | twse-proxy |
| 漲跌幅 | +0.40 | % | twse-proxy |
| 成交金額 | 6,946.6 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 438 | twse-proxy |
| 下跌家數 | 551 | twse-proxy |
| 平盤家數 | 97 | twse-proxy |
| 漲停家數 | 20 | twse-proxy |
| 跌停家數 | 5 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 262 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 下跌家數 | 524 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 平盤家數 | 76 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 漲停家數 | 15 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 跌停家數 | 4 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -296.3 | 億元 | twse-proxy /institutional |
| 投信 | +85.2 | 億元 | twse-proxy /institutional |
| 自營商 | -2.0 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -213.0 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-27；估值 1247 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 158.4150%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 5,601.7 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -39.9 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 207,183 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | 12,329 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 158.41 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-27；估值 1247 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 158.4150%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 35,034,759 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,351,300.065 | 2,106,462.207 | 20,457,762.272 | 張 |
| 借券賣出增減 | -92,195.46 | -11,297.272 | -103,492.732 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261127`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-28T09:45:35+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261127`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-28T09:45:36+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 6,946.6 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,217.8 | 億元 | 漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |
| 上市櫃成交金額合計 | 8,164.4 | 億元 | twse-proxy market_statistics／漲跌家數：TPEx 歷史市場現況 highlight_result.php；成交金額：TPEx 歷史市場現況 highlight_result.php |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,297.49 | 114.71 | +1.60 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,129.50 | 543.70 | +2.31 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,726.39 | 679.49 | +2.61 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,774.94 | 591.99 | +1.18 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,186.71 | 411.85 | +4.69 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 23.81 | -2.99 | -11.16 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | unavailable | unavailable | unavailable | 2026-11-26 | 2026-11-28T01:45:36+00:00 | Asia/Tokyo | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 韓國KOSPI | ^KS11 | unavailable | unavailable | unavailable | 2026-11-26 | 2026-11-28T01:45:36+00:00 | Asia/Seoul | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 香港恆生 | ^HSI | unavailable | unavailable | unavailable | 2026-11-26 | 2026-11-28T01:45:36+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 上海綜合 | 000001.SS | unavailable | unavailable | unavailable | 2026-11-26 | 2026-11-28T01:45:36+00:00 | Asia/Shanghai | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |
| 深圳成分 | 399001.SZ | unavailable | unavailable | unavailable | 2026-11-26 | 2026-11-28T01:45:36+00:00 | Asia/Shanghai | Yahoo Finance Chart API（資料日期早於或無法核對 T0，已排除） |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,308.25 | 112.50 | +1.56 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 26,765.00 | 664.75 | +2.55 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 50,821.00 | 593.00 | +1.18 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,754.40 | 48.30 | +1.78 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.69 | 0.08 | 27-NOV-26 | 2026-11-28T01:45:56+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.94 | 0.09 | 2026-11-27 | 2026-11-28T01:45:56+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.36 | 0.08 | 27-NOV-26 | 2026-11-28T01:45:56+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.32 | 0.09 | 2026-11-27 | 2026-11-28T01:45:56+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 32.92 | -0.27 | -0.82 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 104.01 | 0.34 | +0.33 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 159.28 | 0.07 | +0.04 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,343.53 | 0.56 | +0.04 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API（台積電ADR資料日期 2026-11-25 與美國最近已收盤交易日 2026-11-27 不一致，已排除） |
| 聯電ADR | UMC | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API（聯電ADR資料日期 2026-11-25 與美國最近已收盤交易日 2026-11-27 不一致，已排除） |
| 日月光ADR | ASX | unavailable | unavailable | unavailable | 2026-11-25 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API（日月光ADR資料日期 2026-11-25 與美國最近已收盤交易日 2026-11-27 不一致，已排除） |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 83.08 | -0.60 | -0.72 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 3,668.50 | 132.70 | +3.75 | 2026-11-27 | 2026-11-28T01:45:36+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 60,119.89 | -374.82 | -0.62 | 2026-11-28 | 2026-11-28T01:45:36+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：選前台股翻紅守住3萬9 衛星股亮10顆漲停燈
  - 來源：Yahoo 台股；發布時間：2026-11-27T09:23:22Z；台北時間：2026-11-27 17:23
  - 摘要：台積電尾盤發力，台股選前量縮收紅，守住3萬9千點！加權指數今(27)日上漲156.27點、漲幅0.40%，收39,308.08點，週線翻紅、大漲3,274.79點，上市成交金額縮至6,673.11億元。九合一選舉前觀望氣氛濃厚，大盤早盤一度
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%81%B8%E5%89%8D%E6%9C%80%E5%BE%8C%E4%B8%80%E7%9B%A4%E7%A5%9E%E5%B1%B1%E7%99%BC%E5%8A%9B%E5%8F%B0%E8%82%A1%E7%BF%BB%E7%B4%85%E5%AE%883%E8%90%AC9%EF%BC%81%E6%AC%8A%E5%80%BC%E8%82%A1%E5%90%84%E8%B5%B0%E5%90%84%E7%9A%84-%E8%A1%9B%E6%98%9F%E8%82%A110%E9%A1%86%E7%B4%85%E7%87%88%E6%90%B6%E9%A2%A8%E9%A0%AD-%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-092322357.html
- 事件2：大學生打工買0050「這種做法」慘賠6萬！　網安慰：買到值得的經驗
  - 來源：Yahoo 台股；發布時間：2026-11-27T09:36:00Z；台北時間：2026-11-27 17:36
  - 摘要：一名座標台中的大學生日前在網路發發文分享，自己靠著每天打工存下的40萬元投入元大台灣50（0050），原本帳面一度獲利4萬元，卻因急於賺錢、心態失衡，最終在低點賣出，反而倒虧2萬元，整體資金從40萬元縮水至34萬元，一口氣少了6萬元，說這次
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E5%AD%B8%E7%94%9F%E6%89%93%E5%B7%A5%E8%B2%B70050-%E9%80%99%E7%A8%AE%E5%81%9A%E6%B3%95-%E6%85%98%E8%B3%A06%E8%90%AC-%E7%B6%B2%E5%AE%89%E6%85%B0-%E8%B2%B7%E5%88%B0%E5%80%BC%E5%BE%97%E7%9A%84%E7%B6%93%E9%A9%97-093600689.html
- 事件3：台積電硬撐台股翻紅！三大法人仍賣超213億元 本周提款2,916億元
  - 來源：Yahoo 台股；發布時間：2026-11-27T08:44:18Z；台北時間：2026-11-27 16:44
  - 摘要：台股27日適逢九合一選舉投票前夕，美股因感恩節休市，市場缺乏美股指引，加權指數開高後陷入震盪，盤中一度下探38,890.53點，尾盤在台積電（2330）急拉助攻下，終場上漲156.27點，以39,308.08點作收，漲幅0.39%，成交金額
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E7%A1%AC%E6%92%90%E5%8F%B0%E8%82%A1%E7%BF%BB%E7%B4%85-%E4%B8%89%E5%A4%A7%E6%B3%95%E4%BA%BA%E4%BB%8D%E8%B3%A3%E8%B6%85213%E5%84%84%E5%85%83-%E6%9C%AC%E5%91%A8%E6%8F%90%E6%AC%BE2-916%E5%84%84%E5%85%83-084418540.html
- 事件4：立陶宛總統嫌台灣投資太少！再施壓代表處更名　揚言不排除單方面行動
  - 來源：Yahoo 台股；發布時間：2026-11-27T05:47:00Z；台北時間：2026-11-27 13:47
  - 摘要：[FTNN新聞網]記者林欣愉／綜合報導立陶宛持續推動與中國關係正常化，並要求台灣駐立陶宛代表處改名，爭議再度升溫！立陶宛總統瑙塞達（GitanasNausėda）於當...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%AB%8B%E9%99%B6%E5%AE%9B%E7%B8%BD%E7%B5%B1%E5%AB%8C%E5%8F%B0%E7%81%A3%E6%8A%95%E8%B3%87%E5%A4%AA%E5%B0%91-%E5%86%8D%E6%96%BD%E5%A3%93%E4%BB%A3%E8%A1%A8%E8%99%95%E6%9B%B4%E5%90%8D-%E6%8F%9A%E8%A8%80%E4%B8%8D%E6%8E%92%E9%99%A4%E5%96%AE%E6%96%B9%E9%9D%A2%E8%A1%8C%E5%8B%95-054700956.html
- 事件5：水五金新業務發威！「這檔」前3季純益暴增1.11倍　每股大賺9.03元、12/28除息
  - 來源：Yahoo 台股；發布時間：2026-11-27T04:05:00Z；台北時間：2026-11-27 12:05
  - 摘要：[FTNN新聞網]實習記者盛琳／綜合報導家飾鑄件廠泰金-KY（6629）公布2026年前3季財報，受惠於水五金代工新業務及新客戶訂單挹注，前3季營收衝上19.38億元、年...
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%B0%B4%E4%BA%94%E9%87%91%E6%96%B0%E6%A5%AD%E5%8B%99%E7%99%BC%E5%A8%81-%E9%80%99%E6%AA%94-%E5%89%8D3%E5%AD%A3%E7%B4%94%E7%9B%8A%E6%9A%B4%E5%A2%9E1-11%E5%80%8D-%E6%AF%8F%E8%82%A1%E5%A4%A7%E8%B3%BA9-040500765.html
- 事件6：美股感恩節休市 台股選前多頭續攻 小幅開高後平盤震盪守住39000點
  - 來源：Yahoo 台股；發布時間：2026-11-27T02:10:00Z；台北時間：2026-11-27 10:10
  - 摘要：【緯來新聞網】 適逢感恩節，美股週四（26日）休市，受美股不開盤影響，台指期夜盤今（27）日收平盤
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%BE%8E%E8%82%A1%E6%84%9F%E6%81%A9%E7%AF%80%E4%BC%91%E5%B8%82-%E5%8F%B0%E8%82%A1%E9%81%B8%E5%89%8D%E5%A4%9A%E9%A0%AD%E7%BA%8C%E6%94%BB-%E5%B0%8F%E5%B9%85%E9%96%8B%E9%AB%98%E5%BE%8C%E5%B9%B3%E7%9B%A4%E9%9C%87%E7%9B%AA%E5%AE%88%E4%BD%8F39000%E9%BB%9E-021000840.html
- 事件7：Inflation has shoppers hunting for value. That bodes well for Black Friday
  - 來源：CNBC；發布時間：Fri, 27 Nov 2026 22:00:57 GMT；台北時間：2026-11-28 06:00
  - 摘要：Even as consumers face macroeconomic headwinds, retailers are expecting robust holiday spending through Black Friday and beyond.
  - 原文連結：https://www.cnbc.com/2026/11/27/black-friday-2026-inflation-value-deals.html
- 事件8：Trump demands probe into 'record setting error' after third-quarter GDP data gets massive revision higher
  - 來源：CNBC；發布時間：Fri, 27 Nov 2026 15:52:00 GMT；台北時間：2026-11-27 23:52
  - 摘要：President Donald Trump on Thursday deemed the latest gross domestic product revision a mistake, claiming that it should be "immediately investigated."
  - 原文連結：https://www.cnbc.com/2026/11/26/trump-gdp-revision-investigation.html
- 事件9：The S&P 500 is in a correction. Bear markets and recessions don't always follow
  - 來源：CNBC；發布時間：Fri, 27 Nov 2026 13:21:56 GMT；台北時間：2026-11-27 21:21
  - 摘要：The November sell-off has so far pushed the S&P 500 into a correction. History shows that a correction doesn't always lead to a bear market, or a rece
  - 原文連結：https://www.cnbc.com/2026/11/27/the-sp-500-is-in-a-correction-bear-markets-and-recessions-dont-always-follow.html
- 事件10：Spain’s Pablo Hernández de Cos set to lead European Central Bank
  - 來源：CNBC；發布時間：Fri, 27 Nov 2026 06:50:38 GMT；台北時間：2026-11-27 14:50
  - 摘要：De Cos will lead the ECB into a period of political uncertainty and choppy growth, after winning the backing needed to succeed Christine Lagarde next 
  - 原文連結：https://www.cnbc.com/2026/11/26/pablo-hernandez-de-cos-ecb-president.html
- 事件11：Agencies announce dollar thresholds for applicability of truth in lending and consumer leasing rules for consumer credit and lease transactions
  - 來源：Federal Reserve；發布時間：Wed, 25 Nov 2026 20:00:00 GMT；台北時間：2026-11-26 04:00
  - 摘要：Agencies announce dollar thresholds for applicability of truth in lending and consumer leasing rules for consumer credit and lease transactions
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261125b.htm
- 事件12：Agencies announce dollar thresholds for smaller loan exemption from appraisal requirements for higher-priced mortgage loans
  - 來源：Federal Reserve；發布時間：Wed, 25 Nov 2026 20:00:00 GMT；台北時間：2026-11-26 04:00
  - 摘要：Agencies announce dollar thresholds for smaller loan exemption from appraisal requirements for higher-priced mortgage loans
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261125a.htm


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202612 (日盤成交量最大者)；交易日期：2026-11-27

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 39,525 | 點 | TAIFEX Proxy |
| 最高價 | 39,652 | 點 | TAIFEX Proxy |
| 最低價 | 39,050 | 點 | TAIFEX Proxy |
| 收盤價 | 39,363 | 點 | TAIFEX Proxy |
| 漲跌點數 | -129 | 點 | TAIFEX Proxy |
| 漲跌幅 | -0.33 | % | TAIFEX Proxy |
| 成交量 | 59,337 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 39,652 / 39,050 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 39,350 | 點 | TAIFEX Proxy |
| 最高價 | 39,444 | 點 | TAIFEX Proxy |
| 最低價 | 38,465 | 點 | TAIFEX Proxy |
| 收盤價 | 39,153 | 點 | TAIFEX Proxy |
| 漲跌點數 | -197 | 點 | TAIFEX Proxy |
| 漲跌幅 | -0.50 | % | TAIFEX Proxy |
| 成交量 | 45,928 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 39,444 / 38,465 | 點 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 7,862 | TAIFEX Proxy |
| 外資空方 OI | 115,365 | TAIFEX Proxy |
| 外資多空淨 OI | -107,503 | TAIFEX Proxy |
| 投信多方 OI | 107,671 | TAIFEX Proxy |
| 投信空方 OI | 3,316 | TAIFEX Proxy |
| 投信多空淨 OI | +104,355 | TAIFEX Proxy |
| 自營商多方 OI | 2,076 | TAIFEX Proxy |
| 自營商空方 OI | 5,642 | TAIFEX Proxy |
| 自營商多空淨 OI | -3,566 | TAIFEX Proxy |
| 三大法人合計多方 OI | 117,609 | TAIFEX Proxy |
| 三大法人合計空方 OI | 124,323 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -6,714 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -1,228 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | -565 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,156 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 108,640 | TAIFEX Proxy |
| 前十大交易人空方 OI | 95,166 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,474 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-26→2026-11-27) | -3,274 | TAIFEX Proxy snapshots (2026-11-26) |
- 資料日期：2026-11-27 (TypeOfTraders=0 全部交易人；契約月份 202612)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 53,803 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 53,882 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -79 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 27,402 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 26,191 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,211 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -1,290 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | -565 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | -565 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,147 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -87 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -1,060 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -1,791 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,124 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -140.4 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | +87.4 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 39,363 | TAIFEX Proxy |
| 加權指數價格 | 39,308.08 | twse-proxy |
| 台指期與加權指數價差 | +54.92 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +0.14 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +54.92 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -210 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,363 | 39,153 | +210 | TAIFEX Proxy |
| 成交量 | 59,337 | 45,928 | +13,409 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-2,949（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 53,803 | 53,882 | -79 | 27,402 | 26,191 | +1,211 | -1,290 | 7,862 | 115,365 | -107,503 | -1,228 | TAIFEX Proxy |
| 投信 | 159 | 724 | -565 | 0 | 0 | +0 | -565 | 107,671 | 3,316 | +104,355 | -565 | TAIFEX Proxy |
| 自營商 | 2,896 | 4,043 | -1,147 | 808 | 895 | -87 | -1,060 | 2,076 | 5,642 | -3,566 | -1,156 | TAIFEX Proxy |
| 三大法人合計 | 56,858 | 58,649 | -1,791 | 28,210 | 27,086 | +1,124 | -2,915 | 117,609 | 124,323 | -6,714 | -2,949 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 108,640 | TAIFEX Proxy |
| 前十大交易人空方 OI | 95,166 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +13,474 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-26→2026-11-27) | -3,274 | TAIFEX Proxy snapshots (2026-11-26) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 43.63% | TAIFEX Proxy |
| 夜盤漲跌點數 | -197 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,211 | TAIFEX Proxy |
| 劇本分類 | 劇本四 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏多 | 規則對應 |
| 劇本特徵 | 先跌、開低反彈 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-27 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F4 | TAIFEX Proxy |
| 本次報告產製時間 | 2026-11-28 09:45:23 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 248,739 | TAIFEX Proxy |
| Call 總未平倉量 OI | 114,521 | TAIFEX Proxy |
| Call OI 增減（共同合約） (2026-11-26→2026-11-27) | +31,493 | TAIFEX Proxy snapshot bundle (2026-11-26→2026-11-27) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 217,897 | TAIFEX Proxy |
| Put 總未平倉量 OI | 66,637 | TAIFEX Proxy |
| Put OI 增減（共同合約） (2026-11-26→2026-11-27) | +24,397 | TAIFEX Proxy snapshot bundle (2026-11-26→2026-11-27) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.14 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.72 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.58 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-26→2026-11-27) | -3.84 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-26→2026-11-27) | -5.86 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 86,538 | TAIFEX Proxy |
| 外資 Call日賣 | 78,434 | TAIFEX Proxy |
| 外資 Call日淨 | +8,104 | TAIFEX Proxy |
| 外資 Put日買 | 80,497 | TAIFEX Proxy |
| 外資 Put日賣 | 79,136 | TAIFEX Proxy |
| 外資 Put日淨 | +1,361 | TAIFEX Proxy |
| 外資 Call夜買 | 10,377 | TAIFEX Proxy |
| 外資 Call夜賣 | 10,656 | TAIFEX Proxy |
| 外資 Call夜淨 | -279 | TAIFEX Proxy |
| 外資 Put夜買 | 8,123 | TAIFEX Proxy |
| 外資 Put夜賣 | 8,164 | TAIFEX Proxy |
| 外資 Put夜淨 | -41 | TAIFEX Proxy |
| 外資 日盤淨總量 | +6,743 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +8,383 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,402 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 67,590 | TAIFEX Proxy |
| 自營商 Call日賣 | 72,490 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,900 | TAIFEX Proxy |
| 自營商 Put日買 | 57,387 | TAIFEX Proxy |
| 自營商 Put日賣 | 68,261 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,874 | TAIFEX Proxy |
| 自營商 Call夜買 | 8,065 | TAIFEX Proxy |
| 自營商 Call夜賣 | 9,723 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,658 | TAIFEX Proxy |
| 自營商 Put夜買 | 8,938 | TAIFEX Proxy |
| 自營商 Put夜賣 | 9,078 | TAIFEX Proxy |
| 自營商 Put夜淨 | -140 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +5,974 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -3,242 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -10,734 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 42,000 | 12,794 | TAIFEX Proxy |
| Call OI 第2大履約價 | 43,000 | 8,602 | TAIFEX Proxy |
| Call OI 第3大履約價 | 40,000 | 5,632 | TAIFEX Proxy |
| Call OI 最大履約價 | 42,000 | 12,794 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 42,000 | 12,794 | 11.17% | TAIFEX Proxy |
| C2 | 43,000 | 8,602 | 7.51% | TAIFEX Proxy |
| C3 | 40,000 | 5,632 | 4.92% | TAIFEX Proxy |
| C4 | 41,000 | 4,270 | 3.73% | TAIFEX Proxy |
| C5 | 37,600 | 3,629 | 3.17% | TAIFEX Proxy |
| C6 | 39,500 | 3,614 | 3.16% | TAIFEX Proxy |
| C7 | 37,800 | 3,439 | 3.0% | TAIFEX Proxy |
| C8 | 39,300 | 3,042 | 2.66% | TAIFEX Proxy |
| C9 | 37,500 | 2,980 | 2.6% | TAIFEX Proxy |
| C10 | 35,000 | 2,802 | 2.45% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 34,000 | 4,367 | TAIFEX Proxy |
| Put OI 第2大履約價 | 32,400 | 3,875 | TAIFEX Proxy |
| Put OI 第3大履約價 | 36,000 | 3,747 | TAIFEX Proxy |
| Put OI 最大履約價 | 34,000 | 4,367 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F4)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 34,000 | 4,367 | 6.55% | TAIFEX Proxy |
| P2 | 32,400 | 3,875 | 5.82% | TAIFEX Proxy |
| P3 | 36,000 | 3,747 | 5.62% | TAIFEX Proxy |
| P4 | 35,000 | 2,904 | 4.36% | TAIFEX Proxy |
| P5 | 37,000 | 2,505 | 3.76% | TAIFEX Proxy |
| P6 | 39,200 | 2,395 | 3.59% | TAIFEX Proxy |
| P7 | 39,000 | 2,263 | 3.4% | TAIFEX Proxy |
| P8 | 38,000 | 2,249 | 3.38% | TAIFEX Proxy |
| P9 | 39,250 | 2,232 | 3.35% | TAIFEX Proxy |
| P10 | 38,500 | 2,016 | 3.03% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價（共同合約） | 40,000 (+3,429) | TAIFEX Proxy snapshot bundle (2026-11-26→2026-11-27) |
| Call OI 減少最多的履約價（共同合約） | 43,000 (-803) | TAIFEX Proxy snapshot bundle (2026-11-26→2026-11-27) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價（共同合約） | 39,200 (+2,286) | TAIFEX Proxy snapshot bundle (2026-11-26→2026-11-27) |
| Put OI 減少最多的履約價（共同合約） | 32,400 (-295) | TAIFEX Proxy snapshot bundle (2026-11-26→2026-11-27) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 42,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-26→2026-11-27) | +0 | TAIFEX Proxy snapshots (2026-11-26) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 34,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-26→2026-11-27) | +0 | TAIFEX Proxy snapshots (2026-11-26) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 38,900.00 | options-gamma-levels |
| GEX 實際使用到期月份 | 202612W1 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-12-02 | options-gamma-levels（GEX 實際使用） |
| Options Key Levels 主到期月份 | 202611F4 | TAIFEX Proxy |
| 資料日期 | 2026-11-27 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 37,182.94 | options-market-structure-compact (proxy) |
| GEX 實際使用到期月份 | 202612W1 | options-gamma-levels（GEX 實際使用） |
| GEX 實際到期日 | 2026-12-02 | options-gamma-levels（GEX 實際使用） |
| 主到期月份（Key Levels） | 202611F4 | TAIFEX Proxy |
| 原始 Call OI（選定到期日全部有效 Chain 合約） | 30,494 | options-gamma-levels（GEX 到期日） |
| 模型納入 Call OI（通過 GEX 計算條件） | 30,494 | TAIFEX Gamma model（逐履約價） |
| 原始 Put OI（選定到期日全部有效 Chain 合約） | 8,722 | options-gamma-levels（GEX 到期日） |
| 模型納入 Put OI（通過 GEX 計算條件） | 8,722 | TAIFEX Gamma model（逐履約價） |
| GEX 資料日期 | 2026-11-27 | TAIFEX Proxy (options-gamma-levels + options-market-structure-compact (proxy)) |
- OI 對帳口徑：原始 OI 統計選定到期日全部有效 Chain 合約；模型納入 OI 僅統計通過結算價、IV 與 Gamma 計算條件並納入逐履約價 GEX 的合約。兩者差額不等於 Chain 缺漏。

**Gamma Flip 零交叉搜尋診斷**
- 搜尋標的區間：35,377.27～43,238.89
- 搜尋步長／計算次數：10.00／787
- 起點／終點 Net GEX：370,265,110.15／1,403,327,270.66
- 搜尋區間最低／最高 Net GEX：370,265,110.15／2,796,469,003.79
- 正負號交叉次數：0
- 解讀限制：此 Flip 僅代表目前 Call 正／Put 負假設下的模型零交叉；Aggregate OI 無法識別 Dealer 實際淨部位，不等同市場實際 Dealer Gamma Flip。

**GEX 到期日配對診斷（原始候選清單）**
```json
{"requested_date":"2026-11-27","chain_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612F2","expiry":"2026-12-11"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612F2","expiry":"2026-12-11"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F2","expiry":"2026-12-11","delta_contract_month":"202612F2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F2","expiry":"2026-12-11","delta_contract_month":"202612F2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F2","expiry":"2026-12-11","delta_contract_month":"202612F2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":0},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":364,"delta_rows":364},{"contract_month":"202612W2","expiry":"2026-12-09","chain_rows":286,"delta_rows":286},{"contract_month":"202612F2","expiry":"2026-12-11","chain_rows":206,"delta_rows":206},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"}
```

**TAIFEX Delta 原始資料與 Parser 階段診斷**
```json
{"requested_date":"2026-11-27","source":"taifex_csv","fallback_used":false,"csv_duration_ms":660,"attempts":[{"source":"taifex_csv","duration_ms":660,"http_status":200,"bytes":479358,"parser":{"requested_date":"2026-11-27","source_date":"2026-11-27","published_at":"2026/11/27 04:33:23 PM","input_lines":9684,"txo_rows":3228,"parsed_rows":3228,"invalid_rows":0,"call_rows":1614,"put_rows":1614},"accepted_txo_rows":3228}],"parser":{"requested_date":"2026-11-27","source_date":"2026-11-27","published_at":"2026/11/27 04:33:23 PM","input_lines":9684,"txo_rows":3228,"parsed_rows":3228,"invalid_rows":0,"call_rows":1614,"put_rows":1614},"final_rows":3228}
```

**擴大區間 Gamma Flip 診斷（±15%；不覆蓋正式 ±10% 結果）**
- 搜尋標的區間：33,411.87～45,204.29
- 搜尋步長／計算次數：10.00／1180
- 起點／終點 Net GEX：-258,197,673.26／822,717,990.10
- 搜尋區間最低／最高 Net GEX：-258,197,673.26／2,796,465,915.90
- 正負號交叉次數：1
- 擴大區間診斷 Flip：34,633.93

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 2,796,115,536.05 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 3,811,852,720.23 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 部位正負號假設 | Call 正／Put 負為模型假設；Aggregate OI 不揭露 Dealer 實際淨部位，此值不可視為實際 Dealer GEX | 模型限制；非 TAIFEX 公布的 Dealer 部位 |
| 履約價資料筆數 | 184 | 資料日期：2026-11-27 |
| 正 Net GEX 最大履約價 | 38,900 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 37,000 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：38,900（505,146,155.28 NT$）、38,800（483,028,873.68 NT$）、38,700（477,864,786.91 NT$）、37,700（349,360,300.55 NT$）、39,200（205,359,774.09 NT$）
- 負 Net GEX Top 5：37,000（-34,982,413.95 NT$）、38,000（-33,463,492.98 NT$）、36,000（-27,755,586.72 NT$）、35,000（-25,384,689.76 NT$）、32,400（-18,185,966.07 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-27","underlying":39308.08,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":2796115536.0532346,"gross_gex_1pct":3811852720.232466,"gamma_diagnostics":{"chain_rows":368,"delta_rows":368,"matched_strike_keys":368,"positive_oi_settlement_eligible":280,"invalid_oi":88,"invalid_settlement":0,"below_intrinsic":0,"iv_failed":0,"iv_out_of_range":0,"gamma_failed":0,"modeled_contracts":280},"formal_flip_diagnostics":{"search_lower_underlying":35377.272000000004,"search_upper_underlying":43238.888000000006,"step":10,"evaluations":787,"start_net_gex_1pct":370265110.14617825,"end_net_gex_1pct":1403327270.6616566,"min_net_gex_1pct":370265110.14617825,"max_net_gex_1pct":2796469003.7935357,"zero_crossings":0,"found":false},"wide_range_flip":{"lower_underlying":34631.868,"upper_underlying":34641.868,"estimated_underlying":34633.92573397863,"lower_net_gex_1pct":-778986.1938265353,"upper_net_gex_1pct":3006664.4389502425},"wide_range_flip_diagnostics":{"search_lower_underlying":33411.868,"search_upper_underlying":45204.292,"reference_underlying":39308.08,"step":10,"evaluations":1180,"start_net_gex_1pct":-258197673.26067653,"end_net_gex_1pct":822717990.101126,"min_net_gex_1pct":-258197673.26067653,"max_net_gex_1pct":2796465915.895098,"zero_crossings":1,"found":true,"selected_crossing_distance":4674.1542660213745},"expiry_selection_diagnostics":{"requested_date":"2026-11-27","chain_expiries":[{"contract_month":"202611F4","expiry":"2026-11-27"},{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612F2","expiry":"2026-12-11"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"delta_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02"},{"contract_month":"202612F1","expiry":"2026-12-04"},{"contract_month":"202612W2","expiry":"2026-12-09"},{"contract_month":"202612F2","expiry":"2026-12-11"},{"contract_month":"202612","expiry":"2026-12-16"},{"contract_month":"202701","expiry":"2027-01-20"},{"contract_month":"202702","expiry":"2027-02-17"},{"contract_month":"202703","expiry":"2027-03-17"},{"contract_month":"202706","expiry":"2027-06-16"}],"common_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F2","expiry":"2026-12-11","delta_contract_month":"202612F2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"same_day_common_expiries":[],"future_common_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F2","expiry":"2026-12-11","delta_contract_month":"202612F2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_exact_common_expiries":[{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F1","expiry":"2026-12-04","delta_contract_month":"202612F1","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612W2","expiry":"2026-12-09","delta_contract_month":"202612W2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612F2","expiry":"2026-12-11","delta_contract_month":"202612F2","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202612","expiry":"2026-12-16","delta_contract_month":"202612","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202701","expiry":"2027-01-20","delta_contract_month":"202701","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202702","expiry":"2027-02-17","delta_contract_month":"202702","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202703","expiry":"2027-03-17","delta_contract_month":"202703","match_type":"exact_contract_month_and_expiry"},{"contract_month":"202706","expiry":"2027-06-16","delta_contract_month":"202706","match_type":"exact_contract_month_and_expiry"}],"future_date_fallback_common_expiries":[],"per_expiry_row_counts":[{"contract_month":"202611F4","expiry":"2026-11-27","chain_rows":516,"delta_rows":0},{"contract_month":"202612W1","expiry":"2026-12-02","chain_rows":368,"delta_rows":368},{"contract_month":"202612F1","expiry":"2026-12-04","chain_rows":364,"delta_rows":364},{"contract_month":"202612W2","expiry":"2026-12-09","chain_rows":286,"delta_rows":286},{"contract_month":"202612F2","expiry":"2026-12-11","chain_rows":206,"delta_rows":206},{"contract_month":"202612","expiry":"2026-12-16","chain_rows":592,"delta_rows":592},{"contract_month":"202701","expiry":"2027-01-20","chain_rows":472,"delta_rows":472},{"contract_month":"202702","expiry":"2027-02-17","chain_rows":316,"delta_rows":316},{"contract_month":"202703","expiry":"2027-03-17","chain_rows":312,"delta_rows":312},{"contract_month":"202706","expiry":"2027-06-16","chain_rows":312,"delta_rows":312}],"selected":{"contract_month":"202612W1","expiry":"2026-12-02","delta_contract_month":"202612W1","match_type":"exact_contract_month_and_expiry"},"selection_reason":"earliest_future_exact_common_expiry"},"levels":[{"strike":32400.0,"call_gex_1pct":0.0,"put_gex_1pct":-18185966.07447114,"net_gex_1pct":-18185966.07447114,"gross_gex_1pct":18185966.07447114,"call_oi":0,"put_oi":1575},{"strike":32500.0,"call_gex_1pct":0.0,"put_gex_1pct":-483089.00621391094,"net_gex_1pct":-483089.00621391094,"gross_gex_1pct":483089.00621391094,"call_oi":0,"put_oi":40},{"strike":32600.0,"call_gex_1pct":0.0,"put_gex_1pct":-328085.1025242535,"net_gex_1pct":-328085.1025242535,"gross_gex_1pct":328085.1025242535,"call_oi":0,"put_oi":26},{"strike":32700.0,"call_gex_1pct":0.0,"put_gex_1pct":-287150.6224221149,"net_gex_1pct":-287150.6224221149,"gross_gex_1pct":287150.6224221149,"call_oi":0,"put_oi":22},{"strike":32800.0,"call_gex_1pct":0.0,"put_gex_1pct":-311891.24246698036,"net_gex_1pct":-311891.24246698036,"gross_gex_1pct":311891.24246698036,"call_oi":0,"put_oi":23},{"strike":32900.0,"call_gex_1pct":0.0,"put_gex_1pct":-169002.14475800717,"net_gex_1pct":-169002.14475800717,"gross_gex_1pct":169002.14475800717,"call_oi":0,"put_oi":12},{"strike":33000.0,"call_gex_1pct":0.0,"put_gex_1pct":-3202266.221208133,"net_gex_1pct":-3202266.221208133,"gross_gex_1pct":3202266.221208133,"call_oi":0,"put_oi":219},{"strike":33100.0,"call_gex_1pct":0.0,"put_gex_1pct":-106652.47333714417,"net_gex_1pct":-106652.47333714417,"gross_gex_1pct":106652.47333714417,"call_oi":0,"put_oi":7},{"strike":33200.0,"call_gex_1pct":0.0,"put_gex_1pct":-157503.09050978697,"net_gex_1pct":-157503.09050978697,"gross_gex_1pct":157503.09050978697,"call_oi":0,"put_oi":10},{"strike":33300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1122959.353806036,"net_gex_1pct":-1122959.353806036,"gross_gex_1pct":1122959.353806036,"call_oi":0,"put_oi":68},{"strike":33400.0,"call_gex_1pct":0.0,"put_gex_1pct":-409619.21802321606,"net_gex_1pct":-409619.21802321606,"gross_gex_1pct":409619.21802321606,"call_oi":0,"put_oi":24},{"strike":33500.0,"call_gex_1pct":0.0,"put_gex_1pct":-1544693.9056370724,"net_gex_1pct":-1544693.9056370724,"gross_gex_1pct":1544693.9056370724,"call_oi":0,"put_oi":87},{"strike":33600.0,"call_gex_1pct":0.0,"put_gex_1pct":-668671.6417710724,"net_gex_1pct":-668671.6417710724,"gross_gex_1pct":668671.6417710724,"call_oi":0,"put_oi":36},{"strike":33700.0,"call_gex_1pct":0.0,"put_gex_1pct":-1113297.9053552034,"net_gex_1pct":-1113297.9053552034,"gross_gex_1pct":1113297.9053552034,"call_oi":0,"put_oi":58},{"strike":33800.0,"call_gex_1pct":0.0,"put_gex_1pct":-793591.7765859421,"net_gex_1pct":-793591.7765859421,"gross_gex_1pct":793591.7765859421,"call_oi":0,"put_oi":40},{"strike":33900.0,"call_gex_1pct":0.0,"put_gex_1pct":-354220.9189774929,"net_gex_1pct":-354220.9189774929,"gross_gex_1pct":354220.9189774929,"call_oi":0,"put_oi":17},{"strike":34000.0,"call_gex_1pct":0.0,"put_gex_1pct":-7553148.676655049,"net_gex_1pct":-7553148.676655049,"gross_gex_1pct":7553148.676655049,"call_oi":0,"put_oi":349},{"strike":34100.0,"call_gex_1pct":0.0,"put_gex_1pct":-451595.394044974,"net_gex_1pct":-451595.394044974,"gross_gex_1pct":451595.394044974,"call_oi":0,"put_oi":20},{"strike":34200.0,"call_gex_1pct":0.0,"put_gex_1pct":-351649.534169404,"net_gex_1pct":-351649.534169404,"gross_gex_1pct":351649.534169404,"call_oi":0,"put_oi":15},{"strike":34300.0,"call_gex_1pct":0.0,"put_gex_1pct":-1265629.1564944463,"net_gex_1pct":-1265629.1564944463,"gross_gex_1pct":1265629.1564944463,"call_oi":0,"put_oi":52},{"strike":34400.0,"call_gex_1pct":0.0,"put_gex_1pct":-2782398.94519417,"net_gex_1pct":-2782398.94519417,"gross_gex_1pct":2782398.94519417,"call_oi":0,"put_oi":111},{"strike":34500.0,"call_gex_1pct":0.0,"put_gex_1pct":-2475328.4589657136,"net_gex_1pct":-2475328.4589657136,"gross_gex_1pct":2475328.4589657136,"call_oi":0,"put_oi":94},{"strike":34600.0,"call_gex_1pct":0.0,"put_gex_1pct":-440439.5815883761,"net_gex_1pct":-440439.5815883761,"gross_gex_1pct":440439.5815883761,"call_oi":0,"put_oi":16},{"strike":34700.0,"call_gex_1pct":0.0,"put_gex_1pct":-428565.387677241,"net_gex_1pct":-428565.387677241,"gross_gex_1pct":428565.387677241,"call_oi":0,"put_oi":15},{"strike":34800.0,"call_gex_1pct":0.0,"put_gex_1pct":-984711.9212188825,"net_gex_1pct":-984711.9212188825,"gross_gex_1pct":984711.9212188825,"call_oi":0,"put_oi":33},{"strike":34900.0,"call_gex_1pct":0.0,"put_gex_1pct":-2694584.6737940903,"net_gex_1pct":-2694584.6737940903,"gross_gex_1pct":2694584.6737940903,"call_oi":0,"put_oi":87},{"strike":35000.0,"call_gex_1pct":24598.357076132055,"put_gex_1pct":-25409288.11650131,"net_gex_1pct":-25384689.75942518,"gross_gex_1pct":25433886.47357744,"call_oi":1,"put_oi":786},{"strike":35050.0,"call_gex_1pct":0.0,"put_gex_1pct":-2865552.602691239,"net_gex_1pct":-2865552.602691239,"gross_gex_1pct":2865552.602691239,"call_oi":0,"put_oi":87},{"strike":35100.0,"call_gex_1pct":0.0,"put_gex_1pct":-874765.4111494061,"net_gex_1pct":-874765.4111494061,"gross_gex_1pct":874765.4111494061,"call_oi":0,"put_oi":26},{"strike":35150.0,"call_gex_1pct":0.0,"put_gex_1pct":-479953.41958286084,"net_gex_1pct":-479953.41958286084,"gross_gex_1pct":479953.41958286084,"call_oi":0,"put_oi":14},{"strike":35200.0,"call_gex_1pct":0.0,"put_gex_1pct":-908301.2204066013,"net_gex_1pct":-908301.2204066013,"gross_gex_1pct":908301.2204066013,"call_oi":0,"put_oi":26},{"strike":35250.0,"call_gex_1pct":0.0,"put_gex_1pct":-499564.37743610376,"net_gex_1pct":-499564.37743610376,"gross_gex_1pct":499564.37743610376,"call_oi":0,"put_oi":14},{"strike":35300.0,"call_gex_1pct":0.0,"put_gex_1pct":-732013.6756939803,"net_gex_1pct":-732013.6756939803,"gross_gex_1pct":732013.6756939803,"call_oi":0,"put_oi":20},{"strike":35350.0,"call_gex_1pct":0.0,"put_gex_1pct":-74596.33043947055,"net_gex_1pct":-74596.33043947055,"gross_gex_1pct":74596.33043947055,"call_oi":0,"put_oi":2},{"strike":35400.0,"call_gex_1pct":0.0,"put_gex_1pct":-798262.180568895,"net_gex_1pct":-798262.180568895,"gross_gex_1pct":798262.180568895,"call_oi":0,"put_oi":21},{"strike":35450.0,"call_gex_1pct":0.0,"put_gex_1pct":-661166.3418991937,"net_gex_1pct":-661166.3418991937,"gross_gex_1pct":661166.3418991937,"call_oi":0,"put_oi":17},{"strike":35500.0,"call_gex_1pct":101136.14611560838,"put_gex_1pct":-3786058.346570144,"net_gex_1pct":-3684922.2004545354,"gross_gex_1pct":3887194.4926857525,"call_oi":3,"put_oi":95},{"strike":35550.0,"call_gex_1pct":0.0,"put_gex_1pct":-773054.8820071243,"net_gex_1pct":-773054.8820071243,"gross_gex_1pct":773054.8820071243,"call_oi":0,"put_oi":19},{"strike":35600.0,"call_gex_1pct":0.0,"put_gex_1pct":-582453.0987390041,"net_gex_1pct":-582453.0987390041,"gross_gex_1pct":582453.0987390041,"call_oi":0,"put_oi":14},{"strike":35650.0,"call_gex_1pct":0.0,"put_gex_1pct":-84942.04666970136,"net_gex_1pct":-84942.04666970136,"gross_gex_1pct":84942.04666970136,"call_oi":0,"put_oi":2},{"strike":35700.0,"call_gex_1pct":0.0,"put_gex_1pct":-434183.9192234248,"net_gex_1pct":-434183.9192234248,"gross_gex_1pct":434183.9192234248,"call_oi":0,"put_oi":10},{"strike":35750.0,"call_gex_1pct":0.0,"put_gex_1pct":-178213.60233586893,"net_gex_1pct":-178213.60233586893,"gross_gex_1pct":178213.60233586893,"call_oi":0,"put_oi":4},{"strike":35800.0,"call_gex_1pct":0.0,"put_gex_1pct":-1133985.7051805835,"net_gex_1pct":-1133985.7051805835,"gross_gex_1pct":1133985.7051805835,"call_oi":0,"put_oi":25},{"strike":35850.0,"call_gex_1pct":0.0,"put_gex_1pct":-926005.7207978796,"net_gex_1pct":-926005.7207978796,"gross_gex_1pct":926005.7207978796,"call_oi":0,"put_oi":20},{"strike":35900.0,"call_gex_1pct":0.0,"put_gex_1pct":-1416273.0405774135,"net_gex_1pct":-1416273.0405774135,"gross_gex_1pct":1416273.0405774135,"call_oi":0,"put_oi":30},{"strike":35950.0,"call_gex_1pct":0.0,"put_gex_1pct":-482474.06171051465,"net_gex_1pct":-482474.06171051465,"gross_gex_1pct":482474.06171051465,"call_oi":0,"put_oi":10},{"strike":36000.0,"call_gex_1pct":353882.89576876716,"put_gex_1pct":-28109469.615861807,"net_gex_1pct":-27755586.72009304,"gross_gex_1pct":28463352.511630572,"call_oi":8,"put_oi":569},{"strike":36050.0,"call_gex_1pct":0.0,"put_gex_1pct":-555216.9365308378,"net_gex_1pct":-555216.9365308378,"gross_gex_1pct":555216.9365308378,"call_oi":0,"put_oi":11},{"strike":36100.0,"call_gex_1pct":0.0,"put_gex_1pct":-2845345.7413698714,"net_gex_1pct":-2845345.7413698714,"gross_gex_1pct":2845345.7413698714,"call_oi":0,"put_oi":55},{"strike":36150.0,"call_gex_1pct":0.0,"put_gex_1pct":-633621.4556342728,"net_gex_1pct":-633621.4556342728,"gross_gex_1pct":633621.4556342728,"call_oi":0,"put_oi":12},{"strike":36200.0,"call_gex_1pct":251806.44934226043,"put_gex_1pct":-1077199.695516452,"net_gex_1pct":-825393.2461741916,"gross_gex_1pct":1329006.1448587123,"call_oi":5,"put_oi":20},{"strike":36250.0,"call_gex_1pct":0.0,"put_gex_1pct":-826330.8494232583,"net_gex_1pct":-826330.8494232583,"gross_gex_1pct":826330.8494232583,"call_oi":0,"put_oi":15},{"strike":36300.0,"call_gex_1pct":0.0,"put_gex_1pct":-3041843.848702599,"net_gex_1pct":-3041843.848702599,"gross_gex_1pct":3041843.848702599,"call_oi":0,"put_oi":54},{"strike":36350.0,"call_gex_1pct":0.0,"put_gex_1pct":-633450.1543013012,"net_gex_1pct":-633450.1543013012,"gross_gex_1pct":633450.1543013012,"call_oi":0,"put_oi":11},{"strike":36400.0,"call_gex_1pct":55707.737789965664,"put_gex_1pct":-1763583.3391074932,"net_gex_1pct":-1707875.6013175275,"gross_gex_1pct":1819291.0768974589,"call_oi":1,"put_oi":30},{"strike":36450.0,"call_gex_1pct":0.0,"put_gex_1pct":-600630.4591164516,"net_gex_1pct":-600630.4591164516,"gross_gex_1pct":600630.4591164516,"call_oi":0,"put_oi":10},{"strike":36500.0,"call_gex_1pct":589310.5309676935,"put_gex_1pct":-9879634.496040309,"net_gex_1pct":-9290323.965072615,"gross_gex_1pct":10468945.027008003,"call_oi":10,"put_oi":161},{"strike":36550.0,"call_gex_1pct":121708.15328736427,"put_gex_1pct":-752096.9858653945,"net_gex_1pct":-630388.8325780302,"gross_gex_1pct":873805.1391527588,"call_oi":2,"put_oi":12},{"strike":36600.0,"call_gex_1pct":621995.3647903386,"put_gex_1pct":-2820034.9379269835,"net_gex_1pct":-2198039.573136645,"gross_gex_1pct":3442030.302717322,"call_oi":10,"put_oi":44},{"strike":36650.0,"call_gex_1pct":576839.9604542273,"put_gex_1pct":-916769.9789157936,"net_gex_1pct":-339930.0184615663,"gross_gex_1pct":1493609.9393700208,"call_oi":9,"put_oi":14},{"strike":36700.0,"call_gex_1pct":1114055.479099877,"put_gex_1pct":-936111.1898664051,"net_gex_1pct":177944.28923347185,"gross_gex_1pct":2050166.6689662822,"call_oi":17,"put_oi":14},{"strike":36750.0,"call_gex_1pct":0.0,"put_gex_1pct":-1638958.378788356,"net_gex_1pct":-1638958.378788356,"gross_gex_1pct":1638958.378788356,"call_oi":0,"put_oi":24},{"strike":36800.0,"call_gex_1pct":689490.4809486195,"put_gex_1pct":-4323877.806023824,"net_gex_1pct":-3634387.3250752045,"gross_gex_1pct":5013368.286972444,"call_oi":10,"put_oi":62},{"strike":36850.0,"call_gex_1pct":0.0,"put_gex_1pct":-926046.9780744498,"net_gex_1pct":-926046.9780744498,"gross_gex_1pct":926046.9780744498,"call_oi":0,"put_oi":13},{"strike":36900.0,"call_gex_1pct":797136.2857150567,"put_gex_1pct":-1890512.0123345288,"net_gex_1pct":-1093375.7266194723,"gross_gex_1pct":2687648.2980495854,"call_oi":11,"put_oi":26},{"strike":36950.0,"call_gex_1pct":74344.5229991378,"put_gex_1pct":-371278.99775982666,"net_gex_1pct":-296934.47476068884,"gross_gex_1pct":445623.52075896447,"call_oi":1,"put_oi":5},{"strike":37000.0,"call_gex_1pct":4495076.085818389,"put_gex_1pct":-39477490.03516134,"net_gex_1pct":-34982413.94934295,"gross_gex_1pct":43972566.12097973,"call_oi":59,"put_oi":521},{"strike":37050.0,"call_gex_1pct":0.0,"put_gex_1pct":-232208.04188882065,"net_gex_1pct":-232208.04188882065,"gross_gex_1pct":232208.04188882065,"call_oi":0,"put_oi":3},{"strike":37100.0,"call_gex_1pct":1118100.9379743738,"put_gex_1pct":-949247.2692412825,"net_gex_1pct":168853.66873309133,"gross_gex_1pct":2067348.2072156563,"call_oi":14,"put_oi":12},{"strike":37150.0,"call_gex_1pct":408546.2973958075,"put_gex_1pct":-402700.84636515036,"net_gex_1pct":5845.451030657161,"gross_gex_1pct":811247.1437609579,"call_oi":5,"put_oi":5},{"strike":37200.0,"call_gex_1pct":2092497.7714224544,"put_gex_1pct":-1804072.1685043722,"net_gex_1pct":288425.60291808215,"gross_gex_1pct":3896569.9399268264,"call_oi":25,"put_oi":22},{"strike":37250.0,"call_gex_1pct":0.0,"put_gex_1pct":-752717.355954091,"net_gex_1pct":-752717.355954091,"gross_gex_1pct":752717.355954091,"call_oi":0,"put_oi":9},{"strike":37300.0,"call_gex_1pct":958841.3990375777,"put_gex_1pct":-1450702.755407729,"net_gex_1pct":-491861.3563701513,"gross_gex_1pct":2409544.1544453064,"call_oi":11,"put_oi":17},{"strike":37350.0,"call_gex_1pct":1250550.1436028106,"put_gex_1pct":-1564151.3195625413,"net_gex_1pct":-313601.17595973075,"gross_gex_1pct":2814701.463165352,"call_oi":14,"put_oi":18},{"strike":37400.0,"call_gex_1pct":1367870.4711875587,"put_gex_1pct":-3802037.429200427,"net_gex_1pct":-2434166.9580128687,"gross_gex_1pct":5169907.900387986,"call_oi":15,"put_oi":43},{"strike":37450.0,"call_gex_1pct":187005.46961049095,"put_gex_1pct":-540915.7575408324,"net_gex_1pct":-353910.28793034144,"gross_gex_1pct":727921.2271513233,"call_oi":2,"put_oi":6},{"strike":37500.0,"call_gex_1pct":7157565.88891725,"put_gex_1pct":-20448726.731611118,"net_gex_1pct":-13291160.842693869,"gross_gex_1pct":27606292.620528366,"call_oi":75,"put_oi":223},{"strike":37550.0,"call_gex_1pct":10029441.16259888,"put_gex_1pct":-280111.2874634764,"net_gex_1pct":9749329.875135403,"gross_gex_1pct":10309552.450062357,"call_oi":103,"put_oi":3},{"strike":37600.0,"call_gex_1pct":131206040.86304978,"put_gex_1pct":-13431280.360255089,"net_gex_1pct":117774760.50279468,"gross_gex_1pct":144637321.22330487,"call_oi":1321,"put_oi":141},{"strike":37650.0,"call_gex_1pct":5469538.809910136,"put_gex_1pct":-1560490.3792436866,"net_gex_1pct":3909048.4306664495,"gross_gex_1pct":7030029.189153823,"call_oi":54,"put_oi":16},{"strike":37700.0,"call_gex_1pct":361651308.4521481,"put_gex_1pct":-12291007.902787225,"net_gex_1pct":349360300.5493609,"gross_gex_1pct":373942316.3549353,"call_oi":3502,"put_oi":125},{"strike":37750.0,"call_gex_1pct":315818.968425331,"put_gex_1pct":-6315635.777409247,"net_gex_1pct":-5999816.808983916,"gross_gex_1pct":6631454.745834578,"call_oi":3,"put_oi":63},{"strike":37800.0,"call_gex_1pct":150327377.78195152,"put_gex_1pct":-11430593.242587507,"net_gex_1pct":138896784.539364,"gross_gex_1pct":161757971.02453902,"call_oi":1401,"put_oi":112},{"strike":37850.0,"call_gex_1pct":328062.7202098663,"put_gex_1pct":-7020656.014973326,"net_gex_1pct":-6692593.294763459,"gross_gex_1pct":7348718.735183192,"call_oi":3,"put_oi":68},{"strike":37900.0,"call_gex_1pct":1989377.3883587185,"put_gex_1pct":-6742683.628935486,"net_gex_1pct":-4753306.240576767,"gross_gex_1pct":8732061.017294204,"call_oi":18,"put_oi":64},{"strike":37950.0,"call_gex_1pct":1013290.6549596308,"put_gex_1pct":-1502854.1284910971,"net_gex_1pct":-489563.4735314663,"gross_gex_1pct":2516144.783450728,"call_oi":9,"put_oi":14},{"strike":38000.0,"call_gex_1pct":9519347.510897517,"put_gex_1pct":-42982840.493130445,"net_gex_1pct":-33463492.98223293,"gross_gex_1pct":52502188.00402796,"call_oi":83,"put_oi":396},{"strike":38050.0,"call_gex_1pct":233666.56612970226,"put_gex_1pct":-773509.140366243,"net_gex_1pct":-539842.5742365407,"gross_gex_1pct":1007175.7064959452,"call_oi":2,"put_oi":7},{"strike":38100.0,"call_gex_1pct":235820.96408403353,"put_gex_1pct":-2446338.834494026,"net_gex_1pct":-2210517.8704099925,"gross_gex_1pct":2682159.7985780593,"call_oi":2,"put_oi":22},{"strike":38150.0,"call_gex_1pct":360269.63072328555,"put_gex_1pct":-909738.7263832585,"net_gex_1pct":-549469.0956599729,"gross_gex_1pct":1270008.357106544,"call_oi":3,"put_oi":8},{"strike":38200.0,"call_gex_1pct":1345490.6621152733,"put_gex_1pct":-3824596.0320457662,"net_gex_1pct":-2479105.3699304927,"gross_gex_1pct":5170086.69416104,"call_oi":11,"put_oi":33},{"strike":38250.0,"call_gex_1pct":370064.13121803664,"put_gex_1pct":-2092219.4428955421,"net_gex_1pct":-1722155.3116775055,"gross_gex_1pct":2462283.5741135785,"call_oi":3,"put_oi":18},{"strike":38300.0,"call_gex_1pct":628180.335649144,"put_gex_1pct":-2478112.034716754,"net_gex_1pct":-1849931.6990676103,"gross_gex_1pct":3106292.370365898,"call_oi":5,"put_oi":21},{"strike":38350.0,"call_gex_1pct":506610.4857472466,"put_gex_1pct":-2774712.960618577,"net_gex_1pct":-2268102.4748713304,"gross_gex_1pct":3281323.4463658235,"call_oi":4,"put_oi":23},{"strike":38400.0,"call_gex_1pct":1389613.9831358024,"put_gex_1pct":-1209220.9387751406,"net_gex_1pct":180393.04436066188,"gross_gex_1pct":2598834.921910943,"call_oi":11,"put_oi":10},{"strike":38450.0,"call_gex_1pct":6630307.0066929255,"put_gex_1pct":-1575353.1564133808,"net_gex_1pct":5054953.8502795445,"gross_gex_1pct":8205660.163106306,"call_oi":51,"put_oi":13},{"strike":38500.0,"call_gex_1pct":10218046.991927728,"put_gex_1pct":-9934613.01017228,"net_gex_1pct":283433.9817554485,"gross_gex_1pct":20152660.002100006,"call_oi":78,"put_oi":81},{"strike":38550.0,"call_gex_1pct":1467793.813337989,"put_gex_1pct":-748661.6995981006,"net_gex_1pct":719132.1137398883,"gross_gex_1pct":2216455.5129360897,"call_oi":11,"put_oi":6},{"strike":38600.0,"call_gex_1pct":1075494.9495628476,"put_gex_1pct":-757812.2291194476,"net_gex_1pct":317682.7204434,"gross_gex_1pct":1833307.1786822951,"call_oi":8,"put_oi":6},{"strike":38650.0,"call_gex_1pct":948030.8826606397,"put_gex_1pct":-1017433.5818240824,"net_gex_1pct":-69402.69916344271,"gross_gex_1pct":1965464.4644847221,"call_oi":7,"put_oi":8},{"strike":38700.0,"call_gex_1pct":486481511.10935163,"put_gex_1pct":-8616724.202380406,"net_gex_1pct":477864786.9069712,"gross_gex_1pct":495098235.31173205,"call_oi":3606,"put_oi":68},{"strike":38750.0,"call_gex_1pct":7558086.677839969,"put_gex_1pct":-128933.85122196676,"net_gex_1pct":7429152.826618003,"gross_gex_1pct":7687020.529061936,"call_oi":55,"put_oi":1},{"strike":38800.0,"call_gex_1pct":499814906.4090988,"put_gex_1pct":-16786032.726113494,"net_gex_1pct":483028873.6829853,"gross_gex_1pct":516600939.1352123,"call_oi":3611,"put_oi":130},{"strike":38850.0,"call_gex_1pct":11423529.003106924,"put_gex_1pct":-1293063.7443883743,"net_gex_1pct":10130465.25871855,"gross_gex_1pct":12716592.747495297,"call_oi":81,"put_oi":10},{"strike":38900.0,"call_gex_1pct":506198854.711029,"put_gex_1pct":-1052699.4289092834,"net_gex_1pct":505146155.2821197,"gross_gex_1pct":507251554.1399383,"call_oi":3605,"put_oi":8},{"strike":38950.0,"call_gex_1pct":1272827.5598750685,"put_gex_1pct":-3577025.852793553,"net_gex_1pct":-2304198.2929184847,"gross_gex_1pct":4849853.412668621,"call_oi":9,"put_oi":27},{"strike":39000.0,"call_gex_1pct":15752092.931083417,"put_gex_1pct":-14645289.247688575,"net_gex_1pct":1106803.6833948418,"gross_gex_1pct":30397382.17877199,"call_oi":108,"put_oi":111},{"strike":39050.0,"call_gex_1pct":1606496.9804659414,"put_gex_1pct":-934911.1041146698,"net_gex_1pct":671585.8763512715,"gross_gex_1pct":2541408.0845806114,"call_oi":11,"put_oi":7},{"strike":39100.0,"call_gex_1pct":215222484.0689287,"put_gex_1pct":-19152457.63483053,"net_gex_1pct":196070026.43409815,"gross_gex_1pct":234374941.70375922,"call_oi":1507,"put_oi":144},{"strike":39150.0,"call_gex_1pct":1892177.8656589973,"put_gex_1pct":-1472937.4684041485,"net_gex_1pct":419240.39725484885,"gross_gex_1pct":3365115.334063146,"call_oi":13,"put_oi":11},{"strike":39200.0,"call_gex_1pct":219919589.51060215,"put_gex_1pct":-14559815.423608154,"net_gex_1pct":205359774.086994,"gross_gex_1pct":234479404.9342103,"call_oi":1509,"put_oi":108},{"strike":39250.0,"call_gex_1pct":7168260.008222263,"put_gex_1pct":-6041075.9004640505,"net_gex_1pct":1127184.1077582128,"gross_gex_1pct":13209335.908686314,"call_oi":50,"put_oi":45},{"strike":39300.0,"call_gex_1pct":22513223.23086335,"put_gex_1pct":-8514922.626685398,"net_gex_1pct":13998300.604177954,"gross_gex_1pct":31028145.85754875,"call_oi":155,"put_oi":63},{"strike":39350.0,"call_gex_1pct":6958781.189369592,"put_gex_1pct":-5413180.4449700015,"net_gex_1pct":1545600.7443995904,"gross_gex_1pct":12371961.634339593,"call_oi":47,"put_oi":40},{"strike":39400.0,"call_gex_1pct":7237980.739187986,"put_gex_1pct":-3234223.878599077,"net_gex_1pct":4003756.8605889087,"gross_gex_1pct":10472204.617787063,"call_oi":50,"put_oi":24},{"strike":39450.0,"call_gex_1pct":5394620.2584707,"put_gex_1pct":-3001336.264364866,"net_gex_1pct":2393283.994105834,"gross_gex_1pct":8395956.522835566,"call_oi":37,"put_oi":22},{"strike":39500.0,"call_gex_1pct":14657720.433483928,"put_gex_1pct":-2048951.3802811133,"net_gex_1pct":12608769.053202815,"gross_gex_1pct":16706671.813765042,"call_oi":101,"put_oi":15},{"strike":39550.0,"call_gex_1pct":2940740.301855289,"put_gex_1pct":-680076.4008952258,"net_gex_1pct":2260663.900960063,"gross_gex_1pct":3620816.7027505147,"call_oi":20,"put_oi":5},{"strike":39600.0,"call_gex_1pct":6758425.368973535,"put_gex_1pct":-406316.5994270835,"net_gex_1pct":6352108.769546451,"gross_gex_1pct":7164741.968400618,"call_oi":47,"put_oi":3},{"strike":39650.0,"call_gex_1pct":3455308.466459385,"put_gex_1pct":-10908126.048093759,"net_gex_1pct":-7452817.581634373,"gross_gex_1pct":14363434.514553145,"call_oi":24,"put_oi":80},{"strike":39700.0,"call_gex_1pct":5477391.778868009,"put_gex_1pct":-1629220.2743095933,"net_gex_1pct":3848171.504558416,"gross_gex_1pct":7106612.053177603,"call_oi":38,"put_oi":12},{"strike":39750.0,"call_gex_1pct":4329204.75605989,"put_gex_1pct":-405563.3890460291,"net_gex_1pct":3923641.3670138605,"gross_gex_1pct":4734768.145105919,"call_oi":30,"put_oi":3},{"strike":39800.0,"call_gex_1pct":5489635.3397878315,"put_gex_1pct":-1065345.2063715071,"net_gex_1pct":4424290.133416325,"gross_gex_1pct":6554980.546159338,"call_oi":38,"put_oi":8},{"strike":39850.0,"call_gex_1pct":706673.0850319196,"put_gex_1pct":-938212.0314645984,"net_gex_1pct":-231538.94643267873,"gross_gex_1pct":1644885.116496518,"call_oi":5,"put_oi":7},{"strike":39900.0,"call_gex_1pct":2532142.8759180116,"put_gex_1pct":-132039.9795937749,"net_gex_1pct":2400102.896324237,"gross_gex_1pct":2664182.8555117864,"call_oi":18,"put_oi":1},{"strike":39950.0,"call_gex_1pct":1132739.3947500223,"put_gex_1pct":-131473.46414853894,"net_gex_1pct":1001265.9306014834,"gross_gex_1pct":1264212.8588985612,"call_oi":8,"put_oi":1},{"strike":40000.0,"call_gex_1pct":62145912.15231413,"put_gex_1pct":-2618067.327210139,"net_gex_1pct":59527844.82510399,"gross_gex_1pct":64763979.47952426,"call_oi":446,"put_oi":20},{"strike":40050.0,"call_gex_1pct":2758073.717706402,"put_gex_1pct":-390984.0365920969,"net_gex_1pct":2367089.681114305,"gross_gex_1pct":3149057.754298499,"call_oi":20,"put_oi":3},{"strike":40100.0,"call_gex_1pct":5732331.996001281,"put_gex_1pct":-128425.01042418374,"net_gex_1pct":5603906.985577097,"gross_gex_1pct":5860757.0064254645,"call_oi":42,"put_oi":1},{"strike":40150.0,"call_gex_1pct":679734.0494070528,"put_gex_1pct":-383549.818172519,"net_gex_1pct":296184.2312345338,"gross_gex_1pct":1063283.867579572,"call_oi":5,"put_oi":3},{"strike":40200.0,"call_gex_1pct":5123052.757817663,"put_gex_1pct":-1542607.8842416713,"net_gex_1pct":3580444.873575992,"gross_gex_1pct":6665660.642059335,"call_oi":38,"put_oi":12},{"strike":40250.0,"call_gex_1pct":1316269.2463670366,"put_gex_1pct":0.0,"net_gex_1pct":1316269.2463670366,"gross_gex_1pct":1316269.2463670366,"call_oi":10,"put_oi":0},{"strike":40300.0,"call_gex_1pct":9788189.260141082,"put_gex_1pct":-624122.9485726593,"net_gex_1pct":9164066.311568422,"gross_gex_1pct":10412312.208713742,"call_oi":74,"put_oi":5},{"strike":40350.0,"call_gex_1pct":5615962.7268771,"put_gex_1pct":-372631.5594073009,"net_gex_1pct":5243331.167469799,"gross_gex_1pct":5988594.286284401,"call_oi":43,"put_oi":3},{"strike":40400.0,"call_gex_1pct":5640647.430493302,"put_gex_1pct":-489645.8735764752,"net_gex_1pct":5151001.556916826,"gross_gex_1pct":6130293.304069777,"call_oi":44,"put_oi":4},{"strike":40450.0,"call_gex_1pct":1407249.0188479028,"put_gex_1pct":-603252.6579008972,"net_gex_1pct":803996.3609470056,"gross_gex_1pct":2010501.6767488,"call_oi":11,"put_oi":5},{"strike":40500.0,"call_gex_1pct":31460618.23993684,"put_gex_1pct":-6360431.300040048,"net_gex_1pct":25100186.939896792,"gross_gex_1pct":37821049.53997689,"call_oi":251,"put_oi":53},{"strike":40550.0,"call_gex_1pct":2122956.864830296,"put_gex_1pct":-236553.68576346018,"net_gex_1pct":1886403.179066836,"gross_gex_1pct":2359510.550593756,"call_oi":17,"put_oi":2},{"strike":40600.0,"call_gex_1pct":8565551.699640065,"put_gex_1pct":-233154.5173831134,"net_gex_1pct":8332397.182256952,"gross_gex_1pct":8798706.217023179,"call_oi":70,"put_oi":2},{"strike":40650.0,"call_gex_1pct":3369790.532767803,"put_gex_1pct":-114907.12169696135,"net_gex_1pct":3254883.4110708414,"gross_gex_1pct":3484697.6544647645,"call_oi":28,"put_oi":1},{"strike":40700.0,"call_gex_1pct":3581014.822894622,"put_gex_1pct":-114203.86609073263,"net_gex_1pct":3466810.9568038895,"gross_gex_1pct":3695218.6889853547,"call_oi":30,"put_oi":1},{"strike":40750.0,"call_gex_1pct":2338073.072471955,"put_gex_1pct":-337640.8245742603,"net_gex_1pct":2000432.2478976946,"gross_gex_1pct":2675713.897046215,"call_oi":20,"put_oi":3},{"strike":40800.0,"call_gex_1pct":8135866.826297584,"put_gex_1pct":-110913.213491178,"net_gex_1pct":8024953.612806406,"gross_gex_1pct":8246780.039788762,"call_oi":70,"put_oi":1},{"strike":40850.0,"call_gex_1pct":1476495.805945212,"put_gex_1pct":0.0,"net_gex_1pct":1476495.805945212,"gross_gex_1pct":1476495.805945212,"call_oi":13,"put_oi":0},{"strike":40900.0,"call_gex_1pct":8529288.004809922,"put_gex_1pct":0.0,"net_gex_1pct":8529288.004809922,"gross_gex_1pct":8529288.004809922,"call_oi":76,"put_oi":0},{"strike":40950.0,"call_gex_1pct":1984272.701268036,"put_gex_1pct":-106129.67768702215,"net_gex_1pct":1878143.0235810138,"gross_gex_1pct":2090402.378955058,"call_oi":18,"put_oi":1},{"strike":41000.0,"call_gex_1pct":55980583.78423642,"put_gex_1pct":-209134.53415264084,"net_gex_1pct":55771449.25008378,"gross_gex_1pct":56189718.318389066,"call_oi":517,"put_oi":2},{"strike":41050.0,"call_gex_1pct":2456223.771087556,"put_gex_1pct":0.0,"net_gex_1pct":2456223.771087556,"gross_gex_1pct":2456223.771087556,"call_oi":23,"put_oi":0},{"strike":41100.0,"call_gex_1pct":5852452.93345527,"put_gex_1pct":-507388.52437460184,"net_gex_1pct":5345064.409080668,"gross_gex_1pct":6359841.457829871,"call_oi":56,"put_oi":5},{"strike":41150.0,"call_gex_1pct":2160602.4406082164,"put_gex_1pct":0.0,"net_gex_1pct":2160602.4406082164,"gross_gex_1pct":2160602.4406082164,"call_oi":21,"put_oi":0},{"strike":41200.0,"call_gex_1pct":5863116.927828124,"put_gex_1pct":-98420.37691338977,"net_gex_1pct":5764696.550914734,"gross_gex_1pct":5961537.304741514,"call_oi":58,"put_oi":1},{"strike":41250.0,"call_gex_1pct":3074134.9856276554,"put_gex_1pct":0.0,"net_gex_1pct":3074134.9856276554,"gross_gex_1pct":3074134.9856276554,"call_oi":31,"put_oi":0},{"strike":41300.0,"call_gex_1pct":2822795.786785221,"put_gex_1pct":0.0,"net_gex_1pct":2822795.786785221,"gross_gex_1pct":2822795.786785221,"call_oi":29,"put_oi":0},{"strike":41350.0,"call_gex_1pct":2005700.544813451,"put_gex_1pct":0.0,"net_gex_1pct":2005700.544813451,"gross_gex_1pct":2005700.544813451,"call_oi":21,"put_oi":0},{"strike":41400.0,"call_gex_1pct":4964892.237754084,"put_gex_1pct":0.0,"net_gex_1pct":4964892.237754084,"gross_gex_1pct":4964892.237754084,"call_oi":53,"put_oi":0},{"strike":41500.0,"call_gex_1pct":24178521.214702398,"put_gex_1pct":-3193324.3262062366,"net_gex_1pct":20985196.88849616,"gross_gex_1pct":27371845.540908635,"call_oi":269,"put_oi":36},{"strike":41600.0,"call_gex_1pct":5781234.157176686,"put_gex_1pct":0.0,"net_gex_1pct":5781234.157176686,"gross_gex_1pct":5781234.157176686,"call_oi":67,"put_oi":0},{"strike":41700.0,"call_gex_1pct":2977591.8195780236,"put_gex_1pct":0.0,"net_gex_1pct":2977591.8195780236,"gross_gex_1pct":2977591.8195780236,"call_oi":36,"put_oi":0},{"strike":41800.0,"call_gex_1pct":4747833.680438051,"put_gex_1pct":-318893.376890624,"net_gex_1pct":4428940.303547427,"gross_gex_1pct":5066727.057328675,"call_oi":60,"put_oi":4},{"strike":41900.0,"call_gex_1pct":4007557.564457966,"put_gex_1pct":0.0,"net_gex_1pct":4007557.564457966,"gross_gex_1pct":4007557.564457966,"call_oi":53,"put_oi":0},{"strike":42000.0,"call_gex_1pct":36039147.007078245,"put_gex_1pct":-73910.50679890174,"net_gex_1pct":35965236.500279345,"gross_gex_1pct":36113057.513877146,"call_oi":499,"put_oi":1},{"strike":42100.0,"call_gex_1pct":2823931.0652761473,"put_gex_1pct":0.0,"net_gex_1pct":2823931.0652761473,"gross_gex_1pct":2823931.0652761473,"call_oi":41,"put_oi":0},{"strike":42200.0,"call_gex_1pct":6900921.62826412,"put_gex_1pct":0.0,"net_gex_1pct":6900921.62826412,"gross_gex_1pct":6900921.62826412,"call_oi":105,"put_oi":0},{"strike":42300.0,"call_gex_1pct":7281731.055836543,"put_gex_1pct":0.0,"net_gex_1pct":7281731.055836543,"gross_gex_1pct":7281731.055836543,"call_oi":117,"put_oi":0},{"strike":42400.0,"call_gex_1pct":9461628.18438782,"put_gex_1pct":0.0,"net_gex_1pct":9461628.18438782,"gross_gex_1pct":9461628.18438782,"call_oi":160,"put_oi":0},{"strike":42500.0,"call_gex_1pct":15789237.336801028,"put_gex_1pct":-60908.01564174179,"net_gex_1pct":15728329.321159286,"gross_gex_1pct":15850145.35244277,"call_oi":281,"put_oi":1},{"strike":42600.0,"call_gex_1pct":3188058.520479313,"put_gex_1pct":0.0,"net_gex_1pct":3188058.520479313,"gross_gex_1pct":3188058.520479313,"call_oi":60,"put_oi":0},{"strike":42700.0,"call_gex_1pct":3426821.734784933,"put_gex_1pct":0.0,"net_gex_1pct":3426821.734784933,"gross_gex_1pct":3426821.734784933,"call_oi":68,"put_oi":0},{"strike":42800.0,"call_gex_1pct":7725774.254142095,"put_gex_1pct":0.0,"net_gex_1pct":7725774.254142095,"gross_gex_1pct":7725774.254142095,"call_oi":162,"put_oi":0},{"strike":42900.0,"call_gex_1pct":6094113.316382019,"put_gex_1pct":0.0,"net_gex_1pct":6094113.316382019,"gross_gex_1pct":6094113.316382019,"call_oi":136,"put_oi":0},{"strike":43000.0,"call_gex_1pct":20150989.57156609,"put_gex_1pct":0.0,"net_gex_1pct":20150989.57156609,"gross_gex_1pct":20150989.57156609,"call_oi":467,"put_oi":0},{"strike":43100.0,"call_gex_1pct":3029824.475219563,"put_gex_1pct":0.0,"net_gex_1pct":3029824.475219563,"gross_gex_1pct":3029824.475219563,"call_oi":76,"put_oi":0},{"strike":43200.0,"call_gex_1pct":7012263.445909998,"put_gex_1pct":0.0,"net_gex_1pct":7012263.445909998,"gross_gex_1pct":7012263.445909998,"call_oi":185,"put_oi":0},{"strike":43300.0,"call_gex_1pct":4015473.078169165,"put_gex_1pct":0.0,"net_gex_1pct":4015473.078169165,"gross_gex_1pct":4015473.078169165,"call_oi":114,"put_oi":0},{"strike":43400.0,"call_gex_1pct":4766414.352020355,"put_gex_1pct":0.0,"net_gex_1pct":4766414.352020355,"gross_gex_1pct":4766414.352020355,"call_oi":143,"put_oi":0},{"strike":43500.0,"call_gex_1pct":9430789.653789658,"put_gex_1pct":0.0,"net_gex_1pct":9430789.653789658,"gross_gex_1pct":9430789.653789658,"call_oi":301,"put_oi":0},{"strike":43600.0,"call_gex_1pct":4329652.541127757,"put_gex_1pct":0.0,"net_gex_1pct":4329652.541127757,"gross_gex_1pct":4329652.541127757,"call_oi":146,"put_oi":0},{"strike":43700.0,"call_gex_1pct":2637885.5779515184,"put_gex_1pct":0.0,"net_gex_1pct":2637885.5779515184,"gross_gex_1pct":2637885.5779515184,"call_oi":97,"put_oi":0},{"strike":43800.0,"call_gex_1pct":25224410.81413306,"put_gex_1pct":0.0,"net_gex_1pct":25224410.81413306,"gross_gex_1pct":25224410.81413306,"call_oi":974,"put_oi":0},{"strike":43900.0,"call_gex_1pct":1786037.4408544023,"put_gex_1pct":0.0,"net_gex_1pct":1786037.4408544023,"gross_gex_1pct":1786037.4408544023,"call_oi":73,"put_oi":0},{"strike":44000.0,"call_gex_1pct":10401604.945806723,"put_gex_1pct":-34157.43429723591,"net_gex_1pct":10367447.511509487,"gross_gex_1pct":10435762.380103959,"call_oi":451,"put_oi":1},{"strike":44100.0,"call_gex_1pct":5707411.529630689,"put_gex_1pct":0.0,"net_gex_1pct":5707411.529630689,"gross_gex_1pct":5707411.529630689,"call_oi":268,"put_oi":0},{"strike":44200.0,"call_gex_1pct":7879528.909290331,"put_gex_1pct":0.0,"net_gex_1pct":7879528.909290331,"gross_gex_1pct":7879528.909290331,"call_oi":384,"put_oi":0},{"strike":44300.0,"call_gex_1pct":14673419.329406798,"put_gex_1pct":0.0,"net_gex_1pct":14673419.329406798,"gross_gex_1pct":14673419.329406798,"call_oi":782,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 38,200 | TAIFEX Proxy |
| 對應到期月份 | 202611F4 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-26→2026-11-27) | +1,200 | TAIFEX Proxy snapshots (2026-11-26) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 165,674 | 158,931 | +6,743 | 18,541 | 18,779 | -238 | +6,981 | TAIFEX Proxy |
| 投信 | 0 | 20,980 | -20,980 | 0 | 0 | +0 | -20,980 | TAIFEX Proxy |
| 自營商 | 135,851 | 129,877 | +5,974 | 17,143 | 18,661 | -1,518 | +7,492 | TAIFEX Proxy |
| 三大法人合計 | 301,525 | 309,788 | -8,263 | 35,684 | 37,440 | -1,756 | -6,507 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 17.14 | 11.39 | +5.75 | 3.25 | 3.27 | -0.02 | +5.77 | TAIFEX Proxy |
| 投信 | 0.00 | 12.07 | -12.07 | 0.00 | 0.00 | +0 | -12.07 | TAIFEX Proxy |
| 自營商 | 15.52 | 10.39 | +5.12 | 3.77 | 4.03 | -0.26 | +5.38 | TAIFEX Proxy |
| 三大法人合計 | 32.66 | 33.86 | -1.20 | 7.02 | 7.29 | -0.28 | -0.92 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 16,792 | TAIFEX Proxy |
| 買權空方 OI | 19,250 | TAIFEX Proxy |
| 買權多空淨 OI | -2,458 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-26→2026-11-27) | -86 | TAIFEX Proxy snapshots (2026-11-26) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 13,372 | TAIFEX Proxy |
| 賣權空方 OI | 15,575 | TAIFEX Proxy |
| 賣權多空淨 OI | -2,203 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-26→2026-11-27) | +235 | TAIFEX Proxy snapshots (2026-11-26) |
- 資料日期：買權 2026-11-27／賣權 2026-11-27 (TypeOfTraders=0 全部交易人；契約月份 202612)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -3,274 | 2026-11-26→2026-11-27 | TAIFEX Proxy snapshots (2026-11-26) |
| 買權前十大 | -86 | 2026-11-26→2026-11-27 | TAIFEX Proxy snapshots (2026-11-26) |
| 賣權前十大 | +235 | 2026-11-26→2026-11-27 | TAIFEX Proxy snapshots (2026-11-26) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-27；本次報告產製時間：2026-11-28 09:45:23；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：--force-rewrite 明示覆蓋（人工指定）
- 註記：同 T0 覆蓋：24 格以本次新抓取覆蓋（該 T0 尚無報告，無凍結對象）
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
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-27；估值 1247 檔；0 檔採最近有效收盤價；Blave 同 T0 交叉驗證 158.4150%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：亞洲主要指數資料日期落後 T0 2026-11-27，已將舊行情排除並標示 unavailable；原始資料日期：日經225 2026-11-26、韓國KOSPI 2026-11-26、香港恆生 2026-11-26、上海綜合 2026-11-26、深圳成分 2026-11-26
- 註記：台灣相關 ADR 新鮮度異常，已排除舊行情：台積電ADR（TSM，資料日期 2026-11-25；台積電ADR資料日期 2026-11-25 與美國最近已收盤交易日 2026-11-27 不一致）；聯電ADR（UMC，資料日期 2026-11-25；聯電ADR資料日期 2026-11-25 與美國最近已收盤交易日 2026-11-27 不一致）；日月光ADR（ASX，資料日期 2026-11-25；日月光ADR資料日期 2026-11-25 與美國最近已收盤交易日 2026-11-27 不一致）
<!-- ADR_STALE_SYMBOLS:TSM -->
<!-- ADR_STALE_SYMBOLS:UMC -->
<!-- ADR_STALE_SYMBOLS:ASX -->
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；0 檔採最近有效收盤價。Blave 同 T0 交叉驗證 158.4150%；差異 0.000 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- TAIFEX 註記：futures-price-after-hours 日期 2026-11-27 非今日 2026-11-30，視為無新節次，不採用
- TAIFEX 註記：法人交易量未提供前日變化端點；日盤、夜盤交易量及日夜淨額差仍照常列示
- TAIFEX 註記：Gamma GEX 實際使用到期月份 202612W1（到期日 2026-12-02）與 Options Key Levels 主到期月份 202611F4 不同；GEX 數值應以實際使用到期月份為準
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -296.3 | -107,503 | -79 | +1,211 | +6,743 | -238 | 避險／對沖 | 對沖避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +85.2 | +104,355 | -565 | +0 | -20,980 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -2.0 | -3,566 | -1,147 | -87 | +5,974 | -1,518 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
