import unittest
from src.data_loader import load_data, preprocess_data
from src.recommender import build_similarity_matrix, recommend_movies

class TestRecommender(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        credits_path = 'data/tmdb_5000_credits.csv'
        movies_path = 'data/tmdb_5000_movies.csv'
        cls.credits_df, cls.movies_df = load_data(credits_path, movies_path)
        cls.movies_df = preprocess_data(cls.movies_df)
        cls.cosine_sim = build_similarity_matrix(cls.movies_df)

    def test_recommend_movies(self):
        recommendations = recommend_movies('The Dark Knight', self.movies_df, self.cosine_sim)
        self.assertTrue(len(recommendations) > 0)
        self.assertIn('The Dark Knight Rises', recommendations)

if __name__ == '__main__':
    unittest.main()
