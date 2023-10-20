# We can use break to stop a loop

for char in 'Australia':
    print(char)
    if char == 't':
        print('Char found:', char)
        break
print('for has ended with break')

counter = 0
while counter < 10:
    print(counter)
    if counter == 5:
        print('Number found:', counter)
        break
    counter += 1
print('while has ended with break')
