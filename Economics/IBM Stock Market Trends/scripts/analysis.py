import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_prices(df):
    """Plot stock prices over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.title('IBM Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.savefig('outputs/figures/stock_prices.png')
    plt.show()

def plot_moving_averages(df, window=50):
    """Plot moving averages of the stock prices."""
    df[f'MA{window}'] = df['Close'].rolling(window=window).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df[f'MA{window}'], label=f'{window}-Day Moving Average')
    plt.title(f'IBM Stock Closing Prices and {window}-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'outputs/figures/moving_average_{window}.png')
    plt.show()

def plot_volume(df):
    """Plot trading volume over time."""
    plt.figure(figsize=(12, 6))
    plt.bar(df.index, df['Volume'], width=1)
    plt.title('IBM Stock Trading Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.savefig('outputs/figures/volume.png')
    plt.show()

def plot_volatility(df):
    """Plot stock price volatility."""
    df['Returns'] = df['Close'].pct_change()
    df['Volatility'] = df['Returns'].rolling(window=30).std()
    plt.figure(figsize=(12, 6))
    plt.plot(df['Volatility'], label='30-Day Volatility')
    plt.title('IBM Stock Price Volatility')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.grid(True)
    plt.savefig('outputs/figures/volatility.png')
    plt.show()
