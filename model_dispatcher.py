import nltk.stem.porter
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

models = {
    'cVec' : CountVectorizer(max_features= 5000, stop_words= 'english'),
    'porterStemmer' : PorterStemmer()
}