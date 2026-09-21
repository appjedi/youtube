import mysql.connector

def get_conn():
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jedi2023",
            database="appjedin_student_temp"
    )
    return conn

def get_customer(user_id):

    conn =get_conn()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM customer WHERE id = %s",
            (user_id,)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()
        
def list_customers():
    conn =get_conn()

    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM customer"           
        )
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    finally:
        cursor.close()
        conn.close()

#cid = input("Customer ID:")
list_customers()
