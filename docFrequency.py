import numpy as np
import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter
from nltk.corpus import gutenberg


def doc_frequency(doc_tokens_list, vocabList):
    doc_freq_vector = np.zeros(len(vocabList))
    i = 0
    for w in vocabList:
        for u in doc_tokens_list:
            if w in u:
                doc_freq_vector[i] += 1
        i += 1
    return doc_freq_vector
