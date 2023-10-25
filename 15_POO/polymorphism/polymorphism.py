# Polymorphism in python lets us define methods in a child class
# that have the same name as the methods in the parent class
# This allows to modify a method in a child class that is inherited from the parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employee: [Name: {self.name}, Salary: {self.salary}]'


class Manager(Employee):
    def __init__(self, name, salary, area):
        super().__init__(name, salary)
        self.area = area

    # This is polymorphism
    # We are modifying __str__ method inherited from parent class
    def __str__(self):
        return f'Manager: [Area: {self.area}] {super().__str__()}'


employee = Employee('Juan', 2000)
manager = Manager('Peter', 5000, 'Sales')

print(employee, type(employee))
print(manager, type(manager))
