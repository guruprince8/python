import os
import psycopg2
from config import load_config

def connect(configuration):
    try:
        with psycopg2.connect(**configuration) as conn:
            print('connect to sql')
            with conn.cursor() as cur:
                cur.execute("select * from ml.vendors")
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (psycopg2.DatabaseError, Exception) as err:
        print("Error is ",err)

connect(load_config())