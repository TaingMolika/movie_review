from feature_engineering import MovieBaseRecommender
from filter_recommeder import CollaborativeFilteringRecommender
import pandas as pd

class HybridRecommender:
    def __init__(self, content_weight=0.3, collaborative_weight=0.7):
        self.content_recommender = MovieBaseRecommender()
        self.cf_recommender = CollaborativeFilteringRecommender()
        self.content_weight = content_weight
        self.collaborative_weight = collaborative_weight

    def fit(self, movies_df, ratings_df):
        self.content_recommender.fit(movies_df)
        self.cf_recommender.train(ratings_df)

    def recommend(self, user_id=None, movie_title=None, movies_df=None, ratings_df=None, n_recommendations=5):
        if user_id and movies_df is not None and ratings_df is not None:
            cf_recs = self.cf_recommender.recommend_for_user(user_id, movies_df, ratings_df, n_recommendations*2)
    
            if movie_title:
                content_recs = self.content_recommender.recommend(movie_title, n_recommendations*2)
        
                if isinstance(content_recs, pd.DataFrame):
                    combined_movies = set(cf_recs['clean_title'].tolist() + content_recs['clean_title'].tolist())
                else:
                    combined_movies = set(cf_recs['clean_title'].tolist())
        
                return cf_recs.head(n_recommendations)
            else:
                return cf_recs.head(n_recommendations)


        elif movie_title:
            return self.content_recommender.recommend(movie_title, n_recommendations)
        else: 
            return "Please provide either user_id or movie title "