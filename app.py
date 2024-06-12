import os
import sys

from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
from utils.data_loader import load_data

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=user_input,
            max_tokens=150
        )
        return jsonify({"response": response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pretrain', methods=['POST'])
def pretrain():
    data_path = './data'
    data = load_data(data_path)
    return jsonify({"message": "Data loaded successfully", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
