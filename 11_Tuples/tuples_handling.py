# Tuples are immutable

# Transform a tuple into List
fruits = ('Orange', 'Banana', 'Papaya')
print(fruits)
fruitsList = list(fruits)
print(fruitsList)

# You can only modify items from a list
fruitsList[0] = 'Coco'

# Transform a list into tuple
fruits = tuple(fruitsList)
print(fruits)
