import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def preprocess_data(ratings, movies, users):

    ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

    movies['year'] = (
    movies['title']
      .str.extract(r'\((\d{4})\)', expand=False)
      .astype('Int64')  
    )

    movies['clean_title'] = movies['title'].str.replace(r'\s*\(\d{4}\)', '', regex=True)

    genre_columns = [
        'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
        'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'
    ]

    movies['genres'] = movies[genre_columns].apply(
        lambda x: [genre for genre, val in zip(genre_columns, x) if val == 1],
        axis=1
    )

    movie_ratings = ratings.merge(
        movies[['movie_id', 'clean_title', 'genres', 'year']],
        on='movie_id'
    )

    return ratings, movies, users, movie_ratings