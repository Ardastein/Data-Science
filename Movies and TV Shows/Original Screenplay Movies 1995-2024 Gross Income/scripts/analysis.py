import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'C:\Users\HP\Desktop\Missions\Huawei\Movies and TV Shows\Original Screenplay Movies 1995-2024 Gross Income\data\mov.csv'
data = pd.read_csv(file_path)

print(data.info())
print(data.head())

data['Released Date'] = pd.to_datetime(data['Released Date'], errors='coerce')

data['Year'] = data['Released Date'].dt.year

data['Gross Income'] = data['Year Gross'].replace(r'[\$,]', '', regex=True).astype(float)
data['Tickets Sold'] = data['Tickets Sold'].replace(r'[,]', '', regex=True).astype(float)

print(data.info())
print(data.head())

plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Gross Income', data=data)
plt.title('Gross Income Over the Years')
plt.xlabel('Year')
plt.ylabel('Gross Income (in millions)')
plt.grid(True)
plt.tight_layout()
plt.savefig('gross_income_over_years.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Gross Income'].dropna(), bins=30, kde=True)
plt.title('Distribution of Gross Income')
plt.xlabel('Gross Income (in millions)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('gross_income_distribution.png')
plt.show()

top_10_movies = data.nlargest(10, 'Gross Income')
print(top_10_movies[['Movie Name', 'Gross Income']])

plt.figure(figsize=(12, 8))
sns.barplot(x='Gross Income', y='Movie Name', data=top_10_movies, palette='viridis')
plt.title('Top 10 Movies by Gross Income')
plt.xlabel('Gross Income (in millions)')
plt.ylabel('Movie Name')
plt.tight_layout()
plt.savefig('top_10_movies_gross_income.png')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(y='Genre', data=data, order=data['Genre'].value_counts().index)
plt.title('Distribution of Movies by Genre')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.tight_layout()
plt.savefig('genre_distribution.png')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='Gross Income', y='Genre', data=data, palette='Set2')
plt.title('Gross Income by Genre')
plt.xlabel('Gross Income (in millions)')
plt.ylabel('Genre')
plt.tight_layout()
plt.savefig('gross_income_by_genre.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=data, order=sorted(data['Year'].dropna().unique()), palette='coolwarm')
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.tight_layout()
plt.savefig('movies_per_year.png')
plt.show()

summary_stats = data.describe()
summary_stats.to_csv('summary_statistics.csv')

print("Summary statistics and visualizations have been generated and saved.")
