# Comparison operators allows us to compare values
# The comparison operators return a Bolean

a = 4
b = 2

# Equal operator (==)
comparison = a == b
print(f'{a} is equal than {b}: {comparison}')  # ==> False

# Different operator (!=)
comparison = a != b
print(f'{a} is different than {b}: {comparison}')  # ==> True

# Greater operator (>)
comparison = a > b
print(f'{a} is greater than {b}: {comparison}')  # ==> True

# Greater or equal operator (>=)
comparison = a >= b
print(f'{a} is greater or equal than {b}: {comparison}')  # ==> True
a = 4
b = 4
comparison = a >= b
print(f'{a} is greater or equal than {b}: {comparison}')  # ==> True

# less operator (<)
a = 4
b = 2
comparison = a < b
print(f'{a} is less than {b}: {comparison}')  # ==> False

# less or equal operator (<=)
comparison = a <= b
print(f'{a} is less or equal than {b}: {comparison}')  # ==> False
a = 4
b = 4
comparison = a <= b
print(f'{a} is less or equal than {b}: {comparison}')  # ==> True
