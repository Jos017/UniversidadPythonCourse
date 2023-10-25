# Creating static method
# We use decorator @staticmethod to create an static method

class My_class:
    var_class = 'This is a class variable'

    def __init__(self, var_instance):
        self.var_instance = var_instance

    # This is an static method
    # An static method does not receive an implicit first argument self
    # This method is bound to the class
    # Cannot modify the state of an object
    # Cannot modify the state of a class
    @staticmethod
    def static_method():
        print(My_class.var_class)
