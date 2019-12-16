from flask.views import MethodView
from flask import request, jsonify


class Test(MethodView):
    def get(self):
        return "this is a test"

    def post(self):
        data = request.json
        print(data)
        return jsonify(data)
