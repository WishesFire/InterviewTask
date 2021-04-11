from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
    app.config.from_object('config.Config')
    db.init_app(app)

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    from .handlers.base import base_views
    from .handlers.schema.schema import schema_views
    from .handlers.error import error_hd
    from .handlers.user.create_user import auth

    from website.database.models_user import User, Profile
    from website.database.models_schema import Schema, ColumnSchema, FileSchema

    app.register_blueprint(base_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(schema_views, url_prefix='/')
    app.register_blueprint(error_hd)

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

    return app, migrate
