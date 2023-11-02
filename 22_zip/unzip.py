# unzip
mix = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*mix)
print(f'Numbers: {numbers}, Letters: {letters}')
