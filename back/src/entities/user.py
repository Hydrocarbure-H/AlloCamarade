import hashlib

from src.entities.database import Database
from passlib.hash import sha256_crypt


class User:
    """
    User entity
    """

    def __init__(self, data):
        self.username = data['username']
        self.password = data['password']

    def login(self):
        """
        Login user
        :return:
        """
        db = Database()
        db.connect()

        query = "SELECT password FROM users WHERE username = %s"
        params = (self.username,)
        result = db.execute_one(query, params)

        if result is None:
            return False

        else:
            if self.check_password(result[0]):
                return True

        return False

    def check_password(self, hashed_password):

        sha256_hash = hashlib.sha256()
        sha256_hash.update(self.password.encode("utf-8"))
        computed_hash = sha256_hash.hexdigest()

        return computed_hash == hashed_password
