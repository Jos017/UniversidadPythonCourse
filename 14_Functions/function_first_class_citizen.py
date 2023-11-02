# A function is a first class citizen
# a first class citizen is a entity that supports to be used in all operations by other entities
# Some of this operations are:
# - Being passed as argument
# - Returned from function
# - Be assigned to a variable

# Define a function
def add(a, b):
    return a + b


# 1. Assign a function to a variable
# A function without parenthesis means the function it self
# The parenthesis means execute the function
my_function = add
print(type(my_function))
print('Function assigned to variable:', my_function(1, 2))


# 2. Use a function as argument
def calculator(a, b, operation):
    result = operation(a, b)
    return result


print('Function used as argument:', calculator(1, 2, add))


# 3. Return a function
def return_function():
    return add


my_returned_function = return_function()
print('Function returned:', my_returned_function(1, 2))
