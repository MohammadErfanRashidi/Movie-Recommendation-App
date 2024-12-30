# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset from GitHub
@st.cache(allow_output_mutation=True)
def load_data():
    # Replace this URL with the raw GitHub link to your dataset
    url = "https://raw.githubusercontent.com/MohammadErfanRashidi/Movie-Recommendation-App/refs/heads/main/movies%20(1).csv"
    dataset = pd.read_csv(url)
    return dataset

# Preprocess the dataset
@st.cache(allow_output_mutation=True)
def preprocess_data(dataset):
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

    # Fill null values
    for feature in selected_features:
        dataset[feature] = dataset[feature].fillna('')

    # Combine the features into a single string
    dataset['combined_features'] = (
        dataset['genres'] + ' ' +
        dataset['keywords'] + ' ' +
        dataset['tagline'] + ' ' +
        dataset['cast'] + ' ' +
        dataset['director']
    )

    # Generate feature vectors using TF-IDF
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(dataset['combined_features'])

    # Compute similarity matrix
    similarity = cosine_similarity(feature_vectors)
    return dataset, similarity

# Recommend movies
def recommend_movies(movie_name, dataset, similarity):
    list_of_all_titles = dataset['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        return []

    close_match = find_close_match[0]
    index_of_the_movie = dataset[dataset.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i, movie in enumerate(sorted_similar_movies[1:30], start=1):  # Skip the first (it’s the input movie itself)
        index = movie[0]
        title_from_index = dataset[dataset.index == index]['title'].values[0]
        recommended_movies.append(title_from_index)

    return recommended_movies

# Main Streamlit app
def main():
    st.title("Movie Recommendation System 🎥")
    st.markdown("Enter your favorite movie, and we'll recommend similar movies!")

    # Load and preprocess data
    dataset = load_data()
    dataset, similarity = preprocess_data(dataset)

    # User input
    movie_name = st.text_input("Enter a movie title:")

    if st.button("Recommend"):
        if movie_name:
            recommendations = recommend_movies(movie_name, dataset, similarity)

            if recommendations:
                st.subheader(f"Movies recommended based on '{movie_name}':")
                for i, movie in enumerate(recommendations, start=1):
                    st.write(f"{i}. {movie}")
            else:
                st.error("Sorry, no close matches found. Please try another movie!")
        else:
            st.warning("Please enter a movie title.")

# Run the app
if __name__ == "__main__":
    main()
