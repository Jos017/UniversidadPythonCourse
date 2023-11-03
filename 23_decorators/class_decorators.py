# Class decorators
# Transform our class
import inspect


def decorator_repr(cls):
    print('Decorator is executed')
    print(f'Receiving class object: {cls.__name__}')

    # Review the class attributes with vars method
    attributes = vars(cls)
    # for name, attribute in attributes.items():
    #     print(name, attribute)

    # Review if the method __init__ has been overwritten
    if '__init__' not in attributes:
        raise TypeError(f'{cls.__name__} has not overwritten __init__')

    init_sign = inspect.signature(cls.__init__)
    print(f'Sign of __init__: {init_sign}')

    # Retrieve parameters except self
    init_params = list(init_sign.parameters)[1:]
    print(f'Init params: {init_params}')

    # Review if the init params has a property method associated
    for param in init_params:
        is_property_method = isinstance(attributes.get(param), property)
        if not is_property_method:
            raise TypeError('There is no method property with name: "{param}"')

    # Create method repr dynamic
    def repr_method(self):
        # Obtain the name of the class
        class_name = self.__class__.__name__
        # Obtain property names and values
        # Generator expression, create name_atr=value_atr
        key_values_list = [
            f'{name}={getattr(self, name)!r}' for name in init_params
        ]
        # Create the string from the list of arguments
        arguments = ', '.join(key_values_list)

        # Create the method __repr__ return
        return f'{class_name}({arguments})'

    # Add the method repr dynamic
    setattr(cls, '__repr__', repr_method)

    return cls


@decorator_repr
class Person:
    def __init__(self, name, last_name):
        print('Execute Initializer')
        self.__name = name
        self.__last_name = last_name

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    # def __repr__(self):
    #     return f'{self.__class__.name}({self.__name} {self.__last_name})'


person_1 = Person('Juan', 'Perez')
person_2 = Person('Karla', 'Gomez')
print(person_1)
print(person_2)
