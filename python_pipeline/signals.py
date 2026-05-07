def find_reversal_signals(prices):
    signals = []

    for i in range(2, len(prices)):
        two_days_ago = prices[i - 2]
        yesterday = prices[i - 1]
        today = prices[i]

        two_days_ago_red = two_days_ago["close"] < two_days_ago["open"]
        yesterday_red = yesterday["close"] < yesterday["open"]
        today_green = today["close"] > today["open"]
        
        two_days_ago_green = two_days_ago["close"] > two_days_ago["open"]
        yesterday_green = yesterday["close"] > yesterday["open"]
        today_red = today["close"] < today["open"]

        if two_days_ago_red and yesterday_red and today_green:
            signals.append({
                "date": today["date"],
                "signal": "possible_reversal",
                "pattern": "two_red_then_green",
                "close": today["close"],
            })

        if two_days_ago_green and yesterday_green and today_red:
            signals.append({
                "date": today["date"],
                "signal": "possible_bearish_reversal",
                "pattern": "two_green_then_red",
                "close": today["close"],
            })  

    return signals
