# app.py
from flask import Flask, request, jsonify
from model_utils import load_model, generate_text
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/generate": {"origins": "*"}})
model = load_model()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    print("📩 Data received:", data)
    keyword = data.get("keyword", "")
    proverb = generate_text(model, keyword)
    return jsonify({"proverb": proverb})

if __name__ == '__main__':
    app.run(debug=True)
