import numpy
from numpy.linalg import norm
from numpy import dot

def cosine_similarity(vec1, vec2):
    return (dot(vec1 , vec2)) / (norm(vec1) * norm(vec2))