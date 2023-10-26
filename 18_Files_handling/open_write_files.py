try:
    # Try to open a text.txt file, if not found is created
    # Open the file in write mode
    # If no path provided the file will open or created from the current directory
    # The current directory is the route in your console you are executing the file from
    # The encoding is important if some characters are needed for example á
    file = open('text.txt', 'w', encoding='utf8')
    # Write in the open file
    # This replace all the file text
    file.write('Adding information to our file')
    file.write('\nuft8 allows accents (á)')
    file.write('\nThe end')

except Exception as e:
    print(e)
finally:
    file.close()
