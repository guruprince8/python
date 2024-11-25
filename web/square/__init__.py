from flask import Flask, jsonify, request
from flask_restful import Resource

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


class SquareRouter(Resource):
    def get(self, num):
        return jsonify(({'square': num ** 2}))
