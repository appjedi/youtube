import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$Data2026",
        database="appjedin_student_temp"
    )

cursor = conn.cursor()
username=input("Username:")
password=input("Password:")
cursor.callproc("usp_user_auth", [username,password])

for result in cursor.stored_results():
    # 3. Fetch one row
    row = result.fetchone()
    break
print(row)
cursor.close()
conn.close()