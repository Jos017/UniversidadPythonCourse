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

            cursor.execute(
                'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)',
                ('Juan', 'Perez', 'jperez@email.com')
            )

            cursor.execute(
                'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)',
                ('Peter', 'Parker', 'pparker@email.com')
            )

            person_id = input('Introduce the person id: ')
            sentence = 'SELECT * FROM persons WHERE person_id = %s'
            # When using %s as placeholder whe should provide the values as a tuple
            cursor.execute(sentence, (person_id,))
            register = cursor.fetchone()
            print(register)

except psycopg.DatabaseError as e:
    print(f'Error: {e}')
