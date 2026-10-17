#Sentiment classification using Naive Bayes and SVM
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

texts = [
    "I love this movie", "This film is excellent", "Amazing wonderful story",
    "I hate this movie", "This film is terrible", "Very boring and bad story",
    "The movie was great", "The movie was awful", "I enjoyed the film",
    "I disliked the film", "Fantastic acting and story", "Poor acting and terrible story"
]
labels = [
    "positive", "positive", "positive", "negative", "negative", "negative",
    "positive", "negative", "positive", "negative", "positive", "negative"
]

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=42, stratify=labels
)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Naive Bayes
nb = MultinomialNB()
nb.fit(X_train_vec, y_train)
pred_nb = nb.predict(X_test_vec)
print("Naive Bayes accuracy:", accuracy_score(y_test, pred_nb))

# Support Vector Machine
svm = LinearSVC()
svm.fit(X_train_vec, y_train)
pred_svm = svm.predict(X_test_vec)
print("SVM accuracy:", accuracy_score(y_test, pred_svm))

sample = vectorizer.transform(["This movie is excellent"])
print("Sample sentiment (SVM):", svm.predict(sample)[0])
