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
    df['26 EMA'] = calculate_ema_gpt(df['Close'], 26)
    df['12 EMA'] = calculate_ema_gpt(df['Close'], 12)
    df['MACD'] = df['12 EMA'] - df['26 EMA']
    df['Signal'] = calculate_ema_gpt(df['MACD'], 9)
    df['Histogram'] = df['MACD'] - df['Signal']
    # numeric_df = df.select_dtypes(include=['number'])
    # numeric_df['open-close']  = numeric_df['Open'] - numeric_df['Close'] 
    # numeric_df['low-high']  = numeric_df['Low'] - numeric_df['High'] 
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
    print('Dataframe: ', df.tail(15))
    signals = macd_histogram_trend_reversal_signal(df['Histogram'].tail(1500))
    print('Signals: ', signals[-15:])
    backtest(df, signals)