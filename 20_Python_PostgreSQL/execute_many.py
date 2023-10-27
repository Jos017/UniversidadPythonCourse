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

            sentence = 'SELECT * FROM persons'
            cursor.execute(sentence)
            registers = cursor.fetchall()
            print(registers)

except psycopg.DatabaseError as e:
    print(f'Error: {e}')
