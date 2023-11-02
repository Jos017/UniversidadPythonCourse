# Variables scope

# Global scope
# A global variable can be accessed from all the code
var_global = 'Global Scope'


def print_var():
    # if we want to modify a global variable from inside a scope we must define the global variable
    # if we only want to read it its not necessary to define the global variable
    global var_global
    # Access to a global variable
    print(f'Global variable from function: {var_global}')
    # if we don't define the global variable and try to modify the value
    # it behaves as declaring a new local variable
    var_global = 'Modified Global variable'
    print(var_global)

    # Local variable
    # A local variable can be accessed only from its block of code
    # In this case the function
    var_local = 'Local Scope'
    print(f'Local variable from function: {var_local}')

    def nested_func():
        print(f'Global variable from nested function: {var_global}')
        print(f'Local variable from nested function: {var_local}')

    nested_func()


print_var()
print(f'Global variable from file: {var_global}')

# The local variable can only be accessed from its scope
# In this case the function
# print(f'Local variable from file: {var_local}')


# The same as the global scope whe can do in the local scope
def outer_function():
    outer_local_variable = 'Outer local variable'

    def nested_function():
        nested_local_variable = 'Nested local variable'
        # if want to modify the outer local variable you must define with nonlocal
        nonlocal outer_local_variable
        # to access a outer local variable only need to call the variable
        print(outer_local_variable)
        outer_local_variable = 'New outer value'
        print(outer_local_variable)
        print(nested_local_variable)

    nested_function()

    print(f'Outer local variable value: {outer_local_variable}')


outer_function()
