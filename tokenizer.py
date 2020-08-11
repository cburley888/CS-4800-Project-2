from nltk.tokenize import RegexpTokenizer

"""This function turns the string into an array of alphanumerical terms using regex"""
def tokenizer(string):
    tk = RegexpTokenizer(r'\w+')
    return tk.tokenize(string)
