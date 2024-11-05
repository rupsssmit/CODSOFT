contacts = []

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone_number": phone_number, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone_number']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone_number']]
    if found_contacts:
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone_number']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of the contact to update: ")
    found_contact = None
    for contact in contacts:
        if contact['name'] == name:
            found_contact = contact
            break
    if found_contact:
        print("Enter new details:")
        new_phone_number = input("New phone number: ")
        new_email = input("New email: ")
        new_address = input("New address: ")
        found_contact['phone_number'] = new_phone_number
        found_contact['email'] = new_email
        found_contact['address'] = new_address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")