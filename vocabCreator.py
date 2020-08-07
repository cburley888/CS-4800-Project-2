import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter


def vocabcreator(string):
    lower = string.lower()
    tokenized = tokenizer.tokenizer(lower)
    stopwords = stopWordRemover.stopwordremover(tokenized)
    stem = stemmer.stemmer(stopwords)
    uniquetokens = uniqueTokenFilter.uniquetokenfilter(stem)
    return uniquetokens
