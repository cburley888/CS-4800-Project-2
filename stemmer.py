from nltk.stem import PorterStemmer

"""This function returns a stemmed version of each term in a given array"""
def stemmer(array):
    st = PorterStemmer()
    return [st.stem(word) for word in array]
