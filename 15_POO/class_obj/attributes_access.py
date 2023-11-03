# Attributes public, protected and private

class My_class:
    def __init__(self, public, protected, private):
        # Public should be accessed by any place
        self.public = public
        # Protected should be accessed by the same class or subclasses
        self._protected = protected
        # Private should be accessed only by the same class
        self.__private = private


my_object = My_class('Public value', 'Protected value', 'Private value')

# Access public attribute
print(my_object.public)

# Modify public attribute
my_object.public = 'New public value'
print(my_object.public)

# Access to protected attribute
# Should only access from children class or same class
print(my_object._protected)

# Cannot access to private attribute from an instance
# Only from the same class
# print(my_object.__private) # This throws error
