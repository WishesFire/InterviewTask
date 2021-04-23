from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity, create_access_token
from website.database.api.models_token import Token
from .utils import generate_secure_password, check_secure_password, provide_token
from website.database.models_user import User
from website import db

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("username", help="Name of your user's account", required=True)
user_put_args.add_argument("password", help="Password from your account", required=True)

user_login_resource_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "password": fields.String
}


class UserRegistrationPage(Resource):
    def post(self):
        args = user_put_args.parse_args()
        username = args["username"]
        password = args["password"]
        status_exists = User.query.filter_by(username=username).first()
        if status_exists:
            return jsonify({"message": f"User {username} already exists"})
        try:
            new_user = User(username=username, password=generate_secure_password(password))
            db.session.add(new_user)
            db.session.commit()
            true_token, refresh_token = provide_token(username)
            return jsonify({
                "message": f"User {username} was successfully created",
                "access_token": true_token,
                "refresh_token": refresh_token,
            }), 200

        except:
            return jsonify({"message": "Something wrong!"}), 500


class UserLoginPage(Resource):
    @marshal_with(user_login_resource_fields)
    def post(self):
        args = user_put_args.parse_args()
        username = args["username"]
        password = args["password"]
        exist_user = User.query.filter_by(username=username).first()
        if not exist_user:
            return jsonify({"message": f"User {username} not exist"})
        if check_secure_password(password, exist_user.password):
            true_token, refresh_token = provide_token(username)
            return jsonify({
                "message": f"User {username} is logged",
                "access_token": true_token,
                "refresh_token": refresh_token
            }), 200
        else:
            return jsonify({"message": "Something wrong!"}), 500


class UserLogoutToken(Resource):
    @jwt_required
    def post(self):
        jti_token = get_jwt()["jti"]
        try:
            token = Token(jti=jti_token)
            db.session.add(token)
            db.session.commit()
            return jsonify({'message': 'Access token has been revoked'}), 200
        except:
            return jsonify({"message": "Something wrong"}), 500


class RefreshToken(Resource):
    @jwt_required
    def post(self):
        try:
            now_user = get_jwt_identity()
            create_access_token(identity=now_user)
            return jsonify({"message": "Token refresh successfully"}), 200
        except:
            return jsonify({"message": "Something wrong!"}), 500
