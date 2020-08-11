import numpy

"""This function returns an array with only unique terms that were contained in a given array"""
def uniquetokenfilter(array):
    uniquetokens = set()
    returnarray = []
    for word in array:
        if word not in uniquetokens:
            uniquetokens.add(word)
            returnarray.append(word)

    return returnarray