from nltk.stem import WordNetLemmatizer

"""This function takes an array, and returns an array of the lemmatized version of each word in the array"""


def lemmatize(self, array):
    lm = WordNetLemmatizer()
    return [lm.lemmatize(word) for word in array]
