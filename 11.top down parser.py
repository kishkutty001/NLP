import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'ball'
    Adj -> 'big' | 'small'
    V -> 'chased' | 'saw' | 'barked'
""")
parser = nltk.ChartParser(grammar)
sentences = [
    "the dog chased a cat"  
]
for sentence in sentences:
    print(f"\nParsing: {sentence}")
    words = sentence.split()
    for tree in parser.parse(words):
        print(tree)
        tree.pretty_print()
