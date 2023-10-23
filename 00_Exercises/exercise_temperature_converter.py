# Exercise: Temperature Converter
# Create two functions to convert temperature
# from Celsius to Fahrenheit and viceversa
def convert_from_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convert_from_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius_input = float(
    input('Write Celsius Degrees to convert to Fahrenheit: '))
fahrenheit_input = float(
    input('Write Fahrenheit to convert to Celsius Degrees: '))

celsius_conversion = convert_from_fahrenheit_to_celsius(fahrenheit_input)
fahrenheit_conversion = convert_from_celsius_to_fahrenheit(celsius_input)

print(f'{celsius_input} Celsius to Fahrenheit is: {fahrenheit_conversion: 0.2f}')
print(f'{fahrenheit_input} Fahrenheit to Celsius is: {celsius_conversion: 0.2f}')
