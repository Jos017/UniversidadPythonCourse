import psycopg

try:
    with psycopg.connect(user='postgres', password='admin', dbname='test_db') as connection:
        with connection.cursor() as cursor:
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

            # Update multiple records
            sentence = '''
                UPDATE persons
                   SET name=(%s), last_name=(%s), email=(%s)
                 WHERE person_id=(%s)'''
            values = (
                ('Peter', 'Parker', 'pparker@email.com', 1),
                ('Tony', 'Stark', 'tstark@email.com', 2)
            )
            cursor.executemany(sentence, values)
            # Number of records affected by the precedent sentence
            updated_records = cursor.rowcount
            print(f'Updated Records: {updated_records}')

            cursor.execute('SELECT * FROM persons ORDER BY person_id ASC')
            records = cursor.fetchall()
            print(records)

except psycopg.DatabaseError as e:
    print(f'Error: {e}')
