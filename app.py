
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="gpt2")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    result = generator(prompt, max_length=200, num_return_sequences=1)
    return jsonify(result[0])

if __name__ == "__main__":
    app.run(debug=True)
    