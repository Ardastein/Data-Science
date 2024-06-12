from data_loading import load_data, preprocess_data
from data_analysis import plot_histogram, plot_bar, plot_scatter, plot_box

file_path = 'C:/Users/HP/Desktop/Missions/Huawei/Economics/Exploring E-commerce Trends/data/ecommerce_product_dataset.csv'

data = load_data(file_path)

if data is not None:
    data = preprocess_data(data)

    print(data.info())
    print(data.describe())

    plot_histogram(data, column='Price', title='Price Distribution', xlabel='Price', ylabel='Frequency')

    plot_bar(data, column='Category', title='Product Category Distribution', xlabel='Category', ylabel='Count')

    plot_scatter(data, x_col='Price', y_col='Rating', title='Price vs Rating', xlabel='Price', ylabel='Rating')

    plot_box(data, column='Price', title='Box Plot of Prices', xlabel='Price', ylabel='Frequency')
