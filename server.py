from flask import Flask, request, jsonify
import os
from nanoid import generate
import cv2

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/photo", methods=["POST"])
def upload_photo():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = generate() + ".jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # OpenCVで画像を読み込んで処理（例：白黒にする）
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filepath, gray)

    return jsonify({"message": "File uploaded and processed", "filename": filename}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
