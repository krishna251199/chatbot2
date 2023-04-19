from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Flask initialization
app = Flask(__name__)

chatbot=ChatBot('Pythonscholar')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/app/get', methods=['POST'])
def get():
    # Your code to handle the request goes here
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)
    





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7303)
