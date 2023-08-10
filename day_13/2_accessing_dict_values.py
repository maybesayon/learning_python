vowels = ["a", "e", "i", "o", "u"]
print(vowels[2])


# Accessing dictionary is similar to that of accessing list elements
student = {"name": "Jon", "age": 25, "department": "CS"}
dept = student["department"]
print(dept) #CS


name = student["name"]
print(name) # Jon

#print(student["dob"]) # This raises Key error

# Accessing values using get() method
department = student.get("department")
print(department) # CS
dob = student.get("dob")
print(dob) #None


# Adding key value pair in a dictionary
vowels = ["a", "e", "i", "o"]
vowels.append("u")
vowels.insert(2, "A")



student = {"name": "Jon", "age": 25, "department": "CS"}
student["dob"] = "22 july"
print(student) # {'name': 'Jon', 'age': 25, 'department': 'CS', 'dob': '22 july'}


student.update(roll_no=12)
print(student)


student["name"] = "Jane"
print(student) #{'name': 'Jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}


# REmoving a key-value pair from a dictionary
student = {'name': 'Jane', 'age': 25, 'department': 'CS', 'dob': '22 july', 'roll_no': 12}
result = student.pop("dob")
print(student) # {'name': 'Jane', 'age': 25, 'department': 'CS', 'roll_no': 12}

#result = student.pop("address")
#print(result)

result = student.popitem()
print(result) # ("roll_no", 12)
print(student)#{'name': 'Jane', 'age': 25, 'department': 'CS',}