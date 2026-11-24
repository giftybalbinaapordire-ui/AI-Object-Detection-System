
from flask import Flask, render_template, request
from ultralytics import YOLO
from pathlib import Path
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

MODEL_PATH = BASE_DIR / "model" / "best.pt"
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
RESULT_FOLDER = BASE_DIR / "static" / "results"

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
RESULT_FOLDER.mkdir(parents=True, exist_ok=True)

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

model = YOLO(str(MODEL_PATH))

@app.route("/", methods=["GET", "POST"])
def home():
    result_image = None
    people_count = None
    detections = []

    if request.method == "POST":
        file = request.files.get("image")

        if not file or not file.filename:
            return render_template("index.html", error="Please select an image.")

        allowed = {".jpg", ".jpeg", ".png", ".webp"}
        extension = Path(secure_filename(file.filename)).suffix.lower()

        if extension not in allowed:
            return render_template("index.html", error="Please upload JPG, PNG or WEBP.")

        filename = f"{uuid.uuid4().hex}{extension}"
        image_path = UPLOAD_FOLDER / filename
        file.save(image_path)

        prediction = model.predict(
            source=str(image_path),
            conf=0.25,
            verbose=False
        )[0]

        people_count = len(prediction.boxes)
        result_name = f"result_{filename}.jpg"
        result_path = RESULT_FOLDER / result_name

        prediction.save(filename=str(result_path))

        result_image = f"results/{result_name}"

        for box in prediction.boxes:
            detections.append({
                "confidence": round(float(box.conf[0]) * 100, 2)
            })

    return render_template(
        "index.html",
        result_image=result_image,
        people_count=people_count,
        detections=detections
    )

if __name__ == "__main__":
    app.run(debug=True)
