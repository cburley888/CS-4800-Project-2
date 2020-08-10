from nltk.corpus import gutenberg
import createVocabString
import vocabCreator
import makeVector
import cosineSimilarity

"""testSentence01 = "I am searching. I have searched. You will search. You will be looking, as I have looked."
testSentence02 = "Look around and you will see, a world of true tranquility. Searching far, searched it wide, it is the search that all abide."
testSentence02 = "Back again, I can wait to get on the road again, back again, like frodo baggins?"""

vocabString = createVocabString.createvocabstring()
vocabulary = vocabCreator.vocabcreator(vocabString)

query = input("Enter query: ")
queryVector = makeVector.make_vector(query, vocabulary)
docs = []
docVectors = []
similarityScores = []

for w in gutenberg.fileids():
    docs[w] = gutenberg.raw(w)
    docVectors[w] = makeVector.make_vector(docs[w], vocabulary)
    similarityScores[w] = cosineSimilarity(queryVector, docVectors[w])

"""document01 = gutenberg.raw('austen-persuasion.txt')
document02 = gutenberg.raw('austen-sense.txt')
document01_vector = makeVector.make_vector(testSentence01, vocabulary)
document02_vector = makeVector.make_vector(testSentence02, vocabulary)
"""
"""similarity = cosineSimilarity.cosine_similarity(document01_vector, document02_vector)"""
print(vocabulary)
