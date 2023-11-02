# A generator is a special function that returns a sequence of values
# It suspend the execution of the function
# We use the keyword yield, instead return

def generator():
    yield 1
    yield 2
    yield 3


# Use the generator on demand
gen = generator()

# With every call we obtain a value
print(next(gen))
print(next(gen))
print(next(gen))

# If we call the function and obtain more values from the provided from the generator
# an error is thrown
# print(next(gen))

# We can also get values from a generator using a loop
for value in generator():
    print(f'Generated number: {value}')
