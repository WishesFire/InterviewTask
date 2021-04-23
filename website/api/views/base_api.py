from flask_restful import Resource, fields, marshal_with
from flask_jwt_extended import jwt_required
from flask_login import current_user
from website.database.models_schema import Schema

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "separate": fields.String,
    "user": fields.Integer,
    "order": fields.Integer
}


class Profile(Resource):
    @marshal_with(resource_fields)
    @jwt_required
    def get(self):
        tables = Schema.query.filter_by(user=current_user.id)
        return tables

    def delete(self):
        pass

