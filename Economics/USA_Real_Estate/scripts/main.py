from data_processing import load_data, clean_data, summarize_data
from visualization import plot_price_distribution, plot_price_by_region, plot_price_trends

file_path = 'data/RealEstateUnitedStates.csv'
df = load_data(file_path)

df = clean_data(df)

summary = summarize_data(df)
print(summary)

plot_price_distribution(df)

plot_price_by_region(df)

plot_price_trends(df)
