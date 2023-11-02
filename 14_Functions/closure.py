# A closure is a function that defines other, and can return it
# The nested function can access the local variables defined in the outer function

# Principal function
def operation(a, b):
    # Defining a nested function
    def add():
        return a + b

    # Return the function
    return add


my_closure_function = operation(5, 2)
print(f'Result closure function: {my_closure_function()}')

# Call a function and return it on fly
print(f'Result closure function on fly: {operation(2, 3)()}')


# Closures with lambda function
def operation_lambda(a, b):
    # define and return the function
    return lambda: a + b


my_closure_function_lambda = operation_lambda(5, 2)
print(f'Result closure function: {my_closure_function_lambda()}')

# Call a function and return it on fly
print(f'Result closure function on fly: {operation_lambda(2, 3)()}')
