# Format strings


# Format with regular strings
print('Format regular string'.center(50, '-'))
name = 'Juan'
age = 28
formatted_message = 'My name is %s' % name
print(formatted_message)

formatted_message = 'My name is %s and I am %d years old' % (name, age)
print(formatted_message)

person = ('Karla', 'Gomez', 5000.00)
formatted_message = 'My name is %s %s and my salary is %.1f' % person
print(formatted_message)


# Format with format method
print('Method format'.center(50, '-'))
name_1 = 'Juan'
age = 28
salary = 3000

format_message = 'My name is {} and I am {} years old'.format(name, age)
print(format_message)

format_message = 'My name is {} and my salary is {:.1f}'.format(name, salary)
print(format_message)

# Can use the index
format_message = 'My salary is {2:.1f} and I am {0} {1}'.format(
    name, age, salary)
print(format_message)

# Can use named args
msg = 'My salary is {b:.1f} and I am {n} {a}'.format(n=name, a=age, b=salary)
print(msg)

# Can use dictionary
dictionary = {'name': 'Ivan', 'age': 35, 'salary': 8000.00}
msg = 'My salary is {person[salary]:.1f} and I am {person[name]} {person[age]}'.format(
    person=dictionary)
print(msg)


# Format with regular strings
print('Format with f-string'.center(50, '-'))
name = 'Juan'
age = 28
f_string_message = f'My name is {name}'
print(f_string_message)

f_string_message = f'My name is {name} and I am {age} years old'
print(f_string_message)

person = ('Karla', 'Gomez', 5000.00)
f_string_message = f'My name is {person[0]} {person[1]} and my salary is {person[2]:.1f}'
print(f_string_message)
