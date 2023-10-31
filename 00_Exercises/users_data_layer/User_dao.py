from Connection import Connection
from logger_base import log
from User import User


class User_dao:
    _SELECT = 'SELECT * FROM users ORDER BY user_id'
    _INSERT = 'INSERT INTO users(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE users SET username=(%s), password=(%s) WHERE user_id=(%s)'
    _DELETE = 'DELETE FROM users WHERE user_id=(%s)'

    @classmethod
    def select(cls):
        with Connection.get_pool().connection() as conn:
            log.debug(f'Connection successful: {conn}')
            with conn.cursor() as cursor:
                log.debug('Select users')
                cursor.execute(cls._SELECT)
                records = cursor.fetchall()
                users = []
                for record in records:
                    user = User(record[0], record[1], record[2])
                    users.append(user)
                return users

    @classmethod
    def insert(cls, user: User):
        with Connection.get_pool().connection() as conn:
            log.debug(f'Connection successful: {conn}')
            with conn.cursor() as cursor:
                log.debug(f'Insert user: [{user.username} {user.password}]')
                values = (user.username, user.password)
                cursor.execute(cls._INSERT, values)
                return cursor.rowcount

    @classmethod
    def update(cls, user: User):
        with Connection.get_pool().connection() as conn:
            log.debug(f'Connection successful: {conn}')
            with conn.cursor() as cursor:
                log.debug(
                    f'Update user: [{user.user_id} {
                        user.username} {user.password}]'
                )
                values = (user.username, user.password, user.user_id)
                cursor.execute(cls._UPDATE, values)
                return cursor.rowcount

    @classmethod
    def delete(cls, user: User):
        with Connection.get_pool().connection() as conn:
            log.debug(f'Connection successful: {conn}')
            with conn.cursor() as cursor:
                log.debug(f'Delete user: [{user.user_id}]')
                values = (user.user_id,)
                cursor.execute(cls._DELETE, values)
                return cursor.rowcount
