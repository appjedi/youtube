import mysql.connector

conn = None
cursor = None

try:
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

except mysql.connector.Error as e:
    print("MySQL error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()