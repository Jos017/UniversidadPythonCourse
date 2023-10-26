# Creating a custom exception
class Same_numbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    if a == b:
        # Raise is used to throw an exception
        raise Same_numbers('Exception: The numbers are the same')
    result = a / b
except ZeroDivisionError:
    print('Cannot divide by Zero')
except Exception as e:
    print(f'An error ocurred: {e}, {type(e)}')
# The else block executes the code if no exception has been thrown
else:
    print('No exception thrown')
# The finally block executes the code after the try or except block
# even if an exception has been thrown
finally:
    print('This is the finally block')
