from models.users import Users
from session import session


class Authentication:
    def check_auth(self, login_user: str, login_password: str) -> bool:
        user = session.query(Users).filter_by(username=login_user).one()
        if user.username == login_user and user.password == login_password:
            return True
        # return True
