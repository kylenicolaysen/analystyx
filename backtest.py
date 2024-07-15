def buy(balance, price):
    shares = int(balance / price)
    remaining_bal = balance % price
    print('BUY ', shares, ' @ ', price)
    return (shares, remaining_bal)

def sell(balance, price, shares):
    amt = price * shares
    print('SELL ', shares, ' @ ', price)
    return balance + amt

def backtest(df, signals):
    balance = 100000
    shares = 0
    df = df.head(5000)
    signals = signals[:5000]
    for index, item in enumerate(signals):
        if item[1] == True and item[0] == 'increasing':
            shares, balance = buy(balance, df.Close[index])
            print(index, shares, balance)
        elif item[1] == True and item[0] == 'decreasing':
            balance = sell(balance, df.Close[index], shares)
            shares = 0
            print(index, shares, balance)
 
    print('Balance: ', balance)
    print('Shares: ', shares)
    if shares != 0:
        balance = sell(balance, df.tail(1).Close, shares)
    print('Final Balance: ', balance)

    print('\n*\n*\n*\n*')
    b = buy(100000, df.Close[0])
    s = sell(b[1], df.tail(1).Close, b[0])
    print('Buy and Hold: ', s)
    return