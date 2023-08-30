# If we want to connect database from a program(Python, javascript) than we need a database connector
# Database connectors connect your program with a database mysqlclient, psycopg2 etc. which are the database connectors


def estd_connections():
    import psycopg2
    conn = psycopg2.connect(
        database="studentdb",
        user="postgres",
        password="Sayoncoldplay10",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully!!")
    cursor = conn.cursor()
    return cursor

if __name__ == "__main__":
    estd_connections()
