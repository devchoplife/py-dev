"""To make sure a string will display as expected, we can format the result with 
the format() method"""

# String format()
"""The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come 
from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run 
the values through the format() method"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

"""You can add parameters inside the curly brackets to specify how to convert the value"""
txt = "The price is {:.2f} dollars"

# Multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""Also, if you want to refer to the same value more than once, use the index number"""
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
