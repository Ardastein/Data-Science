import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_price_distribution(df):
    """ Plot the distribution of real estate prices. """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title('Distribution of Real Estate Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

def plot_price_by_region(df):
    """ Plot the average price by region. """
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Region', y='price', data=df, estimator=sum)
    plt.title('Average Price by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    plt.show()

def plot_price_trends(df):
    """ Plot the trend of prices over time if the date columns exist. """
    if 'Year' in df.columns and 'Month' in df.columns:
        try:
            df['date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
            df.set_index('date', inplace=True)
            plt.figure(figsize=(14, 7))
            df['price'].plot()
            plt.title('Real Estate Price Trends Over Time')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.show()
        except Exception as e:
            print(f"Error converting to date: {e}")
    else:
        print("Year or Month columns not found to plot trends.")
