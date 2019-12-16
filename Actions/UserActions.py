
from Model.User import User


class UserActions:

    def __init__(self, db_session):
        self.session = db_session

    def add_user(self, name: str, surname: str, mail: str, login: str, password: str):
        return self.session.add(User(name=name, surname=surname, mail=mail, login=login, password=password))

    def get_all_users(self):
        return self.session.query(User).all()