from flask import Flask, render_template
from flask_cors import CORS
from flask_bootstrap import Bootstrap5
from transkript.config import App_Config
import logging
from logging.handlers import RotatingFileHandler

bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)

    # Load configuration from App_Config
    app.config.from_object(App_Config)

    # Set up extensions
    bootstrap.init_app(app)

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Initialize CORS
    CORS(app, supports_credentials=True)

    # Set up logging
    configure_logging(app)

    # Import blueprint
    from transkript.views import user

    # Register blueprint
    app.register_blueprint(user)

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        """
        Render 404.html incase of 404 status code.
        """
        return render_template("404.html")

    @app.errorhandler(413)
    def entity_too_larg(e):
        """
        Render 413.html incase of 413 status code.
        """
        return render_template("413.html")

    @app.errorhandler(500)
    def internal_server_error(e):
        """
        Render 500.html incase of 500 status code.
        """
        return render_template("500.html")

    return app


def configure_logging(app):
    # Configure logging to a file
    log_file_path = app.config.get("LOG_FILE_PATH", "transkript.log")
    handler = RotatingFileHandler(log_file_path, maxBytes=100000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Configure logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    app.logger.addHandler(console_handler)

    # Set the Flask app logger level
    app.logger.setLevel(logging.DEBUG)
