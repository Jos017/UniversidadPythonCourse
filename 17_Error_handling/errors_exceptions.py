# There are (at least) two distinguishable kinds of errors: syntax errors and exceptions
# It is posible to handle exceptions, to do this whe use "try" and "except"

# The try statement works as follows:
# - First, try the code
# - If no exception occurs, the except clause is skipped and the try statement is finished
# - If an exception occurs, the except clause is executed if matches the Exception

# ZeroDivisionError
try:
    10/0
# The following line is general exception
# except Exception as e:
except ZeroDivisionError as e:  # In this case is more specific exception
    print(f'An error ocurred: {type(e)}')
