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
    keyword = data.get("keyword", "").strip().lower()
    if not keyword:
        return jsonify({"proverb": "❌ No keyword provided."}), 400

    proverb = generate_text(model, seed_text=keyword)
    return jsonify({"proverb": proverb})

if __name__ == '__main__':
    app.run(debug=True)
