# DATA_REPORT_TEMPLATE.md — 資料層報告模板規範 (資料層 Rule 3/4)

版本： V2.0 | 正本：`D:\Chatgpt 正式文件\每日盤前分析\Github\cloudflare-github-test-main-09162150\cloudflare-github-test-main\DATA_REPORT_TEMPLATE.md`
(正本為準；本檔為實作對照摘要，`fetch_data.py` 依此產出)

## Header (逐字)

```markdown
# DATA_REPORT_yyyymmdd

- 報告日期：`YYYY-MM-DD`
- T0 交易日期：`YYYY-MM-DD`
- 資料產出時間：`YYYY-MM-DD HH:MM:SS`
- 時區：`Asia/Taipei`
```

## 一、現貨 (6 節，表頭見正本)

1. 台股大盤行情 — 加權/開/高/低/收/漲跌/漲跌幅/成交金額 (開高低目前 unavailable，MI_INDEX 無此欄)
2. 市場漲跌家數 — 2.1 上市 (twse-proxy) / 2.2 上櫃 (TPEX)，上漲/下跌/平盤/漲停/跌停
3. 三大法人現貨買賣超 — 外資/投信/自營商/合計 (億元)
4. 融資融券 — 餘額/增減 (張) + 維持率 (unavailable)
5. 借券資料 — 餘額/賣出餘額 (股) + 賣出增減 (unavailable)
6. 市場成交結構 — 上市/上櫃/合計 (億元；上櫃百萬元→億元)

## 二、重要市場 (9 節，API 優先、失敗 unavailable 不推估，保留 data_source/retrieved_at/timezone)

1. 美股指數 `^GSPC ^IXIC ^NDX ^DJI ^SOX ^VIX` 2. 亞洲 `^N225 ^KS11 ^HSI 000001.SS 399001.SZ`
3. 美股期貨 `ES=F NQ=F YM=F RTY=F` 4. 美債 `2 Yr 10 Yr 30 Yr` (FiscalData 主、Yahoo 備)
5. 匯率 `TWD=X DX-Y.NYB JPY=X KRW=X` 6. ADR `TSM UMC ASX`
7. 商品 `CL=F GC=F BTC-USD` (期貨勿標現貨；BTC 用最新價) 8. 重大事件/新聞 (Phase 2，本階段 unavailable)
9. 產業資金流向 (StockIntelli API，流入/流出前5；備援 unavailable)

## 三、期貨 (7 項骨架，Phase 2 接 TAIFEX Proxy；本階段 unavailable)

日盤行情 / 夜盤行情 / 法人多空 OI / 前十大 OI / 日夜盤法人交易 / 期現關係 / 日夜盤籌碼對照

## 四、選擇權 (16 項骨架，Phase 2；本階段 unavailable)

日期到期 / Call 總量 / Put 總量 / C/P 比例 / 外資部位 / 自營部位 / Call 集中 / Put 集中 /
Call 增減集中 / Put 增減集中 / Call Wall / Put Wall / Gamma Wall / Gamma Flip / Max Pain /
來源時間時區狀態

## 五、資料來源、時間與完整性 (實作追加，滿足「保留來源/時間/時區」規則)

來源列表 + 未取得欄位 + 註記 + 「僅整理資料，不提供交易判斷」
