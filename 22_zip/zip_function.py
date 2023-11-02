# print(dir(__builtins__))
# help(zip)

# zip function
# This function joins two or more items into a tuple from iterables
# Joins in order (same index)
# In the case of sets it joins at random
# and returns a zip object (iterator of tuples)
# If one iterator has more items the items are ignores
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
booleans = (True, False)
days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
joined_iterables = zip(numbers, letters, booleans, days)
print(list(joined_iterables))

# Iterate over a zip
# You must use zip not the value in a variable
for number, letter, boolean, day in zip(numbers, letters, booleans, days):
    print(f'Number: {number}, Letter: {letter}, Boolean: {boolean}, Day: {day}')

new_list = []
for number, letter, boolean, day in zip(numbers, letters, booleans, days):
    new_list.append(f'{number}-{letter}-{boolean}: {day}')
print(new_list)
