import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

os.makedirs('outputs', exist_ok=True)

data_path = 'data/niv.csv'
df = pd.read_csv(data_path)

print("First few rows of the dataset:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

if not pd.api.types.is_datetime64_any_dtype(df['Date']):
    df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

df.sort_index(inplace=True)

plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price')
plt.title('NVIDIA Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()
plt.savefig('outputs/close_price_over_time.png')
plt.show()

df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['MA50'], label='50-Day Moving Average')
plt.plot(df['MA200'], label='200-Day Moving Average')
plt.title('NVIDIA Stock Prices with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()
plt.savefig('outputs/moving_averages.png')
plt.show()

plt.figure(figsize=(14, 7))
plt.bar(df.index, df['Volume'], width=1.0, label='Volume')
plt.title('Volume Traded Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.savefig('outputs/volume_traded.png')
plt.show()

df['Daily Return'] = df['Close'].pct_change()
df['Cumulative Return'] = (1 + df['Daily Return']).cumprod() - 1

plt.figure(figsize=(14, 7))
plt.plot(df['Daily Return'], label='Daily Return')
plt.title('NVIDIA Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.savefig('outputs/daily_returns.png')
plt.show()

plt.figure(figsize=(14, 7))
plt.plot(df['Cumulative Return'], label='Cumulative Return')
plt.title('NVIDIA Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.savefig('outputs/cumulative_returns.png')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('outputs/correlation_heatmap.png')
plt.show()

print("Analysis and visualization complete. Check the 'outputs' directory for generated plots.")
