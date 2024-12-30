# Movie Recommendation System 🎥

This is a Streamlit web application that recommends movies based on a user's favorite movie. It uses a **content-based filtering approach** by analyzing genres, keywords, taglines, cast, and director information from a movie dataset.

---

## Features
- Input your favorite movie and get a list of similar movies.
- Dynamic recommendations using TF-IDF vectorization and cosine similarity.
- Easy-to-use interface powered by Streamlit.

---

## How It Works
1. **Dataset**: The app uses a CSV file containing movie details such as genres, keywords, tagline, cast, and director.
2. **Preprocessing**: Combines selected features into a single text column and converts it into numerical feature vectors using the **TF-IDF Vectorizer**.
3. **Similarity Calculation**: Calculates cosine similarity between movies based on the feature vectors.
4. **Recommendation**: Identifies and lists movies similar to the one input by the user.

---

## Prerequisites
To run this app locally, ensure the following are installed:
- Python 3.8 or higher
- The libraries listed in `requirements.txt`:
  ```
  streamlit
  pandas
  numpy
  scikit-learn
  ```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/MohammadErfanRashidi/Movie-Recommendation-App.git
cd Movie-Recommendation-App
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

### 4. Open the App
After running the above command, open the URL displayed in the terminal (typically `http://localhost:8501/`) in your web browser.

---

## Dataset
The movie dataset is loaded dynamically from the following GitHub URL:
```
https://raw.githubusercontent.com/MohammadErfanRashidi/Movie-Recommendation-App/refs/heads/main/movies%20(1).csv
```
Ensure the dataset is available and accessible from the repository.

---

## How to Use
1. Enter the title of your favorite movie in the input box.
2. Click the **Recommend** button.
3. View a list of recommended movies based on your input.

---

## File Structure
- **app.py**: The main Python script for the Streamlit app.
- **requirements.txt**: Contains the list of dependencies required to run the app.
- **README.md**: Documentation for the app.

---

## Contributing
Feel free to fork this repository, create a feature branch, and submit a pull request for improvements or new features. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

