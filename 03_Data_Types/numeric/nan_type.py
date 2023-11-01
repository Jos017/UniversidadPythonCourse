# NaN - Not a Number
# NaN is not case sensitive
# NaN is a numeric type when not defined

import math
from decimal import Decimal

# Not a Number using float
print('NaN using float'.center(50, '-'))
a = float('NaN')
is_nan = math.isnan(a)
print(f'a: {a}')
print(f'Is NaN?: {is_nan}')

# Not a Number using Decimal class
print('NaN using Decimal'.center(50, '-'))
a = Decimal('NaN')
is_nan = math.isnan(a)
print(f'a: {a}')
print(f'Is NaN?: {is_nan}')
