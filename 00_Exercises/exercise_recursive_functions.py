# Print numbers from 5 to 1 in descendent order using recursive functions.
# The Value can be any positive number
# If the value is negative do not print anything
def nums_descendent(number):
    if number >= 1:
        print(number)
        nums_descendent(number - 1)
    elif number == 0:
        return
    else:
        print('Incorrect value...')


my_number = int(input('Introduce un numero positivo: '))
nums_descendent(my_number)
