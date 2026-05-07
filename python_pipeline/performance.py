def calculate_performance(signals):
    if not signals:
        return {
            "avg_return": 0,
            "win_rate": 0,
            "total_trades": 0,
        }

    total_return = 0
    wins = 0

    for signal in signals:
        r = signal["next_day_return"]
        total_return += r

        if r > 0:
            wins += 1

    avg_return = total_return / len(signals)
    win_rate = wins / len(signals)

    return {
        "avg_return": avg_return,
        "win_rate": win_rate,
        "total_trades": len(signals),
    }
