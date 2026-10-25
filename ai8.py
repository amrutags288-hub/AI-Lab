import re
import random

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye"],
        "responses": ["Goodbye!", "Take care!", "See you later!"]
    },
    "name": {
        "patterns": ["what is your name", "who are you"],
        "responses": ["I am a chatbot!", "You can call me Chatbot."]
    },
    "thanks": {
        "patterns": ["thank you", "thanks"],
        "responses": ["You're welcome!", "No problem!"]
    },
    "help": {
        "patterns": ["help me", "can you help me"],
        "responses": ["Sure! I am here to help you."]
    }
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def match_intent(user_input):
    words = preprocess(user_input)
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if all(word in words for word in preprocess(pattern)):
                return intent
    return None

def chatbot():
    print("Chatbot: Hello! Type bye to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye!")
            break

        intent = match_intent(user_input)

        if intent:
            print("Chatbot:", random.choice(intents[intent]["responses"]))
        else:
            print("Chatbot: Sorry, I could not understand that.")

chatbot()