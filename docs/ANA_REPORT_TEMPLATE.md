# ANA_REPORT_TEMPLATE.md — 分析層報告模板規範 V2.0 (OpenCode 分析師用)

> 讀 `data_reports/DATA_REPORT_yyyymmdd.md` → 產出 `reports/Daily_REPORT_yyyymmdd.md`。
> 鐵律：數字只能來自 DATA_REPORT；缺值寫 N/A，不得臆測；**數據與判斷分開寫**；
> 總長 800~1500 字，繁體中文。文末附「機器可讀數據」供 Dashboard 繪圖。

```markdown
# 每日盤前分析 Daily_REPORT_yyyymmdd

- 報告日期： yyyymmdd
- 資料基準： DATA_REPORT_yyyymmdd.md
- 原始資料： [DATA_REPORT_yyyymmdd.md](../data_reports/DATA_REPORT_yyyymmdd.md)
- 一句話結論： (偏多 / 偏空 / 震盪整理 + 關鍵理由，30字內)

## 1. 關鍵數據一覽 (純數據，不評論，8~10 項)

| 數據 | 數值 |
|------|------|
| ... | ... |

## 2. 國際市場解讀 (數據 → 判斷)

...

## 3. 台股籌碼解讀 (數據 → 判斷)

...

## 4. 期貨選擇權解讀 (數據 → 判斷)

...

## 5. 關鍵價位與今日交易計畫

- 壓力： xxxxx (來源：Call Wall)
- 中軸： xxxxx (來源：Max Pain)
- 支撐： xxxxx (來源：Put Wall)

| 情境 | 條件 | 操作建議 |
|------|------|----------|
| 開高 | ... | ... |
| 開平 | ... | ... |
| 開低 | ... | ... |

## 6. 資料限制聲明

- N/A 項目不做臆測；非投資建議，僅供參考。

## 附錄：機器可讀數據

```kpi
名稱|數值|單位 (每行一筆)
```
```levels
類型|價位|來源 (壓力/中軸/支撐)
```
```oidist
方向|履約價|OI (call/put 各前 10，照抄 DATA 附表)
```
```scenarios
情境|條件|操作 (與第 5 節表格同內容)
```
```

## 執行方式 (方式 1：手動)

由操作者將當日 DATA_REPORT 全文貼給分析師，取得 Daily_REPORT 全文後存入
`reports/Daily_REPORT_yyyymmdd.md`，並更新 `reports/latest.json`
(`report_date`/`report_path`/`generated_at`/`status`) 後 commit。
