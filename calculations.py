def calculate_ema_gpt(prices, periods):
    weight = 2 / (periods + 1)
    ema = [prices[0]]
    for price in prices[1:]:
        ema.append((price - ema[-1]) * weight + ema[-1])
    return ema
