from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager
from flask_wtf.csrf import CSRFProtect
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


def create_app():
    app.config.from_object('config.Config')
    db.init_app(app)

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    from .handlers.base import base_views
    from .handlers.schema.schema import schema_views
    from .handlers.error import error_hd
    from .handlers.user.create_user import auth

    app.register_blueprint(base_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(schema_views, url_prefix='/')
    app.register_blueprint(error_hd)

    from website.database.models_user import User, Profile
    from website.database.models_schema import Schema, ColumnSchema, FileSchema

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Авторизуйтесь для доступа'
    login_manager.login_message_category = 'success'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        if user_id is not None:
            return User.query.get(int(user_id))
        return None

    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    manager = Manager(app)

    return app, manager


def make_celery():
    celery = Celery(app.import_name, backend=os.getenv('CELERY_RESULT_BACKEND'), broker=os.getenv('CELERY_BROKER_URL'))
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery
