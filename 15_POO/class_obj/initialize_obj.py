class Parent:
    # The __init__ method is called when an instance of the class is created
    def __init__(self):
        print('Parent initializer')

    def method(self):
        print('Parent method')


class Child(Parent):
    # If no __init__ method is defined in a child class, the parent __init__ method is called
    def __init__(self):
        print('Child initializer')
        # calling the parent __init__ from child __init__
        super().__init__()

    # If no method is defined is used the parent method
    # If defined is used the children method
    def method(self):
        print('Child method')
        super().method()


print('Parent'.center(50, '-'))
parent_1 = Parent()
parent_1.method()

print('\n')

print('Child'.center(50, '-'))
child_1 = Child()
child_1.method()
