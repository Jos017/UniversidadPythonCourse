result = None
a = '10'
b = 0

print('\n', 'Example 1'.center(50, '-'))
try:
    result = a / b
except (ZeroDivisionError, TypeError) as e:
    print(f'An error ocurred: {e}')


print('\n', 'Example 2'.center(50, '-'))
try:
    result = a / b
except ZeroDivisionError:
    print('Cannot divide by 0')
except TypeError:
    print('Type error')
except Exception as e:
    print(f'An error ocurred: {e}')


print('\n', 'Example 3'.center(50, '-'))
try:
    a = int(input('First Number: '))
    b = int(input('Second Number: '))
    result = a / b
except ZeroDivisionError:
    print('Cannot divide by 0')
except TypeError:
    print('Type error')
except Exception as e:
    print(f'An error ocurred: {e}, Type: {type(e)}')
