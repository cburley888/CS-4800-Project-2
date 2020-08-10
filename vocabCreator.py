import stemmer
import tokenizer
import stopWordRemover
import uniqueTokenFilter


def vocabcreator(string):
    lower = string.lower()
    tokenized = tokenizer.tokenizer(lower)
    stopwords = stopWordRemover.stopwordremover(tokenized)
    stem = stemmer.stemmer(stopwords)
    unique_tokens = uniqueTokenFilter.uniquetokenfilter(stem)
    vocab = {}
    i = 0
    for word in unique_tokens:
        vocab.update({word: i})
        i += 1
    return vocab
