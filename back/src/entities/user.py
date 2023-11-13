from src.entities.database import Database
from passlib.hash import sha256_crypt


class User:
    """
    User entity
    """

    def __init__(self, data):
        self.username = data['username']
        self.password = sha256_crypt.using(rounds=5000).hash(data['password'])

    def login(self):
        """
        Login user
        :return:
        """
        db = Database()
        db.connect()

        query = "SELECT password FROM users WHERE username = %s AND password = %s"
        params = (self.username, self.password)
        result = db.execute(query, params)

        if result is None:
            return False

        else:
            if sha256_crypt.verify(self.password, result[0][0]):
                return True

        return False
