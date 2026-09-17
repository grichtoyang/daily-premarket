# DATA_SCHEMA.md — 資料格式規範 (資料層 Rule 2/4)

版本： V2.0

## 1. 日期與時間

- 報告日期： `YYYY-MM-DD` (產出日，Asia/Taipei)；T0 交易日期： `YYYY-MM-DD`。
- 檔名： `data_reports/DATA_REPORT_yyyymmdd.md` (yyyymmdd 取自 T0，標題同)。
- `fetch_data.py --date YYYY-MM-DD --t0 YYYY-MM-DD`；`--t0` 缺省取 ≤ date 的最近平日。
- TPEX/部分 TWSE 端點忽略 `date` 參數回傳最新 → 程式必須驗 Date (西元 `YYYYMMDD` 或民國 `yyyMMDD`，`roc8()` 轉換)，不符標 unavailable。
- 時間一律附時區；Yahoo/期貨保留 `retrieved_at` (UTC)，不得把最新報價誤當現貨收盤。

## 2. 數值格式

| 類型 | 規範 | 範例 |
|------|------|------|
| 指數/價格 | 千分位 + 2 位 | `45,511.49` |
| 漲跌點/幅 | 附號 2 位 | `-351.03`、`+0.63` |
| 金額 (台股現貨) | 億元 1 位 | `-179.8` |
| 家數/張數 | 整數千分位 | `207`、`12,534,118` |
| 殖利率/日變化 | 2 位，變化單位百分點 | `4.97` |
| 缺值 | 一律 `unavailable` (舊 `N/A`/`TBD` 不再使用) | `unavailable` |

## 3. latest.json Schema (不變)

```json
{
  "report_date": "20260916",
  "report_path": "reports/Daily_REPORT_20260916.md",
  "generated_at": "2026-09-16T08:30:00+08:00",
  "status": "completed"
}
```

## 4. 無日期端點規則 (Proxy 主原則配套)

- 無 `date` 參數的端點 (期貨日盤價/法人交易/夜盤/選擇權法人) 一律回傳抓取當下最新盤勢，
  08:00 正式執行時即等於 T0，不另標註；盤中驗收若判定資料日期非 T0，註記「最新盤勢快照」。
- 有日期端點一律驗日期，不符標 unavailable 或採最新可得＋標示實際日期。

## 5. Markdown 規則

- UTF-8 / LF；表格必有 header separator；章節固定 (一〜五)，失敗章節寫 unavailable 不刪節。
- 與舊版差異：檔名/標題不變 (DATA_REPORT_yyyymmdd)，header 改四行式，內文改一〜五節。
