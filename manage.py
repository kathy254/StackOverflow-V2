import psycopg2
from psycopg2.extras import RealDictCursor
import datetime
import os
from sys import modules

from instance.config import app_config, db_url, test_url

class DbSetup(object):
    '''this class initializes the database connections'''
    def __init__(self, config_name):
        self.connection = None

    def createConnection(self):
        try:
            if 'pytest' in modules:
                URL = test_url
            if app_config['development']:
                URL = db_url
            self.connection = psycopg2.connect(database = URL)
        except Exception:
            try:
                if app_config['production']:
                    self.connection = psycopg2.connect(os.environ["DATABASE_URL"],
                                                                sslmode = 'require')
            except Exception:
                return "Database connection failed."
        
        self.connection.autocommit =  True
        return self.connection


    def closeConnection(self):
        return self.connection.close()


    def createTables(self):
        cursor = self.createConnection().cursor(cursor_factory=RealDictCursor)
        tables = [
            """CREATE TABLE IF NONE EXISTS user_accounts(
                id serial PRIMARY KEY NOT NULL,
                email_address varchar(100) UNIQUE NOT NULL,
                username varchar(100) NOT UNIQUE NULL,
                password varchar(50) NOT NULL,
                member_since timestamp with time zone DEFAULT('now'::text)::date NOT NULL
            )"""
        ]
        for table in tables:
            cursor.execute(table)
        self.connection.commit()
        self.connection.close()


    def dropTables(self):
        cursor = self.createConnection().cursor(cursor_factory=RealDictCursor)
        table1 = """DROP TABLE IF EXISTS test_users CASCADE"""
        table2 = """DROP TABLE IF EXISTS test_questions CASCADE"""
        table3 = """DROP TABLE IF EXISTS test_answers CASCADE"""

        queries = [table1, table2, table3]
        for query in queries:
            cursor.execute(query)
        self.connection.commit()
        self.connection.close()