
-- V8 Pro SQLite 真DB - 若 v8_pro_history.db 無法下載，用此 SQL 建表
-- 執行: sqlite3 dashboards/v8_pro_history.db < v8_pro_history.sql

CREATE TABLE IF NOT EXISTS v8_pro_history (
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
);

CREATE TABLE IF NOT EXISTS factor_performance (
    factor TEXT PRIMARY KEY,
    wins INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    win_rate REAL DEFAULT 0.5,
    weight REAL DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 範例資料 (今日)
INSERT OR IGNORE INTO v8_pro_history (date, bias, spot_close, spot_pct, foreign_spot, pcr) 
VALUES ('2026-10-27', 0, 46041.43, -1.81, -815.8, 0.57);
