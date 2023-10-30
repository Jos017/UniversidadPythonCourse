from logger_base import log


class Person:
    def __init__(self, person_id=None, name=None, last_name=None, email=None):
        self._person_id = person_id
        self._name = name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return f'\n Person Id: {self._person_id}, Name: {self._name}, \n Last name: {self._last_name}, Email: {self._email}'

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    person_1 = Person(1, 'Juan', 'Perez', 'jperez@email.com')
    log.debug(person_1)
    # Insert simulation
    person_2 = Person(
        person_id=2,
        name='Juan',
        last_name='Perez',
        email='jperez@email.com'
    )
    log.debug(person_2)
    person_3 = Person(person_id=3)
    log.debug(person_3)
