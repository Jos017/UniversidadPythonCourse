# bool contains values of true and false

# boolean with numbers
# 0 is False
# Any other number is True
print('Boolean with numbers'.center(50, '-'))
a = 0
b = 4
a_bool = bool(a)
b_bool = bool(b)
print(f'Number {a} is {a_bool}')
print(f'Number {b} is {b_bool}')


# boolean with strings
# An empty string ('') is False
# Any other string is True
print('Boolean with Strings'.center(50, '-'))
a = ''
b = 'False'
a_bool = bool(a)
b_bool = bool(b)
print(f"Empty string '{a}' is {a_bool}")
print(f"String '{b}' is {b_bool}")


# boolean with collections
# An empty collection ([], (), {}) is False
# Any collection with content is True

# boolean with lists
print('Boolean with List'.center(50, '-'))
a = []
b = [0, True, 'False']
a_bool = bool(a)
b_bool = bool(b)
print(f"Empty list {a} is {a_bool}")
print(f'List {b} is {b_bool}')

# boolean with tuples
print('Boolean with Tuple'.center(50, '-'))
a = ()
b = (0, True, 'False')
a_bool = bool(a)
b_bool = bool(b)
print(f"Empty tuple {a} is {a_bool}")
print(f'Tuple {b} is {b_bool}')

print('Boolean with Dictionary'.center(50, '-'))
a = {}
b = {'number': 0, 'boolean': True, 'string': 'False'}
a_bool = bool(a)
b_bool = bool(b)
print(f"Empty Dictionary {a} is {a_bool}")
print(f'Dictionary {b} is {b_bool}')
