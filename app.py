from flask import Flask, request, jsonify
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]
    img = Image.open(file).convert("RGB")
    pixels = np.array(img)

    # basic entropy-like logic (improve later)
    variance = np.var(pixels)

    score = 0
    if variance > 2000:
        score = 80
    elif variance > 1000:
        score = 50
    else:
        score = 20

    return jsonify({
        "score": int(score),
        "result": "Suspicious" if score > 60 else "Clean"
    })

if __name__ == "__main__":
    app.run()