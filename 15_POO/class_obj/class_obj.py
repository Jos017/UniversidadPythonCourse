# A class is like an object constructor, or a "blueprint" for creating objects
# To create a class we use the keyword "class"
# Classes names starts with capital letter (Convention)
class Person:
    # Constructor method
    # The constructor method allow us to create attributes
    # in the moment of creating an instance (object)
    def __init__(self, name, last_name, age):
        self.status = 'Learning Python'
        self.name = name
        self.last_name = last_name
        self.age = age

    # To create a class method we define as functions
    # A method is a function available in all instances of a class
    def show_details(self):
        print(f'Persona: {self.name}, {self.last_name}, {self.age}')


# To create an object Person whe only call the class
# and define the values needed in the constructor method
# When creating an instance the param "self" is inferred so its not needed
person_1 = Person('Jose', 'Rios', 29)

# To obtain a object attributes we use a "."
print(f'Person 1: {person_1.status}, {person_1.age}, {
      person_1.last_name}, {person_1.name}')

# You can modify an attribute of an object assigning a new value to the attribute
person_1.name = 'Alan'
print(f'Person 1: {person_1.status}, {person_1.age}, {
      person_1.last_name}, {person_1.name}')

# You can add an attribute to an object only available in that object
person_1.phone = '445545'
print(person_1.phone)

# We can create other object with the same class
person_2 = Person('Juan', 'Perez', 22)
print(f'Person 2: {person_2.status}, {person_2.age}, {
      person_2.last_name}, {person_2.name}')

# Calling class methods
person_1.show_details()
person_2.show_details()
