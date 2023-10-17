# Define variables
# No need data type
myVariable = "Hello from Python"
print("-----Variables intro-----")
print(myVariable)
print(myVariable)

# Change its value
print("-----Changing value-----")

myVariable = 10
print(myVariable)
print(myVariable)

myVariable = True
print(myVariable)
print(myVariable)

# Use variables to declare a new variable
x = 10
y = 2
z = x + y
print("-----Using variables to declare new one-----")
print(x)
print(y)
print(z)

# Variables are assigned to a memory direction (memory reference)
# Use id(variable) to obtain the memory direction
print("-----Memory direction in variables-----")
print("Id:", id(x))
print("Id:", id(y))
print("Id:", id(z))
