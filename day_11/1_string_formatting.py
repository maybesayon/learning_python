# We can format using f-strings
name = input("Enter your name")
age = int(input("Enter your age"))
language = input("Enter the language you're learning")
message = f"Hello I an {name}. I am learning {language}"
print(message)

message = "I am %s and I am %d years old" % (name, age)
print(message)

message = f"I am {name} and i am learning {language}"
print(message)


message = "I am {} and I am {} years old.".format(name, age)
print(message)

message = "I have {1}, {0} and {2} in my bag."
formatted_message = message.format('book', 'pen', 'copy')
print(formatted_message)

#message = "I have {1}, {0} and {2} in my bag.".format('book', 'pen') # It raises error

message = "I have {} and {} in my bag." .format('book', 'pen', 'pencil', 'copy')
print(message)

