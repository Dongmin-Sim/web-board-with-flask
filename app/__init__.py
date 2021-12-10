from flask import Flask
from flask_migrate import Migrate
from .config import config_by_name
from flask_wtf.csrf import CSRFProtect

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
flask_bcrypt = Bcrypt()
csrf = CSRFProtect()


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)

    # config
    app.config.from_object(config_by_name[config_name])

    # db
    from .model import post, user
    db.init_app(app)
    migrate.init_app(app, db)
    # bcrypt
    flask_bcrypt.init_app(app)

    # flask_wtf - csrf
    csrf.init_app(app)

    return app
