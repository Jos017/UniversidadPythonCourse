from Person import Person

# Object creation
print('Object creation'.center(30, '-'))
person_1 = Person('Karla', 'Gomez', 30)
person_1.show_details()

# Object destruction
print('Object destruction'.center(30, '-'))
del person_1
