#Named Entity Recognition and noun phrase chunking
import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import wordpunct_tokenize
from nltk.chunk import RegexpParser

text = "Rahul works at Google in Mumbai."
tokens = wordpunct_tokenize(text)
tagged = pos_tag(tokens)

print("POS tags:", tagged)
print("Named entities:")
print(ne_chunk(tagged))

# NP = optional determiner + optional adjectives + one or more nouns
grammar = r"NP: {<DT>?<JJ>*<NN.*>+}"
parser = RegexpParser(grammar)
print("Noun phrase chunks:")
print(parser.parse(tagged))
