# You want to watch a movie
# You can only watch it if you are on vacation or have a free day

vacation = bool(input('Are you on vacation? (True or False): '))
free_day = bool(input('Are you on your free day? (True or False): '))

isFreeToWatchMovie = vacation or free_day
if isFreeToWatchMovie:
    print('You can watch a movie')
else:
    print('You cannot watch a movie, go to work')
