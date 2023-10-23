# To receive variable arguments we use a * before the param name
# The param when received is transformed into a tuple

def listNames(*names):
    # In this case names is a tuple
    for name in names:
        print(name)


listNames('Juan', 'Karla', 'Maria', 'Ernesto')
