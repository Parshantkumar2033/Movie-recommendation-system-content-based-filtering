import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import requests
import config

api = config.APIREQUEST

similarity = pickle.load(open(config.SIMILARITY_PKL, 'rb'))    

def fetch_poster(movie_id):
    rq = requests.get(api.format(movie_id))
    data = rq.json()
    return 'https://image.tmdb.org/t/p/original/' + data['poster_path']


def recommend(movie):
    recommended_movies = []
    recommended_movies_posters = []

    idx = df[df['title'] == movie].index[0]
    distances = similarity[idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    for i in movies_list:
        movie_id = df.iloc[i[0]].movie_id
        recommended_movies.append(df.iloc[i[0]].title)

        # fetching poster using API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movie_dict = pickle.load(open(config.MOVIES_PKL, 'rb'))
df = pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose a Movie',
    df['title'].values
)

if st.button('Recommend'):
    recommendation, poster = recommend(selected_movie_name)

    cols1 = st.columns(3)
    j = 0
    k = 0
    for i in range(3):
        with cols1[i]:
            st.header(recommendation[i])
            st.image(poster[i])

    cols2 = st.columns(3)
    for i in range(3, 6):
        with cols2[j]:
            st.header(recommendation[i])
            st.image(poster[i])
        j += 1


    cols3 = st.columns(3)
    for i in range(6, 9):
        with cols3[k]:
            st.header(recommendation[i])
            st.image(poster[i])
        k += 1