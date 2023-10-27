Important for this section:
  - Install PostgreSQL
    - port: 5432
    - password: admin
  - Create a new database: test_db
    - Add a table "persons" with (person_id, name, last_name, email)
  - Configure and activate a virtual environment(venv) venv
  - Install Package "psycopg" to handle connection between Python and PostgreSQL
    $ pip install psycopg[binary]
