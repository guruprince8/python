from configparser import ConfigParser
import psycopg2
# import os
import pkgutil
from random import randint

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


def load_config(filename="database.ini", section="postgres"):
    """
        function to load database configuration taking filename and section as input parameters
        returns a dictionary
        currently supported databases are
        1. postgres
    """
    parser = ConfigParser()
    content = pkgutil.get_data('database', filename)
    if content is not None:
        parser.read_string(content.decode('utf-8'))
    else:
        raise Exception('failed to load database configuration from file ', filename)
    dbconfig = {}
    print(parser.sections())
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            dbconfig[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in filename {1}'.format(section, filename))
    return dbconfig


def db_connection():
    conn = None
    try:
        dbconfig = load_config(filename="database.ini", section="postgres")
        conn = psycopg2.connect(**dbconfig)
    except psycopg2.Error as err:
        print(f"Database connection failed: {err}")
    return conn


class DBConnectionPool:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnectionPool, cls).__new__(cls)
            cls.instance.max_connections = 10
            cls.instance.active_connections = [0] * cls.instance.max_connections
            for index, value in enumerate(cls.instance.active_connections):
                cls.instance.active_connections[index] = db_connection()
        return cls.instance


def execute_query(query: str):
    results = []
    rowcount = 0
    record = {}
    """
        function executes query and return the result set
        takes sql query as input parameter
    """
    connection = DBConnectionPool().instance.active_connections[randint(0, 9)]
    if connection is not None:
        try:
            with connection.cursor() as cur:
                cur.execute(query)
                rowcount = cur.rowcount
                column_names = [desc[0] for desc in cur.description]
                row = cur.fetchone()
                while row is not None:
                    for index, value in enumerate(column_names):
                        record[column_names[index]] = row[index]
                    results.append(record)
                    row = cur.fetchone()
        except (psycopg2.DatabaseError, Exception) as err:
            print("Error is ", err)
    else:
        raise Exception('failed execute query due as db connection not acquired')
    return results
