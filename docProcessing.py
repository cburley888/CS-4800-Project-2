import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter


def process_doc(string, vocabList):
    documentTokenized = tokenizer.tokenizer(string)
    documentStopWord = stopWordRemover.stopwordremover(documentTokenized)
    documentStemmed = stemmer.stemmer(documentStopWord)
    document_filtered = [word for word in documentStemmed if word in vocabList]
    return document_filtered
