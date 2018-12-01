from __future__ import print_function

# from keras.preprocessing import sequence
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation
# from keras.layers import Embedding
# from keras.layers import LSTM
# from keras.layers import Conv1D, MaxPooling1D
# from keras.datasets import imdb
import pandas as pd
import nltk

# print('Loading data...')
data=pd.read_csv("E:\imdb_master.csv",encoding="ISO-8859-1")

#lemmatization
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_review(review):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(review)]


df = pd.DataFrame(data, columns=['review'])
df['text_lemmatized'] = df.review.apply(lemmatize_review)
print(df['text_lemmatized'])

# stop_words
from nltk.corpus import stopwords

stop = stopwords.words('english')
df = pd.DataFrame(data, columns=['review'])

data['text_without_stopwords'] = data['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
print(data['text_without_stopwords'])

#lower case

import pandas as pd
import numpy as np
df=pd.DataFrame(data,columns=['review'])
xSecureLower = data['review'].astype(str).str.lower()
xLower = data['review'].str.lower()
print(xLower)