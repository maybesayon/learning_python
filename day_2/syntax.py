#Python syntax

#Backslash can be used to take the statement to the next line


message = " Hello I learning Python"

import json,\
       csv

# We can use ';' to write multiple statemens in the same line\
name = "John"; age = 25

# Indentation in python is very important.
# An indentation is equivalent to 4 spaces
# We do not use curly bracket in python to determine a block of code. Insted, we use indentation
# Following is an example of a c code
# if (a==2)
# print("hello world")
# here the block of if condition is determined by indentatio
# For example
a=2
if a == 2:
       print("hello world")
       b=2
       if b == 2:
              print ("python")
              print("Is")
              print("Awesome")
       print("Another message")
print("sth")

# Docstring Example
message = """Python is high level language
it is easy to use"""

print(message)

message = " I'm learning python"
msg ='he said, "hello!"'
# Escape sequence
message = 'I\'m learning python'
