# Importing Required Libraries
import urllib.request
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize
from nltk.stem import LancasterStemmer, SnowballStemmer, WordNetLemmatizer, PorterStemmer
from nltk import pos_tag, ne_chunk, ngrams
import numpy

import nltk

# Download Required Packages using below piece of code
# nltk.download()


# Reading Text from the URL
wikiURL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
openURL = urllib.request.urlopen(wikiURL)

# Assigning Parsed Web Page into a Variable
soup = BeautifulSoup(openURL.read(), "lxml")

# Kill all script and style elements
for script in soup(["script", "style"]):
    # Rip it Off
    script.extract()

# get text
text = soup.body.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = ' '.join(chunk for chunk in chunks if chunk)


# Saving to a Text File
with open('Input.txt', 'w') as text_file:
    text_file.write(str(text.encode("utf-8")))


# Tokenization
"""Sentence Tokenization"""
sentTok = sent_tokenize(text)
f=open("sentence tokenization.txt",'w',encoding="utf-8")
print("Sentence Tokenization : \n", sentTok, file=f)



"""Word Tokenization"""
tokens = [word_tokenize(t) for t in sentTok]
f=open("word tokenization.txt",'w',encoding="utf-8")
print ("Word Tokenization : \n", tokens,file=f)


# Stemming
# 1 -> LancasterStemmer
lStem = LancasterStemmer()

f=open("Lancster stemming.txt",'w',encoding="utf-8")
for tok in tokens:
    print("Lancaster Stemming : \n",lStem.stem(str(tok)),file=f)

# 2 -> SnowBallStemmer
sStem = SnowballStemmer('english')

of=open("snowballstemmer.txt",'w',encoding="utf-8")
for tok in tokens:
    print("SnowBall Stemming : \n",sStem.stem(str(tok)),file=f)

# 3 -> PorterStemmer
pStem = PorterStemmer()

f=open("PorterStemming.txt",'w',encoding="utf-8")
for tok in tokens:
    print("Porter Stemming : \n",pStem.stem(str(tok)),file=f)




# POS
f=open("pos.txt",'w',encoding="utf-8")
print("Part of Speech Tagging :\n", pos_tag(word_tokenize(text)),file=f)

# Lemmatization
lemmatizer = WordNetLemmatizer()


f=open("lemmatization.txt",'w',encoding="utf-8")
for tok in tokens:
    print("Lemmatization :\n",lemmatizer.lemmatize(str(tok)),file=f)

# Trigram

f=open("trigrams.txt",'w',encoding="utf-8")
trigram = []
for x in tokens:
    trigram.append(list(ngrams(x, 3)))
print("Trigrams :\n",trigram,file=f)


# Named Entity Recognition
f=open("NER.txt",'w',encoding="utf-8")
print("NER : \n", ne_chunk(pos_tag(wordpunct_tokenize(str(tokens)))),file=f)