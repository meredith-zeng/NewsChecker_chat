from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    message = request.json["message"]

    # Generate response using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        max_tokens=1024,
        temperature=0.5,
        n=1,
        stop=None
    )
    reply = response.choices[0]['message']['content']
    json = jsonify(reply)
    print(json.data)
    return json

if __name__ == "__main__":
    app.run(debug=True)