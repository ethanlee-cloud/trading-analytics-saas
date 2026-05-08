def print_signals(signals):
    if not signals:
        print("No signals found.")
        return

    for signal in signals:
        print(
            f'{signal["date"]} {signal["direction"]} {signal["pattern"]} '
            f'next-day return {signal["next_day_return"] * 100:.2f}%'
        )

def print_performance(perf):
    print("\n--- Strategy Performance ---")
    print(f'Total trades: {perf["total_trades"]}')
    print(f'Average return: {perf["avg_return"] * 100:.2f}%')
    print(f'Win rate: {perf["win_rate"] * 100:.2f}%')


def print_performance_by_direction(results):
    print("\n--- Performance by Direction ---")

    for row in results:
        print(
            f'{row["direction"]}: '
            f'{row["total_trades"]} trades, '
            f'avg return {row["avg_return"] * 100:.2f}%, '
            f'win rate {row["win_rate"] * 100:.2f}%'
        )