import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter

"""This function controls the tokenization, stemming,stop word removal, and unique word filtering of a given list"""
def process_doc(string, vocabList):
    documentTokenized = tokenizer.tokenizer(string)
    documentStopWord = stopWordRemover.stopwordremover(documentTokenized)
    documentStemmed = stemmer.stemmer(documentTokenized)
    document_filtered = [word for word in documentStemmed if word in vocabList]
    return document_filtered
