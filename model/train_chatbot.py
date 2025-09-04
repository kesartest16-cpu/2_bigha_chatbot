import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
with open("data/intents.json") as f:
    data = json.load(f)["chatbot_responses"]

X = []
y = []

for intent in data:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])

# Vectorizer
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model training completed and saved.")
