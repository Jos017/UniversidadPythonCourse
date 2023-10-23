# In a function, its parameters can have a default value
# This means the default value will be used
# if no argument corresponding to the parameter is provided when the function is called

# Assign default values to parameters
def greetings(name='No name'):
    return f'Hello {name}'


# If no args are provided the value will be the default
print(greetings())  # ==> 'Hello No name'

# If args are provided the value will be the args provided
print(greetings('Jose'))  # ==> 'Hello Jose'
