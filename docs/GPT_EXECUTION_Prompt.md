# GPT_EXECUTION_Prompt.md — 分析層執行手冊 (ChatGPT 用)

> 用途：每天 08:10~08:30，由操作者將 DATA_REPORT 貼給 ChatGPT，產生 Daily_REPORT 並寫回 GitHub。
> 含重試機制。

## 步驟一：啟動 (複製以下整段到 ChatGPT)

```
你是「每日盤前分析」分析層，負責將標準化資料報告解讀為盤前分析。

規則：
1. 嚴格依照 docs/ANA_REPORT_TEMPLATE.md 的章節產出，不可增刪章節。
2. 只能使用我提供的 DATA_REPORT_yyyymmdd.md 內的數字，嚴禁虛構，缺值寫 N/A。
3. 繁體中文，800~1500字，條列優先。
4. 首行必須是 # 每日盤前分析 Daily_REPORT_yyyymmdd。
5. 結尾必須有「資料限制聲明」。

我接著會貼上 DATA_REPORT 全文，請確認理解後回覆「已就緒，請貼上 DATA_REPORT」。
```

## 步驟二：貼上資料

將 `data_reports/DATA_REPORT_yyyymmdd.md` 全文貼上。

## 步驟三：取得產出並存檔

1. 將 ChatGPT 輸出存為 `reports/Daily_REPORT_yyyymmdd.md`。
2. 更新 `reports/latest.json`：

```json
{
  "report_date": "yyyymmdd",
  "report_path": "reports/Daily_REPORT_yyyymmdd.md",
  "generated_at": "yyyy-mm-ddT08:30:00+08:00",
  "status": "completed"
}
```

`status` 對照：正常 `completed` / 部分缺料 `partial` / 休市 `holiday`。

3. Commit + Push：

```bash
git add reports/
git commit -m "feat(report): Daily_REPORT_yyyymmdd"
git push
```

## 步驟四：錯誤重試

| 錯誤 | 處理 |
|------|------|
| ChatGPT 虛構數字 | 回覆：「請檢查第X節數字，DATA_REPORT 並無此數據，請改為 N/A 並重出該節」 |
| 章節缺漏 | 回覆：「請依 ANA_REPORT_TEMPLATE 補上缺失章節，全文重出」 |
| 字數過長/過短 | 回覆：「請壓縮/擴充至 800~1500 字，重點摘要維持 3~5 條」 |
| latest.json 路徑錯 | 確認 `report_path` 與實際檔名一致，重新提交 |

最多重試 3 次，仍失敗則當日標 `partial` 並記錄原因。
