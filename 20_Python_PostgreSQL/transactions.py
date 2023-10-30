# A transaction is a group of multiple steps into a single one
# A transaction is an all or nothing operation

# If all sentences executes successfully the operation
# is committed and the database is modified

# If one or more of the sentences is not successful
# the database rolls back to a state before the transaction

# When we use the context manager "with" the transactions do automatically
import psycopg

try:
    connection = psycopg.connect(
        user='postgres', password='admin', dbname='test_db')
    connection.autocommit = False
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS persons')

    cursor.execute('''
        CREATE TABLE persons (
            person_id serial PRIMARY KEY,
            name varchar,
            last_name varchar,
            email varchar
        )
    ''')

    values = (
        ('Marcos', 'Cantu', 'mcantu@email.com'),
        ('Angel', 'Quintana', 'aquintana@email.com'),
        ('Maria', 'Gonzalez', 'mgonzalez@email.com'),
    )

    cursor.executemany(
        'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)',
        values
    )

    connection.commit()

    print('Transaction has ended')

except Exception as e:
    connection.rollback()
    print(f'Error: {e}')

finally:
    connection.close()
