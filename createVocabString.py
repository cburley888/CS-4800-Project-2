import nltk
from nltk.corpus import gutenberg

"""This function turns the gutenberg texts into a single string"""
def createvocabstring():
    resultstring = ""
    for w in nltk.corpus.gutenberg.fileids():
        resultstring += gutenberg.raw(w)

    return resultstring
