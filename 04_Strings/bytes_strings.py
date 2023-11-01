# Characters in bytes
char_byte = b'Hello World'
print(char_byte)

message = b'Python University'
print(message)
print(message[0])
print(chr(message[0]))


# Transform str to byte
string = 'Python Programming (Español)'
print('Original string', string)
bytes_str = string.encode('utf-8')
print('Bytes encoded:', bytes_str)

# Transform from bytes to str
string_2 = bytes_str.decode('utf-8')
print('String decoded:', string_2)
