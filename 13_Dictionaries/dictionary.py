# A dictionary its defined with brackets {}
# The elements in a dictionary are defined as key: value
# A dictionary is mutable
# A dictionary has no index
# Keys cannot be duplicated

dictionary = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(dictionary)

# Dictionary length
print(len(dictionary))

# Access items in dictionary
# Use key to access the value
print(dictionary['IDE'])  # ==> 'Integrated Development Environment'
print(dictionary['OOP'])  # ==> 'Object Oriented Programming'

# Modify values
dictionary['IDE'] = 'Description not found'
print(dictionary)

# Iterate over a dictionary

# Get dictionary items
# Returns tuples with key and values
for item in dictionary.items():
    print(item)
# get both values from loop
for key, value in dictionary.items():
    print(key, value)

# Get dictionary keys
for key in dictionary.keys():
    print(key)

# Get dictionary values
for value in dictionary.values():
    print(value)

# If you iterate directly in over the dictionary iterates over the keys
for key in dictionary:
    print(key)

# Know if a key is found in a dictionary
print('IDE' in dictionary)  # ==> True

# Add a new element
dictionary['PK'] = 'Primary Key'
print(dictionary)

# Remove an element
dictionary.pop('DBMS')
print(dictionary)

# Delete an element
del dictionary['IDE']
print(dictionary)

# Clear a dictionary
dictionary.clear()
print(dictionary)

# Delete dictionary from memory
del dictionary
