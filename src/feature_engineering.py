from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieBaseRecommender:
    def __init__(self):
        self.tfidf = TfidfVectorizer(stop_words = 'english')
        self.cosine = None
        self.movie_df = None

    def fit(self, movie_df):
        self.movie_df = movie_df.copy()

        self.movie_df['content'] = self.movie_df['genres'].apply(
            lambda x: ' '.join(x) if isinstance(x, list) else str(x)
        )

        self.movie_df = self.movie_df[self.movie_df['content'].str.strip().astype(bool)]

        if self.movie_df.empty:
            raise ValueError("No valid movie content to build TF-IDF matrix on.")

        tfidf_matrix = self.tfidf.fit_transform(self.movie_df['content'])

        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


    def recommend(self, movie_title, n_recommend=5):

        try: 
            idx = self.movie_df[self.movie_df['clean_title'] == movie_title].index[0]
        
        except IndexError:
            return f"Movie '{movie_title}' not found in list"

        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)

        movie_indice = [i[0] for i in sim_scores[1:n_recommend+1]]

        recommedations = self.movie_df.iloc[movie_indice][['clean_title', 'genres']].copy()

        recommedations['similarity_score'] = [sim_scores[i+1][1] for i in range (n_recommend)]

        return recommedations.reset_index(drop=True)

