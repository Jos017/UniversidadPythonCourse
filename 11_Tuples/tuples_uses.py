# Declare variables
a, b = 'Hello', 'Bye'
print(a, b)


# Swap
a, b = b, a
print(a, b)


# Return multiple values in a function
def min_max(elements):
    return min(elements), max(elements)


min_num, max_num = min_max([1, 2, 3, 4, 5])
print(min_num, max_num)


# Return a tuple sum
result = sum((1, 2, 3, 4, 5))
print(f'Result: {result}')


def add(*args):
    return sum(args)


result = add(1, 2, 3, 4, 5)
print(f'Result: {result}')
