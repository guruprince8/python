from flask import jsonify, request
from flask_restful import Resource


class HelloRouter(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

    def post(self):
        data = request.get_json()
        return jsonify({'data': data})
