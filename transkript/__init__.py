from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap5
from transkript.config import App_Config


bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    # Load configuration from App_Config
    app.config.from_object(App_Config)

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Initialize CORS
    CORS(app)
    
    from transkript.views import user

    app.register_blueprint(user)

    return app
