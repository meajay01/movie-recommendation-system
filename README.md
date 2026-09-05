# 🎬 Movie Recommendation System

A simple content-based movie recommendation system built using Python and Machine Learning.

## 🌐 Live Demo

[Movie Recommendation System](https://YOUR-RENDER-URL.onrender.com)

## 📌 Features

- Select a movie from the list
- Get 5 similar movie recommendations
- Shows similarity score
- Supports Hollywood and Indian movies
- Simple and user-friendly web interface

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS

## 🤖 Machine Learning

This project uses:

- **TF-IDF Vectorization**
- **Cosine Similarity**
- **Content-Based Filtering**

The movie genre and description are combined and converted into numerical vectors using TF-IDF. Cosine similarity is then used to compare movies and find the most similar ones.

## 📂 Project Structure

```text
movie-recommendation-system
│
├── data
│   └── movies.csv
│
├── static
│   └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── recommendation.py
├── requirements.txt
├── README.md
└── .gitignore
