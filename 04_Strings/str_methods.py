text = '''Elden Ring is a 2022 action role-playing game developed by FromSoftware.
It was directed by Hidetaka Miyazaki with worldbuilding provided by fantasy writer George R. R. Martin.
It was released for PlayStation 4, PlayStation 5, Windows, Xbox One, and Xbox Series X/S on February 25 by FromSoftware
in Japan and Bandai Namco Entertainment internationally. Players control a customizable player character who
is on a quest to repair the Elden Ring and become the new Elden Lord.'''
# Count occurrences
print('Repeated times "Elden":', text.count('Elden'))
print('Repeated times "e":', text.count('e'))

# Transform to uppercase
print('\n')
print(text.upper())

# Transform to lowercase
print('\n')
print(text.lower())

# Find if some string is in the string
print('\n')
print('Elden'.lower() in text.lower())
print('Elden'.upper() in text.upper())

# Starts with
print('\n')
print('The text starts with "Elden":', text.startswith('Elden'))
print('The text starts with "Ring":', text.startswith('Ring'))

# Ends with
print('\n')
print('The text starts with "Elden":', text.endswith('Lord.'))
print('The text starts with "Ring":', text.lower().endswith('lord.'.lower()))

# The string contains only lowercase
print('\n')
print('a'.islower())
print(text.lower().islower())

# The string contains only uppercase
print('\n')
print('A'.isupper())
print(text.upper().isupper())
