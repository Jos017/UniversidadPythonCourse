# We can use continue to skip the current iteration in a loop
# and continue with next one

for char in 'Australia':
    if char == 'a':
        continue
    print(char)
print('for has ended')

counter = 0
while counter <= 10:
    if counter % 2 != 0:
        counter += 1
        continue
    print(counter)
    counter += 1
print('while has ended')
