from nltk.stem import PorterStemmer


def stemmer(array):
    st = PorterStemmer()
    return [st.stem(word) for word in array]
