# Arithmetic operators are used with numbers
# The results can be float
# can mix the different numeric types

# If both numbers are int, in most cases the result will be int
# If a number is float the result will be float

number_1 = 3
number_2 = 2

# Addition (+)
addition = number_1 + number_2
print(f'The addition result is: {addition}')  # ==> 5

# Subtraction (-)
subtraction = number_1 - number_2
print(f'The subtraction result is: {subtraction}')  # ==> 1

# multiplication (*)
product = number_1 * number_2
print(f'The multiplication result is: {product}')  # ==> 6

# Division (/)
# Returns a float number
division = number_1 / number_2
print(f'The division result is: {division}')  # ==> 1.5

# Floor Division
# Returns the int part of a number when dividing
floor_div = number_1 // number_2
print(f'The flood div result is: {floor_div}') # ==> 1

# Module or Remainder (%)
# Returns the reminder in a division
module = number_1 % number_2
print(f'The remainder is: {module}') # ==> 1

# Exponent (**)
exponent = number_1 ** number_2
print(f'The exponent operation result is: {exponent}') # ==> 9
