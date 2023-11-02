# Number generator from 1 to 5
def number_generator():
    for number in range(1, 6):
        yield number
        print('The execution continues')


# Using the generator
generator = number_generator()
print(f'Object generator: {generator}')
print(type(generator))

# Consume generator
for value in generator:
    print(f'Number obtained: {value}')
