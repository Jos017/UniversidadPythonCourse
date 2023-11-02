# List of Lists
# The reference of the item is the same for all the 5 copies
print('List of Lists'.center(50, '-'))
list_multiplied = 5*[[2, 5]]
print(list_multiplied)
print(f'Same list reference? {list_multiplied[0] is list_multiplied[1]}')
print(f'Same content? {list_multiplied[0] == list_multiplied[1]}')
list_multiplied[2].append(10)
print(list_multiplied)

# A List of list is called Matrix
print('\n')
print('Matrix'.center(50, '-'))
matrix = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Original matrix: {matrix}')
print(f'Row 0, Column 0: {matrix[0][0]}')
print(f'Row 2, Column 2: {matrix[2][3]}')

# Order list of list
print('\n')
print('Order Lists'.center(50, '-'))
list_lists = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 14, 45, 61, 70]]
print(f'Original List: {list_lists}')
list_lists.sort(key=len)  # sort by list length
print(f'Order List by item length: {list_lists}')

# Using built-in sorted
print('\n')
print('Order Lists (built-in)'.center(50, '-'))
names = ['Juan', 'Carlos', 'Karla', 'Pedro', 'Esperanza']
names_sorted_asc = sorted(names)
names_sorted_desc = sorted(names, reverse=True)
names_sorted_length_asc = sorted(names, key=len)
names_sorted_length_desc = sorted(names, key=len, reverse=True)
print(f'Original List: {names}')
print(f'Sort alphabetically ascendant: {names_sorted_asc}')
print(f'Sort alphabetically descendant: {names_sorted_desc}')
print(f'Sort length ascendant: {names_sorted_length_asc}')
print(f'Sort length descendant: {names_sorted_length_desc}')
