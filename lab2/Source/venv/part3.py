from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import ngrams, FreqDist

#reading the data from a file
with open('E:\qs3input.txt','r') as text_file:
    fileData = text_file.read()

# Word Tokenization - to extarct each wprd ffrom the text
tokens = word_tokenize(fileData)

# Applying Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatizerOutput = []
print("Lemmatization Output : \n")
for tok in tokens:
    #itearting through each word and lematizing and appending it to list
    lemmatizerOutput.append(lemmatizer.lemmatize(str(tok)))
print(lemmatizerOutput)

# performing Bigram on the  Lemmatizer Output
print("Bigrams :\n")
bigramsOutput = []
for big in ngrams(tokens, 2):
    # Fetching Bigrams using 'ngrams' method and Iterating it and appending it to list
    bigramsOutput.append(big)
print(bigramsOutput)

# BiGram- Word Frequency
# Using bigramOutput fetch the WordFreq Details
wordFreq = FreqDist(bigramsOutput)
# Getting Most Common Words and Printing them - Will get the Counts from top to least
mostCommon = wordFreq.most_common()
print("BiGrams Frequency (From Top to Least) : \n", mostCommon)
# Fetching the Top 5 Bigrams
top5 = wordFreq.most_common(5)
print("Top 5 BiGrams : \n", top5)


# Getting Sentences using Sentence Tokenization
sentTokens = sent_tokenize(fileData)
# Creating an Array to append the sentence
concatenatedArray = []
# Iterating the Sentences
for sentence in sentTokens:
    # Iterating the BiGrams present
    for a, b in bigramsOutput:
        # Iterating the Top 5 BiGrams
        for ((c, m), length) in top5:
            # Comparing the each with each of the Top 5 Bigram
            if(a, b == c, m):
                concatenatedArray.append(sentence)

print("Concatenated Array : ",concatenatedArray)
print("Maximum of Concatenated Array : ", max(concatenatedArray))