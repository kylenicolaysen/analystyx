def calculate_ema(prices, periods):
    weight = 2 / (periods + 1)
    ema = [prices[0]]
    for price in prices[1:]:
        ema.append((price - ema[-1]) * weight + ema[-1])
    return ema

def calculate_sma(prices, window_length):
    if window_length <= 0:
        raise ValueError("Window length must be a positive integer.")
    
    sma = []
    for i in range(len(prices)):
        if i + 1 < window_length:
            # Calculate the average of the available values so far
            sma.append(sum(prices[:i+1]) / (i+1))
        else:
            window = prices[i - window_length + 1:i + 1]
            sma.append(sum(window) / window_length)

    return sma