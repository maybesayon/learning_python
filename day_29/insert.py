from estd_connection import estd_connections

cursor = estd_connections()

id = input("Enter Student ID ")
name = input("Student name ")
age = int(input("Enter student's age "))

sql = f"""
INSERT INTO STUDENT (ID, Name, AGE) VALUES ('{id}', '{name}', {age})
"""

cursor.execute(sql)
print("Student added successfully")
