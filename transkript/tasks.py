from flask import current_app
from pathlib import Path
import whisper
from whisper.utils import get_writer
import logging
import os
from celery import shared_task


logger = logging.getLogger(__name__)


@shared_task
def transcribe_file(file_path):
    try:
        # Ensure the upload folder exists
        output_directory = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(output_directory, exist_ok=True)

        path = Path(file_path)

        # Load whisper model
        model = whisper.load_model("base")

        # Run Whisper
        result = model.transcribe(file_path, verbose=False, language="en")

        # Write transkript to file
        logger.info("Creating SRT file")
        srt_writer = get_writer("srt", output_directory)
        srt_writer(result, path.stem)

        return result
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        raise
