# An abstract class is a blueprint for other classes
# You cannot create a instance of an abstract class

# To create an abstract class you have to import ABC from abc
from abc import ABC, abstractmethod


# To Create an abstract class you must inherit from ABC
# An abstract class should contain one or more abstract methods
class Geometric_shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # You can also create abstract methods
    # An abstract method force the children classes to have a implementation of the parent class
    @abstractmethod
    def get_area(self):
        pass  # We use pass to define a function without code inside

    def __str__(self):
        return f'[Width: {self.width}, Height: {self.height}, Area: {self.get_area()}]'


class Rectangle(Geometric_shape):
    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color

    def get_area(self):
        return self.width * self.height


# Cannot instantiate an abstract class without implementing abstract method
# geometric = Geometric_shape(10, 5)

rectangle = Rectangle(5, 6, 'red')
print(rectangle)
# print(rectangle.height)
