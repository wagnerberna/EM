from src.static.message import *
import os
import psycopg2
from dotenv import load_dotenv
from src.utils.response import Response

response = Response()

load_dotenv()
DATABASE_LOCAL = os.getenv("DATABASE_LOCAL")
DATABASE_URL = os.getenv("DATABASE_URL")
POSTGRES_LOCAL = os.getenv("POSTGRES_LOCAL")


class Postgresql:
    def postgresql_connect(self):
        try:
            connection = psycopg2.connect(DATABASE_LOCAL, sslmode="require")
            return connection

        except Exception as error:
            return error

    def create_db(self, sql_query):
        connection = psycopg2.connect(POSTGRES_LOCAL, sslmode="require")
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(sql_query)
        cursor.close()
        connection.close()

    # add /update / delete
    def execute_modify(self, sql_query, data=None):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, data)
        connection.commit()
        count = cursor.rowcount
        cursor.close()
        connection.close()
        return count

    # get_one
    def fetch_one(self, sql_query, field=None):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, field)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result

    # get_all
    def fetch_all(self, sql_query, data=None):
        connection = self.postgresql_connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, data)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
