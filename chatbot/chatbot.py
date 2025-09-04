import json
import joblib

# Load intents
with open("data/intents.json") as f:
    intents = json.load(f)["chatbot_responses"]

# Load trained model and vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def get_response(user_msg, intents):
    # Transform user message
    X = vectorizer.transform([user_msg])
    intent_tag = model.predict(X)[0]

    # Find corresponding response
    for intent in intents:
        if intent["tag"] == intent_tag:
            return intent["response"]

    return "Sorry, I did not understand that. Can you rephrase?"
