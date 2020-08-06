import numpy
from numpy import array
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.corpus import gutenberg

persuasion = gutenberg.raw('austen-persuasion.txt')
print(persuasion)

lm = WordNetLemmatizer()
tk = RegexpTokenizer(r'\w+')
stopWords = set(stopwords.words('english'))

persuasionLower = persuasion.lower()
uniqueTokens = set()

testWordsTokenized = tk.tokenize(persuasionLower)
testWordStop = [word for word in testWordsTokenized if word not in stopWords]
testWordStem = [lm.lemmatize(word) for word in testWordStop]
testWordUnique = array([])
for word in testWordStem:
    if word not in uniqueTokens:
        uniqueTokens.add(word)
        testWordUnique = numpy.append(word, testWordUnique)
for w in testWordUnique:
    print(w)
