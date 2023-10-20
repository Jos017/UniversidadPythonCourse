# The loop for allows to execute a code a determined times

# for in
# for in allows to iterate over any iterable (string, list, range, tuple)
# you can use every value iterated in the code
# Syntax:
# for <value> in <toIterate>
my_string = 'Hello'
my_list = ['apple', 'banana', 'cherry']
my_range = range(1, 6)
my_tuple = ('apple', 'banana', 'cherry')

print('String loop for')
for char in my_string:
    print(char)

print('List loop for')
for item in my_list:
    print(item)

print('Range loop for')
for numb in my_range:
    print(numb)

print('Tuple loop for')
for item in my_tuple:
    print(item)

print('loop for has ended')
