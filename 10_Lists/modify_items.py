# The items in a list are mutable
# You can modify the items by using its index and assign a new value

#######
# The new value must be of the same type of the initial value
#######

names = ['Juan', 'Karla', 'Ricardo', 'Maria']
print(names)  # ==> ['Juan', 'Karla', 'Ricardo', 'Maria']

names[0] = 'New Juan'
print(names)  # ==> ['New Juan', 'Karla', 'Ricardo', 'Maria']
