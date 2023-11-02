class Person:
    person_counter: 0

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


person_1 = Person('Juan', 'Perez')

# Show all attributes of an object as a dictionary
# __dict__
print(person_1.__dict__)

# Create an attribute
# the new attribute will be available in this object
person_1.new_attribute = 10
print(person_1.__dict__)
