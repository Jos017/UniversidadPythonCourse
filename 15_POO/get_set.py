# Encapsulation refers to group data as methods,
# attributes and information within a single unit
# The most common example is in a class

# When we have protected or private members
# To avoid any warning we use setters and getters

# A setter is a method that is named the same as the protected member
# It allows to assign a value to a protected or private member

# A getter is a method that is named the same as the protected member
# It allows to obtain the value of a protected or private member

class Person:
    def __init__(self, name, last_name, age):
        self._name = name
        self._last_name = last_name
        self._age = age

    @property # Decorator, allows the getter methods behaves as an attribute
    def name(self): # Getter method
        print(f'Calling get method name: {self._name}')
        return self._name

    @name.setter # Decorator, allows the setter method behaves as an attribute
    def name(self, name): # Setter method
        print(f'Calling set method name with: {name}')
        self._name = name

    def show_details(self):
        print(f'Person: {self._name} {self._last_name} {self._age}')


# A public data can by modified and also a protected attribute
person_1 = Person('Juan', 'Perez', 28)
print(person_1.name)
person_1.name = 'Peter'
print(person_1.name)
