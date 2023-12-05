import os
from dotenv import load_dotenv

load_dotenv(".env")


class App_Config:
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get("SECRET_KEY", "hello_world!")
    # Video uploads folder
    UPLOAD_FOLDER = "/home/ubuntu/transkript/uploads"
