# Object representation (str, repr, format)
# print(dir(object)) # This shows all the methods of the object class

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    # repr, focused on developers
    # Its called when print is used
    def __repr__(self):
        return f'{self.__class__.__name__}(name: {self.name}, last_name: {self.last_name})'

    # str, focused on final user
    # The default implementation calls the repr method
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} {self.last_name}'

    # format
    # By default format calls the method str if no implemented
    # Its called when using f-strings
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} with name {self.name} and last name {self.last_name}'


person_1 = Person('Juan', 'Perez')

# Calling str method
# If no str method implemented by default the str method calls repr
print(person_1)

# With !r we force calling repr method
print(f'Force repr: {person_1!r}')

# With !r we force calling str method
print(f'Force str: {person_1!s}')

# Calling method format
# format method is called in a f-string
print(f'Format: {person_1}')
