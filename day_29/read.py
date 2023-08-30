from estd_connection import estd_connections

cursor = estd_connections()

id = input("Enter student ID ")

sql =f"""
SELECT * FROM STUDENT WHERE ID = '{id}'
"""

cursor.execute(sql)
result = cursor.fetchone()
print(result)