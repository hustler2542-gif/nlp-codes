#Compare stemming and lemmatization
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer

words = ["playing", "played", "studies", "cars"]
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")
lemma = WordNetLemmatizer()

for word in words:
    print(
        word,
        "| Porter:", porter.stem(word),
        "| Lancaster:", lancaster.stem(word),
        "| Snowball:", snowball.stem(word),
        "| Lemma (verb):", lemma.lemmatize(word, pos="v")
    )
