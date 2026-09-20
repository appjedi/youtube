import mysql.connector

def get_conn():
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Data2026",
            database="appjedin_student_temp"
        )
    return conn

def auth():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        username=input("Username:")
        password=input("Password:")
        cursor.callproc("usp_user_auth", [username,password])

        for result in cursor.stored_results():
            # 3. Fetch one row
            row = result.fetchone()
            break
        print(row)
    finally:
        cursor.close()
        conn.close()

auth()
