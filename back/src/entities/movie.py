import mysql.connector

from src.entities.database import Database
from src.utils.utils import server_error


class Movie:
    def __init__(self, data):
        if not data or "title" not in data or "duration" not in data or "language" not in data or "subtitles" not in data or "director" not in data or "actors" not in data or "min_age" not in data or "start_date" not in data or "end_date" not in data:
            raise Exception("Invalid data")

        self.title = data["title"]
        self.duration = data["duration"]
        self.language = data["language"]
        self.subtitles = data["subtitles"]
        self.director = data["director"]
        self.actors = data["actors"]
        self.min_age = data["min_age"]
        self.start_date = data["start_date"]
        self.end_date = data["end_date"]
        self.theater = 1

    def add(self):
        """
        Add the movie to the database
        :return:
        """
        db = Database()
        try:
            db.execute(
                "INSERT INTO `movies` "
                "(`title`,"
                " `duration`,"
                " `language`,"
                " `subtitles`,"
                " `director`,"
                " `actors`,"
                " `min_age`,"
                " `start_date`,"
                " `end_date`,"
                " `theater`) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                , (self.title,
                   self.duration,
                   self.language,
                   self.subtitles,
                   self.director,
                   self.actors,
                   self.min_age,
                   self.start_date,
                   self.end_date,
                   self.theater))
        except mysql.connector.Error as err:
            server_error("Can't add movie : " + str(err), True)
            return False

        return True

    @staticmethod
    def get_all():
        """
        Get all movies
        :return:
        """
        db = Database()
        try:
            db.execute("SELECT * FROM movies;")
        except mysql.connector.Error as err:
            server_error("Can't get movies : " + str(err), True)
            return False

        return db.cursor.fetchall()
