import os
import datetime
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class Config:
    DEBUG = True
    TESTING = True
    JWT_SECRET_KEY = JWT_SECRET_KEY
    JWT_BLACKLIST_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    # JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
