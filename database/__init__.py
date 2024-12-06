from configparser import ConfigParser
import psycopg2

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


def load_config(filename="database.ini", section="postgres"):
    """
        function to load database configuration taking filename and section as input parameters
        returns a dictionary
        currently supported databases are postgres
    """
    parser = ConfigParser()
    parser.read(filename)
    dbconfig = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            dbconfig[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in filename'.format(section, filename))
    return dbconfig


def execute_query(query: str):
    """
        function executes query and return the result set
    """
    configuration = load_config()
    results = []
    try:
        with psycopg2.connect(**configuration) as conn:
            print('connected to sql')
            with conn.cursor() as cur:
                cur.execute(query)
                print(f'Total number of records fetched are {0}', cur.rowcount)
                row = cur.fetchone()
                while row is not None:
                    row = cur.fetchone()
                    if row is not None:
                        results.append({'pzjar': row[0], 'pzpackage': row[1], 'pzclass': row[2]})
    except (psycopg2.DatabaseError, Exception) as err:
        print("Error is ", err)
    return results
