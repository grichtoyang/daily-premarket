# 每日盤前分析 Daily Pre-Market Analysis (V1.0)

三層架構：資料層 → 分析層 → 視覺層
標準化資料報告 × AI 分析解讀 × Dashboard 顯示

目標：
- 每天 08:00 (Asia/Taipei) 產生最新盤前分析
- 手機 / 電腦 隨時查看
- 單一資料來源、標準化流程、穩定可持續

## 系統架構

```
GitHub Actions (資料層)
  └─ 08:00 執行 src/fetch_data.py → data_reports/DATA_REPORT_yyyymmdd.md
        │
        ▼
ChatGPT (分析層, 手動/半自動)
  └─ 讀 DATA_REPORT → 依 ANA_TEMPLATE 產出 reports/Daily_REPORT_yyyymmdd.md + 更新 reports/latest.json
        │
        ▼
Streamlit Cloud (視覺層)
  └─ 讀 latest.json → 讀 Daily_REPORT → dashboard/app.py 顯示
```

架構圖詳見需求附件（系統架構圖 V1.0）。

## 目錄結構

```
.
├── .github/workflows/daily_data.yml  # 資料層排程 (每天 08:00 Asia/Taipei)
├── src/
│   ├── fetch_data.py                 # 資料層主程式 (V2 新規範模板)
│   ├── sources/
│   │   ├── twse.py                   # 三大法人金額 (RWD BFI82U)
│   │   ├── twse_proxy.py             # 現貨主來源 twse-proxy + MI_INDEX 備援
│   │   ├── spot_raw.py               # TWSE/TPEX raw 採集 (融資/借券/成交/漲跌)
│   │   ├── spot.py                   # 現貨正規化 (日期驗證 + unavailable)
│   │   ├── us_market.py              # Yahoo：美股/亞股/期貨/匯率/ADR/商品
│   │   ├── treasury.py               # 美債：FiscalData 主、Yahoo 備援
│   │   └── taifex.py                 # 期貨 stub (Phase 2 接 TAIFEX Proxy)
│   └── utils.py
├── docs/                             # Rules 規範
│   ├── DATA_SOURCES.md
│   ├── DATA_SCHEMA.md
│   ├── DATA_REPORT_TEMPLATE.md       # 對齊正式規範 V2.0
│   ├── AUTO_FLOW.md
│   ├── ANA_REPORT_TEMPLATE.md
│   ├── GPT_EXECUTION_Prompt.md
│   └── DASHBOARD_SPEC.md
├── data_reports/                     # 資料層產出 DATA_REPORT_yyyymmdd.md (T0)
├── reports/
│   ├── Daily_REPORT_yyyymmdd.md      # 分析層產出
│   └── latest.json                   # {report_date, report_path, generated_at, status}
├── dashboard/
│   ├── app.py
│   └── requirements.txt
└── requirements.txt
```

## 快速開始

### 1. 資料層 (本地測試)

```bash
pip install -r requirements.txt
python src/fetch_data.py --date 2026-09-16 --t0 2026-09-15
# --date 報告日期 (預設今天)；--t0 交易日期 (預設最近平日)
# 產出 data_reports/DATA_REPORT_20260915.md (檔名取自 T0)
```

### 2. 分析層

開啟 `docs/GPT_EXECUTION_Prompt.md`，複製 Prompt 到 ChatGPT，
貼上當日 `DATA_REPORT_yyyymmdd.md` 內容，取得 `Daily_REPORT_yyyymmdd.md`，
存入 `reports/` 並更新 `reports/latest.json`：

```json
{
  "report_date": "20260915",
  "report_path": "reports/Daily_REPORT_20260915.md",
  "generated_at": "2026-09-15T08:30:00+08:00",
  "status": "completed"
}
```

### 3. 視覺層

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
```

部署到 Streamlit Cloud 時，指定主檔案為 `dashboard/app.py`。

## 時間軸 (每天)

| 時間 | 動作 |
|------|------|
| 08:00 | GitHub Actions 開始執行，收集整理資料 |
| 08:00~08:10 | 產出 DATA_REPORT_yyyymmdd.md |
| 08:10~08:30 | ChatGPT 分析產生 Daily_REPORT_yyyymmdd.md |
| 08:30以後 | 寫回 GitHub 並更新 latest.json |
| 隨後 | Streamlit Cloud 偵測更新並重新部署 |
| 隨時 | 用戶 手機/電腦查看最新 Dashboard |

## 設計原則

1. 資料層只做事實收集 + 標準化，不做主觀判斷
2. 分析層只依 DATA_REPORT 內容分析，不虛構數據，缺資料標示 N/A
3. 視覺層只讀 latest.json 指向的報告，不寫入
4. 所有日期格式 yyyymmdd，時間 Asia/Taipei (UTC+8)，詳見 `docs/DATA_SCHEMA.md`
