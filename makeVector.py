import sys
import numpy as np
import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter
np.set_printoptions(threshold=sys.maxsize)

"""This function creates a term frequency vector given a list of document tokens"""
def make_vector(documentTokens, vocabList):
    doc_vector = np.zeros(len(vocabList))
    for word in documentTokens:
        doc_vector[vocabList[word]] += 1
    """for word in vocabList:
        print(word)"""

    return doc_vector
