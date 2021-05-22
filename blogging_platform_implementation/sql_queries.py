#!/usr/bin/env python3

import psycopg2
from config import config
from sys import exit

def sql_query_1():
    cur.execute('SELECT * FROM posts ORDER BY date DESC;')

def sql_query_2():
    # get all posts from user == 'user1'
    cur.execute("SELECT * FROM posts WHERE posts.writer = 'user1';")

def sql_query_3():
     cur.execute("SELECT * FROM posts WHERE position('programming' in main_body)>0;")

def sql_query_4():
    # posts from October of 2020
    cur.execute("SELECT * FROM posts WHERE extract(month FROM date::timestamp) = 10 AND extract(year from date::timestamp)=2020;")

def sql_query_5():
    cur.execute("SELECT * FROM posts WHERE position('programming' in main_body)>0 AND position('exercise' in main_body)>0;")

def sql_query_6():
    cur.execute("SELECT writer, COUNT(*) FROM posts GROUP BY writer ORDER BY count(*) DESC LIMIT 1;")

# *** MAIN ***
if __name__== '__main__':
    try:
        params = config()

        # connect to the PostgreSQL server
        print('\n*** SQL QUERIES ***\n')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        #
        print('\n*** SQL QUERY 1 - SORTED based on date column ***\n')
        sql_query_1()

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        print('\n*** SQL QUERY 2 - all posts from user1 ***\n\n')
        sql_query_2()

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        print('\n*** SQL QUERY 3 - all posts with keyword ~programming~ ***\n\n')
        sql_query_3()
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        print('\n*** SQL QUERY 4 - all posts added in October (10th month) of  year 2020 ***\n\n')
        sql_query_4()

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        print('\n*** SQL QUERY 5 - all posts with both keywords ~programming~ and ~exercise~ ***\n\n')
        sql_query_5()

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        print('\n*** SQL QUERY 6 - user with the most posts ***\n\n')
        sql_query_6()

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

