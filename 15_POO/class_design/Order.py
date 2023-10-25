from Product import Product


class Order:
    order_counter = 0

    def __init__(self, products):
        Order.order_counter += 1
        self._order_id = Order.order_counter
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product)

    def get_total_cost(self):
        total = 0

        for product in self._products:
            total += product.cost

        return total

    def __str__(self):
        products_str = ''

        for product in self._products:
            products_str += product.__str__() + ' | '

        return f'Order: [Id: {self._order_id}, Products: {products_str}]'


if __name__ == '__main__':
    product_1 = Product('Shirt', 100)
    product_2 = Product('Coat', 150)
    order = Order([product_1, product_2])
    print(order)
