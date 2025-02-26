import nltk
from nltk.corpus import brown
from collections import defaultdict
import random

nltk.download('brown')
nltk.download('universal_tagset')

tagged_sentences = brown.tagged_sents(tagset='universal')

word_tag_freq = defaultdict(lambda: defaultdict(int))

for sentence in tagged_sentences:
    for word, tag in sentence:
        word = word.lower()  
        word_tag_freq[word][tag] += 1


def stochastic_pos_tagger(sentence):
    pos_tags = []
    for word in sentence:
        word_lower = word.lower()
        if word_lower in word_tag_freq:
        
            most_probable_tag = max(word_tag_freq[word_lower], key=word_tag_freq[word_lower].get)
        else:
  
            most_probable_tag = random.choice(['NOUN', 'VERB', 'ADJ', 'ADV'])
        pos_tags.append((word, most_probable_tag))
    return pos_tags

sentence = ["The", "dog", "chased", "the", "cat"]
tagged_sentence = stochastic_pos_tagger(sentence)


print("Word\tPOS Tag")
print("-" * 20)
for word, tag in tagged_sentence:
    print(f"{word}\t{tag}")
