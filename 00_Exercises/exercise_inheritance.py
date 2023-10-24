'''
Define a parent class named Vehicle and two children classes named Car and Bicycle,
those classes will inherit from the parent class Vehicle.

The classes should have the following attributes and methods:

Vehicle (Parent class)
- Attributes (color, wheels)
- Methods (__init__() and __str__())

Car (Children class)
- Attributes (speed (km/h))
- Methods (__init__() and __str__())

Bicycle (Children class)
- Attributes (type (urban/mountain/other))
- Methods (__init__() and __str__())
'''


class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return f'Vehicle: [Color: {self.color}, Wheels: {self.wheels}]'


class Car(Vehicle):
    def __init__(self, color, wheels, speed):
        super().__init__(color, wheels)
        self.speed = speed

    def __str__(self):
        return f'{super().__str__()} Car: [Speed: {self.speed} km/h]'


class Bicycle(Vehicle):
    def __init__(self, color, wheels, bike_type):
        super().__init__(color, wheels)
        self.bike_type = bike_type

    def __str__(self):
        return f'{super().__str__()} Bicycle: [Type: {self.bike_type}]'

vehicle = Vehicle('red', 4)
car = Car('Yellow', 4, 140)
bicycle = Bicycle('Blue', 2, 'Mountain')

print(vehicle)
print(car)
print(bicycle)
