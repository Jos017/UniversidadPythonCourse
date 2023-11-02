# Advances dictionaries

# Dictionaries are ordered
from pprint import pprint
dictionary = {'name': 'Juan', 'last_name': 'Perez', 'age': 28}
print(dictionary)

# Dictionaries ar mutable, but keys must be immutables
# dictionary = {[1,2]: 'Value'} # Wrong
dictionary_2 = {(1, 2): 'Value 1'}
print(dictionary_2)

# Can add a key if not found
dictionary['area'] = 'System'
print(dictionary)

# Cannot have duplicated keys, if duplicated the value is replaced
dictionary['name'] = 'Peter'
print(dictionary)

# Recover a value using a key
print(dictionary['name'])

# If the key is not found throws error
# print(dictionary['rank'])

# Recover a value using method get
# With this method if no key found, it can return a default value
# If the default value is not provided it returns None
# Do not add a new key
print(dictionary.get('rank'))
print(dictionary.get('rank', 'No key found'))
print(dictionary)

# Add a key by default
default = dictionary.setdefault('default_key', 'default_value')
print(default)
print(dictionary)

# Print with pprint
# help(pprint)
# pprint prints a more readable value
# by default pprint orders the dict by key
pprint(dictionary)
pprint(dictionary, sort_dicts=False)
