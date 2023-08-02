message = "hello World"

#### String Methods ####
# capitalize()


result = message.capitalize()
print(result)

#Title()
result = message.title()
print(result)

#Upper(0
result = message.upper()
print(result)

#Lower()
result = message.lower()
print(result)

# Split()
message = "Hello World"
result = message.split()
print(result) # ['Hello', 'World']

result = message.split('o')
print(result) # ['Hell', ' W', 'rld']

message = "I, am, learning, python"
result = message.split(",")
print(result) # ['I', ' am', ' learning', ' python']

#join()
message = ['I', ' am', ' learning', ' python']
result = " ".join(message)
print(result) # I am learning python
#message.join(" ") # this raises error
result = ", ".join(message)
print(result)



#find()
message = "Hello World"
result = message.find("l")
print(result) #2
result = message.find("Wor")
print(result) #6
result = message.find("wor")
print(result) #-1

#replace()
message = "hello world"
result = message.replace("hello", "HELLO")
print(result)
