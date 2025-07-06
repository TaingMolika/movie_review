from feature_engineering import MovieBaseRecommender
from filter_recommeder import CollaborativeFilteringRecommender
from hybrid_recommender import HybridRecommender
from generate_data.load_data import loader
from processor import preprocess_data

class MovieRecommendationSystem:
    def __init__(self):
        self.content_recommender = MovieBaseRecommender()
        self.cf_recommender = CollaborativeFilteringRecommender()
        self.hybrid_recommender = HybridRecommender()
        self.movies_df = None
        self.ratings_df = None
        self.users_df = None

    def load_data(self):
        """Load and preprocess all data"""
        print("Loading data...")
        self.ratings_df, self.movies_df, self.users_df = loader()
        self.ratings_df, self.movies_df, self.users_df = preprocess_data(
            self.ratings_df, self.movies_df, self.users_df
        )
        print("Data loaded successfully!")



#     def train_models(self):
#         """Train all recommendation models"""
#         print("Training models...")
#         self.content_recommender.fit(self.movies_df)
#         self.cf_recommender.train(self.ratings_df)
#         self.hybrid_recommender.fit(self.movies_df, self.ratings_df)
#         print("Models trained successfully!")

#     def get_recommendations(self, method='hybrid', user_id=None, movie_title=None, n_recs=5):
#         """Get recommendations using specified method"""
        
#         if method == 'content' and movie_title:
#             return self.content_recommender.recommend(movie_title, n_recs)
#         elif method == 'collaborative' and user_id:
#             return self.cf_recommender.recommend_for_user(
#                 user_id, self.movies_df, self.ratings_df, n_recs
#             )
#         elif method == 'hybrid':
#             return self.hybrid_recommender.recommend(
#                 user_id, movie_title, self.movies_df, self.ratings_df, n_recs
#             )
#         else:
#             return "Invalid method or missing parameters"

#     def get_movie_info(self, movie_title):
#         """Get information about a specific movie"""
#         movie_info = self.movies_df[self.movies_df['clean_title'].str.contains(movie_title, case=False)]
#         return movie_info[['clean_title', 'genres', 'year']].head()

#     def get_user_profile(self, user_id):
#         """Get user's rating history and preferences"""
#         user_ratings = self.ratings_df[self.ratings_df['user_id'] == user_id].merge(
#             self.movies_df[['movie_id', 'clean_title', 'genres']], on='movie_id'
#         )
        
#         # User statistics
#         stats = {
#             'total_ratings': len(user_ratings),
#             'average_rating': user_ratings['rating'].mean(),
#             'favorite_genres': self._get_favorite_genres(user_ratings),
#             'top_rated_movies': user_ratings.nlargest(5, 'rating')[['clean_title', 'rating']].to_dict('records')
#         }
        
#         return stats

#     def _get_favorite_genres(self, user_ratings):
#         """Helper function to find user's favorite genres"""
#         genre_counts = {}
#         for genres in user_ratings['genres']:
#             for genre in genres:
#                 genre_counts[genre] = genre_counts.get(genre, 0) + 1
        
#         return sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:5]

# # Usage example
# def main():

#     # Initialize system
#     rec_system = MovieRecommendationSystem()
    
#     # Load and train
#     rec_system.load_data()
#     rec_system.train_models()
    
#     # Example recommendations
#     print("=== CONTENT-BASED RECOMMENDATIONS ===")
#     content_recs = rec_system.get_recommendations('content', movie_title='Toy Story')
#     print(content_recs)
    
#     print("\n=== COLLABORATIVE FILTERING RECOMMENDATIONS ===")
#     cf_recs = rec_system.get_recommendations('collaborative', user_id=1)
#     print(cf_recs)
    
#     print("\n=== HYBRID RECOMMENDATIONS ===")
#     hybrid_recs = rec_system.get_recommendations('hybrid', user_id=1, movie_title='Toy Story')
#     print(hybrid_recs)
    
#     print("\n=== USER PROFILE ===")
#     user_profile = rec_system.get_user_profile(1)
#     print(f"User 1 Profile: {user_profile}")

# if __name__ == "__main__":
#     main()