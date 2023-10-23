class Arithmetic:
    def __init__(self, number_a, number_b):
        self.number_a = number_a
        self.number_b = number_b

    def add(self):
        return self.number_a + self.number_b

    def subtract(self):
        return self.number_a - self.number_b

    def multiply(self):
        return self.number_a * self.number_b

    def divide(self):
        if self.number_b == 0:
            return 'Error: division by 0'
        return self.number_a / self.number_b


a = float(input('Introduce number A: '))
b = float(input('Introduce number B: '))
arithmetic = Arithmetic(a, b)
print(f'Addition: {a} + {b} = {arithmetic.add()}')
print(f'Subtraction: {a} - {b} = {arithmetic.subtract()}')
print(f'Multiplication: {a} * {b} = {arithmetic.multiply()}')
print(f'Division: {a} / {b} = {arithmetic.divide()}')
