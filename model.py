import ast
import pandas as pd
import numpy as np

class Data:
    def __init__(self, credits, movies): # pass the path to these datasets
        self.credits = credits
        self.movies = movies
    def convert(self, obj, column):
        L = []
        if column not in ['genres', 'cast', 'crew']:
            raise ValueError("No such column present")
        
        if column == 'genres':
            for i in ast.literal_eval(obj):
                L.append(i['name'])

        if column == 'cast':
            cnt = 0
            for i in ast.literal_eval(obj):
                if cnt == 3:
                    break
                else:
                    L.append(i['name'])
                    cnt += 1

        if column == 'crew':
            for i in ast.literal_eval(obj):
                if i['job'] == 'Director':
                    L.append(i['name'])
        return L
    
    def data_preparation(self):
        credits = pd.read_csv(self.credits)
        credit = credits.copy(deep = True)

        movies = pd.read_csv(self.movies)
        movie = movies.copy(deep = True)

        temp = movie.merge(credit, on = 'title')
        movie = temp[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

        movie.dropna(inplace = True)

        # conveting columns
        movie['genres'] = movie['genres'].apply(lambda x : self.convert(x, column = 'genres'))
        movie['cast'] = movie['cast'].apply(lambda x : self.convert(x, column = 'cast'))
        movie['crew'] = movie['crew'].apply(lambda x : self.convert(x, column = 'crew'))

        movie['overview'] = movie['overview'].apply(lambda x : x.split())

        movie['genres'] = movie['genres'].apply(lambda x : [i.replace(" ", "") for i in x])
        movie['keywords'] = movie['keywords'].apply(lambda x : [i.replace(" ", "") for i in x])
        movie['cast'] = movie['cast'].apply(lambda x : [i.replace(" ", "") for i in x])
        movie['crew'] = movie['crew'].apply(lambda x : [i.replace(" ", "") for i in x])

        # Creating tags feature using overview, cast, genres, crew
        movie['tags'] = movie.overview + movie.cast + movie.crew + movie.genres

        df = movie[['movie_id', 'title', 'tags']]
        df['tags'] = df['tags'].apply(lambda x : " ".join(x))

        df['tags'] = df['tags'].apply(lambda x : x.lower())
        
        return df
