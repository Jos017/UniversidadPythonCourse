# A Tuple is defined by parenthesis ()
# A Tuple works the same way as a List
# The difference is that a Tuple is not mutable
# You cannot change any value, add items, or remove items

########
# If a tuple only has one element you should use a comma after this element
# This is know that is a tuple
# single_item_tuple = ('Item',)

fruits = ('Orange', 'Banana', 'Papaya')
print(fruits)

# tuple length
print(len(fruits))  # ==> 3

# access an item
print(fruits[0])  # ==> Orange

# access an item inverse
print(fruits[-1])  # ==> Papaya

# access multiple items
print(fruits[0:2])  # ==> (Orange', 'Banana')
