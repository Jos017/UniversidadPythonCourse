text = '     ***** This is a short text *****     '
print('Original:', text)

# Replace content in a string (replace)
print('Replaced (-):', text.replace('*', '-'))

# Remove characters at the start and end of a string (strip)
print('Stripped (space):', text.strip())
print('Stripped (*):', text.strip().strip('*'))

# Remove characters at the left (lstrip)
print('Stripped left:', text.lstrip().lstrip('*'))

# Remove characters at the right (rstrip)
print('Stripped right:', text.rstrip().rstrip('*'))
