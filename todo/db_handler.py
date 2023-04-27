import sqlite3
from contextlib import closing

from settings import database


def db_get(model):
    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {model};')
        value = cursor.fetchall()
        return value
