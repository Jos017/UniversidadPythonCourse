from Person import Person


class Employee(Person):
    def __init__(self, name, age, payment):
        super().__init__(name, age)
        self.payment = payment
