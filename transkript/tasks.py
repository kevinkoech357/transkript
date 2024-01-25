from flask import current_app
from pathlib import Path
import whisper
from whisper.utils import get_writer
import logging

logger = logging.getLogger(__name__)


def transcribe_file(file_path):
    try:
        with current_app.app_context():
            # Ensure the upload folder exists
            output_directory = current_app.config["UPLOAD_FOLDER"]

            path = Path(file_path)

            # Load whisper model
            model = whisper.load_model("base")

            # Run Whisper
            result = model.transcribe(file_path, verbose=False, language="en")

            # Write transkript to file
            logger.info("Creating SRT file")
            srt_writer = get_writer("srt", output_directory)
            srt_writer(result, path.stem)

            # Construct download link directly using the file name
            download_link = f"/download/{path.stem}.srt"
            return download_link
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        raise
