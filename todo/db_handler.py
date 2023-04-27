import sqlite3
from contextlib import closing

from settings import database
from utils import form_filter_request


def db_get(model: str, filter_fields: dict | None = None) -> list[dict]:
    if filter_fields:
        filters = form_filter_request(filter_fields)
    else:
        filters = ''

    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {model}{filters};')
        rows = cursor.fetchall()
        values = [dict(row) for row in rows]
        return values
