from nltk.corpus import gutenberg
import createVocabString
import vocabCreator
import makeVector

"""testSentence = "I am searching. I have searched. You will search. You will be looking, as I have looked."""
"""print(testString)"""

vocabString = createVocabString.createvocabstring()
vocabulary = vocabCreator.vocabcreator(vocabString)

document01 = gutenberg.raw('austen-persuasion.txt')
document01_vector = makeVector.make_vector(document01, vocabulary)
print(document01_vector)
