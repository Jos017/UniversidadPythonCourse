'''
Create a function to sum the numeric values received,
using variable arguments (*args) as function parameters,
then return the sum of all the values provided as arguments
'''


def sum_values(*args):
    result = 0
    for arg in args:
        result += arg
    return result


my_sum = sum_values(1, 2, 3, 4)
print(my_sum)
