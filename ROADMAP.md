# 未來擴充：交易策略模擬系統保留區 (本機優先)

- `strategies/` — 策略腳本 (訊號函數統一介面，待定義)
- `backtest/` — 回測引擎 (吃 `data_reports/DATA_REPORT_*.md` 歷史)
- `papertrade/` — 模擬交易 (紙上部位＋對帳)

## 資料保留規範

- `data_reports/`、`reports/` 歷史檔**永久保留不刪** (回測資料庫)。
- 每日 08:00 由 Windows 工作排程器執行 `python src/fetch_data.py` (取代 GitHub Actions)。
