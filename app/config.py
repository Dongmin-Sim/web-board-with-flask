import os
import dotenv

dotenv.load_dotenv('../.env')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    # Swagger
    # RESTX_MASK_SWAGGER = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig
)
