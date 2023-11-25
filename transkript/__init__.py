from flask import Flask
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    
    from transkript.views import user

    app.register_blueprint(user)

    return app
