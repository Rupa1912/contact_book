import json

CONTACTS_FILE="contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE,"r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
def save_contacts(contacts):
    with open(CONTACTS_FILE,"w") as file:
        json.dump(contacts,file,indent=4)

def add_contact():
    name=input("Enter the contact's name: ")
    phone=input("Enter the contact's phone number: ")
    email=input("Enter the contact's email address: ")

    contact={
        "name":name,
        "phone":phone,
        "email":email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added succssfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(f"\nContact {index+1}:")
            print("Name:",contact["name"])
            print("Phone:",contact["phone"])
            print("Email:", contact["email"])

def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    results = []
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            results.append(contact)
    
    if results:
        print("Search results:")
        for contact in results:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
    else:
        print("No matching contacts found.")
def delete_contact():
    index = int(input("Enter the index of the contact to delete: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Invalid contact index.")
    else:
        deleted_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Deleted contact: {deleted_contact['name']}")

def menu():
    print("\n*** Contact Book Menu ***")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

contacts = load_contacts()

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")