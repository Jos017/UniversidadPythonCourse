'''
Create a function to multiply the numeric values received,
using variable arguments (*args) as function parameters,
then return the sum of all the values provided as arguments
'''


def multiply_values(*args):
    result = 1
    for value in args:
        result *= value
    return result


print(multiply_values(1, 2, 3, 4))
