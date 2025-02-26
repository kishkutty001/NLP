from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = "The bank of the river was calm and peaceful."
word = "bank"

sense = lesk(word_tokenize(sentence), word)
print(f"Best Sense: {sense.name()}\nDefinition: {sense.definition()}")
