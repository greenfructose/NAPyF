import sqlite3
from sqlite3 import Error

from NAPyF.Types import Field
from Settings import DB_TYPE, BASE_DIR
from NAPyF.Model import Model


def open_db_connection():
    con = None
    if DB_TYPE == 'sqlite3':
        try:
            print(BASE_DIR)
            con = sqlite3.connect(f'{BASE_DIR}/NAPyF.db')
        except Error as e:
            print(e)
        finally:
            if con:
                return con


def create_table(connection, model: Model):
    try:
        cursor = connection.cursor()
        model = model
        table, headers = model_to_sql(model)
        statement = f'CREATE TABLE {table} {headers}'
        cursor.execute(statement)
        connection.commit()
    except Error as e:
        print(e)


def insert(connection, model: Model):
    sqlite3.register_adapter(bool, int)
    sqlite3.register_converter("BOOLEAN", lambda v: bool(int(v)))
    cursor = connection.cursor()
    values = ""
    try:
        cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{model.name}'")
        if cursor.fetchone()[0] != 1:
            print(f'Table "{model.name}" does not exist, attempting to create . . .')
            create_table(connection, model)
    except Error as e:
        print(e)
    try:
        if DB_TYPE == 'sqlite3':
            for field in model.fields:
                if field["data_type"] == str:
                    data = field["data"]
                    values += f"'{data}', "
                else:
                    values += f'{field["data"]}, '
            values = values[:-2]
            statement = f'INSERT INTO {model.name} VALUES ' \
                        f'(NULL, {values})'
            cursor.execute(statement)
            connection.commit()
    except Error as e:
        print(e)


def model_to_sql(model: Model):
    table = model.name
    headers = ''
    if DB_TYPE == 'sqlite3':
        headers = f'({table}_id INTEGER PRIMARY KEY AUTOINCREMENT, '
        for field in model.fields:
            headers += f'{field["name"]} {python_type_to_sqlite3_type[field["data_type"]]}, '
        headers = headers[:-2] + ")"
    return table, headers


def list_tables(connection):
    cursor = connection.cursor()
    try:
        if DB_TYPE == 'sqlite3':
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table';"
            )
            print(cursor.fetchall())
    except Error as e:
        print(e)


python_type_to_sqlite3_type = {
    None: 'NULL',
    int: 'INTEGER',
    float: 'REAL',
    str: 'TEXT',
    bytes: 'BLOB',
    bool: 'BOOLEAN'
}