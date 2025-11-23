# Customer Support Chatbot for Agricultural purposes
An ML-powered conversational agent that uses a JSON knowledge base + machine learning models to auto-reply to customer queries on a website.
# 🚀 Overview
This project delivers an end-to-end AI customer support chatbot designed for websites.
It leverages a structured JSON dataset and machine learning/NLP models to automatically generate context-aware responses to customer messages in real time.

It’s lightweight, scalable, and production-ready — optimized for businesses seeking fast customer engagement without huge overhead.
#✨ Features
🔍 Intent Classification using ML models

💬 Automated Replies generated directly from JSON-based Q/A dataset

🌐 Web-integrated Chat Widget for front-end

⚙️ Backend API for message processing

📚 Expandable Knowledge Base (just update the JSON file)

📈 Smart matching for near-similar queries

💡 Fallback responses using NLP similarity
#🏗️ Tech Stack
Machine Learning & NLP


Backend


Frontend
HTML / CSS / JavaScript chat widget

Dataset
.json file containing intents, patterns, and responses


📁 Project Structure



⚙️ Installation & Setup
1. Clone the repository
    git clone https://github.com/your-username/chatbot-project.git
cd chatbot-project
2. Install Dependencies
  pip install -r requirements.txt

3. Train the Model (if needed)
   python model/train_chatbot.py
4. Run the Backend Server
   python app/app.py
   The backend will start at:
http://localhost:5000

# How this works 
User types a message in the website chat widget.

Message is sent to your backend API.

Model predicts intent based on trained ML classifier.

A matching reply is retrieved from intents.json.

Bot sends the answer back to the user.

#Json dataset format 
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Is anyone there?", "Hey"],
      "responses": ["Hello! How can I help you today?"]
    },
    {
      "tag": "payment_issue",
      "patterns": ["Payment failed", "I can't complete my payment"],
      "responses": ["Sorry for the trouble! Please try again or contact support."]
    }
  ]
}

#🧪 API Endpoint

POST /predict
Request:
{
  "message": "How do I track my order?"
}
Response:
{
  "reply": "You can track your order from the 'Orders' section in your account."
}

 
   


