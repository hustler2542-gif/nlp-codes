# Word Sense Disambiguation using Lesk + WordNet relations
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk.tokenize import wordpunct_tokenize

sentence = "I deposited money in the bank"
tokens = wordpunct_tokenize(sentence.lower())

sense = lesk(tokens, "bank")
print("Sentence:", sentence)
print("Lesk sense:", sense)
if sense:
    print("Definition:", sense.definition())
    print("Examples:", sense.examples())

# WordNet semantic relations
synsets = wn.synsets("car", pos=wn.NOUN)
if synsets:
    car = synsets[0]
    print("\nWord:", "car")
    print("Definition:", car.definition())
    print("Synonyms:", car.lemma_names())
    print("Hypernyms (broader categories):", [s.name() for s in car.hypernyms()])
    print("Hyponyms (more specific types):", [s.name() for s in car.hyponyms()])
