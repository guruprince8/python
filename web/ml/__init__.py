from flask import jsonify, request, make_response
from flask_restful import Resource
import csv
from database import execute_query



__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


class MLRouter(Resource):
    """"
     REST ML router returns the data based on dataset requested and source
    """

    def get(self):
        """"
             REST ML router returns the data based on dataset requested and source
        """
        dataset = request.args.get("dataset")
        source = request.args.get("source")
        response = {'Access-Control-Allow-Origin':'https://localhost:3000'}
        if dataset == "naukri_data_science_jobs_india":
            if source == "database":
                response = make_response(
                    {'data': execute_query("select * from ml_dev.naukri_data_science_jobs_india;")}, 200)
                response.headers['Access-Control-Allow-Origin']='https://localhost:3000'
            elif source == "file":
                with open('../../datasets/naukri_data_science_jobs_india.csv', 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    data = [row for row in csv_reader]
                    response = make_response({'data': data}, 200)
        return response
