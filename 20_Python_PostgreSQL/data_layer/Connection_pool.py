import sys
from psycopg_pool import pool
from logger_base import log


class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def get_pool(cls) -> pool.ConnectionPool:
        if cls._pool is None or cls._pool.closed:
            try:
                cls._pool = pool.ConnectionPool(
                    min_size=cls._MIN_CON,
                    max_size=cls._MAX_CON,
                    kwargs={
                        'password': cls._PASSWORD,
                        'dbname': cls._DATABASE,
                        'user': cls._USERNAME,
                        'port': cls._DB_PORT,
                        'host': cls._HOST
                    },
                )
                log.debug(f'Connection pool Successful created: {cls._pool}')
                return cls._pool
            except pool.e.DatabaseError as e:
                log.error(f'Cannot obtain the connection pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_connection(cls) -> pool.Connection:
        # connection = cls.get_pool().getconn()
        connection = cls.get_pool().connection()
        log.debug(f'Connection obtained from pool: {connection}')
        return connection

    # @classmethod
    # def release_connection(cls, connection):
    #     cls.get_pool().putconn(connection)
    #     log.debug(f'Release pool connection: {connection}')

    @classmethod
    def close_all(cls):
        cls.get_pool().close()


if __name__ == '__main__':
    with Connection.get_pool():
        with Connection.get_connection():
            pass
        with Connection.get_connection():
            pass
        with Connection.get_connection():
            pass
        with Connection.get_connection():
            pass
        with Connection.get_connection():
            pass
        Connection.close_all()
        with Connection.get_connection():
            pass

    # connection_1 = Connection.get_connection()
    # connection_2 = Connection.get_connection()
    # connection_3 = Connection.get_connection()
    # connection_4 = Connection.get_connection()
    # connection_5 = Connection.get_connection()
    # connection_6 = Connection.get_connection()
    # connection_6 = Connection.get_connection()
