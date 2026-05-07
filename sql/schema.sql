CREATE TABLE prices (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    open REAL NOT NULL,
    close REAL NOT NULL
);

CREATE TABLE signals (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    date TEXT NOT NULL,
    signal TEXT NOT NULL,
    direction TEXT NOT NULL,
    pattern TEXT NOT NULL,
    close REAL NOT NULL,
    next_day_return REAL NOT NULL
);

CREATE TABLE strategy_performance (
    id INTEGER PRIMARY KEY,
    strategy_name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    total_trades INTEGER NOT NULL,
    avg_return REAL NOT NULL,
    win_rate REAL NOT NULL
);
