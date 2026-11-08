# DATA_REPORT_20261106

- 報告日期：`2026-11-08`
- T0 交易日期：`2026-11-06`
- 資料產出時間：`2026-11-08 10:38:08`
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
| 加權指數 | 39,701.64 | 點 | twse-proxy |
| 開盤 | 38,915.76 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 40,435.83 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 37,837.05 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 39,701.64 | 點 | twse-proxy |
| 漲跌點數 | -1,873.08 | 點 | twse-proxy |
| 漲跌幅 | -4.51 | % | twse-proxy |
| 成交金額 | 13,210.7 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 105 | twse-proxy |
| 下跌家數 | 952 | twse-proxy |
| 平盤家數 | 27 | twse-proxy |
| 漲停家數 | 4 | twse-proxy |
| 跌停家數 | 24 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 104 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 733 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 38 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 14 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 29 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `twse-proxy /institutional`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | -911.9 | 億元 | twse-proxy /institutional |
| 投信 | +266.9 | 億元 | twse-proxy /institutional |
| 自營商 | -494.8 | 億元 | twse-proxy /institutional |
| 三大法人合計 | -1,139.7 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)` (金額口徑)；維持率 `TWSE 上市自建估算（當日暫估；資料日期：2026-11-06；估值 1240 檔；3 檔採最近有效收盤價（價格日期 20260402 至 20261106）；Blave 同 T0 交叉驗證 151.9300%；差異 0.209 個百分點；門檻 <1.00 個百分點；PASS）`；官方無每日維持率序列

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 7,040.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資增減 | -564.2 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券餘額 | 272,748 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融券增減 | -40,371 | 張 | HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整) |
| 融資維持率 | 152.14 | % | TWSE 上市自建估算（當日暫估；資料日期：2026-11-06；估值 1240 檔；3 檔採最近有效收盤價（價格日期 20260402 至 20261106）；Blave 同 T0 交叉驗證 151.9300%；差異 0.209 個百分點；門檻 <1.00 個百分點；PASS） |

### 5. 借券資料

**資料來源：** 各欄位依實際取得市場分別標示；借券賣出餘額／增減使用上市 TWT93U 與上櫃 tpex_margin_sbl，缺值市場不納入加總。

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 整體市場借券餘額 | 33,203,111 | 張 | TWSE TWT72U（SLBNLB；上市+上櫃） |

| 項目 | 上市 | 上櫃 | 兩者合計 | 單位 |
|---|---|---|---|---|
| 借券賣出餘額 | 18,225,070 | 2,189,311 | 20,414,381 | 張 |
| 借券賣出增減 | 358,193 | 2,818 | 361,010 | 張 |

- 上市來源：TWSE TWT93U（上市）；增減來源：TWSE TWT93U（上市）
- 上櫃來源：TPEx S47（上櫃）；增減來源：TPEx S47（上櫃）
- 借券賣出餘額完整性：`complete`
- 借券賣出增減完整性：`complete`
- TWSE TWT93U（上市）：資料日期：`20261106`；最後預定更新：`23:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-08T11:04:51+08:00`；狀態：`available_after_schedule`
- TPEx S47（上櫃）：資料日期：`20261106`；最後預定更新：`22:30`；來源回報產製時間：`unavailable`；本次查詢時間：`2026-11-08T11:04:54+08:00`；狀態：`available_after_schedule`

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 13,210.7 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 1,643.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 14,854.6 | 億元 | twse-proxy market_statistics／TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,376.86 | 23.13 | +0.31 | 2026-11-06 | 2026-11-08T02:38:28+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 24,579.43 | 264.43 | +1.09 | 2026-11-06 | 2026-11-08T02:38:28+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 26,989.99 | 360.18 | +1.35 | 2026-11-06 | 2026-11-08T02:38:28+00:00 | America/New_York | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,285.73 | -237.33 | -0.46 | 2026-11-06 | 2026-11-08T02:38:28+00:00 | America/New_York | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 9,390.25 | 379.11 | +4.21 | 2026-11-06 | 2026-11-08T02:38:28+00:00 | America/New_York | Yahoo Finance Chart API |
| VIX | ^VIX | 25.64 | -2.54 | -9.01 | 2026-11-06 | 2026-11-08T02:38:28+00:00 | America/Chicago | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 日經225 | ^N225 | 57,434.77 | -3,643.13 | -5.96 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Asia/Tokyo | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 5,059.69 | -324.11 | -6.02 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Asia/Seoul | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,481.86 | -315.12 | -1.27 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Asia/Hong_Kong | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,649.18 | -40.73 | -1.10 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Asia/Shanghai | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 11,175.78 | -295.31 | -2.57 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Asia/Shanghai | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,402.00 | 19.00 | +0.26 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 27,085.25 | 333.25 | +1.25 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,385.00 | -230.00 | -0.45 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,760.50 | 25.10 | +0.92 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率（%） | 日變化（百分點） | 資料日期 | 擷取時間（UTC） | 資料來源 |
|---|---|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.51 | 0.05 | 06-NOV-26 | 2026-11-08T02:38:51+00:00 | U.S. Treasury yield.xml（BC_2YEAR 備援） |
| 美國 10 年期殖利率 | 10 Yr | 4.86 | 0.02 | 2026-11-06 | 2026-11-08T02:38:51+00:00 | Yahoo Finance (備援) |
| 美國 20 年期殖利率 | 20 Yr | 5.29 | 0.02 | 06-NOV-26 | 2026-11-08T02:39:09+00:00 | U.S. Treasury yield.xml（BC_20YEAR 備援） |
| 美國 30 年期殖利率 | 30 Yr | 5.26 | 0.01 | 2026-11-06 | 2026-11-08T02:39:09+00:00 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| USD/TWD | TWD=X | 33.11 | 0.29 | +0.88 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Europe/London | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.30 | 0.75 | +0.74 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.43 | 0.93 | +0.59 | 2026-11-07 | 2026-11-08T02:38:29+00:00 | Europe/London | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,356.34 | 16.27 | +1.21 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | Europe/London | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 台積電ADR | TSM | 375.44 | 22.34 | +6.33 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| 聯電ADR | UMC | 13.85 | 0.47 | +3.51 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| 日月光ADR | ASX | 31.63 | 1.91 | +6.43 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌值 | 漲跌幅 | 資料日期（交易所時區） | 擷取時間（UTC） | 交易所時區 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 90.83 | 0.31 | +0.34 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,074.90 | -38.60 | -0.94 | 2026-11-06 | 2026-11-08T02:38:29+00:00 | America/New_York | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 75,636.59 | -110.34 | -0.15 | 2026-11-08 | 2026-11-08T02:38:29+00:00 | UTC | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：｜配息基金推薦｜
  - 來源：Yahoo 台股；發布時間：2026-11-03T03:03:12Z；台北時間：2026-11-03 11:03
  - 摘要：對於習慣領月薪的上班族來說，「每月配息」的基金特別有吸引力。不過，許多人在找「月配息基金推薦」或「2026 配息基金推薦名單」時，往往只注意配息率高低、以及能否每月穩定領息。
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%9C%88%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E9%85%8D%E6%81%AF%E5%9F%BA%E9%87%91%E6%8E%A8%E8%96%A6%E6%80%8E%E9%BA%BC%E6%8C%91%EF%BC%9F4%E5%A4%A7%E6%8C%91%E9%81%B8%E9%87%8D%E9%BB%9E%E4%B8%80%E6%AC%A1%E7%9C%8B-030312577.html
- 事件2：陳珮騏為動保燒5000萬「完全沒存款」　靠愛國情操買股賺30％
  - 來源：Yahoo 台股；發布時間：2026-11-07T16:20:29Z；台北時間：2026-11-08 00:20
  - 摘要：陳珮騏昨（11╱7）擔任精品燕窩品牌「皇燕の恵」一日店長，與粉絲近距離互動，投入動保15年的她坦言：「我捐出去的或是我照顧的這些毛孩，金額超過5000萬，比我現在住的那間房子還貴，所以我完全沒有存款。」還好有股票被動收入，即使這幾天台股綠油
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%99%B3%E7%8F%AE%E9%A8%8F%E7%82%BA%E5%8B%95%E4%BF%9D%E7%87%925000%E8%90%AC-%E5%AE%8C%E5%85%A8%E6%B2%92%E5%AD%98%E6%AC%BE-%E9%9D%A0%E6%84%9B%E5%9C%8B%E6%83%85%E6%93%8D%E8%B2%B7%E8%82%A1%E8%B3%BA30-162029136.html
- 事件3：陳珮騏投入動保15年燒光5000萬！沒存款全靠股市 買1檔飆漲30％
  - 來源：Yahoo 台股；發布時間：2026-11-07T08:29:09Z；台北時間：2026-11-07 16:29
  - 摘要：陳珮騏今出席燕窩品牌代言活動，她提到接連拍兩檔三立八點檔，收工回家包包一丟下、內衣一脫，就要花6小時馬不停蹄照顧兩隻16歲老病愛犬，都靠一天喝4瓶燕窩保養身體。她是圈內眾所皆知的愛狗人士，從2011年投入動保至今，投入的錢已經超過5000萬
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%99%B3%E7%8F%AE%E9%A8%8F%E6%8A%95%E5%85%A5%E5%8B%95%E4%BF%9D15%E5%B9%B4%E7%87%92%E5%85%895000%E8%90%AC-%E6%B2%92%E5%AD%98%E6%AC%BE%E5%85%A8%E9%9D%A0%E8%82%A1%E5%B8%82-%E8%B2%B71%E6%AA%94%E9%A3%86%E6%BC%B230-082909939.html
- 事件4：台股跌逾20％想認賠！他問「短期盤整可以先賣再立刻買回嗎」 鄉民急勸：別亂動
  - 來源：Yahoo 台股；發布時間：2026-11-07T05:17:00Z；台北時間：2026-11-07 13:17
  - 摘要：[FTNN新聞網]實習記者周宗怡／綜合報導台股近期重挫，6日更收在39,701.64點，下跌1873.08點。一名投資人透露，自己連續2次單筆買進市值型ETF，都買在歷史相對...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E8%B7%8C%E9%80%BE20-%E6%83%B3%E8%AA%8D%E8%B3%A0-%E4%BB%96%E5%95%8F-%E7%9F%AD%E6%9C%9F%E7%9B%A4%E6%95%B4%E5%8F%AF%E4%BB%A5%E5%85%88%E8%B3%A3%E5%86%8D%E7%AB%8B%E5%88%BB%E8%B2%B7%E5%9B%9E%E5%97%8E-%E9%84%89%E6%B0%91%E6%80%A5%E5%8B%B8-051700431.html
- 事件5：台股急跌想借錢加碼！他考慮「理財型房貸投入市值型ETF」　鄉民曝風險
  - 來源：Yahoo 台股；發布時間：2026-11-07T04:46:00Z；台北時間：2026-11-07 12:46
  - 摘要：[FTNN新聞網]實習記者周宗怡／綜合報導台股昨（6）日盤中狂瀉3737.67點，終場重挫1873.08點、收在39,701.64點，失守4萬點大關，讓部分投資人開始思考是否該「...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%80%A5%E8%B7%8C%E6%83%B3%E5%80%9F%E9%8C%A2%E5%8A%A0%E7%A2%BC-%E4%BB%96%E8%80%83%E6%85%AE-%E7%90%86%E8%B2%A1%E5%9E%8B%E6%88%BF%E8%B2%B8%E6%8A%95%E5%85%A5%E5%B8%82%E5%80%BC%E5%9E%8Betf-%E9%84%89%E6%B0%91%E6%9B%9D%E9%A2%A8%E9%9A%AA-044600022.html
- 事件6：台股急跌正5族卻越跌越買！他質疑「跌20%了也打死不退嗎」　投資人搖頭：本多終勝
  - 來源：Yahoo 台股；發布時間：2026-11-07T04:16:00Z；台北時間：2026-11-07 12:16
  - 摘要：[FTNN新聞網]實習記者周宗怡／綜合報導台股近期出現劇烈修正，採取高槓桿投資人卻仍持續加碼，引發市場關注。一名網友觀察融資融券數據後，好奇正5族群為何在...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E6%80%A5%E8%B7%8C%E6%AD%A35%E6%97%8F%E5%8D%BB%E8%B6%8A%E8%B7%8C%E8%B6%8A%E8%B2%B7-%E4%BB%96%E8%B3%AA%E7%96%91-%E8%B7%8C20-%E4%BA%86%E4%B9%9F%E6%89%93%E6%AD%BB%E4%B8%8D%E9%80%80%E5%97%8E-%E6%8A%95%E8%B3%87%E4%BA%BA%E6%90%96%E9%A0%AD-041600846.html
- 事件7：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 來源：Federal Reserve；發布時間：Thu, 5 Nov 2026 16:00:00 GMT；台北時間：2026-11-06 00:00
  - 摘要：Federal Reserve Board announces termination of enforcement action with Allegiant United Holdings, LLC, Nano Financial Holdings, Inc., and Nano Banc
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261105a.htm
- 事件8：Berkshire shares surge as Wall Street swoons amid AI fears
  - 來源：CNBC；發布時間：Sat, 07 Nov 2026 14:06:20 GMT；台北時間：2026-11-07 22:06
  - 摘要：Berkshire Hathaway shares roared past the S&P 500 index this week and are outperforming the benchmark for the year-to-date.
  - 原文連結：https://www.cnbc.com/2026/11/07/berkshire-shares-surge-as-wall-street-swoons-amid-ai-fears.html
- 事件9：Why the prognosis for healthcare stocks is uncertain ahead of Congress’ new makeup
  - 來源：CNBC；發布時間：Sat, 07 Nov 2026 16:02:33 GMT；台北時間：2026-11-08 00:02
  - 摘要：Healthcare stocks may struggle to find momentum as the Democrats get ready to take over Congress.
  - 原文連結：https://www.cnbc.com/2026/11/07/healthcare-stocks-may-face-trouble-due-to-midterm-results.html
- 事件10：Watch the Annual Meeting: Cramer on the fate of the AI buildout and stocks to buy now
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 19:36:12 GMT；台北時間：2026-11-07 03:36
  - 摘要：At the Investing Club's 4th annual meeting, Cramer also reveals his outlook for 2027 and answers questions from the live audience and members at home.
  - 原文連結：https://www.cnbc.com/investingclub/2026/11/06/watch-jim-cramer-live.html
- 事件11：Democrat shaping AI policy bought chip stocks despite backing congressional trading ban
  - 來源：CNBC；發布時間：Sat, 07 Nov 2026 13:30:01 GMT；台北時間：2026-11-07 21:30
  - 摘要：Rep. Josh Gottheimer disclosed new AI-linked stock purchases months after voting for a congressional trading ban, as Democrats prepare to regulate the
  - 原文連結：https://www.cnbc.com/2026/11/07/josh-gottheimer-ai-stocks-congress-trading-ban.html
- 事件12：Mississippi Senate: Longshot Ty Pinkins says he aimed to spoil Hyde-Smith, boost Colom vote
  - 來源：CNBC；發布時間：Fri, 06 Nov 2026 19:44:33 GMT；台北時間：2026-11-07 03:44
  - 摘要：Ty Pinkins said he avoided campaigning in heavily Black areas of Mississippi to avoid harming chances for Democrat Scott Colom, who, like him, is Blac
  - 原文連結：https://www.cnbc.com/2026/11/06/mississippi-senate-ty-pinkins-colom-hyde-smith.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202611 (日盤成交量最大者)；交易日期：2026-11-06

### 1．台指期近月日盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 38,888 | 點 | TAIFEX Proxy |
| 最高價 | 40,690 | 點 | TAIFEX Proxy |
| 最低價 | 37,694 | 點 | TAIFEX Proxy |
| 收盤價 | 39,786 | 點 | TAIFEX Proxy |
| 漲跌點數 | -2,096 | 點 | TAIFEX Proxy |
| 漲跌幅 | -5.00 | % | TAIFEX Proxy |
| 成交量 | 143,277 | 口 | TAIFEX Proxy |
| 日盤高點及低點 | 40,690 / 37,694 | 點 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 開盤價 | 39,742 | 點 | TAIFEX Proxy |
| 最高價 | 40,845 | 點 | TAIFEX Proxy |
| 最低價 | 39,129 | 點 | TAIFEX Proxy |
| 收盤價 | 40,298 | 點 | TAIFEX Proxy |
| 漲跌點數 | +646 | 點 | TAIFEX Proxy |
| 漲跌幅 | +1.63 | % | TAIFEX Proxy |
| 成交量 | 69,882 | 口 | TAIFEX Proxy |
| 夜盤高點及低點 | 40,845 / 39,129 | 點 | TAIFEX Proxy |
| 結算價 | unavailable | 點 | unavailable |
| 未平倉量 | unavailable | 口 | unavailable |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 15,873 | TAIFEX Proxy |
| 外資空方 OI | 115,803 | TAIFEX Proxy |
| 外資多空淨 OI | -99,930 | TAIFEX Proxy |
| 投信多方 OI | 94,158 | TAIFEX Proxy |
| 投信空方 OI | 3,721 | TAIFEX Proxy |
| 投信多空淨 OI | +90,437 | TAIFEX Proxy |
| 自營商多方 OI | 6,022 | TAIFEX Proxy |
| 自營商空方 OI | 4,342 | TAIFEX Proxy |
| 自營商多空淨 OI | +1,680 | TAIFEX Proxy |
| 三大法人合計多方 OI | 116,053 | TAIFEX Proxy |
| 三大法人合計空方 OI | 123,866 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -7,813 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | -4,279 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +154 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -650 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures`（備援 TAIFEX Proxy；欄位依實際取得來源標示）

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 102,490 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,600 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,890 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-11-04→2026-11-06) | -4,372 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：2026-11-06 (TypeOfTraders=0 全部交易人；契約月份 202611)

### 5．日盤、夜盤法人交易資料

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 外資日盤多單交易量 | 140,566 | 口 | TAIFEX Proxy |
| 外資日盤空單交易量 | 144,876 | 口 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | -4,310 | 口 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 41,133 | 口 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 42,246 | 口 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,113 | 口 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -3,197 | 口 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +154 | 口 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | 口 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +154 | 口 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -875 | 口 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -406 | 口 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -469 | 口 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | -5,031 | 口 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -1,519 | 口 | TAIFEX Proxy |
| 法人日盤交易金額淨額 | -390.3 | 億元 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 | -123.6 | 億元 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 39,786 | TAIFEX Proxy |
| 加權指數價格 | 39,701.64 | twse-proxy |
| 台指期與加權指數價差 | +84.36 | TAIFEX Proxy／twse-proxy |
| 價差百分比 | +0.21 | TAIFEX Proxy／twse-proxy |
| 日盤基差 | +84.36 | TAIFEX Proxy／twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +512 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 39,786 | 40,298 | -512 | TAIFEX Proxy |
| 成交量 | 143,277 | 69,882 | +73,395 | TAIFEX Proxy |
- 台指期總 OI 前日變化：-4,775（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 140,566 | 144,876 | -4,310 | 41,133 | 42,246 | -1,113 | -3,197 | 15,873 | 115,803 | -99,930 | -4,279 | TAIFEX Proxy |
| 投信 | 1,275 | 1,121 | +154 | 0 | 0 | +0 | +154 | 94,158 | 3,721 | +90,437 | +154 | TAIFEX Proxy |
| 自營商 | 18,917 | 19,792 | -875 | 1,991 | 2,397 | -406 | -469 | 6,022 | 4,342 | +1,680 | -650 | TAIFEX Proxy |
| 三大法人合計 | 160,758 | 165,789 | -5,031 | 43,124 | 44,643 | -1,519 | -3,512 | 116,053 | 123,866 | -7,813 | -4,775 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 102,490 | TAIFEX Proxy |
| 前十大交易人空方 OI | 93,600 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +8,890 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-11-04→2026-11-06) | -4,372 | TAIFEX Proxy snapshots (2026-11-05) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 32.78% | TAIFEX Proxy |
| 夜盤漲跌點數 | +646 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -1,113 | TAIFEX Proxy |
| 劇本分類 | 劇本二 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏空 | 規則對應 |
| 劇本特徵 | 先漲、小心開高走低 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與報告產製時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-11-06 | TAIFEX Proxy |
| 到期月份／到期日 | 202611F1 | TAIFEX Proxy |
| 報告產製時間 | 2026-11-08 10:38:08 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 502,306 | TAIFEX Proxy |
| Call 總未平倉量 OI | 138,851 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 393,781 | TAIFEX Proxy |
| Put 總未平倉量 OI | 82,744 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| Call／Put 成交量比例 | 1.28 | 倍 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.68 | 倍 | TAIFEX Proxy |
| Put／Call Ratio | 0.60 | 倍 | TAIFEX Proxy |
| Call／Put 成交量比例變化 (2026-11-05→2026-11-06) | 3.22 | 百分點（pp） | TAIFEX Proxy |
| Call／Put OI 比例變化 (2026-11-05→2026-11-06) | -4.36 | 百分點（pp） | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 160,272 | TAIFEX Proxy |
| 外資 Call日賣 | 161,721 | TAIFEX Proxy |
| 外資 Call日淨 | -1,449 | TAIFEX Proxy |
| 外資 Put日買 | 129,399 | TAIFEX Proxy |
| 外資 Put日賣 | 132,239 | TAIFEX Proxy |
| 外資 Put日淨 | -2,840 | TAIFEX Proxy |
| 外資 Call夜買 | 11,803 | TAIFEX Proxy |
| 外資 Call夜賣 | 11,695 | TAIFEX Proxy |
| 外資 Call夜淨 | +108 | TAIFEX Proxy |
| 外資 Put夜買 | 9,946 | TAIFEX Proxy |
| 外資 Put夜賣 | 9,941 | TAIFEX Proxy |
| 外資 Put夜淨 | +5 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,391 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -1,557 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | -2,845 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 113,529 | TAIFEX Proxy |
| 自營商 Call日賣 | 135,263 | TAIFEX Proxy |
| 自營商 Call日淨 | -21,734 | TAIFEX Proxy |
| 自營商 Put日買 | 95,740 | TAIFEX Proxy |
| 自營商 Put日賣 | 105,967 | TAIFEX Proxy |
| 自營商 Put日淨 | -10,227 | TAIFEX Proxy |
| 自營商 Call夜買 | 14,346 | TAIFEX Proxy |
| 自營商 Call夜賣 | 12,375 | TAIFEX Proxy |
| 自營商 Call夜淨 | +1,971 | TAIFEX Proxy |
| 自營商 Put夜買 | 10,572 | TAIFEX Proxy |
| 自營商 Put夜賣 | 11,338 | TAIFEX Proxy |
| 自營商 Put夜淨 | -766 | TAIFEX Proxy |
| 自營商 日盤淨總量 | -11,507 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -23,705 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -9,461 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 40,000 | 4,752 | TAIFEX Proxy |
| Call OI 第2大履約價 | 46,500 | 4,631 | TAIFEX Proxy |
| Call OI 第3大履約價 | 43,000 | 4,055 | TAIFEX Proxy |
| Call OI 最大履約價 | 40,000 | 4,752 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202611F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 40,000 | 4,752 | 3.42% | TAIFEX Proxy |
| C2 | 46,500 | 4,631 | 3.34% | TAIFEX Proxy |
| C3 | 43,000 | 4,055 | 2.92% | TAIFEX Proxy |
| C4 | 46,000 | 3,846 | 2.77% | TAIFEX Proxy |
| C5 | 44,000 | 3,765 | 2.71% | TAIFEX Proxy |
| C6 | 40,100 | 3,607 | 2.6% | TAIFEX Proxy |
| C7 | 42,000 | 3,607 | 2.6% | TAIFEX Proxy |
| C8 | 41,000 | 3,497 | 2.52% | TAIFEX Proxy |
| C9 | 45,000 | 3,376 | 2.43% | TAIFEX Proxy |
| C10 | 44,500 | 3,325 | 2.39% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 37,400 | 10,404 | TAIFEX Proxy |
| Put OI 第2大履約價 | 37,500 | 7,588 | TAIFEX Proxy |
| Put OI 第3大履約價 | 39,000 | 3,371 | TAIFEX Proxy |
| Put OI 最大履約價 | 37,400 | 10,404 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202611F1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 37,400 | 10,404 | 12.57% | TAIFEX Proxy |
| P2 | 37,500 | 7,588 | 9.17% | TAIFEX Proxy |
| P3 | 39,000 | 3,371 | 4.07% | TAIFEX Proxy |
| P4 | 39,700 | 3,253 | 3.93% | TAIFEX Proxy |
| P5 | 37,600 | 2,951 | 3.57% | TAIFEX Proxy |
| P6 | 39,800 | 2,689 | 3.25% | TAIFEX Proxy |
| P7 | 39,600 | 2,577 | 3.11% | TAIFEX Proxy |
| P8 | 38,600 | 2,478 | 2.99% | TAIFEX Proxy |
| P9 | 38,000 | 2,096 | 2.53% | TAIFEX Proxy |
| P10 | 39,500 | 1,969 | 2.38% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | unavailable | 端點未提供 |
| Call OI 減少最多的履約價 | unavailable | 端點未提供 |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | unavailable | 端點未提供 |
| Put OI 減少最多的履約價 | unavailable | 端點未提供 |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 40,000 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -6,500 | TAIFEX Proxy snapshots (2026-11-05) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 37,400 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -2,600 | TAIFEX Proxy snapshots (2026-11-05) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 38,900.00 | TAIFEX Proxy (options-gamma-levels) |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | unavailable |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 資料日期 | 2026-11-06 | TAIFEX Proxy (options-gamma-levels) |

### 14A．GEX 整體曝險與履約價分布

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Net GEX（標的變動 1%） | 1,992,264,865.97 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| Gross GEX（標的變動 1%） | 3,397,641,282.50 NT$ | TAIFEX Gamma model；NT$／標的變動 1% |
| 模型品質 | usable | Black-Scholes Gamma using TAIFEX settlement-implied volatility |
| 履約價資料筆數 | 223 | 資料日期：2026-11-06 |
| 正 Net GEX 最大履約價 | 38,900 | 依 Net GEX 排序 |
| 負 Net GEX 最低履約價 | 37,400 | 依 Net GEX 排序 |
- 正 Net GEX Top 5：38,900（145,556,830.10 NT$）、38,700（141,606,510.22 NT$）、38,800（141,516,197.97 NT$）、41,000（128,167,834.55 NT$）、38,400（127,877,492.25 NT$）
- 負 Net GEX Top 5：37,400（-40,642,927.91 NT$）、39,000（-14,541,122.57 NT$）、38,000（-13,834,440.46 NT$）、37,600（-12,518,341.48 NT$）、37,500（-11,425,108.23 NT$）

#### GEX_LEVELS_JSON（僅衍生後逐履約價 GEX，不含原始報價；GEX 單位 NT$／標的變動 1%）

```json
{"date":"2026-11-06","underlying":39701.64,"unit":"NTD per 1% underlying move","model":"Black-Scholes Gamma using TAIFEX settlement-implied volatility","quality":"usable","net_gex_1pct":1992264865.9714477,"gross_gex_1pct":3397641282.4984756,"levels":[{"strike":37400.0,"call_gex_1pct":0.0,"put_gex_1pct":-40642927.9116353,"net_gex_1pct":-40642927.9116353,"gross_gex_1pct":40642927.9116353,"call_oi":0,"put_oi":521},{"strike":37500.0,"call_gex_1pct":0.0,"put_gex_1pct":-11425108.232211836,"net_gex_1pct":-11425108.232211836,"gross_gex_1pct":11425108.232211836,"call_oi":0,"put_oi":140},{"strike":37600.0,"call_gex_1pct":0.0,"put_gex_1pct":-12518341.479264924,"net_gex_1pct":-12518341.479264924,"gross_gex_1pct":12518341.479264924,"call_oi":0,"put_oi":147},{"strike":37700.0,"call_gex_1pct":0.0,"put_gex_1pct":-9254470.546544962,"net_gex_1pct":-9254470.546544962,"gross_gex_1pct":9254470.546544962,"call_oi":0,"put_oi":104},{"strike":37800.0,"call_gex_1pct":43403964.792058975,"put_gex_1pct":-32528099.006986108,"net_gex_1pct":10875865.785072867,"gross_gex_1pct":75932063.79904509,"call_oi":1002,"put_oi":353},{"strike":37900.0,"call_gex_1pct":65441680.18908248,"put_gex_1pct":-6017757.379706215,"net_gex_1pct":59423922.80937627,"gross_gex_1pct":71459437.56878869,"call_oi":1000,"put_oi":63},{"strike":38000.0,"call_gex_1pct":2954633.477417232,"put_gex_1pct":-16789073.932502273,"net_gex_1pct":-13834440.455085041,"gross_gex_1pct":19743707.409919504,"call_oi":33,"put_oi":170},{"strike":38100.0,"call_gex_1pct":109000279.56968272,"put_gex_1pct":-4639071.037914368,"net_gex_1pct":104361208.53176835,"gross_gex_1pct":113639350.60759708,"call_oi":1003,"put_oi":45},{"strike":38200.0,"call_gex_1pct":119173317.84044191,"put_gex_1pct":-9568397.93077569,"net_gex_1pct":109604919.90966623,"gross_gex_1pct":128741715.7712176,"call_oi":1000,"put_oi":92},{"strike":38300.0,"call_gex_1pct":131234069.12941542,"put_gex_1pct":-9083095.848154923,"net_gex_1pct":122150973.2812605,"gross_gex_1pct":140317164.97757035,"call_oi":1000,"put_oi":84},{"strike":38400.0,"call_gex_1pct":140002818.4052287,"put_gex_1pct":-12125326.159388361,"net_gex_1pct":127877492.24584034,"gross_gex_1pct":152128144.56461707,"call_oi":1000,"put_oi":111},{"strike":38500.0,"call_gex_1pct":7529649.211149774,"put_gex_1pct":-11745237.69586472,"net_gex_1pct":-4215588.484714947,"gross_gex_1pct":19274886.907014493,"call_oi":51,"put_oi":104},{"strike":38600.0,"call_gex_1pct":155475151.2924947,"put_gex_1pct":-29601130.213810965,"net_gex_1pct":125874021.07868375,"gross_gex_1pct":185076281.5063057,"call_oi":1016,"put_oi":257},{"strike":38700.0,"call_gex_1pct":153876149.02936074,"put_gex_1pct":-12269638.81414063,"net_gex_1pct":141606510.21522012,"gross_gex_1pct":166145787.84350136,"call_oi":1000,"put_oi":105},{"strike":38800.0,"call_gex_1pct":161350140.7670674,"put_gex_1pct":-19833942.799376022,"net_gex_1pct":141516197.9676914,"gross_gex_1pct":181184083.5664434,"call_oi":1000,"put_oi":169},{"strike":38900.0,"call_gex_1pct":163226663.3683283,"put_gex_1pct":-17669833.267579734,"net_gex_1pct":145556830.10074857,"gross_gex_1pct":180896496.63590804,"call_oi":1003,"put_oi":150},{"strike":39000.0,"call_gex_1pct":8841716.463852521,"put_gex_1pct":-23382839.033929903,"net_gex_1pct":-14541122.570077382,"gross_gex_1pct":32224555.497782424,"call_oi":54,"put_oi":195},{"strike":39100.0,"call_gex_1pct":9501692.214820787,"put_gex_1pct":-3608314.868638673,"net_gex_1pct":5893377.346182114,"gross_gex_1pct":13110007.08345946,"call_oi":57,"put_oi":30},{"strike":39200.0,"call_gex_1pct":2509825.7874202444,"put_gex_1pct":-3393843.987505733,"net_gex_1pct":-884018.2000854886,"gross_gex_1pct":5903669.774925977,"call_oi":15,"put_oi":28},{"strike":39300.0,"call_gex_1pct":3524835.5357572483,"put_gex_1pct":-3889132.3069100804,"net_gex_1pct":-364296.7711528321,"gross_gex_1pct":7413967.842667328,"call_oi":21,"put_oi":32},{"strike":39400.0,"call_gex_1pct":11218113.337671118,"put_gex_1pct":-6364531.143913976,"net_gex_1pct":4853582.193757142,"gross_gex_1pct":17582644.481585093,"call_oi":68,"put_oi":53},{"strike":39500.0,"call_gex_1pct":5751016.6009965325,"put_gex_1pct":-15216314.947638007,"net_gex_1pct":-9465298.346641473,"gross_gex_1pct":20967331.54863454,"call_oi":35,"put_oi":127},{"strike":39600.0,"call_gex_1pct":5653885.6293857675,"put_gex_1pct":-12011745.559900725,"net_gex_1pct":-6357859.930514958,"gross_gex_1pct":17665631.189286493,"call_oi":35,"put_oi":100},{"strike":39700.0,"call_gex_1pct":10103461.106153753,"put_gex_1pct":-4213529.068374099,"net_gex_1pct":5889932.037779653,"gross_gex_1pct":14316990.174527852,"call_oi":64,"put_oi":36},{"strike":39800.0,"call_gex_1pct":31019724.633792773,"put_gex_1pct":-5820874.227884982,"net_gex_1pct":25198850.40590779,"gross_gex_1pct":36840598.86167775,"call_oi":196,"put_oi":51},{"strike":39900.0,"call_gex_1pct":12458913.836249437,"put_gex_1pct":-3117747.7681200346,"net_gex_1pct":9341166.068129402,"gross_gex_1pct":15576661.604369473,"call_oi":81,"put_oi":27},{"strike":40000.0,"call_gex_1pct":45516724.1357959,"put_gex_1pct":-17050940.320920523,"net_gex_1pct":28465783.814875375,"gross_gex_1pct":62567664.45671642,"call_oi":297,"put_oi":150},{"strike":40100.0,"call_gex_1pct":12293576.11866341,"put_gex_1pct":-3388044.2116825283,"net_gex_1pct":8905531.906980881,"gross_gex_1pct":15681620.330345938,"call_oi":81,"put_oi":30},{"strike":40200.0,"call_gex_1pct":7919057.437386683,"put_gex_1pct":-3702745.9767965656,"net_gex_1pct":4216311.460590118,"gross_gex_1pct":11621803.414183248,"call_oi":53,"put_oi":33},{"strike":40300.0,"call_gex_1pct":6362645.520124444,"put_gex_1pct":-9282795.747857695,"net_gex_1pct":-2920150.2277332516,"gross_gex_1pct":15645441.26798214,"call_oi":44,"put_oi":84},{"strike":40350.0,"call_gex_1pct":18235430.820160586,"put_gex_1pct":-3304643.4217647207,"net_gex_1pct":14930787.398395866,"gross_gex_1pct":21540074.241925307,"call_oi":126,"put_oi":30},{"strike":40400.0,"call_gex_1pct":7241348.0366488015,"put_gex_1pct":-9772176.353844196,"net_gex_1pct":-2530828.317195394,"gross_gex_1pct":17013524.390492998,"call_oi":50,"put_oi":89},{"strike":40450.0,"call_gex_1pct":2292683.116843193,"put_gex_1pct":-1736230.1390385667,"net_gex_1pct":556452.9778046261,"gross_gex_1pct":4028913.2558817593,"call_oi":16,"put_oi":16},{"strike":40500.0,"call_gex_1pct":145145685.30985424,"put_gex_1pct":-55272169.28577477,"net_gex_1pct":89873516.02407947,"gross_gex_1pct":200417854.595629,"call_oi":1035,"put_oi":511},{"strike":40550.0,"call_gex_1pct":2530422.122137834,"put_gex_1pct":-1401568.412397719,"net_gex_1pct":1128853.7097401149,"gross_gex_1pct":3931990.534535553,"call_oi":18,"put_oi":13},{"strike":40600.0,"call_gex_1pct":4867888.290101542,"put_gex_1pct":-9377974.851070276,"net_gex_1pct":-4510086.560968733,"gross_gex_1pct":14245863.141171817,"call_oi":35,"put_oi":88},{"strike":40650.0,"call_gex_1pct":2749033.7177228886,"put_gex_1pct":-1911922.6323621536,"net_gex_1pct":837111.085360735,"gross_gex_1pct":4660956.350085042,"call_oi":20,"put_oi":18},{"strike":40700.0,"call_gex_1pct":138015434.67895144,"put_gex_1pct":-44731597.172697,"net_gex_1pct":93283837.50625443,"gross_gex_1pct":182747031.85164845,"call_oi":1015,"put_oi":426},{"strike":40750.0,"call_gex_1pct":3090464.512986458,"put_gex_1pct":-2180107.791900011,"net_gex_1pct":910356.7210864471,"gross_gex_1pct":5270572.304886469,"call_oi":23,"put_oi":21},{"strike":40800.0,"call_gex_1pct":6876816.171736366,"put_gex_1pct":-4759467.252426187,"net_gex_1pct":2117348.9193101795,"gross_gex_1pct":11636283.424162552,"call_oi":52,"put_oi":46},{"strike":40850.0,"call_gex_1pct":3796788.876946189,"put_gex_1pct":-1636859.1779424555,"net_gex_1pct":2159929.6990037337,"gross_gex_1pct":5433648.054888644,"call_oi":29,"put_oi":16},{"strike":40900.0,"call_gex_1pct":130139065.1911284,"put_gex_1pct":-52301250.43831797,"net_gex_1pct":77837814.75281043,"gross_gex_1pct":182440315.6294464,"call_oi":1009,"put_oi":517},{"strike":40950.0,"call_gex_1pct":2162016.6118252864,"put_gex_1pct":-1700738.0996141494,"net_gex_1pct":461278.512211137,"gross_gex_1pct":3862754.711439436,"call_oi":17,"put_oi":17},{"strike":41000.0,"call_gex_1pct":149341865.004647,"put_gex_1pct":-21174030.450064313,"net_gex_1pct":128167834.55458267,"gross_gex_1pct":170515895.4547113,"call_oi":1191,"put_oi":214},{"strike":41050.0,"call_gex_1pct":2491636.47647661,"put_gex_1pct":-295777.34299141064,"net_gex_1pct":2195859.1334851994,"gross_gex_1pct":2787413.819468021,"call_oi":20,"put_oi":3},{"strike":41100.0,"call_gex_1pct":125162078.3856391,"put_gex_1pct":-27108214.242198765,"net_gex_1pct":98053864.14344034,"gross_gex_1pct":152270292.62783787,"call_oi":1028,"put_oi":278},{"strike":41150.0,"call_gex_1pct":2278160.554108047,"put_gex_1pct":-385793.6693546171,"net_gex_1pct":1892366.8847534298,"gross_gex_1pct":2663954.223462664,"call_oi":19,"put_oi":4},{"strike":41200.0,"call_gex_1pct":5549107.164173914,"put_gex_1pct":-8109180.486557361,"net_gex_1pct":-2560073.3223834466,"gross_gex_1pct":13658287.650731275,"call_oi":47,"put_oi":85},{"strike":41250.0,"call_gex_1pct":929907.796846183,"put_gex_1pct":-283115.45830937295,"net_gex_1pct":646792.3385368101,"gross_gex_1pct":1213023.255155556,"call_oi":8,"put_oi":3},{"strike":41300.0,"call_gex_1pct":7660569.045606421,"put_gex_1pct":-1680420.0921183217,"net_gex_1pct":5980148.953488099,"gross_gex_1pct":9340989.137724742,"call_oi":67,"put_oi":18},{"strike":41350.0,"call_gex_1pct":1687850.8868573257,"put_gex_1pct":-184711.74216723724,"net_gex_1pct":1503139.1446900885,"gross_gex_1pct":1872562.629024563,"call_oi":15,"put_oi":2},{"strike":41400.0,"call_gex_1pct":1987808.0285374434,"put_gex_1pct":-12882976.829993093,"net_gex_1pct":-10895168.80145565,"gross_gex_1pct":14870784.858530536,"call_oi":18,"put_oi":141},{"strike":41450.0,"call_gex_1pct":108448.3704242214,"put_gex_1pct":0.0,"net_gex_1pct":108448.3704242214,"gross_gex_1pct":108448.3704242214,"call_oi":1,"put_oi":0},{"strike":41500.0,"call_gex_1pct":19913596.54099179,"put_gex_1pct":-7154541.867108222,"net_gex_1pct":12759054.673883568,"gross_gex_1pct":27068138.408100013,"call_oi":187,"put_oi":80},{"strike":41550.0,"call_gex_1pct":417589.8284478063,"put_gex_1pct":0.0,"net_gex_1pct":417589.8284478063,"gross_gex_1pct":417589.8284478063,"call_oi":4,"put_oi":0},{"strike":41600.0,"call_gex_1pct":7701624.899984442,"put_gex_1pct":-1392126.584641492,"net_gex_1pct":6309498.31534295,"gross_gex_1pct":9093751.484625934,"call_oi":75,"put_oi":16},{"strike":41650.0,"call_gex_1pct":503732.88787283126,"put_gex_1pct":-430471.18543423864,"net_gex_1pct":73261.70243859262,"gross_gex_1pct":934204.07330707,"call_oi":5,"put_oi":5},{"strike":41700.0,"call_gex_1pct":6710773.752662926,"put_gex_1pct":-1788983.782690541,"net_gex_1pct":4921789.969972385,"gross_gex_1pct":8499757.535353467,"call_oi":68,"put_oi":21},{"strike":41750.0,"call_gex_1pct":2813812.5613597417,"put_gex_1pct":-421468.21711111604,"net_gex_1pct":2392344.3442486254,"gross_gex_1pct":3235280.778470858,"call_oi":29,"put_oi":5},{"strike":41800.0,"call_gex_1pct":7997444.839197639,"put_gex_1pct":-1492976.851907521,"net_gex_1pct":6504467.987290118,"gross_gex_1pct":9490421.69110516,"call_oi":84,"put_oi":18},{"strike":41850.0,"call_gex_1pct":2145649.0840291525,"put_gex_1pct":-410392.50643690105,"net_gex_1pct":1735256.5775922514,"gross_gex_1pct":2556041.5904660537,"call_oi":23,"put_oi":5},{"strike":41900.0,"call_gex_1pct":4114803.9461988215,"put_gex_1pct":-3248816.059967121,"net_gex_1pct":865987.8862317004,"gross_gex_1pct":7363620.006165942,"call_oi":45,"put_oi":40},{"strike":41950.0,"call_gex_1pct":1702007.8842355448,"put_gex_1pct":-1205523.3952148964,"net_gex_1pct":496484.4890206484,"gross_gex_1pct":2907531.2794504412,"call_oi":19,"put_oi":15},{"strike":42000.0,"call_gex_1pct":79589976.72966453,"put_gex_1pct":-10919322.040122416,"net_gex_1pct":68670654.68954211,"gross_gex_1pct":90509298.76978695,"call_oi":907,"put_oi":138},{"strike":42050.0,"call_gex_1pct":2491030.493230242,"put_gex_1pct":-782995.7239667013,"net_gex_1pct":1708034.7692635404,"gross_gex_1pct":3274026.2171969432,"call_oi":29,"put_oi":10},{"strike":42100.0,"call_gex_1pct":2187173.7015270567,"put_gex_1pct":-1542278.212434761,"net_gex_1pct":644895.4890922958,"gross_gex_1pct":3729451.9139618175,"call_oi":26,"put_oi":20},{"strike":42150.0,"call_gex_1pct":1564313.2999577178,"put_gex_1pct":-610493.7061450921,"net_gex_1pct":953819.5938126256,"gross_gex_1pct":2174807.0061028097,"call_oi":19,"put_oi":8},{"strike":42200.0,"call_gex_1pct":5316574.906257015,"put_gex_1pct":-1585765.4324173362,"net_gex_1pct":3730809.473839679,"gross_gex_1pct":6902340.338674351,"call_oi":66,"put_oi":21},{"strike":42250.0,"call_gex_1pct":1575003.638818912,"put_gex_1pct":-892783.467603963,"net_gex_1pct":682220.171214949,"gross_gex_1pct":2467787.106422875,"call_oi":20,"put_oi":12},{"strike":42300.0,"call_gex_1pct":5862800.302408387,"put_gex_1pct":-1619640.8037598524,"net_gex_1pct":4243159.4986485345,"gross_gex_1pct":7482441.106168239,"call_oi":76,"put_oi":22},{"strike":42350.0,"call_gex_1pct":301049.9667707555,"put_gex_1pct":-145109.5775615225,"net_gex_1pct":155940.38920923296,"gross_gex_1pct":446159.54433227796,"call_oi":4,"put_oi":2},{"strike":42400.0,"call_gex_1pct":2793118.162380833,"put_gex_1pct":-1292303.5030304927,"net_gex_1pct":1500814.6593503405,"gross_gex_1pct":4085421.665411326,"call_oi":38,"put_oi":18},{"strike":42450.0,"call_gex_1pct":504339.07737003855,"put_gex_1pct":0.0,"net_gex_1pct":504339.07737003855,"gross_gex_1pct":504339.07737003855,"call_oi":7,"put_oi":0},{"strike":42500.0,"call_gex_1pct":13742630.980891498,"put_gex_1pct":-1960882.9512872067,"net_gex_1pct":11781748.029604292,"gross_gex_1pct":15703513.932178704,"call_oi":196,"put_oi":28},{"strike":42550.0,"call_gex_1pct":1634630.8719555577,"put_gex_1pct":-485013.07940629154,"net_gex_1pct":1149617.7925492662,"gross_gex_1pct":2119643.9513618494,"call_oi":24,"put_oi":7},{"strike":42600.0,"call_gex_1pct":4545058.967790556,"put_gex_1pct":-1366523.819482514,"net_gex_1pct":3178535.1483080424,"gross_gex_1pct":5911582.78727307,"call_oi":68,"put_oi":20},{"strike":42650.0,"call_gex_1pct":1307016.8401762005,"put_gex_1pct":-202788.29136864137,"net_gex_1pct":1104228.548807559,"gross_gex_1pct":1509805.131544842,"call_oi":20,"put_oi":3},{"strike":42700.0,"call_gex_1pct":20891322.49836039,"put_gex_1pct":-533395.3467460257,"net_gex_1pct":20357927.151614364,"gross_gex_1pct":21424717.84510642,"call_oi":327,"put_oi":8},{"strike":42750.0,"call_gex_1pct":871463.059217159,"put_gex_1pct":-328883.3786548627,"net_gex_1pct":542579.6805622964,"gross_gex_1pct":1200346.4378720217,"call_oi":14,"put_oi":5},{"strike":42800.0,"call_gex_1pct":4941220.784257102,"put_gex_1pct":-1106229.5052507396,"net_gex_1pct":3834991.279006362,"gross_gex_1pct":6047450.289507842,"call_oi":82,"put_oi":17},{"strike":42850.0,"call_gex_1pct":234801.17548475522,"put_gex_1pct":-898949.4322758986,"net_gex_1pct":-664148.2567911434,"gross_gex_1pct":1133750.6077606538,"call_oi":4,"put_oi":14},{"strike":42900.0,"call_gex_1pct":3241870.7064535823,"put_gex_1pct":-1651423.2781465242,"net_gex_1pct":1590447.428307058,"gross_gex_1pct":4893293.984600106,"call_oi":57,"put_oi":26},{"strike":42950.0,"call_gex_1pct":4947790.407052561,"put_gex_1pct":-1379153.096929916,"net_gex_1pct":3568637.3101226445,"gross_gex_1pct":6326943.503982477,"call_oi":89,"put_oi":22},{"strike":43000.0,"call_gex_1pct":38961976.94903507,"put_gex_1pct":-4084196.0398245337,"net_gex_1pct":34877780.90921054,"gross_gex_1pct":43046172.9888596,"call_oi":719,"put_oi":66},{"strike":43050.0,"call_gex_1pct":894899.482293551,"put_gex_1pct":-612077.4565875187,"net_gex_1pct":282822.0257060323,"gross_gex_1pct":1506976.9388810697,"call_oi":17,"put_oi":10},{"strike":43100.0,"call_gex_1pct":15421990.322469551,"put_gex_1pct":-1631662.5956423953,"net_gex_1pct":13790327.726827156,"gross_gex_1pct":17053652.918111946,"call_oi":299,"put_oi":27},{"strike":43150.0,"call_gex_1pct":894612.1186161811,"put_gex_1pct":-1193496.26912754,"net_gex_1pct":-298884.150511359,"gross_gex_1pct":2088108.3877437213,"call_oi":18,"put_oi":20},{"strike":43200.0,"call_gex_1pct":17954483.711367022,"put_gex_1pct":-1416441.1759876648,"net_gex_1pct":16538042.535379358,"gross_gex_1pct":19370924.887354687,"call_oi":373,"put_oi":24},{"strike":43250.0,"call_gex_1pct":420767.81110597536,"put_gex_1pct":-582898.9175342795,"net_gex_1pct":-162131.10642830416,"gross_gex_1pct":1003666.7286402548,"call_oi":9,"put_oi":10},{"strike":43300.0,"call_gex_1pct":2916775.1673465944,"put_gex_1pct":-748519.8543337178,"net_gex_1pct":2168255.3130128765,"gross_gex_1pct":3665295.021680312,"call_oi":64,"put_oi":13},{"strike":43350.0,"call_gex_1pct":751454.9916589308,"put_gex_1pct":-910993.114251299,"net_gex_1pct":-159538.12259236816,"gross_gex_1pct":1662448.1059102297,"call_oi":17,"put_oi":16},{"strike":43400.0,"call_gex_1pct":2336322.9324401505,"put_gex_1pct":-562519.9373794979,"net_gex_1pct":1773802.9950606525,"gross_gex_1pct":2898842.8698196486,"call_oi":54,"put_oi":10},{"strike":43450.0,"call_gex_1pct":746147.0609477543,"put_gex_1pct":-833737.9600941788,"net_gex_1pct":-87590.89914642449,"gross_gex_1pct":1579885.021041933,"call_oi":18,"put_oi":15},{"strike":43500.0,"call_gex_1pct":15479142.916828945,"put_gex_1pct":-878850.6053564049,"net_gex_1pct":14600292.31147254,"gross_gex_1pct":16357993.52218535,"call_oi":384,"put_oi":16},{"strike":43550.0,"call_gex_1pct":1507152.6146139873,"put_gex_1pct":-325852.64673685963,"net_gex_1pct":1181299.9678771277,"gross_gex_1pct":1833005.2613508468,"call_oi":38,"put_oi":6},{"strike":43600.0,"call_gex_1pct":2737245.893478249,"put_gex_1pct":-590457.8456090817,"net_gex_1pct":2146788.0478691673,"gross_gex_1pct":3327703.739087331,"call_oi":71,"put_oi":11},{"strike":43650.0,"call_gex_1pct":4128873.7370290887,"put_gex_1pct":-583671.7122378936,"net_gex_1pct":3545202.024791195,"gross_gex_1pct":4712545.449266982,"call_oi":111,"put_oi":11},{"strike":43700.0,"call_gex_1pct":3031937.715123145,"put_gex_1pct":-577033.2451149373,"net_gex_1pct":2454904.4700082075,"gross_gex_1pct":3608970.9602380823,"call_oi":84,"put_oi":11},{"strike":43750.0,"call_gex_1pct":526995.756457789,"put_gex_1pct":-259335.3520447961,"net_gex_1pct":267660.4044129929,"gross_gex_1pct":786331.1085025851,"call_oi":15,"put_oi":5},{"strike":43800.0,"call_gex_1pct":3760078.3274064204,"put_gex_1pct":-512743.68809035997,"net_gex_1pct":3247334.6393160606,"gross_gex_1pct":4272822.01549678,"call_oi":110,"put_oi":10},{"strike":43850.0,"call_gex_1pct":1196712.3458129882,"put_gex_1pct":-507044.40164072986,"net_gex_1pct":689667.9441722584,"gross_gex_1pct":1703756.747453718,"call_oi":36,"put_oi":10},{"strike":43900.0,"call_gex_1pct":2197117.7392219855,"put_gex_1pct":-150439.49318588956,"net_gex_1pct":2046678.246036096,"gross_gex_1pct":2347557.232407875,"call_oi":68,"put_oi":3},{"strike":43950.0,"call_gex_1pct":1035778.2745674788,"put_gex_1pct":0.0,"net_gex_1pct":1035778.2745674788,"gross_gex_1pct":1035778.2745674788,"call_oi":33,"put_oi":0},{"strike":44000.0,"call_gex_1pct":31081322.26360485,"put_gex_1pct":-588781.4643029295,"net_gex_1pct":30492540.79930192,"gross_gex_1pct":31670103.72790778,"call_oi":1015,"put_oi":12},{"strike":44050.0,"call_gex_1pct":2881882.051744216,"put_gex_1pct":0.0,"net_gex_1pct":2881882.051744216,"gross_gex_1pct":2881882.051744216,"call_oi":96,"put_oi":0},{"strike":44100.0,"call_gex_1pct":1317568.6693094636,"put_gex_1pct":0.0,"net_gex_1pct":1317568.6693094636,"gross_gex_1pct":1317568.6693094636,"call_oi":45,"put_oi":0},{"strike":44150.0,"call_gex_1pct":889785.6357580381,"put_gex_1pct":0.0,"net_gex_1pct":889785.6357580381,"gross_gex_1pct":889785.6357580381,"call_oi":31,"put_oi":0},{"strike":44200.0,"call_gex_1pct":3089147.541366618,"put_gex_1pct":-141093.12441420343,"net_gex_1pct":2948054.416952415,"gross_gex_1pct":3230240.6657808213,"call_oi":111,"put_oi":3},{"strike":44250.0,"call_gex_1pct":566180.096011461,"put_gex_1pct":0.0,"net_gex_1pct":566180.096011461,"gross_gex_1pct":566180.096011461,"call_oi":21,"put_oi":0},{"strike":44300.0,"call_gex_1pct":2374562.643038786,"put_gex_1pct":-92021.82055263172,"net_gex_1pct":2282540.8224861543,"gross_gex_1pct":2466584.4635914178,"call_oi":91,"put_oi":2},{"strike":44350.0,"call_gex_1pct":1337107.5371336625,"put_gex_1pct":0.0,"net_gex_1pct":1337107.5371336625,"gross_gex_1pct":1337107.5371336625,"call_oi":53,"put_oi":0},{"strike":44400.0,"call_gex_1pct":3754004.745948348,"put_gex_1pct":-45084.353567211685,"net_gex_1pct":3708920.3923811363,"gross_gex_1pct":3799089.09951556,"call_oi":153,"put_oi":1},{"strike":44450.0,"call_gex_1pct":190803.3068937026,"put_gex_1pct":0.0,"net_gex_1pct":190803.3068937026,"gross_gex_1pct":190803.3068937026,"call_oi":8,"put_oi":0},{"strike":44500.0,"call_gex_1pct":10783303.514448343,"put_gex_1pct":-220964.21659017776,"net_gex_1pct":10562339.297858166,"gross_gex_1pct":11004267.73103852,"call_oi":469,"put_oi":5},{"strike":44550.0,"call_gex_1pct":317480.54875875864,"put_gex_1pct":0.0,"net_gex_1pct":317480.54875875864,"gross_gex_1pct":317480.54875875864,"call_oi":14,"put_oi":0},{"strike":44600.0,"call_gex_1pct":1652050.5020126926,"put_gex_1pct":-43334.47330042692,"net_gex_1pct":1608716.0287122657,"gross_gex_1pct":1695384.9753131196,"call_oi":77,"put_oi":1},{"strike":44650.0,"call_gex_1pct":249407.51868217182,"put_gex_1pct":0.0,"net_gex_1pct":249407.51868217182,"gross_gex_1pct":249407.51868217182,"call_oi":12,"put_oi":0},{"strike":44700.0,"call_gex_1pct":893729.5308958348,"put_gex_1pct":-169649.70467234842,"net_gex_1pct":724079.8262234863,"gross_gex_1pct":1063379.2355681832,"call_oi":44,"put_oi":4},{"strike":44750.0,"call_gex_1pct":275113.216156097,"put_gex_1pct":-84016.20323801016,"net_gex_1pct":191097.01291808684,"gross_gex_1pct":359129.4193941072,"call_oi":14,"put_oi":2},{"strike":44800.0,"call_gex_1pct":2544928.3209248413,"put_gex_1pct":-208055.43330779628,"net_gex_1pct":2336872.887617045,"gross_gex_1pct":2752983.7542326376,"call_oi":134,"put_oi":5},{"strike":44850.0,"call_gex_1pct":128341.01567395282,"put_gex_1pct":0.0,"net_gex_1pct":128341.01567395282,"gross_gex_1pct":128341.01567395282,"call_oi":7,"put_oi":0},{"strike":44900.0,"call_gex_1pct":822852.1042313171,"put_gex_1pct":-40838.22604652206,"net_gex_1pct":782013.878184795,"gross_gex_1pct":863690.3302778391,"call_oi":46,"put_oi":1},{"strike":44950.0,"call_gex_1pct":568787.8874771827,"put_gex_1pct":-40462.01678126157,"net_gex_1pct":528325.8706959211,"gross_gex_1pct":609249.9042584442,"call_oi":33,"put_oi":1},{"strike":45000.0,"call_gex_1pct":31789611.71549233,"put_gex_1pct":-120277.16805354452,"net_gex_1pct":31669334.547438785,"gross_gex_1pct":31909888.883545876,"call_oi":1917,"put_oi":3},{"strike":45050.0,"call_gex_1pct":1469794.657421078,"put_gex_1pct":0.0,"net_gex_1pct":1469794.657421078,"gross_gex_1pct":1469794.657421078,"call_oi":91,"put_oi":0},{"strike":45100.0,"call_gex_1pct":1006431.0779295333,"put_gex_1pct":0.0,"net_gex_1pct":1006431.0779295333,"gross_gex_1pct":1006431.0779295333,"call_oi":64,"put_oi":0},{"strike":45150.0,"call_gex_1pct":301540.04252990725,"put_gex_1pct":0.0,"net_gex_1pct":301540.04252990725,"gross_gex_1pct":301540.04252990725,"call_oi":20,"put_oi":0},{"strike":45200.0,"call_gex_1pct":1539144.5939056957,"put_gex_1pct":-116029.32683002281,"net_gex_1pct":1423115.267075673,"gross_gex_1pct":1655173.9207357184,"call_oi":105,"put_oi":3},{"strike":45250.0,"call_gex_1pct":484308.0034636846,"put_gex_1pct":-38337.32833923146,"net_gex_1pct":445970.67512445315,"gross_gex_1pct":522645.331802916,"call_oi":34,"put_oi":1},{"strike":45300.0,"call_gex_1pct":1359487.5020044139,"put_gex_1pct":0.0,"net_gex_1pct":1359487.5020044139,"gross_gex_1pct":1359487.5020044139,"call_oi":100,"put_oi":0},{"strike":45350.0,"call_gex_1pct":342828.60027464374,"put_gex_1pct":0.0,"net_gex_1pct":342828.60027464374,"gross_gex_1pct":342828.60027464374,"call_oi":26,"put_oi":0},{"strike":45400.0,"call_gex_1pct":332274.61331402516,"put_gex_1pct":-37223.065144964545,"net_gex_1pct":295051.5481690606,"gross_gex_1pct":369497.6784589897,"call_oi":26,"put_oi":1},{"strike":45450.0,"call_gex_1pct":99014.25470798707,"put_gex_1pct":0.0,"net_gex_1pct":99014.25470798707,"gross_gex_1pct":99014.25470798707,"call_oi":8,"put_oi":0},{"strike":45500.0,"call_gex_1pct":9557125.038534729,"put_gex_1pct":-73182.77089837601,"net_gex_1pct":9483942.267636353,"gross_gex_1pct":9630307.809433104,"call_oi":798,"put_oi":2},{"strike":45550.0,"call_gex_1pct":1099923.4237458475,"put_gex_1pct":-108849.59133125682,"net_gex_1pct":991073.8324145908,"gross_gex_1pct":1208773.0150771043,"call_oi":95,"put_oi":3},{"strike":45600.0,"call_gex_1pct":2381723.776765984,"put_gex_1pct":-35979.950697882785,"net_gex_1pct":2345743.8260681015,"gross_gex_1pct":2417703.7274638666,"call_oi":213,"put_oi":1},{"strike":45650.0,"call_gex_1pct":86295.58295698262,"put_gex_1pct":-35681.53146177592,"net_gex_1pct":50614.051495206695,"gross_gex_1pct":121977.11441875855,"call_oi":8,"put_oi":1},{"strike":45700.0,"call_gex_1pct":924992.7410149251,"put_gex_1pct":-70775.65627046498,"net_gex_1pct":854217.0847444601,"gross_gex_1pct":995768.3972853901,"call_oi":89,"put_oi":2},{"strike":45750.0,"call_gex_1pct":170001.00976330828,"put_gex_1pct":0.0,"net_gex_1pct":170001.00976330828,"gross_gex_1pct":170001.00976330828,"call_oi":17,"put_oi":0},{"strike":45800.0,"call_gex_1pct":869910.3474406281,"put_gex_1pct":-69628.2815627773,"net_gex_1pct":800282.0658778509,"gross_gex_1pct":939538.6290034053,"call_oi":89,"put_oi":2},{"strike":45850.0,"call_gex_1pct":207691.93203606838,"put_gex_1pct":-69067.900980082,"net_gex_1pct":138624.03105598636,"gross_gex_1pct":276759.8330161504,"call_oi":22,"put_oi":2},{"strike":45900.0,"call_gex_1pct":227705.95659766588,"put_gex_1pct":-342580.6334716609,"net_gex_1pct":-114874.67687399502,"gross_gex_1pct":570286.5900693268,"call_oi":25,"put_oi":10},{"strike":45950.0,"call_gex_1pct":70216.37478062684,"put_gex_1pct":-169931.91828024,"net_gex_1pct":-99715.54349961317,"gross_gex_1pct":240148.29306086682,"call_oi":8,"put_oi":5},{"strike":46000.0,"call_gex_1pct":23780004.397364017,"put_gex_1pct":-168594.09250866598,"net_gex_1pct":23611410.30485535,"gross_gex_1pct":23948598.489872683,"call_oi":2796,"put_oi":5},{"strike":46050.0,"call_gex_1pct":230579.50965178877,"put_gex_1pct":-200731.66590767587,"net_gex_1pct":29847.843744112906,"gross_gex_1pct":431311.1755594646,"call_oi":28,"put_oi":6},{"strike":46100.0,"call_gex_1pct":260936.68849021045,"put_gex_1pct":-165978.3672912606,"net_gex_1pct":94958.32119894985,"gross_gex_1pct":426915.0557814711,"call_oi":33,"put_oi":5},{"strike":46150.0,"call_gex_1pct":38199.44790616223,"put_gex_1pct":-263519.3661701043,"net_gex_1pct":-225319.91826394206,"gross_gex_1pct":301718.81407626654,"call_oi":5,"put_oi":8},{"strike":46200.0,"call_gex_1pct":324453.9223200207,"put_gex_1pct":-326879.368463499,"net_gex_1pct":-2425.4461434783298,"gross_gex_1pct":651333.2907835196,"call_oi":44,"put_oi":10},{"strike":46250.0,"call_gex_1pct":220383.1776779623,"put_gex_1pct":-356836.05389313586,"net_gex_1pct":-136452.87621517357,"gross_gex_1pct":577219.2315710981,"call_oi":31,"put_oi":11},{"strike":46300.0,"call_gex_1pct":794402.6624457397,"put_gex_1pct":-193169.73506236405,"net_gex_1pct":601232.9273833757,"gross_gex_1pct":987572.3975081037,"call_oi":115,"put_oi":6},{"strike":46350.0,"call_gex_1pct":245881.85430683638,"put_gex_1pct":-255630.4366142103,"net_gex_1pct":-9748.58230737393,"gross_gex_1pct":501512.2909210467,"call_oi":37,"put_oi":8},{"strike":46400.0,"call_gex_1pct":186977.69459235945,"put_gex_1pct":-158580.56771114102,"net_gex_1pct":28397.126881218428,"gross_gex_1pct":345558.26230350044,"call_oi":29,"put_oi":5},{"strike":46450.0,"call_gex_1pct":284589.80534968706,"put_gex_1pct":-314818.1084092671,"net_gex_1pct":-30228.303059580037,"gross_gex_1pct":599407.9137589541,"call_oi":46,"put_oi":10},{"strike":46500.0,"call_gex_1pct":7040001.997101865,"put_gex_1pct":-186550.50948499225,"net_gex_1pct":6853451.487616872,"gross_gex_1pct":7226552.506586857,"call_oi":1175,"put_oi":6},{"strike":46550.0,"call_gex_1pct":208714.66908568484,"put_gex_1pct":0.0,"net_gex_1pct":208714.66908568484,"gross_gex_1pct":208714.66908568484,"call_oi":36,"put_oi":0},{"strike":46600.0,"call_gex_1pct":210452.21663048555,"put_gex_1pct":-30638.727628807275,"net_gex_1pct":179813.48900167827,"gross_gex_1pct":241090.94425929282,"call_oi":38,"put_oi":1},{"strike":46650.0,"call_gex_1pct":219187.9286685221,"put_gex_1pct":-30416.957613387178,"net_gex_1pct":188770.97105513493,"gross_gex_1pct":249604.88628190928,"call_oi":41,"put_oi":1},{"strike":46700.0,"call_gex_1pct":159798.6271425881,"put_gex_1pct":0.0,"net_gex_1pct":159798.6271425881,"gross_gex_1pct":159798.6271425881,"call_oi":31,"put_oi":0},{"strike":46750.0,"call_gex_1pct":45299.57120453566,"put_gex_1pct":0.0,"net_gex_1pct":45299.57120453566,"gross_gex_1pct":45299.57120453566,"call_oi":9,"put_oi":0},{"strike":46800.0,"call_gex_1pct":184081.17750593595,"put_gex_1pct":-297698.5913272161,"net_gex_1pct":-113617.41382128018,"gross_gex_1pct":481779.7688331521,"call_oi":38,"put_oi":10},{"strike":46850.0,"call_gex_1pct":33079.45751659488,"put_gex_1pct":0.0,"net_gex_1pct":33079.45751659488,"gross_gex_1pct":33079.45751659488,"call_oi":7,"put_oi":0},{"strike":46900.0,"call_gex_1pct":41475.92394925281,"put_gex_1pct":0.0,"net_gex_1pct":41475.92394925281,"gross_gex_1pct":41475.92394925281,"call_oi":9,"put_oi":0},{"strike":46950.0,"call_gex_1pct":39801.224916131556,"put_gex_1pct":0.0,"net_gex_1pct":39801.224916131556,"gross_gex_1pct":39801.224916131556,"call_oi":9,"put_oi":0},{"strike":47000.0,"call_gex_1pct":1085524.2055315927,"put_gex_1pct":-144736.76140689207,"net_gex_1pct":940787.4441247006,"gross_gex_1pct":1230260.9669384847,"call_oi":252,"put_oi":5},{"strike":47050.0,"call_gex_1pct":20970.69446262235,"put_gex_1pct":0.0,"net_gex_1pct":20970.69446262235,"gross_gex_1pct":20970.69446262235,"call_oi":5,"put_oi":0},{"strike":47100.0,"call_gex_1pct":92232.38896905977,"put_gex_1pct":0.0,"net_gex_1pct":92232.38896905977,"gross_gex_1pct":92232.38896905977,"call_oi":23,"put_oi":0},{"strike":47150.0,"call_gex_1pct":46783.669626927855,"put_gex_1pct":0.0,"net_gex_1pct":46783.669626927855,"gross_gex_1pct":46783.669626927855,"call_oi":12,"put_oi":0},{"strike":47200.0,"call_gex_1pct":87128.97031453442,"put_gex_1pct":-84503.07067408563,"net_gex_1pct":2625.899640448799,"gross_gex_1pct":171632.04098862005,"call_oi":23,"put_oi":3},{"strike":47250.0,"call_gex_1pct":14715.121140105077,"put_gex_1pct":-83937.27086769788,"net_gex_1pct":-69222.1497275928,"gross_gex_1pct":98652.39200780296,"call_oi":4,"put_oi":3},{"strike":47300.0,"call_gex_1pct":10710.829880518828,"put_gex_1pct":0.0,"net_gex_1pct":10710.829880518828,"gross_gex_1pct":10710.829880518828,"call_oi":3,"put_oi":0},{"strike":47350.0,"call_gex_1pct":34626.49276655296,"put_gex_1pct":0.0,"net_gex_1pct":34626.49276655296,"gross_gex_1pct":34626.49276655296,"call_oi":10,"put_oi":0},{"strike":47400.0,"call_gex_1pct":110742.76522866655,"put_gex_1pct":0.0,"net_gex_1pct":110742.76522866655,"gross_gex_1pct":110742.76522866655,"call_oi":33,"put_oi":0},{"strike":47450.0,"call_gex_1pct":42247.332082009176,"put_gex_1pct":-81745.6693611197,"net_gex_1pct":-39498.33727911052,"gross_gex_1pct":123993.00144312887,"call_oi":13,"put_oi":3},{"strike":47500.0,"call_gex_1pct":1817491.9853322464,"put_gex_1pct":-108286.68299597486,"net_gex_1pct":1709205.3023362716,"gross_gex_1pct":1925778.6683282212,"call_oi":578,"put_oi":4},{"strike":47550.0,"call_gex_1pct":9119.234622107366,"put_gex_1pct":0.0,"net_gex_1pct":9119.234622107366,"gross_gex_1pct":9119.234622107366,"call_oi":3,"put_oi":0},{"strike":47600.0,"call_gex_1pct":35227.393883402685,"put_gex_1pct":0.0,"net_gex_1pct":35227.393883402685,"gross_gex_1pct":35227.393883402685,"call_oi":12,"put_oi":0},{"strike":47650.0,"call_gex_1pct":8724.965837182113,"put_gex_1pct":0.0,"net_gex_1pct":8724.965837182113,"gross_gex_1pct":8724.965837182113,"call_oi":3,"put_oi":0},{"strike":47700.0,"call_gex_1pct":25252.2673843324,"put_gex_1pct":0.0,"net_gex_1pct":25252.2673843324,"gross_gex_1pct":25252.2673843324,"call_oi":9,"put_oi":0},{"strike":47750.0,"call_gex_1pct":10814.863889657843,"put_gex_1pct":0.0,"net_gex_1pct":10814.863889657843,"gross_gex_1pct":10814.863889657843,"call_oi":4,"put_oi":0},{"strike":47800.0,"call_gex_1pct":18213.824078517155,"put_gex_1pct":0.0,"net_gex_1pct":18213.824078517155,"gross_gex_1pct":18213.824078517155,"call_oi":7,"put_oi":0},{"strike":47850.0,"call_gex_1pct":7734.960514397081,"put_gex_1pct":0.0,"net_gex_1pct":7734.960514397081,"gross_gex_1pct":7734.960514397081,"call_oi":3,"put_oi":0},{"strike":47900.0,"call_gex_1pct":17885.231640099613,"put_gex_1pct":0.0,"net_gex_1pct":17885.231640099613,"gross_gex_1pct":17885.231640099613,"call_oi":7,"put_oi":0},{"strike":47950.0,"call_gex_1pct":2455.623874715267,"put_gex_1pct":0.0,"net_gex_1pct":2455.623874715267,"gross_gex_1pct":2455.623874715267,"call_oi":1,"put_oi":0},{"strike":48000.0,"call_gex_1pct":2367989.354825138,"put_gex_1pct":-25418.32852627598,"net_gex_1pct":2342571.026298862,"gross_gex_1pct":2393407.6833514143,"call_oi":973,"put_oi":1},{"strike":48050.0,"call_gex_1pct":4824.2189448244535,"put_gex_1pct":0.0,"net_gex_1pct":4824.2189448244535,"gross_gex_1pct":4824.2189448244535,"call_oi":2,"put_oi":0},{"strike":48100.0,"call_gex_1pct":275464.5396718279,"put_gex_1pct":0.0,"net_gex_1pct":275464.5396718279,"gross_gex_1pct":275464.5396718279,"call_oi":119,"put_oi":0},{"strike":48150.0,"call_gex_1pct":6883.569156372284,"put_gex_1pct":0.0,"net_gex_1pct":6883.569156372284,"gross_gex_1pct":6883.569156372284,"call_oi":3,"put_oi":0},{"strike":48200.0,"call_gex_1pct":4549.0459144440365,"put_gex_1pct":0.0,"net_gex_1pct":4549.0459144440365,"gross_gex_1pct":4549.0459144440365,"call_oi":2,"put_oi":0},{"strike":48250.0,"call_gex_1pct":4509.64286177122,"put_gex_1pct":0.0,"net_gex_1pct":4509.64286177122,"gross_gex_1pct":4509.64286177122,"call_oi":2,"put_oi":0},{"strike":48300.0,"call_gex_1pct":12210503.43249255,"put_gex_1pct":-24517.56924815423,"net_gex_1pct":12185985.863244396,"gross_gex_1pct":12235021.001740705,"call_oi":5652,"put_oi":1},{"strike":48350.0,"call_gex_1pct":44979.423557405535,"put_gex_1pct":0.0,"net_gex_1pct":44979.423557405535,"gross_gex_1pct":44979.423557405535,"call_oi":21,"put_oi":0},{"strike":48400.0,"call_gex_1pct":36101.88144010376,"put_gex_1pct":0.0,"net_gex_1pct":36101.88144010376,"gross_gex_1pct":36101.88144010376,"call_oi":17,"put_oi":0},{"strike":48500.0,"call_gex_1pct":328249.1789194447,"put_gex_1pct":-23950.923277804755,"net_gex_1pct":304298.25564163993,"gross_gex_1pct":352200.1021972494,"call_oi":163,"put_oi":1},{"strike":48600.0,"call_gex_1pct":17822.868810894837,"put_gex_1pct":-23677.097629126813,"net_gex_1pct":-5854.228818231975,"gross_gex_1pct":41499.96644002165,"call_oi":9,"put_oi":1},{"strike":48700.0,"call_gex_1pct":37487.32588238878,"put_gex_1pct":0.0,"net_gex_1pct":37487.32588238878,"gross_gex_1pct":37487.32588238878,"call_oi":20,"put_oi":0},{"strike":48800.0,"call_gex_1pct":23970.582456183587,"put_gex_1pct":0.0,"net_gex_1pct":23970.582456183587,"gross_gex_1pct":23970.582456183587,"call_oi":13,"put_oi":0},{"strike":48900.0,"call_gex_1pct":7257.047845334892,"put_gex_1pct":0.0,"net_gex_1pct":7257.047845334892,"gross_gex_1pct":7257.047845334892,"call_oi":4,"put_oi":0},{"strike":49000.0,"call_gex_1pct":87400.91192928668,"put_gex_1pct":0.0,"net_gex_1pct":87400.91192928668,"gross_gex_1pct":87400.91192928668,"call_oi":51,"put_oi":0},{"strike":49100.0,"call_gex_1pct":16867.916783120047,"put_gex_1pct":0.0,"net_gex_1pct":16867.916783120047,"gross_gex_1pct":16867.916783120047,"call_oi":10,"put_oi":0},{"strike":49200.0,"call_gex_1pct":11623.957654014595,"put_gex_1pct":0.0,"net_gex_1pct":11623.957654014595,"gross_gex_1pct":11623.957654014595,"call_oi":7,"put_oi":0},{"strike":49300.0,"call_gex_1pct":3129.66711143022,"put_gex_1pct":0.0,"net_gex_1pct":3129.66711143022,"gross_gex_1pct":3129.66711143022,"call_oi":2,"put_oi":0},{"strike":49400.0,"call_gex_1pct":6164.01517594052,"put_gex_1pct":0.0,"net_gex_1pct":6164.01517594052,"gross_gex_1pct":6164.01517594052,"call_oi":4,"put_oi":0},{"strike":49500.0,"call_gex_1pct":727024.3994582937,"put_gex_1pct":0.0,"net_gex_1pct":727024.3994582937,"gross_gex_1pct":727024.3994582937,"call_oi":479,"put_oi":0},{"strike":49600.0,"call_gex_1pct":4066.494035261699,"put_gex_1pct":0.0,"net_gex_1pct":4066.494035261699,"gross_gex_1pct":4066.494035261699,"call_oi":3,"put_oi":0},{"strike":49700.0,"call_gex_1pct":2527.352672716645,"put_gex_1pct":0.0,"net_gex_1pct":2527.352672716645,"gross_gex_1pct":2527.352672716645,"call_oi":2,"put_oi":0},{"strike":49800.0,"call_gex_1pct":5861.057058907557,"put_gex_1pct":0.0,"net_gex_1pct":5861.057058907557,"gross_gex_1pct":5861.057058907557,"call_oi":5,"put_oi":0},{"strike":49900.0,"call_gex_1pct":3242.6161404763525,"put_gex_1pct":0.0,"net_gex_1pct":3242.6161404763525,"gross_gex_1pct":3242.6161404763525,"call_oi":3,"put_oi":0},{"strike":50000.0,"call_gex_1pct":901333.1401627203,"put_gex_1pct":0.0,"net_gex_1pct":901333.1401627203,"gross_gex_1pct":901333.1401627203,"call_oi":911,"put_oi":0},{"strike":50100.0,"call_gex_1pct":2692.3153101558005,"put_gex_1pct":0.0,"net_gex_1pct":2692.3153101558005,"gross_gex_1pct":2692.3153101558005,"call_oi":3,"put_oi":0},{"strike":50200.0,"call_gex_1pct":7077.625260808796,"put_gex_1pct":0.0,"net_gex_1pct":7077.625260808796,"gross_gex_1pct":7077.625260808796,"call_oi":8,"put_oi":0},{"strike":50300.0,"call_gex_1pct":41250.9074799227,"put_gex_1pct":0.0,"net_gex_1pct":41250.9074799227,"gross_gex_1pct":41250.9074799227,"call_oi":52,"put_oi":0},{"strike":50400.0,"call_gex_1pct":700.4836802067804,"put_gex_1pct":0.0,"net_gex_1pct":700.4836802067804,"gross_gex_1pct":700.4836802067804,"call_oi":1,"put_oi":0},{"strike":50500.0,"call_gex_1pct":35229.96328046408,"put_gex_1pct":0.0,"net_gex_1pct":35229.96328046408,"gross_gex_1pct":35229.96328046408,"call_oi":51,"put_oi":0},{"strike":50700.0,"call_gex_1pct":1767.417479264892,"put_gex_1pct":0.0,"net_gex_1pct":1767.417479264892,"gross_gex_1pct":1767.417479264892,"call_oi":3,"put_oi":0},{"strike":50800.0,"call_gex_1pct":2469.754102015166,"put_gex_1pct":0.0,"net_gex_1pct":2469.754102015166,"gross_gex_1pct":2469.754102015166,"call_oi":5,"put_oi":0},{"strike":50900.0,"call_gex_1pct":487.3241142258464,"put_gex_1pct":0.0,"net_gex_1pct":487.3241142258464,"gross_gex_1pct":487.3241142258464,"call_oi":1,"put_oi":0},{"strike":51000.0,"call_gex_1pct":473156.3584953,"put_gex_1pct":-18562.00462826893,"net_gex_1pct":454594.35386703105,"gross_gex_1pct":491718.36312356894,"call_oi":984,"put_oi":1},{"strike":51100.0,"call_gex_1pct":2686.910040655104,"put_gex_1pct":0.0,"net_gex_1pct":2686.910040655104,"gross_gex_1pct":2686.910040655104,"call_oi":7,"put_oi":0},{"strike":51200.0,"call_gex_1pct":757.6309915922507,"put_gex_1pct":0.0,"net_gex_1pct":757.6309915922507,"gross_gex_1pct":757.6309915922507,"call_oi":2,"put_oi":0},{"strike":51300.0,"call_gex_1pct":373.89977902652566,"put_gex_1pct":0.0,"net_gex_1pct":373.89977902652566,"gross_gex_1pct":373.89977902652566,"call_oi":1,"put_oi":0},{"strike":51500.0,"call_gex_1pct":269.09951636716227,"put_gex_1pct":0.0,"net_gex_1pct":269.09951636716227,"gross_gex_1pct":269.09951636716227,"call_oi":1,"put_oi":0},{"strike":51700.0,"call_gex_1pct":2361.029374902771,"put_gex_1pct":0.0,"net_gex_1pct":2361.029374902771,"gross_gex_1pct":2361.029374902771,"call_oi":9,"put_oi":0},{"strike":51800.0,"call_gex_1pct":7771.942474912459,"put_gex_1pct":0.0,"net_gex_1pct":7771.942474912459,"gross_gex_1pct":7771.942474912459,"call_oi":30,"put_oi":0}]}
```

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 40,300 | TAIFEX Proxy |
| 對應到期月份 | 202611F1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-11-05→2026-11-06) | -1,650 | TAIFEX Proxy snapshots (2026-11-05) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 292,511 | 291,120 | +1,391 | 21,744 | 21,641 | +103 | +1,288 | TAIFEX Proxy |
| 投信 | 224 | 15,330 | -15,106 | 0 | 0 | +0 | -15,106 | TAIFEX Proxy |
| 自營商 | 219,496 | 231,003 | -11,507 | 25,684 | 22,947 | +2,737 | -14,244 | TAIFEX Proxy |
| 三大法人合計 | 512,231 | 537,453 | -25,222 | 47,428 | 44,588 | +2,840 | -28,062 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 32.09 | 31.02 | +1.06 | 20.78 | 20.89 | -0.11 | +1.18 | TAIFEX Proxy |
| 投信 | 0.14 | 11.00 | -10.86 | 0.00 | 0.00 | +0 | -10.86 | TAIFEX Proxy |
| 自營商 | 45.40 | 37.81 | +7.59 | 7.22 | 6.76 | +0.46 | +7.13 | TAIFEX Proxy |
| 三大法人合計 | 77.63 | 79.84 | -2.21 | 28.00 | 27.66 | +0.35 | -2.56 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 14,097 | TAIFEX Proxy |
| 買權空方 OI | 19,390 | TAIFEX Proxy |
| 買權多空淨 OI | -5,293 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-11-04→2026-11-06) | -1,167 | TAIFEX Proxy snapshots (2026-11-05) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 10,486 | TAIFEX Proxy |
| 賣權空方 OI | 13,491 | TAIFEX Proxy |
| 賣權多空淨 OI | -3,005 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-11-04→2026-11-06) | -286 | TAIFEX Proxy snapshots (2026-11-05) |
- 資料日期：買權 2026-11-06／賣權 2026-11-06 (TypeOfTraders=0 全部交易人；契約月份 202611)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -4,372 | 2026-11-04→2026-11-06 | TAIFEX Proxy snapshots (2026-11-05) |
| 買權前十大 | -1,167 | 2026-11-04→2026-11-06 | TAIFEX Proxy snapshots (2026-11-05) |
| 賣權前十大 | -286 | 2026-11-04→2026-11-06 | TAIFEX Proxy snapshots (2026-11-05) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-11-06；報告產製時間：2026-11-08 10:38:08；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 部分取得欄位 (0)：無
- 註記：同 T0 穩定：33 格新舊皆有值，沿用前版（不再靜默覆寫）
- 未取得欄位 (4)：futures.futures.night.settle, futures.futures.night.oi, futures.gamma_flip, options.chain_oi_change

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_breadth：`twse-proxy`
- listed_turnover：`twse-proxy market_statistics`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑；合計需雙市場欄位完整)`
- margin_ratio：`TWSE 上市自建估算（當日暫估；資料日期：2026-11-06；估值 1240 檔；3 檔採最近有效收盤價（價格日期 20260402 至 20261106）；Blave 同 T0 交叉驗證 151.9300%；差異 0.209 個百分點；門檻 <1.00 個百分點；PASS）`
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
- 註記：上市市場維持率為當日暫估，以 TWSE 自建計算為主；3 檔採最近有效收盤價（價格日期 20260402 至 20261106）。Blave 同 T0 交叉驗證 151.9300%；差異 0.209 個百分點；門檻 <1.00 個百分點；PASS。Blave 不可用不影響 DATA_REPORT 產出。
- 註記：上市 MI_MARGN 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | -911.9 | -99,930 | -4,310 | -1,113 | +1,391 | +103 | 避險／對沖 | 趨勢偏空 | twse-proxy／TAIFEX Proxy |
| 投信 | +266.9 | +90,437 | +154 | +0 | -15,106 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | -494.8 | +1,680 | -875 | -406 | -11,507 | +2,737 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
