import os
from data_loader import load_data, preprocess_data
from recommender import build_similarity_matrix, recommend_movies
from visualization import plot_genre_distribution, plot_movie_length_distribution, plot_movies_per_year

def main():
    data_dir = 'data'
    credits_path = os.path.join(data_dir, 'tmdb_5000_credits.csv')
    movies_path = os.path.join(data_dir, 'tmdb_5000_movies.csv')

    credits_df, movies_df = load_data(credits_path, movies_path)
    movies_df = preprocess_data(movies_df, credits_df)

    cosine_sim = build_similarity_matrix(movies_df)

    title = 'The Dark Knight'
    recommendations = recommend_movies(title, movies_df, cosine_sim)
    print(f"Movies recommended for '{title}':")
    for movie in recommendations:
        print(movie)

    plot_genre_distribution(movies_df)
    plot_movie_length_distribution(movies_df)
    plot_movies_per_year(movies_df)

if __name__ == '__main__':
    main()
