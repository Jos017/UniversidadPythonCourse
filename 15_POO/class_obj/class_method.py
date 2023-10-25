# Creating class method
# We use decorator @classmethod to create a class method

class My_class:
    var_class = 'This is a class variable'

    def __init__(self, var_instance):
        self.var_instance = var_instance

    # This is a class method
    # A class method receive an implicit first argument cls
    # This method is bound to the class
    # Can modify the class state
    @classmethod
    def class_method(cls):
        print(cls.var_class)


My_class.class_method()
