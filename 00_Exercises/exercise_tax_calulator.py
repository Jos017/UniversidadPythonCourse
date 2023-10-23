# Exercise: Tax Calculator
# Create a function to calculate the total payment including taxes
# total_payment = payment + payment * (tax / 100)
paymentInputValue = float(input('Introduce the payment amount: '))
taxInputValue = float(input('Introduce the tax percent: '))


def calculate_payment_with_tax(payment, tax):
    total_payment = payment + payment * (tax / 100)
    return total_payment


payment_with_tax = calculate_payment_with_tax(paymentInputValue, taxInputValue)
print('The payment with taxes is:', payment_with_tax)
