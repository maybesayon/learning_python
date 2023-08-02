# We can concatenate strings


n1 = "Hello"
n2 = "World"
message = n1 + n2
print(message)

# Repetation operation

message = "Hello World"
print(message * 3) # Hello WorldHello WorldHello World]
#Membership Operation
message = "Hello World"
print("H" in message) #True
print("W" not in message) #False
print("k" in message) #False


####Built-in functions that can be used in string####

message = "Hello World"
print(len(message)) # 11
print(bool(message)) # True
print(type(message)) # <class 'str'>


x = slice(2, 6)
print(message[x]) # llo
