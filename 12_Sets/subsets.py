# People
hair_black = {'Juan', 'Karla', 'Pedro', 'Maria'}
hair_blond = {'Lorenzo', 'Laura', 'Marco'}
eyes_brown = {'Karla', 'Laura'}
non_adult = {'Juan', 'Karla', 'Maria'}

# subset
# Ask if all the elements in the first set ar contained in the second set
print(non_adult.issubset(hair_black))

# superset
# Ask if the first set contains the second set
print(hair_black.issuperset(non_adult))

# disjoint
# Ask if the sets are not related
print(hair_black.isdisjoint(hair_blond))
