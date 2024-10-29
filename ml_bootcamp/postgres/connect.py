import os
import psycopg2
from config import load_config

def connect(configuration,query:str):
    try:
        with psycopg2.connect(**configuration) as conn:
            print('connect to sql')
            with conn.cursor() as cur:
                cur.execute(query)
                print(f'Total number of records fetched are {0}',cur.rowcount)
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (psycopg2.DatabaseError, Exception) as err:
        print("Error is ",err)
query = "select * from ml.vendors"
query = "select * from rules_241.pr_engineclasses"
connect(load_config(),query)