def find_reversal_signals(prices):
    signals = []

    for i in range(2, len(prices)-1):
        two_days_ago = prices[i - 2]
        yesterday = prices[i - 1]
        today = prices[i]
        next_day = prices[i + 1]

        two_days_ago_red = two_days_ago["close"] < two_days_ago["open"]
        yesterday_red = yesterday["close"] < yesterday["open"]
        today_green = today["close"] > today["open"]
        
        two_days_ago_green = two_days_ago["close"] > two_days_ago["open"]
        yesterday_green = yesterday["close"] > yesterday["open"]
        today_red = today["close"] < today["open"]

        next_day_return = (next_day["close"] - today["close"]) / today["close"]

        if two_days_ago_red and yesterday_red and today_green:
            signals.append({
                "date": today["date"],
                "signal": "possible_reversal",
                "direction": "bullish",
                "pattern": "two_red_then_green",
                "next_day_return": next_day_return,
                "close": today["close"],
            })

        if two_days_ago_green and yesterday_green and today_red:
            signals.append({
                "date": today["date"],
                "signal": "possible_bearish_reversal",
                "direction": "bearish",
                "pattern": "two_green_then_red",
                "next_day_return": next_day_return,
                "close": today["close"],
            })  

    return signals
