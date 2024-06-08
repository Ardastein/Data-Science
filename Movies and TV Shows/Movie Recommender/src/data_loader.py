# src/data_loader.py

import pandas as pd

def load_data(credits_path: str, movies_path: str):
    credits = pd.read_csv(credits_path)
    movies = pd.read_csv(movies_path)
    return credits, movies

def preprocess_data(movies_df, credits_df):
    # Merge the movies and credits dataframes on 'id'
    credits_df.rename(columns={'movie_id': 'id'}, inplace=True)
    movies_df = movies_df.merge(credits_df[['id', 'cast', 'crew']], on='id')
    
    # Fill missing values
    movies_df = movies_df.fillna('')

    # Extract director from crew
    def get_director(crew):
        for member in eval(crew):
            if member['job'] == 'Director':
                return member['name']
        return ''
    
    movies_df['director'] = movies_df['crew'].apply(get_director)

    # Extract relevant features
    movies_df['genres'] = movies_df['genres'].apply(lambda x: ' '.join([i['name'] for i in eval(x)]))
    movies_df['keywords'] = movies_df['keywords'].apply(lambda x: ' '.join([i['name'] for i in eval(x)]))
    movies_df['cast'] = movies_df['cast'].apply(lambda x: ' '.join([i['name'] for i in eval(x)][:5]))  # top 5 cast members

    return movies_df
