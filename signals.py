def macd_histogram_trend_reversal_signal(data):
    data = list(data)
    if len(data) < 2:
        return []
    trends = [(None, False)]
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


        # if new_trend != current_trend and new_trend != 'no trend':
        #     if current_trend is not None or current_trend is not 'no trend':
        #         trends.append((i, current_trend, data[trend_start_index + 1], False))
        #     current_trend = new_trend
        #     trend_start_index = i - 1
        # else:
        #     if trend_start_index == i - 2:
    return trends

if __name__ == '__main__':
    macd_histogram = [0.5, 1.0, 1.5, 1.2, 0.8, 0.4, -0.1, -0.6, -0.2, 0.3, 0.7, 1.0]
    trends = macd_histogram_trend_reversal_id(macd_histogram)
    for item in trends:
        print(item)