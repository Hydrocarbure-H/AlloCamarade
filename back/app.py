from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from src.strings import API
from src.utils.db import construct_db, populate_db
from src.routes.movies import route as route1
from src.routes.sign import route as route2
from src.utils.utils import response

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "incredible-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": "*"}},
     origins="*",
     methods=["GET", "POST", "UPDATE", "DELETE", "PUT"],
     allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials", "Access-Control-Allow-Origin",
                    "Access-Control-Allow-Headers", "x-access-token", "Origin", "Accept", "X-Requested-With",
                    "Access-Control-Request-Method", "Access-Control-Request-Headers"])

app.register_blueprint(route1)
app.register_blueprint(route2)

# Create the database
if construct_db() is False:
    print('\033[31m\033[1m' + "Error creating the tables" + '\033[30m\033[0m')
    exit(1)

# Populate the database
if populate_db() is False:
    print('\033[31m\033[1m' + "Error populating the tables" + '\033[30m\033[0m')
    exit(1)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    """
    Callback called when the token has expired
    :param jwt_header:
    :param jwt_payload:
    :return:
    """
    return response(API.UNAUTHORIZED, "Token has expired.", "token_expired")


@jwt.invalid_token_loader
def my_invalid_token_callback(jwt_header):
    """
    Callback called when the token is invalid
    :param jwt_header:
    :return:
    """
    return response(API.UNAUTHORIZED, "Token is invalid.", "token_invalid")


# create all jwt callbacks here
@jwt.unauthorized_loader
def my_unauthorized_loader_callback(jwt_header):
    """
    Callback called when the token is missing
    :param jwt_header:
    :return:
    """
    return response(API.UNAUTHORIZED, "Token is missing.", "token_missing")


@jwt.needs_fresh_token_loader
def my_needs_fresh_token_loader_callback(jwt_header, jwt_payload):
    """
    Callback called when the token is not fresh
    :param jwt_header:
    :param jwt_payload:
    :return:
    """
    return response(API.UNAUTHORIZED, "Token is not fresh.")


@jwt.revoked_token_loader
def my_revoked_token_loader_callback(jwt_header, jwt_payload):
    """
    Callback called when the token is revoked
    :param jwt_header:
    :param jwt_payload:
    :return:
    """
    return response(API.UNAUTHORIZED, "Token is revoked.")