# Movie Recommendation System

This project implements a **hybrid movie recommender** that combines collaborative filtering and content-based filtering to provide personalized movie suggestions.

---

## How It Works

- **Collaborative Filtering:**  
  Learns user preferences from past ratings using algorithms like SVD or KNN to recommend movies liked by similar users.

- **Content-Based Filtering:**  
  Analyzes movie features such as genres and titles to suggest movies similar to a given movie.

- **Hybrid Approach:**  
  Combines recommendations from both models for improved accuracy and personalization. Users can get recommendations by providing either a user ID or a movie title.

---

## Features

- Personalized movie recommendations based on user behavior and movie content
- Flexibility to use either or both recommendation strategies
- Easily extendable and customizable
- Built with Python, leveraging libraries such as Surprise and scikit-learn

---

## How to Use

1. Prepare your movie metadata and user rating datasets.
2. Train the hybrid recommender with your data.
3. Get recommendations by passing a user ID or movie title.

---

## Why It’s Useful

- Helps users discover movies they are likely to enjoy
- Enhances user engagement on streaming platforms or movie databases
- Provides a foundation for building more complex recommendation systems

---

## Requirements

- Python 3.7+
- scikit-learn
- Surprise
- pandas
- Streamlit (for deployment)

---

## Deployment

You can deploy this recommender as a web app using Streamlit. Run:

```bash
streamlit run app.py
