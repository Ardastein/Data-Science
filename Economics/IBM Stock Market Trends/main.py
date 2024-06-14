import os
from scripts.data_processing import load_data, preprocess_data
from scripts.analysis import plot_stock_prices, plot_moving_averages, plot_volume, plot_volatility

data_file = 'data/ibm_stock_data.csv'

if not os.path.exists('outputs/figures'):
    os.makedirs('outputs/figures')

df = load_data(data_file)
df = preprocess_data(df)

plot_stock_prices(df)
plot_moving_averages(df, window=50)
plot_moving_averages(df, window=200)
plot_volume(df)
plot_volatility(df)
