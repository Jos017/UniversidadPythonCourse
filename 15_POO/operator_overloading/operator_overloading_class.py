class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload "+"
    # obj_1 + obj_2
    # obj_1.__add__(obj_2)
    def __add__(self, other):
        return f'{self.name} {other.name}'

    # Overload "_"
    # obj_1 _ obj_2
    # obj_1.__sub__(obj_2)
    def __sub__(self, other):
        return f'{self.age} {other.age}'

person_1 = Person('Juan', 28)
person_2 = Person('Carlos', 20)

print(person_1 + person_2)
print(person_1 - person_2)
