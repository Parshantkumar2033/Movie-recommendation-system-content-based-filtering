
# **Movie-recommendation-system-content-based-filtering**

## **Description**

This project is a **Movie Recommendation System** built using **content-based** filtering techniques. It recommends movies based on the similarity of their features (such as *genres*, *keywords*, *cast*, and *crew*) to a user-selected movie. The system is designed to help users discover movies that match their preferences based on a movie they already like.  


The dataset used in this project was sourced from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), and it contains detailed information about movies such as titles, genres, cast, and more.


## Tech Stack

The recommendation engine is implemented using Python and the following technologies:

- **Streamlit**: For creating an interactive web interface where users can input a movie title and view the recommended movies.
- **NLTK**(Natural Language Tool Kit): For text processing and feature extraction from movie descriptions.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations and handling multi-dimensional arrays.
- **Scikit-learn**: For implementing content-based filtering and **cosine similarity**.


## Detailed Working
**Data preparation**: There are two datasets which are grouped together on "title" feature and several  features are removed from the dataset, left with (movie_id, title, overview, genres, keywords, cast and crew).
Cleaning of the data, and for feature-extraction [CountVectorizer()](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) is used to pick 5000 tags which will be used to find the similarity (using [cosine_similarity()](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)).


Furthermore, [steming](https://www.nltk.org/api/nltk.stem.porter.html) is used to remove redundancy from the tags.

Using *bag-of-word* to get the Term-Frequency.

Using **Streamlit** to create a web interface in which user can select a movie which he/she has watched in history and he/she can get Recommendations based on this movie. In total, 9 Movies are recommended based on the cosine similarity. The top 9 valued movies fetched.


## **Demo**




![Movie, you have watched](demo_pictures/Screenshot%20(7435).png)
![Recommended Movies](demo_pictures/Screenshot%20(7437).png)


## **Installation**


Follow these steps to set up the Movie Recommendation System on your local machine.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Creating Virtual environment
It's recommended to create a virtual environment to manage dependencies:
```bash
python -m venv env-name
```

### Activating Virtual environment:

### Windows
```bash
./env-name/Scripts/activate
```
### macOS/Linux
```bash
source env-name/bin/activate
```

### 3. Install dependencies
Install all the required packages using **pip** and the **requirement.txt** file:
```bash
pip install -r requirement.txt
```
This provides a comprehensive guide for users to set up your project correctly on their local machines. Adjust the directory paths and any other specific details based on your actual project setup.
## **How to use**
After cloning the repository,


- Download the datasets from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and keep them in **/inputs/** folder.

    Update the **src/config.py**

        TRAININGFILE_CREDIT = "Path to credits dataset"
        TRAININGFILE_MOVIE = "Path to movies dataset"

    Similarly update the paths where you want to keep the **.pkl** files generated by the system.
  
        MOVIES_PKL = "path where you want the **Movies.pkl** file to get created"
        SIMILARITY_PKL = "path where you want the **Similarity.pkl** file to get created"
    It is advised to keep the **Movies.pkl** and **Similarity.pkl** in the **/inputs/** folder.

    **API key**
        
    Register on [TMDB](https://www.themoviedb.org/) to generate your API key.
        
        Go to profile > setting > API

    Use the obtained key in place of **<YOUR-API-KEY>**

        APIREQUEST = "https://api.themoviedb.org/3/movie/{}?api_key=<YOUR-API-KEY>"

- Open a terminal in the project folder and activate **Virtural-environment** using 

        ./env-name/Scripts/activate
    traverse to the **/src** directory and run the command

        python train.py       

    After the execution of train.py

        streamlit run app.py

- Some links will appear in the terminal like

        Local URL: http://localhost:8500
        Network URL: http://10.1.***.***:8500
        External URL: http://14.139.***.***:8500

- Upon clicking you will be directed to browser.
## **Datasets**

### 1. Dataset Source

- **Name**: tmdb_5000_credits and tmdb_5000_movies
- **Source**: [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Description**: This dataset contains metadata for over 5,000 movies, including details such as titles, genres, cast, etc.

### 2. Dataset Structure

- **Movies dataset**:
    + **budget**: The budget of the movie.
    + **genres**: The genre(s) associated with the movie.
    + **homepage**: The official website of the movie.
    + **id**: The unique identifier for the movie.
    + **keywords**: Keywords describing the main themes or elements of the movie.
    + **original_language**: The original language in which the movie was released.
    + **original_title**: The original title of the movie.
    + **overview**: A brief summary or description of the movie's plot.
    + **popularity**: A popularity score assigned to the movie.
    + **production_companies**: The companies involved in the production of the movie.
    + **production_countries**: The countries where the movie was produced.
    + **release_date**: The date when the movie was released.
    + **revenue**: The total revenue generated by the movie.
    + **runtime**: The duration of the movie in minutes.
    + **spoken_languages**: The languages spoken in the movie.
    + **status**: The release status of the movie (e.g., Released, Post Production).
    + **tagline**: A short promotional phrase or tagline for the movie.
    + **title**: The title of the movie.
    + **vote_average**: The average rating the movie received.
    + **vote_count**: The number of votes the movie received.

- **Credits dataset**:
    - **movie_id**: The unique identifier for the movie.
    - **title**: The title of the movie.
    - **cast**: A list of the main actors in the movie.
    - **crew**: A list of key crew members involved in the movie, such as directors and producers.

### 3. Preprocessing

- **Steps Taken**:
  - Removed rows with missing values in crucial columns like `title` and `overview`.
  - Converted all text data to lowercase for consistency.
  - Extracted tags from the columns using NLTK.

- **Tools Used**:
  - **Pandas**: For data manipulation.
  - **NLTK**: For text processing and keyword extraction.


## **Project Structure**

### **Explanation**

- **inputs/**: Contains dataset files required for the project.
  - **movies_dataset**
  - **credits_dataset**
  - Keep the **.pkl** files, generated from the model training.
- **notebooks/**:
  - **raw_model.ipynb**: Notebook for initial model experiments and development.
- **src/**: Contains the source code for the project.
  - **app.py**: The main script for running the application.
  - **train.py**: Script to train the recommendation model.
  - **models.py**: Defines the recommendation models and their functions.
  - **config.py**: Configuration file with settings for the project.
  - **model_dispatcher.py**: Manages model selection and dispatching.
- **requirements.txt**: Lists all Python dependencies required for the project.

## **Features**

- **Content-based filtering.**
- **Cosine-similarity.**
- **Displays movie titles along with thumbnails.**
- **Recommend Most Related Movies.**

