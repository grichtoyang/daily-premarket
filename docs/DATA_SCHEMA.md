# DATA_SCHEMA.md — 資料格式規範 (資料層 Rule 2/4)

版本： V2.0

## 1. 日期與時間

- 報告日期： `YYYY-MM-DD` (產出日，Asia/Taipei)；T0 交易日期： `YYYY-MM-DD`。
- 檔名： `data_reports/DATA_REPORT_yyyymmdd.md` (yyyymmdd 取自 T0，標題同)。
- 分析檔名： `reports/Daily_REPORT_yyyymmdd_日盤.md` 或 `_全日.md`
  (yyyymmdd 取自 T0；日盤版＝T0 當日 13:45 後可產，夜盤用前一夜＋即時狀態；
  全日版＝T0 次日 05:00 後可產，夜盤完整；同 T0 兩版並存不覆蓋)。
- `fetch_data.py --date YYYY-MM-DD --t0 YYYY-MM-DD`；`--t0` 缺省由 `src/t0.py` 判定。
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


## 6. 現貨借券資料契約（2026-11-03 修訂）

- margin.s_bal／margin.s_chg：融券餘額／增減（張）；不得與借券資料合併。
- sbl.bal：借券餘額（張，借入尚未返還），來源 TWSE TWT72U selectType=SLBNLB。回傳需符合 T0，並以市場別分開加總「集中市場」與「櫃檯買賣中心」個股；核對各市場「合計」列及「整體市場」列，避免把總計列再次加總。逐列檢查前日餘額＋新增借券－還券＝當日餘額。
- sbl.sale_bal／sbl.sale_chg：借券賣出餘額／增減（張，借券賣出尚未回補）。上市 TWSE TWT93U；上櫃 TPEx S47。兩來源均依日期、欄名、row 長度及餘額遞推公式驗證；只有兩市場同 T0 都有效才可稱上市櫃合計。僅部分市場成功時，來源範圍必須清楚標示，不可把部分值標成全市場值。
- TWT93U 與 TPEx S47 各自同時包含融券與借券賣出欄位；欄名可能重複。Parser 不可用固定 row index 或單純依第一個「前日餘額」定位；需以欄位群組結構辨識借券賣出欄，並檢查前日＋當日賣出－當日還券＋當日調整＝當日餘額。
- TWT96U 僅代表當日可借券賣出限額，禁止映射到 sbl.bal、sbl.sale_bal 或 sbl.sale_chg。
- 2026-10-30 live source check：TWT72U 2,072 筆個股（上市 1,237、上櫃 835），市場小計及整體合計一致；TWT93U 1,307 筆個股；TPEx S47 932 筆資料列。三個端點回傳日期皆為 2026-10-30。這只證明來源端點及 parser 的目標日驗證，不代表舊 DATA_REPORT 中既有數字已由新 parser 重建。
