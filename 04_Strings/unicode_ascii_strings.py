# Unicode characters (\u \U \x)
print('Hello\u0020World')  # => space
print('Simple notation:', '\u0041')
print('Extended notation:', '\U00000041')
print('Hexadecimal notation:', '\x41')
print('Hearth:', '\u2665')
print('Smile Face:', '\U0001f600')
print('Snake:', '\U0001f40d')

# ASCII Characters
character = chr(65)
print('A (uppercase):', character)
character = chr(64)
print('Symbol @:', character)
character = chr(97)
print('A (lowercase):', character)
