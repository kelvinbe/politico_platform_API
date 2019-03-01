import psycopg2
import os
from flask import current_app 


# host = 'localhost'
# user = 'politico'
# port = 5432
# password = 'root'
# dbname = 'politico'

con_url = "dbname='politico' host='127.0.0.1' port='5432' user='politico' password='root'"
test_url = "dbname='politico' host='127.0.0.1' port='5432' user='politico' password='root'"

#url for database connection
#uri = os.getenv('DATABASE_URL')


#url for test database connection
#test_uri = os.getenv('DATABSE_TEST_URL')


#return connection
def connection(url):
    connect = psycopg2.connect(url)
    return connect
    


#return connection and creates tables
def init_db():
    connect = connection(con_url)
    cur = connect.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    connect.commit()
    return connect
    


#return connection and creates tables(TDD)
def init_test_db(test_url):
    connect = connection(test_url)
    cur = connect.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    connect.commit()
    return connect


#delete all tables after tests have been run
def destroydb():
    connect = connection(test_url)
    cur = connect.cursor()
    votes = """ DROP TABLES IF EXISTS votes CASCADE; """
    users = """ DROP TABLES IF EXISTS users CASCADE; """
    offices = """ DROP TABLES IF EXISTS offices CASCADE; """

    for query in queries:
        cur.execute(query)
    connect.commit()


#contain all table creation queries
def tables():
    users = """ CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    name CHARACTER varying(50) NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(50),
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
    password character varying(500) NOT NULL);"""

    votes = """ CREATE TABLE IF NOT EXISTS votes (
    vote_id serial PRIMARY KEY NOT NULL,
    voter character varying(20) NOT NULL,
    candidate character varying(50),
    office character varying(50),
    voted_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL);"""

    offices = """ CREATE TABLE IF NOT EXISTS offices (
        
        office_id serial PRIMARY KEY NOT NULL,
        type character varying(50),
        name CHARACTER varying(50) NOT NULL,
        created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL);"""

    parties = """ CREATE TABLE IF NOT EXISTS parties (
        
        party_id serial PRIMARY KEY NOT NULL,
        hqAddress character varying(50),
        logourl CHARACTER varying(50) NOT NULL,
        name CHARACTER varying(50) NOT NULL,
        created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL);"""

    queries = [votes, users, offices, parties]
    return queries
