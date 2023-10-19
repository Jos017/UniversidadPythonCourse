# Print if a number is inside a 0 to 10 range
min_number = int(input('Introduce a min int number: '))
max_number = int(input('Introduce a max int number: '))
number = int(input('Introduce a int number: '))
isInRange = number >= min_number and number <= max_number
if isInRange:
    print(f'The number {number} is in the range {min_number} - {max_number}')
else:
    print(f'The number {number} is NOT in the range {min_number} - {max_number}')
