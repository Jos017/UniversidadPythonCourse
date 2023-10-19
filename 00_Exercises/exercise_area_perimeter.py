# Calc the area and perimeter of a rectangle,
# You should have the following variables: height (int) width (int)
# The user should give the data
# Print the result in

print('Rectangle calculator')

height = int(input('Introduce the rectangle height: '))
width = int(input('Introduce the rectangle width: '))

perimeter = 2 * (height + width)
area = height * width

print(f'The rectangle area is: {area}')
print(f'The rectangle perimeter is: {perimeter}')
