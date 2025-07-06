# ------------ app.py ------------
import streamlit as st
import pandas as pd

# local imports (update the paths to match your project)
from generate_data.load_data import loader
from processor import preprocess_data
from hybrid_recommender import HybridRecommender   # your code above

# ---------- LOAD + PREP DATA ----------
@st.cache_data(show_spinner="Loading MovieLens…")
def load_data():
    rating_path = "../data/raw/ml-100k/u.data"
    movie_path  = "../data/raw/ml-100k/u.item"
    user_path   = "../data/raw/ml-100k/u.user"
    ratings, movies, users = loader(rating_path, movie_path, user_path)
    return preprocess_data(ratings, movies, users)

ratings, movies, users, movie_ratings = load_data()

# ---------- TRAIN HYBRID MODEL ----------
@st.cache_resource(show_spinner="Training Hybrid model…")
def get_hybrid():
    model = HybridRecommender(content_weight=0.3, collaborative_weight=0.7)
    model.fit(movies, ratings)
    return model

hybrid = get_hybrid()

# ---------- STREAMLIT UI ----------
st.title("Hybrid Movie Recommender")

col1, col2 = st.columns(2)
with col1:
    user_id = st.number_input("User ID (optional)", min_value=1, step=1, value=1)
with col2:
    movie_title = st.text_input("Movie title (clean_title)")

n_recs = st.slider("How many recommendations?", 1, 15, 5)

if st.button("Recommend"):
    # decide which parameters to send
    uid = int(user_id) if user_id else None
    title = movie_title.strip() if movie_title else None

    recs = hybrid.recommend(
        user_id=uid if title or uid else None,
        movie_title=title if title else None,
        movies_df=movies,
        ratings_df=ratings,
        n_recommendations=n_recs,
    )
    st.write(recs)

