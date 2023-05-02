from models.users import Users
from session import session


class SQLDatabase:
    def create_user(self, name: str, surname: str, username: str, password: str):
        user_data = Users(
            name=name, surname=surname, username=username, password=password
        )
        session.add(user_data)
        session.commit()

    def get_user(self, username: str):
        user = session.query(Users).filter_by(username=username).one()
        return user

    def get_user_id(self, username):
        user = session.query(Users).filter_by(username=username).one()
        return user.id
