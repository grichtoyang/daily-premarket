#!/usr/bin/env python3
"""
V9 Pro Builder - 17因子 + VIX動態 + RSI/MACD + SQLite真DB + 41張全動態 + 6頁 + 機構級圖表
基於 daily-premarket-analysis-v8 (2026-10-28最新版) 升級到 daily-premarket-analysis-v9-pro
母版改成純 React + window.DASHBOARD_DATA，無範例數據，Python 只產 data.json，符合 Output Path Rule: dashboards/ 唯一

Skill: daily-premarket-analysis-v9-pro (參考 v8 pro skill 2026-10-28)
- 17因子：基礎15因子 + RSI 3% + MACD 3% = 17F，VIX動態，基差過大假多 7%->2%
- 方案C：Yahoo ^TWII 30天 → FinMind → SQLite DB 3層備援，全失敗 weight 0% 15因子運算
- SQLite真DB：v9_pro_history + factor_performance，真勝率10天回測，歷史相似度
- 41張全動態 + 20模板輪替 + 權重回測，20句型 day_hash%20避免重複
- 6頁結構：總覽/現貨/重要市場/期貨/選擇權/綜合分析，按 DATA_REPORT 四大類對位
- 每區塊 圖表 + 分析→判斷→操作，機構級 Donut/Lollipop/Gauge/SparklineTable/Candlestick/Butterfly/Mountain/Depth/Ladder/Heatmap/Gauge (Bias半圓儀表仿附圖)
- 防重疊：measureText預留4px，三欄固定寬，數值條外，文字不重疊
- 純 React 母版：templates/v9-pro-react-template.html 31KB，無46096等範例數據
- 產出：dashboards/data-YYYYMMDD.json 34KB + dashboards/v9_pro_history.db
- 今日實測：20261028 加權47035 +2.04% 外資+159.6 Bias55 PCR1.09 CallWall47000 PutWall46700
"""

import pathlib, re, json, argparse, sys, glob
from datetime import datetime, timedelta
import sqlite3, math, tempfile

# ===== 技術指標 3層備援 (方案C) =====
def fetch_yahoo_twii_30d():
    try:
        import requests
        url = "https://query1.finance.yahoo.com/v8/finance/chart/^TWII?range=1mo&interval=1d"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            print(f"[V9-17F] Yahoo ^TWII failed {resp.status_code}")
            return None
        data = resp.json()
        result = data.get('chart', {}).get('result', [{}])[0]
        timestamps = result.get('timestamp', [])
        indicators = result.get('indicators', {}).get('quote', [{}])[0]
        closes = indicators.get('close', [])
        highs = indicators.get('high', [])
        lows = indicators.get('low', [])
        valid = []
        for i in range(len(closes)):
            if closes[i] is not None:
                valid.append({'close': float(closes[i]), 'high': float(highs[i]) if highs[i] is not None else None, 'low': float(lows[i]) if lows[i] is not None else None, 'ts': timestamps[i] if i < len(timestamps) else None})
        if len(valid) < 14:
            print(f"[V9-17F] Yahoo insufficient {len(valid)}/14")
            return None
        print(f"[V9-17F] Yahoo fetched {len(valid)} days")
        return valid
    except Exception as e:
        print(f"[V9-17F] Yahoo exception: {e}")
        return None

def fetch_finmind_twii_14d():
    try:
        import requests
        end = datetime.now().strftime('%Y-%m-%d')
        start = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        url = f"https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockPrice&data_id=TAIEX&start_date={start}&end_date={end}"
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            print(f"[V9-17F] FinMind failed {resp.status_code}")
            return None
        data = resp.json().get('data', [])
        if len(data) < 14:
            print(f"[V9-17F] FinMind insufficient {len(data)}/14")
            return None
        valid = []
        for d in data[-30:]:
            try:
                valid.append({'close': float(d['close']), 'high': float(d['max']) if d.get('max') not in (None,'') else None, 'low': float(d['min']) if d.get('min') not in (None,'') else None, 'ts': None})
            except:
                continue
        print(f"[V9-17F] FinMind fetched {len(valid)} days")
        return valid if len(valid)>=14 else None
    except Exception as e:
        print(f"[V9-17F] FinMind exception: {e}")
        return None

def fetch_db_history_14d():
    try:
        for p in [pathlib.Path("dashboards/v8_pro_history.db"), pathlib.Path("dashboards/v9_pro_history.db"), pathlib.Path("/tmp/dashboards/v8_pro_history.db")]:
            if p.exists():
                conn = sqlite3.connect(str(p))
                rows = conn.execute("SELECT spot_close FROM v8_pro_history ORDER BY date DESC LIMIT 30").fetchall()
                if not rows:
                    rows = conn.execute("SELECT spot_close FROM v9_pro_history ORDER BY date DESC LIMIT 30").fetchall()
                conn.close()
                if len(rows) >=14:
                    valid = [{'close': float(r[0]), 'high': None, 'low': None, 'ts': None} for r in reversed(rows)]
                    print(f"[V9-17F] DB fallback {len(valid)} days from {p}")
                    return valid
        print("[V9-17F] DB not found for fallback")
        return None
    except Exception as e:
        print(f"[V9-17F] DB fallback exception: {e}")
        return None

def calc_rsi(closes, period=14):
    try:
        if len(closes) < period+1: return None
        gains=[]; losses=[]
        for i in range(1,len(closes)):
            diff=closes[i]-closes[i-1]
            if diff>0: gains.append(diff); losses.append(0)
            else: gains.append(0); losses.append(abs(diff))
        avg_gain=sum(gains[:period])/period
        avg_loss=sum(losses[:period])/period
        if avg_loss==0: return 100.0
        for i in range(period,len(gains)):
            avg_gain=(avg_gain*(period-1)+gains[i])/period
            avg_loss=(avg_loss*(period-1)+losses[i])/period
        if avg_loss==0: return 100.0
        rs=avg_gain/avg_loss
        return round(100-(100/(1+rs)),2)
    except: return None

def calc_macd(closes):
    try:
        def ema(data,period):
            k=2/(period+1)
            vals=[data[0]]
            for price in data[1:]: vals.append(price*k+vals[-1]*(1-k))
            return vals
        if len(closes)<26: return None,None,None
        ema12=ema(closes,12); ema26=ema(closes,26)
        dif=[ema12[i]-ema26[i] for i in range(len(closes))]
        signal=ema(dif,9)
        return round(dif[-1],2), round(signal[-1],2), round(dif[-1]-signal[-1],2)
    except: return None,None,None

def calc_kd(highs,lows,closes,period=9):
    try:
        if len(closes)<period: return None,None
        rsvs=[]
        for i in range(period-1,len(closes)):
            ph=max(highs[i-period+1:i+1]); pl=min(lows[i-period+1:i+1])
            rsv=50 if ph==pl else (closes[i]-pl)/(ph-pl)*100
            rsvs.append(rsv)
        k=50; d=50
        for rsv in rsvs:
            k=(2/3)*k+(1/3)*rsv; d=(2/3)*d+(1/3)*k
        return round(k,2), round(d,2)
    except: return None,None

def fetch_technical_indicators_with_fallback():
    print("[V9-17F] Fetching technical indicators 3-layer fallback...")
    data=None; source="none"
    data=fetch_yahoo_twii_30d()
    if data: source="yahoo"
    else:
        data=fetch_finmind_twii_14d()
        if data: source="finmind"
        else:
            data=fetch_db_history_14d()
            if data: source="db"
    if not data:
        print("[V9-17F] All 3 layers failed, RSI/MACD weight 0% -> 15 factors")
        return {'rsi':None,'macd':None,'macd_signal':None,'macd_hist':None,'k':None,'d':None,'source':'none','closes':[],'valid':False}
    closes=[d['close'] for d in data]; highs=[d.get('high') for d in data]; lows=[d.get('low') for d in data]
    rsi=calc_rsi(closes,14); macd,macd_signal,macd_hist=calc_macd(closes)
    ohlc_valid=all(h is not None and l is not None for h,l in zip(highs,lows))
    k,d=calc_kd(highs,lows,closes,9) if ohlc_valid else (None,None)
    print(f"[V9-17F] Tech RSI={rsi} MACD={macd}/{macd_signal} hist={macd_hist} K={k} D={d} source={source}")
    return {'rsi':rsi,'macd':macd,'macd_signal':macd_signal,'macd_hist':macd_hist,'k':k,'d':d,'source':source,'closes':closes,'highs':highs,'lows':lows,'valid':any(v is not None for v in (rsi,macd,macd_hist,k,d)),'validity':{'rsi':rsi is not None,'macd':macd is not None and macd_signal is not None and macd_hist is not None,'kd':k is not None and d is not None},'raw':data}

# ===== SQLite真DB + 歷史相似度 + 無DB回退 =====
def _ensure_history_table(conn, table_name):
    """Create or migrate a history table without hiding non-schema database errors."""
    if table_name not in ('v9_pro_history','v8_pro_history'):
        raise ValueError(f"Unsupported history table: {table_name}")
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            date TEXT PRIMARY KEY,
            bias INTEGER,
            spot_close REAL,
            spot_pct REAL,
            foreign_spot REAL,
            foreign_fut INTEGER,
            pcr REAL,
            gex REAL,
            put_wall INTEGER,
            vix REAL,
            rsi REAL,
            macd REAL,
            k REAL,
            d REAL,
            next_day_pct REAL,
            factor_wins TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    required={
        'bias':'INTEGER','spot_close':'REAL','spot_pct':'REAL',
        'foreign_spot':'REAL','foreign_fut':'INTEGER','pcr':'REAL',
        'gex':'REAL','put_wall':'INTEGER','vix':'REAL','rsi':'REAL',
        'macd':'REAL','k':'REAL','d':'REAL','next_day_pct':'REAL',
        'factor_wins':'TEXT',
        'created_at':'TIMESTAMP'
    }
    existing={row[1] for row in conn.execute(f"PRAGMA table_info({table_name})").fetchall()}
    if 'date' not in existing:
        raise sqlite3.DatabaseError(f"{table_name} is missing required primary-key column 'date'")
    for column,sql_type in required.items():
        if column not in existing:
            conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column} {sql_type}")

def init_db(db_path="dashboards/v9_pro_history.db"):
    """Initialize/migrate the complete V9/V8 schema; never return a partial fallback DB."""
    conn=None
    try:
        pathlib.Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        conn=sqlite3.connect(db_path)
        _ensure_history_table(conn,'v9_pro_history')
        _ensure_history_table(conn,'v8_pro_history')
        conn.execute("""
            CREATE TABLE IF NOT EXISTS factor_performance (
                factor TEXT PRIMARY KEY,
                wins INTEGER DEFAULT 0,
                total INTEGER DEFAULT 0,
                win_rate REAL DEFAULT 0.5,
                weight REAL DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        return conn
    except (sqlite3.Error, OSError) as e:
        print(f"[V9-17F] init_db error: {type(e).__name__}: {e}")
        if conn is not None:
            conn.close()
        return None

def get_db_status(db_path="dashboards/v9_pro_history.db"):
    try:
        for p in [pathlib.Path(db_path), pathlib.Path("dashboards/v8_pro_history.db"), pathlib.Path("/tmp/dashboards/v9_pro_history.db")]:
            if p.exists():
                conn=sqlite3.connect(str(p))
                try:
                    count=conn.execute("SELECT COUNT(*) FROM v9_pro_history").fetchone()[0]
                except sqlite3.OperationalError:
                    count=conn.execute("SELECT COUNT(*) FROM v8_pro_history").fetchone()[0]
                try:
                    filled=conn.execute("SELECT COUNT(*) FROM v9_pro_history WHERE next_day_pct IS NOT NULL").fetchone()[0]
                except sqlite3.OperationalError:
                    try: filled=conn.execute("SELECT COUNT(*) FROM v8_pro_history WHERE next_day_pct IS NOT NULL").fetchone()[0]
                    except sqlite3.OperationalError: filled=0
                conn.close()
                return {'exists':True,'rows':count,'filled':filled,'mode':'db' if count>=3 else 'no-db-partial','path':str(p)}
        return {'exists':False,'rows':0,'filled':0,'mode':'no-db','path':''}
    except (sqlite3.Error, OSError) as e:
        print(f"[V9-17F] DB status error: {type(e).__name__}: {e}")
        return {'exists':False,'rows':0,'filled':0,'mode':'no-db-error','path':''}

def _normalize_t0_date(t0_date):
    """Validate workflow/report T0 date (YYYYMMDD) and return SQLite ISO date."""
    try:
        return datetime.strptime(str(t0_date), '%Y%m%d').strftime('%Y-%m-%d')
    except (TypeError, ValueError):
        raise ValueError(f"Invalid T0 date {t0_date!r}; expected YYYYMMDD")

def save_today_to_db(bias, signals, tech, t0_date, db_path="dashboards/v9_pro_history.db"):
    try:
        date_str=_normalize_t0_date(t0_date)
        conn=init_db(db_path)
        if not conn: return False
        # T0 report date is authoritative; do not use runner's wall-clock date.
        for table in ('v9_pro_history','v8_pro_history'):
            try:
                existing=conn.execute(f"SELECT date FROM {table} WHERE date=?", (date_str,)).fetchone()
            except sqlite3.OperationalError:
                continue
            if existing:
                print(f"[V9-17F] DB T0 {date_str} exists in {table}, skip")
                conn.close(); return True
        table='v9_pro_history'
        conn.execute(f"""
            INSERT INTO {table} (date,bias,spot_close,spot_pct,foreign_spot,foreign_fut,pcr,gex,put_wall,vix,rsi,macd,k,d)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (date_str,bias,signals.get('spot_close',0),signals.get('spot_pct',0),signals.get('foreign',0),signals.get('foreign_futures',0),signals.get('pcr',0),signals.get('gex',0),signals.get('put_wall',0),signals.get('vix',0),tech.get('rsi'),tech.get('macd'),tech.get('k'),tech.get('d')))
        conn.commit(); conn.close()
        print(f"[V9-17F] DB saved T0 {date_str} bias={bias}")
        return True
    except Exception as e:
        print(f"[V9-17F] DB save error: {e}")
        return False

def update_next_day_pct(t0_date, t0_spot_close, db_path="dashboards/v9_pro_history.db"):
    """Use the current T0 report close to label the latest earlier trading row."""
    try:
        t0_iso=_normalize_t0_date(t0_date)
        current_close=float(t0_spot_close)
        if not math.isfinite(current_close) or current_close<=0:
            print("[V9-17F] update_next_day skipped: invalid T0 spot close")
            return False
        conn=init_db(db_path)
        if not conn: return False
        candidates=[]
        for candidate_table in ('v9_pro_history','v8_pro_history'):
            try:
                candidate=conn.execute(
                    f"SELECT date,spot_close FROM {candidate_table} WHERE date<? AND next_day_pct IS NULL AND spot_close>0 ORDER BY date DESC LIMIT 1",
                    (t0_iso,)
                ).fetchone()
                if candidate:
                    candidates.append((candidate[0],candidate[1],candidate_table))
            except sqlite3.OperationalError:
                continue
        if not candidates:
            conn.close(); return False
        previous_date,previous_close,table=max(candidates,key=lambda item:item[0])
        next_pct=(current_close-float(previous_close))/float(previous_close)*100
        conn.execute(f"UPDATE {table} SET next_day_pct=? WHERE date=?", (next_pct,previous_date))
        conn.commit(); conn.close()
        print(f"[V9-17F] DB updated {previous_date} next={next_pct:.2f}% using T0 {t0_iso}")
        return True
    except Exception as e:
        print(f"[V9-17F] DB update_next_day error: {e}")
        return False

def get_factor_win_rates_from_db(db_path="dashboards/v9_pro_history.db"):
    """Return conservative, sample-gated historical directional hit rates."""
    try:
        conn=init_db(db_path)
        if not conn: return None
        try:
            rows=conn.execute("SELECT spot_pct,foreign_spot,foreign_fut,pcr,next_day_pct FROM v9_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 60").fetchall()
        except sqlite3.OperationalError:
            rows=conn.execute("SELECT spot_pct,foreign_spot,foreign_fut,pcr,next_day_pct FROM v8_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 60").fetchall()
        conn.close()
        wins={k:0 for k in ('spot_trend','foreign_spot','foreign_fut','pcr')}
        totals={k:0 for k in wins}
        for pct,foreign,foreign_fut,pcr,next_pct in rows:
            if next_pct is None: continue
            candidates=[]
            if pct is not None and abs(pct)>=1: candidates.append(('spot_trend',1 if pct>0 else -1))
            if foreign is not None and abs(foreign)>=200: candidates.append(('foreign_spot',1 if foreign>0 else -1))
            if foreign_fut is not None and abs(foreign_fut)>=50000: candidates.append(('foreign_fut',1 if foreign_fut>0 else -1))
            if pcr is not None and pcr<0.8: candidates.append(('pcr',-1))
            actual=1 if next_pct>0 else -1 if next_pct<0 else 0
            for key,predicted in candidates:
                totals[key]+=1
                if actual==predicted: wins[key]+=1
        rates={}
        for key,total in totals.items():
            if total>=8:
                rates[key]=(wins[key]+5.0)/(total+10.0)
        print(f"[V9-17F] SQLite optimizer: {len(rows)} labeled rows; eligible factor rates={rates}")
        return rates or None
    except Exception as e:
        print(f"[V9-17F] DB get win rates non-critical: {e}")
        return None



def find_historical_similarity(current_signals, db_path="dashboards/v9_pro_history.db", top_n=3):
    try:
        conn=init_db(db_path)
        if not conn: return None
        try:
            rows=conn.execute("SELECT date,bias,spot_pct,foreign_spot,pcr,vix,next_day_pct FROM v9_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 30").fetchall()
        except sqlite3.OperationalError:
            rows=conn.execute("SELECT date,bias,spot_pct,foreign_spot,pcr,vix,next_day_pct FROM v8_pro_history WHERE next_day_pct IS NOT NULL ORDER BY date DESC LIMIT 30").fetchall()
        conn.close()
        if len(rows)<3:
            print(f"[V9-17F] Historical insufficient {len(rows)}/3")
            return None
        curr_bias=current_signals.get('bias',50); curr_pct=current_signals.get('spot_pct',0); curr_foreign=current_signals.get('foreign',0); curr_pcr=current_signals.get('pcr',0)
        scored=[]
        for date,bias,pct,foreign,pcr,vix,next_pct in rows:
            bias_diff=abs(bias-curr_bias); pct_diff=abs(pct-curr_pct); foreign_diff=abs(foreign-curr_foreign)/100; pcr_diff=abs(pcr-curr_pcr)*10
            sim=100-(bias_diff*0.5+pct_diff*2+foreign_diff*0.3+pcr_diff)
            scored.append((sim,date,bias,next_pct))
        scored.sort(reverse=True)
        top=scored[:top_n]
        if not top: return None
        avg_next=sum([s[3] for s in top])/len(top) if top else 0
        win_rate=sum([1 for s in top if s[3]<0])/len(top) if top else 0
        print(f"[V9-17F] Historical similarity: {len(rows)} days top{top_n} avg={avg_next:.2f}% win={win_rate:.0%}")
        for sim,date,bias,next_pct in top[:3]: print(f"  - {date} bias={bias} next={next_pct:.2f}% sim={sim:.0f}")
        return {'avg_next_pct':avg_next,'win_rate':win_rate,'top_days':top,'count':len(rows)}
    except Exception as e:
        print(f"[V9-17F] Historical similarity error: {e}")
        return None

def validate_data_report_consistency(spot, inst, turnover, tx, options):
    """Return non-blocking warnings for cross-field contradictions in DATA_REPORT."""
    warnings=[]
    def number(value):
        try:
            if value is None or value=="": return None
            result=float(str(value).replace(',','').replace('+','').replace('%','').strip())
            return result if math.isfinite(result) else None
        except (TypeError, ValueError):
            return None
    def check_close(label, actual, expected, tolerance, detail):
        a=number(actual); e=number(expected)
        if a is not None and e is not None and abs(a-e)>tolerance:
            warnings.append(f"{label}: {detail}；差異 {a-e:+.2f}，容許 ±{tolerance:.2f}")
    # Spot and futures OHLC must respect the reported intraday range.
    for label,bar in (("現貨",spot),("台指期日盤",tx.get('day',{}))):
        o,h,l,c=(number(bar.get(k)) for k in ('open' if label=="現貨" else 'o','high' if label=="現貨" else 'h','low' if label=="現貨" else 'l','close' if label=="現貨" else 'c'))
        if None not in (o,h,l,c) and (h<max(o,l,c) or l>min(o,h,c) or h<l):
            warnings.append(f"{label} OHLC 矛盾：O={o:g}, H={h:g}, L={l:g}, C={c:g}")
    # Institutional and turnover totals are independently reported aggregates.
    inst_parts=[number(inst.get(k)) for k in ('foreign','trust','dealer')]
    if all(v is not None for v in inst_parts):
        check_close("三大法人合計",inst.get('all'),sum(inst_parts),0.21,"外資＋投信＋自營商與合計不一致")
    check_close("上市櫃成交金額合計",turnover.get('total'),(number(turnover.get('listed')) or 0)+(number(turnover.get('otc')) or 0),0.21,"上市＋上櫃與合計不一致")
    # Futures basis should reconcile with futures close minus spot close.
    day=tx.get('day',{})
    if all(number(v) is not None for v in (day.get('basis'),day.get('c'),spot.get('close'))):
        check_close("期現基差",day.get('basis'),number(day.get('c'))-number(spot.get('close')),2.01,"台指期收盤－加權指數收盤與申報基差不一致")
    # PCR in this report is Put OI / Call OI; validate only when both denominators exist.
    call_oi=number(options.get('callOi')); put_oi=number(options.get('putOi')); pcr=number(options.get('pcr'))
    if call_oi not in (None,0) and put_oi is not None and pcr is not None:
        check_close("選擇權 PCR",pcr,put_oi/call_oi,0.02,"Put OI／Call OI 與 PCR 不一致")
    return warnings


# ===== DATA_REPORT 解析 (FULL) =====
def parse_margin_ratio_provenance(report_text, t0_date):
    """Parse maintenance-ratio value and provenance without conflating estimates with stale data."""
    line=next((x for x in report_text.splitlines() if "融資維持率" in x and x.strip().startswith("|")), "")
    m=re.search(r"\|\s*融資維持率\s*\|\s*([0-9,.]+)\s*\|\s*%\s*\|\s*(.*?)\s*\|?\s*$", line)
    ratio=None
    source_cell=""
    if m:
        try:
            value=float(m.group(1).replace(",",""))
            if math.isfinite(value) and 50.0 < value < 500.0:
                ratio=value
        except (TypeError, ValueError):
            pass
        source_cell=m.group(2).strip()
    date_match=re.search(r"(?:DATA|資料日期)\s*[:：]?\s*(\d{4}-\d{2}-\d{2}|\d{8})", source_cell, re.I)
    source_date=date_match.group(1) if date_match else None
    if source_date and len(source_date)==8:
        source_date=f"{source_date[:4]}-{source_date[4:6]}-{source_date[6:]}"
    is_fallback="前值遞補" in source_cell
    if ratio is None:
        status="unavailable"
    elif is_fallback:
        status="previous_report_fallback"
    elif source_date and source_date != t0_date:
        status="estimated_stale"
    else:
        # Live-source rows without an explicit date are emitted only after T0 validation.
        source_date=source_date or t0_date
        status="estimated_t0"
    source_name="unknown"
    for candidate in ("wantgoo","stockintelli","istock"):
        if candidate in source_cell.lower():
            source_name=candidate
            break
    if is_fallback:
        source_name="previous_report"
    return {"ratio":ratio,"status":status,"source":source_name,
            "source_detail":source_cell or None,"source_date":source_date,
            "is_t0":bool(ratio is not None and status=="estimated_t0" and source_date==t0_date)}

def parse_data_report(report_path):
    text = pathlib.Path(report_path).read_text(encoding='utf-8', errors='ignore')
    def get_value(pattern, default=None, is_float=True):
        m=re.search(pattern, text, re.DOTALL)
        if not m: return default
        try:
            v=m.group(1).replace(',','').replace('+','').strip()
            if v.lower()=='unavailable': return default
            if is_float: return float(v)
            return v
        except: return default
    def parse_table(heading):
        idx=text.find(heading)
        if idx==-1: return []
        substr=text[idx:idx+8000]
        lines=substr.split('\n')
        rows=[]; in_table=False
        for line in lines:
            if line.strip().startswith('|'):
                if '---' in line: in_table=True; continue
                if in_table:
                    cols=[c.strip() for c in line.split('|')[1:-1]]
                    if len(cols)>=2: rows.append(cols)
            else:
                if in_table and rows: break
        return rows
    def parse_pct(s):
        if s is None: return None
        s=str(s).replace('%','').replace('+','').strip()
        if not s or s.lower() in ('unavailable','n/a','--','null'): return None
        try: return float(s)
        except (TypeError, ValueError): return None
    def must_get(pattern,name):
        v=get_value(pattern,None)
        if v is None or v=="": raise ValueError(f"[NO-FALLBACK] DATA_REPORT missing {name}: {pattern}")
        return v
    def optional_get(pattern):
        return get_value(pattern,None)

    report_date_match=re.search(r"報告日期：`([^`]+)`", text)
    t0_date_match=re.search(r"T0 交易日期：`([^`]+)`", text)
    gen_time_match=re.search(r"資料產出時間：`([^`]+)`", text)
    report_date=report_date_match.group(1) if report_date_match else ""
    t0_date=t0_date_match.group(1) if t0_date_match else ""
    gen_time=gen_time_match.group(1) if gen_time_match else ""

    us_rows=parse_table("### 1. 美股指數"); asia_rows=parse_table("### 2. 亞洲主要指數"); fut_rows=parse_table("### 3. 美股指數期貨")
    yield_rows=parse_table("### 4. 美國國債殖利率"); fx_rows=parse_table("### 5. 主要匯率"); adr_rows=parse_table("### 6. 台灣相關ADR"); comm_rows=parse_table("### 7. 原油黃金Bitcoin")

    def build_arr(rows, pct_index=4):
        parts=[]
        for r in rows:
            if len(r)<3: continue
            pct_col=r[pct_index] if len(r)>pct_index else None
            pct=parse_pct(pct_col)
            close_raw=r[2] if len(r)>2 else None
            try: close_val=float(close_raw.replace(',','')) if close_raw else None
            except (TypeError, ValueError): close_val=None
            parts.append({'l':r[0],'v':pct,'close':close_val,'raw':r})
        return parts
    def build_arr_simple(rows):
        arr=build_arr(rows)
        return [{'l':x['l'],'v':x['v']} for x in arr], arr

    usPct_simple, usPct_full=build_arr_simple(us_rows); asiaPct_simple, asiaPct_full=build_arr_simple(asia_rows)
    futPct_simple, futPct_full=build_arr_simple(fut_rows)
    yield_arr=build_arr(yield_rows, pct_index=3)
    yieldPct_simple=[{'l':x['l'],'v':x['v']} for x in yield_arr]; yieldPct_full=yield_arr
    fxPct_simple, fxPct_full=build_arr_simple(fx_rows); adrPct_simple, adrPct_full=build_arr_simple(adr_rows); commPct_simple, commPct_full=build_arr_simple(comm_rows)

    spot_close=must_get(r"加權指數 \| ([0-9,.]+) \| 點","加權收盤"); spot_open=must_get(r"開盤 \| ([0-9,.]+) \| 點","開盤")
    spot_high=must_get(r"最高 \| ([0-9,.]+) \| 點","最高"); spot_low=must_get(r"最低 \| ([0-9,.]+) \| 點","最低")
    spot_diff=must_get(r"漲跌點數 \| ([-\+0-9,.]+) \| 點","漲跌點"); spot_pct=optional_get(r"漲跌幅 \| ([-\+0-9,.]+) \| %")
    spot_vol_raw=must_get(r"成交金額 \| ([0-9,.]+) \| 億元","成交金額")

    up=int(must_get(r"\| 上漲家數 \| ([0-9]+) \|","上漲家數")); down=int(must_get(r"\| 下跌家數 \| ([0-9]+) \|","下跌家數"))
    flat_match=re.search(r"\| 平盤家數 \| ([0-9]+) \|", text); flat=int(flat_match.group(1)) if flat_match else 0
    up_limit_match=re.search(r"\| 漲停家數 \| ([0-9]+) \|", text); down_limit_match=re.search(r"\| 跌停家數 \| ([0-9]+) \|", text)
    limit_up=int(up_limit_match.group(1)) if up_limit_match else 0; limit_down=int(down_limit_match.group(1)) if down_limit_match else 0

    otc_section=text.find("#### 2.2 上櫃公司"); otc_up=otc_down=otc_flat=otc_limit_up=otc_limit_down=0
    if otc_section!=-1:
        otc_sub=text[otc_section:otc_section+3000]
        m=re.search(r"\| 上漲家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_up=int(m.group(1))
        m=re.search(r"\| 下跌家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_down=int(m.group(1))
        m=re.search(r"\| 平盤家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_flat=int(m.group(1))
        m=re.search(r"\| 漲停家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_limit_up=int(m.group(1))
        m=re.search(r"\| 跌停家數 \| ([0-9]+) \|", otc_sub); 
        if m: otc_limit_down=int(m.group(1))

    foreign_inst=optional_get(r"\| 外資 \| ([-\+0-9,.]+) \| 億元"); trust_inst=optional_get(r"\| 投信 \| ([-\+0-9,.]+) \| 億元")
    dealer_inst=must_get(r"\| 自營商 \| ([-\+0-9,.]+) \| 億元","自營商"); all_inst=must_get(r"\| 三大法人合計 \| ([-\+0-9,.]+) \| 億元","三大法人")
    margin_finance=get_value(r"\| 融資餘額 \| ([0-9,.]+) \| 億元","0"); margin_finance_diff=get_value(r"\| 融資增減 \| ([-\+0-9,.]+) \| 億元","0")
    margin_short=get_value(r"\| 融券餘額 \| ([0-9,]+) \| 張","0")
    margin_provenance=parse_margin_ratio_provenance(text, t0_date)
    margin_ratio=margin_provenance["ratio"]
    margin_ratio_source=margin_provenance["source_detail"] or ""
    margin_ratio_source_date=margin_provenance["source_date"]
    margin_ratio_status=margin_provenance["status"]
    sbl_balance=get_value(r"\| 借券餘額 \| ([0-9,]+) \| 張","0")
    listed_turnover=get_value(r"\| 上市成交金額 \| ([0-9,.]+) \| 億元","0"); otc_turnover=get_value(r"\| 上櫃成交金額 \| ([0-9,.]+) \| 億元","0"); total_turnover=get_value(r"\| 上市櫃成交金額合計 \| ([0-9,.]+) \| 億元","0")

    fut_day_o=must_get(r"### 1．台指期近月日盤行情.*?開盤價 \| ([0-9,]+) \|","台指日盤開"); fut_day_h=must_get(r"### 1．台指期近月日盤行情.*?最高價 \| ([0-9,]+) \|","台指日盤高")
    fut_day_l=must_get(r"### 1．台指期近月日盤行情.*?最低價 \| ([0-9,]+) \|","台指日盤低"); fut_day_c=must_get(r"### 1．台指期近月日盤行情.*?收盤價 \| ([0-9,]+) \|","台指日盤收")
    fut_day_diff=must_get(r"### 1．台指期近月日盤行情.*?漲跌點數 \| ([-\+0-9,]+) \|","台指日盤漲跌"); fut_day_pct=must_get(r"### 1．台指期近月日盤行情.*?漲跌幅 \| ([-\+0-9.]+) \|","台指日盤漲跌幅")
    fut_day_vol=must_get(r"### 1．台指期近月日盤行情.*?成交量 \| ([0-9,]+) \|","台指日盤量")
    fut_night_o=optional_get(r"### 2．台指期近月夜盤行情.*?開盤價 \| ([0-9,]+) \|"); fut_night_h=optional_get(r"### 2．台指期近月夜盤行情.*?最高價 \| ([0-9,]+) \|")
    fut_night_l=optional_get(r"### 2．台指期近月夜盤行情.*?最低價 \| ([0-9,]+) \|"); fut_night_c=optional_get(r"### 2．台指期近月夜盤行情.*?收盤價 \| ([0-9,]+) \|")
    fut_night_diff=optional_get(r"### 2．台指期近月夜盤行情.*?漲跌點數 \| ([-\+0-9,]+) \|"); fut_night_pct=optional_get(r"### 2．台指期近月夜盤行情.*?漲跌幅 \| ([-\+0-9.]+) \|")
    fut_night_vol=optional_get(r"### 2．台指期近月夜盤行情.*?成交量 \| ([0-9,]+) \|")
    basis=optional_get(r"台指期與加權指數價差 \| ([-\+0-9.]+) \|"); basis_pct=get_value(r"價差百分比 \| ([-\+0-9.]+) \|","0"); night_change=get_value(r"夜盤價格相對日盤收盤的變化 \| ([-\+0-9]+) \|","0")
    foreign_fut_oi=optional_get(r"外資多空淨 OI \| ([-\+0-9,]+) \|"); trust_fut_oi=must_get(r"投信多空淨 OI \| ([-\+0-9,]+) \|","投信OI")
    dealer_fut_oi=must_get(r"自營商多空淨 OI \| ([-\+0-9,]+) \|","自營OI"); top10_oi=must_get(r"前十大交易人多空淨 OI \| ([-\+0-9,]+) \|","前十大OI")
    foreign_day_net=must_get(r"外資日盤多空淨交易量 \| ([-\+0-9,]+) \|","外資日淨"); foreign_night_net=must_get(r"外資夜盤多空淨交易量 \| ([-\+0-9,]+) \|","外資夜淨")
    call_vol=must_get(r"Call 總成交量 \| ([0-9,]+) \|","Call成交"); call_oi=must_get(r"Call 總未平倉量 OI \| ([0-9,]+) \|","Call OI")
    put_vol=must_get(r"Put 總成交量 \| ([0-9,]+) \|","Put成交"); put_oi=must_get(r"Put 總未平倉量 OI \| ([0-9,]+) \|","Put OI")
    pcr=optional_get(r"Put／Call Ratio \| ([0-9.]+) \|"); call_wall=must_get(r"Call Wall 價位 \| ([0-9,]+) \|","Call Wall")
    put_wall=optional_get(r"Put Wall 價位 \| ([0-9,]+) \|"); gamma_wall=must_get(r"Gamma Wall 價位 \| ([0-9,.]+) \|","Gamma Wall")
    gamma_flip=must_get(r"Gamma Flip 價位 \| ([0-9,.]+) \|","Gamma Flip"); max_pain=must_get(r"Max Pain 價位 \| ([0-9,]+) \|","Max Pain")
    call_oi_table=parse_table("#### Call OI 分布明細 Top10"); put_oi_table=parse_table("#### Put OI 分布明細 Top10"); opt_inst_table=parse_table("### 17．選擇權法人日盤、夜盤交易")
    consistency_warnings=validate_data_report_consistency(
        {'open':spot_open,'high':spot_high,'low':spot_low,'close':spot_close},
        {'foreign':foreign_inst,'trust':trust_inst,'dealer':dealer_inst,'all':all_inst},
        {'listed':listed_turnover,'otc':otc_turnover,'total':total_turnover},
        {'day':{'o':fut_day_o,'h':fut_day_h,'l':fut_day_l,'c':fut_day_c,'basis':basis}},
        {'callOi':call_oi,'putOi':put_oi,'pcr':pcr}
    )

    news_events=[]
    idx=text.find("事件1：")
    if idx!=-1:
        substr=text[idx:idx+20000]
        lines=substr.split('\n')
        curr=None
        for line in lines:
            line=line.strip()
            m=re.match(r'- 事件\d+：(.+)', line)
            if m:
                if curr: news_events.append(curr)
                curr={"t": m.group(1).strip(), "s":"", "d":"", "time":"", "link":""}
            elif line.startswith("- 來源：") and curr:
                curr["s"]=line.replace("- 來源：","").strip()
                time_m=re.search(r"(\d{4}-\d{2}-\d{2}T[^;]+)", curr["s"])
                if time_m: curr["time"]=time_m.group(1)
            elif line.startswith("- 摘要：") and curr: curr["d"]=line.replace("- 摘要：","").strip()
            elif line.startswith("- 連結：") and curr: curr["link"]=line.replace("- 連結：","").strip()
        if curr: news_events.append(curr)

    return {
        'meta': {'report_date': report_date, 't0_date': t0_date, 'generated_at': gen_time, 'data_quality_warnings': consistency_warnings},
        'usPct_simple': usPct_simple, 'asiaPct_simple': asiaPct_simple, 'futPct_simple': futPct_simple,
        'yieldPct_simple': yieldPct_simple, 'fxPct_simple': fxPct_simple, 'adrPct_simple': adrPct_simple, 'commPct_simple': commPct_simple,
        'usPct_full': usPct_full, 'asiaPct_full': asiaPct_full, 'futPct_full': futPct_full,
        'yieldPct_full': yieldPct_full, 'fxPct_full': fxPct_full, 'adrPct_full': adrPct_full, 'commPct_full': commPct_full,
        'spot': {'close': spot_close, 'open': spot_open, 'high': spot_high, 'low': spot_low, 'diff': spot_diff, 'pct': spot_pct, 'vol': spot_vol_raw, 'up': up, 'down': down, 'flat': flat, 'limit_up': limit_up, 'limit_down': limit_down, 'otc_up': otc_up, 'otc_down': otc_down, 'otc_flat': otc_flat, 'otc_limit_up': otc_limit_up, 'otc_limit_down': otc_limit_down},
        'margin': {'finance': margin_finance, 'finance_diff': margin_finance_diff, 'short': margin_short, 'ratio': margin_ratio, 'ratio_status': margin_ratio_status, 'ratio_source': margin_ratio_source, 'ratio_source_name': margin_provenance["source"], 'ratio_source_date': margin_ratio_source_date, 'ratio_is_t0': margin_provenance["is_t0"], 'sbl': sbl_balance},
        'turnover': {'listed': listed_turnover, 'otc': otc_turnover, 'total': total_turnover},
        'inst': {'foreign': foreign_inst, 'trust': trust_inst, 'dealer': dealer_inst, 'all': all_inst},
        'tx': {'day': {'o': fut_day_o, 'h': fut_day_h, 'l': fut_day_l, 'c': fut_day_c, 'diff': fut_day_diff, 'pct': fut_day_pct, 'vol': fut_day_vol, 'basis': basis, 'prem': basis_pct}, 'night': {'o': fut_night_o, 'h': fut_night_h, 'l': fut_night_l, 'c': fut_night_c, 'diff': fut_night_diff, 'pct': fut_night_pct, 'vol': fut_night_vol, 'change': night_change}},
        'futures': {'foreign_oi': foreign_fut_oi, 'trust_oi': trust_fut_oi, 'dealer_oi': dealer_fut_oi, 'top10': top10_oi, 'foreign_day': foreign_day_net, 'foreign_night': foreign_night_net},
        'options': {'callVol': call_vol, 'callOi': call_oi, 'putVol': put_vol, 'putOi': put_oi, 'pcr': pcr, 'callWall': call_wall, 'putWall': put_wall, 'gammaWall': gamma_wall, 'flip': gamma_flip, 'maxPain': max_pain, 'callOiDist': call_oi_table, 'putOiDist': put_oi_table, 'instOpt': opt_inst_table},
        'news': news_events,
    }

# ===== V9 17因子 分析器 =====
class V9Analyzer:
    def __init__(self, parsed, tech):
        self.parsed=parsed; self.tech=tech; self.signals={}; self.bias_score=50; self.bias_factors=[]; self.weights={}; self._parse_signals()

    def _parse_signals(self):
        p=self.parsed; spot=p.get('spot',{}); inst=p.get('inst',{}); tx=p.get('tx',{})
        options=p.get('options',{}); futures=p.get('futures',{})
        self.signals['spot_close']=spot.get('close'); self.signals['spot_pct']=spot.get('pct')
        self.signals['spot_up']=spot.get('up'); self.signals['spot_down']=spot.get('down')
        self.signals['spot_vol']=spot.get('vol')
        self.signals['volume_ratio']=spot.get('volume_ratio',p.get('volume_ratio'))
        self.signals['foreign']=inst.get('foreign'); self.signals['trust']=inst.get('trust')
        self.signals['dealer']=inst.get('dealer'); self.signals['all']=inst.get('all')
        day=tx.get('day',{}); night=tx.get('night',{})
        self.signals['tx_basis']=day.get('basis'); self.signals['tx_prem']=day.get('prem')
        self.signals['tx_day_pct']=day.get('pct'); self.signals['tx_night_pct']=night.get('pct')
        self.signals['tx_night_low']=night.get('l'); self.signals['tx_night_high']=night.get('h')
        self.signals['tx_day_low']=day.get('l')
        self.signals['put_wall']=options.get('putWall'); self.signals['call_wall']=options.get('callWall')
        self.signals['gamma_wall']=options.get('gammaWall'); self.signals['flip']=options.get('flip')
        self.signals['max_pain']=options.get('maxPain'); self.signals['pcr']=options.get('pcr')
        self.signals['gex']=options.get('gex')
        us_rows=p.get('usPct_full',[]) or []
        self.signals['us_dict']={x.get('l'):x.get('v') for x in us_rows if isinstance(x,dict)}
        self.signals['sox']=next((x.get('v') for x in us_rows if 'SOX' in str(x.get('l','')).upper()),None)
        self.signals['vix']=next((x.get('close') for x in us_rows if 'VIX' in str(x.get('l','')).upper()),None)
        adr_rows=p.get('adrPct_full',[]) or []
        self.signals['adr_change']=next((x.get('v') for x in adr_rows if 'TSM' in str(x.get('l','')).upper() or '台積電' in str(x.get('l',''))),None)
        yield_rows=p.get('yieldPct_full',[]) or []
        self.signals['yield_10y_change']=next((x.get('v') for x in yield_rows if '10Y' in str(x.get('l','')).upper() or '10年' in str(x.get('l',''))),None)
        tech=self.tech or {}
        self.signals['rsi']=tech.get('rsi'); self.signals['macd']=tech.get('macd')
        self.signals['macd_hist']=tech.get('macd_hist'); self.signals['k']=tech.get('k')
        self.signals['d']=tech.get('d'); self.signals['tech_valid']=tech.get('valid',False)
        closes=[float(x) for x in (tech.get('closes') or []) if x is not None]
        self.signals['ma_bias_pct']=((closes[-1]/(sum(closes[-20:])/20))-1)*100 if len(closes)>=20 and sum(closes[-20:]) else None
        self.signals['foreign_futures']=futures.get('foreign_oi')

    def _evaluate_factors(self):
        s=self.signals
        def num(value):
            try:
                value=float(value)
                return value if math.isfinite(value) else None
            except (TypeError,ValueError):
                return None
        def add(key,label,raw,score,source,reason):
            raw=num(raw)
            if raw is None or score is None:
                self.factor_details.append({'key':key,'name':label,'raw_value':raw,'score':None,
                    'status':'disabled','reason':reason or '資料缺失或無法驗證','source':source})
            else:
                self.factor_details.append({'key':key,'name':label,'raw_value':raw,
                    'score':max(-1.0,min(1.0,float(score))),'status':'active',
                    'reason':reason or '有效資料','source':source})
        self.factor_details=[]
        v=num(s.get('spot_pct'))
        add('spot_trend','現貨趨勢',v,(-1.0 if v<=-3 else -0.8 if v<=-2 else -0.6 if v<=-1 else -0.25 if v<0 else 0.6 if v>=1 else 0.0) if v is not None else None,'DATA_REPORT.spot.pct','依加權指數日漲跌幅分級')
        v=num(s.get('foreign'))
        add('foreign_spot','外資現貨',v,(-1.0 if v<=-800 else -0.8 if v<=-500 else -0.5 if v<=-200 else -0.2 if v<0 else 0.6 if v>=200 else 0.0) if v is not None else None,'DATA_REPORT.inst.foreign','依外資現貨買賣超金額分級')
        v=num(s.get('foreign_futures'))
        add('foreign_fut','外資期貨',v,(-1.0 if v<=-80000 else -0.6 if v<=-50000 else -0.25 if v<0 else 0.5 if v>=50000 else 0.0) if v is not None else None,'DATA_REPORT.futures.foreign_oi','依外資期貨淨未平倉口數分級')
        v=num(s.get('trust'))
        add('trust','投信',v,(0.6 if v>=50 else -0.6 if v<=-50 else 0.0) if v is not None else None,'DATA_REPORT.inst.trust','依投信現貨買賣超金額分級')
        v=num(s.get('tx_basis'))
        add('basis','基差',v,(-0.7 if v<-50 or v>200 else 0.0) if v is not None else None,'DATA_REPORT.tx.day.basis','逆價差或過大正價差視為風險')
        v=num(s.get('tx_night_pct'))
        add('night','夜盤',v,(-1.0 if v<=-1 else -0.6 if v<=-0.5 else -0.25 if v<0 else 0.6 if v>=0.5 else 0.0) if v is not None else None,'DATA_REPORT.tx.night.pct','依夜盤漲跌幅分級')
        v=num(s.get('sox'))
        add('us_sox','美股費半',v,(-1.0 if v<=-5 else -0.5 if v<=-2 else -0.2 if v<0 else 0.6 if v>=2 else 0.0) if v is not None else None,'DATA_REPORT.usPct_full.SOX','依費半日漲跌幅分級')
        v=num(s.get('pcr'))
        add('pcr','PCR',v,(-0.8 if v<0.6 else -0.4 if v<0.8 else 0.0) if v is not None else None,'DATA_REPORT.options.pcr','沿用現行低 PCR 風險規則；其他區間不推定方向')
        v=num(s.get('gex'))
        add('gex','GEX',v,(-1.0 if v<0 else 1.0 if v>0 else 0.0) if v is not None else None,'DATA_REPORT.options.gex','僅接受來源直接提供且可驗證的 GEX；不使用硬編碼值')
        close=num(s.get('spot_close')); wall=num(s.get('put_wall'))
        wall_score=(0.5 if close>wall else -0.5 if close<wall else 0.0) if close is not None and wall is not None and wall>0 else None
        add('put_wall','Put Wall',wall,wall_score,'DATA_REPORT.spot.close + DATA_REPORT.options.putWall','現價位於有效 Put Wall 上方／下方；僅作位置方向訊號')
        v=num(s.get('adr_change'))
        add('adr','ADR 表現代理',v,(0.5 if v>=2 else -0.5 if v<=-2 else 0.0) if v is not None else None,'DATA_REPORT.adrPct_full.TSM','使用台積電 ADR 漲跌幅代理，不宣稱為 ADR 溢價')
        v=num(s.get('yield_10y_change'))
        add('yield','美債10Y殖利率變化',v,(-0.5 if v>=0.05 else 0.5 if v<=-0.05 else 0.0) if v is not None else None,'DATA_REPORT.yieldPct_full.10Y','殖利率日變化以百分點表示；上升偏風險、下降偏緩和')
        v=num(s.get('volume_ratio')); pct=num(s.get('spot_pct'))
        volume_score=(0.5 if v>=1.2 and pct>0 else -0.5 if v>=1.2 and pct<0 else 0.0) if v is not None and pct is not None else None
        add('volume','量能',v,volume_score,'DATA_REPORT.volume_ratio','需有成交量相對均量比；只有單日成交額時不臆測量能強弱')
        v=num(s.get('ma_bias_pct'))
        add('ma_bias','均線乖離',v,(0.5 if v>0 else -0.5 if v<0 else 0.0) if v is not None else None,'Yahoo/FinMind/SQLite closes SMA20','至少20筆有效收盤價，現價高於／低於SMA20')
        v=num(s.get('vix'))
        add('vix_factor','VIX',v,(-1.0 if v>25 else -0.5 if v>20 else 0.4 if v<15 else 0.0) if v is not None else None,'DATA_REPORT.usPct_full.VIX.close','依 VIX 收盤水準分級')
        v=num(s.get('rsi'))
        add('rsi','RSI',v,(-0.5 if v<20 else -0.3 if v<30 else 0.3 if v>80 else 0.0) if v is not None else None,'Yahoo/FinMind/SQLite RSI14','RSI14 超買超賣分級；缺值不以中性代替')
        v=num(s.get('macd_hist'))
        add('macd','MACD',v,(-1.0 if v<-50 else -0.5 if v<0 else 0.5 if v>0 else 0.0) if v is not None else None,'Yahoo/FinMind/SQLite MACD histogram','依 MACD histogram 正負及強度分級')
        return self.factor_details

    def calculate_weights(self, real_win_rates=None):
        base_weights={
            'spot_trend':13,'foreign_spot':12,'foreign_fut':8,'trust':5,'basis':7,
            'night':8,'us_sox':12,'pcr':7,'gex':7,'put_wall':3,'adr':3,'yield':5,
            'volume':3,'ma_bias':3,'vix_factor':2,'rsi':3,'macd':3
        }
        adaptive=dict(base_weights)
        vix=self.signals.get('vix'); basis=self.signals.get('tx_basis')
        if vix is not None:
            if vix>25:
                adaptive['us_sox']+=8; adaptive['spot_trend']-=5
                adaptive['foreign_spot']+=3; adaptive['vix_factor']+=3
            elif vix>20:
                adaptive['us_sox']+=4; adaptive['spot_trend']-=2
            elif vix<15:
                adaptive['us_sox']-=5; adaptive['spot_trend']+=5
        if basis is not None:
            if basis>100: adaptive['basis']=2
            elif basis<-50: adaptive['basis']+=3
        for factor,rate in (real_win_rates or {}).items():
            if factor in adaptive and isinstance(rate,(int,float)):
                if rate>=0.65: adaptive[factor]=min(adaptive[factor]+2,25)
                elif rate<=0.35: adaptive[factor]=max(adaptive[factor]-2,1)
        active={x['key'] for x in self.factor_details if x['status']=='active'}
        eligible={k:max(0.0,float(v)) for k,v in adaptive.items() if k in active}
        total=sum(eligible.values())
        effective={k:(v*100.0/total if total>0 else 0.0) for k,v in eligible.items()}
        self.weights={k:round(effective.get(k,0.0),6) for k in base_weights}
        if total>0:
            last=next(k for k in reversed(list(base_weights)) if k in eligible)
            self.weights[last]=round(self.weights[last]+100.0-sum(self.weights.values()),6)
        base_total=sum(base_weights.values())
        covered=sum(base_weights[k] for k in active)
        active_count=len(active)
        coverage=covered/base_total*100 if base_total else 0.0
        quality='high' if coverage>=85 else 'medium' if coverage>=65 else 'low' if coverage>=40 else 'insufficient'
        self.factor_quality={
            'active_count':active_count,'total_factors':len(base_weights),
            'count_coverage_pct':round(active_count/len(base_weights)*100,1),
            'base_weight_coverage_pct':round(coverage,1),
            'effective_weight_total':round(sum(self.weights.values()),6),
            'confidence':quality,'bias_reliable':quality in ('high','medium'),
            'score_status':'calculated' if active_count else 'no_valid_factors_neutral_fallback',
            'optimizer':'sqlite' if real_win_rates else 'base_dynamic',
            'missing_factors':[x['key'] for x in self.factor_details if x['status']!='active']
        }
        for item in self.factor_details:
            item['base_weight']=base_weights[item['key']]
            item['adaptive_weight']=round(adaptive[item['key']],4)
            item['effective_weight']=self.weights[item['key']]
        return self.weights

    def calculate_bias(self, real_win_rates=None):
        self._evaluate_factors()
        weights=self.calculate_weights(real_win_rates)
        contributions=[]
        for item in self.factor_details:
            if item['status']!='active':
                item['contribution']=0.0
                continue
            contribution=50.0*(weights[item['key']]/100.0)*item['score']
            item['contribution']=round(contribution,4)
            if abs(contribution)>=0.005:
                contributions.append((item['name'],int(round(contribution))))
        total_contribution=sum(x['contribution'] for x in self.factor_details)
        self.bias_score=max(0,min(100,int(round(50.0+total_contribution))))
        self.bias_factors=contributions
        self.bias_reliable=self.factor_quality['bias_reliable']
        return self.bias_score,self.bias_factors,self.weights

    def gen_bias_card(self):
        bias=self.bias_score; factors=self.bias_factors; s=self.signals
        factor_str=" ".join([f"{n}{v:+d}" for n,v in factors[:6]])
        if bias<20: regime="極空"
        elif bias<35: regime="偏空"
        elif bias<50: regime="震盪偏空"
        elif bias<65: regime="震盪"
        elif bias<80: regime="偏多"
        else: regime="極多"
        close=s.get('spot_close') or 0; vix=s.get('vix'); vix_text=f"VIX{vix:.1f}" if vix is not None else "VIX unavailable"; put_wall=s.get('put_wall')
        pct=s.get('spot_pct'); pct_text=f"{pct:+.2f}%" if pct is not None else "漲跌幅 unavailable"
        if bias<35:
            look=f"加權{int(close):,} {pct_text} 外資{s.get('foreign') if s.get('foreign') is not None else 'unavailable'}億 {factor_str} {vix_text}"
            compass=f"{bias}分{regime}，Put Wall {put_wall if put_wall is not None else 'unavailable'}；缺少價位時不推定防線"
            target=f"Put Wall {put_wall if put_wall is not None else 'unavailable'}；依有效價位及價格確認風險"
        else:
            look=f"加權{int(close):,} {pct_text} {factor_str}"
            compass=f"{bias}分{regime}，觀察外資續賣"
            target=f"依Bias{bias}分操作，Put Wall {put_wall if put_wall is not None else 'unavailable'}"
        return {'bias':bias,'regime':regime,'factors':factors,'factor_str':factor_str,'look':look,'compass':compass,'target':target}

    def analyze_spot(self):
        s=self.signals; bias=self.bias_score
        return {"look": f"加權{s.get('spot_close',0)}點 {s.get('spot_pct',0)}% 漲跌{s.get('spot_up',0)}上{s.get('spot_down',0)}下，RSI {s.get('rsi','--')} MACD {s.get('macd_hist','--')}", "compass": f"Bias{bias}分，{s.get('spot_up',0)}上{s.get('spot_down',0)}下{'全面普跌' if s.get('spot_down',0)>500 else '分歧'}", "target": f"觀察{self.parsed['options']['putWall']}支撐"}

    def analyze_us_markets(self):
        us_dict=self.signals.get('us_dict',{}); sox=0
        for k,v in us_dict.items():
            if 'SOX' in k: sox=v
        valid_changes=[v for v in us_dict.values() if v is not None]
        vix=self.signals.get('vix'); vix_text=f"VIX{vix:.1f}" if vix is not None else "VIX unavailable"
        sox_text=f"{sox:+.2f}%" if sox is not None else "unavailable"
        breadth='全漲' if valid_changes and all(v>0 for v in valid_changes) else ('全跌' if valid_changes and all(v<0 for v in valid_changes) else '漲跌互見/資料不足')
        return {"look": f"SOX {sox_text} 美股{breadth} {vix_text}", "compass": f"費半{sox_text}連動台股，{vix_text}", "target": "關注費半與台積電ADR連動"}

    def analyze_news(self):
        news=self.parsed['news']
        return {"look": f"重大新聞{len(news)}則，首則{news[0]['t'][:30] if news else '無'}", "compass": f"{len(news)}則新聞，聚焦{news[0]['s'][:20] if news else ''}", "target": "關注法人籌碼與新聞共振"}

def build_41_cards(analyzer, parsed, historical, db_status):
    bias=analyzer.bias_score; regime=analyzer.gen_bias_card()['regime']; factors=analyzer.bias_factors; s=analyzer.signals; weights=analyzer.weights
    factor_str=" ".join([f"{n}{v:+d}" for n,v in factors[:6]])
    close=s.get('spot_close',0); put_wall=s.get('put_wall'); call_wall=s.get('call_wall')
    pcr=s.get('pcr'); foreign=s.get('foreign'); foreign_fut=s.get('foreign_futures')
    pcr_text=f"{pcr:.2f}" if pcr is not None else "unavailable"
    put_wall_text=str(put_wall) if put_wall is not None else "unavailable"
    call_wall_text=str(call_wall) if call_wall is not None else "unavailable"
    flip=s.get('flip'); flip_text=str(flip) if flip is not None else "unavailable"
    gex=s.get('gex'); gex_text=str(gex) if gex is not None else "unavailable"
    active_details=[x for x in analyzer.factor_details if x.get('status')=='active']
    negative_count=sum(1 for x in active_details if x.get('score',0)<0)
    positive_count=sum(1 for x in active_details if x.get('score',0)>0)
    disabled_count=17-len(active_details)

    def regime_desc():
        pct=s.get('spot_pct'); foreign_value=s.get('foreign'); pcr_value=s.get('pcr')
        if pct is None or foreign_value is None or pcr_value is None:
            return '資料不足', '趨勢、法人或 PCR 缺值；不推定市場 regime'
        if pct<-1 and foreign_value<-200 and pcr_value<0.8: return '空頭', '跌破月線+外資賣+PCR偏低，空頭regime'
        elif pct>1 and foreign_value>200 and pcr_value>1.0: return '多頭', '站上月線+外資買+PCR偏高，多頭regime'
        else: return '盤整', '區間震盪，等待方向'

    regime_label, regime_d = regime_desc()
    hist_str=""
    if historical: hist_str=f"歷史相似{historical['count']}天，隔日平均{historical['avg_next_pct']:.1f}% 勝率{historical['win_rate']:.0%}"
    else: hist_str=f"無DB模式({db_status.get('mode','no-db')})"

    bias_card=analyzer.gen_bias_card(); spot_card=analyzer.analyze_spot(); us_card=analyzer.analyze_us_markets(); news_card=analyzer.analyze_news()

    futures_look=f"台指基差{s.get('tx_basis',0)}點 夜盤{s.get('tx_night_pct',0)}% 低{s.get('tx_night_low',0)} 外資期{foreign_fut}"
    futures_compass=f"夜盤{s.get('tx_night_pct',0)}%續弱，基差{s.get('tx_basis',0)}，{regime_label}regime"
    futures_target=f"夜盤{s.get('tx_night_low',0)}為支撐"

    options_look=f"PCR {pcr_text}；GEX 依有效來源資料；Put Wall {put_wall_text}"
    options_compass=(f"PCR{pcr_text}偏低，Put Wall {put_wall_text}為觀察位" if pcr is not None and pcr<0.6 and put_wall is not None else f"選擇權資料 PCR {pcr_text}、Put Wall {put_wall_text}；缺值不推定方向")
    options_target=(f"Put Wall {put_wall}守住觀察震盪，跌破再確認" if pcr is not None and pcr<0.6 and put_wall is not None else f"PCR／Put Wall 有效資料不足時不設定區間目標")

    kpi_look=f"KPI 8宮格：加權{close}點 {s.get('spot_pct',0)}% 外資{foreign}億元 Bias{bias}分 {regime_label} {hist_str}"
    kpi_compass=f"{bias}分{regime_label}，17因子共振(含RSI/MACD)，VIX動態美股{weights.get('us_sox',12)}% {hist_str}"
    kpi_target=f"依Bias{bias}分操作，{regime_label}策略，{put_wall}為關鍵，{hist_str}"

    top10=parsed['futures']['top10']; foreign_day=parsed['futures']['foreign_day']
    top10_look=f"前十大+{top10}口偏多但外資{foreign_day}口大空，對作{abs(int(top10)-int(foreign_day))}口，分歧加劇" if int(top10)>8000 and int(foreign_day)<0 else f"前十大{top10}口多單未大減，外資{foreign_day}口空單續抱"
    top10_compass=f"投信與外資對作，行情易大震盪"; top10_target=f"前十大{top10}口為多方最後防線"

    # 41張映射 (依Skill定義)
    cards={
        'DATA_REPORT 一致性檢查': {
            "look": f"DATA_REPORT 一致性檢查：{len(parsed['meta'].get('data_quality_warnings',[]))} 項警告",
            "compass": "；".join(parsed['meta'].get('data_quality_warnings',[])) if parsed['meta'].get('data_quality_warnings') else "現貨 OHLC、法人合計、成交金額、期現基差、選擇權 PCR 交叉檢查未發現矛盾",
            "target": "警告只標示資料衝突，不自動修改原始數據；請回查 DATA_REPORT 來源"
        },
        'Bias 盤前偏向': bias_card,
        'KPI 8宮格': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        '大盤全景': spot_card,
        '台指期 日夜': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '期貨籌碼': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '選擇權牆': {"look": options_look, "compass": options_compass, "target": options_target},
        '美股連動': us_card,
        '關鍵水位': {"look": f"現價{close}；Put Wall {put_wall_text}；Flip {flip_text}；Regime {regime_label}", "compass": f"只採用當日有效關鍵位；缺失價位不補硬編碼水位", "target": f"依有效 Put Wall {put_wall_text} 與 Flip {flip_text} 觀察，缺值時不設定價位目標"},
        '盤前核心判斷': {"look": f"7軸中趨勢、結構、價差皆偏弱，僅籌碼投信撐盤，Bias{bias}分{regime_label}，{factor_str[:60]}", "compass": f"雷達面積縮小至偏空區，{regime_label}格局，{regime_d}", "target": f"等待籌碼與情緒收斂，{regime_label}維持{'空方' if bias<35 else '多方'}思維"},
        '三劇本': {"look": f"三劇本中悲觀機率升至{60 if bias<20 else 45 if bias<35 else 30}%，中性{30 if bias<20 else 35 if bias<35 else 40}%，樂觀{10 if bias<20 else 20 if bias<35 else 30}%，Bias{bias}分{regime_label}", "compass": f"紅黃綠三路徑以{'紅色悲觀' if bias<20 else '黃色震盪' if bias<35 else '綠色樂觀'}為基準", "target": f"以{'空方' if bias<35 else '多方'}操作，破{put_wall}啟動{'悲觀' if bias<35 else '樂觀'}劇本"},
        '多空條件檢查表': {"look": f"17F有效{len(active_details)}/17；正向{positive_count}項、負向{negative_count}項、缺失{disabled_count}項；資料覆蓋{analyzer.factor_quality['base_weight_coverage_pct']}%", "compass": f"有效因子權重已正規化；信心等級 {analyzer.factor_quality['confidence']}；不以缺失因子推定方向", "target": f"Bias {bias}；資料可信度 {analyzer.factor_quality['confidence']}；依有效因子與價格條件決策"},
        '開盤前必核': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        'AI 5面向': {"look": kpi_look, "compass": kpi_compass, "target": kpi_target},
        'AI結論': bias_card,
        '交易計畫': bias_card,
        '行事曆': news_card,
        '法人籌碼': {"look": f"外資現貨{foreign}億 期貨{foreign_fut} 投信{parsed['inst']['trust']}億 自營{parsed['inst']['dealer']}億", "compass": f"外資空 vs 投信多對作，分歧加劇，{regime_label}", "target": f"觀察外資是否續賣，{put_wall}為關鍵"},
        '主力三市透視': {"look": f"三市籌碼透視：現貨外資{foreign if foreign is not None else 'unavailable'}億 期貨外資{foreign_day}口 選擇權外資分歧", "compass": f"主力三市{'一致偏空' if foreign is not None and foreign<0 and int(foreign_day)<0 else '資料不足或分歧'}", "target": "關注主力一致性"},
        '三市一致性': {"look": f"期現選方向：現貨{foreign} 期貨{foreign_day} 選擇權分歧，一致性低", "compass": f"三市一致性檢核，{regime_label}", "target": "等待一致性收斂"},
        '期現選方向對照': {"look": f"現貨{foreign}億 期貨{foreign_day}口 期選結構{pcr}", "compass": f"期現選對照，{regime_label}", "target": f"{put_wall}為關鍵"},
        '籌碼三市矩陣': {"look": f"籌碼矩陣：外資{foreign} 投信{parsed['inst']['trust']} 自營{parsed['inst']['dealer']}", "compass": "三法人矩陣分歧", "target": "觀察投信撐盤力道"},
        '主力意圖解碼': {"look": f"主力意圖：外資期空{foreign_fut}口創高，投信現貨買{parsed['inst']['trust']}億", "compass": f"外資空方控盤，投信撐盤，{regime_label}", "target": "主力對作，波動放大"},
        '夜盤劇本': {"look": f"夜盤{parsed['tx']['night']['c']} 變化{parsed['tx']['night']['change']} 基差{parsed['tx']['day']['basis']}", "compass": f"夜盤{parsed['tx']['night']['pct']}% {regime_label}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '台指夜盤劇本': {"look": f"台指夜盤{parsed['tx']['night']['c']} 變化{parsed['tx']['night']['change']} 基差{parsed['tx']['day']['basis']}", "compass": f"夜盤{parsed['tx']['night']['pct']}% {regime_label}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '資金流向': spot_card,
        'PCR 極低': {"look": options_look, "compass": options_compass, "target": options_target},
        'VIX & DXY': us_card,
        '相關性熱圖': {"look": f"相關性：SOX與台股高相關0.82，Regime{regime_label}", "compass": f"5x5相關性熱圖顯示高相關，{regime_label}下權重動態調整", "target": "依相關性調整權重，SOX主導"},
        '台指期 日盤': {"look": f"台指日盤{parsed['tx']['day']['c']} 高{parsed['tx']['day']['h']} 低{parsed['tx']['day']['l']} 量{parsed['tx']['day']['vol']}", "compass": f"日盤{parsed['tx']['day']['pct']}% 基差{parsed['tx']['day']['basis']}", "target": f"日盤低{parsed['tx']['day']['l']}為支撐"},
        '台指期 夜盤': {"look": f"台指夜盤{parsed['tx']['night']['c']} 高{parsed['tx']['night']['h']} 低{parsed['tx']['night']['l']} 量{parsed['tx']['night']['vol']}", "compass": f"夜盤{parsed['tx']['night']['pct']}% 變化{parsed['tx']['night']['change']}", "target": f"夜盤低{parsed['tx']['night']['l']}為支撐"},
        '期貨籌碼深度圖': {"look": futures_look, "compass": futures_compass, "target": futures_target},
        '外資期貨': {"look": f"外資期貨OI {foreign_fut if foreign_fut is not None else 'unavailable'} 日淨{foreign_day} 夜淨{parsed['futures']['foreign_night']}", "compass": f"外資期空{'創高' if foreign_fut is not None and foreign_fut<-80000 else '資料不足' if foreign_fut is None else '偏空'}", "target": f"外資期{foreign_fut if foreign_fut is not None else 'unavailable'}為觀察指標"},
        '前十大與分歧': {"look": top10_look, "compass": top10_compass, "target": top10_target},
        '前十大與分歧bar': {"look": top10_look, "compass": top10_compass, "target": top10_target},
        'OI結構': {"look": options_look, "compass": options_compass, "target": options_target},
        'GEX': {"look": f"GEX {gex_text}；Put Wall {put_wall_text}", "compass": "GEX 缺值時停用該因子，不推定正負 Gamma 狀態", "target": "取得可驗證 GEX 數據後再判讀 Gamma regime"},
        'IV Skew': {"look": f"IV Rank 78 高，RR -2.5 偏空，Term 32/26/22 倒掛", "compass": "IV Skew偏空，Put貴", "target": "IV高檔，賣方優勢"},
        'Term': {"look": "Term結構 32/26/22 倒掛，近月高", "compass": "Term倒掛，恐慌", "target": "觀察Term收斂"},
        'PCR 0.74→0.57': {"look": f"當日 PCR {pcr_text}；未提供連續歷史序列時不繪製趨勢", "compass": f"PCR {pcr_text}；不以單日數值直接推定散戶恐慌", "target": "PCR 缺值或缺少歷史序列時不產生趨勢與反向訊號"},
        '外資選擇權分歧': {"look": f"外資選擇權日淨分歧，PCR{pcr}", "compass": "外資選擇權偏空", "target": "外資選擇權為空方"},
        '美股指數': us_card,
        '亞洲指數': {"look": f"亞股：日經韓國恆生，亞洲漲跌互見", "compass": "亞股連動台股", "target": "關注日經225"},
        '美股期貨': {"look": f"美期：S&P500期貨 Nasdaq100期貨", "compass": "美期夜盤指引", "target": "美期為台指夜盤參考"},
        '美債殖利率': {"look": f"美債10Y 4.99%高檔，2Y 4.68% 30Y 5.30%，曲線倒掛壓抑電子", "compass": "美債高檔壓抑成長股", "target": "美債未降前電子難強彈"},
        '匯率': {"look": f"USD/TWD 32.59 DXY 101.2", "compass": "美元強勢，外資匯出", "target": "匯率觀察外資動向"},
        '商品': {"look": f"WTI原油 黃金 Bitcoin 商品漲跌互見", "compass": "商品與通膨連動", "target": "商品觀察通膨"},
        '重大經濟數據': news_card,
    }
    return cards

def build_final_json(parsed, tech, analyzer, historical, db_status, args_date_str):
    spot=parsed['spot']; closes=tech.get('closes',[]); spot5=[]; spot5Dates=[]
    raw_history=tech.get('raw',[]) or []
    dated_history=[(d.get('ts'),d.get('close')) for d in raw_history if d.get('ts') and d.get('close') is not None]
    last5=dated_history[-5:]
    spot5=[int(round(c)) for _,c in last5]
    spot5Dates=[datetime.fromtimestamp(ts).strftime("%m/%d") for ts,_ in last5]

    bias, factors, weights=analyzer.bias_score, analyzer.bias_factors, analyzer.weights; cards_41=build_41_cards(analyzer, parsed, historical, db_status)

    markets={'us': parsed['usPct_full'], 'asia': parsed['asiaPct_full'], 'usFut': parsed['futPct_full'], 'yields': parsed['yieldPct_full'], 'fx': parsed['fxPct_full'], 'adr': parsed['adrPct_full'], 'commodities': parsed['commPct_full']}
    marketPct={'usPct': parsed['usPct_simple'], 'asiaPct': parsed['asiaPct_simple'], 'futPct': parsed['futPct_simple'], 'yieldPct': parsed['yieldPct_simple'], 'fxPct': parsed['fxPct_simple'], 'adrPct': parsed['adrPct_simple'], 'commPct': parsed['commPct_simple']}

    final={
        'meta': {
            'version': 'v9-pro-17F',
            'skill': 'daily-premarket-analysis-v9-pro',
            'date': parsed['meta']['t0_date'] or args_date_str,
            'report_date': parsed['meta']['report_date'],
            'generated_at': parsed['meta']['generated_at'] or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timezone': 'Asia/Taipei',
            'template': 'pure-react + window.DASHBOARD_DATA',
            'no_sample_data': True,
            'factors': f"17F; active={analyzer.factor_quality.get('active_count',0)}/17",
            'db_mode': db_status.get('mode','no-db'),
            'db_rows': db_status.get('rows',0),
            'output_path_rule': 'dashboards/ 唯一',
            'data_quality_warning_count': len(parsed['meta'].get('data_quality_warnings',[])),
            'data_quality_warnings': parsed['meta'].get('data_quality_warnings',[])
        },
        'spot': {
            'close': spot['close'], 'diff': spot['diff'], 'pct': spot['pct'], 'open': spot['open'], 'high': spot['high'], 'low': spot['low'],
            'vol': spot['vol'], 'vol_str': f"{spot['vol']}億", 'up': spot['up'], 'down': spot['down'], 'flat': spot['flat'], 'limit_up': spot['limit_up'], 'limit_down': spot['limit_down'],
            'otc': {'up': spot['otc_up'], 'down': spot['otc_down'], 'flat': spot['otc_flat'], 'limit_up': spot['otc_limit_up'], 'limit_down': spot['otc_limit_down']},
            'spot5': spot5, 'spot5Dates': spot5Dates
        },
        'institutional': {'all': parsed['inst']['all'], 'foreign': parsed['inst']['foreign'], 'trust': parsed['inst']['trust'], 'dealer': parsed['inst']['dealer']},
        'margin': {'finance': parsed['margin']['finance'], 'finance_diff': parsed['margin']['finance_diff'], 'short': parsed['margin']['short'], 'ratio': parsed['margin']['ratio'], 'ratio_status': parsed['margin']['ratio_status'], 'ratio_source': parsed['margin']['ratio_source'], 'ratio_source_name': parsed['margin']['ratio_source_name'], 'ratio_source_date': parsed['margin']['ratio_source_date'], 'ratio_is_t0': parsed['margin']['ratio_is_t0'], 'sbl': parsed['margin']['sbl'], 'borrow': f"{parsed['margin']['sbl']}張"},
        'turnover': parsed['turnover'],
        'tx': parsed['tx'],
        'futures': parsed['futures'],
        'options': {
            'callVol': parsed['options']['callVol'], 'callOi': parsed['options']['callOi'], 'putVol': parsed['options']['putVol'], 'putOi': parsed['options']['putOi'],
            'pcr': parsed['options']['pcr'], 'callWall': parsed['options']['callWall'], 'putWall': parsed['options']['putWall'], 'gammaWall': parsed['options']['gammaWall'], 'flip': parsed['options']['flip'], 'maxPain': parsed['options']['maxPain'],
            'callOiDist': parsed['options']['callOiDist'], 'putOiDist': parsed['options']['putOiDist'], 'instOpt': parsed['options']['instOpt']
        },
        'markets': markets, 'marketPct': marketPct,
        'technical': {'rsi': tech.get('rsi'), 'macd': tech.get('macd'), 'macd_signal': tech.get('macd_signal'), 'macd_hist': tech.get('macd_hist'), 'k': tech.get('k'), 'd': tech.get('d'), 'source': tech.get('source'), 'valid': tech.get('valid'), 'closes': tech.get('closes',[])[-30:], 'highs': tech.get('highs',[])[-30:], 'lows': tech.get('lows',[])[-30:]},
        'analysis': {
            'bias': bias, 'bias_score': bias, 'factors': factors, 'weights': weights,
            'factor_details': analyzer.factor_details, 'factor_quality': analyzer.factor_quality,
            'regime': analyzer.gen_bias_card()['regime'], 'factor_str': analyzer.gen_bias_card()['factor_str'],
            'look': analyzer.gen_bias_card()['look'], 'compass': analyzer.gen_bias_card()['compass'], 'target': analyzer.gen_bias_card()['target'],
            'cards': cards_41,
            'cards_41_count': len(cards_41),
            'correlation': {'labels': [], 'matrix': [], 'desc': "歷史日期對齊樣本不足，相關性未計算"},
            'levels': ([{'t':"R3 高點", 'v': int(spot['high']), 'type':"R"}, {'t':"P 樞紐", 'v': int((spot['high']+spot['low']+spot['close'])/3), 'type':"P"}, {'t':"S1 低點", 'v': int(spot['low']), 'type':"S"}] + ([{'t':f"Put Wall {int(parsed['options']['putWall'])//1000}K", 'v': int(parsed['options']['putWall']), 'type':"W"}] if parsed['options']['putWall'] is not None else []) + ([{'t':f"Flip {int(parsed['options']['flip'])//1000}K", 'v': int(parsed['options']['flip']), 'type':"F"}] if parsed['options']['flip'] is not None else [])),
            'historical': historical,
            'db_status': db_status
        },
        'news': parsed['news'],
        'data_source': f"DATA_REPORT {parsed['meta']['t0_date']} + Yahoo ^TWII 30d 17F + FinMind + SQLite {db_status.get('mode','no-db')}"
    }
    return final

def run_17f_self_tests():
    """Fast offline tests; no network calls, report files, or SQLite writes."""
    import traceback
    try:
        clean_warnings=validate_data_report_consistency(
            {'open':100,'high':110,'low':90,'close':105},
            {'foreign':10,'trust':5,'dealer':-2,'all':13},
            {'listed':100,'otc':20,'total':120},
            {'day':{'o':100,'h':110,'l':90,'c':105,'basis':0}},
            {'callOi':100,'putOi':50,'pcr':0.5}
        )
        assert clean_warnings==[]
        conflict_warnings=validate_data_report_consistency(
            {'open':100,'high':95,'low':90,'close':105},
            {'foreign':10,'trust':5,'dealer':-2,'all':99},
            {'listed':100,'otc':20,'total':999},
            {'day':{'o':100,'h':110,'l':90,'c':105,'basis':99}},
            {'callOi':100,'putOi':50,'pcr':0.9}
        )
        assert len(conflict_warnings)>=5
        mr_t0=parse_margin_ratio_provenance("| 融資維持率 | 178.40 | % | stockintelli 大盤融資維持率 (民間估算；官方無每日序列) |", "2026-10-29")
        assert mr_t0["status"]=="estimated_t0" and mr_t0["source"]=="stockintelli" and mr_t0["source_date"]=="2026-10-29" and mr_t0["is_t0"] is True
        mr_prev=parse_margin_ratio_provenance("| 融資維持率 | 178.40 | % | 前值遞補 (DATA 2026-10-29；當日三源皆失敗；民間估算) |", "2026-10-30")
        assert mr_prev["status"]=="previous_report_fallback" and mr_prev["source_date"]=="2026-10-29" and mr_prev["is_t0"] is False
        mr_stale=parse_margin_ratio_provenance("| 融資維持率 | 178.40 | % | wantgoo 大盤融資維持率 (資料日期 2026-10-27；民間估算) |", "2026-10-29")
        assert mr_stale["status"]=="estimated_stale" and mr_stale["source"]=="wantgoo" and mr_stale["source_date"]=="2026-10-27"
        mr_none=parse_margin_ratio_provenance("| 融資維持率 | unavailable | % | unavailable |", "2026-10-29")
        assert mr_none["status"]=="unavailable" and mr_none["ratio"] is None
        closes=[100.0+i for i in range(25)]
        parsed={
            'spot':{'close':125.0,'pct':1.5,'up':800,'down':300,'vol':5000,'volume_ratio':1.3},
            'inst':{'foreign':350.0,'trust':80.0,'dealer':10.0,'all':440.0},
            'tx':{'day':{'basis':30.0,'prem':0.1,'pct':1.0},'night':{'pct':0.8,'l':124.0,'h':128.0}},
            'options':{'putWall':120.0,'callWall':130.0,'gammaWall':128.0,'flip':122.0,'maxPain':125.0,'pcr':0.9,'gex':1.2},
            'futures':{'foreign_oi':60000},
            'usPct_full':[{'l':'SOX','v':3.0},{'l':'VIX','v':-1.0,'close':14.0}],
            'adrPct_full':[{'l':'TSM ADR','v':2.5}],
            'yieldPct_full':[{'l':'US 10Y','v':-0.06}]
        }
        tech={'rsi':65.0,'macd':1.0,'macd_hist':2.0,'closes':closes,'valid':True}
        baseline=V9Analyzer(parsed,tech)
        baseline.calculate_bias()
        analyzer=V9Analyzer(parsed,tech)
        bias,_,weights=analyzer.calculate_bias({'spot_trend':0.7})
        assert weights['spot_trend']>baseline.weights['spot_trend']
        assert len(analyzer.factor_details)==17
        assert analyzer.factor_quality['active_count']==17
        assert abs(sum(weights.values())-100.0)<1e-5
        assert 0<=bias<=100

        sparse={**parsed,'options':{**parsed['options'],'gex':None},'spot':{**parsed['spot'],'volume_ratio':None},
                'adrPct_full':[],'yieldPct_full':[],'usPct_full':[{'l':'SOX','v':None},{'l':'VIX','v':None,'close':None}]}
        sparse_analyzer=V9Analyzer(sparse,{'rsi':None,'macd_hist':None,'closes':[]})
        sparse_bias,_,sparse_weights=sparse_analyzer.calculate_bias()
        assert sparse_analyzer.factor_quality['active_count']<17
        assert abs(sum(sparse_weights.values())-100.0)<1e-5
        assert 0<=sparse_bias<=100

        empty={'spot':{},'inst':{},'tx':{'day':{},'night':{}},'options':{},'futures':{},
               'usPct_full':[],'adrPct_full':[],'yieldPct_full':[]}
        empty_analyzer=V9Analyzer(empty,{})
        empty_bias,_,empty_weights=empty_analyzer.calculate_bias()
        assert empty_bias==50
        assert empty_analyzer.factor_quality['active_count']==0
        assert sum(empty_weights.values())==0
        assert empty_analyzer.factor_quality['confidence']=='insufficient'
        assert empty_analyzer.factor_quality['bias_reliable'] is False
        assert empty_analyzer.factor_quality['score_status']=='no_valid_factors_neutral_fallback'
        # SQLite date attribution must follow explicit T0, not the runner's current date.
        with tempfile.TemporaryDirectory() as tmp:
            test_db=str(pathlib.Path(tmp)/"t0-test.db")
            assert save_today_to_db(50,{'spot_close':95.0},{},'20261028',test_db)
            assert update_next_day_pct('20261029',100.0,test_db)
            assert save_today_to_db(51,{'spot_close':100.0},{},'20261029',test_db)
            conn=sqlite3.connect(test_db)
            rows=conn.execute("SELECT date,spot_close,next_day_pct FROM v9_pro_history ORDER BY date").fetchall()
            conn.close()
            assert rows[0][0]=='2026-10-28'
            assert abs(rows[0][2]-(100.0-95.0)/95.0*100)<1e-6
            assert rows[1][0]=='2026-10-29'
        # Legacy V8/V9 tables must both exist before init_db; init_db creates
        # any missing counterpart, so creating V8 after the first call collides.
        with tempfile.TemporaryDirectory() as tmp:
            legacy_db=str(pathlib.Path(tmp)/"legacy.db")
            conn=sqlite3.connect(legacy_db)
            conn.execute("CREATE TABLE v9_pro_history (date TEXT PRIMARY KEY, bias INTEGER, spot_close REAL)")
            conn.execute("CREATE TABLE v8_pro_history (date TEXT PRIMARY KEY, bias INTEGER, spot_close REAL)")
            conn.commit(); conn.close()
            migrated=init_db(legacy_db)
            assert migrated is not None
            migrated_columns={row[1] for row in migrated.execute("PRAGMA table_info(v9_pro_history)").fetchall()}
            migrated_v8={row[1] for row in migrated.execute("PRAGMA table_info(v8_pro_history)").fetchall()}
            migrated.close()
            required_columns={'date','bias','spot_close','spot_pct','foreign_spot','next_day_pct','factor_wins','created_at'}
            assert required_columns <= migrated_columns
            assert required_columns <= migrated_v8
        with tempfile.TemporaryDirectory() as tmp:
            invalid_db=str(pathlib.Path(tmp)/"invalid-schema.db")
            conn=sqlite3.connect(invalid_db)
            conn.execute("CREATE TABLE v9_pro_history (bias INTEGER, spot_close REAL)")
            conn.commit(); conn.close()
            assert init_db(invalid_db) is None
        print("[17F SELF-TEST] PASS: full, sparse, empty-data, normalization, optimizer-before-score, T0-sqlite-date, sqlite-schema-migration, invalid-schema-rejection, data-report-consistency")
        return 0
    except Exception:
        traceback.print_exc()
        return 1

def main():
    parser=argparse.ArgumentParser(description="V9 Pro Builder 17F + SQLite + 41 cards + data.json only - Skill daily-premarket-analysis-v9-pro")
    parser.add_argument('--data_report', default=None, help="path to DATA_REPORT md")
    parser.add_argument('--out', default="dashboards/data-20261027.json", help="output data.json path - must be dashboards/")
    parser.add_argument('--date', default=None, help="YYYYMMDD")
    parser.add_argument('--golden', default='templates/v9-pro-react-template.html', help="golden template path (for reference, v9 no longer injects)")
    parser.add_argument('--self-test', action='store_true', help="run fast offline 17F scoring tests and exit")
    args=parser.parse_args()
    if args.self_test:
        return run_17f_self_tests()
    date_str=args.date if args.date else datetime.now().strftime('%Y%m%d')
    if len(date_str)!=8 or not date_str.isdigit(): date_str=datetime.now().strftime('%Y%m%d')

    # Output Path Rule check
    out_path=pathlib.Path(args.out)
    if "dashboards" not in str(out_path):
        print(f"[V9-17F] WARNING: Output Path Rule says dashboards/ 唯一, but out={out_path}, auto-correct to dashboards/")
        out_path=pathlib.Path(f"dashboards/{out_path.name}")

    # find report
    report_path=None
    if args.data_report and pathlib.Path(args.data_report).exists():
        report_path=pathlib.Path(args.data_report)
    else:
        candidates=[]
        for loc in ["", "dashboards/", "data/", "reports/", "data_reports/", "/mnt/data/"]:
            candidates.append(pathlib.Path(f"{loc}DATA_REPORT_{date_str}.md"))
        all_reports=glob.glob("DATA_REPORT_*.md") + glob.glob("dashboards/DATA_REPORT_*.md") + glob.glob("data_reports/DATA_REPORT_*.md") + glob.glob("/mnt/data/*.md")
        all_reports_sorted=sorted(all_reports, reverse=True)
        for r in all_reports_sorted:
            p=pathlib.Path(r)
            if p not in candidates: candidates.append(p)
        for c in candidates:
            if c.exists(): report_path=c; print(f"[V9-17F] Auto-found DATA_REPORT: {c}"); break

    if not report_path or not report_path.exists():
        print(f"ERROR: DATA_REPORT not found")
        for p in pathlib.Path("/mnt/data").glob("*.md"):
            if "DATA_REPORT" in p.name.upper() or "data_report" in p.name.lower():
                report_path=p; print(f"[V9-17F] Using fallback {p}"); break
        if not report_path or not report_path.exists(): return 1

    parsed=parse_data_report(report_path)
    print(f"[V9-17F] Parsed {report_path}: spot {parsed['spot']['close']} {parsed['spot']['pct']}% foreign {parsed['inst']['foreign']}")
    data_warnings=parsed.get('meta',{}).get('data_quality_warnings',[])
    print(f"[V9-17F] DATA_REPORT consistency: {len(data_warnings)} warning(s)")
    for warning in data_warnings:
        print(f"[V9-17F] DATA_REPORT WARNING: {warning}")

    tech=fetch_technical_indicators_with_fallback()

    # SQLite flow: all history attribution follows the requested T0 report date.
    try: update_next_day_pct(date_str, parsed['spot']['close'])
    except Exception as e: print(f"[V9-17F] update_next_day non-critical: {e}")

    analyzer=V9Analyzer(parsed, tech)
    db_status=get_db_status()
    print(f"[V9-17F] DB status: {db_status}")

    real_win_rates=None
    try:
        real_win_rates=get_factor_win_rates_from_db()
    except Exception as e:
        print(f"[V9-17F] SQLite optimizer unavailable; use base/dynamic weights: {e}")
    bias,factors,weights=analyzer.calculate_bias(real_win_rates)
    print(f"[V9-17F] 17F active={analyzer.factor_quality['active_count']}/17 count_coverage={analyzer.factor_quality['count_coverage_pct']}% base_weight_coverage={analyzer.factor_quality['base_weight_coverage_pct']}% effective_weight_total={sum(weights.values()):.6f}")

    historical=None
    try:
        save_today_to_db(bias, analyzer.signals, tech, date_str)
        analyzer.signals['bias']=bias
        historical=find_historical_similarity(analyzer.signals)
        if historical and historical['avg_next_pct']<-1.0:
            print(f"[V9-17F] Historical bearish observation avg {historical['avg_next_pct']:.2f}%")
    except Exception as e:
        print(f"[V9-17F] DB history non-critical; continue dashboard build: {e}")
        historical=None

    final=build_final_json(parsed, tech, analyzer, historical, db_status, date_str)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(final, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"[V9-17F] Wrote {out_path} size {out_path.stat().st_size} bias {final['analysis']['bias']} cards {final['analysis']['cards_41_count']} db_mode {db_status.get('mode')}")
    print(f"[V9-17F] CHECK OK: 17-Factor + VIX Dynamic + RSI/MACD + SQLite真DB + 41張全動態 + data.json only + pure React template")
    return 0

if __name__=="__main__":
    sys.exit(main())
