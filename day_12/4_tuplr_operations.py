# Concatenation(+)
a = (1, 2, 3)
b = (4, 5, 6)
result = a + b
print(result)

# Repetation / Broadcast (*)
a = (1, 2)
result = a * 3
print(result) # (1, 2, 1, 2, 1, 2)

# Membership operation ("in" or "not in")
print(2 in (1, 2, 3)) #True
print(3 not in (1, 2, 3)) #False

# Iteration
vowels = ("a", "e", "i", "o", "u")
for each in vowels:
    print(each) # a e i o u

data = [i ** 2 for i in range(10)] # List comprehension
print(data)
data = (i ** 2 for i in range(10)) # Generator comprehension
print(data)
print(list(data))