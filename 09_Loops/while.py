# The while loop executes a block of code any times while the condition remains true
# while condition:
#     print('Executing while loop')
# else:
#     print('While loop has ended')

##########################
# Is important to modify de condition inside the running code,
# if not the code will run infinite times and the loop will never end
##########################

counter = 0
while counter < 3:
    print(counter)
    counter += 1

print('While loop has ended')
