# Encapsulation refers to group data as methods,
# attributes and information within a single unit
# The most common example is in a class

# In a class we can have three types of data
# Public: Accesible within or outside of a class (any name)
# Protected: Accesible within the class and it's sub-clases (starts with underscore _)
# Private: Accesible only within a class (starts with double underscore __)

class Person:
    def __init__(self, name, last_name, age):
        # Public attribute name
        self.name = name

        # Protected attribute last_name (most used)
        self._last_name = last_name

        # Private attribute age
        self.__age = age

    def show_details(self):
        print(f'Person: {self.name} {self._last_name} {self.__age}')


# A public data can by modified and also a protected attribute
person_1 = Person('Juan', 'Perez', 28)
person_1.name = 'Peter'

# Its a warning if we modify a protected member
person_1._last_name = 'Parker'
person_1.show_details()

# A Private attribute cannot be modified
person_2 = Person('Juan', 'Perez', 20)
person_2.__age = 30
person_2.show_details()
