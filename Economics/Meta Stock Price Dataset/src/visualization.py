import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_time_series(df, column):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df[column], label=column)
    plt.title(f'{column} Over Time')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.legend()
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

def plot_moving_averages(df, column, windows=[10, 20, 50]):
    plt.figure(figsize=(14, 7))
    for window in windows:
        df[f'MA_{window}'] = df[column].rolling(window=window).mean()
        plt.plot(df.index, df[f'MA_{window}'], label=f'MA_{window}')
    
    plt.plot(df.index, df[column], label=column, alpha=0.5)
    plt.title(f'Moving Averages for {column}')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    file_path = 'data/Meta.csv'
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    plot_time_series(df, 'Close')
    plot_correlation_matrix(df)
    plot_moving_averages(df, 'Close')
