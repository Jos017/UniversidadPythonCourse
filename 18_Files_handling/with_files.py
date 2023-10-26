# To have cleaner code we use statement "with" to work with files
# The with statement closes the file without the needed to close it manually
from File_manager import File_manager

with open('text.txt', 'r', encoding='utf8') as file:
    print(file.read())

with File_manager('text.txt') as file:
    print(file.read())
