
from flask.views import MethodView
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Services.UserService import UserService
from init import InitApp


class User(MethodView):
    def __init__(self):
        self.engine = create_engine(InitApp.db_uri())

    def get(self):
        session = sessionmaker(bind=self.engine)()
        users = UserService(session).get_all_users()
        session.close()

        responce = dict()
        counter = 0

        for user in users:
            responce[counter] = {
                "id": user.id,
                "name": user.name,
                "surname": user.surname,
                "login": user.login,
                "password": user.password
            }

            counter += 1

        return jsonify(responce)

    def post(self):
        try:
            data = request.json
            print(data)
            session = sessionmaker(bind=self.engine)()
            UserService(session).add_user(data["name"], data["surname"], data["mail"],
                                          data["login"], data["password"])
            session.commit()
            session.close()

            return jsonify({
                "message": "User was created"
            })

        except KeyError:
            return jsonify({
                "message": "Wrong input data"
            })

    def put(self):
        pass

    def delete(self):
        pass
