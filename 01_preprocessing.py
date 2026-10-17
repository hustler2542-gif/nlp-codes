
import re
from nltk.tokenize import wordpunct_tokenize

text = "This is a simple NLP example, with 2 numbers!"

tokens = wordpunct_tokenize(text.lower())

valid_words = [word for word in tokens if re.fullmatch(r"[a-z]+", word)]

stop_words = {"is", "a", "the", "this", "with", "and", "of", "in", "to"}
result = [word for word in valid_words if word not in stop_words]

print("Tokens:", tokens)
print("Valid words:", valid_words)
print("After stop-word removal:", result)
