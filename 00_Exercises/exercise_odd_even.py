# The user should provide a number
# You should show in console if the number is odd or even

print('Odd Even calculator')
number = int(input('Introduce a integer number: '))
isEven = number % 2 == 0

if isEven:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')
