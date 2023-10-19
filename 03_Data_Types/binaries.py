# Binary data is divided into three types

# 1. bytes (bytes)
my_bytes = b'Hello'
print(my_bytes, type(my_bytes))

# 2. bytearray (bytearray)
my_bytearray = bytearray(5)
print(my_bytearray, type(my_bytearray))

# 3. memoryview (memoryview)
my_memoryview = memoryview(bytes(5))
print(my_memoryview, type(my_memoryview))
