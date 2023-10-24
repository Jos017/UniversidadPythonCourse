# Inheritance allows us to define a class that inherits
# all the methods and properties from another class

# Parent class is the class being inherited from, also called base class

# Child class is the class that inherits from another class, also called derived class
# If you want to extend this class from another you just create a class,
# and in parenthesis write the parent class that is extended from

# This is the parent class
# By default it extends or inherits from the "object" class
# class Person(object)
# For this case is not needed to write (object)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person [Name: {self.name}, Age: {self.age}]'


class Employee(Person):
    # If we want to use the parent attributes we must define them in the constructor
    def __init__(self, name, age, payment):
        # We must use the method super() to use the parent attributes
        # We must use the constructor as well
        super().__init__(name, age)
        self.payment = payment


employee_1 = Employee('Juan', 28, 5000)
print(employee_1.name)
print(employee_1.age)
print(employee_1.payment)
print(employee_1)
