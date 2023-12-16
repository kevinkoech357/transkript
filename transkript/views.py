from flask import Blueprint, render_template, current_app, request, jsonify
from werkzeug.utils import secure_filename
from transkript.tasks import transcribe_file
import os
import logging

user = Blueprint("user", __name__)
logger = logging.getLogger(__name__)

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
    logger.info("Rendering index.html")
    return render_template("index.html")


@user.route("/upload", methods=["POST"])
def upload():
    try:
        if "file" not in request.files:
            logger.error("No file part")
            return jsonify({"error": "No file part"})

        file = request.files["file"]

        if file.filename == "":
            logger.error("No selected file")
            return jsonify({"error": "No selected file"})

        if file and allowed_file(file.filename):
            # Save the file to the upload folder
            file_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
            )
            file.save(file_path)
            logger.info("file saved, transcription starting")

            # Transcription
            transcribe_file.delay(file_path)

            logger.info("Transcription in progress. It might take a while...")

            logger.info("File uploaded successfully")
            return jsonify({"success": "File uploaded successfully"})

        logger.error("Invalid file type")
        return jsonify({"error": "Invalid file type"})

    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred during file upload"})
