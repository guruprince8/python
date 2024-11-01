import numpy as np
from flask import Flask, jsonify, request
import json
from datetime import datetime
from postgresql import execute_query

app = Flask(__name__)
query = "select pzjar, pzpackage, pzclass from rules_241.pr_engineclasses"

#  export DYLD_LIBRARY_PATH=/Library/PostgreSQL/16/lib

@app.route("/")
def hell_world():
    print("request receive at ", datetime.now())
    result = {"incomes": [
        {
            'description': 'Salary',
            'amount': 5000
        }
    ], 'engineClasses': execute_query(query=query)}
    print("request served at ", datetime.now())

    return jsonify(result)
