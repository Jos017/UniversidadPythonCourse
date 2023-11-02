# Lists are mutable
names_1 = ['Juan', 'Karla', 'Pedro']
names_2 = 'Laura Mario Gonzalo Ernesto'.split()

# Sum lists
# This creates a new list
names = names_1 + names_2
print(f'Sum lists {names}')

# Extend a list with other list
# This modify the extended list
names_1.extend(names_2)
print(f'Extend list {names_1}')

# Numbers List
numbers_1 = [10, 40, 15, 4, 20, 90, 4]

# obtain the index of the first element found
# if not found a ValueError is thrown
index_4 = numbers_1.index(4)
print(f'Index of 4: {index_4}')

# Invert the order of a list elements (Modifies the original)
print('Original List:', numbers_1)
numbers_1.reverse()
print('Reversed List:', numbers_1)
# Order a list elements ascendant (Modifies the original)
numbers_1.sort()
print('Order Asc:', numbers_1)
# Order a list elements descendant (Modifies the original)
numbers_1.sort(reverse=True)
print('Order Desc:', numbers_1)

# Obtain the min and max values from a list
print(f'Min value: {min(numbers_1)}')
print(f'Max value: {max(numbers_1)}')
