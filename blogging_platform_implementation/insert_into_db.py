#!/usr/bin/env python3

import psycopg2
from config import config
from sys import exit

dbKeywords = ['programming', 'learning', 'exercise']
user_names = ['user1', 'user2', 'user3']
manual_posts = [('post1', 'this is a testing post for a programming exercise','user1','2020-10-04'),
                ('post2', 'this is a testing post for a programming programming programming exercise','user3','2021-11-09'),
                ('post3', 'this is a testing post for ','user2','2019-10-04'),
                ('post4', 'this is a testing post for a programming exercise learning','user2','2020-10-10'),
                ('post5', 'this is a testing post for a programming exercise','user1','2020-04-28'),
                ('post6', 'this is a testing post for a programming exercise','user1','2020-09-09'),
                ('post7', 'this is a testing post for a programming exercise','user2','2021-09-27'),
                ('post8', 'this is a testing post for a programming exercise','user1','2019-07-16'),
                ('post9', 'this is a testing post for a programming exercise','user3','2021-10-01'),
                ('post10','this is a testing post for a programming exercise','user1','2020-05-12')]

def keyword_exists(dbKeywords, main_body):
    '''Function that checks if at least 
       one of the keywords exists in main body'''

    if all(keyword not in main_body for keyword in dbKeywords ):
        print('Error...main body contains no keywords')
        return False
    else:
        return True

def keyword_uniqueness(dbKeywords, main_body):
    '''Function that checks if main body of 
       post contains a keyword more than once'''

    words = main_body.split()

    for keyword in dbKeywords:
        count = 0
        count = words.count(keyword)
        
        if count > 1:
            print('Error...main body contains a keyword more than once...skipping INSERT...')
            return False
        else:
            continue

    return True

def load_user(username):
    try:
        cur.execute(""" INSERT INTO users(username) VALUES(%s);""", (username,))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit(1)

def load_post(post):
    try:
        insert_query = """INSERT INTO posts (title, main_body, writer, date) VALUES(
                        %s,%s,%s,%s);"""    
        cur.execute(insert_query, post)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit(1)

# *** MAIN ***
if __name__ == '__main__':

    try:
        params = config()

        # connect to the PostgreSQL server
        print('\n*** Inserting users and posts into the PostgreSQL database... ***\n')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

#      Insert 3 users inside our database in a users table 
        for username in user_names:
            load_user(username)

        for post in manual_posts:
            if  keyword_exists(dbKeywords, str(post[1])) and keyword_uniqueness(dbKeywords, str(post[1])): 
                load_post(post)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur.close()
        conn.close()
        exit(1)
    
    try:
        conn.commit()
    except:
        conn.rollback()
        print('Could not commint changes... rolling back...')
        exit(1)
    finally:
        conn.close()
