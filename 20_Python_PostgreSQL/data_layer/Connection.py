import sys
import psycopg as db
from logger_base import log


class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _connection = None
    _cursor = None

    @classmethod
    def get_connection(cls) -> db.Connection:
        if cls._connection is None or cls._connection.closed:
            try:
                cls._connection = db.connect(
                    dbname=cls._DATABASE,
                    host=cls._HOST,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    user=cls._USERNAME,
                )
                log.debug(f'Connection Successful: {cls._connection}')
                return cls._connection
            except db.DatabaseError as e:
                log.error(f'An connection error has ocurred: {e}')
                sys.exit()
        else:
            return cls._connection

    @classmethod
    def get_cursor(cls) -> db.Cursor:
        if cls._cursor is None or cls._cursor.closed:
            try:
                cls._cursor = cls.get_connection().cursor()
                log.debug(f'Cursor Successful: {cls._cursor}')
                return cls._cursor
            except db.DatabaseError as e:
                log.error(f'A cursor error has ocurred: {e}')
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    Connection.get_connection()
    Connection.get_cursor()
