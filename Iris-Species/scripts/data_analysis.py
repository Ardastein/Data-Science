import pandas as pd

file_path = 'data/Iris.csv'
df = pd.read_csv(file_path)

print(df.info())
print(df.describe())
print(df.head())
