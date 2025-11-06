from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key = openai_api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_text = request.json.get("text")

    return jsonify({"response": user_text})

if __name__ == "__main__":
    app.run(debug=True)



#print(openai_api_key[:7])

#response = openai_client
