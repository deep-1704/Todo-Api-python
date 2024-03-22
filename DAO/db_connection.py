import os
from dotenv import load_dotenv
import pymysql.cursors

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')


def get_db_connection():
    return pymysql.connect(user=username, password=password,
                           host=host, database=database,
                           cursorclass=pymysql.cursors.DictCursor)
