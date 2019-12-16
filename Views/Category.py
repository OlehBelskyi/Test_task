from flask.views import MethodView
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

from Services.CategoryService import CategorySevice
from init import InitApp


class Category(MethodView):

    def __init__(self):
        self.engine = create_engine(InitApp.db_uri())

    def get(self):
        user_id = request.args['user_id']
        session = sessionmaker(bind=self.engine)()
        categories = CategorySevice(session).get_all_users_categories(user_id)
        session.close()

        responce = dict()
        counter = 0

        for category in categories:
            responce[counter] = {
                "id": category.id,
                "title": category.title,
                "user_id": category.user_id
            }

            counter += 1

        return jsonify(responce)

    def post(self):
        try:
            data = request.json

            session = sessionmaker(bind=self.engine)()
            CategorySevice(session).add_category(data["title"], data["user_id"])
            session.commit()
            session.close()

            return jsonify({
                "message": "Category created"
            })
        except IntegrityError:
            return jsonify({
                "message": "No such order"
            })
        except KeyError:
            return jsonify({
                "message": "Wrong input data"
            })

    def put(self):
        pass

    def delete(self):
        pass
