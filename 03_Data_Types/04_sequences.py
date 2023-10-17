# Sequence data is divided into three types

# 1. Lists (list), we define lists with square brackets []
# The list content is mutable
myList = ['apple', 1, 'cherry']
print(myList, type(myList))

# 2. Tuples (tuple), we define lists with parenthesis ()
# The tuple content is immutable
myTuple = ('apple', 1, 'cherry')
print(myTuple, type(myTuple))

# 3. Ranges (range), we define ranges with function range(int)
# A range creates a sequence of numbers with step by default 1
myRange = range(3)
print(myRange, type(myRange))
