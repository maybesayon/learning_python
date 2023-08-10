# Membership operation
# Membersip is checked only in dictionary keys but not in values
student = {"name": "Jon", "age": 25, "department": "CS"}
print("name" in student) # True
print("Jon" in student) # False


# Built-in Functionw
print(len(student)) # 3

result = sorted(student)
print(student)
print(str(student))