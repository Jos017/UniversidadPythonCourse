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

            for i in range(5):
                cursor.execute(
                    'INSERT INTO persons (name, last_name, email) VALUES (%s, %s, %s)',
                    (f'user-{i}', 'last', f'user{i}@email.com')
                )

            user_input = input(
                'Provide the id\'s to search (separated by commas): ')
            sentence = 'SELECT * FROM persons WHERE person_id = ANY(%s)'
            primary_keys = user_input.split(',')
            cursor.execute(sentence, (primary_keys,))
            registers = cursor.fetchall()
            print(registers)

except psycopg.DatabaseError as e:
    print(f'Error: {e}')
