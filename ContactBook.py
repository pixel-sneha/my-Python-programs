#Contact book application
def display_menu(): 
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input()
    email = input()
    address = input()

    contact_book[name] = {
        "phone" : phone,
        "email" : email,
        "address" : address
    }
    print("Contact added successfully!")

def view_contact(contact_book):
    contact = input()
    if contact in contact_book:
        print(f"Name: {contact}")
        print(f"Phone: {contact_book[contact]['phone']}")
        print(f"Email: {contact_book[contact]['email']}")
        print(f"Address: {contact_book[contact]['address']}")
    else:
        print("Contact not found!")
        return

