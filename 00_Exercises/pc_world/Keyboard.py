from Input_device import Input_device


class Keyboard(Input_device):
    keyboard_counter = 0

    def __init__(self, brand, input_type):
        super().__init__(brand, input_type)
        Keyboard.keyboard_counter += 1
        self._keyboard_id = Keyboard.keyboard_counter

    @property
    def keyboard_id(self):
        return self._keyboard_id

    def __str__(self):
        return f'Id: {self._keyboard_id}, Brand: {self._brand}, Input_type: {self._input_type}'


if __name__ == '__main__':
    keyboard_1 = Keyboard('Red Dragon', 'USB')
    print(keyboard_1)
