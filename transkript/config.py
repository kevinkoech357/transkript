import os
from dotenv import load_dotenv

load_dotenv()


class App_Config:
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get("SECRET_KEY", "Transkript!")
    # Video uploads folder
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")
    LOG_FILE_PATH = "transkript.log"
