phone_book = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print("Contact added successfully.")

def look_up_contact():
    name = input("Enter contact name: ")
    if name in phone_book:
        print(f"{name}'s phone number is {phone_book[name]}.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_menu():
    print("Phone Book:")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Delete contact")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            look_up_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()