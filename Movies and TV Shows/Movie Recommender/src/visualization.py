import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_genre_distribution(movies_df):
    genre_data = movies_df['genres'].str.split().explode()
    
    genre_counts = genre_data.value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']

    plt.figure(figsize=(12, 6))
    sns.barplot(y='genre', x='count', data=genre_counts, palette="viridis", hue='genre', dodge=False, legend=False)
    plt.title('Distribution of Movie Genres')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.show()

def plot_movie_length_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['runtime'], bins=30, kde=True, color='blue')
    plt.title('Distribution of Movie Lengths')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('Frequency')
    plt.show()

def plot_movies_per_year(movies_df):
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
    movies_df['year'] = movies_df['release_date'].dt.year.dropna().astype(int)
    movies_per_year = movies_df['year'].value_counts().reset_index()
    movies_per_year.columns = ['year', 'count']

    plt.figure(figsize=(14, 8))
    sns.countplot(x='year', data=movies_per_year, order=movies_per_year['year'], palette="magma", hue='year', dodge=False, legend=False)
    plt.title('Number of Movies Released Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=90)
    plt.show()
