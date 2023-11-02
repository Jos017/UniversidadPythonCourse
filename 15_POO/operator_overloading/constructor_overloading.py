# In python there is no constructor overloading
# But it is posible to simulate this behavior
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    # Simulating constructor overloading
    @classmethod
    def create_empty_person(cls):
        return cls(None, None)

    @classmethod
    def create_full_person(cls, name, last_name):
        return cls(f'{name}-full', f'{last_name}-full')

    def __str__(self):
        return f'"name": {self.name}, "last_name": {self.last_name}'


person_1 = Person('Juan', 'Perez')
person_2 = Person.create_empty_person()
person_3 = Person.create_full_person('Peter', 'Parker')

print(person_1)
print(person_2)
print(person_3)
