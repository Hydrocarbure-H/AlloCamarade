import src.constants as CONSTANTS
import mysql.connector
import mysql.connector
from src.utils.utils import server_error
from src.entities.database import Database
from src.strings import API


def construct_db(drop=False):
    """
    Create the models and the tables
    :param drop: Drop the database before creating it
    :return: None
    """
    db = Database()

    # If drop is True, drop the database
    if drop:
        db.drop()
        db.already_created = False

    # Create the database
    db.create()

    # Check if the database exists
    try:
        db.execute("USE " + CONSTANTS.DB_NAME, cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't use database " + CONSTANTS.DB_NAME + " : " + str(err), True)

    users()

    return API.SUCCESS


def users():
    """
    Create the movies table
    :return: True, exit 1 if error
    """

    # db = Database()
    # try:
    #     db.execute(
    #         "CREATE TABLE"
    #         " IF NOT EXISTS "
    #         " ..."
    #         , cursorBuffered=False)
    # except mysql.connector.Error as err:
    #     server_error("Can't create movies table : " + str(err), True)

    return True


def populate_db():
    """
    Populate the database (insert data inside)
    """
    db = Database()
    pop_movies(db)

    return True


def pop_movies(db):
    """
    Populate the users table
    """

    # try:
    #     db.execute(
    #         "INSERT INTO ... VALUES ... "
    #         , cursorBuffered=False)
    # except mysql.connector.Error as err:
    #     server_error("Can't populate users table : " + str(err), True)

    return True
