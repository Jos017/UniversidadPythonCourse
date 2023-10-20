# A set is an iterable and its defined with brackets {}
# Cannot modify the items of a set but you can add or remove items
# A set is not ordered, so it does not have an index
# A set cannot have duplicated elements

planets = {'Mars', 'Venus', 'Earth'}
print(planets)

# Set length
print(len(planets))  # ==> 3

# Know if an item is in the set
isMarsInSet = 'Mars' in planets
print(isMarsInSet)  # ==> True

# Add an item
planets.add('Saturn')
print(planets)  # ==> {'Mars', 'Venus', 'Earth', 'Saturn}

# Cannot have duplicated elements
planets.add('Saturn')
print(planets)  # ==> {'Mars', 'Venus', 'Earth', 'Saturn}

# Remove an item
planets.remove('Saturn')
print(planets)  # ==> {'Mars', 'Venus', 'Earth'}
# the remove function throws an error if item is no found
# planets.remove('Russia')
# print(planets)

# Remove items with discard
planets.discard('Earth')
print(planets)  # ==> {'Mars', 'Venus'}
# the discard function do not remove anything if item is no found
planets.discard('Russia')
print(planets)  # ==> {'Mars', 'Venus'}

# Clear items from set
planets.clear()
print(planets)  # ==> {}

# Delete set from memory
del planets
