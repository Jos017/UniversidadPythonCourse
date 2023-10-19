# pylint: disable=invalid-name

# If we use numbers in a string we concatenate it,
number_1 = '1'
number_2 = '2'

print(number_1 + number_2)  # ==> 12

# if we want to add the numbers both values must be numeric
# We can transform a string into a int number using function int(number)

print(int(number_1) + int(number_2)) # ==> 3
