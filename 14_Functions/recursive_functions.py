# A recursive function is a function that calls itself
def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
