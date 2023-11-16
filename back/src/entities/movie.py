import mysql.connector

from src.entities.database import Database
from src.utils.utils import server_error


class Movie:
    def __init__(self, data=None, id=None):
        """
        Initialize the movie
        """

        # If the id is specified, get the movie from the database
        if id is not None:
            db = Database()
            d = None
            try:
                d = db.execute_one("SELECT * FROM movies WHERE id = %s", (id,))
            except mysql.connector.Error as err:
                server_error("Can't get movie : " + str(err), True)

            data = {
                "title": d[1],
                "duration": d[2],
                "language": d[3],
                "subtitles": d[4],
                "director": d[5],
                "actors": d[6],
                "min_age": d[7],
                "start_date": d[8],
                "end_date": d[9]
            }

        if not data or "title" not in data or "duration" not in data or "language" not in data or "subtitles" not in data or "director" not in data or "actors" not in data or "min_age" not in data or "start_date" not in data or "end_date" not in data:
            raise Exception("Invalid data")

        self.id = id
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

    def update(self):
        """
        Update the movie in the database
        :return:
        """
        db = Database()
        try:
            db.execute(
                "UPDATE `movies` SET "
                "`title` = %s,"
                "`duration` = %s,"
                "`language` = %s,"
                "`subtitles` = %s,"
                "`director` = %s,"
                "`actors` = %s,"
                "`min_age` = %s,"
                "`start_date` = %s,"
                "`end_date` = %s,"
                "`theater` = %s "
                "WHERE `id` = %s"
                , (self.title,
                   self.duration,
                   self.language,
                   self.subtitles,
                   self.director,
                   self.actors,
                   self.min_age,
                   self.start_date,
                   self.end_date,
                   self.theater,
                   self.id))
        except mysql.connector.Error as err:
            server_error("Can't update movie : " + str(err), True)
            return False

        return True

    def delete(self):
        """
        Delete the movie from the database
        :return:
        """
        db = Database()
        try:
            db.execute("DELETE FROM `movies` WHERE `id` = %s", (self.id,))
        except mysql.connector.Error as err:
            server_error("Can't delete movie : " + str(err), True)
            return False

        return True

    @staticmethod
    def get_all(location=None):
        """
        Get all movies
        :return:
        """
        db = Database()

        if location is None:
            try:
                res = db.execute("SELECT theaters.id, movies.title, movies.duration, movies.language, "
                                 "movies.subtitles,"
                                 "movies.director, movies.actors, movies.min_age, movies.start_date, movies.end_date, "
                                 "theaters.location "
                                 "FROM movies INNER JOIN theaters ON movies.theater = theaters.id", cursorBuffered=False, commit=True)
            except mysql.connector.Error as err:
                server_error("Can't get movies : " + str(err), True)
                return False
        else:
            try:
                res = db.execute("SELECT theaters.id, movies.title, movies.duration, movies.language, "
                                 "movies.subtitles,"
                                 "movies.director, movies.actors, movies.min_age, movies.start_date, movies.end_date, "
                                 "theaters.location "
                                 "FROM movies INNER JOIN theaters ON movies.theater = theaters.id WHERE "
                                 "theaters.location ="
                                 "%s", (location,), cursorBuffered=False, commit=True)
            except mysql.connector.Error as err:
                server_error("Can't get movies : " + str(err), True)
                return False

        return res
