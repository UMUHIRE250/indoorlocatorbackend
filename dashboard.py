# Dictionary to store admin credentials
admin_credentials = {
    "admin": "password123"
}

# Dictionary to store information added by admin
information = {}

def admin_login():
    while True:
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username in admin_credentials and admin_credentials[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")

def add_information():
    title = input("Enter title for the information: ")
    details = input("Enter details: ")
    information[title] = details
    print("Information added successfully!")

def display_information():
    print("\nInformation added by admin:")
    for title, details in information.items():
        print(f"Title: {title}")
        print(f"Details: {details}")
        print()

if __name__ == "__main__":
    logged_in = admin_login()
    if logged_in:
        while True:
            choice = input("\nWhat would you like to do? (add/display/exit): ").lower()
            if choice == "add":
                add_information()
            elif choice == "display":
                display_information()
            elif choice == "exit":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Exiting...")
