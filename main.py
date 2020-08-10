from nltk.corpus import gutenberg
import createVocabString
import vocabCreator
import makeVector
import cosineSimilarity
import docFrequency
import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter
import docProcessing
import tfidf_weighting

"""testSentence01 = "I am searching. I have searched. You will search. You will be looking, as I have looked."
testSentence02 = "Look around and you will see, a world of true tranquility. Searching far, searched it wide, it is the search that all abide."
testSentence02 = "Back again, I can wait to get on the road again, back again, like frodo baggins?"""

vocabString = createVocabString.createvocabstring()
vocabulary = vocabCreator.vocabcreator(vocabString)

query = input("Enter query: ")
queryTokens = docProcessing.process_doc(query, vocabulary)
queryVector = makeVector.make_vector(queryTokens, vocabulary)
docs = []
docTokens = []
docVectors = []
tfidf_docs = []
similarityScoresFreq = []
similarityScoresTfidf = []
i = 0
for w in gutenberg.fileids():
    docs.append(gutenberg.raw(w))
    document_processed = docProcessing.process_doc(docs[i], vocabulary)
    docTokens.append(document_processed)
    docVectors.append(makeVector.make_vector(docTokens[i], vocabulary))
    similarityScoresFreq.append(cosineSimilarity.cosine_similarity(queryVector, docVectors[i]))
    i += 1

docFreq = docFrequency.doc_frequency(docTokens, vocabulary)
k = 0
for w in gutenberg.fileids():
    tfidf_docs.append(tfidf_weighting.tfidf_weighting(docVectors[k], docFreq, gutenberg.fileids()))
    similarityScoresTfidf.append(cosineSimilarity.cosine_similarity(queryVector, tfidf_docs[k]))
    k += 1

docWeightsFreq = {}
docWeightsTfidf = {}
j = 0
for w in gutenberg.fileids():
    docWeightsFreq.update({w: similarityScoresFreq[j]})
    docWeightsTfidf.update({w: similarityScoresTfidf[j]})
    j += 1

docWeightsFreqSorted = sorted(docWeightsFreq.items(), key=lambda x: x[1], reverse=True)
docWeightsTfidfSorted = sorted(docWeightsTfidf.items(), key=lambda x: x[1], reverse=True)
print("Term Frequency: ")
print(docWeightsFreqSorted)
print("TF-IDF: ")
print(docWeightsTfidfSorted)
