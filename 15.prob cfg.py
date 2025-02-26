import nltk
from nltk import PCFG, ViterbiParser

grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> 'John' [0.5] | 'Mary' [0.5]
    VP -> 'runs' [0.6] | 'eats' [0.4]
""")

parser = ViterbiParser(grammar)
sentence = ['John', 'runs']
for tree in parser.parse(sentence):
    print(tree)
