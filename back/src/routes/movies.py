from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from src.entities.movie import Movie
from src.strings import API
from src.utils.utils import response

route = Blueprint('movies', __name__)


@jwt_required
@route.route('/movies/add', methods=['POST'])
def add_movies():
    """
    Add movies
    :return:
    """

    data = request.get_json()
    if data is None:
        return response(API.BAD_REQUEST, "Invalid data")

    # Add the movie to the database
    movie = Movie(data)
    if not movie.add():
        return response(API.BAD_REQUEST, "Can't add movie")

    return response(API.SUCCESS, "OK")


@route.route('/movies/get', methods=['GET'])
def get_movies():
    """
    Get movies
    :return:
    """

    # Get the movies from the database
    movies = Movie.get_all()

    return response(API.SUCCESS, movies)
