from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai


client = genai.Client(api_key="AIzaSyCsvTdYLkYznHuz5tSqv5yMKy_3bp-unjc")

def study_assistant(user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt
    )
    return response.text

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask_api():
    data = request.get_json()
    question = data.get("question")

    answer = study_assistant(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
