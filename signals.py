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
        
        if current_trend == new_trend and trends[i-1][2] == new_trend and trends[i-2][2] != new_trend:
            if new_trend == 'increasing':
                trends.append(('buy', data[i], new_trend)) 
            elif new_trend == 'decreasing':
                trends.append(('sell', data[i], new_trend))        
        else:
            trends.append((None, data[i], new_trend))
        current_trend = new_trend
    return trends