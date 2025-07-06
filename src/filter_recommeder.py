from surprise import Dataset, Reader, SVD, KNNBasic
from surprise.model_selection import cross_validate, train_test_split
from surprise import accuracy

class CollaborativeFilteringRecommender:

    def __init__ (self, algorithm='SVD'):
        self.algorithm = algorithm
        self.model = None
        self.trainset = None

    def prepare_data (self, ratings_df):
        reader = Reader(rating_scale= (1, 5))
        data = Dataset.load_from_df(ratings_df[['user_id', 'movie_id', 'rating']],
        reader)
        return data

    def train(self, ratings_df):
        data = self.prepare_data(ratings_df)
        self.trainset = data.build_full_trainset()
        if self.algorithm == 'SVD':
            self.model = SVD(n_factors=100, n_epochs=20, lr_all=0.005, reg_all=0.02)
        elif self.algorithm == 'KNN':
            self.model = KNNBasic(sim_options={'name': 'cosine', 'user_based':True})
        self.model.fit(self.trainset)

    def predict_rating(self, user_id, movie_id):
        prediction = self.model.predict(user_id, movie_id)
        return prediction.est

    def recommend_for_user(self, user_id, movies_df, ratings_df, n_recommendations=10):
        user_ratings = ratings_df[ratings_df['user_id'] == user_id]['movie_id'].tolist()  # FIXED
        all_movies = movies_df['movie_id'].tolist()
        unrated_movies = [movie for movie in all_movies if movie not in user_ratings]

        predictions = []
        for movie_id in unrated_movies:
            pred_rating = self.predict_rating(user_id, movie_id)
            predictions.append((movie_id, pred_rating))

        predictions.sort(key=lambda x: x[1], reverse=True)
        top_movie_ids = [pred[0] for pred in predictions[:n_recommendations]]
        recommendations = movies_df[movies_df['movie_id'].isin(top_movie_ids)].copy()
        recommendations['predicted_rating'] = [pred[1] for pred in predictions[:n_recommendations]]
        return recommendations[['clean_title', 'genres', 'predicted_rating']]



