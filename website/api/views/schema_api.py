from flask_restful import Resource, fields, marshal_with, reqparse, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from website.database.models_schema import Schema
from website import db

schema_put_args = reqparse.RequestParser()
schema_put_args.add_argument("name", help="Name of schema", required=True)
schema_put_args.add_argument("separate", type=str, help="Schema separator", required=True)
schema_put_args.add_argument("user", help="Whose schema", required=True)
schema_put_args.add_argument("orders", help="Schema columns", required=True)

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "separate": fields.String,
    "user": fields.Integer,
    "orders": fields.Integer,
}


class SchemaDetail(Resource):
    @marshal_with(resource_fields)
    @jwt_required
    def put(self):
        args = schema_put_args.parse_args()
        now_user = get_jwt_identity()
        status = Schema.query.filter_by(user=now_user, name=args["name"]).first()
        if not status:
            abort(404, message="This schema is exist")

        schema = Schema(name=args["name"], separate=args["separate"], user=now_user, order=args["orders"])
        db.session.add(schema)
        db.session.commit()

        return "Successfully created", 200
