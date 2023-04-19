from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    # Your logic for the chatbot response goes here
    bot_text = "I'm just a simple Flask chatbot."
    return str(bot_text)

if __name__ == "__main__":
    app.run()
