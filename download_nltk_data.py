import nltk

# Download resources used by the practical scripts.
packages = [
    "wordnet",
    "omw-1.4",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "maxent_ne_chunker",
    "maxent_ne_chunker_tab",
    "words",
    "treebank",
]
for package in packages:
    try:
        nltk.download(package, quiet=False)
    except Exception as exc:
        print(f"Could not download {package}: {exc}")

print("\nFinished. If an experiment reports a missing NLTK resource, read its error and download that resource.")
