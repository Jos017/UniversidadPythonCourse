# We can provide any type as argument in a variable,
# But we have to consider the function operations
# Some sentences could not be compatible with the args type

def displayNames(values):
    for name in values:
        print(name)


# Providing a list as a argument
names = ['Juan', 'Karla', 'Guillermo']
displayNames(names)

# Providing a string as a argument
displayNames('Juan')

# Providing a tuple as a argument
displayNames((10, 11))

# Providing number
# displayNames(10) # ==> Error
