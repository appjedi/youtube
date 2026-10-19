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
            print(f"ID: {row['ID']}, Last Name: {row['lastName']}, First Name: {row['firstName']}, Email: {row['email']}, Phone: {row['phone']}, Address: {row['address1']}, Zip: {row['zip']}")
    finally:
        cursor.close()
        conn.close()

def add_customer():
    conn =get_conn()
    cursor = conn.cursor(dictionary=True)

    try:
        lastname=input("Last Name:")
        firstname=input("First Name:")
        email=input("Email:")
        phone=input("Phone:")
        address=input("Address:")

        zip=input("Zip:")
        dob=input("Birth Date (YYYY-MM-DD):")

        cursor.callproc("usp_customer_save", [0,firstname,lastname,  email, address,'',phone,dob, zip])
        for result in cursor.stored_results():
            # 3. Fetch one row
            row = result.fetchone()
            break
        conn.commit()
        print("Customer added successfully.")
    finally:
        cursor.close()
        conn.close()

def update_customer(user_id):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    try:
        customer = get_customer(user_id)
        if not customer:
            print("Customer not found.")
            return

        print("Leave fields blank to keep current values.")
        lastname = input(f"Last Name [{customer['lastName']}]: ") or customer['lastName']
        firstname = input(f"First Name [{customer['firstName']}]: ") or customer['firstName']
        email = input(f"Email [{customer['email']}]: ") or customer['email']
        phone = input(f"Phone [{customer['phone']}]: ") or customer['phone']
        address = input(f"Address [{customer['address1']}]: ") or customer['address1']
        zip_code = input(f"Zip [{customer['zip']}]: ") or customer['zip']
        dob = input(f"Birth Date [{customer['birthDate']}]: ") or customer['birthDate']
        cursor.callproc("usp_customer_save", [user_id,firstname,lastname,  email, address,'',phone,dob, zip_code])

        for result in cursor.stored_results():
            # 3. Fetch one row
            row = result.fetchone()
            break
        
        conn.commit()
        print("Customer updated successfully.",row)
        return # Return True if update is successful, False otherwise
    finally:
        cursor.close()
        conn.close()

def delete_customer(user_id):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    try:
        customer = get_customer(user_id)
        if not customer:
            print("Customer not found.")
            return

        confirm = input(f"Are you sure you want to delete customer {customer['firstName']} {customer['lastName']}? (y/n): ")
        if confirm.lower() == 'y':
            cursor.execute(
                "DELETE FROM customer WHERE id=%s",
                (user_id,)
            )
            conn.commit()
            print("Customer deleted successfully.")
        else:
            print("Deletion cancelled.")
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
    print("3. Update Customer")
    print("4. Delete Customer")

    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            list_customers()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            list_customers()
            user_id = input("Enter Customer ID to update: ")

            update_customer(user_id)
        elif choice == "4":
            list_customers()
            user_id = input("Enter Customer ID to delete: ")
            delete_customer(user_id)

        elif choice == "5":
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

