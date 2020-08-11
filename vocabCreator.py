import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter

"""This function creates a vocabulary of unique terms given a string"""
def vocabcreator(string):
    lower = string.lower()
    tokenized = tokenizer.tokenizer(lower)
    stopwords = stopWordRemover.stopwordremover(tokenized)
    stem = stemmer.stemmer(tokenized)
    unique_tokens = uniqueTokenFilter.uniquetokenfilter(stem)
    vocab = {}
    i = 0
    for word in unique_tokens:
        vocab.update({word: i})
        i += 1
    return vocab
