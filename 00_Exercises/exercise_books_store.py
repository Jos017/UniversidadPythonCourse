# Create a book store
# Should provide the book name
# Should provide id number
# Should provide the cost
# Should provide if the delivery is free
# Show all the values provided

name = input('Provide the book name: ')
book_id = int(input('Provide the book id: '))
cost = float(input('Provide the book cost: '))
delivery = bool(input('Is the delivery free? (True/False): '))

print('Book name:', name)
print('Book id:', book_id)
print('Book cost:', cost)
print('Delivery Free:', delivery)
