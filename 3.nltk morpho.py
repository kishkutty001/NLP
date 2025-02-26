import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

text = "The cats are running happily towards the biggest trees."


words = word_tokenize(text)

print("Word\t\tStemmed\t\tLemmatized")
print("-" * 40)
for word in words:
    print(f"{word}\t\t{stemmer.stem(word)}\t\t{lemmatizer.lemmatize(word)}")
