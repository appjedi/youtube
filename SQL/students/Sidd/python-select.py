import mysql.connector
# pip3 install mysql-connector-python
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

def add_customer():
    conn =get_conn()
    cursor = conn.cursor(dictionary=True)

    try:
        name=input("Name:")
        email=input("Email:")
        phone=input("Phone:")
        cursor.execute(
            "INSERT INTO customer (name,email,phone) VALUES (%s,%s,%s)",
            (name,email,phone)
        )
        conn.commit()
        print("Customer added successfully.")
    finally:
        cursor.close()
        conn.close()

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
        #print(row[0])
        return row[0] ==1 # Return True if authentication is successful, False otherwise
    finally:
        cursor.close()
        conn.close()
def show_menu():
    print("\n=== Main Menu ===")
    print("1. Show Customers")
    print("2. Add Customer")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            list_customers()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
# Clean up by closing the connection


#main()
while not auth():
    print("Invalid credentials. Please try again.")

main()
#cid = input("Customer ID:")

