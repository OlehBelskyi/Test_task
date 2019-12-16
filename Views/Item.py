
from flask.views import MethodView
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Services.ItemService import ItemService
from init import InitApp


class Item(MethodView):

    def __init__(self):
        self.engine = create_engine(InitApp.db_uri())

    def get(self):
        user_id = request.args['user_id']
        session = sessionmaker(bind=self.engine)()
        items = ItemService(session).get_all_users_items(user_id)
        session.close()

        responce = dict()
        counter = 0

        for item in items:
            responce[counter] = {
                "id": item.id,
                "title": item.title,
                "price": item.price,
                "user_id": item.user_id,
                "category_id": item.category_id,
            }

            counter += 1

        return jsonify(responce)

    def post(self):
        try:
            data = request.json

            session = sessionmaker(bind=self.engine)()
            ItemService(session).create_item(data["title"], data["price"], data["user_id"],
                                             data["category_id"])
            session.commit()
            session.close()

            return jsonify({
                "message": "Item created"
            })
        except KeyError:
            return jsonify({
                "message": "Wrong input data"
            })

    def put(self):
        pass

    def delete(self):
        pass