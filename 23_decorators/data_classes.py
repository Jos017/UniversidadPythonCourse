# dataclasses is a module that provides decorators
from dataclasses import dataclass
from typing import ClassVar

# decorator dataclass


@dataclass
class Person:
    # Instance variables
    name: str
    last_name: str

    # Class variables
    person_counter: ClassVar[int] = 0

    # If we want to validate some values post init
    def __post_init__(self):
        if not self.name:
            raise ValueError('Empty name provided')
        if not self.last_name:
            raise ValueError('Empty last name provided')


person_1 = Person('Juan', 'Perez')
print(f'{person_1!r}')

# Class variable
print(f'Class variable: {Person.person_counter}')

# Instance variable
print(person_1.__dict__)

# Variable with empty values
# empty_person = Person('', '')
# print(empty_person)
