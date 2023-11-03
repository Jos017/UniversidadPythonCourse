# Example multiple inheritance
class Simple_list:
    def __init__(self, elements=[]):
        self.__elements = list(elements)

    def add(self, element):
        self.__elements.append(element)

    def __getitem__(self, index):
        return self.__elements[index]

    def sort(self):
        self.__elements.sort()

    def __len__(self):
        return len(self.__elements)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__elements!r})'


class Ordered_list(Simple_list):
    def __init__(self, elements=[]):
        super().__init__(elements)
        # Always order elements when initialize
        self.sort()

    def add(self, element):
        super().add(element)
        # Order the new element
        self.sort()


class Int_list(Simple_list):
    def __init__(self, elements=[]):
        for element in elements:
            self.__validate(element)
        # Once the elements are validated we add the elements
        super().__init__(elements)

    def __validate(self, element):
        # Validate if the element is int type
        if not isinstance(element, int):
            raise ValueError(f'It is not an int type: {element}')

    def add(self, element):
        self.__validate(element)
        # Once validated is added to the list
        super().add(element)


class Int_ordered_list(Int_list, Ordered_list):
    pass


simple_list = Simple_list([15, 4, 6, 8])
print(simple_list)

ordered_list = Ordered_list([2, 7, 2, 4])
print(ordered_list)

int_list = Int_list([3, 1, 2, -14])
int_list.add(3)
print(int_list)

int_ordered_list = Int_ordered_list([3, 4, 12, 5, -13])
int_ordered_list.add(3)
print(int_ordered_list)
# Know parent clases and order
print(Int_ordered_list.__bases__)
# MRO - Method resolution order
print(Int_ordered_list.__mro__)
