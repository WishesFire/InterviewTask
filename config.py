import os
import datetime
from dotenv import load_dotenv

load_dotenv()
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = str(os.getenv("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=10)
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)
    CELERY_TRACK_STARTED = True


class ConfigAPI:
    DEBUG = True
    SECRET_KEY = str(os.getenv("SECRET_KEY_API"))
    SQLALCHEMY_DATABASE_URI = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #JWT_TOKEN_LOCATION = ['cookies']
    #JWT_COOKIE_SECURE = False
    #JWT_ACCESS_COOKIE_PATH = '/api/'
    #JWT_REFRESH_COOKIE_PATH = '/token/refresh'
    #JWT_COOKIE_CSRF_PROTECT = True
    JWT_SECRET_KEY = str(os.getenv("SECRET_KEY_API_JWT"))
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
