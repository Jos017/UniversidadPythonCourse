class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Geometric_shape:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __str__(self):
        return f'[Width: {self._width}, Height: {self._height}]'


class Square(Geometric_shape, Color):
    def __init__(self, side, color):
        Geometric_shape.__init__(self, side, side)
        Color.__init__(self, color)

    def get_area(self):
        return self._width ** 2

    def get_perimeter(self):
        return self._width * 4

    def __str__(self):
        return f'Square {super().__str__()} [Area: {self.get_area()}, Perimeter: {self.get_perimeter()}]'


class Rectangle(Geometric_shape, Color):
    def __init__(self, width, height, color):
        Geometric_shape.__init__(self, width, height)
        Color.__init__(self, color)

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return f'Rectangle {super().__str__()} [Area: {self.get_area()}, Perimeter: {self.get_perimeter()}]'


square = Square(5, 'red')
rectangle = Rectangle(10, 5, 'blue')
print(square)
print(rectangle)
