from data_loader import load_prices
from signals import find_reversal_signals
from report import print_signals


def main():
    file_path = "data/sample_prices.csv"

    prices = load_prices(file_path)
    signals = find_reversal_signals(prices)
    print_signals(signals)


if __name__ == "__main__":
    main()
