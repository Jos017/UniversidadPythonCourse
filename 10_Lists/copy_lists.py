
# Numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Copy elements from a list

##### Shallow copy #####
# Only changes the reference of the list
# The memory reference of the items is the same

# Using method copy
print('Copy method'.center(50, '-'))
numbers_copy = numbers.copy()
# This compares the memory reference
print(f'Same list reference? {numbers is numbers_copy}')
# This compares the values
print(f'Same content? {numbers == numbers_copy}')

# Using list constructor
print('List constructor'.center(50, '-'))
numbers_copy_2 = list(numbers)
print(f'Same list reference? {numbers is numbers_copy_2}')
print(f'Same content? {numbers == numbers_copy_2}')

# Slicing
print('Slicing'.center(50, '-'))
numbers_copy_3 = numbers[:]
print(f'Same list reference? {numbers is numbers_copy_3}')
print(f'Same content? {numbers == numbers_copy_3}')

# List of Lists
# The reference of the item is the same for all the 5 copies
print('List of Lists'.center(50, '-'))
list_multiplied = 5*[[2, 5]]
print(list_multiplied)
print(f'Same list reference? {list_multiplied[0] is list_multiplied[1]}')
print(f'Same content? {list_multiplied[0] == list_multiplied[1]}')
list_multiplied[2].append(10)
print(list_multiplied)
