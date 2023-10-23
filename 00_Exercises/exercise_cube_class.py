# Create a class cube to calculate the volume
class Cube:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def get_volume(self):
        return self.width * self.height * self.length


print('Cube info')

cube_width = float(input('Introduce width: '))
cube_height = float(input('Introduce height: '))
cube_length = float(input('Introduce length: '))
cube = Cube(cube_width, cube_height, cube_length)

print(f'Cube volume: {cube.get_volume()}')
