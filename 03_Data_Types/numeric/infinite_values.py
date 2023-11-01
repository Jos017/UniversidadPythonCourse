import math
from decimal import Decimal
# Infinite values


# Define infinite values with float
print('Infinite with float constructor'.center(50, '-'))

positive_infinite = float('inf')
is_infinite = math.isinf(positive_infinite)
print(f'Positive Infinite: {positive_infinite}')
print(f'Is Infinite?: {is_infinite}')

negative_infinite = float('-inf')
is_infinite = math.isinf(negative_infinite)
print(f'Positive Infinite: {negative_infinite}')
print(f'Is Infinite?: {is_infinite}')


# Define infinite values with math module
print('Infinite with math module'.center(50, '-'))

positive_infinite = math.inf
is_infinite = math.isinf(positive_infinite)
print(f'Positive Infinite: {positive_infinite}')
print(f'Is Infinite?: {is_infinite}')

negative_infinite = -math.inf
is_infinite = math.isinf(negative_infinite)
print(f'Positive Infinite: {negative_infinite}')
print(f'Is Infinite?: {is_infinite}')


# Define infinite values with Decimal class
print('Infinite with Decimal class'.center(50, '-'))

positive_infinite = Decimal('inf')
is_infinite = math.isinf(positive_infinite)
print(f'Positive Infinite: {positive_infinite}')
print(f'Is Infinite?: {is_infinite}')

negative_infinite = Decimal('-inf')
is_infinite = math.isinf(negative_infinite)
print(f'Positive Infinite: {negative_infinite}')
print(f'Is Infinite?: {is_infinite}')
