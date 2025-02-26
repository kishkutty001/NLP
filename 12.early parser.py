import nltk
from nltk.parse import EarleyChartParser
from nltk.grammar import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'ball' | 'man'
    Adj -> 'big' | 'small'
    V -> 'chased' | 'saw' | 'barked'
""")

parser = EarleyChartParser(grammar)

sentences = [
    "a big man saw the ball"    
]
for sentence in sentences:
    print(f"\nParsing: {sentence}")
    words = sentence.split()
    for tree in parser.parse(words):
        print(tree)
        tree.pretty_print()

