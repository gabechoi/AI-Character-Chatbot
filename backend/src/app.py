from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key = openai_api_key)

character = {"name": None, "description": None}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set_character", methods=["POST"])
def set_character():
    global character
    data = request.json
    character["name"] = data.get("name")
    character["description"] = data.get("description")

    return jsonify({"character": character})

@app.route("/send_message", methods=["POST"])
def send_message():
    user_text = request.json.get("text")

    # Simple mock response (you could integrate OpenAI logic here)
    if character["name"]:
            #response_text = f"{character['name']} ({character['description']}): I heard you say '{user_text}'. Interesting!"
        response = openai_client.chat.completions.create(model = "gpt-4o-mini",
                                                         messages = [
                                                             {"role": "system", "content": character["description"]},
                                                             {"role": "user", "content": user_text},
                                                         ],)
        response_text = response.choices[0].message.content
    else:
        response_text = f"You said: {user_text}"

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)



#print(openai_api_key[:7])

#response = openai_client
