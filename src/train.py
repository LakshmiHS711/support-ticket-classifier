import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


# 1. Load dataset
df = pd.read_csv("data/customer_support_tickets.csv")


# 2. Combine ticket subject and description
df["text"] = (
    df["Ticket Subject"].fillna("")
    + " "
    + df["Ticket Description"].fillna("")
)


# 3. Input and target
X = df["text"]
y = df["Ticket Type"]


# 4. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 5. Convert text into TF-IDF features
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    min_df=2,
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# 6. Create Logistic Regression model
model = LogisticRegression(
    max_iter=1000
)


# 7. Train the model
model.fit(X_train_tfidf, y_train)


# 8. Make predictions
y_pred = model.predict(X_test_tfidf)


# 9. Evaluate model
accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)


# 10. Display results
print("=" * 50)
print("SUPPORT TICKET CLASSIFIER")
print("=" * 50)

print("\nModel training completed successfully!")

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nTF-IDF features:", X_train_tfidf.shape[1])

print("\nCategories:")
for category in model.classes_:
    print("-", category)

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print(f"F1-score: {f1:.4f}")


# 11. Save model and vectorizer
joblib.dump(model, "models/ticket_classifier.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nModel saved to:")
print("models/ticket_classifier.pkl")

print("\nTF-IDF vectorizer saved to:")
print("models/tfidf_vectorizer.pkl")