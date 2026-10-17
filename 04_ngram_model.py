#Unigram, bigram, trigram counts and bigram probability
from collections import Counter

text = "i love NLP and i love Python"
words = text.lower().split()

unigrams = Counter(words)
bigrams = Counter((words[i], words[i + 1]) for i in range(len(words) - 1))
trigrams = Counter((words[i], words[i + 1], words[i + 2]) for i in range(len(words) - 2))

print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)

pair = ("i", "love")
probability = bigrams[pair] / unigrams[pair[0]]
print("P(love | i) =", probability)
