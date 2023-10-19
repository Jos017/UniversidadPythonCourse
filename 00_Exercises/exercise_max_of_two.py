# Print what of two numbers is the greatest

number_1 = int(input('Write first number (integer): '))
number_2 = int(input('Write second number (integer): '))

if number_1 > number_2:
    print(f'{number_1} is the greatest')
else:
    if number_1 < number_2:
        print(f'{number_2} is the greatest')
    else:
        print('Both numbers are the same')
