from flask import Blueprint, render_template, current_app, request, jsonify
from werkzeug.utils import secure_filename
import os

user = Blueprint("user", __name__)

ALLOWED_EXTENSIONS = {
    "mpeg",
    "mp3",
    "mpeg3",
    "mpga",
    "mp4",
    "m4a",
    "wav",
    "webm",
    "mp4",
}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@user.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@user.route("/upload", methods=["POST"])
def upload():
    try:
        if "file" not in request.files:
            print("No file part")
            return jsonify({"error": "No file part"})

        file = request.files["file"]

        if file.filename == "":
            print("No selected file")
            return jsonify({"error": "No selected file"})

        if file and allowed_file(file.filename):
            # Save the file to the upload folder
            file_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
            )
            file.save(file_path)

            # Transcription

            print("File uploaded successfully")
            return jsonify({"success": "File uploaded successfully"})

        print("Invalid file type")
        return jsonify({"error": "Invalid file type"})

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred during file upload"})
