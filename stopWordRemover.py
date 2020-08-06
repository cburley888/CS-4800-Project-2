from nltk.corpus import stopwords


def stopwordremover(array):
    stopWords = set(stopwords.words('english'))
    return [word for word in array if word not in stopWords]