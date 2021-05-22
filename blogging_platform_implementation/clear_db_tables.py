#!/usr/bin/env python3

import psycopg2
from config import config

def clear_db_tables():
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Deleting DB tables...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('DROP SCHEMA public CASCADE')
        cur.execute('CREATE SCHEMA public')
        cur.execute('GRANT ALL ON SCHEMA public TO postgres')
        cur.execute('GRANT ALL ON SCHEMA public TO public')

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    conn.commit()
    cur.close()
    conn.close()
    
# *** MAIN ***
if __name__ == '__main__':
    clear_db_tables()
