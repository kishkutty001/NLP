import spacy

nlp = spacy.load("en_core_web_sm")
text = "Barack Obama was the 44th President of the United States."
doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
