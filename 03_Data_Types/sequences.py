# Sequence data is divided into three types

# 1. Lists (list), we define lists with square brackets []
# The list content is mutable
my_list = ['apple', 1, 'cherry']
print(my_list, type(my_list))

# 2. Tuples (tuple), we define lists with parenthesis ()
# The tuple content is immutable
my_tuple = ('apple', 1, 'cherry')
print(my_tuple, type(my_tuple))

# 3. Ranges (range), we define ranges with function range(int)
# A range creates a sequence of numbers with step by default 1
my_range = range(3)
print(my_range, type(my_range))
