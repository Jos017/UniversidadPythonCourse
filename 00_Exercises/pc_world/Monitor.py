class Monitor:
    monitor_counter = 0

    def __init__(self, brand, size):
        Monitor.monitor_counter += 1
        self._monitor_id = Monitor.monitor_counter
        self._brand = brand
        self._size = size

    @property
    def monitor_id(self):
        return self._monitor_id

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __str__(self):
        return f'Id: {self._monitor_id}, Brand: {self._brand}, Size: {self._size}'


if __name__ == '__main__':
    monitor_1 = Monitor('HP', 15)
    print(monitor_1)
