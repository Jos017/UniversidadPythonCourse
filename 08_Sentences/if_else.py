# IF is a sentence that executes code when the condition is true
# The sentence if can be user with else
# else executes the code when the condition is false

condition = True
if condition:
    print('The condition is True')
else:
    print('The condition is False')

condition = False
if condition:
    print('The condition is True')
else:
    print('The condition is False')

# You can use elif to assign another condition when the initial condition is false

number = 5
if number < 5:
    print('The number is lower than 5')
elif number < 10:
    print('The number is lower than 10 but more or equal than 5')
else:
    print('The number is higher than 10')
