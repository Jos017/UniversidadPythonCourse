class Product:
    product_counter = 0

    def __init__(self, name, cost):
        Product.product_counter += 1
        self._product_id = Product.product_counter
        self._name = name
        self._cost = cost

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    def __str__(self):
        return f'Id: {self._product_id}, Name: {self._name}, Cost: {self._cost}'


# This will execute only if called from the same file
if __name__ == '__main__':
    product_1 = Product('Shirt', 100)
    product_2 = Product('Pants', 120)
    print(product_1)
    print(product_2)
