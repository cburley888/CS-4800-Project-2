import sys
import numpy as np
import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter
np.set_printoptions(threshold=sys.maxsize)


def make_vector(document, vocabList):
    doc_vector = np.zeros(len(vocabList))
    print(doc_vector)
    documentTokenized = tokenizer.tokenizer(document)
    documentStopWord = stopWordRemover.stopwordremover(documentTokenized)
    documentStemmed = stemmer.stemmer(documentStopWord)
    document_filtered = [word for word in documentStemmed if word in vocabList]
    for word in document_filtered:
        doc_vector[vocabList[word]] += 1
    """for word in vocabList:
        print(word)"""

    return doc_vector
