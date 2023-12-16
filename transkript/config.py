import os
from dotenv import load_dotenv

load_dotenv(".env")


class App_Config:
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get("SECRET_KEY", "hello_world!")
    # Video uploads folder
    UPLOAD_FOLDER = "/home/ubuntu/transkript/uploads"
    # Celery configuration
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
    CELERY_TASK_IGNORE_RESULT = True
    # Log file path
    LOG_FILE_PATH = "transkript.log"
