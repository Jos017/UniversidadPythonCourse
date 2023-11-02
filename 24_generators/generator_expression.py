# Generator expression (it's an anonymous generator)

# In this case value*value is the yield value in the for loop
# so multiplication would be a generator equivalent to
# def multiplication():
#     for value in range(4):
#         yield value*value

# a generator expression is wrapped in parenthesis
multiplication = (value*value for value in range(4))
print(next(multiplication))
print(next(multiplication))
print(next(multiplication))
print(next(multiplication))


# Pass a generator expression to a function:
# when passed to a function is not necessary to add parenthesis
addition = sum(value*value for value in range(4))


# Use a list with generator expression
names = ['Juan', 'Perez']
generator = (value for value in names)
print(next(generator))
print(next(generator))

# Create a string from a generator created from a list
names = ['Karla', 'Gomez']
counter = 0


def increment():
    global counter
    counter += 1
    return counter


generator = (f'{increment()}. {name}' for name in names)
my_list = list(generator)
print(my_list)
my_string = ', '.join(my_list)
print(f'Generated string: {my_string}')
