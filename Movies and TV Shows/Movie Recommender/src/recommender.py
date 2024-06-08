# src/recommender.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def combine_features(row):
    return f"{row['genres']} {row['keywords']} {row['tagline']} {row['cast']} {row['director']}"

def build_similarity_matrix(movies_df):
    # Create a combined feature column
    movies_df['combined_features'] = movies_df.apply(combine_features, axis=1)
    # Convert the combined features into a matrix of token counts
    count_matrix = CountVectorizer().fit_transform(movies_df['combined_features'])
    # Compute the cosine similarity matrix
    cosine_sim = cosine_similarity(count_matrix)
    return cosine_sim

def get_movie_index(title, movies_df):
    return movies_df[movies_df['title'] == title].index.values[0]

def recommend_movies(title, movies_df, cosine_sim):
    movie_index = get_movie_index(title, movies_df)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:11]  # Top 10 similar movies
    recommended_titles = [movies_df.iloc[i[0]].title for i in sorted_similar_movies]
    return recommended_titles
