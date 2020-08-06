import numpy
from numpy import array
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

ps = PorterStemmer()
tk = RegexpTokenizer(r'\w+')
stopWords = set(stopwords.words('english'))
testSentence = "I am searching. I have searched. You will search. You will be looking, as I have looked."
testSentenceLower = testSentence.lower()
uniqueTokens = set()

testWordsTokenized = tk.tokenize(testSentenceLower)
testWordStop = [word for word in testWordsTokenized if word not in stopWords]
testWordStem = [ps.stem(word) for word in testWordStop]
testWordUnique = array([])
for word in testWordStem:
    if word not in uniqueTokens:
        uniqueTokens.add(word)
        testWordUnique = numpy.append(word, testWordUnique)
for w in testWordUnique:
    print(w)
