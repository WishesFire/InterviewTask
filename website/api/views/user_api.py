from flask_restful import Resource, reqparse, fields, marshal_with, abort
from website.database.models_user import User


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("username", type=str, help="Name of your user's account")
user_put_args.add_argument("password", type=str, help="Password from your account")

user_login_resource_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "password": fields.String
}


class LoginPage(Resource):
    @marshal_with(user_login_resource_fields)
    def put(self):
        args = user_put_args.parse_args()
        exist_user = User.query.filter_by(username=args["username"]).first()
        if not exist_user:
            abort(409, message="User is not exist")
