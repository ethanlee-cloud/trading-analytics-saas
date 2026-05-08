import sqlite3


def connect_db(db_path="data/trading.db"):
    return sqlite3.connect(db_path)




def save_signals(conn, signals, symbol):
    cursor = conn.cursor()

    # Delete existing signals for this symbol to avoid duplicates
    cursor.execute("DELETE FROM signals WHERE symbol = ?", (symbol,))

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


def get_performance_by_direction(conn, symbol):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            direction,
            COUNT(*) AS total_trades,
            AVG(next_day_return) AS avg_return,
            AVG(CASE WHEN next_day_return > 0 THEN 1.0 ELSE 0.0 END) AS win_rate
        FROM signals
        WHERE symbol = ?
        GROUP BY direction
    """, (symbol,))

    rows = cursor.fetchall()

    results = []
    for row in rows:
        results.append({
            "direction": row[0],
            "total_trades": row[1],
            "avg_return": row[2],
            "win_rate": row[3],
        })

    return results