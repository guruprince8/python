from flask import jsonify, request
from flask_restful import Resource
import numpy as np
from _datetime import datetime

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


class DSARouter(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

    def post(self):
        data = request.get_json()
        data["startTime"] = datetime.now()
        ar = np.arange(100000)
        print(ar)
        data["array"] = ar.tolist()
        data["endTime"] = datetime.now()
        return jsonify({'data': data})
