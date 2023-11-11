import src.constants as CONSTANTS
import mysql.connector
import mysql.connector
from src.utils.utils import server_error
from src.entities.database import Database
from src.strings import API


def construct_db():
    """
    Create the models and the tables
    :return: None
    """
    db = Database()

    # Create the database
    db.create()

    # Check if the database exists
    try:
        db.execute("USE " + CONSTANTS.DB_NAME, cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't use database " + CONSTANTS.DB_NAME + " : " + str(err), True)

    users()
    movies()
    theaters()

    return API.SUCCESS


def movies():
    """
    Create the movies table
    :return: True, exit 1 if error
    """

    db = Database()
    try:
        db.execute(
            "DROP TABLE IF EXISTS `movies`;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't drop movies table : " + str(err), True)
    try:
        db.execute(
            "CREATE TABLE `movies` ("
            " `id` int NOT NULL AUTO_INCREMENT,"
            " `title` varchar(255) DEFAULT NULL,"
            " `duration` int NOT NULL,"
            " `language` varchar(255) DEFAULT NULL,"
            " `subtitles` varchar(255) DEFAULT NULL,"
            " `director` longtext,"
            " `actors` longtext,"
            " `min_age` int NOT NULL,"
            " `start_date` date NOT NULL,"
            " `end_date` date NOT NULL,"
            " PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't create movies table : " + str(err), True)

    return True


def theaters():
    """
    Create the theaters table
    :return: True, exit 1 if error
    """

    db = Database()
    try:
        db.execute(
            "DROP TABLE IF EXISTS `theaters`;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't drop theaters table : " + str(err), True)
    try:
        db.execute(
            "CREATE TABLE `theaters` ("
            " `id` int NOT NULL AUTO_INCREMENT,"
            " `name` varchar(255) DEFAULT NULL,"
            " `location` varchar(255) DEFAULT NULL,"
            " PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't create theaters table : " + str(err), True)

    return True


def users():
    """
    Create the users table
    :return: True, exit 1 if error
    """

    db = Database()
    try:
        db.execute(
            "DROP TABLE IF EXISTS `users`;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't drop users table : " + str(err), True)
    try:
        db.execute(
            "CREATE TABLE `users` ("
            " `id` int NOT NULL AUTO_INCREMENT,"
            " `username` varchar(255) DEFAULT NULL,"
            " `password` varchar(64) DEFAULT NULL,"
            " `admin` tinyint NOT NULL DEFAULT '0',"
            " PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't create users table : " + str(err), True)

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
