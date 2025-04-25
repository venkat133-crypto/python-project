from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import LoginManager # type: ignore
from config import Config
import os 

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'  # ✅ correct blueprint.route name


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
