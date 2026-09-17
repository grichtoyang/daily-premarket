# DASHBOARD_SPEC.md — 視覺層規範 (Streamlit Cloud)

版本： V1.0

## 1. 資料流

1. 讀 `reports/latest.json` → 取得 `report_path`、`report_date`、`generated_at`、`status`。
2. 讀 `report_path` 指向的 `reports/Daily_REPORT_yyyymmdd.md`。
3. 解析 Markdown 並顯示。若任一檔案缺失，顯示友善錯誤頁，不 crash。

## 2. 頁面結構 (dashboard/app.py)

- Header： 📈 每日盤前分析 + 報告日期 + 生成時間 + status badge (completed 綠 / partial 黃 / holiday 灰)
- Tabs：
  - Tab 1「重點摘要」：擷取 `## 1. 重點摘要` 段落 + 一句話結論高亮
  - Tab 2「完整報告」：全文 Markdown (`st.markdown`)
  - Tab 3「數據速覽」：若找得到 DATA_REPORT 對應日期 (`data_reports/DATA_REPORT_yyyymmdd.md`)，解析其表格顯示 `st.table`；找不到則顯示提示
- Sidebar：歷史報告下拉選單 (掃描 `reports/Daily_REPORT_*.md`，依檔名倒序)，切換查看；Streamlit Cloud 部署說明連結。
- 手機/電腦自適應：`layout="wide"`，表格 `use_container_width=True`。

## 3. 解析規則

- 章節擷取：以 `## ` 標題切分，找不到章節則顯示全文。
- 不在 dashboard 做任何數值計算，只做顯示。
- 所有路徑以 repo root 為基準，兼顧本地執行與 Streamlit Cloud (`Path(__file__).parent.parent`)。

## 4. 部署 (Streamlit Cloud)

1. GitHub repo 公開，主檔案 `dashboard/app.py`，Python 3.11。
2. `dashboard/requirements.txt` 僅 `streamlit>=1.33`。
3. Streamlit Cloud 設定：Repository → Branch `main` → Main file `dashboard/app.py`。
4. 當 `latest.json` 更新 push 後，Streamlit Cloud 自動偵測重啟 (約 1~2 分鐘)。

## 5. 錯誤頁

- `latest.json` 缺失/JSON 壞掉 → 顯示「尚無報告，請確認 GitHub Actions 與分析層是否完成」。
- 報告 md 缺失 → 顯示 report_path + 請檢查 commit。
