import nltk
from nltk.tag import RegexpTagger, UnigramTagger
from nltk.tag.brill import Template
from nltk.tag.brill_trainer import BrillTaggerTrainer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

training_data = [
    [('He', 'PRP'), ('runs', 'VBZ')],
    [('She', 'PRP'), ('played', 'VBD')],
    [('They', 'PRP'), ('are', 'VBP'), ('running', 'VBG')],
    [('The', 'DT'), ('dogs', 'NNS'), ('bark', 'VBP')]
]

baseline_tagger = UnigramTagger(training_data, backoff=RegexpTagger([
    (r'.*ing$', 'VBG'), 
    (r'.*ed$', 'VBD'),   
    (r'.*es$', 'VBZ'),   
    (r'.*s$', 'NNS'),   
    (r'.*', 'NN')        
]))

templates = [
    Template(nltk.tag.brill.Pos([1])),   
    Template(nltk.tag.brill.Pos([-1]))   
]

trainer = BrillTaggerTrainer(baseline_tagger, templates)
brill_tagger = trainer.train(training_data, max_rules=5)

test_sentence = "The cat runs quickly".split()
tagged_sentence = brill_tagger.tag(test_sentence)

print("Word\tPOS Tag")
print("-" * 20)
for word, tag in tagged_sentence:
    print(f"{word}\t{tag}")
