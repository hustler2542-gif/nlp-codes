# NLP Practical Codes (Python)

This pack contains short, separate scripts for the NLP practical experiments:
1. Text preprocessing: tokenization, script/character validation, stop-word removal
2. Stemming and lemmatization comparison
3. Minimum Edit Distance (spelling correction)
4. N-gram language model
5. POS tagging: rule-based and NLTK probabilistic/pretrained tagger + accuracy
6. Named Entity Recognition (NER) and noun-phrase chunking
7. Word Sense Disambiguation (Lesk) and WordNet relations
8. Sentiment classification using Naive Bayes and SVM

## Setup
Use Python 3.10–3.12 if possible. Open a terminal in this folder.

```bash
py -m pip install -r requirements.txt
```

Some NLTK experiments need language data. Run this once:

```bash
py download_nltk_data.py
```

Then run any experiment, for example:

```bash
py 01_preprocessing.py
```

Run each `.py` file separately. The scripts use small example inputs so they are easy to remember in a practical exam.

## Important
- Internet may be required the first time NLTK data is downloaded.
- If your lab computer blocks downloads, ask whether the required NLTK datasets are already installed.
- Experiment 8 uses a tiny built-in example dataset. Its accuracy is only a demonstration, not a meaningful real-world evaluation.
