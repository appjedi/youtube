import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="mydatabase"
)

cursor = conn.cursor()

cursor.callproc("get_user", [123])

for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

cursor.close()
conn.close()