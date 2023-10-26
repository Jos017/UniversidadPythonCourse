file = open('text.txt', 'r', encoding='utf8')

# This reads all the file
# print(file.read())

# Read 5 characters
# print(file.read(5))

# Read line
# print(file.readline(2))

# When you read all the read functions share info
# If you already read all the file readline will not work

# We can iterate the file
# for line in file:
#     print(line)

# We can read all lines
# This returns a list
# print(file.readlines()) # ==> []

# We can append information
# This means we add information instead of replacing all
file2 = open('copy.txt', 'a', encoding='utf8')
file2.write(file.read())

file.close()
file2.close()
