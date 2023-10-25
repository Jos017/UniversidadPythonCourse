from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse


class Computer:
    computer_counter = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computer_counter += 1
        self._computer_id = Computer.computer_counter
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    @property
    def computer_id(self):
        return self._computer_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def keyboard(self):
        return self._keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self._keyboard = keyboard

    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, mouse):
        self._mouse = mouse

    def __str__(self):
        return f'''
        {self._name}: {self._computer_id}
        Monitor: {self._monitor}
        Keyboard: {self._keyboard}
        Mouse: {self._mouse}
        '''


if __name__ == '__main__':
    keyboard_1 = Keyboard('Red Dragon', 'USB')
    keyboard_2 = Keyboard('Genius', 'USB')
    monitor_1 = Monitor('HP', 27)
    monitor_2 = Monitor('Dell', 27)
    mouse_1 = Mouse('Logitech', 'USB')
    mouse_2 = Mouse('Razer', 'USB')
    computer_1 = Computer('PC_1', monitor_1, keyboard_1, mouse_1)
    computer_2 = Computer('PC_2', monitor_2, keyboard_2, mouse_2)
    print(computer_1)
    print(computer_2)
