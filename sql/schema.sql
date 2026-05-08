CREATE TABLE IF NOT EXISTS  prices (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    open REAL NOT NULL,
    close REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    signal TEXT NOT NULL,
    direction TEXT NOT NULL,
    pattern TEXT NOT NULL,
    close REAL NOT NULL,
    next_day_return REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS  strategy_performance (
    id INTEGER PRIMARY KEY,
    strategy_name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    total_trades INTEGER NOT NULL,
    avg_return REAL NOT NULL,
    win_rate REAL NOT NULL
);


CREATE INDEX IF NOT EXISTS idx_signals_symbol
ON signals(symbol);

CREATE INDEX IF NOT EXISTS idx_signals_direction
ON signals(direction);

CREATE INDEX IF NOT EXISTS idx_signals_symbol_direction
ON signals(symbol, direction);

CREATE INDEX IF NOT EXISTS idx_signals_date
ON signals(date);