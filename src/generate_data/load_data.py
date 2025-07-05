import pandas as pd

def loader(rating_path, movie_path, user_path):
    ratings = pd.read_csv(rating_path, 
                        sep="\t", 
                        names=["user_id", "movie_id", "rating", "timestamp"])

    
    movie_cols = [
        "movie_id", "title", "release_date", "video_release_date", "imdb_url",
        "unknown", "Action", "Adventure", "Animation", "Children", "Comedy",
        "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
        "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
    ]

    movies = pd.read_csv(
        movie_path,
        sep="|",               
        names=movie_cols,           
        encoding="latin-1"      
    )

    users = pd.read_csv(
        user_path, 
        sep="|", 
        names=["user_id", "age", "gender", "occupation", "zip_code"]
    )

    return ratings, movies, users

# rating_path = "data/raw/ml-100k/u.data"
# movie_path = "data/raw/ml-100k/u.item"
# user_path = "data/raw/ml-100k/u.user"
    
# ratings, movies, users = loader(rating_path, movie_path, user_path)

# print("Rating Info")
# print(ratings.info)
# print("Movie Info")
# print(movies.info)
# print("User Info")
# print(users.info)