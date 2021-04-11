from website import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .views.base_api import MainPage, Profile

app, migrate = create_app()
db = SQLAlchemy()
api = Api(app)

api.add_resource(MainPage, '/')
api.add_resource(Profile, '/profile')

if __name__ == '__main__':
    app.run()
