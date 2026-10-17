# Rule-based and NLTK POS tagging + simple accuracy example
import nltk
from nltk.tokenize import wordpunct_tokenize

text = "The smart boy plays cricket"
tokens = wordpunct_tokenize(text)

# Rule-based tags are deliberately simple for demonstration.
def rule_tag(word):
    low = word.lower()
    if low in {"the", "a", "an"}:
        return "DT"
    if low.endswith("ly"):
        return "RB"
    if low.endswith("ing") or low in {"play", "plays", "is", "are", "was"}:
        return "VB"
    if low in {"smart", "good", "bad", "beautiful"}:
        return "JJ"
    return "NN"

rule_tags = [(word, rule_tag(word)) for word in tokens]
print("Rule-based tags:", rule_tags)

# NLTK's pretrained tagger is the probabilistic/statistical approach.
try:
    nltk_tags = nltk.pos_tag(tokens)
    print("NLTK tags:", nltk_tags)

    # Example gold tags for this exact sentence.
    gold = ["DT", "JJ", "NN", "VBZ", "NN"]
    predicted = [tag for _, tag in nltk_tags]
    correct = sum(g == p for g, p in zip(gold, predicted))
    print(f"NLTK accuracy against example gold tags: {correct}/{len(gold)} = {correct/len(gold)*100:.1f}%")
except LookupError as exc:
    print("NLTK POS data is missing. Run: py download_nltk_data.py")
    print(exc)
