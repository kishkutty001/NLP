from sklearn.feature_extraction.text import TfidfVectorizer

documents = ["The cat in the hat", "A cat is a fine pet", "Dogs and cats are great"]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(tfidf_matrix.toarray())
