from nltk.corpus import stopwords

"""This function returns an array with the stop words removed given an array of terms"""
def stopwordremover(array):
    stopWords = set(stopwords.words('english'))
    return [word for word in array if word not in stopWords]