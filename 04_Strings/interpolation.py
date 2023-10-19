# There is a way to write variables in a string,
# This method is called interpolation
# This transform the variables and write it into a a string

number_1 = 1
number_2 = 3
boolean = False

# To interpolate variables into a string we use the "f" as a prefix to the string
# and write the variable we want to show inside brackets {}
sentence = f'Is {boolean} that the {number_1} is greater than {number_2}'

print(sentence)
