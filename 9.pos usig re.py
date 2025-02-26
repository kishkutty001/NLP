import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Define rules for rule-based POS tagging
patterns = [
    (r'.*ing$', 'VBG'),  # Gerunds (e.g., running, swimming)
    (r'.*ed$', 'VBD'),   # Past tense verbs (e.g., played, worked)
    (r'.*es$', 'VBZ'),   # Present tense verbs third person singular (e.g., runs, flies)
    (r'.*s$', 'NNS'),    # Plural nouns (e.g., cats, dogs)
    (r'\b[A-Z][a-z]*\b', 'NNP'),  # Proper nouns (e.g., John, London)
    (r'.*ly$', 'RB'),    # Adverbs (e.g., quickly, happily)
    (r'.*able$', 'JJ'),  # Adjectives (e.g., comfortable, capable)
    (r'.*ness$', 'NN'),  # Nouns formed from adjectives (e.g., happiness, darkness)
    (r'\d+', 'CD'),      # Cardinal numbers (e.g., 123, 456)
    (r'.*', 'NN')        # Default to noun (NN) if no match
]

# Initialize RegexpTagger
tagger = RegexpTagger(patterns)

# Sample sentence
sentence = "John plays football quickly and runs happily in the morning."
tokens = word_tokenize(sentence)

# Apply POS tagging
tagged_sentence = tagger.tag(tokens)

# Display output
print("Word\tPOS Tag")
print("-" * 20)
for word, tag in tagged_sentence:
    print(f"{word}\t{tag}")
