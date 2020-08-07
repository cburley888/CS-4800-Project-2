import numpy

def uniquetokenfilter(array):
    uniquetokens = set()
    returnarray = []
    for word in array:
        if word not in uniquetokens:
            uniquetokens.add(word)
            returnarray.append(word)

    return returnarray