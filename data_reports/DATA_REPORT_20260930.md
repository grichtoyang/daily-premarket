# DATA_REPORT_20260930

- 報告日期：`2026-10-01`
- T0 交易日期：`2026-09-30`
- 資料產出時間：`2026-10-01 08:08:42`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 47,940.13 | 點 | twse-proxy |
| 開盤 | 47,767.49 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 48,379.71 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 47,767.49 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 47,940.13 | 點 | twse-proxy |
| 漲跌點數 | 308.17 | 點 | twse-proxy |
| 漲跌幅 | +0.65 | % | twse-proxy |
| 成交金額 | 9,214.9 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 828 | twse-proxy |
| 下跌家數 | 187 | twse-proxy |
| 平盤家數 | 65 | twse-proxy |
| 漲停家數 | 32 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 515 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 269 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 93 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 26 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 1 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +308.6 | 億元 | twse-proxy /institutional |
| 投信 | +82.9 | 億元 | twse-proxy /institutional |
| 自營商 | +12.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +403.9 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | 8,381.3 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資增減 | +58.0 | 億元 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券餘額 | 279,242 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融券增減 | 20,675 | 張 | HiStock 上市+上櫃融資融券 (金額口徑) |
| 融資維持率 | 193.87 | % | 前值遞補 (DATA 2026-09-29；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 4,504,816 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | 43,946 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | 3,378 | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 9,214.9 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 2,323.6 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 11,538.5 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,651.54 | -19.30 | -0.25 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,861.06 | 63.53 | +0.24 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,408.50 | 69.17 | +0.23 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 50,906.05 | -443.87 | -0.86 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,628.62 | -0.54 | -0.00 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.34 | 0.30 | +1.87 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 65,481.27 | -396.35 | -0.60 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,870.81 | -18.93 | -0.27 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,523.57 | -118.94 | -0.48 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,830.45 | 6.83 | +0.18 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,901.95 | 43.20 | +0.34 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,744.00 | 12.00 | +0.16 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,820.25 | 207.00 | +0.68 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,425.00 | -277.00 | -0.54 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,826.10 | -3.10 | -0.11 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.88 | -0.01 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.29 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.64 | 0.04 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.87 | 0.02 | +0.05 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.50 | 0.13 | +0.13 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.66 | 0.26 | +0.16 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,358.18 | 7.68 | +0.57 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 456.94 | 4.06 | +0.90 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 24.72 | 0.87 | +3.65 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 45.31 | 1.52 | +3.47 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 89.98 | 0.60 | +0.67 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,186.40 | 6.70 | +0.16 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,457.33 | -165.10 | -0.20 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：面板雙虎漲停攜PCB衝鋒 台股尾盤卻急殺摔下48K
  - 來源：Yahoo 台股；發布時間：2026-09-30T09:13:18Z；台北時間：2026-09-30 17:13
  - 摘要：玻璃基板概念股點火，台股反彈308點、4萬8得而復失！今(30)日加權指數盤中最高衝上48,379.71點，尾盤漲幅收斂，終場上漲308.17點或0.65%，收47,940.13點，成交金額8,774.69億元。櫃買指數上漲1.17%，表現
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E5%9B%9E%E8%A3%9C296%E5%84%84%E5%8F%B0%E8%82%A1%E5%B0%BE%E7%9B%A4%E4%BB%8D%E7%95%99%E4%B8%8D%E4%BD%8F48k-%E9%9D%A2%E6%9D%BF%E9%9B%99%E8%99%8E%E7%88%86%E9%87%8F%E6%BC%B2%E5%81%9C%E6%94%9Cpcb%E5%A4%A7%E8%BB%8D%E9%96%8B%E7%B4%85%E7%9B%A4%E6%B4%BE%E5%B0%8D%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-091318114.html
- 事件2：公股投信整併卡在離職金 華南永昌若不點頭恐遭剔除
  - 來源：Yahoo 台股；發布時間：2026-09-30T10:16:08Z；台北時間：2026-09-30 18:16
  - 摘要：知情人士透露，華南金控旗下的華南永昌投信工會拒簽其他三家工會都已同意的員工安置方案，尤其是退職金的計算高出其他投信工會的共識太多，因此為了避免公股投信最小的一家妨礙四合一的進度，財政部為首的公股陣營已有腹案，若華南永昌投信工會仍不願接受其他
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%8D%A8-%E8%8F%AF%E5%8D%97%E6%B0%B8%E6%98%8C%E6%8A%95%E4%BF%A1%E5%A4%A9%E5%83%B9%E9%9B%A2%E8%81%B7%E9%87%91%E7%89%88%E6%9C%AC%E6%9B%9D%E5%85%89-%E5%85%AC%E8%82%A1%E6%8A%95%E4%BF%A1%E6%95%B4%E4%BD%B5%E4%B8%8D%E6%8E%92%E9%99%A4%E8%AE%8A%E4%B8%89%E5%90%88-101608017.html
- 事件3：轉手預售屋賺530萬 男子漏報稅讓245萬追上門
  - 來源：Yahoo 台股；發布時間：2026-09-30T10:10:11Z；台北時間：2026-09-30 18:10
  - 摘要：一名男子購買預售屋後，尚未付清房款就將購屋權利轉讓他人，收回已付房款並賺進530萬元價差，卻未依規定申報，遭財政部中區國稅局查獲，補稅重罰245萬元。國稅局提醒，轉讓預售屋權利也要報稅，應在簽訂轉讓契約的次日起算30日內完成申報。
  - 原文連結：https://tw.stock.yahoo.com/news/%E8%BD%89%E8%AE%93%E9%A0%90%E5%94%AE%E5%B1%8B%E8%B3%BA%E5%83%B9%E5%B7%AE%EF%BC%9F%E7%94%B7%E5%AD%90%E6%BC%8F%E5%A0%B1%E7%A8%85%E9%81%AD%E5%9C%8B%E7%A8%85%E5%B1%80%E7%9B%AF%E4%B8%8A-%E8%A3%9C%E7%A8%85%E9%87%8D%E7%BD%B0245%E8%90%AC%E5%85%83-101011373.html
- 事件4：羽田5台退稅機搶先亮相 達人曝8大機場能退現
  - 來源：Yahoo 台股；發布時間：2026-09-30T09:46:02Z；台北時間：2026-09-30 17:46
  - 摘要：旅日達人林氏璧在臉書粉專「日本自助旅遊中毒者」發文表示，近期收到網友提供的資訊，羽田機場第二航廈出境審查後的管制區內，已經有5台自助退稅機安裝完成。此外，林氏璧也分享多慶屋提供的資訊，透露免稅系統公司J&amp;J Tax Free回覆，目
  - 原文連結：https://tw.stock.yahoo.com/news/%E6%97%A5%E6%9C%AC%E9%80%80%E7%A8%85%E6%96%B0%E5%88%B6%E5%B0%87%E4%B8%8A%E8%B7%AF-%E7%BE%BD%E7%94%B0%E6%A9%9F%E5%A0%B4%E5%87%BA%E7%8F%BE-5%E5%8F%B0%E6%A9%9F%E5%99%A8-%E6%97%85%E6%97%A5%E9%81%94%E4%BA%BA%E6%9B%9D-8%E5%A4%A7%E6%A9%9F%E5%A0%B4%E5%8F%AF%E9%80%80%E7%8F%BE%E9%87%91-094602744.html
- 事件5：買房人潮回籠了？新北台中交易量年增逾2成
  - 來源：Yahoo 台股；發布時間：2026-09-30T09:31:00Z；台北時間：2026-09-30 17:31
  - 摘要：AI、高效能運算及新興科技需求持續熱絡，8月出口創歷年單月新高，而央行也將2026年全年經濟成長率預測上修至11.48%。國內經濟、就業與薪資表現穩健，加上台股維持相對高檔，均對民眾購屋信心形成支撐。不過，由於適逢中秋節與教師節4天連假影響
  - 原文連結：https://tw.stock.yahoo.com/news/9%E6%9C%88%E6%88%BF%E5%B8%82%E5%9B%9E%E6%9A%96-%E5%85%A8%E5%8F%B0%E4%BA%A4%E6%98%93%E9%87%8F-%E6%9C%88%E5%A2%9E5-%E5%B9%B4%E5%A2%9E17-%E9%80%992%E9%83%BD%E8%B2%B7%E6%B0%A3%E7%8B%82%E5%A2%9E%E9%80%BE2%E6%88%90-093100523.html
- 事件6：砸逾40億元攻光通訊！「觸控模組大廠」連漲9天狂飆49.35%奪強勢股王　訂單到手、Q4拚出貨
  - 來源：Yahoo 台股；發布時間：2026-10-01T00:00:00Z；台北時間：2026-10-01 08:00
  - 摘要：[FTNN新聞網]記者黃詩雯／綜合報導台股30日加權指數終場收在47940.13點，上漲308.17點，漲幅0.65%，成交量達8756億元，觀察昨日強勢個股表現，觸控模組大廠GI...
  - 原文連結：https://tw.stock.yahoo.com/news/%E7%A0%B8%E9%80%BE40%E5%84%84%E5%85%83%E6%94%BB%E5%85%89%E9%80%9A%E8%A8%8A-%E8%A7%B8%E6%8E%A7%E6%A8%A1%E7%B5%84%E5%A4%A7%E5%BB%A0-%E9%80%A3%E6%BC%B29%E5%A4%A9%E7%8B%82%E9%A3%8649-35-%E5%A5%AA%E5%BC%B7%E5%8B%A2%E8%82%A1%E7%8E%8B-000000099.html
- 事件7：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress test-related capital requirements
  - 來源：Federal Reserve；發布時間：Wed, 30 Sep 2026 13:00:00 GMT；台北時間：2026-09-30 21:00
  - 摘要：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress t
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm
- 事件8：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 來源：Federal Reserve；發布時間：Fri, 25 Sep 2026 20:30:00 GMT；台北時間：2026-09-26 04:30
  - 摘要：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260925a.htm
- 事件9：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin issuers under the GENIUS Act
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 18:30:00 GMT；台北時間：2026-09-25 02:30
  - 摘要：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin 
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260924a.htm
- 事件10：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 15:00:00 GMT；台北時間：2026-09-24 23:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260924a.htm
- 事件11：Fed's Kashkari says inflation is 'still too high' even after softer-than-expected PCE data, labor market is 'pretty good'
  - 來源：CNBC；發布時間：Wed, 30 Sep 2026 23:44:28 GMT；台北時間：2026-10-01 07:44
  - 摘要：Kashkari sat down with CNBC's Steve Liesman for an exclusive conversation Wednesday night.
  - 原文連結：https://www.cnbc.com/2026/09/30/watch-minneapolis-fed-president-neel-kashkari.html
- 事件12：Treasury launches student loan support center as new data show 9.3 million borrowers in default
  - 來源：CNBC；發布時間：Wed, 30 Sep 2026 22:15:29 GMT；台北時間：2026-10-01 06:15
  - 摘要：The Trump administration announced on Wednesday that it was launching a "Default Loans Support Center" for student loan borrowers who've fallen behind
  - 原文連結：https://www.cnbc.com/2026/09/30/student-loan-default-support-center.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-09-30

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,467 | TAIFEX Proxy |
| 最高價 | 48,646 | TAIFEX Proxy |
| 最低價 | 48,230 | TAIFEX Proxy |
| 收盤價 | 48,330 | TAIFEX Proxy |
| 漲跌點數 | +549 | TAIFEX Proxy |
| 漲跌幅 | +1.15 | TAIFEX Proxy |
| 成交量 | 72,363 | TAIFEX Proxy |
| 日盤高點及低點 | 48,646 / 48,230 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,320 | TAIFEX Proxy |
| 最高價 | 48,592 | TAIFEX Proxy |
| 最低價 | 48,158 | TAIFEX Proxy |
| 收盤價 | 48,298 | TAIFEX Proxy |
| 漲跌點數 | -32 | TAIFEX Proxy |
| 漲跌幅 | -0.07 | TAIFEX Proxy |
| 成交量 | 29,632 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,592 / 48,158 | TAIFEX Proxy |
| 結算價 | 48,330 | TAIFEX Proxy |
| 未平倉量 | 105,359 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 12,351 | TAIFEX Proxy |
| 外資空方 OI | 90,502 | TAIFEX Proxy |
| 外資多空淨 OI | -78,151 | TAIFEX Proxy |
| 投信多方 OI | 76,739 | TAIFEX Proxy |
| 投信空方 OI | 2,900 | TAIFEX Proxy |
| 投信多空淨 OI | +73,839 | TAIFEX Proxy |
| 自營商多方 OI | 3,182 | TAIFEX Proxy |
| 自營商空方 OI | 4,252 | TAIFEX Proxy |
| 自營商多空淨 OI | -1,070 | TAIFEX Proxy |
| 三大法人合計多方 OI | 92,272 | TAIFEX Proxy |
| 三大法人合計空方 OI | 97,654 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -5,382 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +878 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +1,027 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -582 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,962 | TAIFEX Proxy |
| 前十大交易人空方 OI | 74,433 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,529 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-24→2026-09-30) | -865 | TAIFEX Proxy snapshots (2026-09-29) |
- 資料日期：2026-09-30 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 42,583 | TAIFEX Proxy |
| 外資日盤空單交易量 | 41,737 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +846 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 16,127 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,915 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -788 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +1,634 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,027 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,027 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -536 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | +463 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -999 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,337 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | -325 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +129.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | -31.5 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,330 | TAIFEX Proxy |
| 加權指數價格 | 47,940.13 | twse-proxy |
| 台指期與加權指數價差 | +389.87 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.81 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +389.87 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -32 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,330 | 48,298 | +32 | TAIFEX Proxy |
| 成交量 | 42,731 | 29,632 | +13,099 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,323（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 42,583 | 41,737 | +846 | 16,127 | 16,915 | -788 | +1,634 | 12,351 | 90,502 | -78,151 | +878 | TAIFEX Proxy |
| 投信 | 1,036 | 9 | +1,027 | 0 | 0 | +0 | +1,027 | 76,739 | 2,900 | +73,839 | +1,027 | TAIFEX Proxy |
| 自營商 | 3,841 | 4,377 | -536 | 944 | 481 | +463 | -999 | 3,182 | 4,252 | -1,070 | -582 | TAIFEX Proxy |
| 三大法人合計 | 47,460 | 46,123 | +1,337 | 17,071 | 17,396 | -325 | +1,662 | 92,272 | 97,654 | -5,382 | +1,323 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,962 | TAIFEX Proxy |
| 前十大交易人空方 OI | 74,433 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +6,529 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-24→2026-09-30) | -865 | TAIFEX Proxy snapshots (2026-09-29) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 40.95% | TAIFEX Proxy |
| 夜盤漲跌點數 | -32 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | -788 | TAIFEX Proxy |
| 劇本分類 | 劇本三 | 規則對應 |
| 劇本條件 | 夜盤下跌＋外資偏空 | 規則對應 |
| 劇本特徵 | 開低、續跌機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-30 | TAIFEX Proxy |
| 到期月份／到期日 | 202609W5 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-01 08:08:42 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 312,612 | TAIFEX Proxy |
| Call 總未平倉量 OI | 56,544 | TAIFEX Proxy |
| Call OI 增減 | unavailable | 端點未提供 |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 308,375 | TAIFEX Proxy |
| Put 總未平倉量 OI | 54,216 | TAIFEX Proxy |
| Put OI 增減 | unavailable | 端點未提供 |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 1.01 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.04 | TAIFEX Proxy |
| Put／Call Ratio | 0.96 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-09-29→2026-09-30) | 8.81 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-29→2026-09-30) | 5.27 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 102,171 | TAIFEX Proxy |
| 外資 Call日賣 | 106,681 | TAIFEX Proxy |
| 外資 Call日淨 | -4,510 | TAIFEX Proxy |
| 外資 Put日買 | 105,543 | TAIFEX Proxy |
| 外資 Put日賣 | 104,834 | TAIFEX Proxy |
| 外資 Put日淨 | +709 | TAIFEX Proxy |
| 外資 Call夜買 | 23,209 | TAIFEX Proxy |
| 外資 Call夜賣 | 23,415 | TAIFEX Proxy |
| 外資 Call夜淨 | -206 | TAIFEX Proxy |
| 外資 Put夜買 | 22,029 | TAIFEX Proxy |
| 外資 Put夜賣 | 22,179 | TAIFEX Proxy |
| 外資 Put夜淨 | -150 | TAIFEX Proxy |
| 外資 日盤淨總量 | -5,219 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -4,304 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +859 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 81,837 | TAIFEX Proxy |
| 自營商 Call日賣 | 86,441 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,604 | TAIFEX Proxy |
| 自營商 Put日買 | 83,393 | TAIFEX Proxy |
| 自營商 Put日賣 | 90,032 | TAIFEX Proxy |
| 自營商 Put日淨 | -6,639 | TAIFEX Proxy |
| 自營商 Call夜買 | 13,073 | TAIFEX Proxy |
| 自營商 Call夜賣 | 15,525 | TAIFEX Proxy |
| 自營商 Call夜淨 | -2,452 | TAIFEX Proxy |
| 自營商 Put夜買 | 15,708 | TAIFEX Proxy |
| 自營商 Put夜賣 | 13,229 | TAIFEX Proxy |
| 自營商 Put夜淨 | +2,479 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +2,035 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -2,152 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -9,118 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 48,200 | 3,551 | TAIFEX Proxy |
| Call OI 第2大履約價 | 48,250 | 3,527 | TAIFEX Proxy |
| Call OI 第3大履約價 | 48,300 | 3,527 | TAIFEX Proxy |
| Call OI 最大履約價 | 48,200 | 3,551 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202609W5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 48,200 | 3,551 | 6.28% | TAIFEX Proxy |
| C2 | 48,250 | 3,527 | 6.24% | TAIFEX Proxy |
| C3 | 48,300 | 3,527 | 6.24% | TAIFEX Proxy |
| C4 | 48,500 | 2,968 | 5.25% | TAIFEX Proxy |
| C5 | 48,400 | 2,689 | 4.76% | TAIFEX Proxy |
| C6 | 50,500 | 2,581 | 4.56% | TAIFEX Proxy |
| C7 | 49,000 | 2,554 | 4.52% | TAIFEX Proxy |
| C8 | 48,600 | 2,442 | 4.32% | TAIFEX Proxy |
| C9 | 48,800 | 2,424 | 4.29% | TAIFEX Proxy |
| C10 | 48,700 | 2,403 | 4.25% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 48,000 | 4,772 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,100 | 3,409 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,150 | 3,399 | TAIFEX Proxy |
| Put OI 最大履約價 | 48,000 | 4,772 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202609W5)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 48,000 | 4,772 | 8.8% | TAIFEX Proxy |
| P2 | 48,100 | 3,409 | 6.29% | TAIFEX Proxy |
| P3 | 48,150 | 3,399 | 6.27% | TAIFEX Proxy |
| P4 | 48,200 | 3,183 | 5.87% | TAIFEX Proxy |
| P5 | 47,500 | 2,357 | 4.35% | TAIFEX Proxy |
| P6 | 47,900 | 2,163 | 3.99% | TAIFEX Proxy |
| P7 | 47,600 | 2,161 | 3.99% | TAIFEX Proxy |
| P8 | 47,700 | 2,102 | 3.88% | TAIFEX Proxy |
| P9 | 47,800 | 1,921 | 3.54% | TAIFEX Proxy |
| P10 | 48,050 | 1,701 | 3.14% | TAIFEX Proxy |


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
| Call Wall 價位 | 48,200 | TAIFEX Proxy |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 48,000 | TAIFEX Proxy |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | 47,800.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 資料日期 | 2026-09-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 47,906.74 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 資料日期 | 2026-09-30 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,150 | TAIFEX Proxy |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 207,005 | 212,224 | -5,219 | 45,388 | 45,444 | -56 | -5,163 | TAIFEX Proxy |
| 投信 | 371 | 3,104 | -2,733 | 0 | 0 | +0 | -2,733 | TAIFEX Proxy |
| 自營商 | 171,869 | 169,834 | +2,035 | 26,302 | 31,233 | -4,931 | +6,966 | TAIFEX Proxy |
| 三大法人合計 | 379,245 | 385,162 | -5,917 | 71,690 | 76,677 | -4,987 | -930 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 8.92 | 8.79 | +0.12 | 3.60 | 3.65 | -0.05 | +0.17 | TAIFEX Proxy |
| 投信 | 0.11 | 1.96 | -1.85 | 0.00 | 0.00 | +0 | -1.85 | TAIFEX Proxy |
| 自營商 | 8.80 | 7.00 | +1.79 | 1.81 | 2.42 | -0.61 | +2.40 | TAIFEX Proxy |
| 三大法人合計 | 17.82 | 17.76 | +0.07 | 5.42 | 6.07 | -0.66 | +0.72 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,234 | TAIFEX Proxy |
| 買權空方 OI | 11,188 | TAIFEX Proxy |
| 買權多空淨 OI | +1,046 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-24→2026-09-30) | -70 | TAIFEX Proxy snapshots (2026-09-29) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,471 | TAIFEX Proxy |
| 賣權空方 OI | 9,095 | TAIFEX Proxy |
| 賣權多空淨 OI | -624 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-24→2026-09-30) | +258 | TAIFEX Proxy snapshots (2026-09-29) |
- 資料日期：買權 2026-09-30／賣權 2026-09-30 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -865 | 2026-09-24→2026-09-30 | TAIFEX Proxy snapshots (2026-09-29) |
| 買權前十大 | -70 | 2026-09-24→2026-09-30 | TAIFEX Proxy snapshots (2026-09-29) |
| 賣權前十大 | +258 | 2026-09-24→2026-09-30 | TAIFEX Proxy snapshots (2026-09-29) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-30；資料時間：2026-10-01 08:08:42；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (1)：options.chain_oi_change
- 註記：夜盤 OHLC 資料日期 2026-10-01 (T0 2026-09-30)，來源 proxy
- 註記：法人交易量變化無昨日交易端點，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin：`HiStock 上市+上櫃融資融券 (金額口徑)`
- margin_ratio：`前值遞補 (DATA 2026-09-29；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-09-29)，非 T0 2026-09-30
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 註記：借券賣出增減僅上櫃值 (TWSE TWT93U 未取得)
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +308.6 | -78,151 | +846 | -788 | -5,219 | -56 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +82.9 | +73,839 | +1,027 | +0 | -2,733 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +12.4 | -1,070 | -536 | +463 | +2,035 | -4,931 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
