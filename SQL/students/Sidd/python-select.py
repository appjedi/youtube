import mysql.connector


def get_user(user_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="mydatabase"
    )

    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM users WHERE id = %s",
            (user_id,)
        )

        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()