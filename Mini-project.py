def add_contact(contacts):
    name = input("Enter contact name: ").title().strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()

    # Check 
    existing = [c for c in contacts if c["name"] == name]
    
    if existing:
        print(f"\nWarning: {len(existing)} contact(s) with name '{name}' already exist!")
        for contact in existing:
            print(f"\nExisting contact:")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
        
        overwrite = input("\nDo you want to replace the first one? (yes/no): ").lower().strip()
        if overwrite == "yes":
            # Find and replace the first matching contact
            for i, contact in enumerate(contacts):
                if contact["name"] == name:
                    contacts[i] = {
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "address": address
                    }
                    print(f"Contact '{name}' replaced successfully.")
                    return
        else:
            print("Adding as a new entry...")
    
    # Add contact 
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully.")


def search_contact(contacts):
    name = input("Enter contact name to search: ").title().strip()
    
    found_contacts = [c for c in contacts if c["name"] == name]
    
    if found_contacts:
        print(f"\nFound {len(found_contacts)} contact(s) with name '{name}':")
        for contact in found_contacts:
            print(f"\n--- Contact ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print(f"\nContact List (Total: {len(contacts)}):")
    for contact in contacts:
        print(f"\n--- Contact ---")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")


def delete_contact(contacts):
    if not contacts:
        print("No contacts available to delete.")
        return
    
    # Show all contacts first
    print("\nAll contacts:")
    count = 1
    for contact in contacts:
        print(f"{count}. {contact['name']} - {contact['phone']}")
        count += 1
    
    try:
        entry_num = int(input("\nEnter the entry number to delete: ").strip())
        
        if 1 <= entry_num <= len(contacts):
            contact = contacts[entry_num - 1]
            print(f"\nContact to be deleted:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            confirm = input("\nAre you sure you want to delete this contact? (yes/no): ").lower().strip()
            if confirm == "yes":
                deleted = contacts.pop(entry_num - 1)
                print(f"Contact '{deleted['name']}' deleted successfully.")
            else:
                print("Contact deletion cancelled.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    contacts = []

    while True:
        print("\n" + "="*40)
        print("Contact Management System")
        print("="*40)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()
    
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()