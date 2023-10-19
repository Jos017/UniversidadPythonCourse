# Calc the season depending on the month
month = int(input('Introduce the month (1-12): '))
if 3 <= month <= 5:
    print('Winter')
elif 6 <= month <= 8:
    print('Autumn')
elif 9 <= month <= 11:
    print('Spring')
elif 12 == month or 1 <= month <= 2:
    print('Summer')
else:
    print('Invalid number')
