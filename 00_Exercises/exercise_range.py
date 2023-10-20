# Range Syntax:
# range(start<optional>, end<required>, increment<optional>)

# Exercise 1: Iterate a range from 0 to 10 and print numbers divisible by 3
print('Exercise 1: Iterate a range from 0 to 10 and print numbers divisible by 3')
for number in range(11):
    if number % 3 == 0:
        print(number)

# Exercise 2: Create a range of numbers from 2 to 6 and print them
print('Exercise 2: Create a range of numbers from 2 to 6 and print them')
for number in range(2, 7):
    print(number)

# Exercise 3: Create a range from 3 to 10 with an increment of 2 and print them
print('Exercise 3: Create a range from 3 to 10 with an increment of 2 and print them')
for number in range(3, 11, 2):
    print(number)
