from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import create_access_token, create_refresh_token


def generate_secure_password(password):
    return sha256.hash(password.encode())


def check_secure_password(password, current_password):
    return sha256.verify(password, current_password)


def provide_token(user):
    return create_access_token(identity=user), create_refresh_token(identity=user)
