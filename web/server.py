import numpy as np
from flask import Flask, jsonify, request
from datetime import datetime
from database import execute_query
from model.engine import PR_ENGINE_CLASSES

app = Flask(__name__)
query = "select pzjar, pzpackage, pzclass from rules_241.pr_engineclasses"

#  export DYLD_LIBRARY_PATH=/Library/PostgreSQL/16/lib
environment = {
    'k8s': 'flask-dev'
}

"""
    fetches environment configurations
"""


@app.route("/environment")
def fetch_environment():
    return jsonify(environment)


@app.route("/")
def hell_world():
    pr1 = PR_ENGINE_CLASSES()
    print(pr1.count)
    print("request received from {0} at {1} and headers are {2}".format(request.remote_addr, datetime.now(),
                                                                        request.headers))
    result = {"incomes": [
        {
            'description': 'Salary',
            'amount': 5000
        }
    ], 'engineClasses': execute_query(query=query)}
    print("request served at ", datetime.now())

    return jsonify(result)
