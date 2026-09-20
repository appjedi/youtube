import mysql.connector


def get_customer(user_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$Data2026",
        database="appjedin_student_temp"
    )

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
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$Data2026",
        database="appjedin_student_temp"
    )

    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM customer"           
        )

        for row in cursor.fetchall():
            print(row)
    finally:
        cursor.close()
        conn.close()

#cid = input("Customer ID:")
list_customers()