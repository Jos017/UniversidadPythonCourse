# A set is a collection of unique elements and is mutable
# The elements in a set must be immutable
# group =  {[1, 2], [3, 4]} # This is wrong
group = {'Juan', True, 18.0}
print(group)

# Empty set
# An empty set must be created with its constructor
# If you use {} it creates an empty dictionary
empty_set = set()
print(empty_set)
print(type(empty_set))

# A set is mutable
group.add('Peter')
print(group)

# Contains unique values
group.add('Peter')
print(group)

# Create a set from a iterable
numbers = [1, 2, 3, 4, 1, 2, 3, 4]
numbers_set = set(numbers)
print(numbers_set)

# We can add a set elements to another set
numbers_1 = {1, 2, 3, 4}
numbers_2 = {3, 4, 5, 6}
print(numbers_1)
numbers_1.update(numbers_2)
print(numbers_1)
# also with other iterable
numbers_1.update([5, 6, 7, 8])
print(numbers_1)
