# You want to watch a movie
# You can only watch it if you are on vacation or have a free day
# Use operator not in this exercise

vacation = bool(input('Are you on vacation? (True or False): '))
free_day = bool(input('Are you on your free day? (True or False): '))

isFree = vacation or free_day
if not isFree:
    print('You cannot watch a movie, go to work')
else:
    print('You can watch a movie')
