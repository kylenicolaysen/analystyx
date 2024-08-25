from price_files import file_dict
from calculations import *
from signals import *
from backtest import backtest

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def read_file(ticker):
    df = pd.read_csv(file_dict[ticker])
    df = df.drop(['Adj Close'], axis=1)
    splitted = df['Date'].str.split('-', expand=True)
    df['Year'] = splitted[0].astype('int')
    df['Month'] = splitted[1].astype('int')
    df['Day'] = splitted[2].astype('int')
    df['26 EMA'] = calculate_ema(df['Close'], 26)
    df['12 EMA'] = calculate_ema(df['Close'], 12)
    df['MACD'] = df['12 EMA'] - df['26 EMA']
    df['MACD Signal'] = calculate_ema(df['MACD'], 9)
    df['Histogram'] = df['MACD'] - df['MACD Signal']
    df['200 SMA'] = calculate_sma(df['Close'], 200)
    return df

def get_info():
    print('HEAD', df.head())
    print('SHAPE', df.shape)
    print('DESCRIBE', df.describe())
    print('INFO', df.info())
    print(df.isnull().sum())

# DAILY CLOSE PRICES GRAPH:
def gen_daily_price_graph():
    plt.figure(figsize=(15,5))
    plt.plot(df['Close'])
    plt.title('S&P500 Close price.', fontsize=15)
    plt.ylabel('Price in dollars.')
    plt.show()

# DISTRIBUTION PLOT:
def gen_distribution_plot():
    plt.subplots(figsize=(20,10))
    for i, col in enumerate([1, 2, 3]):
      plt.subplot(2,3,i+1)
      sb.distplot(df['Volume'])
    plt.show()

if __name__ == '__main__':
    # ticker = input('Enter Ticker: ')
    ticker = 'SPY'
    df = read_file(ticker)
    # signals = macd_histogram_trend_reversal_signal(df['Histogram'])
    signals = two_hundred_sma_signal(df['Close'], df['200 SMA'])
    # print(signals)
    backtest(df, signals)
    # x = calculate_sma([2,4,2,4,2,4,2,4,5,6,7,8,9,10], 3)
    # print(x)