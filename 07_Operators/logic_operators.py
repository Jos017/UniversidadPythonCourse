# Logic operators allows us to compare boolean values
# The Logic operators return a Bolean

# AND operator (and)
print(f'The AND operator returns {
      True and True} if both values are True')  # ==> True
print(f'The AND operator returns {
      True and False} if one value is False')  # ==> False
print(f'The AND operator returns {
      False and False} if both values are False')  # ==> False

# OR operator (or)
print(f'The OR operator returns {
      True or True} if both values are True')  # ==> True
print(f'The OR operator returns {
      True or False} if one value is False')  # ==> True
print(f'The OR operator returns {
      False or False} if both values are False')  # ==> False

# NOT operator (not)
print(f'The NOT operator returns {not True} if the value is True')  # ==> False
print(f'The NOT operator returns {
      not False} if the value is False')  # ==> True

# AND operator simplified in ranges
age = 20
print(f'"20 <= age < 30" ({20 <= age < 30}) is equal to "age >= 20 and age < 30" ({
      age >= 20 and age < 30})')
