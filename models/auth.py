# pylint: disable= missing-docstring
from models.database import SQLDatabase

db = SQLDatabase()


class Authentication:
    def check_auth(self, username: str, password: str) -> bool:
        user = db.get_user(username=username)
        if user.username == username and user.password == password:
            return True
        return False
