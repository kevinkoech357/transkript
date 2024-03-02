from flask import Blueprint, render_template, current_app, request, jsonify, send_file
from werkzeug.utils import secure_filename
from transkript.tasks import transcribe_file
import os
import logging

user = Blueprint("user", __name__)
logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {"mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"}


def allowed_file(filename):
    """
    Check if the file extension is allowed.

    Parameters:
        filename (str): The name of the file.

    Returns:
        bool: True if the file extension is allowed, False otherwise.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@user.route("/", methods=["GET"])
def index():
    """
    Render the index.html page.

    Returns:
        str: Rendered HTML content.
    """
    logger.info("Rendering index.html")
    return render_template("index.html")


@user.route("/upload", methods=["POST"])
def upload():
    """
    Handle file upload and initiate transcription.

    Returns:
        JSON: Response indicating success or failure.
    """
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
            logger.info("Transcription in progress. It might take a while...")

            file.save(file_path)
            logger.info("File saved, transcription starting")

            # Transcription
            download_link = transcribe_file(file_path)

            logger.info("Transcription completed successfully")

            return jsonify(
                {
                    "success": "File uploaded successfully",
                    "download_link": download_link,
                }
            )

        logger.error("Invalid file type")
        return jsonify({"error": "Invalid file type"})

    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred during file upload"})


@user.route("/download/<filename>", methods=["GET"])
def download(filename):
    """
    Download the SRT file.

    Parameters:
        filename (str): The name of the SRT file.

    Returns:
        File: SRT file as an attachment.
    """
    srt_file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    return send_file(srt_file_path, as_attachment=True)
