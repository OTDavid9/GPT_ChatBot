from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_content = request.form.get("user_content")

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_content}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return {"ai_response": response.choices[0].message.content}

if __name__ == "__main__":
    app.run(debug=True)
