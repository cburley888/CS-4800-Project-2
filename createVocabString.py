import nltk
from nltk.corpus import gutenberg


def createvocabstring():
    resultstring = ""
    for w in nltk.corpus.gutenberg.fileids():
        resultstring += gutenberg.raw(w)

    return resultstring
