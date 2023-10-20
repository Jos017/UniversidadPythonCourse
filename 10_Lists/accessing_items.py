names = ['Juan', 'Karla', 'Ricardo', 'Maria']

# You can access the items in a list by writing: list[index]
print(names[0])  # ==> Juan
print(names[1])  # ==> Karla
print(names[2])  # ==> Ricardo
print(names[3])  # ==> Maria

# Get elements from the last one with negative index
print(names[-1])  # ==> Maria
print(names[-2])  # ==> Ricardo
print(names[-3])  # ==> Karla
print(names[-4])  # ==> Juan

# Obtain multiple elements from a list
# list[<start_index>:<end_index>]
# the returned elements does not include the end_index item
print(names[0:2])  # ==> ['Juan', 'Karla']
print(names[0:3])  # ==> ['Juan', 'Karla', 'Ricardo']
print(names[1:3])  # ==> ['Karla', 'Ricardo']
print(names[1:2])  # ==> ['Karla']
# From the start of the list to the end_index
print(names[:2])  # ==> ['Juan', 'Karla']
# From the start_index to the end
print(names[1:])  # ==> ['Karla', 'Ricardo', 'Maria']

# If we try to access a list item with a non existing index, we will get an error
# print(names[4])
# print(names[-5])
