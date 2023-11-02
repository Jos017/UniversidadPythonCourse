# List comprehension offers a shorter syntax ehn you want to create
# a new list based on the values of an existing list


# Regular list
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = []

for fruit in fruits:
    if 'a' in fruit:
        new_list.append(fruit)

print(new_list)


# List with list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [fruit for fruit in fruits if 'a' in fruit]
print(new_list)


# List of Lists
list_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
new_list = [value for number_list in list_lists for value in number_list]
print(new_list)
