
from Actions.UserActions import UserActions


class UserService:

    def __init__(self, db_session):
        self.session = db_session

    def add_user(self, name: str, surname: str, mail: str, login: str, password: str):
        return UserActions(self.session).add_user(name=name, surname=surname, mail=mail, login=login, password=password)

    def get_all_users(self):
        return UserActions(self.session).get_all_users()
