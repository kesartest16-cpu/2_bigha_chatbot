from flask import Flask, render_template, request, jsonify
import json
from chatbot.chatbot import get_response

app = Flask(__name__)

# Load intents
with open("data/intents.json") as f:
    intents = json.load(f)["chatbot_responses"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_chatbot_response():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' in request body"}), 400
    user_msg = data["message"]
    response = get_response(user_msg, intents)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
