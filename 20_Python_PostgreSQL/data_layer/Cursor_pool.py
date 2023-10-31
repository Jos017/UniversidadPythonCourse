from Connection_pool import Connection
from logger_base import log


class Cursor_pool:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('Begin method with __enter__')
        self._connection = Connection.get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exception_type, exception_value, exception_detail):
        log.debug(' Method __exit__ is executed')
        if exception_value:
            self._connection.rollback()
            log.error(f'An exception occurred: {exception_value} {
                      exception_type} {exception_detail}')
        else:
            self._connection.commit()
            log.debug('Transaction commit')
        self._cursor.close()
        # Connection.release_connection(self._connection)
