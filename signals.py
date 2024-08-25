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
        
        if current_trend == new_trend and trends[i-2][2] == new_trend and trends[i-3][2] != new_trend:
            if new_trend == 'increasing' and data[i] > 0.09:
                trends.append(('buy', data[i], new_trend)) 
            elif new_trend == 'decreasing' and data[i] < -0.09:
                trends.append(('sell', data[i], new_trend))     
            else:
                trends.append((None, data[i], new_trend))   
        else:
            trends.append((None, data[i], new_trend))
        current_trend = new_trend
    return trends

def two_hundred_sma_signal(close, sma):
    trends = []
    if len(close) != len(sma):
        print('NOT MATCHINGLENGTH!')
        return
    for i in range(1, len(close)):
        # print('Close: ', close[i])
        # print('SMA: ', sma[i])
        if close[i] < sma[i]:
            trends.append(('sell', close[i]))
        elif close[i] > sma[i]:
            trends.append(('buy', close[i]))
        else:
            trends.append((None, close[i]))
    return trends

def two_hund_sma_triple_lev_buy(data):
    data = list()
    if len(data < 2):
        return []
    return