import sqlite3
from contextlib import closing

from settings import database
from utils import form_filter_request


def db_get(model, filter_fields=None):
    if filter_fields:
        filters = form_filter_request(filter_fields)
    else:
        filters = ''

    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {model}{filters};')
        value = cursor.fetchall()
        return value
