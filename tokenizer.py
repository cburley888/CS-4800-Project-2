from nltk.tokenize import RegexpTokenizer


def tokenizer(string):
    tk = RegexpTokenizer(r'\w+')
    return tk.tokenize(string)
