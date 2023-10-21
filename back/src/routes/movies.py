from flask import Blueprint

from src.strings import API
from src.utils.utils import response

# The route name that we will use in app.py
route = Blueprint('route1', __name__)


# Try to connect to http://localhost:5000/route1/helloworld :)
@route.route('/route1/helloworld', methods=['GET'])
def helloworld():
    """
    Say hello to the world
    :return:
    """
    print("You are in the route1/helloworld route !")
    return response(API.SUCCESS, "Hello world !")
