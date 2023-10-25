class Person:
    person_counter = 0

    @classmethod
    def _get_next_id(cls):
        cls.person_counter += 1
        return cls.person_counter

    def __init__(self, name, age):
        self.id_person = self._get_next_id()
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person: [Id: {self.id_person}, Name: {self.name}, Age: {self.age}]'


person_1 = Person('Juan', 28)
person_2 = Person('Peter', 21)
person_3 = Person('Jake', 18)
person_4 = Person('Alan', 34)

print(person_1)
print(person_2)
print(person_3)
print(person_4)
