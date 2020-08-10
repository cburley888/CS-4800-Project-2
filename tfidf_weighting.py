import numpy
from numpy import log


def tfidf_weighting(term_freq_vector, doc_freq_vector, doc_list):
    tfidf_vector = []
    i = 0
    for w in term_freq_vector:
        tfidf = w * log((1+len(doc_list)) / (1 + doc_freq_vector[i]))
        tfidf_vector.append(tfidf)
        i += 1
    return tfidf_vector
