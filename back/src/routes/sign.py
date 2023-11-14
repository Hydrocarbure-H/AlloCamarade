# The login and register routes will be here.
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from src.entities.movie import Movie
from src.entities.user import User
from src.strings import API
from src.utils.utils import response

route = Blueprint('user', __name__)


@route.route('/user/login', methods=['POST'])
def login():
    """
    Add movies
    :return:
    """

    # get data from request

    data = request.get_json()
    if data is None:
        return response(API.UNAUTHORIZED, "Invalid data")

    # Create the user and check if the login is correct
    user = User(data)

    if not user.login():
        return response(API.BAD_REQUEST, "Incorrect username or password.")

    token = create_access_token(identity=user.username)
    return response(API.SUCCESS, token)

