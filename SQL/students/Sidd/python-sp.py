import mysql.connector
#pip install tabulate
def get_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jedi2023",
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
def list_query(query):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    finally:    
        cursor.close()
        conn.close()
#auth()

query="SELECT * FROM view_window_ex1"

list_query(query)
