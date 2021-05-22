# Test-repo
Repo containing palindrome function and a simple database, both implemented on Python.

## Prerequisites
- Linux OS
- virtualenv Python module
- psycopg2 (PostgreSQL Python module / adapter)
- Python3 pip

## Set things up
**1) Install python3-pip and virtual env Python modules** :

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```
**2) Create and activate a Python3 virtual environment** :
```
mkdir ~/virtual_envs
virtualenv -p python3 test_venv
source ~/virtual_envs/test_venv/bin/activate
```
**3) Install PostgreSQL Python Adapte/module** :

```
pip3 install psycopg2
```
## Download repository
```
https://github.com/antondim/Test-repo.git
```
## Palindrome 
Inside Test-repo directory just execute the python script
```
./palindrome.py
```
## Blogging Platform
Local database created with PostgreSQL via Python

- Login to the PostgreSQL server
```
sudo -u postgres psql
```
I chose to put a simple password (pass1234) and our code uses that password as default. 
So inside server's console:
```
\password
```
and use 'pass1234' as password.

- Create new database named 'blogging_db' + 2 x Tables for users and for posts:
```
./create_db_tables.py
```
- Insert 10 x posts (posts 1-10) and 3 x user (user1-3) entries into the tables:
```
./insert_into_db.py
```
- Perform the SQL queries on the created database:
```
./sql_queries.py
```
**Extra scripts where created in order to DROP Database (drop_db.py) and CLEAR/DROP tables (clear_db_tables.py)**

## Inside PostgreSQL server
1) Login
```
sudo -u postgres psql
```
2) Check the databases 
```
\l
```
3) Connect to database 'blogging_db'
```
\c blogging_db
```
4) Check all post intries of posts table
```
SELECT * FROM posts;
```
5) Check all user entries of users table
```
SELECT * FROM users;
```
6) SQL queries
You also can copy and paste the SQL code used in 'sql_queries.py' script , inside the PostgreSQL server's environment to get the results.
