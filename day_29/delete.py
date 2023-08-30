from estd_connection import estd_connections

cursor = estd_connections()

id = input("Enter student ID ")

sql = f"""
DELETE FROM STUDENT WHERE ID ='{id}'
"""

cursor.execute(sql)
print("Student deleted sucessfully")

