import spacy

nlp = spacy.load("en_coreference_web_trf")
text = "John met Mary. He said hello."
doc = nlp(text)

for cluster in doc._.coref_clusters:
    print(cluster)
