# Condition in python or any other programming language is used to make decisions
# We can make conditions in three different ways
# 1. Simple If
# 2. if......else block
# 3. if.......elif ladder

# Note : Nested if conditions are also possible


# 1. Simple if
age = 25
if age > 19:
    print("The person is not a teenager")

# If conditions always takes truthy or falsy statement. IF the statement id truthy the block inside is executes
# If false, the block inside if is not executed

if age:
    print(f"The person's age is {age}")

vowels = []
if vowels:
    print(vowels)


a = 2
if a:
    print(f"The number is {a}")

# 2. If else
age = 18
if age > 19:
    print("The person is not a teenager")
else:
    print("The person is a teenager")

a = 4
if a:
    print(f"The number is {a}")
else:
    print("The number is not provided")

vowels = []
if vowels:
    print(vowels)
else:
    print("The list is empty")

data = [1, 2, 3, 4, 5]
if 2 in data:
    print("2 is in the list")
else:
    print("2 is not in the list")

num = 5
if not num:
    print("The number is not given")
else:
    print(f"The number is {num}")

# If......elif ladder
exam_percent = int(input("Enter exam percentage "))
if exam_percent >= 80:
    print("The student got distinction")
elif exam_percent >= 65:
    print("The student got first division")
elif exam_percent >= 55:
    print("The student got secons division")
elif exam_percent >= 40:
    print("The student got third division")
else:
    print("The student failed!!")

# Ternary if
a = 5
print("The number is  greater than 10") if a > 10 else print("The number is less than 10") # This is ternary if condition




# Nested if ==> nested if is simply if condition inside a if condition
a = 20
if a > 10:
    if a > 15:
        print("The number is greater than 15")
    else:
        print("The number is just greater than 10")
else:
    print("The number is less than 10")
