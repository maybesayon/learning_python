from estd_connection import estd_connections

cursor = estd_connections()

# cursor.execute("DROP TABLE STUDENT")


sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT
)
"""
cursor.execute(sql)
print("Table Created successfully!!")
