from data_loader import load_prices
from signals import find_reversal_signals
from report import print_signals, print_performance, print_performance_by_direction
from performance import calculate_performance
from database import connect_db,save_signals, get_signals, get_performance_by_direction


def main():
    file_path = "data/sample_prices.csv"
    symbol = "SPY"

    prices = load_prices(file_path)
    signals = find_reversal_signals(prices)

    print_signals(signals)

    perf = calculate_performance(signals)
    print_performance(perf)

    conn = connect_db()
    
    save_signals(conn, signals, symbol)
    by_direction = get_performance_by_direction(conn, symbol)
    print_performance_by_direction(by_direction)
    
    print("\n--- Query: Bullish Signals ---")
    queried = get_signals(conn, symbol="SPY", direction="bullish")
    print_signals(queried)

    conn.close()

    print("\nSignals saved to trading.db")


if __name__ == "__main__":
    main()