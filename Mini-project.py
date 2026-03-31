def add_contact(contacts):
    name = input("Enter contact name: ").title().strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")


def search_contact(contacts):
    name = input("Enter contact name to search: ").title().strip()
    contact = contacts.get(name)

    if contact:
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")


def main():
    contacts = {}

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
