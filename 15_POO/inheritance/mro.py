class Class_1:
    def __init__(self):
        print('Class_1.__init__')

    def method(self):
        print('Class_1.method')


class Class_2(Class_1):
    def __init__(self):
        print('Class_2.__init__')

    def method(self):
        print('Class_2.method')


class Class_3(Class_1):
    def __init__(self):
        print('Class_3.__init__')

    def method(self):
        print('Class_3.method')


class Class_4(Class_2, Class_3):
    def method(self):
        print('Class_4.method')


# creating class_4 object
class_4 = Class_4()
print(Class_4.__bases__)
print(Class_4.__mro__)
