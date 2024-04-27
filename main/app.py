# -*- coding: utf-8 -*-
"""
Title: AI Chatbot for Customer Service
Industry: CRM - Customer Relationship Management
@author: Tabish Ali Ansari
"""

from flask import Flask, request, jsonify
import spacy

# Initialize Flask app
app = Flask(__name__)

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Dummy database (replace with actual database integration)
user_data = {}

# Define route for handling user messages
@app.route("/message", methods=["POST"])
def handle_message():
    # Get user message from request
    user_message = request.json["message"]
    
    # Process user message using spaCy NLP
    doc = nlp(user_message)
    
    # Extract intent (dummy implementation, replace with actual intent classification)
    intent = "dummy_intent"
    
    # Perform action based on intent
    if intent == "dummy_intent":
        response = "This is a dummy response."
    else:
        response = "Sorry, I didn't understand that."
    
    # Store user data (dummy implementation, replace with actual database integration)
    user_id = request.json["user_id"]
    if user_id not in user_data:
        user_data[user_id] = []
    user_data[user_id].append({"message": user_message, "response": response})
    
    # Return response to user
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
