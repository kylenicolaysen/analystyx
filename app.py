import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def calculate_ema_gpt(prices, days):
    # Calculate the Exponential Moving Average (EMA) for a given list of prices.
    # -param prices: List of prices (floats)
    # -param days: Number of days for the EMA
    # -return: List of EMA values

    # Calculate the smoothing factor (alpha)
    alpha = 2 / (days + 1)
    # Initialize the EMA list with the first price
    ema = [prices[0]]
    # Calculate the EMA for each subsequent price
    for price in prices[1:]:
        ema.append((price - ema[-1]) * alpha + ema[-1])
    return ema

df = pd.read_csv('/home/usr1/Downloads/SPY(1).csv')
df = df.drop(['Adj Close'], axis=1)
splitted = df['Date'].str.split('-', expand=True)
df['Year'] = splitted[0].astype('int')
df['Month'] = splitted[1].astype('int')
df['Day'] = splitted[2].astype('int')
df['26 EMA'] = calculate_ema_gpt(df['Close'], 26)
df['12 EMA'] = calculate_ema_gpt(df['Close'], 12)
df['9 EMA'] = calculate_ema_gpt(df['Close'], 9)
df['MACD'] = df['12 EMA'] - df['26 EMA']
# df['histogram']
# numeric_df = df.select_dtypes(include=['number'])
# numeric_df['open-close']  = numeric_df['Open'] - numeric_df['Close'] 
# numeric_df['low-high']  = numeric_df['Low'] - numeric_df['High'] 

def get_info():
    print('HEAD', df.head())
    print('SHAPE', df.shape)
    print('DESCRIBE', df.describe())
    print('INFO', df.info())
    print(df.isnull().sum())
features = ['Open', 'High', 'Low', 'Close', 'Volume'] 

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
    for i, col in enumerate(features):
      plt.subplot(2,3,i+1)
      sb.distplot(df[col])
    plt.show()

gen_daily_price_graph()
print(df['MACD'])