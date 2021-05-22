#!/usr/bin/env python3

import psycopg2
from config import config
from sys import exit
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_db():
    try:
        print('Creating the blogging_db DATABASE')
        # not good practice to put pass inside source code but its simple example
        conn = psycopg2.connect("dbname = 'postgres' user = 'postgres' password = 'pass1234'") 
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
        cur = conn.cursor()

        db_name = 'blogging_db' # arbitrary name of database 
        cur.execute('CREATE DATABASE ' + db_name +';')
    except:
        cur.close()
        conn.close()

def create_db_tables():
    """ Connect to the PostgreSQL database server and create the posts table"""
    
    commands = (
                """

                CREATE TABLE users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(25) NOT NULL UNIQUE
                )

                """,

                """

                CREATE TABLE posts (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                main_body VARCHAR(1000),
                writer VARCHAR(25) NOT NULL REFERENCES users(username),
                date VARCHAR(25) NOT NULL
                )
                
                """
            )

    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # create posts table
        for command in commands:
            cur.execute(command)    

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
	    # close the communication with the PostgreSQL
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        cur.close()
        conn.close()
        exit(1)

# *** MAIN ***
if __name__ == '__main__':
    create_db()
    create_db_tables()