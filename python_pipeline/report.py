def print_signals(signals):
    if not signals:
        print("No signals found.")
        return

    for signal in signals:
        print(f'{signal["date"]} {signal["signal"]} at close {signal["close"]}')
