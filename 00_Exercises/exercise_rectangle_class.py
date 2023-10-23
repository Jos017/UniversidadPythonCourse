# Create a class for a rectangle and find perimeter and area
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


print('Rectangle info')

rectangle_width = float(input('Introduce width: '))
rectangle_height = float(input('Introduce height: '))
rectangle = Rectangle(rectangle_width, rectangle_height)

print(f'Rectangle perimeter: {rectangle.get_perimeter()}')
print(f'Rectangle area: {rectangle.get_area()}')
