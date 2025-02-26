import nltk
from nltk import CFG

def check_sentence_agreement(sentence):
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det N | Det Adj N
        VP -> V NP | V
        Det -> 'the' | 'a'
        N -> 'cat' | 'dog' | 'cars' | 'apple'
        Adj -> 'big' | 'small'
        V -> 'eats' | 'eat' | 'runs' | 'run'
    """)
    
    parser = nltk.ChartParser(grammar)
    tokens = sentence.lower().split()
    
    try:
        parse_trees = list(parser.parse(tokens))
        if parse_trees:
            print("Valid sentence according to the grammar.")
        else:
            print("Invalid sentence structure.")
    except ValueError:
        print("Invalid sentence structure.")

test_sentences = [
    "The cat eats",
    "A dog cat",
    "The cars run",
    "A apple eat"
]

for sentence in test_sentences:
    print(f"Checking: {sentence}")
    check_sentence_agreement(sentence)
    print("-")
