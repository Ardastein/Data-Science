import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'C:\\Users\\HP\\Desktop\\Missions\\Huawei\\Economics\\Best-Selling Music Artists\\data\\best.csv'
df = pd.read_csv(data_path)

print("Column names in the dataset:")
print(df.columns)

df.columns = df.columns.str.strip()

print("\nUpdated column names after stripping spaces:")
print(df.columns)

print("\nFirst few rows of the dataset:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

df['Total certified units'] = df['Total certified units'].replace(r'[^0-9]', '', regex=True).astype(float)

print("\nData types after conversion:")
print(df.dtypes)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(df['Total certified units'], bins=30, kde=True)
plt.title('Distribution of Total Certified Units')
plt.xlabel('Total Certified Units')
plt.ylabel('Frequency')
plt.show()

top_artists = df.nlargest(10, 'Total certified units')
plt.figure(figsize=(12, 8))
sns.barplot(x='Total certified units', y='Artist name', hue='Artist name', data=top_artists, palette='viridis', dodge=False, legend=False)
plt.title('Top 10 Artists by Total Certified Units')
plt.xlabel('Total Certified Units (millions)')
plt.ylabel('Artist')
plt.show()

if 'Release year of first charted record' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Release year of first charted record', y='Total certified units', data=df)
    plt.title('Certified Sales Trends Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Certified Units (millions)')
    plt.show()

if 'Genre' in df.columns:
    plt.figure(figsize=(14, 7))
    genre_sales = df.groupby('Genre')['Total certified units'].sum().reset_index().sort_values(by='Total certified units', ascending=False)
    sns.barplot(x='Total certified units', y='Genre', hue='Genre', data=genre_sales, palette='coolwarm', dodge=False, legend=False)
    plt.title('Certified Sales by Genre')
    plt.xlabel('Total Certified Units (millions)')
    plt.ylabel('Genre')
    plt.show()

print("Analysis completed successfully.")
