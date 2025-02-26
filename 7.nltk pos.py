import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The quick brown fox jumps over the lazy dog."

words = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(words)

print("Word\tPOS Tag")
print("-" * 20)
for word, tag in pos_tags:
    print(f"{word}\t{tag}")
