# Nested functions

def calculator(a, b, operation):
    # 1. Define nested function
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return float('inf')
        else:
            return a / b

    # 2. Call nested function
    match operation:
        case 'add':
            print(f'Addition Result: {add(a, b)}')
        case 'subtract':
            print(f'Subtraction Result: {subtract(a, b)}')
        case 'multiply':
            print(f'Multiplication Result: {multiply(a, b)}')
        case 'divide':
            print(f'Division Result: {divide(a, b)}')
        case _:
            print('Invalid operation')


calculator(2, 3, operation='add')
calculator(5, 0, operation='divide')
calculator(5, 0, operation='div')
