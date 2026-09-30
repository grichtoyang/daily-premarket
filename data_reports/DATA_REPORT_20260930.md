# DATA_REPORT_20260930

- 報告日期：`2026-09-30`
- T0 交易日期：`2026-09-30`
- 資料產出時間：`2026-09-30 19:14:48`
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
| 外資 | +296.4 | 億元 | twse-proxy /institutional |
| 投信 | +77.8 | 億元 | twse-proxy /institutional |
| 自營商 | +12.4 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +386.6 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 217,999 | 張 | HiStock |
| 融券增減 | 16,914 | 張 | HiStock |
| 融資維持率 | 193.87 | % | 前值遞補 (DATA 2026-09-29；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,407,135 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

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
| S&P 500 | ^GSPC | 7,670.84 | -12.85 | -0.17 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 26,797.54 | -22.84 | -0.09 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,339.33 | 62.52 | +0.21 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,349.92 | -131.59 | -0.26 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 12,629.16 | 163.92 | +1.32 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.10 | 0.06 | +0.37 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 66,753.72 | 1,272.45 | +1.94 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 6,838.04 | -32.77 | -0.48 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,613.27 | 89.70 | +0.37 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.19 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,730.00 | -2.00 | -0.03 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,572.00 | -41.25 | -0.13 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,662.00 | -40.00 | -0.08 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,824.20 | -5.00 | -0.18 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.89 | -0.03 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.26 | 0.02 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.59 | 0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.87 | 0.08 | +0.27 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 101.22 | -0.15 | -0.15 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 157.10 | -0.26 | -0.17 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,354.75 | -4.81 | -0.35 | Yahoo Finance Chart API |

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
| WTI原油期貨 | CL=F | 90.64 | 1.26 | +1.41 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,215.10 | 35.40 | +0.85 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 83,815.71 | 193.28 | +0.23 | Yahoo Finance Chart API |

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
- 事件6：2026台北生技獎151件參賽創新高　AI助攻迎產業轉型契機
  - 來源：Yahoo 台股；發布時間：2026-09-30T11:01:41Z；台北時間：2026-09-30 19:01
  - 摘要：【互傳媒／記者 謝忠義／台北 報導】臺北市長蔣萬安今（30）日出席「2026臺北生技獎頒獎典禮暨成果交流會」，
  - 原文連結：https://tw.stock.yahoo.com/news/2026%E5%8F%B0%E5%8C%97%E7%94%9F%E6%8A%80%E7%8D%8E151%E4%BB%B6%E5%8F%83%E8%B3%BD%E5%89%B5%E6%96%B0%E9%AB%98-ai%E5%8A%A9%E6%94%BB%E8%BF%8E%E7%94%A2%E6%A5%AD%E8%BD%89%E5%9E%8B%E5%A5%91%E6%A9%9F-110141598.html
- 事件7：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 來源：Federal Reserve；發布時間：Fri, 25 Sep 2026 20:30:00 GMT；台北時間：2026-09-26 04:30
  - 摘要：Federal Reserve Board announces approval of application by Peoples Bancorp Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20260925a.htm
- 事件8：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin issuers under the GENIUS Act
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 18:30:00 GMT；台北時間：2026-09-25 02:30
  - 摘要：Federal Reserve Board requests public comment on two proposals related to establishing a regulatory framework for Board-supervised payment stablecoin 
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260924a.htm
- 事件9：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 來源：Federal Reserve；發布時間：Thu, 24 Sep 2026 15:00:00 GMT；台北時間：2026-09-24 23:00
  - 摘要：Federal Reserve Board issues enforcement action with former employee of Sandy Spring Bank
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260924a.htm
- 事件10：Inside Man: How Chinese spies used lies, love and betrayal to target the Federal Reserve
  - 來源：CNBC；發布時間：Wed, 30 Sep 2026 10:55:49 GMT；台北時間：2026-09-30 18:55
  - 摘要：A CNBC investigation shows how former Fed advisor John Rogers became entangled with a man U.S. officials identify as a Chinese intelligence operative.
  - 原文連結：https://www.cnbc.com/2026/09/30/john-rogers-fed-china-espionage-case.html
- 事件11：The Fed's main inflation measure will be released Wednesday. Here's what to expect
  - 來源：CNBC；發布時間：Tue, 29 Sep 2026 20:51:43 GMT；台北時間：2026-09-30 04:51
  - 摘要：Data is expected to show ongoing price pressures and consumers who nevertheless continue to spend.
  - 原文連結：https://www.cnbc.com/2026/09/29/the-feds-main-inflation-measure-will-be-released-wednesday-heres-what-to-expect.html
- 事件12：Trump denies offering Iran sanctions relief; Tehran receives U.S. proposal following Qatar talks
  - 來源：CNBC；發布時間：Wed, 30 Sep 2026 09:45:54 GMT；台北時間：2026-09-30 17:45
  - 摘要：U.S. President Donald Trump has denied reports that he had offered sanctions relief to Iran in exchange for concessions from Tehran on its nuclear pro
  - 原文連結：https://www.cnbc.com/2026/09/30/us-iran-war-trump-hormuz.html


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
| 開盤價 | 47,992 | TAIFEX Proxy |
| 最高價 | 48,619 | TAIFEX Proxy |
| 最低價 | 47,920 | TAIFEX Proxy |
| 收盤價 | 48,479 | TAIFEX Proxy |
| 漲跌點數 | +698 | TAIFEX Proxy |
| 漲跌幅 | +1.46 | TAIFEX Proxy |
| 成交量 | 29,632 | TAIFEX Proxy |
| 夜盤高點及低點 | 48,619 / 47,920 | TAIFEX Proxy |
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
| 前十大交易人多方 OI | 77,082 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,340 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,742 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-24→2026-09-29) | -2,652 | TAIFEX Proxy snapshots (2026-09-29) |
- 資料日期：2026-09-29 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 42,583 | TAIFEX Proxy |
| 外資日盤空單交易量 | 41,737 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +846 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 16,951 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 15,131 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,820 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | -974 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +1,027 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +1,027 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -536 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -340 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -196 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +1,337 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,480 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +129.1 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +142.9 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 48,330 | TAIFEX Proxy |
| 加權指數價格 | 47,940.13 | twse-proxy |
| 台指期與加權指數價差 | +389.87 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.81 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +389.87 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | +149 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 48,330 | 48,479 | -149 | TAIFEX Proxy |
| 成交量 | 42,731 | 29,632 | +13,099 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+1,323（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 42,583 | 41,737 | +846 | 16,951 | 15,131 | +1,820 | -974 | 12,351 | 90,502 | -78,151 | +878 | TAIFEX Proxy |
| 投信 | 1,036 | 9 | +1,027 | 0 | 0 | +0 | +1,027 | 76,739 | 2,900 | +73,839 | +1,027 | TAIFEX Proxy |
| 自營商 | 3,841 | 4,377 | -536 | 860 | 1,200 | -340 | -196 | 3,182 | 4,252 | -1,070 | -582 | TAIFEX Proxy |
| 三大法人合計 | 47,460 | 46,123 | +1,337 | 17,811 | 16,331 | +1,480 | -143 | 92,272 | 97,654 | -5,382 | +1,323 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 77,082 | TAIFEX Proxy |
| 前十大交易人空方 OI | 72,340 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +4,742 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-24→2026-09-29) | -2,652 | TAIFEX Proxy snapshots (2026-09-29) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 40.95% | TAIFEX Proxy |
| 夜盤漲跌點數 | +698 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +1,820 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-09-30 | TAIFEX Proxy |
| 到期月份／到期日 | 202609W5 | TAIFEX Proxy |
| 資料更新時間 | 2026-09-30 19:14:48 | 本機 |
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
| Call／Put 比例變化 (量比 2026-09-24→2026-09-29) | -30.72 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-09-24→2026-09-29) | -10.03 | TAIFEX Proxy |
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
| 外資 Call夜買 | 36,640 | TAIFEX Proxy |
| 外資 Call夜賣 | 36,765 | TAIFEX Proxy |
| 外資 Call夜淨 | -125 | TAIFEX Proxy |
| 外資 Put夜買 | 34,961 | TAIFEX Proxy |
| 外資 Put夜賣 | 35,296 | TAIFEX Proxy |
| 外資 Put夜淨 | -335 | TAIFEX Proxy |
| 外資 日盤淨總量 | -5,219 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | -4,385 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +1,044 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 81,837 | TAIFEX Proxy |
| 自營商 Call日賣 | 86,441 | TAIFEX Proxy |
| 自營商 Call日淨 | -4,604 | TAIFEX Proxy |
| 自營商 Put日買 | 83,393 | TAIFEX Proxy |
| 自營商 Put日賣 | 90,032 | TAIFEX Proxy |
| 自營商 Put日淨 | -6,639 | TAIFEX Proxy |
| 自營商 Call夜買 | 23,900 | TAIFEX Proxy |
| 自營商 Call夜賣 | 25,835 | TAIFEX Proxy |
| 自營商 Call夜淨 | -1,935 | TAIFEX Proxy |
| 自營商 Put夜買 | 25,519 | TAIFEX Proxy |
| 自營商 Put夜賣 | 26,455 | TAIFEX Proxy |
| 自營商 Put夜淨 | -936 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +2,035 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | -2,669 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -5,703 | TAIFEX Proxy |

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
| Gamma Wall 價位 | 47,500.00 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 資料日期 | 2026-09-29 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | 46,571.99 | TAIFEX Proxy (options-market-structure-compact (proxy)) |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 資料日期 | 2026-09-29 | TAIFEX Proxy (options-market-structure-compact (proxy)) |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,150 | TAIFEX Proxy |
| 對應到期月份 | 202609W5 | TAIFEX Proxy |
| 與前一交易日的變化 | unavailable | 端點未提供 |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 207,005 | 212,224 | -5,219 | 71,936 | 71,726 | +210 | -5,429 | TAIFEX Proxy |
| 投信 | 371 | 3,104 | -2,733 | 0 | 0 | +0 | -2,733 | TAIFEX Proxy |
| 自營商 | 171,869 | 169,834 | +2,035 | 50,355 | 51,354 | -999 | +3,034 | TAIFEX Proxy |
| 三大法人合計 | 379,245 | 385,162 | -5,917 | 122,291 | 123,080 | -789 | -5,128 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 8.92 | 8.79 | +0.12 | 4.31 | 4.23 | +0.08 | +0.04 | TAIFEX Proxy |
| 投信 | 0.11 | 1.96 | -1.85 | 0.00 | 0.00 | +0 | -1.85 | TAIFEX Proxy |
| 自營商 | 8.80 | 7.00 | +1.79 | 2.84 | 2.60 | +0.24 | +1.56 | TAIFEX Proxy |
| 三大法人合計 | 17.82 | 17.76 | +0.07 | 7.15 | 6.83 | +0.32 | -0.25 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 11,785 | TAIFEX Proxy |
| 買權空方 OI | 11,166 | TAIFEX Proxy |
| 買權多空淨 OI | +619 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-24→2026-09-29) | -497 | TAIFEX Proxy snapshots (2026-09-29) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 7,868 | TAIFEX Proxy |
| 賣權空方 OI | 8,669 | TAIFEX Proxy |
| 賣權多空淨 OI | -801 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-24→2026-09-29) | +81 | TAIFEX Proxy snapshots (2026-09-29) |
- 資料日期：買權 2026-09-29／賣權 2026-09-29 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -2,652 | 2026-09-24→2026-09-29 | TAIFEX Proxy snapshots (2026-09-29) |
| 買權前十大 | -497 | 2026-09-24→2026-09-29 | TAIFEX Proxy snapshots (2026-09-29) |
| 賣權前十大 | +81 | 2026-09-24→2026-09-29 | TAIFEX Proxy snapshots (2026-09-29) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-09-30；資料時間：2026-09-30 19:14:48；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (5)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, options.chain_oi_change
- 註記：Gamma 資料日期 2026-09-29 (T0 2026-09-30 尚無，上游 FMTQIK 落後，採最新可得)
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 資料日期 2026-09-29 (來源 options-market-structure-compact (proxy))

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-09-29；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-09-29)，非 T0 2026-09-30
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +296.4 | -78,151 | +846 | +1,820 | -5,219 | +210 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | +77.8 | +73,839 | +1,027 | +0 | -2,733 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +12.4 | -1,070 | -536 | -340 | +2,035 | -999 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
