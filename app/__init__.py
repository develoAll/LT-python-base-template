from flask import Flask
from config import Config

from .routes.prueba_routes import api_prueba
from .routes.two_routes import api_two
from .home import home


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(api_prueba, url_prefix="/api/prueba")
    app.register_blueprint(api_two, url_prefix="/api/two")
    return app
