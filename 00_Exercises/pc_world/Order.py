class Order:
    order_counter = 0

    def __init__(self, computers):
        Order.order_counter += 1
        self._order_id = Order.order_counter
        self._computers = computers

    @property
    def order_id(self):
        return self._order_id

    @property
    def computers(self):
        return self._computers

    @computers.setter
    def computers(self, computers):
        self._computers = computers

    def add_computer(self, computer):
        self._computers.append(computer)

    def __str__(self):
        computers_str = ''
        for computer in self._computers:
            computers_str += computer.__str__()

        return f'''
    Order: {self._order_id}
    Computers: {computers_str}
        '''
