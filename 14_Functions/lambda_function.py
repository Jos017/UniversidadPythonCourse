# A lambda function is anonymous (no name)
# A lambda function is short, (only one line of code)
# A lambda function don't need to use the return keyword
# A lambda function don't need parenthesis for the arguments
# Syntax: lambda <parameters, ...> : <return value>
my_lambda_function = lambda a, b : a + b
print(my_lambda_function(1, 2))

# Lambda function with no arguments
my_lambda_function = lambda : 'No arguments function'
print(my_lambda_function())

# Lambda function with params by default
my_lambda_function = lambda a=2, b=3 : a + b
print(my_lambda_function())

# Lambda function with variable arguments
my_lambda_function = lambda *args, **kwargs : len(args) + len(kwargs)
print(f'Results: {my_lambda_function(5, 5, 5, 5, name='Juan', last_name='Perez')}')
