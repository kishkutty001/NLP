from nltk.corpus import wordnet as wn

word = "bank"
synsets = wn.synsets(word)

for syn in synsets:
    print(f"{syn.name()}: {syn.definition()}")
