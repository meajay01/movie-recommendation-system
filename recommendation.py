import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load movie dataset
movies = pd.read_csv("data/movies.csv")


# Combine genre and description
movies["features"] = (
    movies["genre"].fillna("") + " " +
    movies["description"].fillna("")
)


# Convert text into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(movies["features"])


# Calculate similarity between movies
similarity = cosine_similarity(feature_matrix)


def recommend_movies(movie_title, num_recommendations=5):

    # Find selected movie
    movie_index = movies[
        movies["title"].str.lower() == movie_title.lower()
    ].index

    if len(movie_index) == 0:
        return []

    movie_index = movie_index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    # Sort by highest similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Get recommended movies
    recommendations = []

    for index, score in similarity_scores[1:num_recommendations + 1]:
        recommendations.append({
            "title": movies.iloc[index]["title"],
            "genre": movies.iloc[index]["genre"],
            "score": round(score * 100, 2)
        })

    return recommendations
