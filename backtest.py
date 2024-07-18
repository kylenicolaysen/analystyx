def buy(balance, price, shares):
    new_shares = int(balance / price)
    if new_shares == 0:
        return shares, balance
    remaining_bal = balance % price
    print('BUY ', new_shares, ' @ ', price)
    return (new_shares, remaining_bal)

def sell(balance, price, shares, hide = False):
    if shares < 1:
        return balance
    amt = price * shares
    if hide == False:
        print('SELL ', shares, ' @ ', price)
    return balance + amt

def backtest(price_data, signals, leverage = 1):
    balance = 100000
    shares = 0
    price_data = price_data.head(5000)
    signals = signals[:5000]
    for index, signal in enumerate(signals):
        if signal[0] == 'buy':
            shares, balance = buy(balance, price_data.Close[index], shares)
            # print(index, shares, balance)
        elif signal[0] == 'sell':
            balance = sell(balance, price_data.Close[index], shares)
            shares = 0
            # print(index, shares, balance)
    print('\n****************')
    print('Balance: ', balance)
    print('Shares: ', shares)
    if shares != 0:
        balance = sell(balance, price_data.iloc[-1]['Close'], shares, True)
    print('Strategy Balance: ', balance)
    print('\n****************')
    b = buy(100000, price_data.Close[0], 0)
    s = sell(b[1], price_data.iloc[-1]['Close'], b[0])
    print('Hold Balance: ', s)
    print('****************\n')
    return