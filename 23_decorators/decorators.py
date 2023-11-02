# A decorator allows to modify the behavior of a function or class
# This extends the functionality
# 1. decorator function
# 2. function to decorate
# 3. decorated function

def decorator_function(function_to_decorate):
    def decorated_function():
        print('Before execute function')
        function_to_decorate()
        print('After execute function')

    return decorated_function


@decorator_function
def show_message():
    print('Hello from the function show_message')


show_message()


# A decorator can use multiple parameters
def decorator_function_multiple(function_to_decorate):
    def decorated_function(*args, **kwargs):
        print('Before execute function')
        result = function_to_decorate(*args, **kwargs)
        print('After execute function')
        return result

    return decorated_function


@decorator_function_multiple
def add(a, b, c):
    return a + b + c


# add(4, 5)
print(f'Sum result: {add(4, 5, 5)}')
