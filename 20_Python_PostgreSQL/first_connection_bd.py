# Import the module
import psycopg

connection = psycopg.connect(
    user='postgres',
    password='admin',
    dbname='test_db',
    port='5432',
    host='127.0.0.1'
)

try:
    # Connect to an existing database
    # When using the context manager it closes the connection without closing it manually
    with connection:

        # Open a cursor to perform database operations
        with connection.cursor() as cursor:
            # Delete table if exists
            cursor.execute('DROP TABLE IF EXISTS persons')

            # Execute a command
            cursor.execute('''
                CREATE TABLE persons (
                    person_id serial PRIMARY KEY,
                    name varchar,
                    last_name varchar,
                    email varchar
                )
            ''')

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)``
            cursor.execute(
                'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)',
                ('Juan', 'Perez', 'jperez@email.com')
            )
            cursor.execute(
                'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)',
                ('Peter', 'Parker', 'pparker@email.com')
            )

            # Query the database and obtain data as Python objects
            cursor.execute('SELECT * FROM persons')
            records = cursor.fetchall()  # ==> Will return a list of several items

            print(records)

except psycopg.DatabaseError as e:
    print(f'Error: {type(e)}')
