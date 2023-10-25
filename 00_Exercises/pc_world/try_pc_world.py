from Computer import Computer
from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse
from Order import Order

keyboard_1 = Keyboard('Logitech', 'USB')
keyboard_2 = Keyboard('Red Dragon', 'USB')
keyboard_3 = Keyboard('Razer', 'USB')

mouse_1 = Mouse('Logitech', 'USB')
mouse_2 = Mouse('Red Dragon', 'USB')
mouse_3 = Mouse('Razer', 'USB')

monitor_1 = Monitor('Acer', 16)
monitor_2 = Monitor('HP', 22)
monitor_3 = Monitor('LG', 24)

computer_1 = Computer('PC_A', monitor_1, keyboard_1, mouse_1)
computer_2 = Computer('PC_B', monitor_2, keyboard_2, mouse_2)
computer_3 = Computer('PC_C', monitor_3, keyboard_3, mouse_3)

computers_1 = [computer_1, computer_2]
computers_2 = [computer_1]

order_1 = Order(computers_1)
print(order_1)

order_2 = Order(computers_2)
order_2.add_computer(computer_2)
order_2.add_computer(computer_3)
print(order_2)
