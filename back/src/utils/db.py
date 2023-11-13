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

    print("Dropping the database...")
    # Drop the database
    db.drop()

    print("Creating the database...")
    # Create the database
    db.create()

    # Check if the database exists
    try:
        db.execute("USE " + CONSTANTS.DB_NAME, cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't use database " + CONSTANTS.DB_NAME + " : " + str(err), True)

    print("Creating the users table...")
    users()
    print("Creating the theaters table...")
    theaters()
    print("Creating the movies table...")
    movies()

    return API.SUCCESS


def movies():
    """
    Create the movies table
    :return: True, exit 1 if error
    """

    db = Database()

    try:
        db.execute(
            "CREATE TABLE IF NOT EXISTS `movies` ("
            " `id` int NOT NULL AUTO_INCREMENT,"
            " `title` varchar(255) DEFAULT NULL,"
            " `duration` int NOT NULL,"
            " `language` varchar(255) DEFAULT NULL,"
            " `subtitles` varchar(255) DEFAULT NULL,"
            " `director` longtext,"
            " `actors` longtext,"
            " `min_age` int NOT NULL,"
            " `start_date` varchar(10) NOT NULL,"
            " `end_date` varchar(10) NOT NULL,"
            "  `theater` int NOT NULL,"
            " PRIMARY KEY (`id`),"
            "  CONSTRAINT `movies_ibfk_1` FOREIGN KEY (`theater`) REFERENCES `theaters` (`id`)"
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
            "CREATE TABLE IF NOT EXISTS `theaters` ("
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
            "CREATE TABLE IF NOT EXISTS `users` ("
            " `id` int NOT NULL AUTO_INCREMENT,"
            " `username` varchar(255) DEFAULT NULL,"
            " `password` varchar(255) DEFAULT NULL,"
            " `admin` tinyint NOT NULL DEFAULT '0',"
            " PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't create users table : " + str(err), True)

    return True


def pop_theaters(db):
    """
    Populate the theaters table
    :param db:
    :return:
    """

    try:
        db.execute(
            "INSERT INTO `theaters` VALUES "
            "(1,'Theater 1','Location 1'),"
            "(2,'Theater 2','Location 2'),"
            "(3,'Theater 3','Location 3');"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't populate theaters table : " + str(err), True)

    return True


def pop_users(db):
    """
    Populate the users table
    :param db:
    :return:
    """

    try:
        db.execute(
            "INSERT INTO `users` VALUES "
            "(1,'john_doe','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',0),"
            "(2,'admin','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',1);"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't populate users table : " + str(err), True)

    return True


def populate_db():
    """
    Populate the database (insert data inside)
    """
    db = Database()
    pop_theaters(db)
    pop_movies(db)
    pop_users(db)

    return True


def pop_movies(db):
    """
    Populate the movies table
    """

    try:
        db.execute(
            "INSERT INTO `movies` VALUES "
            "(1,'Movie 1',120,'French','English','Director 1','Actor 1',12,'2020-01-01','2020-01-02',1),"
            "(2,'Movie 2',120,'French','English','Director 2','Actor 2',12,'2020-01-01','2020-01-02',2),"
            "(3,'Movie 3',120,'French','English','Director 3','Actor 3',12,'2020-01-01','2020-01-02',3);"
            , cursorBuffered=False)
    except mysql.connector.Error as err:
        server_error("Can't populate movies table : " + str(err), True)

    return True
