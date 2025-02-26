import nltk
from nltk.classify import NaiveBayesClassifier

data = [("Hello, how are you?", "greeting"),
        ("What time is it?", "question"),
        ("Goodbye!", "farewell")]

classifier = NaiveBayesClassifier.train([(dict(words=nltk.word_tokenize(text)), label) for text, label in data])

test = "Hi there!"
print(classifier.classify(dict(words=nltk.word_tokenize(test))))
