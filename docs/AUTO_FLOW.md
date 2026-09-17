# AUTO_FLOW.md — 自動化流程規範 (資料層 Rule 4/4)

版本： V1.0 | 負責者： GitHub Actions

## 1. 排程

```yaml
# .github/workflows/daily_data.yml
on:
  schedule:
    - cron: '0 0 * * 1-5'   # UTC 00:00 = Asia/Taipei 08:00 (週一~週五)
  workflow_dispatch:         # 允許手動觸發
```

- 台北 08:00 執行。注意夏令/冬令不影響 (台灣無夏令，UTC+8 固定)。
- 國定假日仍執行，由程式判斷 `市場狀態：休市`。

## 2. 執行步驟

1. Checkout repo
2. Setup Python 3.11 + pip cache
3. `pip install -r requirements.txt`
4. `python src/fetch_data.py --date $(TZ=Asia/Taipei date +%F)` (`--t0` 缺省自動取最近平日；假日手動指定 `--t0`)
5. `git config user.name github-actions` / `user.email`
6. `git add data_reports/`
7. 若有變更則 commit `chore(data): DATA_REPORT_yyyymmdd` 並 push；無變更則跳過。

## 3. 重試與容錯

- 單一來源 timeout=15s，重試 3 次 (backoff 2s/4s/8s)。
- 單一來源失敗 → N/A，不 fail job。
- 全部來源失敗 → 仍產出全 N/A 報告，`市場狀態` 標示，job 標 `partial`，發 issue / log 警告但不 blocking。
- Workflow 權限： `contents: write`。

## 4. 本地驗證

```bash
pip install -r requirements.txt
python src/fetch_data.py --date 2026-09-16 --t0 2026-09-15
cat data_reports/DATA_REPORT_20260915.md
```

## 5. 成本與額度

- 全免費額度內：Actions (public repo 無限 / private 2000 min/月足夠)、無付費 API。
