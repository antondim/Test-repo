#!/usr/bin/env python3

import psycopg2
from config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def clear_db():
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'pass1234'")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
        cur = conn.cursor()

        db_name = 'blogging_db'
        cur.execute('DROP DATABASE ' + db_name +';')
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
   
    cur.close()
    conn.close()
    
# *** MAIN ***
if __name__ == '__main__':
    clear_db()
