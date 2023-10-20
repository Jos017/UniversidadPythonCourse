# Multiple functions that can be used with a list
names = ['Juan', 'Karla', 'Ricardo', 'Maria']

# Obtain the length (items quantity) of a list
print(len(names))  # ==> 4

# Add an item to the end of a List
names.append('Lorenzo')
print(names)  # ==> ['Juan', 'Karla', 'Ricardo', 'Maria', 'Lorenzo']

# Add an item to a determined index of a List
names.insert(1, 'Jose')
print(names)  # ==> ['Juan', 'Jose', 'Karla', 'Ricardo', 'Maria', 'Lorenzo']

# Remove the last item of a List
names.pop()
print(names)  # ==> ['Juan', 'Jose', 'Karla', 'Ricardo', 'Maria']

# Remove an item from a determined index of a List
del names[3]
print(names)  # ==> ['Juan', 'Jose', 'Karla', 'Maria']

# Clear a list (Remove all items)
names.clear()
print(names)  # ==> []

# Delete List from memory
del names
# names variable no longer exists
# print(names)
