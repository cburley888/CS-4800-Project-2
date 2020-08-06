import lemmatizer
import tokenizer
import stopWordRemover

testSentence = "I am searching. I have searched. You will search. You will be looking, as I have looked."
testSentenceLower = testSentence.lower()
testSentenceTokenized = tokenizer.tokenizer(testSentenceLower())
testSentenceLemmatize = lemmatizer.lemmatizer(testSentenceTokenized())


print(tokenizer.tokenizer(testSentenceLower))
