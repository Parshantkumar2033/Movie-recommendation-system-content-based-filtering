import model 
import model_dispatcher
import config
import warnings

import pickle as pkl
from collections import Counter
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')

# steming the vectors 
def stemm(text):
    stemmer = model_dispatcher.models['porterStemmer']
    y = []
    for i in text.split():
        y.append(stemmer.stem(i))
    return " ".join(y)

    
# using Bag of words
def run(movie_dataset_location, credit_dataset_location):
    data = model.Data(credit_dataset_location, movie_dataset_location)
    df = data.data_preparation()

    cVec = model_dispatcher.models['cVec']
    vectors = cVec.fit_transform(df['tags']).toarray()   # created vectors using CountVectorizer

    df['tags'] = df['tags'].apply(stemm)

    similarityMatrix = cosine_similarity(vectors)

    return similarityMatrix, df

if __name__ == "__main__":
    movie_dataset_location = config.TRAININGFILE_MOVIE
    credit_dataset_location = config.TRAININGFILE_CREDIT

    similarityMatrix, df = run(movie_dataset_location, credit_dataset_location)

    # saving the model
    pkl.dump(df.to_dict(), open(config.MOVIES_PKL, 'wb'))
    pkl.dump(similarityMatrix, open(config.SIMILARITY_PKL, 'wb'))
    