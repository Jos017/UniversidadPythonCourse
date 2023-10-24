# A class can inherit from multiple parents

class Color:
    def __init__(self, color):
        self.color = color


class Geometric_shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Children class, inherits from Color and Geometric_shape


class Square(Geometric_shape, Color):
    def __init__(self, side, color):
        # If we use super(), the method only calls the first parent
        # In this cases is better to use the parent classes names to call the __init__ method
        # Remember to provide self as argument in this case, to keep the reference to the object
        Geometric_shape.__init__(self, side, side)
        Color.__init__(self, color)

    def get_area(self):
        return self.width ** 2

    def get_perimeter(self):
        return self.width * 4


square = Square(5, 'red')
print('Type:', type(square))
print('Color:', square.color)
print('Side:', square.width)
print('Area:', square.get_area())
print('Perimeter:', square.get_perimeter())

# To know the priority order of inheritance we can use mro()
print('MRO', Square.mro())
