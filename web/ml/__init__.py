from flask import jsonify, request
from flask_restful import Resource


class MLRouter(Resource):
    def get(self):
        return jsonify(({'resource': 'ml'}))

