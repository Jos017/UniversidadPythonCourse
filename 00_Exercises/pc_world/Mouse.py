from Input_device import Input_device


class Mouse(Input_device):
    mouse_counter = 0

    def __init__(self, brand, input_type):
        super().__init__(brand, input_type)
        Mouse.mouse_counter += 1
        self._mouse_id = Mouse.mouse_counter

    @property
    def mouse_id(self):
        return self._mouse_id

    def __str__(self):
        return f'Id: {self._mouse_id}, Brand: {self._brand}, Input_type: {self._input_type}'


if __name__ == '__main__':
    mouse_1 = Mouse('Logitech', 'USB')
    print(mouse_1)
