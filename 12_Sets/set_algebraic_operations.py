# Algebraic set operations

# People
hair_black = {'Juan', 'Karla', 'Pedro', 'Maria'}
hair_blond = {'Lorenzo', 'Laura', 'Marco'}
eyes_brown = {'Karla', 'Laura'}
non_adult = {'Juan', 'Karla', 'Maria'}

# All the people with brown eyes or blond hair
# Union (All the elements of both sets)
print(eyes_brown.union(hair_blond))
# The result is the same don't care about the order
print(hair_blond.union(eyes_brown))

# Only the people with brown eyes and blond hair
# Intersection (Only the elements in both sets)
print(eyes_brown.intersection(hair_blond))
# The result is the same don't care about the order
print(hair_blond.intersection(eyes_brown))

# Only the people with brown eyes ony and not black hair
# Difference (Only the elements in the first set)
print(eyes_brown.difference(hair_black))
# The order is important
# Only the people with black hair ony and not brown eyes
print(hair_black.difference(eyes_brown))

# Only the people with brown eyes or blond hair but not both
# Symmetric difference (All the elements of both sets that are not in both sets)
print(eyes_brown.symmetric_difference(hair_blond))
# The result is the same don't care about the order
print(hair_blond.symmetric_difference(eyes_brown))
