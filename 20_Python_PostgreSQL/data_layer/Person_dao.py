'''
DAO (Data Access Object)
CRUD (Create Read Update Delete)
'''
from logger_base import log
from Connection_pool import Connection
from Person import Person


class Person_dao:
    _SELECT = 'SELECT * FROM persons ORDER BY person_id'
    _INSERT = 'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE persons SET name=(%s), last_name=(%s), email=(%s) WHERE person_id=(%s)'
    _DELETE = 'DELETE FROM persons WHERE person_id=(%s)'

    @classmethod
    def select(cls):
        # with Connection.get_pool():
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls._SELECT)
                records = cursor.fetchall()
                persons = []
                for record in records:
                    person = Person(
                        record[0],
                        record[1],
                        record[2],
                        record[3]
                    )
                    persons.append(person)
                return persons

    @classmethod
    def insert(cls, person: Person):
        # with Connection.get_pool():
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                values = (person.name, person.last_name, person.email)
                cursor.execute(cls._INSERT, values)
                log.debug(f'Inserted person: {person}')
                return cursor.rowcount

    @classmethod
    def update(cls, person: Person):
        # with Connection.get_pool():
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                values = (
                    person.name,
                    person.last_name,
                    person.email,
                    person.person_id
                )
                cursor.execute(cls._UPDATE, values)
                log.debug(f'Updated person: {person}')
                return cursor.rowcount

    @classmethod
    def delete(cls, person: Person):
        # with Connection.get_pool():
        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                values = (person.person_id,)
                cursor.execute(cls._DELETE, values)
                log.debug(f'Deleted person: {person}')
                return cursor.rowcount


if __name__ == '__main__':
    # Insert a record
    person_1 = Person(
        name='Chapa',
        last_name='Bonaparte',
        email='cbonaparte@email.com',
    )
    inserted_persons = Person_dao.insert(person_1)
    log.debug(f'Inserted persons: {inserted_persons}')

    # Update a record
    person_1 = Person(1, 'Pedro', 'Stone', 'pstone@email.com')
    updated_persons = Person_dao.update(person_1)
    log.debug(f'Updated persons: {updated_persons}')

    # Delete a record
    person_1 = Person(person_id=25)
    deleted_persons = Person_dao.delete(person_1)
    log.debug(f'Deleted persons: {deleted_persons}')

    # Select objects
    persons_test = Person_dao.select()
    for person_test in persons_test:
        log.debug(person_test)
