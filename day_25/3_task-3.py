student = {"name": "Jon", "age": 25, "ID": 22011, "Department": "Management"}
try:
    key = input("Enter the key you want to access ")
    data = student[key]
    print(f"The {key} of the student is {data}")
except:
    print("Please enter a valid key")