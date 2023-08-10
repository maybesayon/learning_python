# Dictionary are the mutable data types in python
# They have the element in key-value pair format
# It is also the sequential datatype like list and tuple

# Creating an empty dictionary
a = dict() # Empty dictionary
a = {} # This is also an empty dictionary


# Creating an empty dictionary
student = {"name": "Jon", "age": 25, "department" : "CS"}
print(student) # {'name': 'Jon', 'age': 25, 'department': 'CS'}
student = dict(name="Jon", age=25, department="CS")
print(student)

student = dict({"name": "Jon", "age": 25, "department" : "CS"})
print(student)


student = dict([("name", "Jon"), ("age", 25), ("department", "CS")])
print(student)

# Creating a list of dictionsries
student = [
    {"name": "Jon", "age": 25, "department" : "CS"},
    {"name": "James", "age": 54, "department" : "IT"},
    {"name": "Jonah", "age": 28, "department" : "HR"}

]
print(student)