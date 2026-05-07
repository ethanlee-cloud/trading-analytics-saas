from data_loader import load_prices
from signals import find_reversal_signals
from report import print_signals, print_performance
from performance import calculate_performance
from database import connect_db, create_tables, save_signals, get_signals


def main():
    file_path = "data/sample_prices.csv"
    symbol = "SPY"

    prices = load_prices(file_path)
    signals = find_reversal_signals(prices)

    print_signals(signals)

    perf = calculate_performance(signals)
    print_performance(perf)

    conn = connect_db()
    create_tables(conn)
    save_signals(conn, signals, symbol)

    print("\n--- Query: Bullish Signals ---")
    queried = get_signals(conn, symbol="SPY", direction="bullish")
    print_signals(queried)

    conn.close()

    print("\nSignals saved to trading.db")


if __name__ == "__main__":
    main()