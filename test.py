import numpy
from numpy import array
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

ps = PorterStemmer()
tk = RegexpTokenizer(r'\w+')

testSentence = "searching searched search looking, looked"

testWordsTokenized = tk.tokenize(testSentence)

for w in testWordsTokenized:
    print(w, " ", ps.stem(w))
