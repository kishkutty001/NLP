import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "jumps", "easily", "flies", "argued", "happily", "fishing", "caresses", "ponies", "troubling"]

print("Original Word -> Stemmed Word")
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")
