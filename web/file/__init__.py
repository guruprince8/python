from pathlib import Path
from flask import jsonify, request
from flask_restful import Resource
from file.names import DataSet
from datetime import datetime

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


class FileRouter(Resource):
    def get(self):
        response = {'startTime': datetime.now(), 'message': 'hello world'}
        nd = DataSet()
        response["names"] = nd.getnamesbystate("AK", False)
        response["endTime"] = datetime.now()
        return jsonify(response)

    def post(self):
        data = request.get_json()
        return jsonify({'data': data})
