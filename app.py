from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    if user_text.lower() == "hi" or user_text.lower() == "hello":
        return "Hello! How can I assist you today?"
    elif user_text.lower() == "what's your name?" or user_text.lower() == "what is your name?":
        return "My name is Chatbot. How can I help you?"
    elif user_text.lower() == "bye":
        return "Goodbye! Have a nice day."
    else:
        responses = ["I'm sorry, I don't understand. Can you please rephrase?", 
                     "I'm not sure what you mean. Can you provide more information?",
                     "I'm sorry, I can't help you with that. Is there anything else I can assist you with?"]
        return random.choice(responses)

if __name__ == "__main__":
    app.run(debug=True)
