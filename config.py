import os
import datetime
from dotenv import load_dotenv

load_dotenv()
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    #EXPLAIN_TEMPLATE_LOADING = True
    SECRET_KEY = str(os.getenv("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=10)
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)
    CELERY_TRACK_STARTED = True
