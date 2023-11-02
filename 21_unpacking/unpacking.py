# This is other way to define a tuple
values = 1, 2, 3
print(values)
print(type(values))

# Assign the values of a tuple to a variable in one line
value_1, value_2, value_3 = 1, 2, 3
print(value_1, value_2, value_3)

# By convention we use a "_" when we don't want to use a value
value_1, _, value_3 = 1, 2, 3
print(value_1, value_3)

# We can assign all the remaining values in a variable using an * as the variable prefix
# The remaining values are assigned as a list
value_1, value_2, *value_3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(value_1, value_2, value_3)

# If we add more variables to assign after the * variable\
# The values assigned are the last ones
value_1, value_2, *value_3, value_4, value_5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(value_1, value_2, value_3, value_4, value_5)

# Unpacking can be done also with lists
value_1, value_2, *value_3, value_4, value_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(value_1, value_2, value_3, value_4, value_5)


def return_multiple_data():
    return 1, 2, 3


print(return_multiple_data())
value_1, *_ = return_multiple_data()
print(value_1)
