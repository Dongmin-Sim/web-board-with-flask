from flask import Flask
from .config import config_by_name


def create_app(config_name: str) -> Flask:
    # flask app
    app = Flask(__name__)

    # config
    app.config.from_object(config_by_name[config_name])

    # blueprint
    from app.views import app_views
    app.register_blueprint(app_views)

    # db
    from app.model.db_connect import db
    db.init_app(app)

    return app
