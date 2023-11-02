# order a lists using zip
letters = ['c', 'd', 'a', 'e', 'b']
numbers = [3, 2, 4, 1, 0]
mix = zip(letters, numbers)
print(tuple(mix))

print(sorted(zip(letters, numbers)))
