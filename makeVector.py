import sys
import numpy as np
import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter
np.set_printoptions(threshold=sys.maxsize)


def make_vector(document, vocabList):
    doc_vector = np.zeros(len(vocabList))
    documentTokenized = tokenizer.tokenizer(document)
    documentStopWord = stopWordRemover.stopwordremover(documentTokenized)
    documentStemmed = stemmer.stemmer(documentStopWord)
    """for word in documentStemmed:
        doc_vector[np.where(vocabList == word)] += 1"""
    for word in documentStemmed:
        print(np.where(vocabList == word))

    return doc_vector
