# unpacking operator (*)
numbers = [1, 2, 3]
print(numbers)
print(*numbers)
print(*numbers, sep=' - ')


# unpacking arguments
def add(num_1, num_2, num_3):
    print(f'Sum result: {num_1 + num_2 + num_3}')


add(*numbers)


# unpacking with variables
my_list = [1, 2, 3, 4, 5, 6]
a, *b, c, d = my_list
print(a, b, c, d)


# Create lists with unpacking
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [list_1, list_2]
print(list_3)
list_3 = [*list_1, *list_2]
print(list_3)


# Create dictionaries with unpacking
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'d': 4, 'e': 5, 'a': 6}
dict_3 = {**dict_1, **dict_2}
print(dict_3)


# Create a list from a str
list_str = [*'Hello world']
print(list_str)
print(*list_str, sep=' ')
