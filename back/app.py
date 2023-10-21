import sys

from flask import Flask
from flask_cors import CORS

from src.utils.db import construct_db, populate_db
from src.routes.movies import route as route1

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}},
     origins="*",
     methods=["GET", "POST", "UPDATE", "DELETE", "PUT"],
     allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials", "Access-Control-Allow-Origin",
                    "Access-Control-Allow-Headers", "x-access-token", "Origin", "Accept", "X-Requested-With",
                    "Access-Control-Request-Method", "Access-Control-Request-Headers"])

# Register the route route1. Check on src/routes/movies.py
app.register_blueprint(route1)

# Create the database (if drop=True, it will drop the tables before creating them)
# if construct_db(drop=True) is False:
#     print('\033[31m\033[1m' + "Error creating the tables" + '\033[30m\033[0m')
#     exit(1)

# Populate the database
# if populate_db() is False:
#     print('\033[31m\033[1m' + "Error populating the tables" + '\033[30m\033[0m')
#     exit(1)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
