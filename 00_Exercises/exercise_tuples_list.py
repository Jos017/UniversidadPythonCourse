# Given the following tuple:
my_tuple = (13, 1, 8, 3, 2, 5, 8)

# Create a list that only includes numbers minor to 5
my_list = []
for number in my_tuple:
    if number < 5:
        my_list.append(number)

print(my_list)
