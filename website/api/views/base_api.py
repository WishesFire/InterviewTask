from flask_restful import Resource, fields, marshal_with
from flask_login import current_user, login_required
from website.database.models_schema import Schema

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "separate": fields.String,
    "user": fields.Integer,
    "order": fields.Integer

}


class MainPage(Resource):
    def get(self):
        return {'user': current_user}


class Profile(Resource):
    @marshal_with(resource_fields)
    @login_required
    def get(self):
        tables = Schema.query.filter_by(user=current_user.id)
        return tables, {'user': current_user, 'name': current_user.username}

    @login_required
    def delete(self):
        pass

