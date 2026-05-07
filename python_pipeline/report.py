def print_signals(signals):
    if not signals:
        print("No signals found.")
        return

    for signal in signals:
        print(
            f'{signal["date"]} {signal["direction"]} {signal["pattern"]} '
            f'next-day return {signal["next_day_return"] * 100:.2f}%'
        )