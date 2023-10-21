import mysql.connector
import src.constants as CONSTANTS

from src.utils.utils import server_error


class Database:
    """
    Database class
    """

    def __init__(self, already_created=True):
        """
        Constructor
        """

        self.connection = None
        self.cursor = None
        self.already_created = already_created

    def connect(self):
        """
        Connect to the database
        """
        if self.already_created:
            try:
                self.connection = mysql.connector.connect(
                    host=CONSTANTS.DB_HOST,
                    user=CONSTANTS.DB_USER,
                    password=CONSTANTS.DB_PASS,
                    database=CONSTANTS.DB_NAME,
                    auth_plugin='mysql_native_password')
            except mysql.connector.Error as err:
                server_error("Something went wrong when connecting to the db: " + str(err), True)
        else:
            try:
                self.connection = mysql.connector.connect(
                    host=CONSTANTS.DB_HOST,
                    user=CONSTANTS.DB_USER,
                    password=CONSTANTS.DB_PASS,
                    auth_plugin='mysql_native_password')
            except mysql.connector.Error as err:
                server_error("Something went wrong when connecting to the db: " + str(err), True)

        if self.connection is not None:
            self.cursor = self.connection.cursor()
            return

        server_error("Something went wrong when connecting to the db - Unknown Error.", True)

    def disconnect(self):
        """
        Disconnect from the database
        """
        if self.connection is not None:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def execute(self, query, params=None, cursorBuffered=True, DEBUG=False):
        """
        Execute a query
        :param query: Query
        :param params: Parameters
        :param cursorBuffered: Cursor buffered (avoid mysql.connector.errors.InternalError: Unread result found)
        :param DEBUG: Debug mode
        :return: Query result
        """

        self.connect()
        try:
            if cursorBuffered:
                self.cursor = self.connection.cursor(buffered=True)
            self.cursor.execute(query, params)
        except mysql.connector.Error as err:
            server_error("Something went wrong when executing the query: " + str(err), True)

        self.connection.commit()
        result = None
        if not cursorBuffered:
            result = self.cursor.fetchall()

        if DEBUG:
            print(self.cursor.statement)
            print(result)
        self.disconnect()
        return result

    def execute_one(self, query, params=None, DEBUG=False):
        """
        Execute a query and return the first result
        :param query: Query
        :param DEBUG: Debug mode
        :param params: Parameters
        :return: Query result
        """

        self.connect()
        self.cursor = self.connection.cursor(buffered=True)
        try:
            self.cursor.execute(query, params)
        except mysql.connector.Error as err:
            server_error("Something went wrong when executing the query: " + str(err), True)

        self.connection.commit()
        result = self.cursor.fetchone()
        if DEBUG:
            print(self.cursor.statement)
            print(result)
        self.disconnect()
        return result

    def drop(self):
        """
        Drop the database
        :return: None
        """
        self.execute("DROP DATABASE IF EXISTS " + CONSTANTS.DB_NAME, cursorBuffered=False)

    def create(self):
        """
        Create the database
        :return: None
        """
        self.execute("CREATE DATABASE IF NOT EXISTS " + CONSTANTS.DB_NAME, cursorBuffered=False)
