import sqlite3
from contextlib import closing
from typing import Optional

from settings import database
from utils import form_filter_request


def db_get(model: str, filter_fields: Optional[dict] = None) -> list[dict]:
    if filter_fields:
        filters = form_filter_request(filter_fields)
    else:
        filters = ''

    query = f'SELECT * FROM {model}{filters};'
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        records = [dict(row) for row in rows]
        return records


def db_add(model: str, data: dict) -> list[dict]:
    keys = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    query = f'INSERT INTO {model} ({keys}) VALUES ({placeholders})'
    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        cursor.execute(query, tuple(data.values()))
        connection.commit()

        record = {'id': cursor.lastrowid, **data}
        return [record]
