def macd_histogram_trend_reversal_signal(data):
    data = list(data)
    if len(data) < 2:
        return []
    trends = [(None, False, data[0])]
    current_trend = None
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            new_trend = 'increasing'
        elif data[i] < data[i - 1]:
            new_trend = 'decreasing'
        else:
            new_trend = 'no trend'
        
        if current_trend == new_trend and trends[i-1][0] == new_trend and trends[i-2][0] != new_trend:
            trends.append((new_trend, True, data[i]))
        else:
            trends.append((new_trend, False, data[i]))
        current_trend = new_trend
    return trends