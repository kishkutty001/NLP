import random
import nltk
from nltk import bigrams
from collections import defaultdict

text = "the cat sat on the mat the cat ate the rat"
words = text.split()

bigram_model = list(bigrams(words))
print(bigram_model)

bigram_dict = defaultdict(list)
for w1, w2 in bigram_model:
    bigram_dict[w1].append(w2)

def generate_text(start_word, length=10):
    current_word = start_word
    generated_text = [current_word]

    for _ in range(length - 1):
        if current_word in bigram_dict:
            current_word = random.choice(bigram_dict[current_word])  
            generated_text.append(current_word)
        else:
            break  

    return ' '.join(generated_text)

print(generate_text("the", length=10))
