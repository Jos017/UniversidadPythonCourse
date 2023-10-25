from Order import Order
from Product import Product

product_1 = Product('Shirt', 100)
product_2 = Product('Pants', 150)
product_3 = Product('Socks', 50)
product_4 = Product('Skirt', 70)

products_1 = [product_1, product_2]
products_2 = [product_3, product_4]

order_1 = Order(products_1)
order_2 = Order(products_2)
order_2.add_product(product_4)

print(order_1)
print('Order_1 Total', order_1.get_total_cost())
print(order_2)
print('Order_2 Total', order_2.get_total_cost())
