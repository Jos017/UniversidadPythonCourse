# A module has property __name__, to know the module name

# Class Person
class Person:
    def __init__(self, name, last_name, age):
        self._name = name
        self._last_name = last_name
        self._age = age

    @property  # Decorator, allows the getter methods behaves as an attribute
    def name(self):  # Getter method
        print(f'Calling get method name: {self._name}')
        return self._name

    @name.setter  # Decorator, allows the setter method behaves as an attribute
    def name(self, name):  # Setter method
        print(f'Calling set method name with: {name}')
        self._name = name

    @property  # Decorator, allows the getter methods behaves as an attribute
    def last_name(self):  # Getter method
        print(f'Calling get method last_name: {self.last_name}')
        return self._last_name

    @last_name.setter  # Decorator, allows the setter method behaves as an attribute
    def last_name(self, last_name):  # Setter method
        print(f'Calling set method last_name with: {last_name}')
        self._last_name = last_name

    @property  # Decorator, allows the getter methods behaves as an attribute
    def age(self):  # Getter method
        print(f'Calling get method age: {self._age}')
        return self._age

    @age.setter  # Decorator, allows the setter method behaves as an attribute
    def age(self, age):  # Setter method
        print(f'Calling set method age with: {age}')
        self._age = age

    def show_details(self):
        print(f'Person: {self._name} {self._last_name} {self._age}')

    # # We can define a destructor method
    # def __del__(self):
    #     print(f'Persona: {self._name} {self._last_name}')
