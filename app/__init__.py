from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)
    # from .routes.prueba_routes import api_prueba
    # from .routes.two_routes import api_two
    from .routes import api_student
    from .home import home

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(api_student, url_prefix="/api/student")
    return app
