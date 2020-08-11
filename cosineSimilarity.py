import numpy
from numpy.linalg import norm
from numpy import dot

"""This function takes two vectors and returns the cosine similarity"""
def cosine_similarity(vec1, vec2):
    return (dot(vec1 , vec2)) / (norm(vec1) * norm(vec2))
