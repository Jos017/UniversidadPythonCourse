import sys
from logger_base import log
from psycopg_pool import pool


class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool: pool.ConnectionPool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None or cls._pool.closed:
            try:
                cls._pool = pool.ConnectionPool(
                    min_size=cls._MIN_CONN,
                    max_size=cls._MAX_CONN,
                    kwargs={
                        'dbname': cls._DATABASE,
                        'user': cls._USERNAME,
                        'password': cls._PASSWORD,
                        'port': cls._DB_PORT,
                        'host': cls._HOST
                    }
                )
                log.debug(f'Connection pool successful: {cls._pool}')
                return cls._pool
            except pool.e.DatabaseError as e:
                log.error(f"Can't obtain a connection pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def close_pool(cls):
        cls.get_pool().close()
