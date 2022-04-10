import nltk
import pandas as pd
import string
import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk import tokenize
paragraph = 'I like to PLay play football. ' \
            'Did you go outside to play Tennis? ' \
            'John and i play Tennis.'


cv = CountVectorizer()
sentences = tokenize.sent_tokenize(paragraph)
print(sentences)
X = cv.fit(sentences)
X = cv.transform(sentences)
df = pd.DataFrame(X.toarray(), columns=cv.get_feature_names_out())
print(df)
