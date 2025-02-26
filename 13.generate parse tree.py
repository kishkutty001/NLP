import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N | 'John'
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'ball' | 'man'
    Adj -> 'big' | 'small'
    V -> 'chased' | 'saw' | 'barked'
""")

parser = nltk.RecursiveDescentParser(grammar)

sentence = "the dog chased a cat".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
