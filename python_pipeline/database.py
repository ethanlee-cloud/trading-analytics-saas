import sqlite3


def connect_db(db_path="data/trading.db"):
    return sqlite3.connect(db_path)


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY,
            symbol TEXT NOT NULL,
            date TEXT NOT NULL,
            signal TEXT NOT NULL,
            direction TEXT NOT NULL,
            pattern TEXT NOT NULL,
            close REAL NOT NULL,
            next_day_return REAL NOT NULL
        )
    """)

    conn.commit()


def save_signals(conn, signals, symbol):
    cursor = conn.cursor()

    for signal in signals:
        cursor.execute("""
            INSERT INTO signals (
                symbol, date, signal, direction, pattern, close, next_day_return
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            symbol,
            signal["date"],
            signal["signal"],
            signal["direction"],
            signal["pattern"],
            signal["close"],
            signal["next_day_return"],
        ))

    conn.commit()


def get_signals(conn, symbol=None, direction=None):
    cursor = conn.cursor()

    query = "SELECT symbol, date, signal, direction, pattern, close, next_day_return FROM signals"
    conditions = []
    params = []

    if symbol:
        conditions.append("symbol = ?")
        params.append(symbol)

    if direction:
        conditions.append("direction = ?")
        params.append(direction)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, params)

    rows = cursor.fetchall()

    signals = []
    for row in rows:
        signals.append({
            "symbol": row[0],
            "date": row[1],
            "signal": row[2],
            "direction": row[3],
            "pattern": row[4],
            "close": row[5],
            "next_day_return": row[6],
        })

    return signals