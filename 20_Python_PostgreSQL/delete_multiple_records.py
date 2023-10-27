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

            # Delete multiple records from table persons
            sentence = 'DELETE FROM persons WHERE person_id = ANY(%s)'
            user_input = input(
                'Provide multiple person_id to delete (Separated by commas): ')
            records_id = user_input.split(',')
            cursor.execute(sentence, (records_id,))
            # Number of records affected by the precedent sentence
            updated_records = cursor.rowcount
            print(f'Deleted Records: {updated_records}')

            cursor.execute('SELECT * FROM persons ORDER BY person_id ASC')
            records = cursor.fetchall()
            print(records)

except psycopg.DatabaseError as e:
    print(f'Error: {e}')
