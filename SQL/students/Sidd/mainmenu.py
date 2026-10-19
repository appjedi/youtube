import importlib

_customer_module = importlib.import_module("python-select")
get_customer = _customer_module.get_customer
list_customers = _customer_module.list_customers
add_customer = _customer_module.add_customer
auth = _customer_module.auth
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

