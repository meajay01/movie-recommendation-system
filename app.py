from flask import Flask, render_template, request
from recommendation import movies, recommend_movies


app = Flask(__name__)


@app.route("/")
def home():
    movie_titles = movies["title"].tolist()

    return render_template(
        "index.html",
        movies=movie_titles,
        recommendations=None,
        selected_movie=None
    )


@app.route("/recommend", methods=["POST"])
def recommend():

    selected_movie = request.form["movie"]

    recommendations = recommend_movies(
        selected_movie,
        num_recommendations=5
    )

    movie_titles = movies["title"].tolist()

    return render_template(
        "index.html",
        movies=movie_titles,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


if __name__ == "__main__":
    app.run(debug=True)