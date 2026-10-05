# DATA_REPORT_20261005

- 報告日期：`2026-10-05`
- T0 交易日期：`2026-10-05`
- 資料產出時間：`2026-10-05 19:16:04`
- 時區：`Asia/Taipei`

---

## 一、現貨

### 1. 台股大盤行情

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI MI_INDEX`)

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 加權指數 | 49,712.04 | 點 | twse-proxy |
| 開盤 | 48,574.95 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最高 | 49,770.66 | 點 | FinMind TaiwanStockPrice TAIEX |
| 最低 | 48,574.95 | 點 | FinMind TaiwanStockPrice TAIEX |
| 收盤 | 49,712.04 | 點 | twse-proxy |
| 漲跌點數 | 1,236.30 | 點 | twse-proxy |
| 漲跌幅 | +2.55 | % | twse-proxy |
| 成交金額 | 12,110.4 | 億元 | twse-proxy market_statistics |

### 2. 市場漲跌家數

#### 2.1 上市公司

**資料來源：** `Cloudflare Worker：twse-proxy` (備援 `TWSE OpenAPI twtazu_od`)

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 364 | twse-proxy |
| 下跌家數 | 631 | twse-proxy |
| 平盤家數 | 87 | twse-proxy |
| 漲停家數 | 27 | twse-proxy |
| 跌停家數 | 0 | twse-proxy |

#### 2.2 上櫃公司

**資料來源：** `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 家數 | 資料來源 |
|---|---|---|
| 上漲家數 | 296 | TPEX OpenAPI tpex_mainborad_highlight |
| 下跌家數 | 499 | TPEX OpenAPI tpex_mainborad_highlight |
| 平盤家數 | 76 | TPEX OpenAPI tpex_mainborad_highlight |
| 漲停家數 | 22 | TPEX OpenAPI tpex_mainborad_highlight |
| 跌停家數 | 4 | TPEX OpenAPI tpex_mainborad_highlight |

### 3. 三大法人現貨買賣超

**資料來源：** `TWSE RWD BFI82U`

| 法人別 | 買賣超金額 | 單位 | 資料來源 |
|---|---|---|---|
| 外資 | +719.0 | 億元 | twse-proxy /institutional |
| 投信 | -63.9 | 億元 | twse-proxy /institutional |
| 自營商 | +109.5 | 億元 | twse-proxy /institutional |
| 三大法人合計 | +764.5 | 億元 | twse-proxy /institutional |

### 4. 融資融券

**資料來源：** 上市+上櫃 `HiStock` (金額口徑)；維持率 `istock.tw`；備援官方逐股加總

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 融資餘額 | unavailable | 億元 | HiStock |
| 融資增減 | unavailable | 億元 | HiStock |
| 融券餘額 | 231,986 | 張 | HiStock |
| 融券增減 | 3,124 | 張 | HiStock |
| 融資維持率 | 195.13 | % | 前值遞補 (DATA 2026-10-02；當日三源皆失敗；民間估算；官方無每日序列) |

### 5. 借券資料

**資料來源：** 上市 `TWSE OpenAPI TWT96U` (可借餘額)、上櫃 `TPEX OpenAPI tpex_margin_sbl`

| 項目 | 數值 | 單位 | 資料來源 |
|---|---|---|---|
| 借券餘額 | 2,394,211 | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出餘額 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |
| 借券賣出增減 | unavailable | 張 | TWSE TWT93U + TPEX margin_sbl |

### 6. 市場成交結構

**資料來源：** 上市 `twse-proxy market_statistics`、上櫃 `TPEX OpenAPI tpex_mainborad_highlight`

| 項目 | 成交金額 | 單位 | 資料來源 |
|---|---|---|---|
| 上市成交金額 | 12,110.4 | 億元 | twse-proxy market_statistics |
| 上櫃成交金額 | 3,213.9 | 億元 | TPEX OpenAPI tpex_mainborad_highlight |
| 上市櫃成交金額合計 | 15,324.3 | 億元 | twse-proxy market_statistics+TPEX OpenAPI tpex_mainborad_highlight |

## 二、重要市場

### 1. 美股指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P 500 | ^GSPC | 7,722.72 | 56.27 | +0.73 | Yahoo Finance Chart API |
| Nasdaq Composite | ^IXIC | 27,190.86 | 319.26 | +1.19 | Yahoo Finance Chart API |
| Nasdaq 100 | ^NDX | 30,807.93 | 306.37 | +1.00 | Yahoo Finance Chart API |
| Dow Jones | ^DJI | 51,176.96 | 250.40 | +0.49 | Yahoo Finance Chart API |
| 費城半導體 SOX | ^SOX | 13,136.67 | 307.67 | +2.40 | Yahoo Finance Chart API |
| VIX | ^VIX | 16.22 | 0.91 | +5.94 | Yahoo Finance Chart API |

### 2. 亞洲主要指數

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 日經225 | ^N225 | 69,946.86 | 1,637.40 | +2.40 | Yahoo Finance Chart API |
| 韓國KOSPI | ^KS11 | 7,003.74 | 32.39 | +0.46 | Yahoo Finance Chart API |
| 香港恆生 | ^HSI | 24,040.34 | 68.05 | +0.28 | Yahoo Finance Chart API |
| 上海綜合 | 000001.SS | 3,842.20 | 11.74 | +0.31 | Yahoo Finance Chart API |
| 深圳成分 | 399001.SZ | 12,887.62 | -14.33 | -0.11 | Yahoo Finance Chart API |

### 3. 美股指數期貨

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| S&P500期貨 | ES=F | 7,768.25 | -9.00 | -0.12 | Yahoo Finance Chart API |
| Nasdaq100期貨 | NQ=F | 30,998.75 | -63.00 | -0.20 | Yahoo Finance Chart API |
| 道瓊期貨 | YM=F | 51,407.00 | -70.00 | -0.14 | Yahoo Finance Chart API |
| Russell2000期貨 | RTY=F | 2,851.50 | 0.60 | +0.02 | Yahoo Finance Chart API |

### 4. 美國國債殖利率

**資料來源：** `U.S. Treasury Fiscal Data API` (失敗時備援 Treasury yield.xml 與 `Yahoo Finance`)

| 項目 | API 資料欄位／識別 | 殖利率 | 日變化 | 資料來源 |
|---|---|---|---|---|
| 美國 2 年期殖利率 | 2 Yr | 4.83 | 0.05 | U.S. Treasury yield.xml (網頁備援) |
| 美國 10 年期殖利率 | 10 Yr | 5.28 | 0.04 | Yahoo Finance (備援) |
| 美國 30 年期殖利率 | 30 Yr | 5.63 | 0.03 | Yahoo Finance (備援) |

### 5. 主要匯率

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| USD/TWD | TWD=X | 31.75 | -0.13 | -0.42 | Yahoo Finance Chart API |
| DXY美元指數 | DX-Y.NYB | 102.22 | 0.29 | +0.29 | Yahoo Finance Chart API |
| USD/JPY | JPY=X | 158.10 | 0.17 | +0.11 | Yahoo Finance Chart API |
| USD/KRW | KRW=X | 1,342.48 | -18.11 | -1.33 | Yahoo Finance Chart API |

### 6. 台灣相關ADR

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| 台積電ADR | TSM | 472.78 | 13.58 | +2.96 | Yahoo Finance Chart API |
| 聯電ADR | UMC | 26.27 | 1.06 | +4.20 | Yahoo Finance Chart API |
| 日月光ADR | ASX | 47.45 | 2.72 | +6.08 | Yahoo Finance Chart API |

### 7. 原油黃金Bitcoin

**資料來源：** `Yahoo Finance Chart API` (API 優先；失敗標 unavailable，不推估)

| 項目 | Yahoo Finance 代號 | 收盤／最新值 | 漲跌點 | 漲跌幅 | 資料來源 |
|---|---|---|---|---|---|
| WTI原油期貨 | CL=F | 90.51 | -0.60 | -0.66 | Yahoo Finance Chart API |
| 黃金期貨 | GC=F | 4,189.70 | 27.40 | +0.66 | Yahoo Finance Chart API |
| Bitcoin | BTC-USD | 85,939.18 | -541.12 | -0.63 | Yahoo Finance Chart API |

### 8. 重大經濟數據、央行事件與重大市場新聞

**資料來源：** 台股 `tw.stock.yahoo.com` (含內文摘要)；國際 `Fed 公告 RSS`＋`CNBC`＋`MarketWatch` (標題、來源、時間與連結)

- 事件1：台股4萬9行情誰在踩油門 神山帶隊衛星PCB齊飛
  - 來源：Yahoo 台股；發布時間：2026-10-05T09:06:11Z；台北時間：2026-10-05 17:06
  - 摘要：台積領軍、電子股點火，台股狂飆1236點再創高！今(5)日加權指數終場上漲1,236.30點，收49,712.04點，成交金額放大至11,528.42億元；盤中最高衝上49,770.66點，距五萬點大關僅約229點。櫃買指數上漲1.30%，
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87719%E5%84%84%E7%81%8C%E5%8F%B0%E8%82%A1%E9%A3%86%E5%8D%83%E9%BB%9E%E8%A1%9D4%E8%90%AC9%E6%96%B0%E9%AB%98%EF%BC%81%E5%8F%B0%E7%A9%8D%E6%8F%AA%E9%AB%98%E5%83%B9%E5%9C%98%E8%A1%9D-%E4%BD%8E%E8%BB%8C%E8%A1%9B%E6%98%9F%E3%80%81pcb%E4%B8%80%E8%B5%B7%E9%A3%9B%EF%BD%9Cyahoo%E8%B2%A1%E7%B6%93%E6%8E%83%E6%8F%8F-090611807.html
- 事件2：外資買超ETF榜主動軍團洗版 00403A領軍包辦前六名
  - 來源：Yahoo 台股；發布時間：2026-10-05T10:30:00Z；台北時間：2026-10-05 18:30
  - 摘要：[FTNN新聞網]記者吳峻光／綜合報導台股今（5）日大漲超過1200點，加權指數收49,712.04史上最高點，成交量放大至1.21兆元，證交所也公布外資大舉買超718.96億...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%96%E8%B3%87%E8%B2%B7%E8%B6%85718%E5%84%84%E4%BB%8A%E5%B9%B4%E7%AC%AC9%E5%A4%A7-%E7%91%A4%E6%B1%A0%E9%87%91%E6%AF%8D%E5%B8%AB%E5%A7%8A%E5%BC%9F%E7%8D%B2%E7%96%BC26%E8%90%AC%E5%BC%B5-%E4%B8%BB%E5%8B%95etf-%E5%8C%85%E8%BE%A6%E5%89%8D6%E5%90%8D-%E7%86%B1%E9%8C%A2%E5%88%B7%E6%A6%9C-103000019.html
- 事件3：自己蓋廠太慢找台積比較快 專家拆解馬斯克合作盤算
  - 來源：Yahoo 台股；發布時間：2026-10-05T09:54:33Z；台北時間：2026-10-05 17:54
  - 摘要：財經中心／楊思敏、吳志恆 台北報導市場傳出台積電評估，在美國德州蓋第二個廠區的傳聞，當時公司表示不予評論，但隨後Space X執行長馬斯克想要和台積電合作建廠，他證實傳聞，說「目前只是在討論階段」。專家分析，馬斯克是晶圓製造門外漢，想透過台
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%A6%AC%E6%96%AF%E5%85%8B%E5%B0%8B%E6%B1%82%E8%88%87%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%90%88%E4%BD%9C-%E5%B0%88%E5%AE%B6-%E6%83%B3%E7%A2%BA%E4%BF%9D%E6%99%B6%E7%89%87%E4%BE%9B%E6%87%89-095433853.html
- 事件4：鳳梨酥名店告別興櫃倒數 維格餅家拚業績改善再回歸
  - 來源：Yahoo 台股；發布時間：2026-10-05T08:58:21Z；台北時間：2026-10-05 16:58
  - 摘要：昔日有「陸客概念股」之稱的鳳梨酥業者維格餅家（2733）退出興櫃市場日期確定。公司今（5）日公告，已接獲櫃買中心通知，股票將自10月20日起終止興櫃買賣。
  - 原文連結：https://tw.stock.yahoo.com/news/%E9%99%B8%E5%AE%A2%E4%B8%8D%E4%BE%86%EF%BC%81%E9%B3%B3%E6%A2%A8%E9%85%A5%E6%A5%AD%E8%80%85%E3%80%8C%E7%B6%AD%E6%A0%BC%E9%A4%85%E5%AE%B6%E3%80%8D1020%E7%B5%82%E6%AD%A2%E8%88%88%E6%AB%83%E8%B2%B7%E8%B3%A3-085108422.html
- 事件5：6檔股票明起抓去關 天擎6個交易日飆59%入列處置
  - 來源：Yahoo 台股；發布時間：2026-10-05T10:38:15Z；台北時間：2026-10-05 18:38
  - 摘要：證交所與櫃買中心公告新增6檔處置股，包含上市的佳大、晶心科、無敵、輝騰電子-KY，以及上櫃由田、天擎，自6日起至13日採2分鐘分盤交易。這6檔個股因股價漲幅過大、成交量放大或週轉率偏高而遭列處置，投資人近期操作相關標的應特別注意市場波動與交
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A2%9E6%E6%AA%94%E6%8A%93%E5%8E%BB%E9%97%9C-6%E5%A4%A9%E9%A3%8659-%E9%80%99%E6%AA%94-%E5%85%A5%E5%88%97-101200386.html
- 事件6：大哥提款63億也要買！國巨受村田停產MLCC掀商機成最愛　「這檔」迎ABF成長強勁、Q4看增同走揚
  - 來源：Yahoo 台股；發布時間：2026-10-05T11:00:00Z；台北時間：2026-10-05 19:00
  - 摘要：[FTNN新聞網]記者邱梓欣／綜合報導由於美股前一交易日全面上漲，激勵台股今（5）日開高走高，加權指數終場大漲1236點，以49712.04點作收，漲幅2.55％，距5萬...
  - 原文連結：https://tw.stock.yahoo.com/news/%E5%A4%A7%E5%93%A5%E6%8F%90%E6%AC%BE63%E5%84%84%E4%B9%9F%E8%A6%81%E8%B2%B7-%E5%9C%8B%E5%B7%A8%E5%8F%97%E6%9D%91%E7%94%B0%E5%81%9C%E7%94%A2mlcc%E6%8E%80%E5%95%86%E6%A9%9F%E6%88%90%E6%9C%80%E6%84%9B-%E9%80%99%E6%AA%94-%E8%BF%8Eabf%E6%88%90%E9%95%B7%E5%BC%B7%E5%8B%81-q4%E7%9C%8B%E5%A2%9E%E5%90%8C%E8%B5%B0%E6%8F%9A-110000734.html
- 事件7：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:45:00 GMT；台北時間：2026-10-03 04:45
  - 摘要：Federal Reserve Board announces approval of application by Fleur Capital Corporation
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/orders20261002a.htm
- 事件8：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 20:00:00 GMT；台北時間：2026-10-03 04:00
  - 摘要：Federal Reserve Board announces it will extend, until November 4, the comment period on its proposal to modernize Regulation O
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20261002a.htm
- 事件9：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 來源：Federal Reserve；發布時間：Fri, 2 Oct 2026 15:00:00 GMT；台北時間：2026-10-02 23:00
  - 摘要：Federal Reserve Board issues enforcement action with Ontario Bancorporation, Inc.
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/enforcement20261002a.htm
- 事件10：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress test-related capital requirements
  - 來源：Federal Reserve；發布時間：Wed, 30 Sep 2026 13:00:00 GMT；台北時間：2026-09-30 21:00
  - 摘要：Federal Reserve Board finalizes changes to enhance the transparency and public accountability of its stress test and reduce volatility in its stress t
  - 原文連結：https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm
- 事件11：What Bessent is now saying after bond yields didn't stop rising on &#x2018;I am the house' remark
  - 來源：MarketWatch；發布時間：Mon, 05 Oct 2026 10:39:00 GMT；台北時間：2026-10-05 18:39
  - 摘要：In a televisxed interview with Axios, Treasury Secretary Bessent defended his department&#x2019;s record in the bond market and walked back his &#x201
  - 原文連結：https://www.marketwatch.com/story/what-bessent-is-now-saying-after-bond-yields-didnt-stop-rising-on-i-am-the-house-remark-0ab359f8?mod=mw_rss_topstories
- 事件12：Saudi Aramco chief says replenishing global oil stockpiles could take two years
  - 來源：CNBC；發布時間：Mon, 05 Oct 2026 11:00:27 GMT；台北時間：2026-10-05 19:00
  - 摘要：Saudi Aramco's CEO warned it could take up to two years to rebuild global oil inventories, saying the squeeze could worsen as the U.S.-Iran war contin
  - 原文連結：https://www.cnbc.com/2026/10/05/aramco-saudi-arabia-iran-hormuz-oil-energy.html


## 三、期貨

**資料來源：**
1. Cloudflare Workers：TAIFEX Proxy — https://taifex.grichtoyang.workers.dev/
2. TAIFEX Open API — https://openapi.taifex.com.tw/

近月契約月份：202610 (日盤成交量最大者)；交易日期：2026-10-05

### 1．台指期近月日盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 49,470 | TAIFEX Proxy |
| 最高價 | 50,097 | TAIFEX Proxy |
| 最低價 | 49,461 | TAIFEX Proxy |
| 收盤價 | 49,949 | TAIFEX Proxy |
| 漲跌點數 | +1,280 | TAIFEX Proxy |
| 漲跌幅 | +2.63 | TAIFEX Proxy |
| 成交量 | 74,146 | TAIFEX Proxy |
| 日盤高點及低點 | 50,097 / 49,461 | TAIFEX Proxy |

### 2．台指期近月夜盤行情

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 開盤價 | 48,671 | TAIFEX Proxy |
| 最高價 | 49,495 | TAIFEX Proxy |
| 最低價 | 48,671 | TAIFEX Proxy |
| 收盤價 | 49,346 | TAIFEX Proxy |
| 漲跌點數 | +677 | TAIFEX Proxy |
| 漲跌幅 | +1.39 | TAIFEX Proxy |
| 成交量 | 32,288 | TAIFEX Proxy |
| 夜盤高點及低點 | 49,495 / 48,671 | TAIFEX Proxy |
| 結算價 | 49,944 | TAIFEX Proxy |
| 未平倉量 | 108,339 | TAIFEX Proxy |

### 3．法人台指期多空未平倉部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資多方 OI | 14,760 | TAIFEX Proxy |
| 外資空方 OI | 91,764 | TAIFEX Proxy |
| 外資多空淨 OI | -77,004 | TAIFEX Proxy |
| 投信多方 OI | 77,893 | TAIFEX Proxy |
| 投信空方 OI | 2,749 | TAIFEX Proxy |
| 投信多空淨 OI | +75,144 | TAIFEX Proxy |
| 自營商多方 OI | 2,810 | TAIFEX Proxy |
| 自營商空方 OI | 4,965 | TAIFEX Proxy |
| 自營商多空淨 OI | -2,155 | TAIFEX Proxy |
| 三大法人合計多方 OI | 95,463 | TAIFEX Proxy |
| 三大法人合計空方 OI | 99,478 | TAIFEX Proxy |
| 三大法人合計多空淨 OI | -4,015 | TAIFEX Proxy |
| 外資多空淨 OI 變化 | +3,300 | TAIFEX Proxy |
| 投信多空淨 OI 變化 | +475 | TAIFEX Proxy |
| 自營商多空淨 OI 變化 | -1,149 | TAIFEX Proxy |

### 4．前十大交易人多空未平倉部位

**資料來源：** `TAIFEX OpenAPI OpenInterestOfLargeTradersFutures` (官方資料落後約一日，標示實際日期)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,719 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,942 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +3,777 | TAIFEX Proxy |
| 多空淨 OI 變化 (2026-09-30→2026-10-02) | -2,752 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：2026-10-02 (TypeOfTraders=0 全部交易人；契約月份 202610)

### 5．日盤、夜盤法人交易資料

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資日盤多單交易量 | 43,262 | TAIFEX Proxy |
| 外資日盤空單交易量 | 39,967 | TAIFEX Proxy |
| 外資日盤多空淨交易量 | +3,295 | TAIFEX Proxy |
| 外資夜盤多單交易量 | 18,921 | TAIFEX Proxy |
| 外資夜盤空單交易量 | 16,325 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,596 | TAIFEX Proxy |
| 外資日盤／夜盤交易量變化 | +699 | TAIFEX Proxy |
| 投信日盤多空淨交易量 | +475 | TAIFEX Proxy |
| 投信夜盤多空淨交易量 | +0 | TAIFEX Proxy |
| 投信日盤／夜盤交易量變化 | +475 | TAIFEX Proxy |
| 自營商日盤多空淨交易量 | -1,003 | TAIFEX Proxy |
| 自營商夜盤多空淨交易量 | -779 | TAIFEX Proxy |
| 自營商日盤／夜盤交易量變化 | -224 | TAIFEX Proxy |
| 三大法人日盤多空淨交易量 | +2,767 | TAIFEX Proxy |
| 三大法人夜盤多空淨交易量 | +1,817 | TAIFEX Proxy |
| 法人日盤交易金額淨額 (億元) | +273.2 | TAIFEX Proxy |
| 法人夜盤交易金額淨額 (億元) | +178.3 | TAIFEX Proxy |

### 6．期貨與現貨關係

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 台指期近月價格 | 49,949 | TAIFEX Proxy |
| 加權指數價格 | 49,712.04 | twse-proxy |
| 台指期與加權指數價差 | +236.96 | TAIFEX Proxy+twse-proxy |
| 價差百分比 | +0.48 | TAIFEX Proxy+twse-proxy |
| 日盤基差 | +236.96 | TAIFEX Proxy+twse-proxy |
| 夜盤價格相對日盤收盤的變化 | -603 | TAIFEX Proxy |

### 7．日盤、夜盤與籌碼變化對照

#### 7.1 日夜盤價格與成交量對照 (變化 = 日盤 - 夜盤)

| 項目 | 日盤 | 夜盤 | 變化 (日-夜) | 資料來源 |
|---|---|---|---|---|
| 收盤價 | 49,949 | 49,346 | +603 | TAIFEX Proxy |
| 成交量 | 41,858 | 32,288 | +9,570 | TAIFEX Proxy |
- 台指期總 OI 前日變化：+2,626（來源：TAIFEX Proxy）


#### 7.2 法人籌碼日夜盤對照 (淨變化 = 日盤淨 - 夜盤淨；OI 為日盤收盤後總量，前日變化另列)

| 法人 | 交易量 |  |  |  |  |  |  | 未平倉量 |  |  |  | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **日盤多單** | **日盤空單** | **日盤淨** | **夜盤多單** | **夜盤空單** | **夜盤淨** | **淨變化 (日-夜)** | **OI多方** | **OI空方** | **OI淨** | **OI前日變化** |  |
| 外資 | 43,262 | 39,967 | +3,295 | 18,921 | 16,325 | +2,596 | +699 | 14,760 | 91,764 | -77,004 | +3,300 | TAIFEX Proxy |
| 投信 | 579 | 104 | +475 | 0 | 0 | +0 | +475 | 77,893 | 2,749 | +75,144 | +475 | TAIFEX Proxy |
| 自營商 | 4,841 | 5,844 | -1,003 | 548 | 1,327 | -779 | -224 | 2,810 | 4,965 | -2,155 | -1,149 | TAIFEX Proxy |
| 三大法人合計 | 48,682 | 45,915 | +2,767 | 19,469 | 17,652 | +1,817 | +950 | 95,463 | 99,478 | -4,015 | +2,626 | TAIFEX Proxy |

#### 7.3 前十大交易人日夜盤對照 (OI 無日夜拆分，列收盤後總量)

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 前十大交易人多方 OI | 80,719 | TAIFEX Proxy |
| 前十大交易人空方 OI | 76,942 | TAIFEX Proxy |
| 前十大交易人多空淨 OI | +3,777 | TAIFEX Proxy |
| 前十大交易人多空淨 OI 變化 (2026-09-30→2026-10-02) | -2,752 | TAIFEX Proxy snapshots (2026-10-01) |

#### 7.4 夜盤劇本分類 (規則對應：夜盤漲跌 × 外資夜盤偏多空)

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 夜盤成交量占比 (夜盤量／(夜盤量＋日盤量)) | 43.55% | TAIFEX Proxy |
| 夜盤漲跌點數 | +677 | TAIFEX Proxy |
| 外資夜盤多空淨交易量 | +2,596 | TAIFEX Proxy |
| 劇本分類 | 劇本一 | 規則對應 |
| 劇本條件 | 夜盤上漲＋外資偏多 | 規則對應 |
| 劇本特徵 | 開高、續漲機率高 | 規則對應 |

## 四、選擇權

**資料來源：** 主要 TAIFEX 經 Cloudflare Worker Proxy；時區 `Asia/Taipei`

### 1．選擇權交易日期、到期日與資料時間

| 項目 | 數值 | 資料來源 |
|---|---|---|
| 交易日期 | 2026-10-05 | TAIFEX Proxy |
| 到期月份／到期日 | 202610W1 | TAIFEX Proxy |
| 資料更新時間 | 2026-10-05 19:16:04 | 本機 |
| 日盤／夜盤標記 | 日盤收盤後資料 | TAIFEX Proxy |

### 2．Call 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call 總成交量 | 150,404 | TAIFEX Proxy |
| Call 總未平倉量 OI | 36,246 | TAIFEX Proxy |
| Call OI 增減 (2026-10-01→2026-10-05) | +30,492 | TAIFEX Proxy snapshots (2026-10-01) |

### 3．Put 總成交量、OI、OI 增減

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put 總成交量 | 151,786 | TAIFEX Proxy |
| Put 總未平倉量 OI | 35,467 | TAIFEX Proxy |
| Put OI 增減 (2026-10-01→2026-10-05) | +29,229 | TAIFEX Proxy snapshots (2026-10-01) |

### 4．Call／Put 比例與變化

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call／Put 成交量比例 | 0.99 | TAIFEX Proxy |
| Call／Put 未平倉量比例 | 1.02 | TAIFEX Proxy |
| Put／Call Ratio | 0.98 | TAIFEX Proxy |
| Call／Put 比例變化 (量比 2026-10-01→2026-10-02) | -1.95 | TAIFEX Proxy |
| 與前一交易日比較 (OI 比 2026-10-01→2026-10-02) | -1.70 | TAIFEX Proxy |
**資料來源：** 比例 `TAIFEX Proxy chain`；變化 `TAIFEX Proxy PutCallRatio`

### 5．外資 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 外資 Call日買 | 52,075 | TAIFEX Proxy |
| 外資 Call日賣 | 50,899 | TAIFEX Proxy |
| 外資 Call日淨 | +1,176 | TAIFEX Proxy |
| 外資 Put日買 | 48,804 | TAIFEX Proxy |
| 外資 Put日賣 | 48,948 | TAIFEX Proxy |
| 外資 Put日淨 | -144 | TAIFEX Proxy |
| 外資 Call夜買 | 23,312 | TAIFEX Proxy |
| 外資 Call夜賣 | 23,420 | TAIFEX Proxy |
| 外資 Call夜淨 | -108 | TAIFEX Proxy |
| 外資 Put夜買 | 20,240 | TAIFEX Proxy |
| 外資 Put夜賣 | 20,479 | TAIFEX Proxy |
| 外資 Put夜淨 | -239 | TAIFEX Proxy |
| 外資 日盤淨總量 | +1,320 | TAIFEX Proxy |
| 外資 Call日夜淨增減 (日－夜) | +1,284 | TAIFEX Proxy |
| 外資 Put日夜淨增減 (日－夜) | +95 | TAIFEX Proxy |

### 6．自營商 Call／Put 部位

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 自營商 Call日買 | 46,390 | TAIFEX Proxy |
| 自營商 Call日賣 | 42,294 | TAIFEX Proxy |
| 自營商 Call日淨 | +4,096 | TAIFEX Proxy |
| 自營商 Put日買 | 44,917 | TAIFEX Proxy |
| 自營商 Put日賣 | 48,939 | TAIFEX Proxy |
| 自營商 Put日淨 | -4,022 | TAIFEX Proxy |
| 自營商 Call夜買 | 15,504 | TAIFEX Proxy |
| 自營商 Call夜賣 | 16,489 | TAIFEX Proxy |
| 自營商 Call夜淨 | -985 | TAIFEX Proxy |
| 自營商 Put夜買 | 15,539 | TAIFEX Proxy |
| 自營商 Put夜賣 | 17,245 | TAIFEX Proxy |
| 自營商 Put夜淨 | -1,706 | TAIFEX Proxy |
| 自營商 日盤淨總量 | +8,118 | TAIFEX Proxy |
| 自營商 Call日夜淨增減 (日－夜) | +5,081 | TAIFEX Proxy |
| 自營商 Put日夜淨增減 (日－夜) | -2,316 | TAIFEX Proxy |

### 7．主要 Call OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Call OI 第1大履約價 | 52,500 | 2,886 | TAIFEX Proxy |
| Call OI 第2大履約價 | 50,000 | 1,794 | TAIFEX Proxy |
| Call OI 第3大履約價 | 50,700 | 1,772 | TAIFEX Proxy |
| Call OI 最大履約價 | 52,500 | 2,886 | TAIFEX Proxy |

#### Call OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| C1 | 52,500 | 2,886 | 7.96% | TAIFEX Proxy |
| C2 | 50,000 | 1,794 | 4.95% | TAIFEX Proxy |
| C3 | 50,700 | 1,772 | 4.89% | TAIFEX Proxy |
| C4 | 52,000 | 1,363 | 3.76% | TAIFEX Proxy |
| C5 | 49,500 | 1,179 | 3.25% | TAIFEX Proxy |
| C6 | 50,500 | 992 | 2.74% | TAIFEX Proxy |
| C7 | 51,000 | 977 | 2.7% | TAIFEX Proxy |
| C8 | 50,400 | 967 | 2.67% | TAIFEX Proxy |
| C9 | 50,200 | 958 | 2.64% | TAIFEX Proxy |
| C10 | 46,600 | 950 | 2.62% | TAIFEX Proxy |


### 8．主要 Put OI 集中區

| 項目 | 履約價 | OI | 資料來源 |
|---|---|---|---|
| Put OI 第1大履約價 | 49,000 | 1,918 | TAIFEX Proxy |
| Put OI 第2大履約價 | 48,000 | 1,789 | TAIFEX Proxy |
| Put OI 第3大履約價 | 48,500 | 1,761 | TAIFEX Proxy |
| Put OI 最大履約價 | 49,000 | 1,918 | TAIFEX Proxy |

#### Put OI 分布明細 Top10 (機器可讀，到期月份 202610W1)

| # | 履約價 | OI | 佔比 | 資料來源 |
|---|---|---|---|---|
| P1 | 49,000 | 1,918 | 5.41% | TAIFEX Proxy |
| P2 | 48,000 | 1,789 | 5.04% | TAIFEX Proxy |
| P3 | 48,500 | 1,761 | 4.97% | TAIFEX Proxy |
| P4 | 48,800 | 1,392 | 3.92% | TAIFEX Proxy |
| P5 | 47,000 | 1,182 | 3.33% | TAIFEX Proxy |
| P6 | 48,200 | 1,108 | 3.12% | TAIFEX Proxy |
| P7 | 48,700 | 1,004 | 2.83% | TAIFEX Proxy |
| P8 | 48,600 | 832 | 2.35% | TAIFEX Proxy |
| P9 | 48,400 | 830 | 2.34% | TAIFEX Proxy |
| P10 | 43,800 | 821 | 2.31% | TAIFEX Proxy |


### 9．Call OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Call OI 增加最多的履約價 | 52,500 (+2,875) | TAIFEX Proxy snapshots (2026-10-01) |
| Call OI 減少最多的履約價 | 47,950 (-5) | TAIFEX Proxy snapshots (2026-10-01) |

### 10．Put OI 增減集中區

| 項目 | 履約價 (增減口數) | 資料來源 |
|---|---|---|
| Put OI 增加最多的履約價 | 49,000 (+1,913) | TAIFEX Proxy snapshots (2026-10-01) |
| Put OI 減少最多的履約價 | 43,300 (-4) | TAIFEX Proxy snapshots (2026-10-01) |

### 11．Call Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Call Wall 價位 | 52,500 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-05) | +3,500 | TAIFEX Proxy snapshots (2026-10-01) |

### 12．Put Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Put Wall 價位 | 49,000 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-05) | +1,000 | TAIFEX Proxy snapshots (2026-10-01) |

### 13．Gamma Wall

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Wall 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 14．Gamma Flip

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Gamma Flip 價位 | unavailable | 端點未提供 |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 資料日期 | unavailable | 端點未提供 |

### 15．Max Pain

| 項目 | 數值 | 資料來源 |
|---|---|---|
| Max Pain 價位 | 48,800 | TAIFEX Proxy |
| 對應到期月份 | 202610W1 | TAIFEX Proxy |
| 與前一交易日的變化 (2026-10-01→2026-10-05) | +850 | TAIFEX Proxy snapshots (2026-10-01) |

### 17．選擇權法人日盤、夜盤交易

| 法人 | 日盤多單 | 日盤空單 | 日盤淨 | 夜盤多單 | 夜盤空單 | 夜盤淨 | 淨變化 (日-夜) | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 101,023 | 99,703 | +1,320 | 43,791 | 43,660 | +131 | +1,189 | TAIFEX Proxy |
| 投信 | 0 | 2,150 | -2,150 | 0 | 0 | +0 | -2,150 | TAIFEX Proxy |
| 自營商 | 95,329 | 87,211 | +8,118 | 32,749 | 32,028 | +721 | +7,397 | TAIFEX Proxy |
| 三大法人合計 | 196,352 | 189,064 | +7,288 | 76,540 | 75,688 | +852 | +6,436 | TAIFEX Proxy |
- 方法論：多方＝買Call＋賣Put（看多），空方＝賣Call＋買Put（看空），淨額＝看多－看空（已用 Call／Put 拆分頁交叉驗算一致）
- 公式：多方(買)－空方(賣)＝（買call＋賣put）－（賣call＋買put）＝看多－看空
- 速記：多＝BC＋SP、空＝SC＋BP

#### 法人多空力道表（金額・億元；上游千元／1e5）

| 法人 | 日多方力道 | 日空方力道 | 日淨多空力道 | 夜多方力道 | 夜空方力道 | 夜淨多空力道 | 日淨－夜淨 | 資料來源 |
|---|---|---|---|---|---|---|---|---|
| 外資 | 10.04 | 9.55 | +0.49 | 4.29 | 4.25 | +0.04 | +0.45 | TAIFEX Proxy |
| 投信 | 0.00 | 1.58 | -1.58 | 0.00 | 0.00 | +0 | -1.58 | TAIFEX Proxy |
| 自營商 | 10.25 | 8.45 | +1.81 | 3.00 | 2.71 | +0.29 | +1.51 | TAIFEX Proxy |
| 三大法人合計 | 20.30 | 19.58 | +0.71 | 7.29 | 6.96 | +0.33 | +0.38 | TAIFEX Proxy |

### 18．選擇權前十大

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 買權多方 OI | 12,559 | TAIFEX Proxy |
| 買權空方 OI | 11,762 | TAIFEX Proxy |
| 買權多空淨 OI | +797 | TAIFEX Proxy |
| 買權多空淨 OI 變化 (2026-09-30→2026-10-02) | -249 | TAIFEX Proxy snapshots (2026-10-01) |

| 項目 | 口數 | 資料來源 |
|---|---|---|
| 賣權多方 OI | 8,179 | TAIFEX Proxy |
| 賣權空方 OI | 9,295 | TAIFEX Proxy |
| 賣權多空淨 OI | -1,116 | TAIFEX Proxy |
| 賣權多空淨 OI 變化 (2026-09-30→2026-10-02) | -492 | TAIFEX Proxy snapshots (2026-10-01) |
- 資料日期：買權 2026-10-02／賣權 2026-10-02 (TypeOfTraders=0 全部交易人；契約月份 202610)

#### 大戶流向（全日；前十大無日夜拆分）

| 項目 | 淨變化 | 區間 | 資料來源 |
|---|---|---|---|
| 期貨前十大 | -2,752 | 2026-09-30→2026-10-02 | TAIFEX Proxy snapshots (2026-10-01) |
| 買權前十大 | -249 | 2026-09-30→2026-10-02 | TAIFEX Proxy snapshots (2026-10-01) |
| 賣權前十大 | -492 | 2026-09-30→2026-10-02 | TAIFEX Proxy snapshots (2026-10-01) |

### 16．資料來源、時間、時區與狀態

- 資料來源：TAIFEX 經 Cloudflare Worker Proxy
- 資料日期：2026-10-05；資料時間：2026-10-05 19:16:04；時區：`Asia/Taipei`
- 日盤／夜盤標記：日盤收盤後 + 夜盤盤後
- 未取得欄位 (6)：margin.fin_yi, margin.fin_chg_yi, sbl.sale_bal, sbl.sale_chg, futures.gamma_wall, futures.gamma_flip
- 註記：法人交易量變化無昨日交易端點，標 unavailable
- 註記：Gamma Wall/Flip 無資料 (proxy 端點上游無資料)，標 unavailable

## 五、資料來源、時間與完整性

- 期貨/匯率為最新報價，其餘為 T0 收盤資料；時間皆為 `Asia/Taipei`。
- taiex：`twse-proxy`
- taiex_ohlc：`FinMind TaiwanStockPrice TAIEX`
- listed_turnover：`twse-proxy market_statistics`
- listed_breadth：`twse-proxy`
- otc：`TPEX OpenAPI tpex_mainborad_highlight`
- institutional：`twse-proxy /institutional`
- margin_short：`TWSE MI_MARGN + TPEX margin_balance (張)`
- margin_ratio：`前值遞補 (DATA 2026-10-02；當日三源皆失敗；民間估算；官方無每日序列)`
- sbl：`TWSE TWT93U + TPEX margin_sbl`
- 期貨選擇權：`TAIFEX Proxy`
- 新聞：台股 Yahoo／國際 Fed＋CNBC＋MarketWatch；台股 Yahoo（不足時財訊快報備援）/ 國際 Fed 公告＋CNBC＋MarketWatch RSS；Fed 無摘要；investing 港股為主已退役；cnyes CSR、wantgoo JS 算繪、中央社/台灣央行路徑待查，未採用
- 美股/亞股/期貨/匯率/ADR/商品：`Yahoo Finance Chart API`；美債：`Yahoo Finance (備援)`
- 註記：HiStock 未取得，融資餘額/增減標 unavailable (官方逐股加總僅有張數)
- 註記：融券沿用官方逐股加總 (張)
- 註記：融資維持率未取得 (三源皆失敗；官方無每日序列)
- 註記：融資維持率採前值遞補 (DATA 2026-10-02)，非 T0 2026-10-05
- 註記：上市 MI_MARGN / TWT96U 無日期欄，採用最新可得
- 本報告僅整理資料，不提供交易判斷。

## 六、期現選方向對照

**規則：** 趨勢偏多／空＝現貨、期貨OI、選擇權日淨三者同向；避險／對沖＝現貨與期選反向；日內反轉＝日淨與夜淨反向；缺值標示，不推估。選擇權多空為看多看空口徑。

| 法人 | 現貨買賣超(億) | 期貨OI淨(口) | 期貨日淨 | 期貨夜淨 | 選擇權日淨 | 選擇權夜淨 | 判定 | 期選組合 | 資料來源 |
|---|---|---|---|---|---|---|---|---|---|
| 外資 | +719.0 | -77,004 | +3,295 | +2,596 | +1,320 | +131 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
| 投信 | -63.9 | +75,144 | +475 | +0 | -2,150 | +0 | 避險／對沖 | 分歧 | twse-proxy／TAIFEX Proxy |
| 自營商 | +109.5 | -2,155 | -1,003 | -779 | +8,118 | +721 | 避險／對沖 | 強避險 | twse-proxy／TAIFEX Proxy |
